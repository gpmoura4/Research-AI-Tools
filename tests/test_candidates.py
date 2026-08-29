"""Testes de candidates.md: aprovação item a item (G4), dedupe e pendências."""

from pathlib import Path

import pytest

from scripts import candidates as cand
from scripts.bibtex import make_incomplete_entry, upsert_entry
from scripts.openalex import Candidate


def make_candidate(title: str, doi: str | None = None, **kwargs) -> Candidate:
    defaults = dict(
        openalex_id=f"https://openalex.org/W{abs(hash(title)) % 10**8}",
        title=title,
        authors=["Alice Silva", "Bob Souza"],
        year=2023,
        venue="Journal of Testing",
        doi=doi,
        abstract="An abstract with real content returned by the API.",
        is_oa=True,
        oa_status="gold",
        pdf_url="https://example.org/paper.pdf",
        landing_page_url="https://doi.org/x",
        host_platform="Journal of Testing",
        work_type="article",
    )
    defaults.update(kwargs)
    return Candidate(**defaults)


@pytest.fixture
def bib_path(tmp_path: Path) -> Path:
    return tmp_path / "references.bib"


@pytest.fixture
def md_path(tmp_path: Path) -> Path:
    return tmp_path / "candidates.md"


# --- Aprovação (G4) -------------------------------------------------------


def test_written_candidates_start_unchecked(md_path: Path, bib_path: Path):
    cand.write_candidates_md(
        md_path, [make_candidate("A", "10.1/a"), make_candidate("B", "10.1/b")],
        location="a/b/c", queries=["q"], review_type="exploratória",
    )
    # Nada vem pré-aprovado: a marcação é sempre do usuário.
    assert cand.parse_approvals(md_path) == []
    assert cand.count_items(md_path) == 2


def test_only_checked_items_are_approved(md_path: Path):
    cand.write_candidates_md(
        md_path,
        [make_candidate("Primeiro", "10.1/a"), make_candidate("Segundo", "10.1/b"),
         make_candidate("Terceiro", "10.1/c")],
        location="a/b/c", queries=["q"], review_type="exploratória",
    )
    text = md_path.read_text(encoding="utf-8")
    text = text.replace("## [ ] 2. Segundo", "## [x] 2. Segundo")
    md_path.write_text(text, encoding="utf-8")

    approved = cand.parse_approvals(md_path)
    assert len(approved) == 1
    assert approved[0].number == 2
    assert approved[0].title == "Segundo"


def test_uppercase_x_is_accepted(md_path: Path):
    cand.write_candidates_md(
        md_path, [make_candidate("Único", "10.1/a")],
        location="a/b/c", queries=["q"], review_type="exploratória",
    )
    md_path.write_text(
        md_path.read_text(encoding="utf-8").replace("## [ ] 1.", "## [X] 1."),
        encoding="utf-8",
    )
    assert len(cand.parse_approvals(md_path)) == 1


def test_approval_carries_doi_and_links(md_path: Path):
    cand.write_candidates_md(
        md_path, [make_candidate("Com DOI", "10.1234/abc")],
        location="a/b/c", queries=["q"], review_type="exploratória",
    )
    md_path.write_text(
        md_path.read_text(encoding="utf-8").replace("## [ ] 1.", "## [x] 1."),
        encoding="utf-8",
    )
    item = cand.parse_approvals(md_path)[0]
    assert item.doi == "10.1234/abc"
    assert item.pdf_url == "https://example.org/paper.pdf"


def test_missing_file_yields_no_approvals(tmp_path: Path):
    assert cand.parse_approvals(tmp_path / "nao-existe.md") == []


# --- Dedupe (item 6) ------------------------------------------------------


def test_dedupe_against_corpus_by_doi(bib_path: Path):
    entry = make_incomplete_entry("k", ["Silva"], "2020", "Paper existente")
    entry.fields["doi"] = "10.1/existente"
    upsert_entry(bib_path, entry)

    fresh, dupes = cand.dedupe_candidates(
        [make_candidate("Outro título", "10.1/existente"), make_candidate("Novo", "10.1/novo")],
        bib_path,
    )
    assert len(fresh) == 1 and fresh[0].title == "Novo"
    assert dupes[0].duplicate_of == "corpus (DOI)"


def test_dedupe_against_corpus_by_title(bib_path: Path):
    upsert_entry(bib_path, make_incomplete_entry("k", ["Silva"], "2020", "Paper Existente"))

    fresh, dupes = cand.dedupe_candidates(
        [make_candidate("paper existente", None), make_candidate("Novo", "10.1/novo")],
        bib_path,
    )
    assert len(fresh) == 1
    assert dupes[0].duplicate_of == "corpus (título)"


def test_dedupe_within_batch(bib_path: Path):
    # A mesma obra retorna em várias strings de busca.
    fresh, dupes = cand.dedupe_candidates(
        [make_candidate("Mesmo", "10.1/x"), make_candidate("Mesmo de novo", "10.1/x")],
        bib_path,
    )
    assert len(fresh) == 1
    assert dupes[0].duplicate_of == "lote (DOI)"


def test_empty_corpus_keeps_all(bib_path: Path):
    fresh, dupes = cand.dedupe_candidates(
        [make_candidate("A", "10.1/a"), make_candidate("B", "10.1/b")], bib_path
    )
    assert len(fresh) == 2 and dupes == []


# --- pending.md -----------------------------------------------------------


def test_pending_row_written(tmp_path: Path):
    path = tmp_path / "pending.md"
    added = cand.append_pending(
        path, "Paper Fechado", 2021, "Elsevier", "https://doi.org/10.1/x", "acesso fechado"
    )
    text = path.read_text(encoding="utf-8")
    assert added
    assert "Paper Fechado" in text
    assert "pendente — cabe revisão manual" in text
    assert "Elsevier" in text


def test_pending_is_not_duplicated(tmp_path: Path):
    path = tmp_path / "pending.md"
    cand.append_pending(path, "Mesmo Paper", 2021, "Host", "link", "motivo")
    added = cand.append_pending(path, "Mesmo Paper", 2021, "Host", "link", "motivo")
    assert added is False
    assert path.read_text(encoding="utf-8").count("Mesmo Paper") == 1


def test_pipes_in_title_do_not_break_table(tmp_path: Path):
    path = tmp_path / "pending.md"
    cand.append_pending(path, "Título com | pipe", 2021, "Host", "link", "motivo")
    row = [ln for ln in path.read_text(encoding="utf-8").splitlines() if "pipe" in ln][0]
    # 6 colunas => 7 pipes delimitadores; nenhum extra vindo do título.
    assert row.count("|") == 7


# --- G7: filtro de idioma -------------------------------------------------


def test_language_filter_keeps_english_and_portuguese():
    kept, rejected = cand.filter_by_language(
        [
            make_candidate("An English Paper", "10.1/a", language="en"),
            make_candidate("Um Artigo em Português", "10.1/b", language="pt"),
        ],
        ("en", "pt"),
    )
    assert len(kept) == 2 and rejected == []


def test_language_filter_rejects_other_languages():
    kept, rejected = cand.filter_by_language(
        [
            make_candidate("Ein deutsches Papier", "10.1/a", language="de"),
            make_candidate("An English Paper", "10.1/b", language="en"),
        ],
        ("en", "pt"),
    )
    assert [c.title for c in kept] == ["An English Paper"]
    assert "de" in rejected[0][1]


def test_language_detected_when_metadata_missing():
    # OpenAlex deixa `language` vazio em parte dos registros.
    ukrainian = make_candidate(
        "Інформаційна технологія моделювання кризових ситуацій",
        "10.1/uk",
        language=None,
        abstract="Актуальність дослідження зумовлена критичною потребою в ефективній "
        "та психологічно реалістичній підготовці фахівців і цивільного населення.",
    )
    kept, rejected = cand.filter_by_language([ukrainian], ("en", "pt"))
    assert kept == []
    assert "detectado no texto" in rejected[0][1]


def test_undetermined_language_is_kept():
    # Sem metadado e sem texto suficiente: manter é mais seguro que descartar em
    # silêncio — o usuário ainda decide item a item.
    kept, rejected = cand.filter_by_language(
        [make_candidate("Ab", "10.1/a", language=None, abstract=None)], ("en", "pt")
    )
    assert len(kept) == 1 and rejected == []


def test_language_variant_codes_normalize():
    kept, _ = cand.filter_by_language(
        [make_candidate("Paper", "10.1/a", language="en-GB")], ("en", "pt")
    )
    assert len(kept) == 1
