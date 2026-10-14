"""Download de uma lista de títulos já triada pelo usuário (lote de triagem).

Complementa o /literature-review para o caso em que a seleção não veio de uma
busca nossa, mas de uma triagem feita pelo usuário (ex.: com o prompt do
screening-protocol.md em outro assistente). A lista de títulos É a aprovação
item a item (G4); o que muda é que cada título precisa ser localizado numa API
antes de qualquer coisa (G2): título sem correspondência verificável não é
baixado nem resumido — vira "não localizado".

Etapas, todas retomáveis (o estado fica em .title-list-<lote>.json):

  1. resolve  — localiza cada título no OpenAlex; aceita só correspondência com
                similaridade >= crossref.title_match_threshold.
  2. download — tenta o PDF open access dos localizados, no máximo
                max_papers_per_run por execução (G5). Rode de novo para seguir.
  3. report   — grava deliverables/batches/<lote>-baixados.md e
                <lote>-nao-baixados.md (lista + abstract de cada item) e registra
                os não baixados em pending.md.

Uso:
  uv run python -m scripts.title_list fetch <area>/<proj>/<tema> \\
      --titles <arquivo.txt> --batch lote-01
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import asdict
from datetime import date
from pathlib import Path
from urllib.parse import quote_plus

import httpx

from scripts import candidates as cand
from scripts import naming, pdf_extract
from scripts.config import load_config
from scripts.crossref import CrossrefClient, title_similarity
from scripts.locations import Location, ensure_location, parse_location
from scripts.oa_resolver import OpenAccessResolver
from scripts.openalex import USER_AGENT_TEMPLATE, Candidate, OpenAlexClient

# Prefixo de venue no estilo DBLP ("HICSS - Título", "WWW - Título"): não faz
# parte do título e derruba a similaridade.
_VENUE_PREFIX_RE = re.compile(r"^[A-Z][A-Za-z0-9]{1,9}\s+-\s+")

# Status de cada item ao longo do pipeline.
UNRESOLVED = "unresolved"
NOT_FOUND = "not_found"
MATCHED = "matched"  # localizado, download ainda não tentado
DOWNLOADED = "downloaded"
NOT_DOWNLOADED = "not_downloaded"
LANGUAGE_DISCARDED = "language_discarded"
DUPLICATE = "duplicate"

STATUS_LABEL = {
    DOWNLOADED: "Baixado",
    NOT_DOWNLOADED: "Não baixado",
    NOT_FOUND: "Não localizado",
    LANGUAGE_DISCARDED: "Descartado (idioma)",
    DUPLICATE: "Duplicado na lista",
    MATCHED: "Localizado (download não tentado)",
    UNRESOLVED: "Não processado",
}


def read_titles(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]


def clean_title(raw: str) -> str:
    return _VENUE_PREFIX_RE.sub("", raw.strip()).strip()


def search_query(title: str) -> str:
    """Título pronto para a API: '?' e '*' são curingas no OpenAlex (HTTP 400)."""
    return re.sub(r"\s+", " ", re.sub(r"[?*]", " ", clean_title(title))).strip()


def pick_match(
    query_title: str, results: list[Candidate], threshold: float
) -> tuple[Candidate | None, float]:
    """Escolhe o registro que corresponde ao título e funde as versões dele.

    O OpenAlex costuma ter o mesmo trabalho duas vezes (preprint e versão
    publicada). Ficamos com a versão publicada como registro principal e
    somamos as URLs de PDF das demais: o preprint aberto é o mesmo paper.
    """
    scored = [(title_similarity(query_title, c.title), c) for c in results]
    matches = [(s, c) for s, c in scored if s >= threshold]
    if not matches:
        return None, max((s for s, _ in scored), default=0.0)

    matches.sort(
        key=lambda sc: (
            round(sc[0], 2),
            bool(sc[1].doi),
            sc[1].work_type == "article",
            sc[1].cited_by_count,
        ),
        reverse=True,
    )
    best_score, best = matches[0]
    for _, other in matches[1:]:
        for url in [other.pdf_url, *other.alternate_pdf_urls]:
            if url and url != best.pdf_url and url not in best.alternate_pdf_urls:
                best.alternate_pdf_urls.append(url)
        if not best.abstract and other.abstract:
            best.abstract = other.abstract
    return best, best_score


def resolve_title(
    client: OpenAlexClient, crossref: CrossrefClient, title: str, threshold: float
):
    """Título -> (candidato, similaridade).

    Ordem: busca no título do OpenAlex, busca livre do OpenAlex e, por fim,
    Crossref por título -> DOI -> registro do OpenAlex (há trabalhos que o
    índice de título do OpenAlex não acha, mas que ele tem pelo DOI).
    """
    query = search_query(title)
    reference = clean_title(title)
    # Vírgula e pipe são separadores na sintaxe de filtro do OpenAlex.
    filter_value = re.sub(r"[,|]", " ", query)
    payload = client._get(
        f"{client.config.openalex.base_url}/works",
        {"filter": f"title.search:{filter_value}", "per-page": "10"},
    )
    results = [
        c for c in (client._candidate_from_work(w) for w in (payload or {}).get("results", []))
        if c
    ]
    match, score = pick_match(reference, results, threshold)
    if match is None:
        results += client.search(query, per_page=10)
        match, score = pick_match(reference, results, threshold)
    if match is None:
        work = crossref.search_by_title(query)
        by_doi = client.fetch_by_doi(work.doi) if work else None
        if by_doi:
            match, doi_score = pick_match(reference, [by_doi], threshold)
            score = max(score, doi_score)
    return match, score


def semantic_scholar(http: httpx.Client, doi: str, fields: str) -> dict:
    """Registro do Semantic Scholar para o DOI ({} quando indisponível)."""
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}"
    for attempt in range(3):
        try:
            response = http.get(url, params={"fields": fields})
        except httpx.HTTPError:
            return {}
        if response.status_code == 429:
            # Pool público compartilhado: o rate limit é agressivo.
            time.sleep(3 * (attempt + 1))
            continue
        if response.status_code != 200:
            return {}
        try:
            return response.json() or {}
        except ValueError:
            return {}
    return {}


def semantic_scholar_pdf(http: httpx.Client, doi: str) -> str | None:
    """URL de PDF open access declarada pelo Semantic Scholar para o DOI."""
    return (semantic_scholar(http, doi, "openAccessPdf").get("openAccessPdf") or {}).get("url")


def backfill_abstracts(store: StatusStore, config) -> None:
    """Terceira fonte de abstract: Semantic Scholar, para quem ainda não tem."""
    todo = [
        i for i in store.items
        if i.get("candidate") and not i["candidate"].get("abstract")
        and i["candidate"].get("doi") and not i.get("abstract_tried_s2")
    ]
    if not todo:
        return
    headers = {"User-Agent": USER_AGENT_TEMPLATE.format(email=config.polite_pool_email)}
    with httpx.Client(timeout=30, headers=headers) as s2:
        for item in todo:
            abstract = semantic_scholar(s2, item["candidate"]["doi"], "abstract").get("abstract")
            item["abstract_tried_s2"] = True
            if abstract:
                item["candidate"]["abstract"] = abstract.strip()
                item["abstract_source"] = "Semantic Scholar"
            store.save()
            time.sleep(1.1)


def language_rejection(candidate: Candidate, accepted: tuple[str, ...]) -> str | None:
    """G7 antes do download. Devolve o motivo do descarte, ou None.

    O metadado de idioma do OpenAlex segue o periódico, não o texto: um artigo
    em inglês num periódico espanhol vem marcado 'es'. Quando o título+abstract
    contradiz o metadado, vale o texto — e o PDF ainda passa pela checagem final.
    """
    metadata = (candidate.language or "").lower()[:2] or None
    detected = cand.detect_language(f"{candidate.title}. {candidate.abstract or ''}")
    if detected:
        return None if detected in accepted else f"{detected} (detectado no texto)"
    if metadata and metadata not in accepted:
        return f"{metadata} (metadado)"
    return None


class StatusStore:
    """Estado do lote em disco — permite retomar em várias execuções (G5)."""

    def __init__(self, path: Path):
        self.path = path
        self.data: dict = (
            json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        )

    @property
    def items(self) -> list[dict]:
        return self.data.setdefault("items", [])

    def save(self) -> None:
        self.path.write_text(
            json.dumps(self.data, ensure_ascii=False, indent=2), encoding="utf-8"
        )


def _candidate(item: dict) -> Candidate:
    record = item["candidate"]
    return Candidate(**{k: v for k, v in record.items() if k in Candidate.__dataclass_fields__})


def step_resolve(store: StatusStore, config) -> None:
    threshold = config.crossref.title_match_threshold
    todo = [i for i in store.items if i["status"] == UNRESOLVED]
    if not todo:
        return
    print(f"Localizando {len(todo)} títulos no OpenAlex…", file=sys.stderr)

    seen_ids = {
        i["candidate"]["openalex_id"] for i in store.items if i.get("candidate")
    }
    with OpenAlexClient(config) as client, CrossrefClient(config) as crossref:
        for item in todo:
            match, score = resolve_title(client, crossref, item["input_title"], threshold)
            item["match_score"] = round(score, 3)
            if match is None:
                item["status"] = NOT_FOUND
                item["reason"] = (
                    f"sem correspondência no OpenAlex (melhor similaridade {score:.2f} "
                    f"< {threshold})"
                )
                print(f"  [{item['n']:02d}] não localizado ({score:.2f})", file=sys.stderr)
                store.save()
                continue

            # Abstract: OpenAlex; na falta, Crossref (o OpenAlex omite o de alguns
            # editores). Sempre com a origem registrada.
            item["abstract_source"] = "OpenAlex" if match.abstract else None
            if not match.abstract and match.doi:
                abstract = crossref.fetch_abstract(match.doi)
                if abstract:
                    match.abstract = abstract
                    item["abstract_source"] = "Crossref"

            if match.openalex_id in seen_ids:
                item["status"] = DUPLICATE
                item["reason"] = "mesmo trabalho de outro item da lista"
            else:
                item["status"] = MATCHED
                seen_ids.add(match.openalex_id)
            item["candidate"] = asdict(match)
            print(f"  [{item['n']:02d}] ok ({score:.2f}) {match.title[:60]}", file=sys.stderr)
            store.save()


def step_download(store: StatusStore, location: Location, config) -> int:
    todo = [i for i in store.items if i["status"] == MATCHED]
    limit = config.max_papers_per_run
    batch, remaining = todo[:limit], todo[limit:]
    if not batch:
        return 0
    print(f"\nTentando download de {len(batch)} (G5: até {limit} por execução)…")

    s2_headers = {"User-Agent": USER_AGENT_TEMPLATE.format(email=config.polite_pool_email)}
    with OpenAccessResolver(config) as resolver, httpx.Client(
        timeout=30, headers=s2_headers
    ) as s2:
        for item in batch:
            candidate = _candidate(item)

            # G7 — idioma pelo título+abstract (ou metadado), antes de baixar.
            rejection = language_rejection(candidate, config.accepted_languages)
            if rejection:
                item["status"] = LANGUAGE_DISCARDED
                item["reason"] = f"idioma {rejection} fora de {config.accepted_languages}"
                store.save()
                continue

            # Mais uma localização open access declarada por API — não um atalho.
            if candidate.doi:
                extra = semantic_scholar_pdf(s2, candidate.doi)
                if extra and extra != candidate.pdf_url and extra not in candidate.alternate_pdf_urls:
                    candidate.alternate_pdf_urls.append(extra)

            filename = naming.build_filename(
                authors=candidate.authors,
                year=candidate.year,
                title=candidate.title,
                max_chars=config.title_max_chars,
            )
            if (location.papers_dir / filename).exists():
                item.update(status=DOWNLOADED, pdf_file=filename, source="já no corpus")
                store.save()
                continue

            print(f"  [{item['n']:02d}] {candidate.title[:65]}")
            result = resolver.resolve(candidate, location.papers_dir / filename)
            if result.ok:
                # G7 — terceira camada, sobre o texto real do PDF.
                language = (pdf_extract.extract(result.pdf_path).language or "")[:2]
                if language and language not in config.accepted_languages:
                    result.pdf_path.unlink(missing_ok=True)
                    item["status"] = LANGUAGE_DISCARDED
                    item["reason"] = f"PDF em '{language}'"
                else:
                    item.update(
                        status=DOWNLOADED, pdf_file=filename,
                        source=result.source, pdf_source_url=result.url,
                    )
                    print(f"      baixado via {result.source}")
            else:
                item["status"] = NOT_DOWNLOADED
                item["reason"] = result.blocked_reason or "desconhecido"
                item["host"] = result.host
                print(f"      não baixado: {item['reason'][:90]}")
            store.save()
            time.sleep(config.download.delay_between_seconds)

    return len(remaining)


def _link(item: dict) -> str:
    c = item.get("candidate") or {}
    if c.get("doi"):
        return f"https://doi.org/{c['doi']}"
    if c.get("landing_page_url"):
        return c["landing_page_url"]
    # Título não localizado: um link de busca, para a conferência manual.
    return f"https://scholar.google.com/scholar?q={quote_plus(clean_title(item['input_title']))}"


def _cell(text: str | None) -> str:
    return (text or "—").replace("|", "/").replace("\n", " ").strip()


def _abstract_block(item: dict) -> list[str]:
    """Bloco de um item na seção de abstracts: metadados, status e abstract."""
    c = item.get("candidate") or {}
    lines = [f"### {item['n']}. {c.get('title') or item['input_title']}", ""]
    if not c:
        return lines + [
            f"- **Status**: {STATUS_LABEL[item['status']]} — {item.get('reason')}",
            f"- **Título na lista**: {item['input_title']}",
            *([f"- **Nota**: {item['note']}"] if item.get("note") else []),
            "",
            "_Sem abstract: o título não foi localizado em nenhuma API._",
            "",
        ]
    authors = c.get("authors") or []
    author_text = ", ".join(authors[:6]) + (" et al." if len(authors) > 6 else "")
    lines.extend([
        f"- **Status**: {STATUS_LABEL[item['status']]}"
        + (f" — `{item['pdf_file']}`" if item.get("pdf_file") else "")
        + (f" — {item['reason']}" if item.get("reason") else ""),
        f"- **Autores**: {author_text or '—'}",
        f"- **Ano / venue**: {c.get('year') or '—'} · {c.get('venue') or '—'}",
        f"- **Link**: {_link(item)}",
    ])
    if item.get("match_score") is not None and item["match_score"] < 0.97:
        lines.append(
            f"- **Título na lista**: {item['input_title']} "
            f"(similaridade {item['match_score']:.2f} — confira)"
        )
    if item.get("note"):
        lines.append(f"- **Nota**: {item['note']}")
    lines.append("")
    if c.get("abstract"):
        lines.append(f"> {c['abstract']}")
        lines.append("")
        lines.append(f"_Fonte do abstract: {item.get('abstract_source') or 'OpenAlex'}._")
    else:
        lines.append(
            "_Sem abstract no OpenAlex, no Crossref nem no Semantic Scholar "
            "(o editor pode ter omitido o campo)._"
        )
    lines.append("")
    return lines


def step_report(
    store: StatusStore, location: Location, batch: str, titles_file: Path
) -> list[Path]:
    """Grava dois relatórios do lote: baixados e não baixados, cada um com abstracts."""
    items = store.items
    downloaded = [i for i in items if i["status"] == DOWNLOADED]
    missing = [i for i in items if i["status"] != DOWNLOADED]
    out_dir = location.deliverables_dir / "batches"
    out_dir.mkdir(parents=True, exist_ok=True)
    done_path = out_dir / f"{batch}-baixados.md"
    missing_path = out_dir / f"{batch}-nao-baixados.md"
    origin = [
        f"- **Origem**: `{titles_file.relative_to(location.path)}` "
        f"(lista triada pelo usuário; cada título localizado no OpenAlex)",
        f"- **Atualizado em**: {date.today().isoformat()}",
    ]

    done = [
        f"# {batch} — papers baixados ({len(downloaded)} de {len(items)})",
        "",
        *origin,
        "- **PDFs**: `deliverables/papers/`",
        f"- **Não baixados**: ver `{missing_path.name}`",
        "",
        "## Lista",
        "",
        "| # | Título | Ano | Arquivo |",
        "|---|---|---|---|",
    ]
    for item in downloaded:
        c = item["candidate"]
        done.append(
            f"| {item['n']} | {_cell(c.get('title'))} | {c.get('year') or '—'} "
            f"| {_cell(item.get('pdf_file'))} |"
        )
    if not downloaded:
        done.append("| — | _Nenhum._ | | |")

    counts: dict[str, int] = {}
    for item in missing:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    pending = [
        f"# {batch} — papers não baixados ({len(missing)} de {len(items)})",
        "",
        *origin,
        "- **Por status**: "
        + (" · ".join(f"{STATUS_LABEL[s]}: {n}" for s, n in sorted(counts.items())) or "—"),
        "- **Cabe revisão manual**: obtenha o PDF pelo link (ex.: acesso institucional) "
        "e deposite em `materials/`. Lista consolidada do tema em `deliverables/pending.md`.",
        f"- **Baixados**: ver `{done_path.name}`",
        "",
        "## Lista",
        "",
        "| # | Título | Ano | Status | Motivo | Link |",
        "|---|---|---|---|---|---|",
    ]
    for item in missing:
        c = item.get("candidate") or {}
        pending.append(
            f"| {item['n']} | {_cell(c.get('title') or item['input_title'])} "
            f"| {c.get('year') or '—'} | {STATUS_LABEL[item['status']]} "
            f"| {_cell(item.get('reason'))} | {_link(item)} |"
        )
    if not missing:
        pending.append("| — | _Nenhum._ | | | | |")

    for lines, selected, path in ((done, downloaded, done_path), (pending, missing, missing_path)):
        lines.extend(["", "## Abstracts", ""])
        for item in selected:
            lines.extend(_abstract_block(item))
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    # Relatório único das versões anteriores, agora substituído pelos dois acima.
    (out_dir / f"{batch}-status.md").unlink(missing_ok=True)

    # As linhas deste lote são reescritas a cada execução: o motivo muda entre
    # tentativas, e um item obtido deixa de ser pendência.
    if location.pending_md.exists():
        prefixes = set()
        for i in items:
            for title in ((i.get("candidate") or {}).get("title"), clean_title(i["input_title"])):
                if title:
                    prefixes.add(f"| {_cell(title)} |")
        rows = location.pending_md.read_text(encoding="utf-8").splitlines(keepends=True)
        location.pending_md.write_text(
            "".join(r for r in rows if not any(r.startswith(p) for p in prefixes)),
            encoding="utf-8",
        )

    for item in items:
        if item["status"] not in {NOT_DOWNLOADED, NOT_FOUND, LANGUAGE_DISCARDED}:
            continue
        c = item.get("candidate") or {}
        cand.append_pending(
            location.pending_md,
            title=c.get("title") or clean_title(item["input_title"]),
            year=c.get("year"),
            host=item.get("host") or c.get("host_platform"),
            link=_link(item),
            reason=f"{batch}: {item.get('reason')}"
            + (f" — {item['note']}" if item.get("note") else ""),
        )
    return [done_path, missing_path]


def reset_for_retry(store: StatusStore) -> int:
    """Devolve à fila os itens não obtidos (falha transitória, fonte nova etc.)."""
    count = 0
    for item in store.items:
        if item["status"] == NOT_FOUND:
            item["status"] = UNRESOLVED
        elif item["status"] in {NOT_DOWNLOADED, LANGUAGE_DISCARDED}:
            item["status"] = MATCHED
        else:
            continue
        item.pop("reason", None)
        count += 1
    store.save()
    return count


def cmd_fetch(location: Location, titles_file: Path, batch: str, retry: bool = False) -> int:
    config = load_config()
    ensure_location(location)

    store = StatusStore(location.path / f".title-list-{batch}.json")
    if not store.items:
        titles = read_titles(titles_file)
        store.data.update(batch=batch, titles_file=str(titles_file))
        store.items.extend(
            {"n": n, "input_title": t, "status": UNRESOLVED}
            for n, t in enumerate(titles, start=1)
        )
        store.save()
    elif retry:
        print(f"Retentando {reset_for_retry(store)} itens não obtidos.")

    step_resolve(store, config)
    backfill_abstracts(store, config)
    remaining = step_download(store, location, config)
    reports = step_report(store, location, batch, titles_file.resolve())

    counts: dict[str, int] = {}
    for item in store.items:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    print("\n" + " | ".join(f"{STATUS_LABEL[s]}: {n}" for s, n in sorted(counts.items())))
    for report in reports:
        print(f"Relatório: {report}")
    discarded = [i for i in store.items if i["status"] == LANGUAGE_DISCARDED]
    if discarded:
        # G7 — descartes por idioma são sempre reportados.
        print(f"Descartados por idioma: {len(discarded)}")
        for item in discarded:
            print(f"  - [{item['n']}] {item['input_title'][:60]} ({item['reason']})")
    if remaining:
        print(f"\n{remaining} itens aguardam download — rode o mesmo comando de novo (G5).")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="title_list", description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)
    p_fetch = sub.add_parser("fetch", help="Localiza, baixa e reporta uma lista de títulos")
    p_fetch.add_argument("location", help="area/projeto/tema")
    p_fetch.add_argument("--titles", required=True, type=Path, help="Arquivo, um título por linha")
    p_fetch.add_argument("--batch", required=True, help="Nome do lote (ex.: lote-01)")
    p_fetch.add_argument(
        "--retry", action="store_true",
        help="Recoloca na fila os não localizados, não baixados e descartados",
    )
    args = parser.parse_args(argv)

    location = parse_location(args.location)
    if location is None:
        print(f"Localização inválida: '{args.location}'. Use area/projeto/tema.")
        return 2
    if not args.titles.exists():
        print(f"Arquivo de títulos não encontrado: {args.titles}")
        return 2
    return cmd_fetch(location, args.titles, args.batch, args.retry)


if __name__ == "__main__":
    raise SystemExit(main())
