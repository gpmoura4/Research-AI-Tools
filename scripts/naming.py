"""Convenção de renomeação de arquivos (ver CLAUDE.md > Convenção de renomeação).

Formato: "<Autores> - <Ano> - <Título>.pdf"
  1 autor  -> "Sobrenome"
  2 autores -> "Sobrenome1 e Sobrenome2"
  3+ autores -> "Sobrenome1 et al"
  Ano ausente -> campo omitido
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

# Caracteres inválidos em filesystem, conforme CLAUDE.md.
_INVALID_CHARS = r'[/\\:*?"<>|]'
# Controles ASCII, que quebram nomes de arquivo silenciosamente.
_CONTROL_CHARS = r"[\x00-\x1f\x7f]"


def sanitize(text: str) -> str:
    """Normaliza Unicode, remove caracteres inválidos e colapsa espaços."""
    if not text:
        return ""
    # NFC mantém acentos como um único code point — nomes estáveis entre macOS e Linux.
    text = unicodedata.normalize("NFC", text)
    # Quebras viram espaço: títulos extraídos de PDF vêm partidos em várias linhas
    # e removê-las colaria as palavras vizinhas.
    text = re.sub(r"[\r\n\t\f\v]+", " ", text)
    text = re.sub(_CONTROL_CHARS, "", text)
    # Aspas escapadas são artefato da API ("Media\'s"), não parte do título.
    text = re.sub(r"\\(?=['\"])", "", text)
    text = re.sub(_INVALID_CHARS, "-", text)
    text = re.sub(r"\s+", " ", text)
    # Pontos e espaços no fim confundem alguns filesystems.
    return text.strip().strip(".").strip()


def surname(name: str) -> str:
    """Extrai o sobrenome de um nome que pode vir completo ("Ashish Vaswani")."""
    cleaned = sanitize(name)
    if not cleaned:
        return ""
    # "Vaswani, Ashish" -> sobrenome antes da vírgula.
    if "," in cleaned:
        return cleaned.split(",")[0].strip()
    return cleaned.split()[-1]


def format_authors(authors: list[str]) -> str:
    """Formata a porção de autores a partir de uma lista de nomes ou sobrenomes."""
    surnames = [s for s in (surname(a) for a in authors) if s]
    if not surnames:
        return ""
    if len(surnames) == 1:
        return surnames[0]
    if len(surnames) == 2:
        return f"{surnames[0]} e {surnames[1]}"
    return f"{surnames[0]} et al"


def truncate_title(title: str, max_chars: int = 80) -> str:
    """Trunca no último espaço antes do limite, conforme CLAUDE.md."""
    title = sanitize(title)
    if len(title) <= max_chars:
        return title

    window = title[:max_chars]
    cut = window.rfind(" ")
    # Sem espaço no intervalo (título de palavra única): corta seco no limite.
    truncated = window[:cut] if cut > 0 else window
    return truncated.rstrip().rstrip(",;:-").rstrip()


def build_filename(
    authors: list[str],
    year: str | int | None,
    title: str,
    max_chars: int = 80,
    extension: str = ".pdf",
) -> str:
    """Monta o nome do arquivo, omitindo campos ausentes."""
    parts: list[str] = []

    author_part = format_authors(authors)
    if author_part:
        parts.append(author_part)

    if year:
        year_str = sanitize(str(year))
        if year_str:
            parts.append(year_str)

    title_part = truncate_title(title, max_chars)
    if title_part:
        parts.append(title_part)

    stem = " - ".join(parts) if parts else "Untitled"

    # Rede de segurança: a maioria dos filesystems limita o nome a 255 bytes, e o
    # sufixo de colisão ainda precisa caber. Sem isto, um campo de autores anômalo
    # derruba o pipeline com OSError.
    max_stem_bytes = 200
    while len(stem.encode("utf-8")) > max_stem_bytes:
        cut = stem.rfind(" ", 0, len(stem) - 1)
        stem = stem[:cut].rstrip() if cut > 0 else stem[: len(stem) - 1]

    return f"{stem}{extension}"


def resolve_collision(directory: Path, filename: str) -> str:
    """Sufixa ' (2)', ' (3)'... quando o nome já existe no diretório."""
    candidate = Path(filename)
    stem, suffix = candidate.stem, candidate.suffix

    if not (directory / filename).exists():
        return filename

    counter = 2
    while True:
        attempt = f"{stem} ({counter}){suffix}"
        if not (directory / attempt).exists():
            return attempt
        counter += 1
