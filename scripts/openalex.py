"""Cliente OpenAlex — busca principal de candidatos.

G2: todo candidato apresentado ao usuário vem de uma resposta real desta API,
com DOI ou URL verificável. Nada é acrescentado pelo modelo.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field

import httpx

from scripts.config import Config, load_config

USER_AGENT_TEMPLATE = (
    "research-workspace/0.1 (https://github.com/gpmoura4/Research-AI-Tools; mailto:{email})"
)


@dataclass
class Candidate:
    """Um trabalho retornado pela busca. Todos os campos vêm da API."""

    openalex_id: str
    title: str
    authors: list[str]  # nomes completos, na ordem
    year: int | None
    venue: str | None
    doi: str | None
    abstract: str | None
    is_oa: bool
    oa_status: str | None  # gold | green | hybrid | bronze | closed
    pdf_url: str | None
    landing_page_url: str | None
    host_platform: str | None
    work_type: str | None
    language: str | None = None
    cited_by_count: int = 0
    # Relevância textual calculada pelo OpenAlex para a consulta. É o sinal certo
    # para ordenar candidatos: citações medem fama, não aderência ao tema.
    relevance_score: float = 0.0
    # Todas as URLs de PDF declaradas em `locations`, não só a melhor: um
    # repositório secundário às vezes hospeda o PDF que a fonte principal omite.
    alternate_pdf_urls: list[str] = field(default_factory=list)
    # Preenchidos depois pelo agente (score) e pelo dedupe.
    score: int | None = None
    score_reason: str | None = None
    duplicate_of: str | None = None
    queries: list[str] = field(default_factory=list)

    @property
    def doi_url(self) -> str | None:
        if not self.doi:
            return None
        return f"https://doi.org/{self.doi}"

    @property
    def best_link(self) -> str | None:
        """Melhor link para o usuário conferir a fonte."""
        return self.doi_url or self.landing_page_url or self.pdf_url


def reconstruct_abstract(inverted_index: dict[str, list[int]] | None) -> str | None:
    """Reconstrói o texto a partir do índice invertido do OpenAlex.

    A API não devolve o abstract como texto corrido: entrega um mapa
    palavra -> posições. Sem esta reconstrução não há abstract para julgar.
    """
    if not inverted_index:
        return None

    positions: dict[int, str] = {}
    for word, indexes in inverted_index.items():
        for index in indexes:
            positions[index] = word

    if not positions:
        return None
    return " ".join(positions[i] for i in sorted(positions))


def summarize_abstract(abstract: str | None, max_words: int = 40) -> str:
    """Encurta o abstract para a tabela de candidatos, sem reescrevê-lo.

    Corta o texto real em vez de parafrasear: o usuário precisa ver o que a API
    devolveu, não a minha versão dele.
    """
    if not abstract:
        return "(sem abstract na API)"
    words = abstract.split()
    if len(words) <= max_words:
        return abstract
    return " ".join(words[:max_words]) + "…"


def _normalize_doi(raw: str | None) -> str | None:
    """OpenAlex devolve o DOI como URL; guardamos só o identificador."""
    if not raw:
        return None
    doi = raw.strip().lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if doi.startswith(prefix):
            doi = doi[len(prefix) :]
    return doi or None


class OpenAlexClient:
    def __init__(self, config: Config | None = None):
        self.config = config or load_config()
        headers = {
            "User-Agent": USER_AGENT_TEMPLATE.format(email=self.config.polite_pool_email)
        }
        if self.config.openalex.api_key:
            # No header, não na URL: assim a chave não aparece em logs nem em mensagens de erro.
            headers["Authorization"] = f"Bearer {self.config.openalex.api_key}"
        self._client = httpx.Client(
            timeout=self.config.openalex.timeout_seconds,
            headers=headers,
            follow_redirects=True,
        )

    def __enter__(self) -> OpenAlexClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    def _get(self, url: str, params: dict[str, str]) -> dict | None:
        """GET com retry em erro transitório. Devolve None quando desiste."""
        params = {**params, "mailto": self.config.polite_pool_email}
        for attempt in range(self.config.openalex.max_retries):
            try:
                response = self._client.get(url, params=params)
                if response.status_code == 404:
                    return None
                if response.status_code == 429 or response.status_code >= 500:
                    time.sleep(2**attempt)
                    continue
                response.raise_for_status()
                return response.json()
            except (httpx.HTTPError, ValueError):
                time.sleep(2**attempt)
        return None

    def search(
        self,
        query: str,
        per_page: int | None = None,
        from_year: int | None = None,
        to_year: int | None = None,
        work_types: list[str] | None = None,
        precise: bool = False,
        languages: tuple[str, ...] | None = None,
    ) -> list[Candidate]:
        """Busca trabalhos, com filtros opcionais.

        `precise=True` usa o filtro `title_and_abstract.search`, que respeita
        frases entre aspas e operadores AND/OR/NOT. É muito mais restritivo que a
        busca livre: para um tema de interseção ("WBS" E "LLM"), a busca livre
        devolve centenas de itens sobre LLM em geral, enquanto o filtro devolve
        apenas os que realmente tratam dos dois assuntos.
        """
        filters: list[str] = []
        if from_year:
            filters.append(f"from_publication_date:{from_year}-01-01")
        if to_year:
            filters.append(f"to_publication_date:{to_year}-12-31")
        if work_types:
            filters.append(f"type:{'|'.join(work_types)}")
        if languages:
            # G7 — filtra na origem para não gastar as vagas do limite de 30 com
            # papers que o usuário não conseguiria ler.
            filters.append(f"language:{'|'.join(languages)}")

        params: dict[str, str] = {
            "per-page": str(per_page or self.config.openalex.results_per_query),
            # Sem isto a API devolve os mais citados, e papers famosos de temas
            # vizinhos afogam os que realmente tratam do assunto buscado.
            "sort": "relevance_score:desc",
        }

        if precise:
            # Vírgula separa filtros na sintaxe do OpenAlex; num valor de busca ela
            # quebraria a query em dois filtros inválidos.
            filters.append(f"title_and_abstract.search:{query.replace(',', ' ')}")
        else:
            params["search"] = query

        if filters:
            params["filter"] = ",".join(filters)

        payload = self._get(f"{self.config.openalex.base_url}/works", params)
        if not payload:
            return []

        candidates: list[Candidate] = []
        for item in payload.get("results", []):
            candidate = self._candidate_from_work(item)
            if candidate:
                candidate.queries = [query]
                candidates.append(candidate)
        return candidates

    def fetch_by_doi(self, doi: str) -> Candidate | None:
        payload = self._get(
            f"{self.config.openalex.base_url}/works/https://doi.org/{doi}", {}
        )
        if not payload:
            return None
        return self._candidate_from_work(payload)

    @staticmethod
    def _candidate_from_work(work: dict) -> Candidate | None:
        title = (work.get("title") or "").strip()
        openalex_id = (work.get("id") or "").strip()
        if not title or not openalex_id:
            return None

        authors = [
            (a.get("author") or {}).get("display_name", "").strip()
            for a in work.get("authorships", [])
        ]
        authors = [a for a in authors if a]

        primary = work.get("primary_location") or {}
        source = primary.get("source") or {}
        open_access = work.get("open_access") or {}
        best_oa = work.get("best_oa_location") or {}

        best_pdf = best_oa.get("pdf_url")
        alternates: list[str] = []
        for location in work.get("locations") or []:
            url = location.get("pdf_url")
            if url and url != best_pdf and url not in alternates:
                alternates.append(url)

        return Candidate(
            openalex_id=openalex_id,
            title=title,
            authors=authors,
            year=work.get("publication_year"),
            venue=source.get("display_name"),
            doi=_normalize_doi(work.get("doi")),
            abstract=reconstruct_abstract(work.get("abstract_inverted_index")),
            is_oa=bool(open_access.get("is_oa")),
            oa_status=open_access.get("oa_status"),
            pdf_url=best_pdf,
            alternate_pdf_urls=alternates,
            landing_page_url=primary.get("landing_page_url")
            or best_oa.get("landing_page_url"),
            host_platform=source.get("display_name"),
            work_type=work.get("type"),
            language=(work.get("language") or None),
            cited_by_count=int(work.get("cited_by_count") or 0),
            relevance_score=float(work.get("relevance_score") or 0.0),
        )
