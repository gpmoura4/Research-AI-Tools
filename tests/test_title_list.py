"""Testes do download por lista de títulos: correspondência (G2), idioma (G7), retomada."""

from pathlib import Path

from scripts import title_list as tl
from scripts.openalex import Candidate


def make_candidate(title: str, doi: str | None = None, **kwargs) -> Candidate:
    defaults = dict(
        openalex_id=f"https://openalex.org/W{abs(hash((title, doi))) % 10**8}",
        title=title,
        authors=["Alice Silva"],
        year=2021,
        venue="Journal of Testing",
        doi=doi,
        abstract="An abstract in English describing echo chambers on social media platforms.",
        is_oa=True,
        oa_status="green",
        pdf_url=None,
        landing_page_url=None,
        host_platform="Journal of Testing",
        work_type="article",
    )
    defaults.update(kwargs)
    return Candidate(**defaults)


def test_clean_title_strips_dblp_venue_prefix():
    assert tl.clean_title("HICSS - The Impact of Online Disinformation") == (
        "The Impact of Online Disinformation"
    )
    assert tl.clean_title("WWW - Searching for polarization") == "Searching for polarization"
    # Hífen dentro do título não é prefixo de venue.
    assert tl.clean_title("Echo chambers - a review") == "Echo chambers - a review"


def test_search_query_removes_openalex_wildcards():
    query = tl.search_query("Augmenting polarization via social media? A comparative analysis")
    assert "?" not in query
    assert query == "Augmenting polarization via social media A comparative analysis"


def test_pick_match_rejects_below_threshold():
    results = [make_candidate("A completely different paper about elections")]
    match, score = tl.pick_match("Echo chambers on Reddit", results, threshold=0.85)
    assert match is None
    assert score < 0.85


def test_pick_match_prefers_published_version_and_merges_preprint_pdf():
    title = "Echo chambers can emerge without algorithmic personalization"
    preprint = make_candidate(
        title, doi=None, work_type="preprint", pdf_url="https://arxiv.org/pdf/2501.00001"
    )
    published = make_candidate(title, doi="10.1/abc")
    match, score = tl.pick_match(title + ".", [preprint, published], threshold=0.85)
    assert match is published
    assert score == 1.0
    assert "https://arxiv.org/pdf/2501.00001" in match.alternate_pdf_urls


def test_language_trusts_text_over_journal_metadata():
    # Artigo em inglês num periódico espanhol: o OpenAlex marca 'es'.
    candidate = make_candidate("The grammatization of emotions on Facebook", language="es")
    assert tl.language_rejection(candidate, ("en", "pt")) is None


def test_language_rejects_text_in_other_language():
    candidate = make_candidate(
        "La gramatización de las emociones en Facebook",
        abstract="Este artículo propone el análisis de las reacciones y emociones de los "
        "usuarios en la red social durante las elecciones al Parlamento de Cataluña.",
        language="es",
    )
    assert tl.language_rejection(candidate, ("en", "pt")) is not None


def test_reset_for_retry_requeues_only_unobtained(tmp_path: Path):
    store = tl.StatusStore(tmp_path / "state.json")
    store.items.extend([
        {"n": 1, "input_title": "a", "status": tl.DOWNLOADED},
        {"n": 2, "input_title": "b", "status": tl.NOT_DOWNLOADED, "reason": "HTTP 503"},
        {"n": 3, "input_title": "c", "status": tl.NOT_FOUND, "reason": "x"},
        {"n": 4, "input_title": "d", "status": tl.LANGUAGE_DISCARDED, "reason": "es"},
    ])
    assert tl.reset_for_retry(store) == 3
    assert [i["status"] for i in store.items] == [
        tl.DOWNLOADED, tl.MATCHED, tl.UNRESOLVED, tl.MATCHED
    ]
    assert "reason" not in store.items[1]
