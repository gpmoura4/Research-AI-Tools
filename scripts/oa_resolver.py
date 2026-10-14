"""Localização e download de PDFs open access.

Ordem: OpenAlex (já traz best_oa_location) -> arXiv -> Unpaywall.

NUNCA contorna bloqueio. Se não há PDF open access declarado, o resultado é uma
pendência com o link da plataforma hospedeira — não uma tentativa de acesso por
outro caminho.
"""

from __future__ import annotations

import re
import time
from dataclasses import dataclass
from pathlib import Path

import httpx

from scripts.config import Config, load_config
from scripts.openalex import USER_AGENT_TEMPLATE, Candidate


@dataclass
class ResolutionResult:
    """Desfecho da tentativa de obter o PDF de um candidato."""

    candidate: Candidate
    pdf_path: Path | None = None
    source: str | None = None  # openalex | arxiv | unpaywall
    blocked_reason: str | None = None
    host: str | None = None
    link: str | None = None
    url: str | None = None  # URL de onde o PDF foi efetivamente baixado

    @property
    def ok(self) -> bool:
        return self.pdf_path is not None


_ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})", re.I)
_ARXIV_DOI_RE = re.compile(r"10\.48550/arxiv\.([0-9]{4}\.[0-9]{4,5})", re.I)


def arxiv_pdf_url(candidate: Candidate) -> str | None:
    """Deriva a URL do PDF no arXiv a partir do DOI ou dos links do candidato."""
    haystack = " ".join(
        filter(None, [candidate.doi, candidate.landing_page_url, candidate.pdf_url])
    )
    match = _ARXIV_DOI_RE.search(haystack) or _ARXIV_ID_RE.search(haystack)
    if match:
        return f"https://arxiv.org/pdf/{match.group(1)}"
    return None


class OpenAccessResolver:
    def __init__(self, config: Config | None = None):
        self.config = config or load_config()
        self._client = httpx.Client(
            timeout=self.config.download.timeout_seconds,
            headers={
                # Identificação honesta, com e-mail de contato. NUNCA nos passamos
                # por navegador para driblar bloqueio: um 403 é registrado como
                # pendência, não contornado.
                "User-Agent": USER_AGENT_TEMPLATE.format(
                    email=self.config.polite_pool_email
                ),
                "Accept": "application/pdf,*/*",
            },
            follow_redirects=True,
        )

    def __enter__(self) -> OpenAccessResolver:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    def unpaywall_pdf_url(self, doi: str) -> str | None:
        """Consulta o Unpaywall como fallback quando o OpenAlex não traz PDF."""
        url = f"{self.config.unpaywall.base_url}/{doi}"
        try:
            response = self._client.get(
                url,
                params={"email": self.config.polite_pool_email},
                timeout=self.config.unpaywall.timeout_seconds,
            )
            if response.status_code != 200:
                return None
            payload = response.json()
        except (httpx.HTTPError, ValueError):
            return None

        best = payload.get("best_oa_location") or {}
        if best.get("url_for_pdf"):
            return best["url_for_pdf"]
        for location in payload.get("oa_locations") or []:
            if location.get("url_for_pdf"):
                return location["url_for_pdf"]
        return None

    def _deposited_formats(self, candidate: Candidate) -> str | None:
        """Formatos realmente depositados, quando o repositório expõe essa lista.

        Hoje cobre o Zenodo, onde é comum o depósito ser .docx em vez de PDF — o
        que faz o item parecer inacessível quando na verdade está aberto, só que
        em outro formato.
        """
        doi = (candidate.doi or "").lower()
        if "zenodo" not in doi:
            return None

        record_id = doi.rsplit(".", 1)[-1]
        if not record_id.isdigit():
            return None

        try:
            response = self._client.get(
                f"https://zenodo.org/api/records/{record_id}",
                timeout=self.config.unpaywall.timeout_seconds,
            )
            if response.status_code != 200:
                return None
            files = response.json().get("files") or []
        except (httpx.HTTPError, ValueError):
            return None

        names = [f.get("key", "") for f in files if f.get("key")]
        return ", ".join(names) if names else None

    def _download(self, url: str, destination: Path) -> tuple[bool, str | None]:
        """Baixa e valida que o conteúdo é mesmo um PDF.

        Uma página de paywall costuma responder 200 com HTML. Gravá-la como .pdf
        criaria um arquivo corrompido no acervo — por isso validamos o conteúdo,
        não apenas o status.
        """
        try:
            with self._client.stream("GET", url) as response:
                if response.status_code == 403:
                    # Editor bloqueia acesso automatizado. Não insistimos nem
                    # forjamos navegador — o PDF pode estar acessível no browser.
                    return False, "HTTP 403 (editor bloqueia download automatizado)"
                if response.status_code != 200:
                    return False, f"HTTP {response.status_code}"

                content_type = response.headers.get("content-type", "").lower()
                if "html" in content_type:
                    return False, "servidor devolveu HTML (provável paywall ou captcha)"

                max_bytes = self.config.download.max_size_mb * 1024 * 1024
                chunks: list[bytes] = []
                total = 0
                for chunk in response.iter_bytes():
                    chunks.append(chunk)
                    total += len(chunk)
                    if total > max_bytes:
                        return False, f"PDF acima de {self.config.download.max_size_mb}MB"

        except httpx.HTTPError as exc:
            return False, f"erro de rede: {type(exc).__name__}"

        content = b"".join(chunks)
        if not content.startswith(b"%PDF"):
            return False, "conteúdo baixado não é um PDF"

        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
        return True, None

    def resolve(self, candidate: Candidate, destination: Path) -> ResolutionResult:
        """Tenta obter o PDF do candidato, em ordem de confiabilidade da fonte."""
        host = candidate.host_platform or candidate.venue
        link = candidate.best_link

        attempts: list[tuple[str, str]] = []
        if candidate.pdf_url:
            attempts.append(("openalex", candidate.pdf_url))

        # Localizações secundárias: um repositório às vezes hospeda o PDF que a
        # fonte principal não declara.
        for url in candidate.alternate_pdf_urls:
            if url not in [u for _, u in attempts]:
                attempts.append(("openalex-alt", url))

        arxiv = arxiv_pdf_url(candidate)
        if arxiv and arxiv not in [u for _, u in attempts]:
            attempts.append(("arxiv", arxiv))

        # Unpaywall como fallback sempre que houver DOI — a cobertura dele difere
        # da do OpenAlex, então vale mesmo quando já há candidatos a URL.
        if candidate.doi:
            fallback = self.unpaywall_pdf_url(candidate.doi)
            if fallback and fallback not in [u for _, u in attempts]:
                attempts.append(("unpaywall", fallback))

        if not attempts:
            if candidate.is_oa:
                # Depósito aberto sem PDF costuma significar que o arquivo está em
                # outro formato (.docx, .zip). Descobrir qual poupa o usuário de
                # abrir a página para encontrar o mesmo.
                deposited = self._deposited_formats(candidate)
                if deposited:
                    reason = (
                        f"acesso aberto, mas o depósito não contém PDF — "
                        f"arquivo disponível: {deposited}. Baixar manualmente e "
                        f"converter, se quiser processá-lo."
                    )
                else:
                    reason = (
                        f"marcado open access ({candidate.oa_status}) mas nenhuma API "
                        "declara URL de PDF — verificar na página do editor"
                    )
            else:
                reason = f"acesso fechado (oa_status: {candidate.oa_status or 'desconhecido'})"

            return ResolutionResult(
                candidate=candidate, blocked_reason=reason, host=host, link=link
            )

        errors: list[str] = []
        for source, url in attempts:
            ok, error = self._download(url, destination)
            if ok:
                return ResolutionResult(
                    candidate=candidate,
                    pdf_path=destination,
                    source=source,
                    host=host,
                    link=link,
                    url=url,
                )
            errors.append(f"{source}: {error}")
            time.sleep(self.config.download.delay_between_seconds)

        return ResolutionResult(
            candidate=candidate,
            blocked_reason="; ".join(errors),
            host=host,
            link=link,
        )
