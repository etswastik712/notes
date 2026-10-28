"""Figures for CH02-CH09 (inorganic chemistry).   .venv/bin/python -W ignore scripts/fig_ch0209.py [name]
Literature inputs are flagged in scripts/ch0209_numbers.py (recalled) and in the chapters ([verify])."""
import itertools
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa

import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon

PI = math.pi
F_, R_, T_ = 96485.332, 8.314462, 298.15


# ------------------------------------------------------------------ helpers
def level(ax, x0, x1, y, label="", n=0, color=INK, lw=2.2, fs=8.5, side="r", up_only=False, dx=0.03):
    ax.hlines(y, x0, x1, color=color, lw=lw)
    xm = 0.5 * (x0 + x1)
    if n:
        kinds = {1: [(xm, "u")], 2: [(xm, "ud")]}
        if n in (1, 2):
            electrons(ax, xm, y, n)
        else:  # degenerate: n electrons spread on equal-width cells (handled by caller)
            pass
    if label:
        if side == "r":
            ax.text(x1 + dx, y, label, va="center", ha="left", fontsize=fs)
        else:
            ax.text(x0 - dx, y, label, va="center", ha="right", fontsize=fs)


def electrons(ax, x, y, n, h=0.55, color=INK, scale=1.0):
    y0, y1 = ax.get_ylim()
    dy = 0.028 * abs(y1 - y0) * scale
    xr = ax.get_xlim(); dxs = 0.014 * abs(xr[1] - xr[0]) * scale
    if n == 1:
        ax.annotate("", (x, y + dy), (x, y - dy), arrowprops=dict(arrowstyle="-|>", color=color, lw=1.4, mutation_scale=9))
    elif n == 2:
        for dxx, up in ((-dxs, True), (dxs, False)):
            a, b = ((y - dy, y + dy) if up else (y + dy, y - dy))
            ax.annotate("", (x + dxx, b), (x + dxx, a), arrowprops=dict(arrowstyle="-|>", color=color, lw=1.4, mutation_scale=9))


def fill_deg(ax, x0, x1, y, n_orb, nel, **kw):
    """Draw a degenerate set of n_orb orbitals side by side filled with nel electrons (Hund)."""
    w = (x1 - x0) / n_orb
    occ = [0] * n_orb
    for i in range(nel):
        occ[i % n_orb] += 1
    for i in range(n_orb):
        xa, xb = x0 + i * w + 0.01, x0 + (i + 1) * w - 0.01
        ax.hlines(y, xa, xb, color=kw.get("color", INK), lw=2.2)
        if occ[i]:
            electrons(ax, 0.5 * (xa + xb), y, occ[i])


# ------------------------------------------------------------------ CH02
def fig_ch02_lcao():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    a = ax[0]
    x = np.linspace(-4, 4, 800)
    R = 1.4
    f = lambda xx: np.exp(-np.abs(xx))  # 1s (a0=1) along the axis
    A, B = f(x + R / 2), f(x - R / 2)
    S = math.exp(-R) * (1 + R + R * R / 3)
    plus = (A + B) / math.sqrt(2 * (1 + S)); minus = (A - B) / math.sqrt(2 * (1 - S))
    a.plot(x, plus, color=BLUE, lw=2.2, label="$\\psi_+=(\\chi_A+\\chi_B)/\\sqrt{2(1+S)}$")
    a.plot(x, minus, color=ORANGE, lw=2.2, label="$\\psi_-=(\\chi_A-\\chi_B)/\\sqrt{2(1-S)}$")
    a.plot(x, A / 1.7, color=MUTED, lw=1, ls=":"); a.plot(x, B / 1.7, color=MUTED, lw=1, ls=":")
    a.axhline(0, color=INK, lw=0.7); a.plot([-R / 2, R / 2], [0, 0], "ko", ms=6)
    a.annotate("node", (0, 0), (0.0, -0.55), ha="center", arrowprops=dict(arrowstyle="->", color=ORANGE), color=ORANGE, fontsize=9)
    a.set_title(f"A  $\\mathrm{{H_2}}$ LCAO on the axis ($R=1.4\\,a_0$, $S={S:.3f}$)")
    a.set_xlabel("$x$ ($a_0$)"); a.legend(fontsize=8, loc="upper right")
    b = ax[1]
    Rs = np.linspace(0.2, 6, 200)
    Ss = np.exp(-Rs) * (1 + Rs + Rs ** 2 / 3)
    b.plot(Rs, Ss, color=BLUE, lw=2, label="$S(R)=e^{-R}(1+R+R^2/3)$")
    b.plot(Rs, (1 + Ss) / (1 - Ss) / 8, color=ORANGE, lw=2, label="(antibond. rise)/(bond. drop) $=(1+S)/(1-S)$ [÷8]")
    b.axvline(1.4, color=MUTED, ls=":"); b.text(1.45, 0.9, "$r_e=0.74$ Å\n$S=0.753$", fontsize=8.5)
    b.set_xlabel("$R$ ($a_0$)"); b.set_title("B  overlap and the asymmetry of the split"); b.legend(fontsize=7.5, loc="upper right"); b.set_ylim(0, 1.1)
    c = ax[2]
    c.set_xlim(0, 3); c.set_ylim(-4, 4.5); c.axis("off")
    gam = 1.0
    S_ = 0.7534
    Eb, Ea = -gam / (1 + S_), gam / (1 - S_)
    c.hlines(0, 0.1, 0.9, color=MUTED); c.hlines(0, 2.1, 2.9, color=MUTED)
    c.text(0.5, 0.25, "$\\chi_A$", ha="center"); c.text(2.5, 0.25, "$\\chi_B$", ha="center")
    c.hlines(Eb, 1.1, 1.9, color=BLUE, lw=3); c.hlines(Ea, 1.1, 1.9, color=ORANGE, lw=3)
    electrons(c, 1.5, Eb, 2)
    for xx in (0.9, 2.1):
        c.plot([xx, 1.1 if xx < 1.5 else 1.9], [0, Eb], color=GRID); c.plot([xx, 1.1 if xx < 1.5 else 1.9], [0, Ea], color=GRID)
    c.text(2.0, Eb - 0.4, f"drop $\\gamma/(1+S)={abs(Eb):.2f}\\gamma$", fontsize=9, color=BLUE, ha="center")
    c.text(2.0, Ea + 0.3, f"rise $\\gamma/(1-S)={Ea:.2f}\\gamma$ (×{Ea/abs(Eb):.1f})", fontsize=9, color=ORANGE, ha="center")
    c.set_title("C  with overlap the antibonding level rises more\n($\\sigma_u^*$ is more antibonding than $\\sigma_g$ is bonding)")
    fig.tight_layout(); save(fig, "fig_ch02_lcao")


def fig_ch02_diatomics():
    fig, ax = plt.subplots(1, 3, figsize=(16, 5.2))
    # N2 type and O2 type ladders (valence only). energies qualitative
    def ladder(a, title, order, nel):
        a.set_xlim(0, 3); a.set_ylim(0, 10.5); a.axis("off")
        a.set_title(title)
        # AO levels
        a.hlines(2.5, 0.0, 0.7, color=MUTED); a.hlines(6.0, 0.0, 0.7, color=MUTED)
        a.hlines(2.5, 2.3, 3.0, color=MUTED); a.hlines(6.0, 2.3, 3.0, color=MUTED)
        a.text(0.35, 2.1, "2s", ha="center", fontsize=9); a.text(0.35, 5.55, "2p", ha="center", fontsize=9)
        a.text(2.65, 2.1, "2s", ha="center", fontsize=9); a.text(2.65, 5.55, "2p", ha="center", fontsize=9)
        ys = {"2sg": 1.0, "2su": 2.4, "1pu": 4.6, "3sg": 5.2, "1pg": 7.2, "3su": 9.2} if order == "N" else {"2sg": 1.0, "2su": 2.4, "3sg": 4.0, "1pu": 4.9, "1pg": 7.2, "3su": 9.2}
        deg = {"1pu": 2, "1pg": 2}
        labels = {"2sg": "$2\\sigma_g$", "2su": "$2\\sigma_u^*$", "3sg": "$3\\sigma_g$", "1pu": "$1\\pi_u$", "1pg": "$1\\pi_g^*$", "3su": "$3\\sigma_u^*$"}
        seq = ["2sg", "2su", "1pu", "3sg", "1pg", "3su"] if order == "N" else ["2sg", "2su", "3sg", "1pu", "1pg", "3su"]
        left = nel
        for k in seq:
            cap = 4 if k in deg else 2
            n = min(cap, left); left -= n
            if k in deg:
                fill_deg(a, 1.0, 2.0, ys[k], 2, n)
            else:
                a.hlines(ys[k], 1.2, 1.8, color=INK, lw=2.2)
                if n:
                    electrons(a, 1.5, ys[k], n)
            a.text(2.05 if k in deg else 1.85, ys[k], labels[k], va="center", fontsize=9)
            for xx in ((0.7,), (2.3,)):
                pass
        bo = None
    ladder(ax[0], "A  $\\mathrm{N_2}$ ladder (s–p mixing: $1\\pi_u<3\\sigma_g$), 10 e⁻", "N", 10)
    ladder(ax[1], "B  $\\mathrm{O_2}$ ladder (no mixing: $3\\sigma_g<1\\pi_u$), 12 e⁻", "O", 12)
    c = ax[2]
    data = [("Li$_2$", 1, 105, 267), ("B$_2$", 1, 290, 159), ("C$_2$", 2, 602, 124), ("N$_2$", 3, 945, 110), ("O$_2$", 2, 498, 121), ("F$_2$", 1, 159, 141),
            ("O$_2^+$", 2.5, 643, 112), ("O$_2^-$", 1.5, 360, 135), ("N$_2^+$", 2.5, 841, 112)]
    for nm, bo, D, r in data:
        c.plot(bo, D, "o", color=BLUE if nm[0] != "O" else ORANGE, ms=8)
        c.text(bo + 0.04, D + 22, nm, fontsize=8.5)
    c.set_xlabel("bond order (from the MO fill)"); c.set_ylabel("dissociation energy (kJ/mol, recalled)")
    c.set_title("C  bond order tracks bond energy ($\\mathrm{B_2}$, $\\mathrm{C_2}$: s–p mixing)")
    c.set_xlim(0.7, 3.4)
    fig.tight_layout(); save(fig, "fig_ch02_diatomics")


def fig_ch02_hetero():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 5.0))
    a = ax[0]
    ao = {"H1s": -13.61, "F2s": -40.17, "F2p": -18.65}
    a.set_xlim(0, 3); a.set_ylim(-45, -5); a.axis("off")
    a.hlines(ao["H1s"], 0.0, 0.7, color=MUTED, lw=2.5); a.text(0.35, ao["H1s"] + 1.0, "H 1s  −13.6", ha="center", fontsize=8.5)
    a.hlines(ao["F2p"], 2.3, 3.0, color=MUTED, lw=2.5); a.text(2.65, ao["F2p"] + 1.0, "F 2p  −18.7", ha="center", fontsize=8.5)
    a.hlines(ao["F2s"], 2.3, 3.0, color=MUTED, lw=2.5); a.text(2.65, ao["F2s"] - 2.0, "F 2s  −40.2", ha="center", fontsize=8.5)
    a.hlines(-21.5, 1.1, 1.9, color=BLUE, lw=3); electrons(a, 1.5, -21.5, 2); a.text(1.95, -21.5, "$2\\sigma$ (bond, mostly F)", fontsize=8.5, va="center")
    a.hlines(-18.65, 1.1, 1.9, color=INK, lw=3, ls="--"); fill_deg(a, 1.0, 2.0, -18.65, 2, 4)
    a.text(2.0, -16.8, "$1\\pi$ (nonbonding, F $2p_{x,y}$)", fontsize=8, ha="left")
    a.hlines(-40.17, 1.1, 1.9, color=INK, lw=3); electrons(a, 1.5, -40.17, 2); a.text(1.95, -42.5, "$1\\sigma$ (F 2s)", fontsize=8.5)
    a.hlines(-8.5, 1.1, 1.9, color=ORANGE, lw=3); a.text(1.95, -8.5, "$3\\sigma^*$ (mostly H)", fontsize=8.5, va="center")
    a.set_title("A  HF: 8 e⁻ on F; one polar bond")
    b = ax[1]
    b.set_xlim(0, 3); b.set_ylim(-36, -4); b.axis("off")
    cao = {"C2s": -19.43, "C2p": -10.66, "O2s": -32.38, "O2p": -15.85}
    for k, (x0, x1) in {"C2s": (0, 0.7), "C2p": (0, 0.7), "O2s": (2.3, 3.0), "O2p": (2.3, 3.0)}.items():
        b.hlines(cao[k], x0, x1, color=MUTED, lw=2.5)
        b.text((x0 + x1) / 2, cao[k] + 0.8, f"{k[0]} {k[1:]}  {cao[k]:.1f}", ha="center", fontsize=8)
    mos = [("1σ  (O 2s)", -32.0, 2, "nonbonding"), ("2σ", -20.5, 2, "bonding (C2s+C2p$_z$+O2p$_z$)"), ("1π", -17.6, 4, "bonding, mostly O"),
           ("3σ  HOMO", -14.2, 2, "weakly bonding, mostly C 2s"), ("2π  LUMO", -8.8, 0, "C 2p character"), ("4σ*", -6.0, 0, "")]
    for nm, y, n, txt in mos:
        if nm.startswith("1π") or nm.startswith("2π"):
            fill_deg(b, 1.0, 2.0, y, 2, n)
        else:
            b.hlines(y, 1.2, 1.8, color=ORANGE if (n == 0) else BLUE, lw=3)
            if n:
                electrons(b, 1.5, y, n)
        b.text(2.05 if "π" in nm else 1.85, y, nm + ("  " + txt if txt else ""), fontsize=7.5, va="center")
    b.set_title("B  CO: HOMO and LUMO both on C → binds metals through C")
    c = ax[2]
    ds = np.linspace(0, 12, 200)
    beta = 3.0
    half = ds / 2
    cF2 = 0.5 * (1 + half / np.sqrt(half ** 2 + beta ** 2))
    c.plot(ds, cF2, color=BLUE, lw=2.2, label="bonding MO: share on the lower AO")
    c.plot(ds, 1 - cF2, color=ORANGE, lw=2.2, label="antibonding MO: share on the lower AO")
    c.axvline(5.05, color=MUTED, ls=":"); c.text(5.2, 0.55, "HF: ΔE(H1s–F2p)=5.05 eV\n→ 82 % on F", fontsize=8.5)
    c.axhline(0.5, color=GRID)
    c.set_xlabel("AO energy mismatch $|\\alpha_A-\\alpha_B|$ (eV)  [β = 3 eV, illustrative]"); c.set_ylabel("coefficient$^2$ on the more electronegative atom")
    c.set_title("C  mismatch ⇒ polarity: equal atoms 50:50, large gap → ionic"); c.legend(fontsize=8, loc="center right")
    fig.tight_layout(); save(fig, "fig_ch02_hetero")


# ------------------------------------------------------------------ CH03
def fig_ch03_h3():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.8))
    def draw_orbital(a, cx, cy, coeffs, pos, scale=0.20):
        for c, (px, py) in zip(coeffs, pos):
            r = abs(c) * scale * 1.2
            if r > 1e-3:
                a.add_patch(Circle((cx + px, cy + py), r, color=BLUE if c > 0 else ORANGE, alpha=0.85))
    a = ax[0]
    a.set_xlim(0, 4); a.set_ylim(-2.6, 2.6); a.axis("off")
    lin_pos = [(-0.6, 0), (0, 0), (0.6, 0)]
    levels = [(-1.414, (0.5, 0.707, 0.5), "$1\\sigma$"), (0.0, (0.707, 0, -0.707), "$2\\sigma$"), (1.414, (0.5, -0.707, 0.5), "$3\\sigma$")]
    for E, co, lab in levels:
        y = -E
        a.hlines(y, 2.6, 3.8, color=INK, lw=2); a.text(3.85, y, lab, va="center", fontsize=9)
        draw_orbital(a, 1.3, y, co, lin_pos)
    a.text(1.5, 2.35, "linear $\\mathrm{H_3}$ (slide 41, left)", ha="center", fontsize=9)
    a.text(3.2, -2.4, "$E=\\alpha\\mp\\sqrt{2}|\\beta|,\\ \\alpha$", ha="center", fontsize=9)
    a.set_title("A  linear H$_3$: coefficients ½, √½, ½")
    b = ax[1]
    b.set_xlim(0, 4); b.set_ylim(-2.6, 2.6); b.axis("off")
    tri_pos = [(0, 0.3), (-0.3, -0.2), (0.3, -0.2)]
    # degenerate pair for triangle: (0, 1/sqrt2, -1/sqrt2) and (2,-1,-1)/sqrt6
    levels = [(-2.0, [(0.577, 0.577, 0.577)], "$a$ (bonding all pairs)"), (1.0, [(0.0, 0.707, -0.707), (0.816, -0.408, -0.408)], "$e$ (2σ, 3σ degenerate)")]
    for E, cos, lab in levels:
        y = -E * 1.0
        for k, co in enumerate(cos):
            xx = 1.2 + 1.5 * k if len(cos) > 1 else 1.9
            b.hlines(y, xx - 0.35, xx + 0.35, color=INK, lw=2)
            draw_orbital(b, xx, y + 0.0, co, tri_pos, scale=0.22)
        b.text(3.55, y, lab, va="center", fontsize=8.5)
    b.text(2.0, 2.35, "triangular $\\mathrm{H_3}$ (slide 41, right)", ha="center", fontsize=9)
    b.set_title("B  triangle: $E=\\alpha+2\\beta,\\ \\alpha-\\beta,\\ \\alpha-\\beta$")
    c = ax[2]
    sp = ["$\\mathrm{H_3^+}$ (2 e⁻)", "$\\mathrm{H_3}$ (3 e⁻)", "$\\mathrm{H_3^-}$ (4 e⁻)"]
    lin = [2.828, 2.828, 2.828]; tri = [4.0, 3.0, 2.0]
    x = np.arange(3)
    c.bar(x - 0.18, lin, 0.36, color=ORANGE, label="linear")
    c.bar(x + 0.18, tri, 0.36, color=BLUE, label="triangle")
    for xi, l_, t_ in zip(x, lin, tri):
        c.text(xi - 0.18, l_ + 0.06, f"{l_:.2f}", ha="center", fontsize=8.5); c.text(xi + 0.18, t_ + 0.06, f"{t_:.2f}", ha="center", fontsize=8.5)
    c.set_xticks(x); c.set_xticklabels(sp); c.set_ylabel("electronic stabilisation / $|\\beta|$ (larger = more stable)")
    c.set_title("C  which shape wins depends on the electron count"); c.legend(fontsize=8)
    fig.tight_layout(); save(fig, "fig_ch03_h3")


def fig_ch03_polyatomics():
    fig, ax = plt.subplots(1, 3, figsize=(16, 5.4))
    # NH3
    a = ax[0]
    a.set_xlim(0, 5.4); a.set_ylim(-2, 10); a.axis("off")
    a.hlines(6.0, 0.0, 0.7, color=MUTED, lw=2.5); a.hlines(2.0, 0.0, 0.7, color=MUTED, lw=2.5)
    a.text(0.35, 6.3, "N 2p", ha="center", fontsize=8.5); a.text(0.35, 1.5, "N 2s", ha="center", fontsize=8.5)
    a.hlines(5.0, 4.6, 5.3, color=MUTED, lw=2.5); a.text(4.95, 4.4, "H$_3$ LGOs\n$a_1+e$", ha="center", fontsize=8)
    mo = [("$1a_1$", 0.0, 2, "N 2s"), ("$1e$", 3.3, 4, ""), ("$2a_1$", 5.5, 2, "lone pair (HOMO)"), ("$2e^*$", 7.8, 0, ""), ("$3a_1^*$", 9.2, 0, "")]
    for nm, y, n, txt in mo:
        if "e" in nm:
            fill_deg(a, 1.4, 2.4, y, 2, n)
        else:
            a.hlines(y, 1.5, 2.3, color=INK, lw=2.5)
            if n:
                electrons(a, 1.9, y, n)
        a.text(2.5, y, nm + ("  " + txt if txt else ""), fontsize=8.5, va="center")
    a.text(0.0, -1.2, "PES (He I, 21.2 eV): 2a₁ ≈ 11 eV, 1e ≈ 16 eV;\n1a₁ ≈ 27 eV is out of range", fontsize=8.5)
    a.set_title("A  NH$_3$: 8 e⁻, lone pair = nearly nonbonding $2a_1$")
    # H2O
    b = ax[1]
    b.set_xlim(0, 6.6); b.set_ylim(-36, 6); b.axis("off")
    b.hlines(-15.85, 0.0, 0.7, color=MUTED, lw=2.5); b.hlines(-32.4, 0.0, 0.7, color=MUTED, lw=2.5)
    b.text(0.35, -14.6, "O 2p", ha="center", fontsize=8.5); b.text(0.35, -31.2, "O 2s", ha="center", fontsize=8.5)
    b.hlines(-13.6, 5.9, 6.5, color=MUTED, lw=2.5); b.text(6.2, -17.5, "H LGOs\n$a_1+b_1$", ha="center", fontsize=8)
    mo = [("$2a_1$", -32.2, 2, "IE 32.2 eV (mostly O 2s)"), ("$1b_1$", -18.6, 2, "IE 18.6 eV: O–H σ, in plane"), ("$3a_1$", -14.7, 2, "IE 14.7 eV: s–p lone pair"), ("$1b_2$", -12.6, 2, "IE 12.6 eV: O $p$ lone pair (HOMO)"),
          ("$4a_1^*$", -2.5, 0, ""), ("$2b_1^*$", 2.0, 0, "")]
    for nm, y, n, txt in mo:
        b.hlines(y, 1.5, 2.3, color=INK if n else ORANGE, lw=2.5)
        if n:
            electrons(b, 1.9, y, n, scale=1.0)
        b.text(2.4, y, nm + ("  " + txt if txt else ""), fontsize=8, va="center")
    b.set_title("B  H$_2$O ($C_{2v}$, slide convention): 8 e⁻, two different lone pairs")
    # SF6
    c = ax[2]
    c.set_xlim(0, 5.2); c.set_ylim(-1, 11); c.axis("off")
    c.hlines(5.5, 0.0, 0.7, color=MUTED, lw=2.5); c.text(0.35, 5.8, "S 3p", ha="center", fontsize=8.5)
    c.hlines(3.0, 0.0, 0.7, color=MUTED, lw=2.5); c.text(0.35, 2.4, "S 3s", ha="center", fontsize=8.5)
    c.hlines(2.0, 4.4, 5.1, color=MUTED, lw=2.5); c.text(4.75, 0.6, "6 F LGOs\n$a_{1g}+t_{1u}+e_g$", ha="center", fontsize=8)
    levels = [("$1a_{1g}$", 0.0, 2, 1, "bonding"), ("$1t_{1u}$", 1.2, 6, 3, "bonding"), ("$1e_g$", 3.0, 4, 2, "nonbonding (F)"), ("$2a_{1g}^*$", 6.0, 0, 1, ""), ("$2t_{1u}^*$", 8.0, 0, 3, "")]
    for nm, y, n, deg, txt in levels:
        fill_deg(c, 1.2, 2.5, y, deg, n)
        c.text(2.6, y, nm + ("  " + txt if txt else ""), fontsize=8.5, va="center")
    c.text(0.0, 10.2, "12 e⁻ = 2 + 6 + 4: all bonding and nonbonding full,\nall antibonding empty; 8 e⁻ in bonding MOs\nover 6 S–F bonds: bond order 0.67", fontsize=8.3, va="top")
    c.set_title("C  SF$_6$ without $d$ orbitals (hypervalence)")
    fig.tight_layout(); save(fig, "fig_ch03_polyatomics")


# ------------------------------------------------------------------ CH04 / CH05
def fig_ch04_acidbase():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    T = np.array([0, 25, 50, 75, 100]); K = np.array([0.112, 1.023, 5.495, 19.95, 56.23]) * 1e-14
    pK = -np.log10(K)
    a = ax[0]
    a.plot(T, pK, "o-", color=BLUE, lw=2, label="$\\mathrm{p}K_w$ (slide 56 table)")
    a.plot(T, pK / 2, "s-", color=ORANGE, lw=2, label="neutral pH = p$K_w/2$")
    a.axhline(7, color=MUTED, ls=":")
    for t, p in zip(T, pK):
        a.text(t, p + 0.18, f"{p:.2f}", ha="center", fontsize=8)
    a.set_xlabel("temperature (°C)"); a.set_title("A  water autoprotolysis: neutral is pH 7.0 only at 25 °C"); a.legend(fontsize=8); a.set_ylim(5.5, 15.6)
    b = ax[1]
    pairs = [("HClO$_4$", "ClO$_4^-$", -8), ("HCl", "Cl$^-$", -6), ("H$_2$SO$_4$", "HSO$_4^-$", -3), ("H$_3$O$^+$", "H$_2$O", 0), ("HF", "F$^-$", 3.17), ("CH$_3$COOH", "CH$_3$COO$^-$", 4.76),
             ("NH$_4^+$", "NH$_3$", 9.25), ("H$_2$O", "OH$^-$", 14)]
    for i, (ac, bs, p) in enumerate(pairs):
        b.plot([p], [i], "o", color=BLUE, ms=7)
        b.text(p + 0.4, i + 0.12, f"{ac}  /  {bs}   p$K_a$={p:g}", fontsize=8.5)
    b.set_yticks([]); b.set_xlabel("p$K_a$ (acid strength falls →; conjugate base strength rises →)"); b.set_xlim(-10, 24)
    b.set_title("B  conjugate pairs: p$K_a$ + p$K_b$ = p$K_w$ = 14"); b.invert_yaxis()
    c = ax[2]
    c.axis("off"); c.set_xlim(0, 10); c.set_ylim(0, 8)
    boxes = [("Arrhenius\nH$^+$ / OH$^-$ in water", 0.3, 5.5, 4.6, 2.0, BLUE),
             ("Brønsted–Lowry\nproton donor / acceptor", 0.3, 3.2, 6.2, 2.0, ORANGE),
             ("Lewis\nelectron-pair acceptor / donor", 0.3, 0.9, 9.3, 2.0, AQUA)]
    for t, x, y, w, h, col in boxes:
        c.add_patch(plt.Rectangle((x, y), w, h, fill=True, alpha=0.18, color=col, lw=0)); c.add_patch(plt.Rectangle((x, y), w, h, fill=False, color=col, lw=1.8))
        c.text(x + 0.2, y + h / 2, t, fontsize=8.5, va="center")
    c.add_patch(plt.Rectangle((7.0, 3.2), 2.7, 2.0, fill=False, color=VIOLET, lw=1.8, ls="--")); c.text(7.2, 4.2, "Lux–Flood\nO$^{2-}$ donor/acceptor", fontsize=8, va="center", color=VIOLET)
    c.text(5.0, 7.7, "nested definitions: each includes the previous (Lux–Flood and solvent-system are siblings)", ha="center", fontsize=8)
    c.set_title("C  the four definitions as a nesting")
    fig.tight_layout(); save(fig, "fig_ch04_acidbase")


def fig_ch05_acids():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    a = ax[0]
    acids = [("HOCl", 0, 7.5), ("H$_3$BO$_3$", 0, 9.2), ("HClO$_2$", 1, 1.96), ("H$_3$PO$_4$", 1, 2.15), ("H$_3$PO$_3$", 1, 1.3), ("HNO$_2$", 1, 3.3),
             ("HNO$_3$", 2, -1.4), ("HClO$_3$", 2, -1.0), ("H$_2$SO$_4$", 2, -3.0), ("HClO$_4$", 3, -8.0)]
    for nm, n, p in acids:
        a.plot(n, p, "o", color=BLUE, ms=7); a.text(n + 0.06, p + 0.1, nm, fontsize=8)
    nn = np.linspace(-0.2, 3.2, 10); a.plot(nn, 8 - 5 * nn, color=ORANGE, lw=2, label="Pauling: p$K_a\\approx8-5n$")
    a.set_xlabel("$n$ = number of non-protonated O (oxo groups)"); a.set_ylabel("p$K_a$ (first)"); a.legend(fontsize=8)
    a.set_title("A  oxo acids: each extra $=$O lowers p$K_a$ by ≈5")
    b = ax[1]
    names = ["CH$_3$COOH", "ClCH$_2$COOH", "Cl$_2$CHCOOH", "Cl$_3$CCOOH"]; pk = [4.76, 2.86, 1.29, 0.65]
    b.bar(names, pk, color=[GRID, BLUE, BLUE, BLUE], edgecolor=INK)
    for i, v in enumerate(pk):
        b.text(i, v + 0.1, f"{v}\n(×{10**(4.76-v):.0f})" if i else f"{v}", ha="center", fontsize=8.5)
    b.set_ylabel("p$K_a$"); b.set_title("B  inductive effect: −I of Cl stabilises the anion"); b.set_ylim(0, 6)
    plt.setp(b.get_xticklabels(), fontsize=8, rotation=10)
    c = ax[2]
    ions = [("Na$^+$", 1, 102, 14.2), ("Mg$^{2+}$", 2, 72, 11.4), ("Zn$^{2+}$", 2, 74, 9.0), ("Fe$^{2+}$", 2, 78, 9.5), ("Cu$^{2+}$", 2, 73, 7.5), ("Al$^{3+}$", 3, 53.5, 5.0),
            ("Cr$^{3+}$", 3, 61.5, 4.0), ("Fe$^{3+}$", 3, 64.5, 2.2), ("Hg$^{2+}$", 2, 102, 3.4)]
    xs = np.array([z * z / r * 100 for _, z, r, _ in ions[:-1]]); ys = np.array([p for *_, p in ions[:-1]])
    m, c0 = np.polyfit(xs, ys, 1)
    for nm, z, r, p in ions:
        xx = z * z / r * 100
        c.plot(xx, p, "o", color=ORANGE if nm.startswith("Hg") else BLUE, ms=7); c.text(xx + 0.2, p + 0.2, nm, fontsize=8)
    xl = np.linspace(0.5, 18, 10); c.plot(xl, c0 + m * xl, color=MUTED, ls="--", label=f"fit (without Hg): p$K_a$ = {c0:.1f} − {abs(m):.2f}·$Z^2/r$")
    c.set_xlabel("$Z^2/r$ (units 100/pm)"); c.set_ylabel("p$K_a$ of $[\\mathrm{M(OH_2)_6}]^{n+}$"); c.legend(fontsize=8)
    c.set_title("C  aqua acids: charge/size, plus covalency (Hg²⁺ is off the line)")
    fig.tight_layout(); save(fig, "fig_ch05_acids")


# ------------------------------------------------------------------ CH06
def fig_ch06_hsab():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.8))
    a = ax[0]
    cat = [("Al$^{3+}$", 45.8, "hard"), ("Li$^+$", 35.1, "hard"), ("Mg$^{2+}$", 32.6, "hard"), ("Na$^+$", 21.1, "hard"), ("Ca$^{2+}$", 19.5, "hard"), ("K$^+$", 13.6, "hard"),
           ("Fe$^{3+}$", 12.1, "border"), ("Zn$^{2+}$", 10.9, "border"), ("Hg$^{2+}$", 7.7, "soft"), ("Fe$^{2+}$", 7.2, "border"), ("Ag$^+$", 7.0, "soft"), ("Cu$^+$", 6.3, "soft"), ("Au$^+$", 5.6, "soft")]
    col = {"hard": BLUE, "border": MUTED, "soft": ORANGE}
    a.barh(range(len(cat)), [c[1] for c in cat], color=[col[c[2]] for c in cat])
    a.set_yticks(range(len(cat))); a.set_yticklabels([c[0] for c in cat], fontsize=8.5); a.invert_yaxis()
    for i, c_ in enumerate(cat):
        a.text(c_[1] + 0.6, i, f"{c_[1]:.1f}", va="center", fontsize=8)
    a.set_xlabel("absolute hardness $\\eta=(I-A)/2$ (eV), from ionisation energies")
    a.set_title("A  Pearson hardness orders the classes (blue hard, grey borderline, orange soft)")
    b = ax[1]
    X = ["F⁻", "Cl⁻", "Br⁻", "I⁻"]
    hg = [1.03, 6.74, 8.94, 12.87]; fe = [6.04, 1.48, 0.6, None]; ag = [-0.4, 3.0, 4.3, 6.6]
    b.plot(range(4), hg, "o-", color=ORANGE, lw=2, label="Hg$^{2+}$ (soft)")
    b.plot(range(4), ag, "s-", color=AQUA, lw=2, label="Ag$^+$ (soft)")
    b.plot(range(3), fe[:3], "^-", color=BLUE, lw=2, label="Fe$^{3+}$ (hard)")
    b.set_xticks(range(4)); b.set_xticklabels(X); b.set_ylabel("log $K_1$ (recalled)")
    b.set_title("B  slide 79: hard acids prefer F⁻, soft acids prefer I⁻"); b.legend(fontsize=8)
    c = ax[2]
    c.set_xlim(0, 10); c.set_ylim(-4, 5); c.axis("off")
    # hard-hard (left) and soft-soft (right) FMO pictures from slide 85
    for x0, ttl, gap_a, gap_b, col_, lab in ((0.3, "hard–hard", 3.2, 2.0, BLUE, "mainly electrostatic\n(Madelung)"), (5.4, "soft–soft", 1.0, 0.8, ORANGE, "mainly covalent\n(overlap, dispersion)")):
        c.text(x0 + 2.2, 4.4, ttl, ha="center", fontsize=10, color=col_)
        for xx, nm in ((x0, "A"), (x0 + 3.2, ":B")):
            hom = -gap_a if nm == "A" else -gap_b
            lum = gap_a * 0.55 if nm == "A" else gap_b * 0.6
            c.hlines(lum, xx, xx + 1.2, color=INK, lw=2); c.hlines(hom, xx, xx + 1.2, color=INK, lw=2)
            electrons(c, xx + 0.6, hom, 2)
            c.text(xx + 0.6, lum + 0.25, f"LUMO {nm}" if nm == "A" else "LUMO", ha="center", fontsize=7.5)
            c.text(xx + 0.6, hom - 0.55, f"HOMO {nm}" if nm == "A" else "HOMO", ha="center", fontsize=7.5)
        c.text(x0 + 2.2, -3.6, lab, ha="center", fontsize=8.5)
    c.set_title("C  frontier orbitals: big HOMO–LUMO gaps (hard) vs small (soft)")
    fig.tight_layout(); save(fig, "fig_ch06_hsab")


# ------------------------------------------------------------------ CH07
def _wire(ax, V, edges, color=INK, ls="-", lw=1.6):
    for i, j in edges:
        ax.plot(*zip(V[i], V[j]), color=color, lw=lw, ls=ls)


def _points(ax, V, labels=None, color=BLUE, s=70):
    V = np.array(V)
    ax.scatter(V[:, 0], V[:, 1], V[:, 2], color=color, s=s, depthshade=False, edgecolor=INK)
    if labels:
        for v, l in zip(V, labels):
            ax.text(v[0] * 1.1, v[1] * 1.1, v[2] * 1.1, l, fontsize=7)


def _clean3d(ax, lim=1.5):
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
    ax.set_axis_off(); ax.set_box_aspect((1, 1, 1))


def fig_ch07_wade():
    fig = plt.figure(figsize=(16, 5.4))
    oct_v = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    opp = {(0, 1), (2, 3), (4, 5)}
    edges = [(i, j) for i, j in itertools.combinations(range(6), 2) if (i, j) not in opp]
    a = fig.add_subplot(1, 4, 1, projection="3d")
    _wire(a, oct_v, edges); _points(a, oct_v, color=BLUE); _clean3d(a); a.view_init(20, 30)
    a.set_title("closo $[\\mathrm{B_6H_6}]^{2-}$\n$n=6$: 7 pairs $=n+1$", fontsize=10)
    b = fig.add_subplot(1, 4, 2, projection="3d")
    keep = [0, 1, 2, 3, 4]
    V = [oct_v[i] for i in keep]
    ed = [(keep.index(i), keep.index(j)) for i, j in edges if i in keep and j in keep]
    _wire(b, V, ed); _points(b, V, color=BLUE)
    # bridging H on the 4 basal edges (dashed)
    base = [(0, 2), (2, 1), (1, 3), (3, 0)]
    for i, j in base:
        m = (np.array(V[i]) + np.array(V[j])) / 2 * 1.25 + np.array([0, 0, -0.35])
        b.scatter(*m, color=ORANGE, s=28, depthshade=False)
        for k in (i, j):
            b.plot(*zip(m, V[k]), color=ORANGE, lw=1, ls="--")
    _clean3d(b); b.view_init(20, 30)
    b.set_title("nido $\\mathrm{B_5H_9}$: octahedron minus a vertex\n$n=5$: 7 pairs $=n+2$", fontsize=10)
    c = fig.add_subplot(1, 4, 3, projection="3d")
    keep = [1, 2, 3, 4]
    V = [oct_v[i] for i in keep]
    ed = [(keep.index(i), keep.index(j)) for i, j in edges if i in keep and j in keep]
    _wire(c, V, ed); _points(c, V, color=BLUE); _clean3d(c); c.view_init(35, 80)
    c.set_title("arachno $\\mathrm{B_4H_{10}}$: minus two adjacent\n$n=4$: 7 pairs $=n+3$", fontsize=10)
    d = fig.add_subplot(1, 4, 4, projection="3d")
    phi = (1 + 5 ** 0.5) / 2
    ico = [(0, s1, s2 * phi) for s1 in (1, -1) for s2 in (1, -1)] + [(s1, s2 * phi, 0) for s1 in (1, -1) for s2 in (1, -1)] + [(s2 * phi, 0, s1) for s1 in (1, -1) for s2 in (1, -1)]
    ico = [tuple(np.array(v) / 1.9) for v in ico]
    ed = [(i, j) for i, j in itertools.combinations(range(12), 2) if abs(np.linalg.norm(np.array(ico[i]) - np.array(ico[j])) - 2 / 1.9) < 1e-6]
    _wire(d, ico, ed, lw=1.2); _points(d, ico, color=BLUE, s=45); _clean3d(d, 0.85); d.view_init(20, 30)
    d.set_title("closo $[\\mathrm{B_{12}H_{12}}]^{2-}$: icosahedron\n$n=12$: 13 pairs $=n+1$", fontsize=10)
    fig.tight_layout(); save(fig, "fig_ch07_wade")


def fig_ch07_diborane_zintl():
    fig = plt.figure(figsize=(16, 5.2))
    a = fig.add_subplot(1, 3, 1, projection="3d")
    B = [(-0.87, 0, 0), (0.87, 0, 0)]; Hb = [(0, 0.98, 0), (0, -0.98, 0)]
    Ht = []
    for bx in (-0.87, 0.87):
        sgn = np.sign(bx)
        Ht.append((bx + sgn * 0.6, 0, 1.03)); Ht.append((bx + sgn * 0.6, 0, -1.03))
    for b in B:
        for h in Hb:
            a.plot(*zip(b, h), color=ORANGE, lw=2, ls="--")
    for b, h in zip([B[0], B[0], B[1], B[1]], Ht):
        a.plot(*zip(b, h), color=INK, lw=2)
    a.scatter(*zip(*B), color=BLUE, s=220, depthshade=False, edgecolor=INK); a.scatter(*zip(*Hb), color=ORANGE, s=90, depthshade=False, edgecolor=INK); a.scatter(*zip(*Ht), color="white", s=90, depthshade=False, edgecolor=INK)
    a.set_xlim(-2, 2); a.set_ylim(-1.5, 1.5); a.set_zlim(-1.5, 1.5); a.set_axis_off(); a.view_init(25, 35); a.set_box_aspect((1.3, 1, 1))
    a.set_title("A  $\\mathrm{B_2H_6}$: 4 terminal (2c–2e) + 2 bridges (3c–2e)\nB–H$_t$ 1.19 Å, B–H$_b$ 1.31 Å, B–H–B 83°", fontsize=9.5)
    b = fig.add_subplot(1, 3, 2)
    b.set_xlim(0, 4); b.set_ylim(-2.3, 2.3); b.axis("off")
    for y, lab, n, col in ((-1.414, "bonding $\\psi_1$", 2, BLUE), (0.0, "nonbonding $\\psi_2$", 0, MUTED), (1.414, "antibonding $\\psi_3$", 0, ORANGE)):
        b.hlines(y, 1.4, 2.6, color=col, lw=3); b.text(2.7, y, lab, va="center", fontsize=9)
        if n:
            electrons(b, 2.0, y, 2)
    b.hlines(0, 0.0, 0.7, color=MUTED, lw=2); b.text(0.35, 0.25, "H 1s", ha="center", fontsize=8.5)
    b.hlines(0.0, 3.5, 4.0, color=MUTED, lw=2); b.text(3.9, 0.25, "$\\mathrm{B\\,sp^3}\\times2$", ha="center", fontsize=8.5)
    b.text(2.0, 2.0, "3-centre MO (B–H–B): 2 e⁻ bind 3 atoms", ha="center", fontsize=9)
    b.text(2.0, -2.15, "stabilisation $2\\sqrt{2}|\\beta|=2.83|\\beta|$ vs $2|\\beta|$ for a 2c–2e pair", ha="center", fontsize=8.3)
    b.set_title("B  one bridge: Hückel levels $\\alpha\\pm\\sqrt{2}\\beta,\\alpha$")
    c = fig.add_subplot(1, 3, 3)
    sp = ["Sn$_5^{2-}$", "Sn$_9^{4-}$", "Bi$_8^{2+}$", "Bi$_5^{3+}$"]
    gv = [22, 40, 38, 22]; n_ = [5, 9, 8, 5]
    cl = ["closo", "nido", "arachno", "closo"]
    for i, (s_, g, n, k) in enumerate(zip(sp, gv, n_, cl)):
        pairs = (g - 2 * n) / 2
        c.bar(i, pairs, color={"closo": BLUE, "nido": AQUA, "arachno": ORANGE}[k])
        c.bar(i, n, color="none", edgecolor=INK, hatch="//")
        c.text(i, pairs + 0.3, f"{k}\n$g-2n={g-2*n}$", ha="center", fontsize=8.5)
    c.set_xticks(range(4)); c.set_xticklabels(sp); c.set_ylabel("skeletal electron pairs $(g-2n)/2$ (hatched: $n$)")
    c.set_title("C  Zintl ions: $g-2n$ and the class (pairs $-n=1,2,3$)")
    fig.tight_layout(); save(fig, "fig_ch07_diborane_zintl")


def fig_ch07_p4():
    fig = plt.figure(figsize=(16, 4.8))
    P = np.array([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]) / math.sqrt(3) * 1.1
    edges = list(itertools.combinations(range(4), 2))
    titles = ["white phosphorus $\\mathrm{P_4}$\n6 P–P edges, 60°", "$\\mathrm{P_4O_6}$: O in each edge", "$\\mathrm{P_4O_{10}}$: + terminal P=O", "$\\mathrm{P_4S_3}$: S in 3 basal edges"]
    for k in range(4):
        a = fig.add_subplot(1, 4, k + 1, projection="3d")
        a.scatter(*zip(*P), color=BLUE, s=160, depthshade=False, edgecolor=INK)
        for (i, j) in edges:
            m = (P[i] + P[j]) / 2
            if k == 0:
                a.plot(*zip(P[i], P[j]), color=INK, lw=2)
            elif k in (1, 2) or (k == 3 and i > 0):
                o = m * 1.45 / np.linalg.norm(m) * np.linalg.norm(m)
                o = m * 1.7
                a.plot(*zip(P[i], o), color=INK, lw=1.6); a.plot(*zip(P[j], o), color=INK, lw=1.6)
                a.scatter(*o, color=ORANGE if k != 3 else "#d7c200", s=70, depthshade=False, edgecolor=INK)
            else:
                a.plot(*zip(P[i], P[j]), color=INK, lw=2)
        if k == 2:
            for p in P:
                t = p * 1.9
                a.plot(*zip(p, t), color=INK, lw=2, ls=":"); a.scatter(*t, color=ORANGE, s=70, depthshade=False, edgecolor=INK)
        _clean3d(a, 2.0); a.view_init(20, 40)
        a.set_title(titles[k], fontsize=10)
    fig.tight_layout(); save(fig, "fig_ch07_p4")


# ------------------------------------------------------------------ CH08
def fig_ch08_rings():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 5.0))
    a = ax[0]
    def hueck(hB, hN, k):
        H = np.zeros((6, 6))
        for i in range(6):
            H[i, i] = hB if i % 2 == 0 else hN
            H[i, (i + 1) % 6] = H[(i + 1) % 6, i] = k
        w, v = np.linalg.eigh(H); idx = np.argsort(-w)
        return w[idx], v[:, idx]
    wb, vb = hueck(0, 0, 1)
    wz, vz = hueck(-1.0, 1.5, 0.8)
    a.set_xlim(0, 6); a.set_ylim(-3.2, 3.2); a.axis("off")
    for x0, w, lab in ((0.2, wb, "benzene"), (3.6, wz, "borazine")):
        a.text(x0 + 0.9, 3.0, lab, ha="center", fontsize=10)
        ys = -w  # bonding (large positive x => low energy) at the bottom
        groups = {}
        for y in ys:
            groups.setdefault(round(y, 2), 0); groups[round(y, 2)] += 1
        n_filled = 3
        order = np.argsort(ys)
        for rank, i in enumerate(order):
            y = ys[i]
            same = [j for j in order if abs(ys[j] - y) < 0.01]
            pos = same.index(i)
            xa = x0 + 0.2 + pos * 0.7
            a.hlines(y, xa, xa + 0.55, color=INK if rank < 3 else ORANGE, lw=2.5)
            if rank < 3:
                electrons(a, xa + 0.275, y, 2, scale=1.0)
    gap_b = wb[2] - wb[3]; gap_z = wz[2] - wz[3]
    a.text(1.1, -3.05, f"gap {gap_b:.2f}|β|", ha="center", fontsize=9); a.text(4.5, -3.05, f"gap {gap_z:.2f}|β| (larger, colourless)", ha="center", fontsize=9)
    a.set_title("A  Hückel π levels, 6 π electrons")
    b = ax[1]
    b.set_xlim(-1.8, 1.8); b.set_ylim(-1.8, 1.8); b.set_aspect("equal"); b.axis("off")
    for k_, (ttl, charges, col, off) in enumerate((("benzene: π charge 1.00 on every C", [1.0] * 6, MUTED, -1.0), ("borazine (Hückel, h$_B$=−1, h$_N$=1.5): B 0.23, N 1.77", [0.23, 1.77] * 3, BLUE, 0.0))):
        pass
    cx = 0
    for i in range(6):
        ang = PI / 2 - i * PI / 3
        x, y = math.cos(ang), math.sin(ang)
        ang2 = PI / 2 - (i + 1) * PI / 3
        b.plot([x, math.cos(ang2)], [y, math.sin(ang2)], color=INK, lw=2)
    for i in range(6):
        ang = PI / 2 - i * PI / 3
        x, y = math.cos(ang), math.sin(ang)
        isB = (i % 2 == 0)
        q = 0.23 if isB else 1.77
        b.add_patch(Circle((x, y), 0.17 + 0.07 * q, color=ORANGE if isB else BLUE, alpha=0.9))
        b.text(x * 1.32, y * 1.32, ("B" if isB else "N") + f"\n{q:.2f}", ha="center", va="center", fontsize=8.5)
    b.text(0, 0, "B$_3$N$_3$H$_6$\nπ charge\nB 0.23 / N 1.77\nπ bond order 0.44\n(benzene 0.67)", ha="center", va="center", fontsize=8.5)
    b.set_title("B  borazine: lumpy π density, weaker π bonds")
    c = ax[2]
    c.set_xlim(0, 10); c.set_ylim(0, 10); c.axis("off")
    steps = [("(NPCl$_2$)$_3$\nplanar ring, P–N all equal", 0.3, 7.6, BLUE), ("210–250 °C\nring-opening", 3.6, 7.6, MUTED), ("[NPCl$_2$]$_n$\nreactive polymer", 6.5, 7.6, ORANGE),
             ("+ RONa, RNH$_2$,\nR$_2$NH, RM", 6.5, 4.2, MUTED), ("[NPR$_2$]$_n$ polyphosphazenes\nrubbers, films, biomedical", 3.0, 1.2, AQUA)]
    for t, x, y, col in steps:
        c.text(x, y, t, fontsize=8.5, bbox=dict(boxstyle="round", fc="white", ec=col, lw=1.6))
    for (x0, y0, x1, y1) in ((2.8, 8.0, 3.5, 8.0), (5.4, 8.0, 6.4, 8.0), (7.4, 7.4, 7.4, 5.1), (7.2, 3.9, 6.0, 2.2)):
        c.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=14, color=INK, lw=1.4))
    c.set_title("C  from the ring to the polymer (slides 116–119)")
    fig.tight_layout(); save(fig, "fig_ch08_rings")


# ------------------------------------------------------------------ CH09
def fig_ch09_redox():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.8))
    a = ax[0]
    E = np.linspace(-2, 2, 200)
    for nu, col in ((1, BLUE), (2, ORANGE)):
        a.plot(E, nu * F_ * E / (R_ * T_ * math.log(10)), color=col, lw=2, label=f"$\\nu={nu}$")
    a.set_xlabel("$E^\\circ_{\\rm cell}$ (V)"); a.set_ylabel("$\\log_{10}K$")
    a.axhline(0, color=INK, lw=0.7); a.axvline(0, color=INK, lw=0.7)
    a.plot([1.10], [2 * F_ * 1.10 / (R_ * T_ * math.log(10))], "o", color=ORANGE, ms=7); a.text(-1.95, 45, "Daniell cell: 1.10 V, $\\nu=2$,\n$K=10^{37.2}$ (orange dot)", fontsize=8.5)
    a.plot([2], [33.8], "o", color=BLUE, ms=7); a.text(-1.95, 20, "±2 V, $\\nu=1$ ↔ $K=10^{\\pm34}$:\n68 decades in all", fontsize=8.5)
    a.legend(fontsize=8, loc="lower right"); a.set_title("A  $\\log_{10}K=\\nu FE^\\circ/RT\\ln10$ (59.16 mV per decade)")
    b = ax[1]
    logQ = np.linspace(-6, 70, 300)
    b.plot(logQ, 1.10 - 0.05916 / 2 * logQ, color=BLUE, lw=2, label="Daniell ($\\nu=2$): $E=1.10-0.0296\\log Q$")
    b.plot(logQ, 0.74 - 0.05916 / 5 * logQ, color=ORANGE, lw=2, label="MnO$_4^-$+5Fe$^{2+}$ ($\\nu=5$): $E=0.74-0.0118\\log Q$")
    b.axhline(0, color=INK, lw=0.7)
    for lk, col in ((37.2, BLUE), (62.5, ORANGE)):
        b.plot([lk], [0], "o", color=col, ms=7); b.text(lk, 0.1, f"$K=10^{{{lk}}}$", ha="center", fontsize=8.5, color=col)
    b.set_xlabel("$\\log_{10}Q$"); b.set_ylabel("$E$ (V)"); b.legend(fontsize=8, loc="upper right")
    b.set_title("B  Nernst: $E$ falls as the reaction proceeds; $E=0$ at $Q=K$")
    c = ax[2]
    tab = {"Li": (161, 526, -520, 16, -3.04), "Na": (109, 502, -406, 22, -2.71), "Cs": (79, 382, -264, 34, -2.92), "Ag": (284, 735, -468, 29, 0.80)}
    names = list(tab)
    x = np.arange(4)
    comp = [("sublimation", 0, BLUE), ("ionisation", 1, ORANGE), ("hydration", 2, AQUA)]
    bottoms_pos = np.zeros(4); bottoms_neg = np.zeros(4)
    for lab, k, col in comp:
        vals = np.array([tab[n][k] for n in names], float)
        pos = np.where(vals > 0, vals, 0); neg = np.where(vals < 0, vals, 0)
        c.bar(x, pos, bottom=bottoms_pos, color=col, label=lab, width=0.55); bottoms_pos += pos
        c.bar(x, neg, bottom=bottoms_neg, color=col, width=0.55); bottoms_neg += neg
    net = [sum(tab[n][:3]) - 445 for n in names]
    for i, n in enumerate(names):
        dG = net[i] - tab[n][3]
        c.text(i, 1130, f"$\\Delta G$={dG:.0f} kJ/mol\nE°={dG*1000/F_:+.2f} V (table {tab[n][4]:+.2f})", ha="center", fontsize=7.8)
        c.plot([i - 0.3, i + 0.3], [sum(tab[n][:3]), sum(tab[n][:3])], color=INK, lw=2.4)
        c.text(i + 0.32, sum(tab[n][:3]) + 15, f"{sum(tab[n][:3])}", fontsize=8)
    c.axhline(445, color=VIOLET, ls="--", lw=1.2); c.text(-0.45, 470, "$\\Delta_fH^\\circ$(H$^+$,aq)=+445", fontsize=7.5, color=VIOLET)
    c.set_xticks(x); c.set_xticklabels([f"{n}$^+$/{n}" for n in names]); c.set_ylim(-700, 1350)
    c.set_ylabel("kJ/mol (black bar = sum of the three terms)"); c.legend(fontsize=8, loc="lower left")
    c.set_title("C  Table 5.1: Li is most reducing because of hydration")
    fig.tight_layout(); save(fig, "fig_ch09_redox")


def fig_ch09_series_frost():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 5.2))
    a = ax[0]
    couples = [("F$_2$/F$^-$", 2.87), ("Ce$^{4+}$/Ce$^{3+}$", 1.76), ("MnO$_4^-$/Mn$^{2+}$", 1.51), ("Cl$_2$/Cl$^-$", 1.36), ("O$_2$/H$_2$O", 1.23), ("Fe$^{3+}$/Fe$^{2+}$", 0.77), ("I$_3^-$/I$^-$", 0.54),
               ("Cu$^{2+}$/Cu", 0.34), ("H$^+$/H$_2$", 0.0), ("Zn$^{2+}$/Zn", -0.76), ("Al$^{3+}$/Al", -1.68), ("Li$^+$/Li", -3.04)]
    for i, (nm, e) in enumerate(couples):
        a.hlines(e, 0, 1, color=BLUE if e > 0 else ORANGE, lw=2.5); a.text(1.04, e, f"{nm}  {e:+.2f}", va="center", fontsize=8.5)
    a.annotate("", (0.45, 1.51), (0.45, -0.76), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.5)); a.text(0.15, 0.4, "Zn reduces\nMnO$_4^-$ and Cu$^{2+}$\n(E = +2.27 V)", fontsize=8, rotation=0)
    a.set_xlim(0, 2.3); a.set_xticks([]); a.set_ylabel("$E^\\circ$ (V, pH 0)")
    a.set_title("A  electrochemical series: the reduced form reduces any couple above it")
    b = ax[1]
    N = [0, 2, 3, 4, 6, 7]; nE = [0.0, -2.36, -0.85, 0.10, 4.62, 5.18]; names = ["Mn", "Mn$^{2+}$", "Mn$^{3+}$", "MnO$_2$", "MnO$_4^{2-}$", "MnO$_4^-$"]
    b.plot(N, nE, "o-", color=BLUE, lw=2)
    for n_, e_, nm in zip(N, nE, names):
        b.text(n_ + 0.12, e_ + 0.2, nm, fontsize=9)
    b.set_xlabel("oxidation number $N$"); b.set_ylabel("$NE^\\circ$ (V)")
    b.set_title("B  Frost diagram of Mn in acid (extra: S&A 5.13)")
    b.annotate("Mn$^{3+}$ sits above the line\nMn$^{2+}$–MnO$_2$ ⇒ disproportionates", (3, -0.85), (3.9, -2.5), arrowprops=dict(arrowstyle="->", color=ORANGE), fontsize=8, color=ORANGE)
    b.annotate("MnO$_4^{2-}$ above the chord\nMnO$_2$–MnO$_4^-$ ⇒ disproportionates", (6, 4.62), (1.5, 4.5), arrowprops=dict(arrowstyle="->", color=ORANGE), fontsize=8, color=ORANGE)
    c = ax[2]
    pH = np.linspace(0, 14, 100)
    c.plot(pH, 1.51 - 8 / 5 * 0.05916 * pH, color=ORANGE, lw=2, label="MnO$_4^-$/Mn$^{2+}$: −94.7 mV/pH")
    c.plot(pH, 1.229 - 0.05916 * pH, color=BLUE, lw=2, label="O$_2$/H$_2$O: −59.2 mV/pH")
    c.plot(pH, -0.05916 * pH, color=AQUA, lw=2, label="H$^+$/H$_2$: −59.2 mV/pH")
    c.plot(pH, 0.77 + 0 * pH, color=VIOLET, lw=2, ls="--", label="Fe$^{3+}$/Fe$^{2+}$: no H$^+$ (flat, ideal)")
    c.set_xlabel("pH"); c.set_ylabel("$E$ (V)"); c.legend(fontsize=7.5, loc="lower left")
    c.set_title("C  pH dependence: slope $=-(m/\\nu)(59.2\\ \\mathrm{mV})$, $m$ = H$^+$ in the half-reaction (extra: 5.6)")
    fig.tight_layout(); save(fig, "fig_ch09_series_frost")


ALL = [fig_ch02_lcao, fig_ch02_diatomics, fig_ch02_hetero, fig_ch03_h3, fig_ch03_polyatomics, fig_ch04_acidbase, fig_ch05_acids, fig_ch06_hsab,
       fig_ch07_wade, fig_ch07_diborane_zintl, fig_ch07_p4, fig_ch08_rings, fig_ch09_redox, fig_ch09_series_frost]

if __name__ == "__main__":
    pat = sys.argv[1] if len(sys.argv) > 1 else ""
    for f in ALL:
        if pat in f.__name__:
            f()
