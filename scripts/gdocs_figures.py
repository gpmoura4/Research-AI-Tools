"""Troca figuras na cópia de revisão em Google Docs (modo revisão de manuscrito).

A API do Docs só insere imagem a partir de uma URL pública. O fluxo, por figura:
  1. envia o PNG ao Drive do usuário (OAuth, escopo drive.file: o app só vê os
     arquivos que ele mesmo criou);
  2. abre um link "qualquer pessoa com o link" pelo tempo da inserção;
  3. insere a imagem nova antes da antiga e apaga a antiga, numa única batchUpdate
     com controle de revisão (a edição no Docs é feita pela conta de serviço);
  4. apaga o arquivo do Drive, dê certo ou não.

A figura é localizada pela legenda ("Figure N." ou "Figure A1.", ignorando texto
riscado): a imagem é a do parágrafo imediatamente anterior. A imagem antiga é salva
localmente antes da troca. Sem --apply, só mostra o que faria.

Uso:
    uv run python -m scripts.gdocs_figures replace <doc-id> --figure 5 --png out/fig05-AF2.png \
        [--width 380] [--archive out/originais] [--log adjustments/T06-ajustes.md] [--apply]

OAuth: cliente "Desktop app" salvo em ~/.config/research-workspace/google-oauth-client.json.
O token do Drive fica em ~/.config/research-workspace/google-drive-token.json.
"""
from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

from scripts.gdocs_apply import CLIENT_SECRET, CONFIG_DIR, doc_id_from, docs_service, fetch

DRIVE_SCOPES = ["https://www.googleapis.com/auth/drive.file"]
DRIVE_TOKEN = CONFIG_DIR / "google-drive-token.json"
LOG_HEADER = (
    "\n## Log de troca de imagens\n\n"
    "| Data | Figura | Arquivo | Objeto antigo | Objeto novo | Revisão antes | Revisão depois |\n"
    "|---|---|---|---|---|---|---|\n"
)


def drive_service():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    from scripts.config import load_config

    client = load_config().google_oauth_client_file or CLIENT_SECRET
    if not client.exists():
        sys.exit(f"Cliente OAuth ausente: {client} (configure google_docs.oauth_client_file)")
    token = client.parent / "google-drive-token.json" if client != CLIENT_SECRET else DRIVE_TOKEN
    creds = None
    if token.exists():
        creds = Credentials.from_authorized_user_file(str(token), DRIVE_SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(client), DRIVE_SCOPES)
            creds = flow.run_local_server(port=0)
        token.parent.mkdir(parents=True, exist_ok=True)
        token.write_text(creds.to_json(), encoding="utf-8")
        token.chmod(0o600)
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def _visible_text(paragraph: dict) -> str:
    """Texto do parágrafo sem os trechos riscados."""
    out = []
    for el in paragraph.get("elements", []):
        run = el.get("textRun")
        if run and not run.get("textStyle", {}).get("strikethrough"):
            out.append(run["content"])
    return re.sub(r"\s+", " ", "".join(out)).strip()


def locate(document: dict, figure: str) -> tuple[str, int]:
    """(id do objeto, índice) da imagem logo antes da legenda 'Figure <figure>.'."""
    caption = re.compile(rf"^Figure {re.escape(figure)}\.(\s|$)")
    last_image: tuple[str, int] | None = None
    since_image = 0
    for el in document["body"]["content"]:
        if "paragraph" not in el:
            last_image, since_image = None, 0
            continue
        para = el["paragraph"]
        images = [(e["inlineObjectElement"]["inlineObjectId"], e["startIndex"])
                  for e in para.get("elements", []) if "inlineObjectElement" in e]
        if images:
            last_image, since_image = images[-1], 0
            continue
        text = _visible_text(para)
        if caption.match(text):
            if last_image is None or since_image > 1:
                sys.exit(f"Figure {figure}: legenda encontrada, mas sem imagem logo antes dela")
            return last_image
        if text:
            since_image += 1
    sys.exit(f"Figure {figure}: legenda não encontrada")


def archive_old(document: dict, object_id: str, folder: Path, figure: str) -> Path | None:
    props = document["inlineObjects"][object_id]["inlineObjectProperties"]["embeddedObject"]
    uri = props.get("imageProperties", {}).get("contentUri")
    if not uri:
        return None
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"figure-{figure}-antes-{object_id.replace('.', '_')}.png"
    with urllib.request.urlopen(uri) as r:
        path.write_bytes(r.read())
    return path


def append_log(md: Path, figure: str, png: Path, old_id: str, new_id: str, rev_before: str,
               rev_after: str) -> None:
    text = md.read_text(encoding="utf-8") if md.exists() else ""
    if "## Log de troca de imagens" not in text:
        text = text.rstrip("\n") + "\n" + LOG_HEADER
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = f"| {stamp} | {figure} | `{png.name}` | `{old_id}` | `{new_id}` | `{rev_before}` | `{rev_after}` |"
    # A linha entra no fim da própria tabela, mesmo que outra seção venha depois dela.
    lines = text.rstrip("\n").split("\n")
    i = lines.index("## Log de troca de imagens") + 1
    while i < len(lines) and not lines[i].startswith("|"):
        i += 1
    while i < len(lines) and lines[i].startswith("|"):
        i += 1
    lines.insert(i, row)
    md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def cmd_replace(args: argparse.Namespace) -> int:
    doc_id = doc_id_from(args.doc)
    png = Path(args.png)
    if not png.is_file():
        sys.exit(f"PNG não encontrado: {png}")
    docs = docs_service()
    document = fetch(docs, doc_id)
    rev = document["revisionId"]
    old_id, index = locate(document, args.figure)
    print(f"Figure {args.figure}: imagem {old_id} no índice {index} · revisão {rev[:16]}…")
    print(f"  nova: {png} · largura {args.width} pt")
    if not args.apply:
        print("Simulação. Use --apply para trocar.")
        return 0

    if args.archive:
        saved = archive_old(document, old_id, Path(args.archive), args.figure)
        print(f"  antiga salva em {saved}")

    from googleapiclient.http import MediaFileUpload

    drive = drive_service()
    meta = drive.files().create(body={"name": png.name}, media_body=MediaFileUpload(str(png), mimetype="image/png"),
                                fields="id").execute()
    file_id = meta["id"]
    try:
        drive.permissions().create(fileId=file_id, body={"type": "anyone", "role": "reader"}).execute()
        last_error = None
        for uri in (f"https://drive.google.com/uc?export=download&id={file_id}",
                    f"https://lh3.googleusercontent.com/d/{file_id}"):
            requests = [
                {"insertInlineImage": {"location": {"index": index}, "uri": uri,
                                       "objectSize": {"width": {"magnitude": args.width, "unit": "PT"}}}},
                {"deleteContentRange": {"range": {"startIndex": index + 1, "endIndex": index + 2}}},
            ]
            try:
                resp = docs.documents().batchUpdate(
                    documentId=doc_id,
                    body={"requests": requests, "writeControl": {"requiredRevisionId": rev}},
                ).execute()
                break
            except Exception as e:  # noqa: BLE001
                last_error = e
                time.sleep(1)
        else:
            raise SystemExit(f"Inserção falhou: {last_error}")
    finally:
        drive.files().delete(fileId=file_id).execute()
        print("  arquivo temporário apagado do Drive")

    new_id = resp["replies"][0]["insertInlineImage"]["objectId"]
    rev_after = resp["writeControl"]["requiredRevisionId"]
    print(f"  trocada: {old_id} → {new_id} · revisão {rev_after[:16]}…")
    if args.log:
        append_log(Path(args.log), args.figure, png, old_id, new_id, rev, rev_after)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("replace", help="troca a imagem de uma figura")
    r.add_argument("doc")
    r.add_argument("--figure", required=True, help="número da figura (ex.: 5, A1)")
    r.add_argument("--png", required=True)
    r.add_argument("--width", type=float, default=380.0, help="largura em pt (altura proporcional)")
    r.add_argument("--archive", help="pasta onde salvar a imagem antiga")
    r.add_argument("--log", help="arquivo .md onde registrar a troca")
    r.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    return {"replace": cmd_replace}[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
