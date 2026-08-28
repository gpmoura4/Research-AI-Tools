"""Leitura, merge e escrita do references.bib do tema.

Dedupe por DOI (primário) e título normalizado (fallback), conforme CLAUDE.md.
Cada references.bib é autossuficiente para uso direto no Overleaf.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter

from scripts.crossref import normalize_title
from scripts.naming import surname

INCOMPLETE_MARKER = "% INCOMPLETE - verificar manualmente"
# Campo interno que persiste o estado incompleto entre execuções. BibTeX ignora
# campos desconhecidos, então isto não afeta a compilação no Overleaf.
INCOMPLETE_FIELD = "x-incomplete"

_BIB_HEADER = """%% references.bib — gerado pelo research workspace.
%% Entradas vêm do Crossref (via DOI ou busca verificada) ou de metadados
%% extraídos do PDF. Entradas marcadas com "{marker}" precisam de conferência.
""".format(marker=INCOMPLETE_MARKER.lstrip("% "))


@dataclass
class BibEntry:
    key: str
    entry_type: str
    fields: dict[str, str]
    incomplete: bool = False

    @property
    def doi(self) -> str | None:
        doi = self.fields.get("doi", "").strip().lower()
        return doi or None

    @property
    def title(self) -> str:
        return self.fields.get("title", "").strip()


def _ascii_slug(text: str) -> str:
    """Reduz a ASCII alfanumérico — citation keys precisam ser seguras no LaTeX."""
    normalized = unicodedata.normalize("NFKD", text or "")
    stripped = "".join(c for c in normalized if not unicodedata.combining(c))
    return re.sub(r"[^A-Za-z0-9]", "", stripped)


def make_citation_key(
    authors: list[str], year: str | None, title: str, existing: set[str] | None = None
) -> str:
    """Gera 'sobrenomeANOprimeirapalavra', desambiguando com sufixo de letra."""
    existing = existing or set()

    # Só o sobrenome: a lista pode trazer nomes completos ("Xiaomin Li") ou
    # invertidos ("Li, Xiaomin"), e a key precisa ser a mesma nos dois casos.
    author_part = _ascii_slug(surname(authors[0])).lower() if authors else "unknown"
    year_part = _ascii_slug(str(year)) if year else "nodate"

    title_word = ""
    for word in normalize_title(title).split():
        # Ignora artigos e preposições iniciais, que não distinguem nada.
        if word not in {"a", "an", "the", "on", "of", "in", "for", "and", "to"}:
            title_word = _ascii_slug(word).lower()
            break

    base = f"{author_part}{year_part}{title_word}" or "entry"

    if base not in existing:
        return base
    for suffix in "abcdefghijklmnopqrstuvwxyz":
        candidate = f"{base}{suffix}"
        if candidate not in existing:
            return candidate
    counter = 2
    while f"{base}{counter}" in existing:
        counter += 1
    return f"{base}{counter}"


def parse_bibtex_string(raw: str) -> BibEntry | None:
    """Converte um BibTeX bruto (ex.: vindo do Crossref) em BibEntry."""
    if not raw or not raw.strip().startswith("@"):
        return None
    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    try:
        db = bibtexparser.loads(raw, parser=parser)
    except Exception:
        return None
    if not db.entries:
        return None

    entry = db.entries[0]
    entry_type = entry.pop("ENTRYTYPE", "article")
    key = entry.pop("ID", "entry")
    return BibEntry(key=key, entry_type=entry_type, fields=entry)


def load_bib_file(path: Path) -> list[BibEntry]:
    """Lê um references.bib existente. Arquivo ausente ou vazio => lista vazia."""
    if not path.exists():
        return []
    raw = path.read_text(encoding="utf-8")
    if not raw.strip():
        return []

    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    try:
        db = bibtexparser.loads(raw, parser=parser)
    except Exception:
        return []

    entries: list[BibEntry] = []
    for entry in db.entries:
        fields = dict(entry)
        entry_type = fields.pop("ENTRYTYPE", "article")
        key = fields.pop("ID", "entry")
        # O estado incompleto viaja num campo da própria entrada, não num comentário
        # solto: comentários não sobrevivem ao round-trip do parser, e inferi-los
        # pela posição no texto produz falso positivo.
        incomplete = fields.pop(INCOMPLETE_FIELD, "").strip().lower() == "true"
        entries.append(
            BibEntry(key=key, entry_type=entry_type, fields=fields, incomplete=incomplete)
        )
    return entries


def find_duplicate(entry: BibEntry, existing: list[BibEntry]) -> BibEntry | None:
    """Dedupe: DOI primário, título normalizado como fallback."""
    if entry.doi:
        for candidate in existing:
            if candidate.doi and candidate.doi == entry.doi:
                return candidate

    normalized = normalize_title(entry.title)
    if normalized:
        for candidate in existing:
            if normalize_title(candidate.title) == normalized:
                return candidate
    return None


def make_incomplete_entry(
    key: str,
    authors: list[str],
    year: str | None,
    title: str,
    extra_fields: dict[str, str] | None = None,
) -> BibEntry:
    """Entrada mínima quando não há DOI nem correspondência confiável (G1).

    Campos desconhecidos ficam vazios de propósito: um vazio é honesto, um
    palpite não é.
    """
    fields: dict[str, str] = {
        "title": title or "",
        "author": " and ".join(authors) if authors else "",
        "year": str(year) if year else "",
        "journal": "",
    }
    if extra_fields:
        fields.update({k: v for k, v in extra_fields.items() if v})

    return BibEntry(key=key, entry_type="article", fields=fields, incomplete=True)


def _format_entry(entry: BibEntry) -> str:
    db = bibtexparser.bibdatabase.BibDatabase()
    record = dict(entry.fields)
    record.pop(INCOMPLETE_FIELD, None)
    if entry.incomplete:
        record[INCOMPLETE_FIELD] = "true"
    record["ENTRYTYPE"] = entry.entry_type
    record["ID"] = entry.key
    db.entries = [record]

    writer = BibTexWriter()
    writer.indent = "  "
    writer.order_entries_by = None
    text = writer.write(db).strip()

    if entry.incomplete:
        return f"{INCOMPLETE_MARKER}\n{text}"
    return text


def write_bib_file(path: Path, entries: list[BibEntry]) -> None:
    """Reescreve o arquivo inteiro, preservando a ordem das entradas."""
    path.parent.mkdir(parents=True, exist_ok=True)
    body = "\n\n".join(_format_entry(e) for e in entries)
    path.write_text(f"{_BIB_HEADER}\n{body}\n" if body else _BIB_HEADER, encoding="utf-8")


def upsert_entry(path: Path, entry: BibEntry) -> tuple[BibEntry, bool]:
    """Insere a entrada se nova. Devolve (entrada_efetiva, foi_adicionada).

    Modo incremental: uma entrada já existente é preservada como está.
    """
    existing = load_bib_file(path)

    duplicate = find_duplicate(entry, existing)
    if duplicate is not None:
        return duplicate, False

    used_keys = {e.key for e in existing}
    if entry.key in used_keys:
        entry.key = make_citation_key(
            [entry.fields.get("author", "").split(" and ")[0]],
            entry.fields.get("year"),
            entry.title,
            used_keys,
        )

    existing.append(entry)
    write_bib_file(path, existing)
    return entry, True
