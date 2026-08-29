"""Pipeline de processamento de PDFs depositados em materials/.

Roda em duas etapas, com um manifest JSON entre elas:

  1. extract  — lê os PDFs, resolve metadados no Crossref, decide nomes de arquivo
                e citation keys, e grava o manifest + o texto extraído.
                NADA é movido ainda.

  2. commit   — com os resumos já escritos pelo agente, renomeia e move os PDFs
                para deliverables/papers/ e atualiza o references.bib.

A separação existe por causa do G3: o resumo precisa ser escrito a partir do texto
real do paper, o que é trabalho do agente — não de um script.

Uso:
  uv run python -m scripts.process_materials list-locations
  uv run python -m scripts.process_materials extract <area>/<projeto>/<tema>
  uv run python -m scripts.process_materials commit  <area>/<projeto>/<tema>
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

from scripts import bibtex as bib
from scripts import naming, pdf_extract
from scripts.config import load_config
from scripts.crossref import CrossrefClient, CrossrefWork, title_similarity
from scripts.locations import (
    Location,
    ensure_location,
    list_all_locations,
    parse_location,
)

MANIFEST_NAME = ".process-manifest.json"
# Texto extraído fica aqui para o agente ler ao escrever os resumos.
EXTRACTED_TEXT_DIR = ".extracted-text"


@dataclass
class PaperPlan:
    """Plano de processamento de um PDF, produzido por `extract`."""

    source_file: str
    source_rel: str
    target_filename: str
    citation_key: str
    title: str
    authors: list[str]
    year: str | None
    doi: str | None
    metadata_source: str  # "crossref-doi" | "crossref-title-search" | "pdf-only"
    match_score: float | None
    incomplete: bool
    language: str | None
    summary_language: str
    text_file: str | None
    text_extraction_failed: bool
    bibtex_raw: str | None = None
    notes: list[str] = field(default_factory=list)
    status: str = "planned"  # planned | duplicate


def _resolve_metadata(
    extraction: pdf_extract.PdfExtraction, client: CrossrefClient
) -> tuple[CrossrefWork | None, str, list[str]]:
    """Tenta DOI primeiro, depois busca por título. Devolve (obra, origem, notas)."""
    notes: list[str] = []

    pdf_title = extraction.embedded_title or pdf_extract.guess_title_from_text(
        extraction.text
    )

    if extraction.doi:
        work = client.fetch_work(extraction.doi)
        if work:
            # Verificação cruzada: o DOI encontrado no PDF precisa apontar para o
            # MESMO paper que o PDF diz ser. Um DOI de bibliografia ou de carimbo
            # de journal resolve com sucesso, mas devolve outro trabalho — aceitá-lo
            # produziria metadados inteiramente trocados.
            if pdf_title and title_similarity(pdf_title, work.title) < 0.60:
                notes.append(
                    f"DOI {extraction.doi} encontrado no PDF resolve para "
                    f"'{work.title}', que não corresponde ao título do documento "
                    f"('{pdf_title}'). DOI descartado — provavelmente veio das "
                    f"referências."
                )
                # O DOI é de outro trabalho: não pode entrar no references.bib.
                extraction.doi = None
            else:
                return work, "crossref-doi", notes
        else:
            notes.append(
                f"DOI {extraction.doi} encontrado no PDF mas não resolvido no Crossref."
            )

    # Sem DOI (ou DOI inválido/descartado): tenta pelo título.
    title_guess = pdf_title
    if title_guess:
        author_hint: list[str] = []
        if extraction.embedded_author:
            author_hint = [extraction.embedded_author]
        work = client.search_by_title(title_guess, author_hint)
        if work:
            notes.append(
                f"Sem DOI no PDF; correspondência por título "
                f"(score {work.match_score}) — confira antes de citar."
            )
            return work, "crossref-title-search", notes
        notes.append(
            "Sem DOI e sem correspondência confiável no Crossref; entrada marcada "
            "como INCOMPLETE."
        )
    else:
        notes.append("Não foi possível determinar o título a partir do PDF.")

    return None, "pdf-only", notes


def _plan_paper(
    pdf_path: Path,
    location: Location,
    client: CrossrefClient,
    used_keys: set[str],
    used_filenames: set[str],
    text_dir: Path,
    config,
) -> PaperPlan:
    extraction = pdf_extract.extract(pdf_path)
    work, source, notes = _resolve_metadata(extraction, client)

    if work is not None:
        title = work.title
        authors = work.authors
        year = work.year
        doi = work.doi
        bibtex_raw = work.bibtex
        incomplete = bibtex_raw is None
        if incomplete:
            notes.append("Crossref não devolveu BibTeX; entrada montada dos metadados.")
        match_score = work.match_score if source == "crossref-title-search" else None
    else:
        # Só o que o PDF realmente forneceu — sem preencher lacunas por conta própria.
        title = (
            extraction.embedded_title
            or pdf_extract.guess_title_from_text(extraction.text)
            or pdf_path.stem
        )
        # Metadados embutidos separam autores por ';' ou ',' conforme o produtor
        # do PDF; dividir só por vírgula transforma a lista inteira num único nome.
        authors = (
            [a.strip() for a in re.split(r"[;,]", extraction.embedded_author) if a.strip()]
            if extraction.embedded_author
            else []
        )
        year = extraction.year_candidates[0] if extraction.year_candidates else None
        if not year:
            # Último recurso: o ano no nome do arquivo dado pelo usuário. É uma
            # evidência mais fraca que o texto do PDF, por isso fica registrada
            # em nota para conferência.
            from_name = re.search(r"\b(19[5-9]\d|20[0-4]\d)\b", pdf_path.stem)
            if from_name:
                year = from_name.group(1)
                notes.append(
                    f"Ano {year} veio do nome do arquivo, não do texto do PDF — confira."
                )
        doi = extraction.doi
        bibtex_raw = None
        incomplete = True
        match_score = None

    # G6: inglês por padrão; português apenas se o paper original for em português.
    summary_language = "pt" if extraction.language == "pt" else config.default_summary_language

    if extraction.text_extraction_failed:
        notes.append(
            "Texto não pôde ser extraído do PDF (possível PDF escaneado sem OCR). "
            "O resumo deve declarar explicitamente essa limitação (G3)."
        )

    filename = naming.build_filename(
        authors=authors, year=year, title=title, max_chars=config.title_max_chars
    )
    # Evita colisão tanto no disco quanto dentro do próprio lote.
    filename = naming.resolve_collision(location.papers_dir, filename)
    while filename in used_filenames:
        stem, suffix = Path(filename).stem, Path(filename).suffix
        counter = 2
        base = stem
        while f"{base} ({counter}){suffix}" in used_filenames:
            counter += 1
        filename = f"{base} ({counter}){suffix}"
    used_filenames.add(filename)

    citation_key = bib.make_citation_key(authors, year, title, used_keys)
    if bibtex_raw:
        parsed = bib.parse_bibtex_string(bibtex_raw)
        if parsed:
            citation_key = (
                parsed.key if parsed.key not in used_keys else citation_key
            )
    used_keys.add(citation_key)

    text_file: str | None = None
    if extraction.text.strip():
        text_dir.mkdir(parents=True, exist_ok=True)
        text_path = text_dir / f"{Path(filename).stem}.txt"
        text_path.write_text(extraction.text, encoding="utf-8")
        text_file = str(text_path.relative_to(location.path))

    return PaperPlan(
        source_file=pdf_path.name,
        # Caminho relativo ao tema: o PDF pode vir de materials/ (depósito manual)
        # ou de .downloads/ (baixado pela revisão de literatura). Guardar só o nome
        # faria o commit procurar sempre em materials/ e não achar os baixados.
        source_rel=str(pdf_path.resolve().relative_to(location.path.resolve())),
        target_filename=filename,
        citation_key=citation_key,
        title=title,
        authors=authors,
        year=year,
        doi=doi,
        metadata_source=source,
        match_score=match_score,
        incomplete=incomplete,
        language=extraction.language,
        summary_language=summary_language,
        text_file=text_file,
        text_extraction_failed=extraction.text_extraction_failed,
        bibtex_raw=bibtex_raw,
        notes=notes,
    )


def build_manifest(
    location: Location, pdfs: list[Path], config, skipped: list[Path] | None = None
) -> Path:
    """Planeja o processamento de uma lista de PDFs e grava o manifest.

    Compartilhada pelo /process-materials (PDFs de materials/) e pelo
    /literature-review (PDFs recém-baixados), para que ambos passem exatamente
    pelo mesmo pipeline de metadados, nomenclatura e dedupe.
    """
    existing_entries = bib.load_bib_file(location.references_bib)
    used_keys = {e.key for e in existing_entries}
    used_filenames: set[str] = set()
    text_dir = location.path / EXTRACTED_TEXT_DIR

    plans: list[PaperPlan] = []
    with CrossrefClient(config) as client:
        for pdf in pdfs:
            print(f"  processando: {pdf.name}", file=sys.stderr)
            plan = _plan_paper(
                pdf, location, client, used_keys, used_filenames, text_dir, config
            )

            # Dedupe contra o que já está no references.bib.
            probe = bib.BibEntry(
                key=plan.citation_key,
                entry_type="article",
                fields={"doi": plan.doi or "", "title": plan.title},
            )
            duplicate = bib.find_duplicate(probe, existing_entries)
            if duplicate is not None:
                plan.status = "duplicate"
                plan.citation_key = duplicate.key
                plan.notes.append(
                    f"Já presente em references.bib como '{duplicate.key}'. "
                    "Modo incremental: não será reprocessado."
                )
            plans.append(plan)

    manifest = {
        "location": str(location),
        "papers": [asdict(p) for p in plans],
        "skipped_over_limit": [p.name for p in (skipped or [])],
        "max_papers_per_run": config.max_papers_per_run,
    }
    manifest_path = location.path / MANIFEST_NAME
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return manifest_path


def cmd_extract(location: Location) -> int:
    config = load_config()
    ensure_location(location)

    pdfs = sorted(p for p in location.materials_dir.glob("*.pdf") if p.is_file())
    if not pdfs:
        print(f"Nenhum PDF em {location.materials_dir}")
        return 1

    # G5 — limite por passada.
    limit = config.max_papers_per_run
    skipped = pdfs[limit:]
    pdfs = pdfs[:limit]

    manifest_path = build_manifest(location, pdfs, config, skipped)
    papers = json.loads(manifest_path.read_text(encoding="utf-8"))["papers"]

    new_count = sum(1 for p in papers if p["status"] == "planned")
    print(f"\nManifest: {manifest_path}")
    print(f"Papers planejados: {new_count} | duplicados: {len(papers) - new_count}")
    if skipped:
        print(f"Fora do limite de {limit} nesta passada: {len(skipped)}")
    return 0


def cmd_commit(location: Location) -> int:
    manifest_path = location.path / MANIFEST_NAME
    if not manifest_path.exists():
        print(f"Manifest não encontrado: {manifest_path}. Rode 'extract' antes.")
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    papers = manifest.get("papers", [])

    moved = 0
    bib_added = 0
    missing_summaries: list[str] = []

    for record in papers:
        if record.get("status") == "duplicate":
            continue

        target_name = record["target_filename"]
        summary_path = location.summaries_dir / f"{Path(target_name).stem}.md"
        if not summary_path.exists():
            missing_summaries.append(target_name)
            continue

        # Entrada BibTeX: do Crossref quando houver, senão INCOMPLETE (G1).
        entry = None
        if record.get("bibtex_raw"):
            entry = bib.parse_bibtex_string(record["bibtex_raw"])
            if entry:
                entry.key = record["citation_key"]
            else:
                # Degradar para INCOMPLETE em silêncio esconde uma entrada boa que
                # se perdeu por falha de parsing — o usuário precisa saber.
                print(
                    f"  ! BibTeX do Crossref não pôde ser interpretado para "
                    f"'{target_name[:50]}'; entrada gravada como INCOMPLETE."
                )
        if entry is None:
            entry = bib.make_incomplete_entry(
                key=record["citation_key"],
                authors=record.get("authors") or [],
                year=record.get("year"),
                title=record.get("title") or "",
                extra_fields={"doi": record.get("doi") or ""},
            )

        _, added = bib.upsert_entry(location.references_bib, entry)
        if added:
            bib_added += 1

        # Manifests antigos não têm source_rel; materials/ é o fallback.
        source = location.path / record.get(
            "source_rel", f"materials/{record['source_file']}"
        )
        destination = location.papers_dir / target_name
        if source.exists() and not destination.exists():
            shutil.move(str(source), str(destination))
            moved += 1

    print(f"PDFs movidos para papers/: {moved}")
    print(f"Entradas adicionadas ao references.bib: {bib_added}")
    if missing_summaries:
        print("\nSem resumo — não processados:")
        for name in missing_summaries:
            print(f"  - {name}")
        return 1

    manifest_path.unlink(missing_ok=True)
    text_dir = location.path / EXTRACTED_TEXT_DIR
    if text_dir.exists():
        shutil.rmtree(text_dir)

    # Área de staging da revisão de literatura: depois que os PDFs foram movidos
    # para papers/, o que sobra ali é lixo de execução.
    downloads_dir = location.path / ".downloads"
    if downloads_dir.exists() and not any(downloads_dir.iterdir()):
        downloads_dir.rmdir()
    return 0


def cmd_list_locations() -> int:
    locations = list_all_locations()
    if not locations:
        print("Nenhuma localização em areas/.")
        return 0
    for location in locations:
        pdf_count = (
            len(list(location.materials_dir.glob("*.pdf")))
            if location.materials_dir.is_dir()
            else 0
        )
        print(f"{location}  (materials: {pdf_count} PDF)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="process_materials", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = parser.add_subparsers(dest="command", required=True)

    for name, help_text in (
        ("extract", "Lê os PDFs de materials/ e gera o manifest"),
        ("commit", "Move os PDFs e atualiza o references.bib"),
    ):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("location", help="area/projeto/tema")

    sub.add_parser("list-locations", help="Lista as localizações existentes")

    args = parser.parse_args(argv)

    if args.command == "list-locations":
        return cmd_list_locations()

    location = parse_location(args.location)
    if location is None:
        print(f"Localização inválida: '{args.location}'. Use area/projeto/tema.")
        return 2

    if args.command == "extract":
        return cmd_extract(location)
    return cmd_commit(location)


if __name__ == "__main__":
    raise SystemExit(main())
