"""Testes do references.bib: dedupe, marcação INCOMPLETE e citation keys (G1)."""

from pathlib import Path

import pytest

from scripts import bibtex as bib

CROSSREF_SAMPLE = """@article{Aspelmeyer_2009, title={Measured measurement},
volume={5}, ISSN={1745-2481}, DOI={10.1038/nphys1170}, number={1},
journal={Nature Physics}, author={Aspelmeyer, Markus}, year={2009}, pages={11-12} }"""


@pytest.fixture
def bib_path(tmp_path: Path) -> Path:
    return tmp_path / "references.bib"


def test_crossref_entry_is_not_marked_incomplete(bib_path: Path):
    entry = bib.parse_bibtex_string(CROSSREF_SAMPLE)
    assert entry is not None
    assert entry.incomplete is False

    bib.upsert_entry(bib_path, entry)
    assert bib.INCOMPLETE_MARKER not in bib_path.read_text(encoding="utf-8")


def test_incomplete_entry_is_marked(bib_path: Path):
    entry = bib.make_incomplete_entry("silva2020x", ["Silva"], "2020", "Sem DOI")
    bib.upsert_entry(bib_path, entry)
    assert bib.INCOMPLETE_MARKER in bib_path.read_text(encoding="utf-8")


def test_incomplete_state_survives_round_trip(bib_path: Path):
    bib.upsert_entry(bib_path, bib.parse_bibtex_string(CROSSREF_SAMPLE))
    bib.upsert_entry(
        bib_path, bib.make_incomplete_entry("silva2020x", ["Silva"], "2020", "Sem DOI")
    )

    states = {e.key: e.incomplete for e in bib.load_bib_file(bib_path)}
    assert states["Aspelmeyer_2009"] is False
    assert states["silva2020x"] is True


def test_dedupe_by_doi(bib_path: Path):
    bib.upsert_entry(bib_path, bib.parse_bibtex_string(CROSSREF_SAMPLE))

    same_doi_other_key = bib.parse_bibtex_string(CROSSREF_SAMPLE)
    same_doi_other_key.key = "outraChave"
    _, added = bib.upsert_entry(bib_path, same_doi_other_key)

    assert added is False
    assert len(bib.load_bib_file(bib_path)) == 1


def test_dedupe_by_normalized_title_when_no_doi(bib_path: Path):
    bib.upsert_entry(
        bib_path, bib.make_incomplete_entry("a2020t", ["Silva"], "2020", "Um Estudo Qualquer")
    )
    # Mesmo título com acento/caixa diferente é a mesma obra.
    _, added = bib.upsert_entry(
        bib_path, bib.make_incomplete_entry("b2020t", ["Silva"], "2020", "um estudo qualquer")
    )
    assert added is False


def test_distinct_entries_both_added(bib_path: Path):
    bib.upsert_entry(bib_path, bib.parse_bibtex_string(CROSSREF_SAMPLE))
    _, added = bib.upsert_entry(
        bib_path, bib.make_incomplete_entry("silva2020x", ["Silva"], "2020", "Outro tema")
    )
    assert added is True
    assert len(bib.load_bib_file(bib_path)) == 2


def test_incomplete_entry_leaves_unknown_fields_empty():
    entry = bib.make_incomplete_entry("k", [], None, "Só o título")
    # Campos desconhecidos ficam vazios — nunca preenchidos por palpite (G1).
    assert entry.fields["author"] == ""
    assert entry.fields["year"] == ""
    assert entry.fields["journal"] == ""


def test_citation_key_format():
    key = bib.make_citation_key(["Silva"], "2020", "The Structure of Debate")
    # Artigo inicial é ignorado na escolha da palavra do título.
    assert key == "silva2020structure"


def test_citation_key_disambiguates():
    existing = {"silva2020structure"}
    key = bib.make_citation_key(["Silva"], "2020", "The Structure of Debate", existing)
    assert key == "silva2020structurea"


def test_citation_key_without_year():
    assert bib.make_citation_key(["Silva"], None, "Debate").startswith("silvanodate")


def test_citation_key_strips_accents():
    key = bib.make_citation_key(["Gonçalves"], "2020", "Educação")
    assert key.isascii()


def test_empty_file_loads_as_empty_list(tmp_path: Path):
    assert bib.load_bib_file(tmp_path / "missing.bib") == []
