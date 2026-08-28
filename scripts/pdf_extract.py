"""Extração de texto e metadados de PDFs.

Tudo aqui é evidência verificável: só reportamos o que o arquivo realmente contém.
Nada é inferido pelo modelo (G1/G3).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import pymupdf

# DOIs conforme o padrão Crossref, tolerando ruído de extração ao redor.
_DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:a-z0-9A-Z]+\b")
# Anos plausíveis para publicação acadêmica.
_YEAR_RE = re.compile(r"\b(19[5-9]\d|20[0-4]\d)\b")


@dataclass
class PdfExtraction:
    source_path: Path
    text: str
    page_count: int
    # Metadados embutidos no PDF (frequentemente vazios ou errados — daí serem
    # apenas pistas, sempre confirmadas no Crossref quando possível).
    embedded_title: str | None = None
    embedded_author: str | None = None
    doi: str | None = None
    year_candidates: list[str] = field(default_factory=list)
    text_extraction_failed: bool = False
    language: str | None = None

    @property
    def first_page_text(self) -> str:
        return self.text[:3000]


def _clean_doi(raw: str) -> str:
    """Remove pontuação de fim de frase que o regex captura junto."""
    doi = raw.strip()
    while doi and doi[-1] in ".,;:)]}>":
        doi = doi[:-1]
    return doi


# Início da bibliografia: daqui em diante todo DOI pertence a OUTRO paper.
_REFERENCES_HEADING_RE = re.compile(
    r"^\s*(?:\d+\s*\.?\s*)?(references|bibliography|works cited|referências|"
    r"referencias|bibliografia|literatura citada)\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def strip_references_section(text: str) -> str:
    """Corta o texto no início da bibliografia."""
    match = _REFERENCES_HEADING_RE.search(text)
    return text[: match.start()] if match else text


def find_doi(text: str, header_chars: int = 4000) -> str | None:
    """DOI do PRÓPRIO paper: só o cabeçalho, nunca a bibliografia.

    O DOI de um paper aparece na primeira página (rodapé, cabeçalho ou bloco de
    identificação). Varrer o documento inteiro captura o primeiro DOI da lista de
    referências — que é de outro trabalho — e leva a metadados completamente
    trocados.
    """
    head = strip_references_section(text)[:header_chars]
    for match in _DOI_RE.finditer(head):
        doi = _clean_doi(match.group(0))
        # DOIs reais têm sufixo com substância; descarta fragmentos.
        if len(doi) > 10:
            return doi
    return None


def detect_language(text: str) -> str | None:
    """Detecta o idioma do corpo do texto — serve o G6 por evidência, não por chute."""
    sample = text.strip()
    if len(sample) < 200:
        return None
    try:
        from langdetect import DetectorFactory, detect

        # Torna a detecção determinística entre execuções.
        DetectorFactory.seed = 0
        return detect(sample[:5000])
    except Exception:
        return None


def extract(pdf_path: Path, max_pages: int = 12) -> PdfExtraction:
    """Extrai texto e pistas de metadados. Nunca levanta exceção por PDF ruim."""
    path = Path(pdf_path)

    try:
        with pymupdf.open(path) as doc:
            page_count = doc.page_count
            meta = doc.metadata or {}
            pages = [doc[i].get_text() for i in range(min(page_count, max_pages))]
            text = "\n".join(pages)
            # Layout da primeira página: o tamanho da fonte identifica o título com
            # muito mais confiabilidade do que o comprimento das linhas.
            layout_title = (
                _title_from_layout(doc[0]) if page_count and doc[0] else None
            )
    except Exception:
        # PDF corrompido ou protegido: devolve um objeto marcado, o pipeline decide.
        return PdfExtraction(
            source_path=path,
            text="",
            page_count=0,
            text_extraction_failed=True,
        )

    # PDF só de imagens (escaneado sem OCR) rende quase nada de texto.
    stripped = text.strip()
    failed = len(stripped) < 100

    # Metadados embutidos costumam vir vazios (arXiv, LaTeX) ou com lixo do editor;
    # o layout da primeira página é a fonte mais confiável.
    embedded_title = (meta.get("title") or "").strip() or None
    if not _plausible_title(embedded_title):
        embedded_title = layout_title

    embedded_author = (meta.get("author") or "").strip() or None
    head = pages[0] if pages else ""
    if not embedded_author:
        found = _authors_from_text(head, embedded_title)
        # ';' separa sem ambiguidade: uma vírgula pode fazer parte do próprio nome
        # ("Vaswani, Ashish"), e dividir por ela quebraria o autor em dois.
        embedded_author = "; ".join(found) if found else None

    # Anos só da primeira página: no corpo, aparecem as datas das referências.
    years = sorted(set(_YEAR_RE.findall(head)), reverse=True)

    return PdfExtraction(
        source_path=path,
        text=text,
        page_count=page_count,
        embedded_title=embedded_title,
        embedded_author=embedded_author,
        doi=find_doi(text),
        year_candidates=years,
        text_extraction_failed=failed,
        language=detect_language(stripped),
    )


# Carimbos de repositório de preprint: "arXiv:1706.03762v7 [cs.CL] 2 Aug 2023",
# "bioRxiv preprint doi: ...", "Preprint. Under review."
_PREPRINT_STAMP_RE = re.compile(
    r"^\s*(arxiv:|biorxiv|medrxiv|ssrn|preprint\b|submitted to\b|under review\b|"
    r"to appear in\b|accepted at\b|proceedings of\b)",
    re.IGNORECASE,
)


def _is_preprint_stamp(text: str) -> bool:
    return bool(_PREPRINT_STAMP_RE.match(text.strip()))


def _plausible_title(title: str | None) -> bool:
    """Descarta títulos de metadado que são nome de arquivo ou lixo do editor."""
    if not title or len(title.strip()) < 8:
        return False
    lowered = title.strip().lower()
    if lowered.endswith((".pdf", ".doc", ".docx", ".tex", ".dvi", ".ps")):
        return False
    if _is_preprint_stamp(title):
        return False
    return "untitled" not in lowered and "microsoft word" not in lowered


def _title_from_layout(page: "pymupdf.Page") -> str | None:
    """Título = maior tamanho de fonte no terço superior da primeira página.

    Reúne as linhas consecutivas nesse tamanho, o que reconstrói títulos quebrados
    em várias linhas ("BERT: ... Transformers for" + "Language Understanding").
    """
    try:
        blocks = page.get_text("dict")["blocks"]
    except Exception:
        return None

    lines: list[tuple[float, float, str]] = []  # (tamanho, y, texto)
    page_height = page.rect.height or 1

    for block in blocks:
        for line in block.get("lines", []):
            # Carimbos laterais de preprint (arXiv) são rotacionados e usam fonte
            # grande — descartamos tudo que não estiver na horizontal.
            direction = line.get("dir", (1, 0))
            if abs(direction[0]) < 0.99:
                continue

            spans = line.get("spans", [])
            text = "".join(s.get("text", "") for s in spans).strip()
            if not text or _is_preprint_stamp(text):
                continue
            max_size = max((s.get("size", 0) for s in spans), default=0)
            y = line.get("bbox", [0, 0, 0, 0])[1]
            # Só o topo da página: evita capturar títulos de seção do corpo.
            if y < page_height * 0.45:
                lines.append((round(max_size, 1), y, text))

    if not lines:
        return None

    biggest = max(size for size, _, _ in lines)
    # Boilerplate de copyright às vezes divide o maior tamanho com o título;
    # ficamos com o bloco contíguo mais longo nesse tamanho.
    title_lines = [(y, t) for size, y, t in lines if size == biggest]
    title_lines.sort()

    parts = [t for _, t in title_lines]
    title = " ".join(parts).strip()
    title = re.sub(r"\s+", " ", title)

    if not _plausible_title(title) or len(title) > 300:
        return None
    return title


# Nome próprio: "Ashish Vaswani", "Ming-Wei Chang", "J. R. Silva", "Kristina Toutanova".
_AUTHOR_LINE_RE = re.compile(
    r"^[A-ZÀ-Þ][\w'’.-]*(?:\s+[A-ZÀ-Þ][\w'’.-]*){1,4}$", re.UNICODE
)
_AFFILIATION_HINTS = (
    "university",
    "universidade",
    "institute",
    "instituto",
    "department",
    "departamento",
    "college",
    "school",
    "laborator",
    "research",
    "google",
    "microsoft",
    "abstract",
    "keywords",
)


def _authors_from_text(head: str, title: str | None) -> list[str]:
    """Sobrenomes das linhas de autoria, entre o título e o abstract.

    Conservador de propósito: uma lista vazia leva a uma entrada INCOMPLETE, que é
    um resultado honesto — inventar autores não é (G1).
    """
    lines = [ln.strip() for ln in head.split("\n")]

    # Começa depois da ÚLTIMA linha do título: títulos quebram em várias linhas e
    # cortar pela primeira deixaria a continuação ("Language Understanding") ser
    # confundida com um nome de autor.
    start = 0
    if title:
        title_words = {w.lower().strip(":,.") for w in title.split() if len(w) > 3}
        seen_title = False
        for i, line in enumerate(lines[:40]):
            line_words = {w.lower().strip(":,.") for w in line.split() if len(w) > 3}
            overlaps = bool(line_words) and len(line_words & title_words) >= max(
                1, len(line_words) // 2
            )
            if overlaps:
                # Linhas do título são contíguas; avança enquanto elas durarem.
                start = i + 1
                seen_title = True
            elif seen_title and line.strip():
                # Primeira linha de conteúdo após o título: daqui vêm os autores.
                break

    surnames: list[str] = []
    for line in lines[start : start + 25]:
        lowered = line.lower()
        if lowered.startswith(("abstract", "resumo", "keywords", "palavras")):
            break
        if not line or "@" in line or any(h in lowered for h in _AFFILIATION_HINTS):
            continue

        # Marcas de nota de rodapé grudadas no nome.
        cleaned = re.sub(r"[∗*†‡§¶0-9]+", "", line).strip().rstrip(",;")
        # Uma linha pode listar vários autores separados por vírgula ou "and".
        for chunk in re.split(r",| and | e ", cleaned):
            name = chunk.strip()
            if _AUTHOR_LINE_RE.match(name):
                surnames.append(name.split()[-1])

        if len(surnames) >= 12:
            break

    # Preserva a ordem, removendo repetições.
    return list(dict.fromkeys(surnames))


def guess_title_from_text(text: str) -> str | None:
    """Heurística de fallback: maior linha destacada no topo da primeira página.

    Usada apenas como *consulta* ao Crossref, nunca como verdade final.
    """
    lines = [ln.strip() for ln in text.split("\n")[:40]]
    candidates = [
        ln
        for ln in lines
        if 20 <= len(ln) <= 250
        and not _DOI_RE.search(ln)
        # Descarta cabeçalhos de journal, e-mails e linhas majoritariamente numéricas.
        and "@" not in ln
        and sum(c.isdigit() for c in ln) < len(ln) * 0.3
        and not ln.lower().startswith(("abstract", "keywords", "introduction"))
    ]
    if not candidates:
        return None
    return max(candidates[:10], key=len)
