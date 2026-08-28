"""Carregamento do config.yaml da raiz do workspace."""

from __future__ import annotations

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
class Config:
    max_papers_per_run: int
    polite_pool_email: str
    default_summary_language: str
    title_max_chars: int
    crossref: CrossrefConfig


@lru_cache(maxsize=1)
def load_config(path: Path | None = None) -> Config:
    config_path = path or CONFIG_PATH
    if not config_path.exists():
        raise FileNotFoundError(f"config.yaml não encontrado em {config_path}")

    raw = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    crossref_raw = raw.get("crossref", {})

    return Config(
        max_papers_per_run=int(raw.get("max_papers_per_run", 30)),
        polite_pool_email=str(raw.get("polite_pool_email", "")),
        default_summary_language=str(raw.get("default_summary_language", "en")),
        title_max_chars=int(raw.get("title_max_chars", 80)),
        crossref=CrossrefConfig(
            base_url=str(crossref_raw.get("base_url", "https://api.crossref.org")),
            timeout_seconds=int(crossref_raw.get("timeout_seconds", 30)),
            max_retries=int(crossref_raw.get("max_retries", 3)),
            title_match_threshold=float(crossref_raw.get("title_match_threshold", 0.85)),
        ),
    )
