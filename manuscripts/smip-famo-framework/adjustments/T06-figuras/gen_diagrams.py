"""Gera as Figuras 1, 2, 3, 15 e A1 no mesmo estilo das Figuras 4-14.

Uso (da raiz do repositório):
    uv run --with matplotlib python manuscripts/smip-famo-framework/adjustments/T06-figuras/gen_diagrams.py [1 2 3 15 A1]
Saída em out/ (fora do Git): figNN-<nome>.svg e .png (600 dpi).

Conteúdo tirado do texto da cópia de revisão lida em 2026-10-20 (Seções 4.3, 5.1-5.3, 8 e
Apêndice A; Tabelas 5 e 7). Pontos em aberto, marcados como CONFIRMAR:
  - Figura 2: loop desenhado de Outcomes para Features (decisão D1, opção a, recomendada);
  - Figura A1: 42 artigos citados, como no texto (a figura antiga dizia 43).
"""
from __future__ import annotations

import sys
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, PathPatch  # noqa: E402
from matplotlib.path import Path as MPath  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_affordance_figs import (  # noqa: E402
    AF_EDGE, AF_FILL, BLOCK_COLOR, DATA, INK, LINE, OUT, parse_link, tint,
)

W = 5.85
ARROW = "-|>,head_length=4,head_width=2.2"
PANEL_FILL = "#F4F4F4"
PANEL_EDGE = "#9A9A9A"

# CONFIRMAR com os autores (ver docstring)
A1_CITED = 42
A1_INCLUDED = 144


def canvas(h: float):
    fig = plt.figure(figsize=(W, h))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(h, 0)
    ax.axis("off")
    return fig, ax


def save(fig, name: str) -> Path:
    OUT.mkdir(exist_ok=True)
    stem = OUT / name
    fig.savefig(stem.with_suffix(".svg"), facecolor="white")
    fig.savefig(stem.with_suffix(".png"), dpi=600, facecolor="white")
    plt.close(fig)
    return stem.with_suffix(".png")


def box(ax, x, y, w, h, title=None, sub=None, fc="white", ec=LINE, lw=0.9, ls="-",
        title_size=9, sub_size=8, wrap=None, bold=True, align="center"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.05",
                                fc=fc, ec=ec, lw=lw, linestyle=ls))
    lines = []
    if title:
        lines.append((title, title_size, "bold" if bold else "normal"))
    if sub:
        for s in sub.split("\n"):
            lines.append((textwrap.fill(s, wrap) if wrap else s, sub_size, "normal"))
    heights = [(t.count("\n") + 1) * sz / 72 * 1.25 for t, sz, _ in lines]
    total = sum(heights)
    cy = y + (h - total) / 2
    xt = x + w / 2 if align == "center" else x + 0.10
    for (t, sz, wt), hh in zip(lines, heights):
        ax.text(xt, cy + hh / 2, t, fontsize=sz, fontweight=wt, color=INK,
                ha=align if align != "left" else "left", va="center", linespacing=1.15)
        cy += hh


def arrow(ax, p1, p2, ls="-", style=ARROW, lw=1.0, color=LINE):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle=style, linestyle=ls, color=color, lw=lw,
                                 shrinkA=0, shrinkB=0, mutation_scale=1))


def label(ax, x, y, text, size=7.5, ha="center", va="center", rot=0, style="italic"):
    ax.text(x, y, text, fontsize=size, color=INK, ha=ha, va=va, rotation=rot, fontstyle=style,
            linespacing=1.1)


# --------------------------------------------------------------------------- #
# Figura 1 — processo de identificação (Seção 4.3, Apêndice A)
# --------------------------------------------------------------------------- #
def fig1() -> Path:
    fig, ax = canvas(5.05)
    cw, bh, gap = 2.55, 0.62, 0.30
    xl, xr = 0.12, W - 0.12 - cw
    y0 = 0.42
    label(ax, xl + cw / 2, 0.18, "First list (Section 4.3, Appendix A.1)", size=8.5, style="normal")
    label(ax, xr + cw / 2, 0.18, "Second survey (Appendix A.2)", size=8.5, style="normal")
    left = [
        ("Four anchor works [2–5]", "SPIR, Arora et al., Tölle and Trier,\nTanyel and Windeler"),
        ("Citation chaining", "to the primary source of each\nmechanism and affordance"),
        ("First list", "41 mechanisms in 9 blocks,\ncompiled with generative AI assistance"),
        ("Mechanism test and naming rules", "39 mechanisms in 7 blocks"),
    ]
    right = [
        ("Lens search, 13 October 2026", "886 records"),
        ("Screening and extraction", "226 eligible records, 223 full texts,\n66 candidate entries"),
        ("Mechanism test", "33 units: 15 already in the first list,\n4 new mechanisms"),
        ("Later review", "partisan flagging (G6) withdrawn,\n3 new mechanisms kept"),
    ]
    ys = [y0 + i * (bh + gap) for i in range(4)]
    for col, x, items in ((0, xl, left), (1, xr, right)):
        for i, (t, s) in enumerate(items):
            box(ax, x, ys[i], cw, bh, t, s, fc=AF_FILL, ec=AF_EDGE)
            if i:
                arrow(ax, (x + cw / 2, ys[i - 1] + bh), (x + cw / 2, ys[i]))
    # a primeira lista é testada pelo segundo levantamento
    yt = ys[2] + bh / 2
    arrow(ax, (xl + cw, ys[3] + bh / 2), (xr, yt), ls=(0, (3, 2)))
    label(ax, W / 2 - 0.22, (ys[3] + bh / 2 + yt) / 2, "list\ntested", size=7.5, ha="right")
    # convergência
    yf = ys[3] + bh + 0.42
    box(ax, 0.9, yf, W - 1.8, 0.62, "Taxonomy",
        "42 mechanisms in 7 blocks (Section 6) and 11 affordances (Section 7)", fc="white", ec=INK, lw=1.1)
    arrow(ax, (xl + cw / 2, ys[3] + bh), (xl + cw / 2, yf))
    arrow(ax, (xr + cw / 2, ys[3] + bh), (xr + cw / 2, yf))
    return save(fig, "fig01-identification")


# --------------------------------------------------------------------------- #
# Figura 2 — o framework (Seção 5)
# --------------------------------------------------------------------------- #
def fig2() -> Path:
    fig, ax = canvas(4.45)
    xc, wc, hl, gap = 2.25, 2.25, 0.66, 0.40
    layers = [
        ("Features", "concrete platform elements"),
        ("Affordances", "action possibilities (AF1–AF11)"),
        ("Mechanisms", "causal processes (42, Blocks A–G)"),
        ("Outcomes", "five polarization types (Table 1)"),
    ]
    ys = [0.20 + i * (hl + gap) for i in range(4)]
    for i, (t, s) in enumerate(layers):
        box(ax, xc, ys[i], wc, hl, t, s, fc=AF_FILL if t == "Affordances" else "white", ec=INK, lw=1.1,
            title_size=10, sub_size=8)
    verbs = ["realize", "activate", "produce"]
    for i, v in enumerate(verbs):
        x = xc + wc / 2
        arrow(ax, (x, ys[i] + hl), (x, ys[i + 1]))
        label(ax, x + 0.08, (ys[i] + hl + ys[i + 1]) / 2, v, ha="left")
    # moderadores
    mx, mw = 0.08, 1.55
    my0, my1 = ys[0], ys[1] + hl
    box(ax, mx, my0, mw, my1 - my0, "Moderators", "Individual\nContextual\nStructural\nCultural",
        fc=PANEL_FILL, ec=PANEL_EDGE, ls=(0, (3, 2)), sub_size=8)
    for i in (0, 1):
        yc = ys[i] + hl / 2
        arrow(ax, (mx + mw, yc), (xc, yc))
        label(ax, (mx + mw + xc) / 2, yc - 0.10, "affect")
    # atores
    ay0, ay1 = ys[2] - 0.10, ys[3] + hl + 0.10
    box(ax, mx, ay0, mw, ay1 - ay0, "Actors",
        "Ordinary users\nSocial groups\nOrganized actors\nAutomated or\ncoordinated agents\nAlgorithmic system\nPlatform",
        fc=PANEL_FILL, ec=PANEL_EDGE, ls=(0, (3, 2)), sub_size=8)
    for i, v in ((2, "enact or\nexploit"), (3, "shape")):
        yc = ys[i] + hl / 2
        arrow(ax, (mx + mw, yc), (xc, yc))
        label(ax, (mx + mw + xc) / 2, yc - 0.06, v, va="bottom")
    # loop (D1, opção a): Outcomes -> Features
    xr, xloop = xc + wc, xc + wc + 0.40
    y_out, y_feat = ys[3] + hl / 2, ys[0] + hl / 2
    ax.plot([xr, xloop, xloop], [y_out, y_out, y_feat], color=LINE, lw=1.0)
    arrow(ax, (xloop, y_feat), (xr, y_feat))
    label(ax, xloop + 0.12, (y_out + y_feat) / 2, "feedback\nloop\n(Figure 3)", ha="left")
    return save(fig, "fig02-framework")


# --------------------------------------------------------------------------- #
# Figura 3 — três pontos de fechamento do loop (Seção 5.2)
# --------------------------------------------------------------------------- #
def mech_box(ax, x, y, w, h, items):
    color = BLOCK_COLOR[items[0][0]]
    sub = "\n".join(f"{DATA['mechanisms'][m]} ({m})" for m in items)
    box(ax, x, y, w, h, None, sub, fc=tint(color, 0.88), ec=color, sub_size=8, wrap=19)


def fig3() -> Path:
    fig, ax = canvas(3.55)
    cw, gw, bh, pitch = 1.38, 0.80, 0.70, 1.05
    xs = [0.08, 0.08 + cw + gw, 0.08 + 2 * (cw + gw)]
    heads = ["Mechanism", "Affordance whose\ndata it changes", "Mechanism\nreinforced"]
    for x, hd in zip(xs, heads):
        label(ax, x + cw / 2, 0.24, hd, size=8, style="normal")
    rows = [
        (["D5"], "AF2", ["B1"], "fewer visible\nmoderate\nvoices", "fewer\ncross-cutting\nsuggestions"),
        (["E1"], "AF1", ["B8"], "hostile\ncontent\nengages more", "more\nmoralized\ncontent shown"),
        (["D3", "D4"], "AF4", ["D3", "D4"], "popular\npositions get\nmore likes", "apparent\nconsensus\ngrows"),
    ]
    for r, (src, af, dst, l1, l2) in enumerate(rows):
        y = 0.52 + r * pitch
        mech_box(ax, xs[0], y, cw, bh, src)
        box(ax, xs[1], y, cw, bh, af, DATA["affordances"][af]["name"], fc=AF_FILL, ec=AF_EDGE,
            title_size=8.5, sub_size=8, wrap=20)
        mech_box(ax, xs[2], y, cw, bh, dst)
        yc = y + bh / 2
        for i, lab in ((0, l1), (1, l2)):
            arrow(ax, (xs[i] + cw, yc), (xs[i + 1], yc))
            label(ax, xs[i] + cw + gw / 2, yc - 0.05, lab, size=6.8, va="bottom")
    return save(fig, "fig03-loop-closures")


# --------------------------------------------------------------------------- #
# Figura 15 — rede bipartida affordances x blocos (Seção 8, Tabela 7)
# --------------------------------------------------------------------------- #
def fig15() -> Path:
    afs = list(DATA["affordances"])
    blocks = list(DATA["blocks"])
    edges = {}
    for a in afs:
        for raw in DATA["affordances"][a]["links"]:
            mid, kind = parse_link(raw)
            e = edges.setdefault((a, mid[0]), {"n": 0, "indirect": 0})
            e["n"] += 1
            e["indirect"] += kind == "indirect"
    pitch = 0.34
    top = 0.25
    h_body = top + pitch * (len(afs) - 1)
    H = h_body + 0.85
    fig, ax = canvas(H)
    xa, xb = 2.20, 3.60
    ya = {a: top + i * pitch for i, a in enumerate(afs)}
    bp = (h_body - top) / (len(blocks) - 1)
    yb = {b: top + i * bp for i, b in enumerate(blocks)}
    for (a, b), e in sorted(edges.items(), key=lambda kv: kv[1]["n"]):
        x1, y1, x2, y2 = xa, ya[a], xb, yb[b]
        dx = (x2 - x1) * 0.5
        path = MPath([(x1, y1), (x1 + dx, y1), (x2 - dx, y2), (x2, y2)],
                     [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4])
        ls = (0, (3, 2)) if e["indirect"] == e["n"] else "-"
        ax.add_patch(PathPatch(path, fc="none", ec=BLOCK_COLOR[b], lw=0.7 + 1.1 * e["n"], linestyle=ls,
                               alpha=0.85, capstyle="butt"))
    for a in afs:
        ax.plot(xa, ya[a], "o", ms=5, mfc=AF_FILL, mec=AF_EDGE, mew=1.0, zorder=3)
        ax.text(xa - 0.10, ya[a], f"{a}  {DATA['affordances'][a]['name']}", fontsize=8, color=INK,
                ha="right", va="center")
    for b in blocks:
        ax.plot(xb, yb[b], "o", ms=7, mfc=tint(BLOCK_COLOR[b], 0.6), mec=BLOCK_COLOR[b], mew=1.2, zorder=3)
        ax.text(xb + 0.12, yb[b], textwrap.fill(f"Block {b}. {DATA['blocks'][b]}", 28), fontsize=8,
                color=INK, ha="left", va="center", linespacing=1.1)
    # legenda
    ly = h_body + 0.45
    x = 0.10
    for n in (1, 2, 3, 4):
        ax.plot([x, x + 0.35], [ly, ly], color=LINE, lw=0.7 + 1.1 * n, solid_capstyle="butt")
        ax.text(x + 0.42, ly, f"{n}", fontsize=8, color=INK, va="center")
        x += 0.62
    ax.text(x, ly, "mechanisms linked", fontsize=8, color=INK, va="center")
    x += 1.35
    ax.plot([x, x + 0.35], [ly, ly], color=LINE, lw=1.8, linestyle=(0, (3, 2)))
    ax.text(x + 0.45, ly, "indirect links only", fontsize=8, color=INK, va="center")
    return save(fig, "fig15-bipartite")


# --------------------------------------------------------------------------- #
# Figura A1 — fluxo do segundo levantamento (Apêndice A.2)
# --------------------------------------------------------------------------- #
def figA1() -> Path:
    fig, ax = canvas(5.35)
    xm, wm, bh, gap = 0.55, 2.75, 0.70, 0.30
    xs, ws, hs = 3.65, 2.10, 0.55
    main = [
        ("Identification", "Records retrieved from Lens", "13 October 2026\nn = 886"),
        ("Screening", "Records judged eligible", "Gemini, titles and available abstracts\nn = 226"),
        ("Extraction", "Candidate mechanisms extracted",
         "Gemini Notebook, full texts of 223 papers\n66 entries, 33 units, 19 mechanisms\n(15 in the first list, 4 new, 1 later withdrawn)"),
        ("Inclusion", "Papers included in the synthesis", f"cited for a resulting mechanism\nn = {A1_INCLUDED}"),
        ("Citation", "Papers cited in this article", f"each checked against the paper\nn = {A1_CITED}"),
    ]
    side = [
        ("Records judged ineligible", "n = 660"),
        ("Eligible records without full text", "n = 3"),
        ("Papers not included", "not cited for any mechanism, or\ncited only in excluded units\nn = 79"),
        ("Included but not cited", f"n = {A1_INCLUDED - A1_CITED}"),
    ]
    heights = [bh, bh, 0.92, bh, bh]
    ys, y = [], 0.15
    for hh in heights:
        ys.append(y)
        y += hh + gap
    for i, ((phase, t, s), hh) in enumerate(zip(main, heights)):
        box(ax, xm, ys[i], wm, hh, t, s, fc=AF_FILL, ec=AF_EDGE, title_size=8.5, sub_size=7.5)
        ax.text(0.22, ys[i] + hh / 2, phase, fontsize=8, fontweight="bold", color=AF_EDGE, rotation=90,
                ha="center", va="center")
        if i:
            xa = xm + wm / 2
            arrow(ax, (xa, ys[i - 1] + heights[i - 1]), (xa, ys[i]))
            yb = ys[i - 1] + heights[i - 1] + gap / 2
            t2, s2 = side[i - 1]
            sh = hs + (0.22 if "\n" in s2 else 0)
            box(ax, xs, yb - sh / 2, ws, sh, t2, s2, fc=PANEL_FILL, ec=PANEL_EDGE, ls=(0, (3, 2)),
                title_size=7.5, sub_size=7.5)
            arrow(ax, (xa, yb), (xs, yb))
    return save(fig, "figA1-second-survey")


FIGS = {"1": fig1, "2": fig2, "3": fig3, "15": fig15, "A1": figA1}

if __name__ == "__main__":
    for key in sys.argv[1:] or list(FIGS):
        print(FIGS[key]())
