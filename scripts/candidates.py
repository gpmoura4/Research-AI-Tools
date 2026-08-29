"""Escrita e leitura de candidates.md, dedupe e registro de pendências.

O candidates.md é o ponto de aprovação humana (G4): o usuário marca item a item,
e só o que estiver marcado é baixado.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from scripts.bibtex import load_bib_file
from scripts.crossref import normalize_title
from scripts.openalex import Candidate, summarize_abstract

# "## [x] 3. Título do paper" — o marcador é a aprovação.
_ITEM_RE = re.compile(r"^##\s*\[([ xX])\]\s*(\d+)\.\s*(.+?)\s*$", re.MULTILINE)
_FIELD_RE = re.compile(r"^-\s*\*\*(.+?)\*\*:\s*(.*)$", re.MULTILINE)


@dataclass
class ApprovedItem:
    """Item marcado pelo usuário em candidates.md."""

    number: int
    title: str
    doi: str | None
    pdf_url: str | None
    landing_page_url: str | None
    host: str | None
    year: int | None
    authors: list[str]
    oa_status: str | None


def detect_language(text: str) -> str | None:
    """Detecta o idioma de um texto curto (título + abstract)."""
    sample = (text or "").strip()
    if len(sample) < 60:
        return None
    try:
        from langdetect import DetectorFactory, detect

        DetectorFactory.seed = 0
        return detect(sample[:2000])
    except Exception:
        return None


def filter_by_language(
    candidates: list[Candidate], accepted: tuple[str, ...]
) -> tuple[list[Candidate], list[tuple[Candidate, str]]]:
    """G7 — mantém apenas candidatos nos idiomas que o usuário lê.

    O campo `language` do OpenAlex vem vazio em parte dos registros; nesses casos
    detectamos pelo título + abstract. Um item cujo idioma não pôde ser
    determinado é MANTIDO: descartar por falta de metadado esconderia trabalho
    relevante, e o usuário ainda decide item a item.
    """
    kept: list[Candidate] = []
    rejected: list[tuple[Candidate, str]] = []

    for candidate in candidates:
        language = (candidate.language or "").lower()[:2] or None
        source = "metadado"

        if not language:
            language = detect_language(f"{candidate.title}. {candidate.abstract or ''}")
            source = "detectado no texto"

        if language and language not in accepted:
            rejected.append((candidate, f"{language} ({source})"))
            continue

        kept.append(candidate)

    return kept, rejected


def existing_corpus_keys(references_bib: Path) -> tuple[set[str], set[str]]:
    """DOIs e títulos normalizados já presentes no tema, para dedupe."""
    dois: set[str] = set()
    titles: set[str] = set()
    for entry in load_bib_file(references_bib):
        if entry.doi:
            dois.add(entry.doi.lower())
        if entry.title:
            titles.add(normalize_title(entry.title))
    return dois, titles


def dedupe_candidates(
    candidates: list[Candidate], references_bib: Path
) -> tuple[list[Candidate], list[Candidate]]:
    """Separa candidatos novos dos já presentes no corpus do tema.

    Dedupe por DOI (primário) e título normalizado (fallback), incluindo
    duplicatas dentro do próprio lote — a mesma obra aparece em várias buscas.
    """
    known_dois, known_titles = existing_corpus_keys(references_bib)

    fresh: list[Candidate] = []
    duplicates: list[Candidate] = []
    # Aponta para o candidato já aceito, para reaproveitar o melhor sinal quando a
    # mesma obra reaparece em outra string de busca.
    seen: dict[str, Candidate] = {}

    for candidate in candidates:
        doi = (candidate.doi or "").lower()
        title_key = normalize_title(candidate.title)

        if doi and doi in known_dois:
            candidate.duplicate_of = "corpus (DOI)"
        elif title_key and title_key in known_titles:
            candidate.duplicate_of = "corpus (título)"
        elif doi and doi in seen:
            candidate.duplicate_of = "lote (DOI)"
        elif title_key and title_key in seen:
            candidate.duplicate_of = "lote (título)"

        if candidate.duplicate_of:
            duplicates.append(candidate)
            # Uma obra encontrada por várias buscas é sinal de aderência ao tema:
            # guardamos o maior score e registramos todas as queries que a acharam.
            original = seen.get(doi) or seen.get(title_key)
            if original is not None:
                original.relevance_score = max(
                    original.relevance_score, candidate.relevance_score
                )
                for query in candidate.queries:
                    if query not in original.queries:
                        original.queries.append(query)
            continue

        if doi:
            seen[doi] = candidate
        if title_key:
            seen[title_key] = candidate
        fresh.append(candidate)

    return fresh, duplicates


def _format_authors(authors: list[str], limit: int = 3) -> str:
    if not authors:
        return "(sem autores na API)"
    shown = ", ".join(authors[:limit])
    return f"{shown} et al." if len(authors) > limit else shown


def write_candidates_md(
    path: Path,
    candidates: list[Candidate],
    location: str,
    queries: list[str],
    review_type: str,
    duplicates_skipped: int = 0,
) -> None:
    """Escreve candidates.md com um checkbox por item (aprovação item a item)."""
    lines: list[str] = [
        "# Candidatos",
        "",
        f"- **Localização**: {location}",
        f"- **Tipo de revisão**: {review_type}",
        f"- **Data da busca**: {date.today().isoformat()}",
        f"- **Fonte**: OpenAlex",
        f"- **Itens**: {len(candidates)}"
        + (f" (— {duplicates_skipped} já no corpus/duplicados)" if duplicates_skipped else ""),
        "",
        "## Strings de busca usadas",
        "",
    ]
    lines += [f"- `{q}`" for q in queries]
    lines += [
        "",
        "---",
        "",
        "## Como aprovar",
        "",
        "Marque `[x]` nos itens que quer baixar e salve o arquivo. Depois rode o passo",
        "de download. **Apenas os itens marcados serão baixados** — nada é baixado sem",
        "aprovação explícita. Itens sem PDF open access vão para `pending.md`.",
        "",
        "---",
        "",
    ]

    for index, candidate in enumerate(candidates, start=1):
        score = f"{candidate.score}/10" if candidate.score is not None else "—"
        oa = (
            f"open access ({candidate.oa_status})"
            if candidate.is_oa
            else f"fechado ({candidate.oa_status or 'desconhecido'})"
        )

        lines.append(f"## [ ] {index}. {candidate.title}")
        lines.append("")
        lines.append(
            f"- **Autores**: {_format_authors(candidate.authors)} · "
            f"**Ano**: {candidate.year or '—'} · "
            f"**Venue**: {candidate.venue or '—'}"
        )
        lines.append(
            f"- **Score**: {score}"
            + (f" — {candidate.score_reason}" if candidate.score_reason else "")
        )
        lines.append(f"- **Acesso**: {oa} · **Citações**: {candidate.cited_by_count}")
        lines.append(f"- **DOI**: {candidate.doi or '—'}")
        lines.append(f"- **Link**: {candidate.best_link or '—'}")
        if candidate.pdf_url:
            lines.append(f"- **PDF**: {candidate.pdf_url}")
        lines.append(f"- **Host**: {candidate.host_platform or '—'}")
        if len(candidate.queries) > 1:
            lines.append(f"- **Encontrado por**: {len(candidate.queries)} strings de busca")
        lines.append(f"- **Abstract**: {summarize_abstract(candidate.abstract)}")
        lines.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_approvals(path: Path) -> list[ApprovedItem]:
    """Lê candidates.md e devolve apenas os itens marcados com [x] (G4)."""
    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8")
    matches = list(_ITEM_RE.finditer(text))

    approved: list[ApprovedItem] = []
    for position, match in enumerate(matches):
        checked = match.group(1).lower() == "x"
        if not checked:
            continue

        number = int(match.group(2))
        title = match.group(3).strip()

        # Bloco de campos até o próximo item.
        start = match.end()
        end = matches[position + 1].start() if position + 1 < len(matches) else len(text)
        fields = {
            key.strip().lower(): value.strip()
            for key, value in _FIELD_RE.findall(text[start:end])
        }

        def clean(value: str | None) -> str | None:
            if not value or value.strip() in {"—", "-", ""}:
                return None
            return value.strip()

        year_raw = (fields.get("autores") or "").split("**Ano**:")
        year: int | None = None
        if len(year_raw) > 1:
            digits = re.search(r"\b(1[89]\d{2}|20\d{2})\b", year_raw[1])
            if digits:
                year = int(digits.group(1))

        approved.append(
            ApprovedItem(
                number=number,
                title=title,
                doi=clean(fields.get("doi")),
                pdf_url=clean(fields.get("pdf")),
                landing_page_url=clean(fields.get("link")),
                host=clean(fields.get("host")),
                year=year,
                authors=[],
                oa_status=clean(fields.get("acesso")),
            )
        )
    return approved


def count_items(path: Path) -> int:
    if not path.exists():
        return 0
    return len(_ITEM_RE.findall(path.read_text(encoding="utf-8")))


PENDING_HEADER = """# Pendências

Papers aprovados cujo PDF não pôde ser obtido por vias open access.
**Cabe revisão manual** — acesse pela plataforma hospedeira, se tiver acesso
institucional, e deposite o PDF em `materials/`.

| Paper | Ano | Host | Link | Motivo | Status |
|---|---|---|---|---|---|
"""


def append_pending(
    path: Path, title: str, year: int | None, host: str | None, link: str | None, reason: str
) -> bool:
    """Registra uma pendência, sem duplicar entrada já existente."""
    if not path.exists() or not path.read_text(encoding="utf-8").strip():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(PENDING_HEADER, encoding="utf-8")

    current = path.read_text(encoding="utf-8")
    # Pipes quebrariam a tabela markdown.
    safe_title = title.replace("|", "/").strip()
    if safe_title in current:
        return False

    row = (
        f"| {safe_title} "
        f"| {year or '—'} "
        f"| {(host or '—').replace('|', '/')} "
        f"| {link or '—'} "
        f"| {reason.replace('|', '/')} "
        f"| pendente — cabe revisão manual |\n"
    )
    path.write_text(current.rstrip("\n") + "\n" + row, encoding="utf-8")
    return True
