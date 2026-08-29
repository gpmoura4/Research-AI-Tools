"""Testes do mapeamento OpenAlex (offline, sem rede)."""

from scripts.oa_resolver import arxiv_pdf_url
from scripts.openalex import (
    OpenAlexClient,
    reconstruct_abstract,
    summarize_abstract,
)

# Resposta reduzida no formato real da API.
WORK = {
    "id": "https://openalex.org/W123",
    "title": "Opportunities and Risks of LLMs",
    "doi": "https://doi.org/10.48550/arxiv.2306.11932",
    "publication_year": 2023,
    "type": "preprint",
    "cited_by_count": 42,
    "authorships": [
        {"author": {"display_name": "Christopher Small"}},
        {"author": {"display_name": "Ivan Vendrov"}},
    ],
    "primary_location": {
        "source": {"display_name": "arXiv (Cornell University)"},
        "landing_page_url": "https://arxiv.org/abs/2306.11932",
    },
    "open_access": {"is_oa": True, "oa_status": "green"},
    "best_oa_location": {"pdf_url": "https://arxiv.org/pdf/2306.11932"},
    "abstract_inverted_index": {"Polis": [0], "is": [1], "a": [2], "platform": [3]},
}


def test_abstract_reconstruction_restores_word_order():
    assert reconstruct_abstract(WORK["abstract_inverted_index"]) == "Polis is a platform"


def test_repeated_words_land_in_all_positions():
    assert reconstruct_abstract({"the": [0, 2], "big": [1], "cat": [3]}) == "the big the cat"


def test_missing_abstract_returns_none():
    assert reconstruct_abstract(None) is None
    assert reconstruct_abstract({}) is None


def test_summarize_truncates_without_rewriting():
    abstract = " ".join(f"w{i}" for i in range(100))
    summary = summarize_abstract(abstract, max_words=40)
    assert summary.startswith("w0 w1")
    assert summary.endswith("…")
    # Corta o texto real; não reescreve. A reticência gruda na última palavra.
    assert len(summary.split()) == 40
    assert summary.split()[-1] == "w39…"


def test_summarize_leaves_short_abstract_intact():
    assert summarize_abstract("curto abstract") == "curto abstract"


def test_summarize_handles_missing_abstract():
    assert "sem abstract" in summarize_abstract(None)


def test_candidate_mapping_from_api_shape():
    candidate = OpenAlexClient._candidate_from_work(WORK)
    assert candidate is not None
    assert candidate.title == "Opportunities and Risks of LLMs"
    # DOI é normalizado: sem o prefixo de URL.
    assert candidate.doi == "10.48550/arxiv.2306.11932"
    assert candidate.authors == ["Christopher Small", "Ivan Vendrov"]
    assert candidate.year == 2023
    assert candidate.is_oa is True
    assert candidate.pdf_url == "https://arxiv.org/pdf/2306.11932"
    assert candidate.cited_by_count == 42


def test_work_without_title_is_rejected():
    assert OpenAlexClient._candidate_from_work({"id": "x", "title": None}) is None


def test_closed_work_maps_without_pdf():
    closed = {
        "id": "https://openalex.org/W9",
        "title": "Paywalled Paper",
        "doi": "https://doi.org/10.1111/x",
        "open_access": {"is_oa": False, "oa_status": "closed"},
        "primary_location": {
            "source": {"display_name": "The Journal of Politics"},
            "landing_page_url": "https://doi.org/10.1111/x",
        },
    }
    candidate = OpenAlexClient._candidate_from_work(closed)
    assert candidate.is_oa is False
    assert candidate.pdf_url is None
    # O link da plataforma hospedeira é o que vai para pending.md.
    assert candidate.host_platform == "The Journal of Politics"
    assert candidate.landing_page_url == "https://doi.org/10.1111/x"


def test_arxiv_url_derived_from_doi():
    candidate = OpenAlexClient._candidate_from_work(WORK)
    assert arxiv_pdf_url(candidate) == "https://arxiv.org/pdf/2306.11932"


def test_arxiv_url_none_for_non_arxiv():
    candidate = OpenAlexClient._candidate_from_work(
        {
            "id": "x",
            "title": "T",
            "doi": "https://doi.org/10.1111/j.1468-2508.2007.00494.x",
            "primary_location": {"landing_page_url": "https://onlinelibrary.wiley.com/x"},
        }
    )
    assert arxiv_pdf_url(candidate) is None
