"""Testes da decomposição de referências MDPI e da regra de aceite de correspondência."""

from scripts.manuscript_refs import Reference, _accept, _is_preprint, parse_reference


def test_preprint_dois_are_recognized():
    assert _is_preprint("10.2139/ssrn.5180249", "journal-article")
    assert _is_preprint("10.31234/osf.io/hkqyv", None)
    assert _is_preprint("10.1234/x", "posted-content")
    assert not _is_preprint("10.1126/science.abp9364", "journal-article")


def test_article_with_multiword_surname():
    ref = parse_reference(
        69,
        "Van Bavel, J.J.; Pereira, A. The Partisan Brain: An Identity-Based Model of "
        "Political Belief. Trends Cogn. Sci. 2018, 22, 213–224.",
    )
    assert ref.first_surname == "Van Bavel"
    assert ref.title == "The Partisan Brain: An Identity-Based Model of Political Belief"
    assert ref.year == 2018
    assert ref.kind == "article"
    assert ref.filename.startswith("Van Bavel e Pereira - 2018 - The Partisan Brain")


def test_et_al_counts_as_three_or_more_authors():
    ref = parse_reference(
        12,
        "Voelkel, J.G.; et al. Megastudy Testing 25 Treatments to Reduce Antidemocratic "
        "Attitudes and Partisan Animosity. Science 2024. [conferir referência completa]",
    )
    assert ref.et_al
    assert ref.year == 2024
    assert ref.filename.startswith("Voelkel et al - 2024 - Megastudy")


def test_us_abbreviation_does_not_end_title():
    ref = parse_reference(
        29,
        "Adamic, L.A.; Glance, N. The Political Blogosphere and the 2004 U.S. Election: "
        "Divided They Blog. In Proceedings of the 3rd International Workshop on Link "
        "Discovery (LinkKDD '05), Chicago, IL, USA, 2005; pp. 36–43.",
    )
    assert ref.title.endswith("U.S. Election: Divided They Blog")
    assert ref.kind == "proceedings"
    assert ref.year == 2005


def test_question_mark_keeps_subtitle_but_not_journal():
    with_subtitle = parse_reference(
        87,
        "Marx, G.T. What's in a Name? Some Reflections on the Sociology of Anonymity. "
        "Inf. Soc. 1999, 15, 99–112.",
    )
    assert with_subtitle.title == "What's in a Name? Some Reflections on the Sociology of Anonymity"

    no_subtitle = parse_reference(
        99,
        "Henrich, J.; Heine, S.J.; Norenzayan, A. The Weirdest People in the World? "
        "Behav. Brain Sci. 2010, 33, 61–83.",
    )
    assert no_subtitle.title == "The Weirdest People in the World?"


def test_book_and_chapter_kinds():
    book = parse_reference(
        18, "Chadwick, A. The Hybrid Media System: Politics and Power; Oxford University "
        "Press: Oxford, UK, 2013.",
    )
    assert book.kind == "book" and book.year == 2013

    chapter = parse_reference(
        33, "Gibson, J.J. The Theory of Affordances. In Perceiving, Acting, and Knowing; "
        "Shaw, R., Bransford, J., Eds.; Lawrence Erlbaum: Hillsdale, NJ, USA, 1977; pp. 67–82.",
    )
    assert chapter.kind == "chapter" and chapter.title == "The Theory of Affordances"


def test_editors_and_lowercase_initials():
    ref = parse_reference(
        60, "Marwick, A.E.; boyd, d. I Tweet Honestly, I Tweet Passionately: Twitter Users, "
        "Context Collapse, and the Imagined Audience. New Media Soc. 2011, 13, 114–133.",
    )
    assert ref.authors == ["Marwick, A.E.", "boyd, d."]
    assert ref.title.startswith("I Tweet Honestly")


def _ref(year: int = 2020) -> Reference:
    return Reference(n=1, text="", authors=["Smith, J."], et_al=False, title="A title",
                     year=year, kind="article", has_pdf=False)


def test_accept_always_requires_author_when_known():
    assert _accept(_ref(), 0.95, ["Smith", "Doe"], 2020)
    assert not _accept(_ref(), 0.95, ["Doe"], 2020)
    # Mesmo título exato, outro autor: resenha do livro, não o livro.
    assert not _accept(_ref(), 1.0, ["Allen"], 2020)


def test_accept_without_authors_needs_near_exact_title():
    assert _accept(_ref(), 0.99, [], 2020)
    assert not _accept(_ref(), 0.90, [], 2020)


def test_accept_rejects_distant_year_and_low_score():
    assert not _accept(_ref(2020), 1.0, ["Smith"], 2010)
    assert not _accept(_ref(), 0.80, ["Smith"], 2020)
