"""Cliente Crossref.

G1: BibTeX NUNCA é construído pelo modelo. Ou vem do endpoint de transform do
Crossref (servidor devolve o BibTeX pronto), ou de metadados extraídos do PDF
marcados como INCOMPLETE.
"""

from __future__ import annotations

import re
import time
import unicodedata
from dataclasses import dataclass
from difflib import SequenceMatcher

import httpx

from scripts.config import Config, load_config

USER_AGENT_TEMPLATE = (
    "research-workspace/0.1 (https://github.com/gpmoura4/Research-AI-Tools; mailto:{email})"
)


@dataclass
class CrossrefWork:
    """Metadados retornados pelo Crossref para uma obra."""

    doi: str
    title: str
    authors: list[str]  # sobrenomes, na ordem
    year: str | None
    container_title: str | None
    entry_type: str
    bibtex: str | None = None
    # Como chegamos até esta obra: "doi" (confiável) ou "title-search" (verificada).
    matched_by: str = "doi"
    match_score: float = 1.0


def normalize_title(title: str) -> str:
    """Forma canônica para comparação e dedupe: sem acento, pontuação ou caixa."""
    text = unicodedata.normalize("NFKD", title or "")
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9\s]", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


def title_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, normalize_title(a), normalize_title(b)).ratio()


class CrossrefClient:
    def __init__(self, config: Config | None = None):
        self.config = config or load_config()
        self._client = httpx.Client(
            timeout=self.config.crossref.timeout_seconds,
            headers={
                "User-Agent": USER_AGENT_TEMPLATE.format(
                    email=self.config.polite_pool_email
                )
            },
            follow_redirects=True,
        )

    def __enter__(self) -> CrossrefClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    def _get(self, url: str, **kwargs: object) -> httpx.Response | None:
        """GET com retry em erro transitório. Devolve None quando desiste."""
        last_exc: Exception | None = None
        for attempt in range(self.config.crossref.max_retries):
            try:
                response = self._client.get(url, **kwargs)  # type: ignore[arg-type]
                if response.status_code == 404:
                    return None
                if response.status_code == 429 or response.status_code >= 500:
                    # Backoff exponencial: respeita o rate limit do polite pool.
                    time.sleep(2**attempt)
                    continue
                response.raise_for_status()
                return response
            except httpx.HTTPError as exc:
                last_exc = exc
                time.sleep(2**attempt)
        if last_exc:
            return None
        return None

    def fetch_bibtex(self, doi: str) -> str | None:
        """BibTeX oficial do Crossref para um DOI. Esta é a fonte da verdade (G1)."""
        url = f"{self.config.crossref.base_url}/works/{doi}/transform/application/x-bibtex"
        response = self._get(url)
        if response is None:
            return None
        text = response.text.strip()
        return text if text.startswith("@") else None

    def search_works(self, query: str, rows: int = 5) -> list[CrossrefWork]:
        """Busca bibliográfica crua, sem threshold: quem chama decide a correspondência."""
        response = self._get(
            f"{self.config.crossref.base_url}/works",
            params={"query.bibliographic": query, "rows": str(rows)},
        )
        if response is None:
            return []
        try:
            items = response.json()["message"]["items"]
        except (KeyError, ValueError):
            return []
        return [w for w in (self._work_from_message(m) for m in items) if w]

    def fetch_abstract(self, doi: str) -> str | None:
        """Abstract depositado pelo editor no Crossref, sem as tags JATS."""
        response = self._get(f"{self.config.crossref.base_url}/works/{doi}")
        if response is None:
            return None
        try:
            raw = response.json()["message"].get("abstract") or ""
        except (KeyError, ValueError):
            return None
        text = re.sub(r"<[^>]+>", " ", raw)
        # O título "Abstract" costuma vir dentro do próprio campo.
        text = re.sub(r"^\s*abstract\s*", "", text, flags=re.I)
        return re.sub(r"\s+", " ", text).strip() or None

    def fetch_work(self, doi: str) -> CrossrefWork | None:
        """Metadados estruturados + BibTeX para um DOI conhecido."""
        url = f"{self.config.crossref.base_url}/works/{doi}"
        response = self._get(url)
        if response is None:
            return None
        try:
            message = response.json()["message"]
        except (KeyError, ValueError):
            return None

        work = self._work_from_message(message)
        if work:
            work.bibtex = self.fetch_bibtex(work.doi)
        return work

    def search_by_title(
        self, title: str, authors: list[str] | None = None
    ) -> CrossrefWork | None:
        """Busca por título quando o PDF não traz DOI.

        Só aceita a correspondência se o título bater acima do threshold — abaixo
        disso devolve None e o pipeline cria uma entrada INCOMPLETE (G1).
        """
        if not title or len(title.strip()) < 10:
            return None

        params: dict[str, str] = {"query.bibliographic": title, "rows": "5"}
        if authors:
            params["query.author"] = " ".join(authors[:3])

        url = f"{self.config.crossref.base_url}/works"
        response = self._get(url, params=params)
        if response is None:
            return None
        try:
            items = response.json()["message"]["items"]
        except (KeyError, ValueError):
            return None

        threshold = self.config.crossref.title_match_threshold
        best: CrossrefWork | None = None
        best_score = 0.0

        for item in items:
            candidate = self._work_from_message(item)
            if not candidate:
                continue
            score = title_similarity(title, candidate.title)
            if score > best_score:
                best, best_score = candidate, score

        if best is None or best_score < threshold:
            return None

        # Títulos curtos inflam a similaridade: "Attention is all you need" casa a
        # 0.88 com "Is Attention All You Need?", que é outro paper. Abaixo de uma
        # correspondência praticamente exata, exigimos confirmação por autor —
        # sem ela, é melhor uma entrada INCOMPLETE do que uma errada (G1).
        if best_score < 0.97 and not self._author_agrees(authors, best.authors):
            return None

        best.matched_by = "title-search"
        best.match_score = round(best_score, 3)
        best.bibtex = self.fetch_bibtex(best.doi)
        return best

    @staticmethod
    def _author_agrees(hint: list[str] | None, found: list[str]) -> bool:
        """Verifica se algum sobrenome do PDF aparece entre os autores do Crossref."""
        if not hint or not found:
            return False

        found_tokens = {
            token
            for name in found
            for token in normalize_title(name).split()
            if len(token) > 2
        }
        hint_tokens = {
            token
            for name in hint
            for token in normalize_title(name).split()
            if len(token) > 2
        }
        return bool(found_tokens & hint_tokens)

    @staticmethod
    def _work_from_message(message: dict) -> CrossrefWork | None:
        doi = (message.get("DOI") or "").strip()
        titles = message.get("title") or []
        title = titles[0].strip() if titles else ""
        if not doi or not title:
            return None

        authors: list[str] = []
        for author in message.get("author") or []:
            family = (author.get("family") or "").strip()
            if family:
                authors.append(family)
            elif author.get("name"):
                # Autoria institucional.
                authors.append(author["name"].strip())

        year: str | None = None
        for key in ("published-print", "published-online", "issued", "created"):
            parts = (message.get(key) or {}).get("date-parts") or []
            if parts and parts[0] and parts[0][0]:
                year = str(parts[0][0])
                break

        containers = message.get("container-title") or []

        return CrossrefWork(
            doi=doi,
            title=title,
            authors=authors,
            year=year,
            container_title=containers[0] if containers else None,
            entry_type=(message.get("type") or "article").strip(),
        )
