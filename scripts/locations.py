"""Resolução de localizações: areas/<area>/<projeto>/<tema>/.

O agente NUNCA assume a área por conta própria (CLAUDE.md, fluxo 1). Este módulo
apenas lista o que existe e cria a estrutura sob demanda — a escolha é do usuário.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from scripts.config import REPO_ROOT

AREAS_ROOT = REPO_ROOT / "areas"

CONTEXT_TEMPLATE = """# Contexto do tema: {theme}

> Preencha este arquivo. Ele orienta os resumos (campo "Relevance to theme")
> e, mais adiante, as buscas de literatura.

## Pergunta de pesquisa


## Escopo
O que está dentro e o que está fora deste tema.

## Conceitos-chave


## Notas
"""


def slugify(text: str) -> str:
    """Converte um nome livre em slug de diretório."""
    normalized = unicodedata.normalize("NFKD", text or "")
    stripped = "".join(c for c in normalized if not unicodedata.combining(c))
    slug = re.sub(r"[^a-z0-9]+", "-", stripped.lower()).strip("-")
    return slug or "sem-nome"


@dataclass(frozen=True)
class Location:
    area: str
    project: str
    theme: str

    @property
    def path(self) -> Path:
        return AREAS_ROOT / self.area / self.project / self.theme

    @property
    def context_file(self) -> Path:
        return self.path / "context.md"

    @property
    def search_protocol(self) -> Path:
        return self.path / "search-protocol.md"

    @property
    def screening_protocol(self) -> Path:
        return self.path / "screening-protocol.md"

    @property
    def materials_dir(self) -> Path:
        return self.path / "materials"

    @property
    def deliverables_dir(self) -> Path:
        return self.path / "deliverables"

    @property
    def papers_dir(self) -> Path:
        return self.deliverables_dir / "papers"

    @property
    def summaries_dir(self) -> Path:
        return self.deliverables_dir / "summaries"

    @property
    def references_bib(self) -> Path:
        return self.deliverables_dir / "references.bib"

    @property
    def pending_md(self) -> Path:
        return self.deliverables_dir / "pending.md"

    @property
    def candidates_md(self) -> Path:
        return self.deliverables_dir / "candidates.md"

    @property
    def maps_dir(self) -> Path:
        return self.deliverables_dir / "maps"

    def exists(self) -> bool:
        return self.path.is_dir()

    def __str__(self) -> str:
        return f"{self.area}/{self.project}/{self.theme}"


def list_areas() -> list[str]:
    if not AREAS_ROOT.is_dir():
        return []
    return sorted(p.name for p in AREAS_ROOT.iterdir() if p.is_dir())


def list_projects(area: str) -> list[str]:
    area_path = AREAS_ROOT / area
    if not area_path.is_dir():
        return []
    return sorted(p.name for p in area_path.iterdir() if p.is_dir())


def list_themes(area: str, project: str) -> list[str]:
    project_path = AREAS_ROOT / area / project
    if not project_path.is_dir():
        return []
    return sorted(p.name for p in project_path.iterdir() if p.is_dir())


def list_all_locations() -> list[Location]:
    locations: list[Location] = []
    for area in list_areas():
        for project in list_projects(area):
            for theme in list_themes(area, project):
                locations.append(Location(area, project, theme))
    return locations


def ensure_location(location: Location, theme_display_name: str | None = None) -> Location:
    """Cria a estrutura completa do tema, sem sobrescrever nada existente."""
    for directory in (
        location.materials_dir,
        location.papers_dir,
        location.summaries_dir,
        location.maps_dir,
    ):
        directory.mkdir(parents=True, exist_ok=True)
        gitkeep = directory / ".gitkeep"
        if not any(directory.iterdir()):
            gitkeep.touch()

    if not location.context_file.exists():
        location.context_file.write_text(
            CONTEXT_TEMPLATE.format(theme=theme_display_name or location.theme),
            encoding="utf-8",
        )

    if not location.references_bib.exists():
        from scripts.bibtex import write_bib_file

        write_bib_file(location.references_bib, [])

    if not location.pending_md.exists():
        # Mesmo cabeçalho que append_pending usa: as colunas precisam bater com
        # as linhas que ele grava, senão a tabela renderiza quebrada.
        from scripts.candidates import PENDING_HEADER

        location.pending_md.write_text(PENDING_HEADER, encoding="utf-8")

    if not location.candidates_md.exists():
        location.candidates_md.write_text(
            "# Candidatos\n\nAguardando aprovação por item.\n",
            encoding="utf-8",
        )

    return location


def parse_location(raw: str) -> Location | None:
    """Interpreta 'area/projeto/tema' já em formato de caminho."""
    parts = [p for p in re.split(r"[/\\]", raw.strip()) if p]
    if len(parts) != 3:
        return None
    return Location(slugify(parts[0]), slugify(parts[1]), slugify(parts[2]))
