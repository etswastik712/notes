"""Dirac Algebra figures.   .venv/bin/python -W ignore scripts/fig_da.py
fig_da_ket, fig_da_representations, fig_da_uncertainty, fig_da_evolution   (hbar = m = omega = 1 unless stated)
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch

PI = math.pi


def hermite_fn(n, x):
    """Normalised oscillator eigenfunction psi_n(x), hbar=m=omega=1."""
    from numpy.polynomial.hermite import hermval
    c = np.zeros(n + 1); c[n] = 1
    return hermval(x, c) * np.exp(-x ** 2 / 2) / math.sqrt(2 ** n * math.factorial(n) * math.sqrt(PI))


def arrow(ax, p, q, color=INK, lw=2, style="-|>", **kw):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=14, color=color, lw=lw, **kw))


def fig_ket():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.8))
    # A: one vector, three coordinate systems
    a = ax[0]
    a.set_aspect("equal"); a.axis("off"); a.set_xlim(-1.35, 1.35); a.set_ylim(-1.35, 1.35)
    v = np.array([0.86, 0.5])
    arrow(a, (0, 0), v, color=INK, lw=3)
    a.text(v[0] + 0.04, v[1] + 0.06, "$|\\alpha\\rangle$", fontsize=14)
    for th, col, lab in ((0, BLUE, "$\\{|n\\rangle\\}$"), (PI / 7, ORANGE, "$\\{|x'\\rangle\\}$"), (-PI / 5, AQUA, "$\\{|p'\\rangle\\}$")):
        e1 = np.array([math.cos(th), math.sin(th)]); e2 = np.array([-math.sin(th), math.cos(th)])
        arrow(a, (0, 0), 1.1 * e1, color=col, lw=1.6); arrow(a, (0, 0), 0.9 * e2, color=col, lw=1.6)
        a.text(1.12 * e1[0], 1.12 * e1[1] - 0.07 + (0.05 if th else 0), lab, color=col, fontsize=11)
    a.set_title("A  one vector, three orthonormal bases")
    # B: the same state in three representations: (|0> + |1>)/sqrt2 of the oscillator
    b = ax[1]
    x = np.linspace(-4.5, 4.5, 800)
    psi = (hermite_fn(0, x) + hermite_fn(1, x)) / math.sqrt(2)
    p = x
    # momentum: psi~_n(p) = (-i)^n psi_n(p): |psi~|^2 = |psi_0 - i psi_1|^2/2
    mom = np.abs(hermite_fn(0, p) + (-1j) * hermite_fn(1, p)) ** 2 / 2
    b.plot(x, psi ** 2, color=ORANGE, lw=2, label="$|\\langle x'|\\alpha\\rangle|^2$ (position)")
    b.plot(p, mom, color=AQUA, lw=2, label="$|\\langle p'|\\alpha\\rangle|^2$ (momentum)")
    b.set_xlabel("$x$ or $p$ (oscillator units)"); b.set_ylabel("probability density")
    b.legend(fontsize=8, loc="upper right")
    ins = b.inset_axes([0.05, 0.55, 0.3, 0.4])
    ins.bar([0, 1, 2, 3], [0.5, 0.5, 0, 0], color=BLUE); ins.set_xticks([0, 1, 2, 3]); ins.set_title("$|\\langle n|\\alpha\\rangle|^2$", fontsize=8)
    ins.tick_params(labelsize=7); ins.set_ylim(0, 0.7)
    b.set_title("B  $|\\alpha\\rangle=(|0\\rangle+|1\\rangle)/\\sqrt{2}$ in three languages")
    # C: dual correspondence
    c = ax[2]
    c.set_xlim(-1.6, 3.6); c.set_ylim(-1.6, 1.6); c.set_aspect("equal"); c.axis("off")
    for cx, lab, sgn in ((0, "ket space $\\mathcal{H}$", 1), (2.3, "bra space $\\mathcal{H}^*$", -1)):
        c.add_patch(Circle((cx, 0), 1.05, fill=False, color=MUTED, lw=1))
        c.text(cx, 1.3, lab, ha="center", fontsize=10)
        arrow(c, (cx, 0), (cx + 0.9, 0), color=BLUE, lw=2)
        ph = sgn * PI / 3
        arrow(c, (cx, 0), (cx + 0.9 * math.cos(ph), 0.9 * math.sin(ph)), color=ORANGE, lw=2)
    c.text(0.95, -0.2, "$|\\alpha\\rangle$", color=BLUE, fontsize=11); c.text(0.5, 0.82, "$e^{i\\varphi}|\\alpha\\rangle$", color=ORANGE, fontsize=11)
    c.text(3.25, -0.2, "$\\langle\\alpha|$", color=BLUE, fontsize=11); c.text(2.7, -0.85, "$e^{-i\\varphi}\\langle\\alpha|$", color=ORANGE, fontsize=11)
    arrow(c, (1.2, 0.2), (1.1 + 0.0, 0.2), color=INK) if False else None
    c.annotate("", (1.95, 0.0), (1.1, 0.0), arrowprops=dict(arrowstyle="<->", color=INK, lw=1.4))
    c.text(1.52, 0.12, "DC", ha="center", fontsize=10)
    c.text(1.15, -1.4, "$c|\\alpha\\rangle\\ \\leftrightarrow\\ c^*\\langle\\alpha|$   (conjugate-linear)", ha="center", fontsize=10)
    c.set_title("C  the 'DC machine': phases are reversed on the bra")
    fig.tight_layout()
    save(fig, "fig_da_ket")


def fig_representations():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    a = ax[0]
    a.set_aspect("equal"); a.set_xlim(-0.2, 2.6); a.set_ylim(-0.2, 2.2); a.axis("off")
    al = np.array([1.0, 0.3]); al = al / np.linalg.norm(al) * 1.5
    ga = np.array([0.7, 1.3]); be = np.array([2.2, 1.5]) * 0.9
    arrow(a, (0, 0), al, color=BLUE, lw=2.4); a.text(al[0] + 0.03, al[1] - 0.15, "$|\\alpha\\rangle$", color=BLUE)
    arrow(a, (0, 0), ga, color=ORANGE, lw=2.4); a.text(ga[0] - 0.2, ga[1] + 0.05, "$|\\gamma\\rangle$", color=ORANGE)
    proj = (al @ ga) / (al @ al) * al
    a.plot([ga[0], proj[0]], [ga[1], proj[1]], color=MUTED, ls=":")
    arrow(a, (0, 0), proj, color=ORANGE, lw=1.4, ls="--")
    a.text(proj[0] + 0.05, proj[1] - 0.18, "$\\langle\\alpha|\\gamma\\rangle$\\n(the amplitude)", fontsize=8.5, color=ORANGE) if False else a.text(proj[0] + 0.05, proj[1] - 0.2, "$\\langle\\alpha|\\gamma\\rangle$ (amplitude)", fontsize=8.5, color=ORANGE)
    arrow(a, (0.0, 0.0), be, color=AQUA, lw=2.4); a.text(be[0] - 0.1, be[1] + 0.07, "$|\\beta\\rangle\\langle\\alpha|\\gamma\\rangle$", color=AQUA)
    a.set_title("A  $|\\beta\\rangle\\langle\\alpha|$: swallow, project, re-emit along $|\\beta\\rangle$")
    b = ax[1]
    rng = np.random.default_rng(3)
    N = 6
    be_v = np.array([1, 0, 0.5, 0, -1, 0.3]); al_v = np.array([0.5, 1, 0, -0.5, 0, 1])
    M = np.outer(be_v, al_v)
    im = b.imshow(M, cmap="RdBu_r", vmin=-1.1, vmax=1.1)
    for i in range(N):
        for j in range(N):
            b.text(j, i, f"{M[i,j]:.1f}", ha="center", va="center", fontsize=8)
    b.set_xticks(range(N)); b.set_yticks(range(N)); b.set_xticklabels([f"$\\alpha_{j}$" for j in range(N)]); b.set_yticklabels([f"$\\beta_{i}$" for i in range(N)])
    b.set_title(f"B  matrix of $|\\beta\\rangle\\langle\\alpha|$: rank {np.linalg.matrix_rank(M)}")
    b.grid(False)
    c = ax[2]
    # completeness: partial sums of |<n|alpha>|^2 for a normalised state
    cn = np.array([0.6, 0.5, 0.4, 0.3, 0.25, 0.2, 0.15, 0.1]); cn = cn / np.linalg.norm(cn)
    c.bar(range(len(cn)), cn ** 2, color=BLUE, label="$|\\langle n|\\alpha\\rangle|^2=\\langle\\alpha|P_n|\\alpha\\rangle$")
    c.plot(range(len(cn)), np.cumsum(cn ** 2), "o-", color=ORANGE, label="partial sum $\\sum_{m\\leq n}$")
    c.axhline(1, color=INK, ls="--", lw=1)
    c.text(len(cn) - 1, 1.03, "$\\sum_nP_n=\\mathbf{1}$ $\\Rightarrow$ total $=\\langle\\alpha|\\alpha\\rangle=1$", ha="right", fontsize=9)
    c.set_ylim(0, 1.12); c.set_xlabel("$n$"); c.legend(fontsize=8, loc="center right")
    c.set_title("C  completeness: the projectors add to the identity")
    fig.tight_layout()
    save(fig, "fig_da_representations")


def fig_uncertainty():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    a = ax[0]
    x = np.linspace(-6, 6, 900)
    for s, col in ((0.5, BLUE), (1.0, ORANGE), (2.0, AQUA)):
        a.plot(x, np.exp(-x ** 2 / (2 * s * s)) / (s * math.sqrt(2 * PI)), color=col, lw=2, label=f"$\\sigma={s}$: $\\Delta x\\,\\Delta p={s*(1/(2*s)):.2f}\\hbar$")
        a.plot(x, np.exp(-2 * s * s * x ** 2) * 2 * s / math.sqrt(2 * PI), color=col, lw=1.2, ls="--")
    a.set_xlabel("$x$ (solid) or $p$ (dashed), $\\hbar=1$"); a.set_ylabel("probability density")
    a.legend(fontsize=8); a.set_title("A  squeeze $x$, spread $p$: product fixed at $\\hbar/2$")
    b = ax[1]
    b.set_aspect("equal"); b.set_xlim(-3.2, 3.2); b.set_ylim(-3.2, 3.2)
    b.add_patch(Circle((0, 0), math.sqrt(1.0), fill=True, alpha=0.25, color=BLUE)); b.text(0, -0.1, "coherent / ground\n(1/e contour)", ha="center", fontsize=8)
    for r, ang, col, lab in ((2.0, 0, ORANGE, "squeezed ($r=2$)"), (2.0, 90, AQUA, "squeezed ($r=2$, rotated)")):
        b.add_patch(Ellipse((0, 0), 2 * r, 2 / r, angle=ang, fill=False, color=col, lw=2))
    b.add_patch(Circle((0, 0), math.sqrt(3), fill=False, color=VIOLET, lw=1.6, ls="--"))
    b.text(1.25, 1.55, "$n=1$: $\\sqrt{2n+1}$", color=VIOLET, fontsize=8.5)
    b.set_xlabel("$x/\\sqrt{\\hbar/m\\omega}$"); b.set_ylabel("$p/\\sqrt{m\\hbar\\omega}$")
    b.text(-3.1, 2.85, "area $\\pi\\hbar/2\\cdot4=2\\pi\\hbar$ for all three\\n(unit circle $=\\Delta x\\Delta p=\\hbar/2$)" if False else "1/e Wigner contours, area $\\pi$ (units $\\hbar=1$)", fontsize=8.5)
    b.set_title("B  phase-space uncertainty regions")
    c = ax[2]
    n = np.arange(0, 11)
    c.plot(n, n + 0.5, "o-", color=BLUE, lw=2, label="oscillator $|n\\rangle$: $(n+\\frac{1}{2})\\hbar$")
    nb = np.arange(1, 11)
    box = np.sqrt(nb ** 2 * PI ** 2 / 12 - 0.5)
    c.plot(nb, box, "s--", color=ORANGE, label="box $n=1,2,\\dots$: $\\sqrt{n^2\\pi^2/12-1/2}\\,\\hbar$")
    c.axhline(0.5, color=INK, ls="--"); c.text(10, 0.62, "bound $\\hbar/2$", ha="right", fontsize=9)
    c.set_xlabel("quantum number $n$ (oscillator from 0)"); c.set_ylabel("$\\Delta x\\,\\Delta p/\\hbar$"); c.legend(fontsize=7.5, loc="upper left")
    c.set_title("C  the bound is saturated only by the Gaussian")
    fig.tight_layout()
    save(fig, "fig_da_uncertainty")


def fig_evolution():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    # A: Schrodinger picture: state rotates, axes fixed. B: Heisenberg: state fixed, axes rotate.
    for k, (ttl, rotate_state) in enumerate((("A  Schrödinger: state moves, axes fixed", True), ("B  Heisenberg: state fixed, axes move", False))):
        a = ax[k]
        a.set_aspect("equal"); a.set_xlim(-1.4, 1.4); a.set_ylim(-1.4, 1.4); a.axis("off")
        a.add_patch(Circle((0, 0), 1, fill=False, color=GRID, lw=1.5))
        for t, alpha in ((0, 1.0), (0.5, 0.55), (1.0, 0.3)):
            ang = 0.6 * t * 2.0
            st = (ang if rotate_state else 0.0)
            ax_ang = (0.0 if rotate_state else -ang)
            sv = np.array([math.cos(PI / 4 + st), math.sin(PI / 4 + st)])
            arrow(a, (0, 0), sv, color=BLUE, lw=2.4 * alpha + 0.6, alpha=alpha)
            for off, col in ((0, ORANGE), (PI / 2, AQUA)):
                e = np.array([math.cos(ax_ang + off), math.sin(ax_ang + off)])
                arrow(a, (0, 0), 1.15 * e, color=col, lw=1.4, alpha=alpha)
        a.text(0, -1.38, "blue $|\\psi\\rangle$, orange/teal: $\\hat A$ eigen-axes", ha="center", fontsize=8.5)
        a.set_title(ttl)
    c = ax[2]
    t = np.linspace(0, 3, 600)
    w = 2 * PI
    c.plot(t, np.cos(w * t), color=BLUE, lw=2, label="$\\langle x\\rangle(t)=d\\cos\\omega_{21}t$")
    c.plot(t, 0.5 * (1 + np.cos(w * t)), color=ORANGE, lw=2, label="$P(E_1)=\\frac{1}{2}\\cdot$ const (no change!)" if False else "right-well weight $\\frac{1}{2}(1+\\cos\\omega_{21}t)$")
    c.axhline(0, color=INK, lw=0.7)
    c.set_xlabel("$t/T_{21}$, $T_{21}=2\\pi\\hbar/(E_2-E_1)$"); c.legend(fontsize=8, loc="lower left")
    c.text(1.5, 1.12, "GaAs well of QM07 ($\\Delta E=98.4$ meV): $T_{21}=42$ fs", ha="center", fontsize=8.5)
    c.set_ylim(-1.15, 1.3)
    c.set_title("C  quantum beats of $(|E_1\\rangle+|E_2\\rangle)/\\sqrt{2}$")
    fig.tight_layout()
    save(fig, "fig_da_evolution")


if __name__ == "__main__":
    fig_ket(); fig_representations(); fig_uncertainty(); fig_evolution()
