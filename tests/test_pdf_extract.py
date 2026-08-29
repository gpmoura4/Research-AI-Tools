"""Testes das heurísticas de extração de PDF (offline)."""

from scripts.pdf_extract import (
    _is_preprint_stamp,
    _looks_like_person_name,
    _plausible_title,
    find_doi,
    strip_references_section,
)


# --- Nome próprio (qualquer alfabeto) ------------------------------------


def test_latin_names_recognized():
    assert _looks_like_person_name("Guilherme Moura")
    assert _looks_like_person_name("Ashish Vaswani")
    assert _looks_like_person_name("Ming-Wei Chang")
    assert _looks_like_person_name("Luiz Filipe Brandi")


def test_initials_recognized():
    assert _looks_like_person_name("J. R. Silva")


def test_cyrillic_names_recognized():
    # Uma classe [A-ZÀ-Þ] descartaria estes nomes silenciosamente.
    assert _looks_like_person_name("С. Л. Чирун")
    assert _looks_like_person_name("В. А. Висоцька")


def test_all_caps_header_rejected():
    assert not _looks_like_person_name("ENGINE DIFFUSION")


def test_single_word_rejected():
    assert not _looks_like_person_name("Moura")
    assert not _looks_like_person_name("D-моделі")


def test_lowercase_start_rejected():
    assert not _looks_like_person_name("using generative agents")


# --- DOI: cabeçalho, nunca bibliografia ----------------------------------


def test_doi_found_in_header():
    assert find_doi("Título\nDOI: 10.1234/abcd.5678\nAbstract") == "10.1234/abcd.5678"


def test_doi_from_references_is_ignored():
    # Regressão: o primeiro DOI da bibliografia é de OUTRO paper.
    text = (
        "Um Paper Sem DOI Próprio\nAbstract...\n"
        + "corpo " * 500
        + "\nReferences\n[1] Benjamini, Y. 10.1111/j.2517-6161.1995.tb02031.x\n"
    )
    assert find_doi(text) is None


def test_references_heading_variants_cut_text():
    for heading in ("References", "REFERENCES", "Bibliography", "Referências", "3. References"):
        text = f"corpo do paper\n{heading}\n10.1111/alheio"
        assert "10.1111/alheio" not in strip_references_section(text)


def test_trailing_punctuation_stripped_from_doi():
    assert find_doi("ver DOI 10.1234/abcd.5678.") == "10.1234/abcd.5678"


# --- Título: carimbos de preprint ----------------------------------------


def test_preprint_stamp_detected():
    assert _is_preprint_stamp("arXiv:1706.03762v7 [cs.CL] 2 Aug 2023")
    assert _is_preprint_stamp("Preprint. Under review.")
    assert _is_preprint_stamp("bioRxiv preprint doi: 10.1101/xyz")


def test_real_title_is_not_a_stamp():
    assert not _is_preprint_stamp("Attention Is All You Need")


def test_stamp_rejected_as_title():
    assert not _plausible_title("arXiv:1706.03762v7 [cs.CL] 2 Aug 2023")


def test_filename_like_title_rejected():
    assert not _plausible_title("manuscript_final_v3.docx")
    assert not _plausible_title("Microsoft Word - paper.doc")


def test_real_title_is_plausible():
    assert _plausible_title("Um Modelo Conceitual para a Mitigação de Debates Improdutivos")
