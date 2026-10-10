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

No bloco ```novo```, *itálico* e **negrito** viram formatação; linhas separadas por
uma linha em branco viram parágrafos distintos.

Uso:
  uv run python -m scripts.gdocs_apply check <doc-id|url>
  uv run python -m scripts.gdocs_apply find  <doc-id|url> "trecho"
  uv run python -m scripts.gdocs_apply apply <doc-id|url> <ajustes.md> --ids A6,A3 [--apply]

Sem --apply, apply apenas simula e mostra o que faria.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "research-workspace"
CLIENT_SECRET = CONFIG_DIR / "google-oauth-client.json"
TOKEN_FILE = CONFIG_DIR / "google-token.json"
SCOPES = ["https://www.googleapis.com/auth/documents"]

ACTIONS = {"substituir", "substituir-paragrafo", "inserir-apos", "inserir-paragrafo-apos"}

BLACK = {"color": {"rgbColor": {"red": 0.0, "green": 0.0, "blue": 0.0}}}
YELLOW = {"color": {"rgbColor": {"red": 1.0, "green": 1.0, "blue": 0.0}}}

# --------------------------------------------------------------------------- #
# Ajustes (parsing do .md)
# --------------------------------------------------------------------------- #

_HEADING = re.compile(r"^## ((?:T\d+(?:\.\d+)?)-A\d+)\b(.*)$", re.MULTILINE)
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
    chosen = []
    for raw in ids:
        adj = by_full.get(raw) or by_short.get(raw)
        if adj is None:
            raise ValueError(f"ajuste {raw} não existe no arquivo")
        chosen.append(adj)
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


def normalize(text: str) -> str:
    chars = [(c, 0, 0) for c in text]
    return _normalize_chars(chars)[0].strip()


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

    @classmethod
    def from_document(cls, document: dict) -> "DocText":
        chars: list[tuple[str, int, int]] = []
        paragraphs: list[Paragraph] = []

        def walk(content: list[dict]) -> None:
            for element in content:
                if "paragraph" in element:
                    paragraphs.append(Paragraph(element["startIndex"], element["endIndex"]))
                    for el in element["paragraph"].get("elements", []):
                        run = el.get("textRun")
                        if not run:
                            continue
                        idx = el["startIndex"]
                        for ch in run.get("content", ""):
                            width = u16(ch)
                            chars.append((ch, idx, idx + width))
                            idx += width
                elif "table" in element:
                    for row in element["table"].get("tableRows", []):
                        for cell in row.get("tableCells", []):
                            walk(cell.get("content", []))
                elif "tableOfContents" in element:
                    walk(element["tableOfContents"].get("content", []))

        walk(document.get("body", {}).get("content", []))
        norm, starts, ends = _normalize_chars(chars)
        return cls(document.get("revisionId", ""), norm, starts, ends, paragraphs)

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
    insert_at: int | None = None
    insert_text: str = ""
    new_offset: int = 0  # onde o novo texto começa dentro de insert_text (após separador)
    spans: list[Span] = field(default_factory=list)


def plan(doc: DocText, adjustments: list[Adjustment]) -> list[Planned]:
    planned: list[Planned] = []
    for adj in adjustments:
        new_plain_md = new_text_paragraphs(adj.new)
        new_plain, spans = parse_inline(new_plain_md)
        if doc.contains(new_plain.split("\n")[0]):
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
        if b.insert_at == a.insert_at or (a.strike and b.insert_at > a.strike[0]):
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
    return requests


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


def docs_service():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

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


def cmd_check(doc_id: str) -> int:
    document = fetch(docs_service(), doc_id)
    doc = DocText.from_document(document)
    print(f"Título: {document.get('title')}")
    print(f"Revisão: {doc.revision_id}")
    print(f"Parágrafos: {len(doc.paragraphs)} · caracteres: {len(doc.norm)}")
    return 0


def cmd_find(doc_id: str, text: str) -> int:
    doc = DocText.from_document(fetch(docs_service(), doc_id))
    hits = doc.find_all(text)
    print(f"{len(hits)} ocorrência(s)")
    for start, end in hits:
        print(f"  índices {start}–{end}")
    return 0 if hits else 1


def cmd_apply(doc_id: str, md_path: Path, ids: list[str], really: bool) -> int:
    adjustments = select(parse_adjustments(md_path.read_text(encoding="utf-8")), ids)
    service = docs_service()
    doc = DocText.from_document(fetch(service, doc_id))
    planned = plan(doc, adjustments)

    print(f"Documento {doc_id} · revisão {doc.revision_id}")
    for p in planned:
        a = p.adjustment
        if p.status == "ok":
            where = f"risca {p.strike[0]}–{p.strike[1]}, " if p.strike else ""
            print(f"  [ok]     {a.id} ({a.action}): {where}insere em {p.insert_at}")
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
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_check = sub.add_parser("check", help="testa o acesso ao documento")
    p_check.add_argument("doc")
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
        return cmd_check(doc_id)
    if args.cmd == "find":
        return cmd_find(doc_id, args.text)
    ids = [i.strip() for i in args.ids.split(",") if i.strip()]
    return cmd_apply(doc_id, args.md, ids, args.apply)


if __name__ == "__main__":
    sys.exit(main())
