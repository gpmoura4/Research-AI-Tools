"""Gera as figuras por affordance (Figuras 4-14) a partir de famo_data.json.

Uso (da raiz do repositório):
    uv run --with matplotlib python manuscripts/smip-famo-framework/adjustments/T06-figuras/gen_affordance_figs.py AF1 [AF2 ...]
Sem argumentos, gera as 11. Saída em out/ (fora do Git): figNN-AFk.svg e figNN-AFk.png (600 dpi).
"""
from __future__ import annotations

import json
import re
import sys
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
DATA = json.loads((HERE / "famo_data.json").read_text())

plt.rcParams.update({
    "font.family": "Arial",
    "svg.fonttype": "path",
})

# Okabe-Ito (seguro para daltonismo): borda/rótulo do bloco; fundo = versão clara.
BLOCK_COLOR = {
    "A": "#E69F00", "B": "#56B4E9", "C": "#009E73", "D": "#C9B400",
    "E": "#0072B2", "F": "#D55E00", "G": "#CC79A7",
}
INK = "#222222"
LINE = "#4D4D4D"
AF_FILL = "#EDEFF2"
AF_EDGE = "#4A5563"

# Geometria em polegadas (largura de 14,9 cm).
W = 5.85
ROW = 0.25          # altura de uma linha de mecanismo
HEAD = 0.25         # cabeçalho do bloco
GAP = 0.10          # espaço entre blocos
PAD_TOP = 0.08
X_AF0, X_AF1 = 0.05, 1.75
X_TRUNK = 2.05
X_GRP0, X_GRP1 = 2.30, 5.80
X_MECH0 = 2.42
LEGEND_H = 0.42


def parse_link(raw: str) -> tuple[str, str]:
    m = re.fullmatch(r"([A-G]\d+)(\*|\(-\)|\(±\))?", raw)
    if not m:
        raise ValueError(f"ligação inválida: {raw}")
    kind = {None: "direct", "*": "indirect", "(-)": "weakens", "(±)": "depends"}[m.group(2)]
    return m.group(1), kind


def sort_key(mid: str) -> tuple[str, int]:
    return mid[0], int(mid[1:])


def tint(hex_color: str, amount: float = 0.86) -> tuple[float, float, float]:
    r, g, b = (int(hex_color[i:i + 2], 16) / 255 for i in (1, 3, 5))
    return (r + (1 - r) * amount, g + (1 - g) * amount, b + (1 - b) * amount)


def draw(af_id: str) -> Path:
    af = DATA["affordances"][af_id]
    links = sorted((parse_link(x) for x in af["links"]), key=lambda t: sort_key(t[0]))
    groups: dict[str, list[tuple[str, str]]] = {}
    for mid, kind in links:
        groups.setdefault(mid[0], []).append((mid, kind))

    body_h = PAD_TOP + sum(HEAD + ROW * len(v) + GAP for v in groups.values())
    H = body_h + LEGEND_H
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)  # y cresce para baixo
    ax.axis("off")

    # Blocos e mecanismos
    y = PAD_TOP
    rows: list[tuple[float, str]] = []
    for b, items in groups.items():
        color = BLOCK_COLOR[b]
        gh = HEAD + ROW * len(items)
        ax.add_patch(FancyBboxPatch((X_GRP0, y), X_GRP1 - X_GRP0, gh,
                                    boxstyle="round,pad=0,rounding_size=0.05",
                                    fc=tint(color, 0.88), ec=color, lw=0.9))
        ax.text(X_GRP0 + 0.10, y + HEAD * 0.55, f"Block {b}. {DATA['blocks'][b]}",
                fontsize=8, fontweight="bold", color=INK, va="center")
        for i, (mid, kind) in enumerate(items):
            yc = y + HEAD + ROW * (i + 0.5)
            ax.add_patch(FancyBboxPatch((X_MECH0, yc - ROW * 0.40), X_GRP1 - X_MECH0 - 0.10, ROW * 0.80,
                                        boxstyle="round,pad=0,rounding_size=0.04",
                                        fc="white", ec=color, lw=0.6))
            mark = {"weakens": "  (−)", "depends": "  (±)"}.get(kind, "")
            ax.text(X_MECH0 + 0.09, yc, mid, fontsize=8.5, fontweight="bold", color=INK, va="center")
            ax.text(X_MECH0 + 0.40, yc, DATA["mechanisms"][mid] + mark, fontsize=8.5, color=INK, va="center")
            rows.append((yc, kind))
        y += gh + GAP

    # Affordance
    y_top, y_bot = rows[0][0], rows[-1][0]
    y_mid = (y_top + y_bot) / 2
    name = textwrap.fill(af["name"], 18)
    n_lines = name.count("\n") + 1
    box_h = 0.42 + 0.16 * n_lines
    ax.add_patch(FancyBboxPatch((X_AF0, y_mid - box_h / 2), X_AF1 - X_AF0, box_h,
                                boxstyle="round,pad=0,rounding_size=0.06",
                                fc=AF_FILL, ec=AF_EDGE, lw=1.0))
    ax.text((X_AF0 + X_AF1) / 2, y_mid - box_h / 2 + 0.17, af_id, fontsize=10, fontweight="bold",
            color=INK, ha="center", va="center")
    ax.text((X_AF0 + X_AF1) / 2, y_mid + 0.11, name, fontsize=9, color=INK, ha="center", va="center",
            linespacing=1.15)

    # Tronco e ramos
    ax.plot([X_AF1, X_TRUNK], [y_mid, y_mid], color=LINE, lw=1.0, solid_capstyle="butt")
    ax.plot([X_TRUNK, X_TRUNK], [min(y_top, y_mid), max(y_bot, y_mid)], color=LINE, lw=1.0)
    for yc, kind in rows:
        ls = {"direct": "-", "indirect": (0, (3, 2)), "weakens": "-", "depends": (0, (1, 1.5))}[kind]
        style = "-[,widthB=3.5,lengthB=0" if kind == "weakens" else "-|>,head_length=4,head_width=2.2"
        ax.add_patch(FancyArrowPatch((X_TRUNK, yc), (X_MECH0, yc), arrowstyle=style,
                                     linestyle=ls, color=LINE, lw=1.0, shrinkA=0, shrinkB=0.5,
                                     mutation_scale=1))

    # Legenda (só os tipos presentes)
    present = []
    for k in ("direct", "indirect", "weakens", "depends"):
        if any(kind == k for _, kind in rows):
            present.append(k)
    labels = {"direct": "Direct link", "indirect": "Indirect link",
              "weakens": "Can weaken the mechanism (−)", "depends": "Sign depends on design (±)"}
    ly = body_h + LEGEND_H * 0.45
    lx = X_AF0
    for k in present:
        ls = {"direct": "-", "indirect": (0, (3, 2)), "weakens": "-", "depends": (0, (1, 1.5))}[k]
        style = "-[,widthB=3.5,lengthB=0" if k == "weakens" else "-|>,head_length=4,head_width=2.2"
        ax.add_patch(FancyArrowPatch((lx, ly), (lx + 0.40, ly), arrowstyle=style, linestyle=ls,
                                     color=LINE, lw=1.0, shrinkA=0, shrinkB=0, mutation_scale=1))
        t = ax.text(lx + 0.50, ly, labels[k], fontsize=8, color=INK, va="center")
        fig.canvas.draw()
        bb = t.get_window_extent().transformed(ax.transData.inverted())
        lx = bb.x1 + 0.30

    OUT.mkdir(exist_ok=True)
    stem = OUT / f"fig{af['figure']:02d}-{af_id}"
    fig.savefig(stem.with_suffix(".svg"), facecolor="white")
    fig.savefig(stem.with_suffix(".png"), dpi=600, facecolor="white")
    plt.close(fig)
    return stem.with_suffix(".png")


if __name__ == "__main__":
    ids = sys.argv[1:] or list(DATA["affordances"])
    for a in ids:
        print(draw(a))
