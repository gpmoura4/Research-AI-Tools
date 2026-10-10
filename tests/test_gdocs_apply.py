import pytest

from scripts.gdocs_apply import (
    DocText,
    build_requests,
    doc_id_from,
    parse_adjustments,
    parse_inline,
    plan,
    select,
    u16,
)


def make_document(paragraphs: list[str], revision: str = "rev1") -> dict:
    """Documento no formato da API do Google Docs, um textRun por parágrafo."""
    content = []
    index = 1
    for text in paragraphs:
        run = text + "\n"
        end = index + u16(run)
        content.append({
            "startIndex": index,
            "endIndex": end,
            "paragraph": {"elements": [{"startIndex": index, "endIndex": end,
                                        "textRun": {"content": run}}]},
        })
        index = end
    return {"revisionId": revision, "body": {"content": content}}


MD = """# Ajustes T01

## T01-A3 — Introdução

| Campo | Valor |
|---|---|
| Ação | substituir |

```original
The approach follows Paré et al. [15].
```

```novo
It is a *theoretical review* [15].
```

## T01-A6 — Seção 4.1

| Campo | Valor |
|---|---|
| Ação | substituir-paragrafo |

```original
This article does not conduct a new systematic review.
```

```novo
First new paragraph.

Second new paragraph.
```
"""


def test_parse_adjustments_reads_action_and_fences():
    adjustments = parse_adjustments(MD)
    assert [a.id for a in adjustments] == ["T01-A3", "T01-A6"]
    assert adjustments[0].action == "substituir"
    assert adjustments[0].original == "The approach follows Paré et al. [15]."
    assert "Second new paragraph." in adjustments[1].new


def test_parse_adjustments_rejects_unknown_action():
    bad = MD.replace("| Ação | substituir |", "| Ação | apagar |")
    with pytest.raises(ValueError, match="ação desconhecida"):
        parse_adjustments(bad)


def test_select_accepts_short_and_full_ids():
    adjustments = parse_adjustments(MD)
    assert [a.id for a in select(adjustments, ["A6", "T01-A3"])] == ["T01-A6", "T01-A3"]
    with pytest.raises(ValueError):
        select(adjustments, ["A9"])


def test_parse_inline_italic_and_bold():
    plain, spans = parse_inline("a *b* and **c** d")
    assert plain == "a b and c d"
    assert (spans[0].start, spans[0].end, spans[0].italic) == (2, 3, True)
    assert (spans[1].start, spans[1].end, spans[1].bold) == (8, 9, True)


def test_find_tolerates_quotes_dashes_and_spaces():
    doc = DocText.from_document(make_document(["He said “no” — twice  here."]))
    assert len(doc.find_all('He said "no" - twice here.')) == 1


def test_find_maps_back_to_document_indices():
    doc = DocText.from_document(make_document(["Alpha beta.", "Gamma delta."]))
    start, end = doc.find_all("Gamma delta.")[0]
    assert (start, end) == (13, 25)  # 1 + len("Alpha beta.\n") = 13


def test_plan_substituir_strikes_and_inserts_inline():
    doc = DocText.from_document(make_document(["Intro. The approach follows Paré et al. [15]. End."]))
    [p] = plan(doc, select(parse_adjustments(MD), ["A3"]))
    assert p.status == "ok"
    original_start = 1 + len("Intro. ")
    assert p.strike == (original_start, original_start + len("The approach follows Paré et al. [15]."))
    assert p.insert_at == p.strike[1]
    assert p.insert_text == " It is a theoretical review [15]."


def test_plan_substituir_paragrafo_inserts_new_paragraphs_after():
    doc = DocText.from_document(make_document(
        ["This article does not conduct a new systematic review.", "Next."]))
    [p] = plan(doc, select(parse_adjustments(MD), ["A6"]))
    paragraph_end = 1 + len("This article does not conduct a new systematic review.\n")
    assert p.insert_at == paragraph_end - 1
    assert p.insert_text == "\nFirst new paragraph.\nSecond new paragraph."


def test_plan_skips_missing_duplicated_and_already_applied():
    adjustments = select(parse_adjustments(MD), ["A3"])
    missing = DocText.from_document(make_document(["Nothing here."]))
    assert "não encontrado" in plan(missing, adjustments)[0].reason
    twice = DocText.from_document(make_document(
        ["The approach follows Paré et al. [15].", "The approach follows Paré et al. [15]."]))
    assert "2 vezes" in plan(twice, adjustments)[0].reason
    applied = DocText.from_document(make_document(
        ["The approach follows Paré et al. [15]. It is a theoretical review [15]."]))
    assert "já está" in plan(applied, adjustments)[0].reason


def test_build_requests_styles_new_text_black_with_yellow_highlight():
    doc = DocText.from_document(make_document(["Intro. The approach follows Paré et al. [15]."]))
    requests = build_requests(plan(doc, select(parse_adjustments(MD), ["A3"])))
    kinds = [next(iter(r)) for r in requests]
    assert kinds == ["updateTextStyle", "insertText", "updateTextStyle", "updateTextStyle",
                     "updateTextStyle"]
    assert requests[0]["updateTextStyle"]["textStyle"] == {"strikethrough": True}
    base = requests[2]["updateTextStyle"]["textStyle"]
    assert base["strikethrough"] is False
    assert base["foregroundColor"]["color"]["rgbColor"] == {"red": 0.0, "green": 0.0, "blue": 0.0}
    highlight = requests[3]["updateTextStyle"]
    assert highlight["textStyle"]["backgroundColor"]["color"]["rgbColor"]["blue"] == 0.0
    # o espaço separador não recebe marca-texto
    assert highlight["range"]["startIndex"] == requests[1]["insertText"]["location"]["index"] + 1
    assert requests[4]["updateTextStyle"]["textStyle"] == {"italic": True}


def test_build_requests_orders_from_end_of_document():
    doc = DocText.from_document(make_document([
        "This article does not conduct a new systematic review.",
        "The approach follows Paré et al. [15].",
    ]))
    requests = build_requests(plan(doc, select(parse_adjustments(MD), ["A6", "A3"])))
    inserts = [r["insertText"]["location"]["index"] for r in requests if "insertText" in r]
    assert inserts == sorted(inserts, reverse=True)


def test_doc_id_from_url():
    url = "https://docs.google.com/document/d/1AbC-dEf_123/edit?tab=t.0"
    assert doc_id_from(url) == "1AbC-dEf_123"
    assert doc_id_from("1AbC-dEf_123") == "1AbC-dEf_123"
