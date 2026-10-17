"""Testes da convenção de renomeação (CLAUDE.md > Convenção de renomeação)."""

from pathlib import Path

from scripts import naming


def test_single_author():
    assert naming.build_filename(["Silva"], 2020, "Um estudo") == "Silva - 2020 - Um estudo.pdf"


def test_two_authors_use_e():
    result = naming.build_filename(["Silva", "Souza"], 2021, "Título")
    assert result == "Silva e Souza - 2021 - Título.pdf"


def test_three_or_more_authors_use_et_al():
    result = naming.build_filename(["Silva", "Souza", "Costa"], 2019, "Título")
    assert result == "Silva et al - 2019 - Título.pdf"

    many = naming.build_filename(["A", "B", "C", "D", "E"], 2019, "Título")
    assert many == "A et al - 2019 - Título.pdf"


def test_missing_year_omits_field():
    assert naming.build_filename(["Silva"], None, "Título") == "Silva - Título.pdf"


def test_title_truncated_at_last_space_before_limit():
    long_title = (
        "Deliberative Democracy and the Structural Conditions of Unproductive "
        "Public Debate in Contemporary Digital Environments"
    )
    result = naming.build_filename(["Silva"], 2022, long_title, max_chars=80)

    title_part = result[len("Silva - 2022 - ") : -len(".pdf")]
    assert len(title_part) <= 80
    # Corta em fronteira de palavra, sem palavra partida ao meio.
    assert not title_part.endswith(" ")
    assert long_title.startswith(title_part)
    assert title_part.split()[-1] in long_title.split()


def test_title_shorter_than_limit_is_untouched():
    assert naming.truncate_title("Curto", 80) == "Curto"


def test_single_word_title_longer_than_limit_is_hard_cut():
    word = "A" * 100
    assert len(naming.truncate_title(word, 80)) == 80


def test_invalid_filesystem_chars_are_replaced():
    result = naming.build_filename(["Silva"], 2020, 'A/B\\C:D*E?F"G<H>I|J')
    assert not any(c in result[:-4] for c in '/\\:*?"<>|')


def test_escaped_quote_from_api_keeps_apostrophe():
    assert naming.sanitize("Exploring Social Media\\'s Role") == "Exploring Social Media's Role"


def test_multiple_spaces_collapse():
    assert naming.sanitize("a    b\n\nc") == "a b c"


def test_collision_suffixes(tmp_path: Path):
    (tmp_path / "Silva - 2020 - T.pdf").touch()
    assert naming.resolve_collision(tmp_path, "Silva - 2020 - T.pdf") == "Silva - 2020 - T (2).pdf"

    (tmp_path / "Silva - 2020 - T (2).pdf").touch()
    assert naming.resolve_collision(tmp_path, "Silva - 2020 - T.pdf") == "Silva - 2020 - T (3).pdf"


def test_no_collision_returns_original(tmp_path: Path):
    assert naming.resolve_collision(tmp_path, "novo.pdf") == "novo.pdf"


def test_accents_are_preserved():
    result = naming.build_filename(["Gonçalves"], 2020, "Educação e política")
    assert "Gonçalves" in result
    assert "Educação" in result


def test_full_names_reduce_to_surnames():
    # Metadados embutidos trazem nomes completos, não sobrenomes.
    result = naming.build_filename(["Ashish Vaswani", "Noam Shazeer", "Niki Parmar"], 2017, "T")
    assert result == "Vaswani et al - 2017 - T.pdf"


def test_inverted_names_reduce_to_surnames():
    assert naming.format_authors(["Vaswani, Ashish"]) == "Vaswani"


def test_many_authors_do_not_blow_up_filename():
    # Caso real: PDF com 90 autores no campo de metadados.
    authors = [f"Nome{i} Sobrenome{i}" for i in range(90)]
    result = naming.build_filename(authors, 2026, "Um título qualquer")
    assert result.startswith("Sobrenome0 et al")
    assert len(result.encode("utf-8")) < 255


def test_filename_stays_within_filesystem_limit():
    # Mesmo com entrada anômala, o nome precisa ser gravável.
    result = naming.build_filename(["X" * 300], 2020, "Y" * 300)
    assert len(result.encode("utf-8")) < 255
