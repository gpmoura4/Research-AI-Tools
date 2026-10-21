"""Carregamento do config.yaml da raiz do workspace."""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "config.yaml"


@dataclass(frozen=True)
class CrossrefConfig:
    base_url: str
    timeout_seconds: int
    max_retries: int
    title_match_threshold: float


@dataclass(frozen=True)
class OpenAlexConfig:
    base_url: str
    timeout_seconds: int
    max_retries: int
    results_per_query: int
    # Chave da API: orçamento diário próprio, em vez do gratuito dividido por IP.
    # Nunca vem do config.yaml (versionado): vem de OPENALEX_API_KEY ou de api_key_file.
    api_key: str | None = None


@dataclass(frozen=True)
class UnpaywallConfig:
    base_url: str
    timeout_seconds: int


@dataclass(frozen=True)
class DownloadConfig:
    timeout_seconds: int
    delay_between_seconds: float
    max_size_mb: int


@dataclass(frozen=True)
class Config:
    max_papers_per_run: int
    polite_pool_email: str
    default_summary_language: str
    accepted_languages: tuple[str, ...]
    title_max_chars: int
    crossref: CrossrefConfig
    openalex: OpenAlexConfig
    unpaywall: UnpaywallConfig
    download: DownloadConfig
    # JSON da conta de serviço do Google Docs (fora do Git, em credentials/). Só o caminho.
    google_service_account_file: Path | None = None
    # JSON do cliente OAuth "Desktop app" (troca de figuras via Drive do usuário). Só o caminho.
    google_oauth_client_file: Path | None = None


def _google_service_account_file(google_docs_raw: dict) -> Path | None:
    """Caminho do JSON da conta de serviço, relativo à raiz do workspace (se configurado)."""
    raw_path = google_docs_raw.get("service_account_file")
    return REPO_ROOT / str(raw_path) if raw_path else None


def _google_oauth_client_file(google_docs_raw: dict) -> Path | None:
    """Caminho do JSON do cliente OAuth, relativo à raiz do workspace (se configurado)."""
    raw_path = google_docs_raw.get("oauth_client_file")
    return REPO_ROOT / str(raw_path) if raw_path else None


def _openalex_api_key(openalex_raw: dict) -> str | None:
    """OPENALEX_API_KEY tem precedência; senão, o arquivo apontado no config (fora do Git)."""
    if os.environ.get("OPENALEX_API_KEY"):
        return os.environ["OPENALEX_API_KEY"].strip()
    key_file = REPO_ROOT / str(openalex_raw.get("api_key_file", "credentials/openalex/api_key.txt"))
    if key_file.exists():
        return key_file.read_text(encoding="utf-8").strip() or None
    return None


@lru_cache(maxsize=1)
def load_config(path: Path | None = None) -> Config:
    config_path = path or CONFIG_PATH
    if not config_path.exists():
        raise FileNotFoundError(f"config.yaml não encontrado em {config_path}")

    raw = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    crossref_raw = raw.get("crossref", {})
    openalex_raw = raw.get("openalex", {})
    unpaywall_raw = raw.get("unpaywall", {})
    download_raw = raw.get("download", {})

    return Config(
        max_papers_per_run=int(raw.get("max_papers_per_run", 30)),
        polite_pool_email=str(raw.get("polite_pool_email", "")),
        default_summary_language=str(raw.get("default_summary_language", "en")),
        accepted_languages=tuple(
            str(lang).lower() for lang in (raw.get("accepted_languages") or ["en", "pt"])
        ),
        title_max_chars=int(raw.get("title_max_chars", 80)),
        crossref=CrossrefConfig(
            base_url=str(crossref_raw.get("base_url", "https://api.crossref.org")),
            timeout_seconds=int(crossref_raw.get("timeout_seconds", 30)),
            max_retries=int(crossref_raw.get("max_retries", 3)),
            title_match_threshold=float(crossref_raw.get("title_match_threshold", 0.85)),
        ),
        openalex=OpenAlexConfig(
            base_url=str(openalex_raw.get("base_url", "https://api.openalex.org")),
            timeout_seconds=int(openalex_raw.get("timeout_seconds", 30)),
            max_retries=int(openalex_raw.get("max_retries", 3)),
            results_per_query=int(openalex_raw.get("results_per_query", 50)),
            api_key=_openalex_api_key(openalex_raw),
        ),
        unpaywall=UnpaywallConfig(
            base_url=str(unpaywall_raw.get("base_url", "https://api.unpaywall.org/v2")),
            timeout_seconds=int(unpaywall_raw.get("timeout_seconds", 30)),
        ),
        download=DownloadConfig(
            timeout_seconds=int(download_raw.get("timeout_seconds", 120)),
            delay_between_seconds=float(download_raw.get("delay_between_seconds", 1.5)),
            max_size_mb=int(download_raw.get("max_size_mb", 80)),
        ),
        google_service_account_file=_google_service_account_file(raw.get("google_docs") or {}),
        google_oauth_client_file=_google_oauth_client_file(raw.get("google_docs") or {}),
    )
