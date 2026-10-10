"""Aplica ajustes de manuscrito numa cópia de revisão em Google Docs.

Modo revisão de manuscrito (manuscripts/CLAUDE.md, "Política de ajustes"):

  - o texto substituído NÃO é apagado: fica riscado, com a formatação original;
  - o novo texto entra logo depois, em preto com marca-texto amarelo;
  - cada ajuste é localizado pelo texto original exato; se ele não for encontrado
    ou não for único, o ajuste é pulado e reportado;
  - ajuste cujo novo texto já está no documento não é reaplicado.

Os ajustes vêm de adjustments/<ID>-ajustes.md. Cada ajuste é uma seção
"## T01-A6 — título" com uma linha "| Ação | <ação> |" na tabela de metadados e
dois blocos cercados: ```original``` e ```novo```. Ações:

  substituir              risca o trecho original e insere o novo logo após, na mesma linha
  substituir-paragrafo    risca o parágrafo original e insere o novo como parágrafo(s) seguinte(s)
  inserir-apos            insere o novo logo após o trecho original (âncora), sem riscar
  inserir-paragrafo-apos  insere o novo como parágrafo(s) após o parágrafo que contém a âncora
  revisar-insercao        troca um texto inserido antes pelo agente (todo com marca-texto
                          amarelo) pela versão revisada, sem riscar; recusa texto dos autores
  substituir-parcial      risca só o trecho marcado com {{…}} no bloco ```original``` e
                          insere o marcado do bloco ```novo``` logo após. O contexto fora das
                          chaves precisa ser idêntico nos dois blocos (ex.: "Table {{4}}" →
                          "Table {{5}}"). Negrito/itálico do trecho riscado são herdados.
  inserir-tabela-apos     insere, após o parágrafo que contém a âncora, uma legenda e uma
                          tabela. No bloco ```novo```: a legenda (1º parágrafo) e uma tabela
                          em markdown (linhas "| a | b |"; a 1ª linha é o cabeçalho).

Revisões de um ajuste usam o ID com sufixo de versão ("## T01-A6v2 — …"). Ajustes
desdobrados usam sufixo numérico ("## T01-A8.1 — …"); --ids A8 seleciona todos os A8.n.

No bloco ```novo```, *itálico* e **negrito** viram formatação; linhas separadas por
uma linha em branco viram parágrafos distintos.

Credencial: conta de serviço via --credentials <json> (antes do subcomando) ou
GOOGLE_APPLICATION_CREDENTIALS; sem ela, OAuth de usuário. O documento precisa estar
compartilhado como Editor com o e-mail da conta de serviço.

Uso:
  uv run python -m scripts.gdocs_apply [--credentials <json>] check <doc-id|url>
  uv run python -m scripts.gdocs_apply find  <doc-id|url> "trecho"
  uv run python -m scripts.gdocs_apply apply <doc-id|url> <ajustes.md> --ids A6,A3 [--apply]

Sem --apply, apply apenas simula e mostra o que faria.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "research-workspace"
CLIENT_SECRET = CONFIG_DIR / "google-oauth-client.json"
TOKEN_FILE = CONFIG_DIR / "google-token.json"
SCOPES = ["https://www.googleapis.com/auth/documents"]

ACTIONS = {"substituir", "substituir-paragrafo", "inserir-apos", "inserir-paragrafo-apos",
           "revisar-insercao", "substituir-parcial", "inserir-tabela-apos"}

# Aparência das tabelas inseridas: replica a Table 2 do documento (cabeçalho cinza, borda
# cinza fina, padding 2 pt, Plus Jakarta Sans 7 pt).
TABLE_WIDTH_PT = 394.0
TABLE_FIRST_COL_PT = 78.0
TABLE_FONT = {"fontFamily": "Plus Jakarta Sans", "weight": 400}
TABLE_FONT_SIZE = {"magnitude": 7, "unit": "PT"}
TABLE_BORDER_COLOR = {"color": {"rgbColor": {"red": 0.6, "green": 0.6, "blue": 0.6}}}
TABLE_HEADER_FILL = {"color": {"rgbColor": {"red": 0.85, "green": 0.85, "blue": 0.85}}}

BLACK = {"color": {"rgbColor": {"red": 0.0, "green": 0.0, "blue": 0.0}}}
YELLOW = {"color": {"rgbColor": {"red": 1.0, "green": 1.0, "blue": 0.0}}}

# --------------------------------------------------------------------------- #
# Ajustes (parsing do .md)
# --------------------------------------------------------------------------- #

_HEADING = re.compile(r"^## ((?:T\d+(?:\.\d+)?)-A\d+(?:\.\d+)?(?:v\d+)?)(?![\w.])(.*)$",
                      re.MULTILINE)
_MARK = re.compile(r"\{\{(.+?)\}\}")
_ACTION_ROW = re.compile(r"^\|\s*Ação\s*\|\s*([^|]+?)\s*\|", re.MULTILINE)
_FENCE = re.compile(r"^```(original|novo)[ \t]*\n(.*?)\n```", re.MULTILINE | re.DOTALL)


@dataclass
class Adjustment:
    id: str
    title: str
    action: str
    original: str
    new: str


def parse_adjustments(md_text: str) -> list[Adjustment]:
    """Lê as seções de ajuste de um adjustments/<ID>-ajustes.md."""
    matches = list(_HEADING.finditer(md_text))
    adjustments: list[Adjustment] = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        body = md_text[m.end():end]
        action_m = _ACTION_ROW.search(body)
        fences = {kind: text for kind, text in _FENCE.findall(body)}
        if not action_m or "original" not in fences or "novo" not in fences:
            raise ValueError(f"{m.group(1)}: faltam 'Ação', ```original``` ou ```novo```")
        action = action_m.group(1).strip().lower()
        if action not in ACTIONS:
            raise ValueError(f"{m.group(1)}: ação desconhecida '{action}'")
        adjustments.append(
            Adjustment(
                id=m.group(1),
                title=m.group(2).strip(" —-"),
                action=action,
                original=fences["original"].strip(),
                new=fences["novo"].strip(),
            )
        )
    return adjustments


def select(adjustments: list[Adjustment], ids: list[str]) -> list[Adjustment]:
    """Filtra por IDs curtos (A6) ou completos (T01-A6), preservando a ordem pedida."""
    by_short = {a.id.split("-")[-1]: a for a in adjustments}
    by_full = {a.id: a for a in adjustments}
    chosen: list[Adjustment] = []
    for raw in ids:
        adj = by_full.get(raw) or by_short.get(raw)
        if adj is not None:
            chosen.append(adj)
            continue
        short = raw.split("-")[-1]
        children = [a for a in adjustments if a.id.split("-")[-1].startswith(short + ".")]
        if not children:
            raise ValueError(f"ajuste {raw} não existe no arquivo")
        chosen.extend(children)
    return chosen


# --------------------------------------------------------------------------- #
# Texto inline: *itálico* e **negrito**
# --------------------------------------------------------------------------- #

_INLINE = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*")


@dataclass
class Span:
    start: int  # offsets em caracteres Python dentro do texto plano
    end: int
    bold: bool = False
    italic: bool = False


def parse_inline(text: str) -> tuple[str, list[Span]]:
    plain: list[str] = []
    spans: list[Span] = []
    pos = 0
    length = 0
    for m in _INLINE.finditer(text):
        plain.append(text[pos:m.start()])
        length += m.start() - pos
        inner = m.group(1) if m.group(1) is not None else m.group(2)
        spans.append(Span(length, length + len(inner), bold=m.group(1) is not None,
                          italic=m.group(2) is not None))
        plain.append(inner)
        length += len(inner)
        pos = m.end()
    plain.append(text[pos:])
    return "".join(plain), spans


def new_text_paragraphs(new: str) -> str:
    """Junta parágrafos do bloco ```novo``` (separados por linha em branco) com \\n."""
    paragraphs = [" ".join(p.split()) for p in re.split(r"\n\s*\n", new) if p.strip()]
    return "\n".join(paragraphs)


def u16(s: str) -> int:
    """Comprimento em unidades UTF-16 — a unidade dos índices do Google Docs."""
    return len(s.encode("utf-16-le")) // 2


# --------------------------------------------------------------------------- #
# Documento: texto com mapa de índices e busca normalizada
# --------------------------------------------------------------------------- #

_CHAR_MAP = {
    "‘": "'", "’": "'", "‚": "'", "′": "'",
    "“": '"', "”": '"', "„": '"', "″": '"',
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-",
    "―": "-", "−": "-",
    "ﬁ": "fi", "ﬂ": "fl",
}
_DROP = {"­", "​", "‌", "‍", "﻿"}


def _normalize_chars(chars: list[tuple[str, int, int]]) -> tuple[str, list[int], list[int]]:
    """Normaliza (caractere, início, fim) → texto normalizado + mapas de início/fim."""
    out: list[str] = []
    starts: list[int] = []
    ends: list[int] = []
    for ch, start, end in chars:
        if ch in _DROP:
            continue
        if ch.isspace():
            if out and out[-1] == " ":
                ends[-1] = end
                continue
            mapped = " "
        else:
            mapped = _CHAR_MAP.get(ch, ch)
        for m in mapped:
            out.append(m)
            starts.append(start)
            ends.append(end)
    return "".join(out), starts, ends


def _norm_raw(text: str) -> str:
    """Normaliza sem aparar as pontas (para medir offsets de prefixo e trecho)."""
    return _normalize_chars([(c, 0, 0) for c in text])[0]


def normalize(text: str) -> str:
    return _norm_raw(text).strip()


def _is_yellow(text_style: dict) -> bool:
    rgb = text_style.get("backgroundColor", {}).get("color", {}).get("rgbColor", {})
    return rgb.get("red", 0) > 0.9 and rgb.get("green", 0) > 0.9 and rgb.get("blue", 0) < 0.1


@dataclass
class Paragraph:
    start: int
    end: int  # exclusivo; o último caractere é o "\n"


@dataclass
class DocText:
    revision_id: str
    norm: str
    starts: list[int]
    ends: list[int]
    paragraphs: list[Paragraph] = field(default_factory=list)
    highlighted: set[int] = field(default_factory=set)  # índices com marca-texto amarelo
    bold: set[int] = field(default_factory=set)
    italic: set[int] = field(default_factory=set)

    @classmethod
    def from_document(cls, document: dict) -> "DocText":
        chars: list[tuple[str, int, int]] = []
        paragraphs: list[Paragraph] = []
        highlighted: set[int] = set()
        bold: set[int] = set()
        italic: set[int] = set()

        def walk(content: list[dict]) -> None:
            for element in content:
                if "paragraph" in element:
                    paragraphs.append(Paragraph(element["startIndex"], element["endIndex"]))
                    for el in element["paragraph"].get("elements", []):
                        run = el.get("textRun")
                        if not run:
                            continue
                        idx = el["startIndex"]
                        style = run.get("textStyle", {})
                        yellow = _is_yellow(style)
                        for ch in run.get("content", ""):
                            width = u16(ch)
                            chars.append((ch, idx, idx + width))
                            for flag, bucket in ((yellow, highlighted),
                                                 (style.get("bold"), bold),
                                                 (style.get("italic"), italic)):
                                if flag:
                                    bucket.update(range(idx, idx + width))
                            idx += width
                elif "table" in element:
                    for row in element["table"].get("tableRows", []):
                        for cell in row.get("tableCells", []):
                            walk(cell.get("content", []))
                elif "tableOfContents" in element:
                    walk(element["tableOfContents"].get("content", []))

        walk(document.get("body", {}).get("content", []))
        norm, starts, ends = _normalize_chars(chars)
        return cls(document.get("revisionId", ""), norm, starts, ends, paragraphs, highlighted,
                   bold, italic)

    def find_all(self, text: str) -> list[tuple[int, int]]:
        """Todas as ocorrências (início, fim) de `text` em índices do documento."""
        needle = normalize(text)
        if not needle:
            return []
        hits = []
        pos = self.norm.find(needle)
        while pos != -1:
            hits.append((self.starts[pos], self.ends[pos + len(needle) - 1]))
            pos = self.norm.find(needle, pos + 1)
        return hits

    def is_highlighted(self, start: int, end: int) -> bool:
        return all(i in self.highlighted for i in range(start, end))

    def is_bold(self, start: int, end: int) -> bool:
        return end > start and all(i in self.bold for i in range(start, end))

    def is_italic(self, start: int, end: int) -> bool:
        return end > start and all(i in self.italic for i in range(start, end))

    def find_marked(self, prefix: str, marked: str, suffix: str) -> list[tuple[int, int]]:
        """Ocorrências de prefix+marked+suffix; devolve o intervalo só do trecho `marked`."""
        full = normalize(prefix + marked + suffix)
        lead = len(_norm_raw(prefix))
        width = len(_norm_raw(marked))
        hits = []
        pos = self.norm.find(full)
        while pos != -1:
            a, b = pos + lead, pos + lead + width - 1
            hits.append((self.starts[a], self.ends[b]))
            pos = self.norm.find(full, pos + 1)
        return hits

    def contains(self, text: str) -> bool:
        return bool(self.find_all(text))

    def paragraph_at(self, index: int) -> Paragraph:
        for p in self.paragraphs:
            if p.start <= index < p.end:
                return p
        raise ValueError(f"nenhum parágrafo contém o índice {index}")


# --------------------------------------------------------------------------- #
# Plano de requisições
# --------------------------------------------------------------------------- #


@dataclass
class Planned:
    adjustment: Adjustment
    status: str  # "ok" | "pulado"
    reason: str = ""
    strike: tuple[int, int] | None = None
    delete: tuple[int, int] | None = None
    insert_at: int | None = None
    insert_text: str = ""
    new_offset: int = 0  # onde o novo texto começa dentro de insert_text (após separador)
    spans: list[Span] = field(default_factory=list)
    inherit_bold: bool = False
    inherit_italic: bool = False
    table: "TablePlan | None" = None


@dataclass
class TablePlan:
    rows: list[list[tuple[str, list[Span]]]]  # (texto plano, spans) por célula; linha 0 = cabeçalho

    @property
    def cols(self) -> int:
        return len(self.rows[0])


def split_marked(text: str, label: str) -> tuple[str, str, str]:
    marks = list(_MARK.finditer(text))
    if len(marks) != 1:
        raise ValueError(f"{label}: esperado exatamente um trecho {{{{…}}}}, achei {len(marks)}")
    m = marks[0]
    return text[:m.start()], m.group(1), text[m.end():]


def parse_table(new: str) -> tuple[str, TablePlan]:
    """Bloco ```novo``` de inserir-tabela-apos: legenda + tabela markdown."""
    caption_lines, rows = [], []
    for line in new.splitlines():
        line = line.strip()
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                continue
            rows.append([parse_inline(c) for c in cells])
        elif line and not rows:
            caption_lines.append(line)
    if len(rows) < 2 or len({len(r) for r in rows}) != 1 or not caption_lines:
        raise ValueError("inserir-tabela-apos: preciso de legenda, cabeçalho e linhas de mesma largura")
    return " ".join(caption_lines), TablePlan(rows)


def _plan_partial(doc: DocText, adj: Adjustment) -> Planned:
    o_pre, o_mark, o_suf = split_marked(adj.original, f"{adj.id} original")
    n_pre, n_mark, n_suf = split_marked(adj.new, f"{adj.id} novo")
    if (o_pre, o_suf) != (n_pre, n_suf):
        raise ValueError(f"{adj.id}: o contexto fora de {{{{…}}}} difere entre original e novo")
    if doc.contains(f"{o_pre}{o_mark} {n_mark}{o_suf}"):
        return Planned(adj, "pulado", "novo texto já está no documento")
    hits = doc.find_marked(o_pre, o_mark, o_suf)
    if len(hits) != 1:
        reason = ("texto original não encontrado" if not hits
                  else f"texto original aparece {len(hits)} vezes")
        return Planned(adj, "pulado", reason)
    start, end = hits[0]
    return Planned(adj, "ok", strike=(start, end), insert_at=end, insert_text=" " + n_mark,
                   new_offset=1, inherit_bold=doc.is_bold(start, end),
                   inherit_italic=doc.is_italic(start, end))


def _plan_table(doc: DocText, adj: Adjustment) -> Planned:
    caption_md, table = parse_table(adj.new)
    caption, spans = parse_inline(caption_md)
    if doc.contains(caption):
        return Planned(adj, "pulado", "novo texto já está no documento")
    hits = doc.find_all(adj.original)
    if len(hits) != 1:
        reason = ("texto original não encontrado" if not hits
                  else f"texto original aparece {len(hits)} vezes")
        return Planned(adj, "pulado", reason)
    para = doc.paragraph_at(hits[0][0])
    # "\n\n" + legenda antes do "\n" final do parágrafo da âncora: fica um parágrafo vazio
    # (como entre o texto e a legenda da Table 2) e a legenda herda o "\n" original.
    return Planned(adj, "ok", insert_at=para.end - 1, insert_text="\n\n" + caption,
                   new_offset=2, spans=spans, table=table)


def plan(doc: DocText, adjustments: list[Adjustment]) -> list[Planned]:
    planned: list[Planned] = []
    for adj in adjustments:
        if adj.action == "substituir-parcial":
            planned.append(_plan_partial(doc, adj))
            continue
        if adj.action == "inserir-tabela-apos":
            planned.append(_plan_table(doc, adj))
            continue
        new_plain_md = new_text_paragraphs(adj.new)
        new_plain, spans = parse_inline(new_plain_md)
        # Na mesma linha, o aplicado é "original novo": procurar o par evita pular um
        # novo texto curto que já exista em outro ponto do documento.
        applied = (f"{adj.original} {new_plain}" if adj.action in {"substituir", "inserir-apos"}
                   else new_plain.split("\n")[0])
        if doc.contains(applied):
            planned.append(Planned(adj, "pulado", "novo texto já está no documento"))
            continue
        hits = doc.find_all(adj.original)
        if len(hits) != 1:
            reason = ("texto original não encontrado" if not hits
                      else f"texto original aparece {len(hits)} vezes")
            planned.append(Planned(adj, "pulado", reason))
            continue
        start, end = hits[0]
        p = Planned(adj, "ok", spans=spans)
        if adj.action == "revisar-insercao":
            if not doc.is_highlighted(start, end):
                planned.append(Planned(adj, "pulado",
                                       "trecho não está todo com marca-texto (não é inserção do agente)"))
                continue
            p.delete = (start, end)
            p.insert_at, p.insert_text, p.new_offset = start, new_plain, 0
            planned.append(p)
            continue
        if adj.action in {"substituir", "substituir-paragrafo"}:
            p.strike = (start, end)
        if adj.action in {"substituir", "inserir-apos"}:
            p.insert_at, p.insert_text, p.new_offset = end, " " + new_plain, 1
        else:
            para = doc.paragraph_at(start)
            p.insert_at, p.insert_text, p.new_offset = para.end - 1, "\n" + new_plain, 1
        planned.append(p)

    ok = sorted((p for p in planned if p.status == "ok"), key=lambda p: p.insert_at, reverse=True)
    for a, b in zip(ok, ok[1:]):
        a_range = a.strike or a.delete
        if b.insert_at == a.insert_at or (a_range and b.insert_at > a_range[0]):
            raise ValueError(f"{a.adjustment.id} e {b.adjustment.id} se sobrepõem no documento")
    return planned


def build_requests(planned: list[Planned]) -> list[dict]:
    """Requisições batchUpdate, do fim para o início do documento (índices estáveis)."""
    requests: list[dict] = []
    ok = sorted((p for p in planned if p.status == "ok"), key=lambda p: p.insert_at, reverse=True)
    for p in ok:
        if p.strike:
            requests.append({"updateTextStyle": {
                "range": {"startIndex": p.strike[0], "endIndex": p.strike[1]},
                "textStyle": {"strikethrough": True},
                "fields": "strikethrough",
            }})
        if p.delete:
            requests.append({"deleteContentRange": {
                "range": {"startIndex": p.delete[0], "endIndex": p.delete[1]},
            }})
        requests.append({"insertText": {"location": {"index": p.insert_at}, "text": p.insert_text}})
        ins_start = p.insert_at
        ins_end = ins_start + u16(p.insert_text)
        new_start = ins_start + u16(p.insert_text[:p.new_offset])
        requests.append({"updateTextStyle": {
            "range": {"startIndex": ins_start, "endIndex": ins_end},
            "textStyle": {"strikethrough": False, "bold": False, "italic": False,
                          "underline": False, "foregroundColor": BLACK},
            "fields": "strikethrough,bold,italic,underline,foregroundColor,backgroundColor",
        }})
        requests.append({"updateTextStyle": {
            "range": {"startIndex": new_start, "endIndex": ins_end},
            "textStyle": {"backgroundColor": YELLOW},
            "fields": "backgroundColor",
        }})
        new_text = p.insert_text[p.new_offset:]
        for flag, key in ((p.inherit_bold, "bold"), (p.inherit_italic, "italic")):
            if flag:
                requests.append({"updateTextStyle": {
                    "range": {"startIndex": ins_start, "endIndex": ins_end},
                    "textStyle": {key: True}, "fields": key,
                }})
        for span in p.spans:
            s = new_start + u16(new_text[:span.start])
            e = new_start + u16(new_text[:span.end])
            style, fields = {}, []
            if span.bold:
                style["bold"], fields = True, fields + ["bold"]
            if span.italic:
                style["italic"], fields = True, fields + ["italic"]
            requests.append({"updateTextStyle": {
                "range": {"startIndex": s, "endIndex": e},
                "textStyle": style, "fields": ",".join(fields),
            }})
        if p.table:
            requests.extend(table_requests(p.table, ins_end))
    return requests


def table_requests(table: TablePlan, at: int) -> list[dict]:
    """Requisições que criam e preenchem uma tabela inserida no índice `at`.

    A API insere um "\n" antes da tabela, que então começa em at+1. Numa tabela vazia
    R×C, a célula (r, c) tem parágrafo em t + 3 + r·(1+2C) + 2c, e a tabela termina em
    t + 2 + R·(1+2C), logo antes do "\n" original (parágrafo vazio sobrando, apagado).
    Conferido na API em 2026-10-10.
    As células são preenchidas da última para a primeira, para manter os índices válidos.
    """
    rows, cols = len(table.rows), table.cols
    t = at + 1
    end = t + 2 + rows * (1 + 2 * cols)
    loc = {"index": t}
    border = {"color": TABLE_BORDER_COLOR, "width": {"magnitude": 0.68181825, "unit": "PT"},
              "dashStyle": "SOLID"}
    pad = {"magnitude": 2, "unit": "PT"}
    reqs: list[dict] = [
        {"insertTable": {"location": {"index": at}, "rows": rows, "columns": cols}},
        {"deleteContentRange": {"range": {"startIndex": end, "endIndex": end + 1}}},
    ]
    avg = [sum(len(r[c][0]) for r in table.rows[1:]) / (rows - 1) or 1 for c in range(cols)]
    rest = TABLE_WIDTH_PT - TABLE_FIRST_COL_PT
    widths = [TABLE_FIRST_COL_PT] + [rest * a / sum(avg[1:]) for a in avg[1:]]
    for c, w in enumerate(widths):
        reqs.append({"updateTableColumnProperties": {
            "tableStartLocation": loc, "columnIndices": [c],
            "tableColumnProperties": {"widthType": "FIXED_WIDTH",
                                      "width": {"magnitude": round(w, 2), "unit": "PT"}},
            "fields": "width,widthType",
        }})
    whole = {"tableCellLocation": {"tableStartLocation": loc, "rowIndex": 0, "columnIndex": 0},
             "rowSpan": rows, "columnSpan": cols}
    reqs.append({"updateTableCellStyle": {
        "tableRange": whole,
        "tableCellStyle": {"borderLeft": border, "borderRight": border, "borderTop": border,
                           "borderBottom": border, "paddingLeft": pad, "paddingRight": pad,
                           "paddingTop": pad, "paddingBottom": pad, "contentAlignment": "MIDDLE"},
        "fields": "borderLeft,borderRight,borderTop,borderBottom,paddingLeft,paddingRight,"
                  "paddingTop,paddingBottom,contentAlignment",
    }})
    reqs.append({"updateTableCellStyle": {
        "tableRange": {"tableCellLocation": {"tableStartLocation": loc, "rowIndex": 0,
                                             "columnIndex": 0}, "rowSpan": 1, "columnSpan": cols},
        "tableCellStyle": {"backgroundColor": TABLE_HEADER_FILL},
        "fields": "backgroundColor",
    }})
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            text, spans = table.rows[r][c]
            start = t + 3 + r * (1 + 2 * cols) + 2 * c
            stop = start + u16(text)
            reqs.append({"insertText": {"location": {"index": start}, "text": text}})
            reqs.append({"updateParagraphStyle": {
                "range": {"startIndex": start, "endIndex": stop + 1},
                "paragraphStyle": {"alignment": "CENTER" if r == 0 else "START",
                                   "lineSpacing": 115,
                                   "indentStart": {"magnitude": 0, "unit": "PT"},
                                   "indentFirstLine": {"magnitude": 0, "unit": "PT"},
                                   "spaceAbove": {"magnitude": 0, "unit": "PT"},
                                   "spaceBelow": {"magnitude": 0, "unit": "PT"}},
                "fields": "alignment,lineSpacing,indentStart,indentFirstLine,spaceAbove,spaceBelow",
            }})
            reqs.append({"updateTextStyle": {
                "range": {"startIndex": start, "endIndex": stop},
                "textStyle": {"bold": r == 0, "italic": False, "strikethrough": False,
                              "underline": False, "foregroundColor": BLACK,
                              "backgroundColor": YELLOW, "fontSize": TABLE_FONT_SIZE,
                              "weightedFontFamily": TABLE_FONT},
                "fields": "bold,italic,strikethrough,underline,foregroundColor,backgroundColor,"
                          "fontSize,weightedFontFamily",
            }})
            for span in spans:
                style = {k: True for k, on in (("bold", span.bold), ("italic", span.italic)) if on}
                reqs.append({"updateTextStyle": {
                    "range": {"startIndex": start + u16(text[:span.start]),
                              "endIndex": start + u16(text[:span.end])},
                    "textStyle": style, "fields": ",".join(style),
                }})
    return reqs


# --------------------------------------------------------------------------- #
# Log no .md
# --------------------------------------------------------------------------- #

LOG_HEADER = (
    "\n## Log de aplicação\n\n"
    "| Data | Documento | Aplicados | Pulados | Revisão antes | Revisão depois |\n"
    "|---|---|---|---|---|---|\n"
)


def append_log(md_path: Path, doc_id: str, planned: list[Planned], rev_before: str,
               rev_after: str) -> None:
    text = md_path.read_text(encoding="utf-8")
    if "## Log de aplicação" not in text:
        text = text.rstrip("\n") + "\n" + LOG_HEADER
    applied = ", ".join(p.adjustment.id for p in planned if p.status == "ok") or "—"
    skipped = "; ".join(f"{p.adjustment.id} ({p.reason})" for p in planned
                        if p.status != "ok") or "—"
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    text = text.rstrip("\n") + (
        f"\n| {stamp} | `{doc_id}` | {applied} | {skipped} | `{rev_before}` | `{rev_after}` |\n"
    )
    md_path.write_text(text, encoding="utf-8")


# --------------------------------------------------------------------------- #
# Google Docs (rede)
# --------------------------------------------------------------------------- #


def doc_id_from(raw: str) -> str:
    m = re.search(r"/document/d/([A-Za-z0-9_-]+)", raw)
    return m.group(1) if m else raw.strip()


def docs_service(credentials_file: Path | None = None):
    """Cliente da API. Conta de serviço (--credentials ou GOOGLE_APPLICATION_CREDENTIALS)
    tem precedência; sem ela, usa OAuth de usuário com token em ~/.config."""
    from googleapiclient.discovery import build

    sa_file = credentials_file or (
        Path(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
        if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") else None
    )
    if sa_file:
        from google.oauth2 import service_account

        creds = service_account.Credentials.from_service_account_file(str(sa_file), scopes=SCOPES)
        return build("docs", "v1", credentials=creds, cache_discovery=False)

    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CLIENT_SECRET.exists():
                sys.exit(f"Credencial OAuth ausente: salve o JSON do cliente em {CLIENT_SECRET}")
            flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET), SCOPES)
            creds = flow.run_local_server(port=0)
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        TOKEN_FILE.write_text(creds.to_json(), encoding="utf-8")
        TOKEN_FILE.chmod(0o600)
    return build("docs", "v1", credentials=creds, cache_discovery=False)


def fetch(service, doc_id: str) -> dict:
    return service.documents().get(documentId=doc_id).execute()


def cmd_check(doc_id: str, creds: Path | None, head: int) -> int:
    document = fetch(docs_service(creds), doc_id)
    doc = DocText.from_document(document)
    print(f"Arquivo: {document.get('title')}")
    print(f"Revisão: {doc.revision_id}")
    print(f"Parágrafos: {len(doc.paragraphs)} · caracteres: {len(doc.norm)}")
    shown = 0
    for element in document.get("body", {}).get("content", []):
        if shown >= head or "paragraph" not in element:
            continue
        text = "".join(el.get("textRun", {}).get("content", "")
                       for el in element["paragraph"].get("elements", [])).strip()
        if text:
            style = element["paragraph"].get("paragraphStyle", {}).get("namedStyleType", "")
            print(f"  [{element['startIndex']}] {style}: {text[:110]}")
            shown += 1
    return 0


def cmd_find(doc_id: str, text: str, creds: Path | None) -> int:
    doc = DocText.from_document(fetch(docs_service(creds), doc_id))
    hits = doc.find_all(text)
    print(f"{len(hits)} ocorrência(s)")
    for start, end in hits:
        print(f"  índices {start}–{end}")
    return 0 if hits else 1


def cmd_apply(doc_id: str, md_path: Path, ids: list[str], really: bool,
              creds: Path | None) -> int:
    adjustments = select(parse_adjustments(md_path.read_text(encoding="utf-8")), ids)
    service = docs_service(creds)
    doc = DocText.from_document(fetch(service, doc_id))
    planned = plan(doc, adjustments)

    print(f"Documento {doc_id} · revisão {doc.revision_id}")
    for p in planned:
        a = p.adjustment
        if p.status == "ok":
            where = (f"risca {p.strike[0]}–{p.strike[1]}, " if p.strike else
                     f"troca inserção {p.delete[0]}–{p.delete[1]}, " if p.delete else "")
            extra = (f" + tabela {p.table.cols}×{len(p.table.rows)}" if p.table else "")
            print(f"  [ok]     {a.id} ({a.action}): {where}insere em {p.insert_at}{extra}")
        else:
            print(f"  [pulado] {a.id}: {p.reason}")

    requests = build_requests(planned)
    if not requests:
        print("Nada a aplicar.")
        return 0
    if not really:
        print(f"Simulação: {len(requests)} requisições. Use --apply para gravar.")
        return 0

    response = service.documents().batchUpdate(
        documentId=doc_id,
        body={"requests": requests, "writeControl": {"requiredRevisionId": doc.revision_id}},
    ).execute()
    rev_after = response.get("writeControl", {}).get("requiredRevisionId", "?")
    append_log(md_path, doc_id, planned, doc.revision_id, rev_after)
    print(f"Aplicado. Revisão {doc.revision_id} → {rev_after}. Log em {md_path}.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--credentials", type=Path,
                        help="JSON da conta de serviço (senão: GOOGLE_APPLICATION_CREDENTIALS ou OAuth)")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_check = sub.add_parser("check", help="testa o acesso ao documento")
    p_check.add_argument("doc")
    p_check.add_argument("--head", type=int, default=5, help="parágrafos iniciais a mostrar")
    p_find = sub.add_parser("find", help="procura um trecho no documento")
    p_find.add_argument("doc")
    p_find.add_argument("text")
    p_apply = sub.add_parser("apply", help="aplica ajustes (simulação sem --apply)")
    p_apply.add_argument("doc")
    p_apply.add_argument("md", type=Path)
    p_apply.add_argument("--ids", required=True, help="ex.: A6,A3")
    p_apply.add_argument("--apply", action="store_true", help="grava no documento")
    args = parser.parse_args(argv)

    doc_id = doc_id_from(args.doc)
    if args.cmd == "check":
        return cmd_check(doc_id, args.credentials, args.head)
    if args.cmd == "find":
        return cmd_find(doc_id, args.text, args.credentials)
    ids = [i.strip() for i in args.ids.split(",") if i.strip()]
    return cmd_apply(doc_id, args.md, ids, args.apply, args.credentials)


if __name__ == "__main__":
    sys.exit(main())
