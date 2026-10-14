"""Obtenção dos PDFs das obras citadas por um manuscrito (modo revisão de manuscrito).

Lê a lista de referências de `manuscripts/<slug>/reference-coverage.md`, identifica
cada obra no Crossref e no OpenAlex (só título e sobrenome do 1º autor saem para as
APIs — o texto do manuscrito, nunca) e baixa o PDF open access pelo mesmo resolver
do /literature-review (OpenAlex -> arXiv -> Unpaywall).

NUNCA contorna bloqueio: paywall, 403 ou ausência de PDF aberto viram pendência com
link e motivo, para obtenção manual.

Nome do arquivo: "<Autores> - <Ano> - <Título>.pdf" (scripts/naming.py), montado a
partir da lista de referências do manuscrito, para o arquivo casar com a citação.

Uso:
    uv run python -m scripts.manuscript_refs fetch <slug> [--only 5,6] [--dry-run]
    uv run python -m scripts.manuscript_refs coverage <slug>
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path

import pymupdf

from scripts.config import REPO_ROOT, load_config
from scripts.crossref import CrossrefClient, normalize_title, title_similarity
from scripts.naming import build_filename, resolve_collision
from scripts.oa_resolver import OpenAccessResolver
from scripts.openalex import Candidate, OpenAlexClient

MANUSCRIPTS_ROOT = REPO_ROOT / "manuscripts"
MANIFEST = ".fetch-manifest.json"
STAGING = ".downloads"

# Abaixo do title_match_threshold do config.yaml a correspondência é ambígua: não
# baixamos, registramos pendência. Acima deste, o título basta, sem confirmar autor.
EXACT_THRESHOLD = 0.97
MAX_YEAR_GAP = 3  # versão online x impressa, reimpressões próximas

_INITIALS = r"[A-Za-z]{1,2}\.(?:-?[A-Za-z]{1,2}\.)*"
_PURE_AUTHOR = re.compile(rf"^(.+?), ({_INITIALS})$")
_AUTHOR_THEN_TITLE = re.compile(rf"^(.+?), ({_INITIALS}) (.*)$")
_YEAR = re.compile(r"\b(1[89]\d\d|20\d\d)\b")
_NOTE = re.compile(r"\s*\[conferir[^\]]*\]")


# --------------------------------------------------------------------------- #
# Lista de referências
# --------------------------------------------------------------------------- #


@dataclass
class Reference:
    n: int
    text: str
    authors: list[str]  # "Sobrenome, I." na ordem da lista
    et_al: bool
    title: str
    year: int | None
    kind: str  # article | proceedings | chapter | book
    has_pdf: bool  # já marcada ✅ no reference-coverage.md

    @property
    def first_surname(self) -> str:
        return self.authors[0].split(",")[0].strip() if self.authors else ""

    @property
    def filename(self) -> str:
        names = list(self.authors)
        if self.et_al:
            # "Voelkel; et al." tem 3+ autores: o "et al" do nome do arquivo vem disso.
            names += ["_, _."] * max(0, 3 - len(names))
        return build_filename(names, self.year, self.title, load_config().title_max_chars)


def parse_reference(n: int, raw: str, has_pdf: bool = False) -> Reference:
    """Decompõe uma referência no estilo MDPI: autores, título, ano, tipo."""
    text = _NOTE.sub("", raw).strip()
    parts = text.split("; ")
    authors: list[str] = []
    et_al = False
    rest = ""
    for i, part in enumerate(parts):
        if part.startswith("et al."):
            et_al = True
            rest = "; ".join([part[len("et al."):].strip(), *parts[i + 1:]])
            break
        pure = _PURE_AUTHOR.match(part)
        if pure:
            authors.append(f"{pure.group(1)}, {pure.group(2)}")
            continue
        mixed = _AUTHOR_THEN_TITLE.match(part)
        if mixed:
            authors.append(f"{mixed.group(1)}, {mixed.group(2)}")
            rest = "; ".join([mixed.group(3), *parts[i + 1:]])
        else:
            rest = "; ".join(parts[i:])
        break

    rest = re.sub(r"^\(Eds?\.\)\s*", "", rest)
    # "U.S." não termina o título.
    protected = rest.replace("U.S.", "U\x00S\x00")
    end = re.search(r"\?\s|\.\s|;\s", protected)
    if end:
        title = protected[: end.start() + (1 if protected[end.start()] == "?" else 0)]
        after = protected[end.end():]
    else:
        title, after = protected, ""
    if title.endswith("?"):
        # "What's in a Name? Some Reflections on…": o que vem depois do "?" é
        # subtítulo quando parece frase (3+ palavras, sem números, sem "In …").
        nxt = re.match(r"([^.;]+?)(\.\s|$)", after)
        if nxt and len(nxt.group(1).split()) >= 3 and not re.search(r"\d", nxt.group(1)) \
                and not nxt.group(1).startswith("In "):
            title = f"{title} {nxt.group(1)}"
            after = after[nxt.end():]
    title = title.replace("\x00", ".").strip()
    after = after.replace("\x00", ".")

    year_match = _YEAR.search(after)
    if end and protected[end.start()] == ";":
        kind = "book"
    elif after.startswith("In Proceedings"):
        kind = "proceedings"
    elif after.startswith("In ") and re.search(r"\bEds?\.", after):
        kind = "chapter"
    else:
        kind = "article"

    return Reference(
        n=n, text=raw, authors=authors, et_al=et_al, title=title,
        year=int(year_match.group(1)) if year_match else None,
        kind=kind, has_pdf=has_pdf,
    )


_COVERAGE_ROW = re.compile(r"^\| (\d+) \| (.+?) \| `([^`]*)` \| (✅|❌) \| (.*) \|$")


def load_references(coverage_md: Path) -> list[Reference]:
    refs = []
    for line in coverage_md.read_text(encoding="utf-8").splitlines():
        m = _COVERAGE_ROW.match(line)
        if m:
            refs.append(parse_reference(int(m.group(1)), m.group(2), m.group(4) == "✅"))
    return refs


# --------------------------------------------------------------------------- #
# Identificação (Crossref + OpenAlex)
# --------------------------------------------------------------------------- #


def _score(ref_title: str, found: str, subtitle: str = "") -> float:
    """Similaridade tolerante a subtítulo: as bases às vezes o separam do título."""
    main = re.split(r":|\?", ref_title)[0]
    options = [title_similarity(ref_title, found)]
    if subtitle:
        options.append(title_similarity(ref_title, f"{found}: {subtitle}"))
    if len(normalize_title(main)) >= 20:
        options.append(title_similarity(main, found))
    return max(options)


def _author_agrees(surname: str, found: list[str]) -> bool:
    tokens = {t for t in normalize_title(surname).split() if len(t) > 2}
    found_tokens = {t for name in found for t in normalize_title(name).split() if len(t) > 2}
    return bool(tokens & found_tokens) if tokens else False


def _accept(ref: Reference, score: float, authors: list[str], year: int | None) -> bool:
    if score < load_config().crossref.title_match_threshold:
        return False
    # Autor sempre confere quando a base o informa: uma resenha do livro tem o mesmo
    # título exato e outro autor. Título quase idêntico só dispensa autor ausente.
    if authors and not _author_agrees(ref.first_surname, authors):
        return False
    if not authors and score < EXACT_THRESHOLD:
        return False
    if ref.year and year and abs(ref.year - year) > MAX_YEAR_GAP:
        return False
    return True


@dataclass
class Match:
    source: str  # crossref | openalex
    doi: str | None
    title: str
    year: int | None
    score: float
    work_type: str | None


def crossref_match(client: CrossrefClient, ref: Reference) -> Match | None:
    params = {"query.bibliographic": ref.title, "rows": "20"}
    if ref.first_surname:
        params["query.author"] = ref.first_surname
    response = client._get(f"{client.config.crossref.base_url}/works", params=params)
    if response is None:
        return None
    try:
        items = response.json()["message"]["items"]
    except (KeyError, ValueError):
        return None

    accepted: list[tuple[bool, float, int, Match]] = []
    for item in items:
        work = client._work_from_message(item)
        if not work:
            continue
        subtitle = (item.get("subtitle") or [""])[0]
        score = _score(ref.title, work.title, subtitle)
        year = int(work.year) if work.year else None
        if _accept(ref, score, work.authors, year):
            gap = abs((ref.year or year or 0) - (year or ref.year or 0))
            full_title = f"{work.title}: {subtitle}" if subtitle else work.title
            published = not _is_preprint(work.doi, work.entry_type)
            accepted.append((published, score, -gap, Match("crossref", work.doi.lower(), full_title,
                                                           year, round(score, 3), work.entry_type)))
    if not accepted:
        return None
    # O DOI registrado deve ser o da versão publicada, não o do SSRN/PsyArXiv (as cópias
    # abertas desses entram de qualquer forma pela busca no OpenAlex). Entre reimpressões
    # e capítulos homônimos: o mais parecido e de ano mais próximo.
    accepted.sort(key=lambda x: (x[0], round(x[1], 2), x[2]), reverse=True)
    return accepted[0][3]


_PREPRINT_PREFIXES = ("10.2139/", "10.31234/", "10.31235/", "10.31219/", "10.48550/", "10.1101/")


def _is_preprint(doi: str, entry_type: str | None) -> bool:
    return entry_type == "posted-content" or doi.lower().startswith(_PREPRINT_PREFIXES)


@dataclass
class OAWork:
    candidate: Candidate
    versions: dict[str, str]  # pdf_url -> version (publishedVersion | acceptedVersion | submittedVersion)


def _oa_work(raw: dict) -> OAWork | None:
    candidate = OpenAlexClient._candidate_from_work(raw)
    if not candidate:
        return None
    versions = {}
    for loc in [raw.get("best_oa_location") or {}, *(raw.get("locations") or [])]:
        if loc.get("pdf_url"):
            versions.setdefault(loc["pdf_url"], loc.get("version") or "")
    return OAWork(candidate, versions)


def openalex_works(client: OpenAlexClient, ref: Reference, doi: str | None) -> list[OAWork]:
    """O registro do DOI e outros registros do mesmo trabalho (preprints, repositórios)."""
    base = client.config.openalex.base_url
    works: list[OAWork] = []
    if doi:
        raw = client._get(f"{base}/works/https://doi.org/{doi}", {})
        if raw and (w := _oa_work(raw)):
            works.append(w)

    query = re.sub(r"[,:;?\"]", " ", ref.title)
    payload = client._get(f"{base}/works", {"search": query, "per-page": "10"})
    for raw in (payload or {}).get("results", []):
        w = _oa_work(raw)
        if not w or any(w.candidate.openalex_id == x.candidate.openalex_id for x in works):
            continue
        score = _score(ref.title, w.candidate.title)
        if _accept(ref, score, w.candidate.authors, w.candidate.year):
            works.append(w)
    return works


def merge(works: list[OAWork]) -> tuple[Candidate, dict[str, str]]:
    """Um candidato só, com as URLs de PDF de todos os registros do trabalho."""
    base = works[0].candidate
    versions: dict[str, str] = {}
    urls: list[str] = list(base.alternate_pdf_urls)
    for w in works:
        versions.update({k: v for k, v in w.versions.items() if k not in versions})
        for url in [w.candidate.pdf_url, *w.candidate.alternate_pdf_urls]:
            if url and url != base.pdf_url and url not in urls:
                urls.append(url)
    base.alternate_pdf_urls = urls
    if not base.pdf_url and urls:
        base.pdf_url = urls.pop(0)
    base.is_oa = base.is_oa or any(w.candidate.is_oa for w in works)
    return base, versions


# --------------------------------------------------------------------------- #
# Conferência do PDF baixado
# --------------------------------------------------------------------------- #


def verify_pdf(path: Path, ref: Reference) -> tuple[bool, str]:
    """O PDF é mesmo a obra citada? Confere título e 1º autor nas primeiras páginas."""
    try:
        with pymupdf.open(path) as doc:
            text = " ".join(doc[i].get_text() for i in range(min(3, doc.page_count)))
    except Exception as exc:  # noqa: BLE001 — PDF corrompido é só mais um motivo de rejeição
        return False, f"PDF ilegível ({type(exc).__name__})"

    norm = normalize_title(text)
    if re.search(r"\bbook reviews?\b|\breview of\b", norm[:400]):
        return False, "PDF é uma resenha da obra, não a obra"
    if len(norm) < 200:
        return True, "sem texto extraível (PDF escaneado?): conferir manualmente"

    words = [w for w in normalize_title(re.split(r":|\?", ref.title)[0]).split() if len(w) > 3]
    words = words or normalize_title(ref.title).split()
    hit = sum(1 for w in words if w in norm) / max(1, len(words))
    # Sem limite no fim da palavra: o PDF cola a afiliação no nome ("Modgil1").
    surname_tokens = [t for t in normalize_title(ref.first_surname).split() if len(t) > 2]
    author_ok = any(re.search(rf"\b{re.escape(t)}", norm) for t in surname_tokens) \
        if surname_tokens else True
    if hit >= 0.75 and author_ok:
        return True, ""
    return False, f"PDF não confere com a referência (título {hit:.0%}, autor {'ok' if author_ok else 'ausente'})"


# --------------------------------------------------------------------------- #
# Comandos
# --------------------------------------------------------------------------- #


@dataclass
class Outcome:
    n: int
    status: str  # downloaded | pending | skipped
    reference: str
    kind: str
    expected_file: str
    file: str | None = None
    doi: str | None = None
    matched_title: str | None = None
    matched_year: int | None = None
    match_score: float | None = None
    source: str | None = None
    version: str | None = None
    url: str | None = None
    note: str | None = None
    reason: str | None = None
    host: str | None = None
    link: str | None = None
    attempts: list[str] = field(default_factory=list)


def _version_label(source: str | None, url: str | None, versions: dict[str, str]) -> str:
    v = versions.get(url or "", "")
    return {"publishedVersion": "publicada", "acceptedVersion": "aceita (pós-print)",
            "submittedVersion": "preprint"}.get(v, "não informada pela API")


def cmd_fetch(slug: str, only: set[int] | None, dry_run: bool) -> int:
    root = MANUSCRIPTS_ROOT / slug
    coverage = root / "reference-coverage.md"
    refs_dir = root / "references"
    if not coverage.exists():
        print(f"Não encontrado: {coverage}")
        return 1
    config = load_config()
    refs = load_references(coverage)
    manifest_path = refs_dir / MANIFEST
    previous = json.loads(manifest_path.read_text("utf-8")) if manifest_path.exists() else {}
    staging = refs_dir / STAGING
    outcomes: dict[str, dict] = dict(previous.get("outcomes", {}))

    todo = [r for r in refs if (only is None or r.n in only)]
    print(f"{len(refs)} referências na lista; {len(todo)} nesta passada\n", flush=True)

    with CrossrefClient(config) as cr, OpenAlexClient(config) as oa, OpenAccessResolver(config) as resolver:
        for ref in todo:
            out = Outcome(n=ref.n, status="pending", reference=ref.text, kind=ref.kind,
                          expected_file=ref.filename)
            print(f"[{ref.n}] {ref.first_surname} {ref.year} — {ref.title[:60]}", flush=True)
            # ✅ que não veio deste script (PDF depositado à mão) fica intocado; os baixados
            # por ele passam pela reidentificação abaixo, que preserva o arquivo.
            if ref.has_pdf and previous.get("outcomes", {}).get(str(ref.n), {}).get("status") != "downloaded":
                out.status, out.note = "skipped", "PDF já estava em references/"
                outcomes[str(ref.n)] = asdict(out)
                print("    já disponível, pulada", flush=True)
                continue

            match = crossref_match(cr, ref)
            works = openalex_works(oa, ref, match.doi if match else None)
            if not match and works:
                c = works[0].candidate
                match = Match("openalex", c.doi, c.title, c.year,
                              round(_score(ref.title, c.title), 3), c.work_type)
            if match:
                out.doi, out.matched_title, out.matched_year = match.doi, match.title, match.year
                out.match_score, out.source = match.score, match.source
                notes = []
                if ref.year and match.year and ref.year != match.year:
                    notes.append(f"ano na base: {match.year} (lista: {ref.year})")
                if match.score < EXACT_THRESHOLD:
                    notes.append(f"título na base difere: \"{match.title}\"")
                out.note = "; ".join(notes) or None

            if not match:
                out.reason = "obra não identificada no Crossref/OpenAlex com segurança"
                out.link = None
                outcomes[str(ref.n)] = asdict(out)
                print(f"    pendente: {out.reason}", flush=True)
                continue

            if not works:
                # Só o Crossref conhece a obra: sem registro OA, só resta o Unpaywall.
                candidate = Candidate(openalex_id="", title=match.title, authors=[], year=match.year,
                                      venue=None, doi=match.doi, abstract=None, is_oa=False,
                                      oa_status=None, pdf_url=None, landing_page_url=None,
                                      host_platform=None, work_type=match.work_type)
                versions: dict[str, str] = {}
            else:
                candidate, versions = merge(works)
                if match.doi and not candidate.doi:
                    candidate.doi = match.doi

            out.host = candidate.host_platform or candidate.venue
            out.link = candidate.best_link
            kept = previous.get("outcomes", {}).get(str(ref.n), {})
            if kept.get("status") == "downloaded" and (refs_dir / kept["file"]).exists():
                # Reidentificação: o PDF já conferido fica; só os metadados são atualizados.
                for key in ("status", "file", "version", "url"):
                    setattr(out, key, kept[key])
                out.source = f"{out.source} → {kept['source'].split(' → ')[-1]}"
                # Notas geradas pela identificação anterior são recalculadas; as manuais ficam.
                manual = [part for part in (kept.get("note") or "").split("; ")
                          if part and not part.startswith(("ano na base", "título na base"))]
                out.note = "; ".join(filter(None, [out.note, *manual])) or None
                outcomes[str(ref.n)] = asdict(out)
                print(f"    já baixado, metadados atualizados (DOI {out.doi})", flush=True)
                continue

            if dry_run:
                out.reason = "dry-run"
                outcomes[str(ref.n)] = asdict(out)
                print(f"    identificada ({match.source}, {match.score}); "
                      f"OA={candidate.is_oa} pdf={'sim' if candidate.pdf_url else 'não'}", flush=True)
                continue

            tmp = staging / f"{ref.n}.pdf"
            result = resolver.resolve(candidate, tmp)
            if result.ok:
                ok, check = verify_pdf(tmp, ref)
                if ok:
                    refs_dir.mkdir(parents=True, exist_ok=True)
                    name = resolve_collision(refs_dir, ref.filename)
                    shutil.move(str(tmp), refs_dir / name)
                    out.status, out.file = "downloaded", name
                    out.version = _version_label(result.source, result.url, versions)
                    out.url = result.url
                    out.source = f"{out.source} → {result.source}"
                    if check:
                        out.note = "; ".join(filter(None, [out.note, check]))
                    print(f"    baixado via {result.source} ({out.version}) → {name}", flush=True)
                else:
                    tmp.unlink(missing_ok=True)
                    out.reason, out.url = check, result.url
                    print(f"    rejeitado: {check}", flush=True)
            else:
                out.reason = result.blocked_reason or "desconhecido"
                print(f"    pendente: {out.reason}", flush=True)
            outcomes[str(ref.n)] = asdict(out)
            time.sleep(config.download.delay_between_seconds)

    if staging.exists() and not any(staging.iterdir()):
        staging.rmdir()
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps({"slug": slug, "updated": date.today().isoformat(),
                                         "outcomes": outcomes}, ensure_ascii=False, indent=1), "utf-8")
    counts = {s: sum(1 for o in outcomes.values() if o["status"] == s)
              for s in ("downloaded", "pending", "skipped")}
    print(f"\nBaixados: {counts['downloaded']} · pendentes: {counts['pending']} · "
          f"já disponíveis: {counts['skipped']}\nManifest: {manifest_path}")
    return 0


PENDING_START = "<!-- pendentes:inicio -->"
PENDING_END = "<!-- pendentes:fim -->"


def _cell(text: str | None) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ")


def cmd_coverage(slug: str) -> int:
    """Reflete o manifest no reference-coverage.md: arquivo, ✅/❌, DOI, pendências."""
    root = MANUSCRIPTS_ROOT / slug
    coverage = root / "reference-coverage.md"
    manifest = json.loads((root / "references" / MANIFEST).read_text("utf-8"))["outcomes"]
    refs_dir = root / "references"

    lines = coverage.read_text("utf-8").splitlines()
    out_lines: list[str] = []
    have = total = 0
    for line in lines:
        m = _COVERAGE_ROW.match(line)
        if not m:
            out_lines.append(line.replace("| Arquivo esperado |", "| Arquivo |"))
            continue
        n, ref_text, file_, mark, notes = m.groups()
        total += 1
        o = manifest.get(n)
        if o and o["status"] != "skipped":
            # Idempotente: descarta o que uma execução anterior deste comando escreveu.
            notes = re.split(r";?\s*(?:Obtido em |pendente: )", notes)[0]
        if o and o["status"] == "downloaded":
            file_, mark = o["file"], "✅"
            extra = [f"Obtido em {manifest_date(root)} via {o['source']}; versão {o['version']}"]
            if o.get("doi"):
                extra.append(f"DOI {o['doi']}")
            if o.get("note"):
                extra.append(o["note"])
            notes = "; ".join(filter(None, [notes.strip(), ". ".join(extra)]))
        elif o and o["status"] == "pending":
            file_ = o["expected_file"]
            extra = [f"pendente: {o['reason']}"]
            if o.get("doi"):
                extra.append(f"DOI {o['doi']}")
            if o.get("note"):
                extra.append(o["note"])
            notes = "; ".join(filter(None, [notes.strip(), "; ".join(extra)]))
        if mark == "✅" or (refs_dir / file_).exists():
            have += 1
        out_lines.append(f"| {n} | {ref_text} | `{file_}` | {mark} | {_cell(notes)} |")

    text = "\n".join(out_lines) + "\n"
    text = re.sub(r"- \*\*Cobertura\*\*: .*", f"- **Cobertura**: {have} de {total} obras com PDF em `references/`.", text)
    text = re.sub(r"- \*\*Atualizado em\*\*: .*", f"- **Atualizado em**: {date.today().isoformat()}", text)

    pending = [manifest[k] for k in sorted(manifest, key=int) if manifest[k]["status"] == "pending"]
    block = [PENDING_START, "## Pendentes de obtenção manual", "",
             "Sem PDF open access acessível por API (ou correspondência insegura). Nunca houve "
             "tentativa de contornar paywall. Baixe pelo acesso institucional e salve em "
             "`references/` com o nome indicado.", "",
             "| n | Obra | Nome do arquivo | Link | Motivo |", "|---|---|---|---|---|"]
    for o in pending:
        title = re.sub(_NOTE, "", o["reference"])[:120]
        block.append(f"| {o['n']} | {_cell(title)} | `{o['expected_file']}` | {o.get('link') or '—'} | {_cell(o['reason'])} |")
    block.append(PENDING_END)
    block_text = "\n".join(block)
    if PENDING_START in text:
        text = re.sub(re.escape(PENDING_START) + r".*?" + re.escape(PENDING_END), block_text, text, flags=re.S)
    else:
        text = text.rstrip("\n") + "\n\n" + block_text + "\n"
    coverage.write_text(text, "utf-8")
    print(f"{coverage}: {have}/{total} com PDF; {len(pending)} pendentes")
    return 0


def manifest_date(root: Path) -> str:
    return json.loads((root / "references" / MANIFEST).read_text("utf-8")).get("updated", "")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_fetch = sub.add_parser("fetch", help="identifica e baixa os PDFs open access")
    p_fetch.add_argument("slug")
    p_fetch.add_argument("--only", help="números da lista, ex.: 5,6,33")
    p_fetch.add_argument("--dry-run", action="store_true", help="só identifica, não baixa")
    p_parse = sub.add_parser("parse", help="mostra como cada referência foi decomposta")
    p_parse.add_argument("slug")
    p_cov = sub.add_parser("coverage", help="atualiza o reference-coverage.md a partir do manifest")
    p_cov.add_argument("slug")
    args = parser.parse_args(argv)

    if args.cmd == "parse":
        for r in load_references(MANUSCRIPTS_ROOT / args.slug / "reference-coverage.md"):
            print(f"{r.n:>3} {r.kind:<11} {r.year} | {r.first_surname} | {r.filename}")
        return 0
    if args.cmd == "coverage":
        return cmd_coverage(args.slug)
    only = {int(x) for x in args.only.split(",")} if args.only else None
    return cmd_fetch(args.slug, only, args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
