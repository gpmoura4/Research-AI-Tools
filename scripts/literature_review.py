"""Pipeline de revisão de literatura: busca -> aprovação -> download.

Três etapas, com aprovação humana obrigatória no meio (G4):

  1. search   — consulta o OpenAlex, deduplica contra o corpus do tema e grava
                candidates.md (todos os itens DESMARCADOS) + um manifest JSON.
                Nada é baixado.

  2. (humano) — o usuário marca [x] nos itens aprovados; o agente escreve o score
                de relevância lendo os abstracts reais retornados pela API.

  3. fetch    — baixa APENAS os itens marcados. Sem PDF open access, registra em
                pending.md com o link da plataforma hospedeira. Nunca contorna
                bloqueio.

Uso:
  uv run python -m scripts.literature_review search <area>/<proj>/<tema> --query "..."
  uv run python -m scripts.literature_review fetch  <area>/<proj>/<tema>
  uv run python -m scripts.literature_review status <area>/<proj>/<tema>
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import asdict
from pathlib import Path

from scripts import candidates as cand
from scripts import pdf_extract
from scripts.config import load_config
from scripts.locations import Location, ensure_location, parse_location
from scripts.oa_resolver import OpenAccessResolver
from scripts.openalex import Candidate, OpenAlexClient
from scripts.process_materials import build_manifest

SEARCH_MANIFEST = ".search-manifest.json"
DOWNLOAD_DIR = ".downloads"


def cmd_search(
    location: Location,
    queries: list[str],
    review_type: str,
    from_year: int | None,
    to_year: int | None,
    precise: bool = False,
) -> int:
    config = load_config()
    ensure_location(location)

    collected: list[Candidate] = []
    with OpenAlexClient(config) as client:
        for query in queries:
            print(f"  buscando: {query}", file=sys.stderr)
            results = client.search(
                query,
                from_year=from_year,
                to_year=to_year,
                precise=precise,
                languages=config.accepted_languages,
            )
            print(f"    {len(results)} resultados", file=sys.stderr)
            collected.extend(results)

    if not collected:
        print("Nenhum resultado retornado pelo OpenAlex.")
        return 1

    # G7 — segunda camada: o filtro da API não pega registros sem metadado de
    # idioma, então revalidamos pelo título + abstract.
    collected, rejected_language = cand.filter_by_language(
        collected, config.accepted_languages
    )

    # Item 6: dedupe contra o corpus do tema ANTES de apresentar ao usuário.
    fresh, duplicates = cand.dedupe_candidates(collected, location.references_bib)

    # Ordena pela relevância textual do OpenAlex, não por citações: o teto de 30
    # (G5) corta a cauda, e ordenar por fama descartaria justamente os papers
    # específicos do tema em favor de clássicos de áreas vizinhas.
    fresh.sort(key=lambda c: c.relevance_score, reverse=True)

    # G5 — teto por passada.
    limit = config.max_papers_per_run
    over_limit = fresh[limit:]
    fresh = fresh[:limit]

    manifest = {
        "location": str(location),
        "review_type": review_type,
        "queries": queries,
        "candidates": [asdict(c) for c in fresh],
        "duplicates_skipped": len(duplicates),
        "over_limit_skipped": len(over_limit),
    }
    manifest_path = location.path / SEARCH_MANIFEST
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    cand.write_candidates_md(
        location.candidates_md,
        fresh,
        location=str(location),
        queries=queries,
        review_type=review_type,
        duplicates_skipped=len(duplicates),
    )

    print(f"\nManifest: {manifest_path}")
    print(f"candidates.md: {location.candidates_md}")
    print(
        f"Candidatos: {len(fresh)} | já no corpus/duplicados: {len(duplicates)}"
        + (f" | acima do limite de {limit}: {len(over_limit)}" if over_limit else "")
    )
    oa_count = sum(1 for c in fresh if c.is_oa)
    print(f"Com open access declarado: {oa_count} de {len(fresh)}")

    # G7 — descartes por idioma ficam visíveis: o usuário precisa saber o que a
    # regra excluiu, não descobrir depois que faltou algo.
    if rejected_language:
        print(
            f"\nDescartados por idioma ({'/'.join(config.accepted_languages)} "
            f"apenas): {len(rejected_language)}"
        )
        for candidate, why in rejected_language[:8]:
            print(f"  - [{why}] {candidate.title[:64]}")
        if len(rejected_language) > 8:
            print(f"  ... e mais {len(rejected_language) - 8}")
    return 0


def cmd_fetch(location: Location) -> int:
    config = load_config()

    manifest_path = location.path / SEARCH_MANIFEST
    if not manifest_path.exists():
        print(f"Manifest de busca não encontrado: {manifest_path}. Rode 'search' antes.")
        return 1

    approved = cand.parse_approvals(location.candidates_md)
    total_items = cand.count_items(location.candidates_md)

    # G4 — sem aprovação explícita, nada é baixado.
    if not approved:
        print(
            f"Nenhum item aprovado em {location.candidates_md} "
            f"({total_items} candidatos listados).\n"
            "Marque [x] nos itens desejados e rode novamente. "
            "Nada foi baixado."
        )
        return 1

    if len(approved) > config.max_papers_per_run:
        print(
            f"{len(approved)} aprovados excedem o limite de "
            f"{config.max_papers_per_run} por passada (G5). Reduza a seleção."
        )
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    by_title = {c["title"]: c for c in manifest["candidates"]}

    download_dir = location.path / DOWNLOAD_DIR
    downloaded: list[Path] = []
    pending: list[tuple[str, str]] = []

    print(f"Aprovados: {len(approved)} de {total_items} candidatos\n")

    with OpenAccessResolver(config) as resolver:
        for item in approved:
            record = by_title.get(item.title)
            if record is None:
                print(f"  ! não encontrado no manifest: {item.title[:60]}")
                continue

            candidate = Candidate(**{
                k: v for k, v in record.items()
                if k in Candidate.__dataclass_fields__
            })

            # Nome provisório; a nomenclatura definitiva vem do pipeline da Fase 1,
            # que lê os metadados do PDF baixado.
            safe_stem = f"{item.number:02d}-{(candidate.doi or candidate.title)[:60]}"
            safe_stem = "".join(ch if ch.isalnum() or ch in "-_. " else "-" for ch in safe_stem)
            destination = download_dir / f"{safe_stem}.pdf"

            print(f"  [{item.number}] {candidate.title[:65]}")
            result = resolver.resolve(candidate, destination)

            if result.ok:
                # G7 — última verificação, agora sobre o texto real do PDF: o
                # metadado do idioma pode estar ausente ou errado.
                extraction = pdf_extract.extract(result.pdf_path)
                pdf_language = (extraction.language or "")[:2]
                if pdf_language and pdf_language not in config.accepted_languages:
                    print(f"      descartado: PDF está em '{pdf_language}'")
                    result.pdf_path.unlink(missing_ok=True)
                    cand.append_pending(
                        location.pending_md,
                        title=candidate.title,
                        year=candidate.year,
                        host=result.host,
                        link=result.link,
                        reason=(
                            f"PDF em '{pdf_language}' — fora dos idiomas aceitos "
                            f"({'/'.join(config.accepted_languages)})"
                        ),
                    )
                    pending.append((candidate.title, f"idioma {pdf_language}"))
                else:
                    print(f"      baixado via {result.source}")
                    downloaded.append(result.pdf_path)
            else:
                print(f"      bloqueado: {result.blocked_reason}")
                cand.append_pending(
                    location.pending_md,
                    title=candidate.title,
                    year=candidate.year,
                    host=result.host,
                    link=result.link,
                    reason=result.blocked_reason or "desconhecido",
                )
                pending.append((candidate.title, result.blocked_reason or ""))

            time.sleep(config.download.delay_between_seconds)

    print(f"\nBaixados: {len(downloaded)} | pendentes: {len(pending)}")

    if downloaded:
        # Mesmo pipeline da Fase 1: metadados, nomenclatura, dedupe, BibTeX.
        build_manifest(location, sorted(downloaded), config)
        print(f"Manifest de processamento: {location.path / '.process-manifest.json'}")
        print("Escreva os resumos e rode: process_materials commit")

    if pending:
        print(f"Pendências registradas em {location.pending_md}")
    return 0


def cmd_status(location: Location) -> int:
    if not location.exists():
        print(f"Localização não existe: {location}")
        return 1

    from scripts.bibtex import load_bib_file

    papers = len(list(location.papers_dir.glob("*.pdf"))) if location.papers_dir.is_dir() else 0
    summaries = (
        len(list(location.summaries_dir.glob("*.md"))) if location.summaries_dir.is_dir() else 0
    )
    entries = load_bib_file(location.references_bib)
    incomplete = sum(1 for e in entries if e.incomplete)
    materials = (
        len(list(location.materials_dir.glob("*.pdf"))) if location.materials_dir.is_dir() else 0
    )

    print(f"Localização: {location}")
    print(f"  materials/ (a processar): {materials} PDF")
    print(f"  papers/                 : {papers} PDF")
    print(f"  summaries/              : {summaries} resumos")
    print(f"  references.bib          : {len(entries)} entradas ({incomplete} INCOMPLETE)")

    total = cand.count_items(location.candidates_md)
    approved = len(cand.parse_approvals(location.candidates_md))
    if total:
        print(f"  candidates.md           : {total} itens ({approved} aprovados)")

    if (location.path / SEARCH_MANIFEST).exists():
        print("  * busca pendente de download (rode 'fetch')")
    if (location.path / ".process-manifest.json").exists():
        print("  * processamento pendente (escreva resumos e rode 'commit')")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="literature_review",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="Busca candidatos no OpenAlex")
    p_search.add_argument("location", help="area/projeto/tema")
    p_search.add_argument(
        "--query", action="append", required=True, help="String de busca (repetível)"
    )
    p_search.add_argument(
        "--type",
        dest="review_type",
        default="exploratória/narrativa",
        help="Tipo de revisão (exploratória/narrativa ou semi-sistemática)",
    )
    p_search.add_argument("--from-year", type=int)
    p_search.add_argument("--to-year", type=int)
    p_search.add_argument(
        "--precise",
        action="store_true",
        help='Busca em título+abstract com aspas e AND/OR (ex.: \'"work breakdown '
        "structure\" AND (LLM OR \"large language model\")'). Muito mais restritiva.",
    )

    p_fetch = sub.add_parser("fetch", help="Baixa apenas os candidatos aprovados")
    p_fetch.add_argument("location")

    p_status = sub.add_parser("status", help="Estado do tema")
    p_status.add_argument("location")

    args = parser.parse_args(argv)

    location = parse_location(args.location)
    if location is None:
        print(f"Localização inválida: '{args.location}'. Use area/projeto/tema.")
        return 2

    if args.command == "search":
        return cmd_search(
            location,
            args.query,
            args.review_type,
            args.from_year,
            args.to_year,
            args.precise,
        )
    if args.command == "fetch":
        return cmd_fetch(location)
    return cmd_status(location)


if __name__ == "__main__":
    raise SystemExit(main())
