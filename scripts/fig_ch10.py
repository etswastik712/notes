"""Figures for CH10 (crystal field theory).   .venv/bin/python -W ignore scripts/fig_ch10.py [name]
All numbers are recomputed in scripts/ch10_numbers.py; the splitting patterns come from the point-charge model itself."""
import itertools
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa

import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle
from scipy.special import sph_harm_y

CM_KJ = 0.0119627
AQUA_LIGHT = "#bfe9d9"


# ------------------------------------------------------------------ point-charge machinery (as in ch10_numbers.py)
def _grid():
    th, wth = np.polynomial.legendre.leggauss(40)
    phi = np.linspace(0, 2 * np.pi, 80, endpoint=False)
    TH, PH = np.meshgrid(np.arccos(th), phi, indexing="ij")
    W = (wth[:, None] * np.ones_like(PH)) * (2 * np.pi / len(phi))
    return TH, PH, W


TH, PH, W = _grid()
X, Y, Z = np.sin(TH) * np.cos(PH), np.sin(TH) * np.sin(PH), np.cos(TH)
cc = math.sqrt(15 / (4 * math.pi))
DORB = {"z2": math.sqrt(5 / (16 * math.pi)) * (3 * Z**2 - 1), "x2-y2": 0.5 * cc * (X**2 - Y**2), "xy": cc * X * Y, "xz": cc * X * Z, "yz": cc * Y * Z}
NAMES = list(DORB)


def realY(l, m, th_, ph_):
    if m == 0:
        return sph_harm_y(l, 0, th_, ph_).real
    y = sph_harm_y(l, abs(m), th_, ph_)
    return math.sqrt(2) * (-1) ** m * (y.real if m > 0 else y.imag)


def ang_diag(l, ligs):
    M = np.zeros((5, 5))
    for m in range(-l, l + 1):
        Ylm = realY(l, m, TH, PH)
        S = sum(realY(l, m, math.acos(np.clip(np.array(v)[2] / np.linalg.norm(v), -1, 1)), math.atan2(v[1], v[0])) for v in ligs)
        for a, na in enumerate(NAMES):
            for b, nb in enumerate(NAMES):
                M[a, b] += 4 * math.pi / (2 * l + 1) * S * np.sum(W * DORB[na] * Ylm * DORB[nb])
    return M


OCT = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
TET = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
EQ = OCT[:4]
AX = OCT[4:]
eo = np.linalg.eigvalsh(ang_diag(4, OCT))
SC4 = 10.0 / (eo.max() - eo.min())            # Dq = 1
E4_eq, E2_eq = np.diag(ang_diag(4, EQ)) * SC4, np.diag(ang_diag(2, EQ))
E4_ax, E2_ax = np.diag(ang_diag(4, AX)) * SC4, np.diag(ang_diag(2, AX))
S_L2 = (-4.28 - E4_eq[0]) / E2_eq[0]          # one fitted number (dz2 of the square-planar ring = -4.28 Dq, Huheey Table 11.5)
LABEL = {"z2": r"$d_{z^2}$", "x2-y2": r"$d_{x^2-y^2}$", "xy": r"$d_{xy}$", "xz": r"$d_{xz}$", "yz": r"$d_{yz}$"}


def energies(rz):
    """Orbital energies (Dq units) for four ligands at R and two at rz R along +-z (rz=1 octahedron, rz->inf square planar)."""
    return E4_eq + S_L2 * E2_eq + (1 / rz) ** 5 * E4_ax + S_L2 * (1 / rz) ** 3 * E2_ax


# ------------------------------------------------------------------ drawing helpers
def arrow(ax, x, y, up=True, h=0.30, color=INK, lw=1.6):
    a, b = (y - h / 2, y + h / 2) if up else (y + h / 2, y - h / 2)
    ax.annotate("", (x, b), (x, a), arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=9), annotation_clip=False)


def box(ax, x, y, n, w=0.46, h=0.62, color=INK, lw=1.5, fc="none"):
    """one orbital 'box' centred at (x,y) holding n (0,1,2) electrons"""
    ax.add_patch(Rectangle((x - w / 2, y - h / 2 * 0.0 - h / 2), w, h, fill=True, fc=fc, ec=color, lw=lw, zorder=2))
    if n >= 1:
        arrow(ax, x - (0.1 if n == 2 else 0), y, True, h=h * 0.8, color=color)
    if n == 2:
        arrow(ax, x + 0.1, y, False, h=h * 0.8, color=color)


def fill_config(nt, ne):
    """occupation of 3 t2g + 2 eg boxes for t2g^nt eg^ne (Hund inside each set)"""
    def spread(n, k):
        occ = [0] * k
        for i in range(n):
            occ[i % k] += 1
        return occ
    return spread(nt, 3), spread(ne, 2)


def draw_cfg(ax, x0, y0, nt, ne, title=None, color=INK, gap=0.45, esep=1.2):
    t, e = fill_config(nt, ne)
    for i, n in enumerate(t):
        box(ax, x0 + i * gap, y0, n, color=color)
    for i, n in enumerate(e):
        box(ax, x0 + (0.5 + i) * gap + 0.0, y0 + esep, n, color=color)
    if title:
        ax.text(x0 + gap, y0 - 0.45, title, ha="center", va="top", fontsize=8.5)


# ================================================================== FIG 1  splitting patterns
def fig_splitting():
    fig = plt.figure(figsize=(13.2, 5.6))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.35, 1], wspace=0.22)
    ax = fig.add_subplot(gs[0])
    ax.set_xlim(0, 10.4)
    ax.set_ylim(-7.4, 14.2)
    ax.axis("off")
    ax.set_title("A. Point-charge d-orbital energies ($Dq=\\Delta_O/10$)")

    def panel(x0, title, levels, delta_lab):
        ax.text(x0 + 1.55, 13.1, title, ha="center", fontsize=10, fontweight="semibold")
        ax.hlines(0, x0, x0 + 0.55, color=MUTED, lw=1.5, ls=":")
        ax.text(x0 + 0.27, -0.55, "barycentre", ha="center", fontsize=7.5, color=MUTED)
        for (nm, e, xo, col) in levels:
            ax.hlines(e, x0 + 0.95 + xo, x0 + 2.0 + xo, color=col, lw=3)
            ax.text(x0 + 2.07 + xo, e, nm, va="center", fontsize=8.5)
        return

    # octahedral
    panel(0.1, "octahedral $O_h$", [(r"$e_g$  +6", 6.0, 0, ORANGE), (r"$t_{2g}$  −4", -4.0, 0, BLUE)], "")
    ax.annotate("", (1.85, 5.9), (1.85, -3.9), arrowprops=dict(arrowstyle="<->", color=INK, lw=1.2))
    ax.text(1.05, 1.0, r"$\Delta_O=10\,Dq$", fontsize=9, ha="center", rotation=90)
    ax.text(1.6, 7.6, r"$+\frac{3}{5}\Delta_O$", fontsize=8.5, color=ORANGE, ha="center")
    ax.text(1.6, -5.3, r"$-\frac{2}{5}\Delta_O$", fontsize=8.5, color=BLUE, ha="center")
    # tetrahedral
    panel(3.5, "tetrahedral $T_d$", [(r"$t_2$  +1.78", 1.78, 0, BLUE), (r"$e$  −2.67", -2.67, 0, ORANGE)], "")
    ax.annotate("", (5.35, 1.7), (5.35, -2.6), arrowprops=dict(arrowstyle="<->", color=INK, lw=1.2))
    ax.text(4.15, -0.4, r"$\Delta_T=\frac{4}{9}\Delta_O$", fontsize=9, ha="center", rotation=90)
    ax.text(5.2, 3.3, r"$+\frac{2}{5}\Delta_T$", fontsize=8.5, color=BLUE, ha="center")
    ax.text(5.2, -4.2, r"$-\frac{3}{5}\Delta_T$", fontsize=8.5, color=ORANGE, ha="center")
    # square planar (computed)
    es = energies(1e6)
    order = [("x2-y2", ORANGE), ("xy", VIOLET), ("z2", AQUA), ("xz", BLUE)]
    lev = []
    for nm, col in order:
        i = NAMES.index(nm)
        lab = LABEL[nm] if nm != "xz" else r"$d_{xz},d_{yz}$"
        lev.append((f"{lab}  {es[i]:+.2f}".replace("-", "−"), es[i], 0, col))
    panel(6.9, "square planar $D_{4h}$", lev, "")
    ax.text(8.5, -7.0, "same M–L distance and ligand;\nnumbers computed (Huheey Table 11.5)", fontsize=7.5, color=MUTED, ha="center")

    # B: correlation Oh -> D4h -> square planar
    ax2 = fig.add_subplot(gs[1])
    rz = np.linspace(1.0, 3.0, 120)
    E = np.array([energies(r) for r in rz])
    cols = {"z2": AQUA, "x2-y2": ORANGE, "xy": VIOLET, "xz": BLUE, "yz": BLUE}
    for nm in ("z2", "x2-y2", "xy", "xz"):
        i = NAMES.index(nm)
        ax2.plot(rz, E[:, i], color=cols[nm], lw=2.3)
        ax2.text(3.04, E[-1, i], LABEL[nm] if nm != "xz" else r"$d_{xz},d_{yz}$", va="center", fontsize=8.5)
    ax2.axvline(1.0, color=GRID, lw=1)
    ax2.set_xlim(0.95, 3.7)
    ax2.set_xlabel("distance of the two $z$ ligands, $R_z/R$   ($1$ = octahedron, $\\infty$ = square planar)")
    ax2.set_ylabel("orbital energy / $Dq$")
    ax2.set_title("B. Removing the trans ligands (Huheey Fig. 11.12, computed)")
    ax2.text(1.02, 6.6, r"$e_g$", color=ORANGE, fontsize=9)
    ax2.text(1.02, -5.4, r"$t_{2g}$", color=BLUE, fontsize=9)
    ax2.annotate("tetragonal\nelongation\n(Jahn–Teller)", (1.35, 3.2), fontsize=8, color=MUTED, ha="center")
    fig.suptitle("Crystal-field splitting patterns: the barycentre is fixed, the pattern is set by the geometry", y=1.0, fontsize=12, fontweight="semibold")
    save(fig, "fig_ch10_splitting")


# ================================================================== FIG 2  high spin vs low spin
def fig_spin():
    fig = plt.figure(figsize=(13.6, 5.8))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.25, 1, 1], wspace=0.28)
    ax = fig.add_subplot(gs[0])
    ax.set_xlim(0, 10.0)
    ax.set_ylim(-1.2, 9.0)
    ax.axis("off")
    ax.set_title("A. $d^4$ to $d^7$: two ground states (S&A Table 20.2)")
    ax.text(2.5, 8.5, "weak field  ($\\Delta_O<P$)\nhigh spin", ha="center", fontsize=9.5, color=ORANGE, fontweight="semibold")
    ax.text(7.5, 8.5, "strong field  ($\\Delta_O>P$)\nlow spin", ha="center", fontsize=9.5, color=BLUE, fontweight="semibold")
    lf = {4: ("0.6", "1.6−P", 4, 2), 5: ("0", "2.0−2P", 5, 1), 6: ("0.4", "2.4−2P", 4, 0), 7: ("0.8", "1.8−P", 3, 1)}
    for r, n in enumerate((4, 5, 6, 7)):
        y = 6.2 - 2.05 * r
        ex = {4: ((3, 1), (4, 0)), 5: ((3, 2), (5, 0)), 6: ((4, 2), (6, 0)), 7: ((5, 2), (6, 1))}[n]
        draw_cfg(ax, 1.6, y, *ex[0], color=ORANGE, gap=0.62, esep=1.0)
        draw_cfg(ax, 6.6, y, *ex[1], color=BLUE, gap=0.62, esep=1.0)
        ax.text(0.15, y + 0.4, f"$d^{n}$", fontsize=12, fontweight="semibold", va="center")
        ax.text(2.55, y - 0.42, f"LFSE = {lf[n][0]} $\\Delta_O$,  $N$={ {4:4,5:5,6:4,7:3}[n] }", ha="center", fontsize=8, va="top")
        ax.text(7.55, y - 0.42, f"LFSE = {lf[n][1]} $\\Delta_O$,  $N$={ {4:2,5:1,6:0,7:1}[n] }".replace("−", "−"), ha="center", fontsize=8, va="top")

    # B: E_LS - E_HS
    ax2 = fig.add_subplot(gs[1])
    x = np.linspace(0, 2.0, 100)
    for n, k, col in ((4, 1, BLUE), (5, 2, ORANGE), (6, 2, AQUA), (7, 1, VIOLET)):
        ax2.plot(x, k * (1 - x), color=col, lw=2.2 if k == 2 else 2.2, ls="-" if k == 2 else "--")
        pass
    ax2.text(2.02, -1.0, "$d^4,d^7$", color=VIOLET, va="center", fontsize=9)
    ax2.text(2.02, -2.0, "$d^5,d^6$", color=AQUA, va="center", fontsize=9)
    ax2.axhline(0, color=INK, lw=0.8)
    ax2.axvline(1, color=MUTED, lw=1, ls=":")
    ax2.set_xlim(0, 2.45)
    ax2.set_xlabel("$\\Delta_O/P$")
    ax2.set_ylabel("$(E_{\\rm LS}-E_{\\rm HS})/P$ for a unit-$P$ pairing cost")
    ax2.set_title("B. All four cross at $\\Delta_O=P$")
    ax2.text(0.5, 1.55, "high spin\nwins", ha="center", color=ORANGE, fontsize=9)
    ax2.text(1.6, -1.6, "low spin\nwins", ha="center", color=BLUE, fontsize=9)
    ax2.text(1.02, 1.5, "$d^5,d^6$: slope $-2$ ; $d^4,d^7$: slope $-1$", fontsize=7.5, color=MUTED)

    # C: observed spin states vs Delta_O and P
    ax3 = fig.add_subplot(gs[2])
    data = [("[Fe(H$_2$O)$_6$]$^{3+}$", 14000, 29876, "H"), ("[Fe(CN)$_6$]$^{3-}$", 35000, 29876, "L"), ("[Fe(H$_2$O)$_6$]$^{2+}$", 10400, 14562, "H"),
            ("[Fe(CN)$_6$]$^{4-}$", 32200, 14562, "L"), ("[CoF$_6$]$^{3-}$", 13100, 19151, "H"), ("[Co(H$_2$O)$_6$]$^{3+}$", 20760, 19151, "L"),
            ("[Co(NH$_3$)$_6$]$^{3+}$", 22870, 19151, "L"), ("[Mn(H$_2$O)$_6$]$^{2+}$", 8500, 23824, "H")]
    ax3.plot([5, 40], [5, 40], color=MUTED, lw=1.2, ls="--")
    ax3.text(34, 37.5, "$\\Delta_O=P$", fontsize=8.5, color=MUTED, rotation=38)
    for nm, d, p, s in data:
        ax3.plot(p / 1000, d / 1000, "o" if s == "L" else "s", ms=8, color=BLUE if s == "L" else ORANGE, mec=INK, mew=0.6)
    offs = {"[Fe(H$_2$O)$_6$]$^{3+}$": (-30, -16), "[Fe(CN)$_6$]$^{3-}$": (-30, 9), "[Fe(H$_2$O)$_6$]$^{2+}$": (-30, -17), "[Fe(CN)$_6$]$^{4-}$": (9, -3),
            "[CoF$_6$]$^{3-}$": (8, 6), "[Co(H$_2$O)$_6$]$^{3+}$": (10, -12), "[Co(NH$_3$)$_6$]$^{3+}$": (10, 3), "[Mn(H$_2$O)$_6$]$^{2+}$": (-30, -17)}
    for nm, d, p, s in data:
        ax3.annotate(nm, (p / 1000, d / 1000), xytext=offs[nm], textcoords="offset points", fontsize=7.5)
    ax3.set_xlim(10, 38)
    ax3.set_ylim(5, 40)
    ax3.set_xlabel("pairing energy $P$ of the free ion / $10^3$ cm$^{-1}$ (Huheey Table 11.4)")
    ax3.set_ylabel("$\\Delta_O$ / $10^3$ cm$^{-1}$")
    ax3.set_title("C. The rule $\\Delta_O\\gtrless P$ against experiment")
    ax3.plot([], [], "s", color=ORANGE, mec=INK, mew=0.6, label="observed high spin")
    ax3.plot([], [], "o", color=BLUE, mec=INK, mew=0.6, label="observed low spin")
    ax3.legend(loc="upper left", fontsize=8)
    save(fig, "fig_ch10_spin")


# ================================================================== FIG 3  LFSE, OSPE
def lfse_oct_hs(n):
    nt, ne = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (5, 2), (6, 2), (6, 3), (6, 4)][n]
    return 0.4 * nt - 0.6 * ne


def lfse_oct_ls(n):
    nt, ne = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4)][n]
    return 0.4 * nt - 0.6 * ne


def lfse_tet(n):
    ne = min(n, 2) + max(0, min(n - 5, 2))
    nt = n - ne
    return (0.6 * ne - 0.4 * nt) * 4 / 9


def fig_lfse():
    fig = plt.figure(figsize=(13.6, 5.2))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.1, 1, 1.05], wspace=0.30)
    n = np.arange(11)
    ax = fig.add_subplot(gs[0])
    ax.plot(n, [lfse_oct_hs(i) for i in n], "o-", color=BLUE, mfc="white", ms=7, label="octahedral, high spin")
    ax.plot(n, [lfse_oct_ls(i) for i in n], "s--", color=ORANGE, ms=5.5, label="octahedral, low spin (before pairing cost)")
    ax.plot(n, [lfse_tet(i) for i in n], "^-", color=AQUA, ms=6.5, label="tetrahedral ($\\Delta_T=\\frac{4}{9}\\Delta_O$)")
    ax.set_xlabel("number of $d$ electrons, $n$")
    ax.set_ylabel("LFSE / $\\Delta_O$")
    ax.set_xticks(range(11))
    ax.set_title("A. LFSE (S&A Fig 20.13)")
    ax.legend(fontsize=8, loc="upper center")
    ax.set_ylim(-0.05, 2.9)

    ax2 = fig.add_subplot(gs[1])
    ospe = [lfse_oct_hs(i) - lfse_tet(i) for i in n]
    cols = [BLUE if o > 0.7 else (AQUA if o > 0.1 else GRID) for o in ospe]
    ax2.bar(n, ospe, color=cols, edgecolor=MUTED, lw=0.6)
    for i, o in enumerate(ospe):
        if o > 0.01:
            ax2.text(i, o + 0.02, f"{o:.2f}", ha="center", fontsize=8)
    ax2.set_xticks(range(11))
    ax2.set_xlabel("number of $d$ electrons, $n$ (high spin)")
    ax2.set_ylabel("OSPE / $\\Delta_O$")
    ax2.set_title("B. Octahedral site preference energy")
    ax2.text(5, 0.95, "$d^3,d^8$ (Cr$^{3+}$, Ni$^{2+}$)\nthe strongest preference;\n$d^0,d^5,d^{10}$ none", fontsize=8, ha="center")
    ax2.set_ylim(0, 1.15)

    ax3 = fig.add_subplot(gs[2])
    ions = [("Cr$^{3+}$ $d^3$", 175.8), ("Ni$^{2+}$ $d^8$", 85.9), ("Mn$^{3+}$ $d^4$", 106.1), ("Co$^{2+}$ $d^7$", 29.3), ("Fe$^{2+}$ $d^6$", 16.6), ("Fe$^{3+}$ $d^5$", 0.0), ("Mn$^{2+}$ $d^5$", 0.0)]
    ions.sort(key=lambda t: t[1])
    ax3.barh([i[0] for i in ions], [i[1] for i in ions], color=BLUE, edgecolor=MUTED, lw=0.6)
    for k, (nm, v) in enumerate(ions):
        ax3.text(v + 3, k, f"{v:.0f}" if v >= 10 else f"{v:.0f}", va="center", fontsize=8)
    ax3.set_xlabel("OSPE / kJ mol$^{-1}$ (aqua $\\Delta_O$, $\\Delta_T=\\frac{4}{9}\\Delta_O$)")
    ax3.set_title("C. Spinel site choice")
    ax3.text(90, 0.2, "Fe$_3$O$_4$: Fe$^{2+}$ (17) vs Fe$^{3+}$ (0)\n→ Fe$^{2+}$ goes octahedral: inverse\nMn$_3$O$_4$: Mn$^{3+}$ (106) vs Mn$^{2+}$ (0)\n→ normal", fontsize=7.8, va="bottom")
    ax3.set_xlim(0, 215)
    save(fig, "fig_ch10_lfse")


# ================================================================== FIG 4  thermochemistry
def fig_thermo():
    fig = plt.figure(figsize=(13.6, 5.2))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.2, 1, 1], wspace=0.30)
    ax = fig.add_subplot(gs[0])
    ions = ["Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"]
    nd = dict(zip(ions, range(0, 11)))
    hyd = {"Ca": 2468, "V": 2814, "Cr": 2799, "Mn": 2743, "Fe": 2843, "Co": 2904, "Ni": 2986, "Cu": 2989, "Zn": 2936}
    dO = {"V": 12400, "Cr": 13900, "Mn": 8500, "Fe": 10400, "Co": 9200, "Ni": 8500, "Cu": 12600}
    lf = {"V": 1.2, "Cr": 0.6, "Mn": 0.0, "Fe": 0.4, "Co": 0.8, "Ni": 1.2, "Cu": 0.6}
    xs = np.array([nd[k] for k in hyd])
    yo = np.array([hyd[k] for k in hyd], float)
    yc = np.array([hyd[k] - lf.get(k, 0) * dO.get(k, 0) * CM_KJ for k in hyd])
    ax.plot(xs, yo, "o-", color=BLUE, mfc="white", ms=7, label="observed $-\\Delta_{\\rm hyd}H$")
    ax.plot(xs, yc, "o-", color=ORANGE, ms=6, label="after subtracting the high-spin LFSE")
    ax.set_xticks(range(11))
    ax.set_xticklabels(ions)
    ax.set_ylabel("$-\\Delta_{\\rm hyd}H^\\circ$ (M$^{2+}$) / kJ mol$^{-1}$")
    ax.set_title("A. The double hump of S&A Fig 20.7, recomputed")
    ax.legend(fontsize=8, loc="upper left")
    for k in ("V", "Ni"):
        ax.annotate(f"{lf[k]}$\\Delta_O$={lf[k]*dO[k]*CM_KJ:.0f} kJ", (nd[k], (hyd[k] + yc[list(hyd).index(k)]) / 2), xytext=(18, -8), textcoords="offset points", fontsize=7.5,
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))

    ax2 = fig.add_subplot(gs[1])
    # lattice enthalpies of MO (rock salt) and MF2 relative to a Ca/Mn(/Zn) baseline
    mo = {"CaO": (0, 3460), "TiO": (2, 3878), "VO": (3, 3913), "MnO": (5, 3810)}
    base = lambda d: 3460 + (3810 - 3460) / 5 * d
    ax2.plot([0, 5], [3460, 3810], color=MUTED, ls="--", lw=1.3, label="linear baseline Ca→Mn ($d^0$, high-spin $d^5$)")
    for nm, (d, v) in mo.items():
        ax2.plot(d, v, "o", color=BLUE, ms=8, mec=INK, mew=0.6)
        ax2.annotate(nm, (d, v), xytext=(6, 5), textcoords="offset points", fontsize=8.5)
    for nm, d, lfv in (("TiO", 2, 0.8), ("VO", 3, 1.2)):
        v = mo[nm][1]
        ax2.annotate("", (d, v), (d, base(d)), arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.6))
        ax2.text(d + 0.1, (v + base(d)) / 2, f"{lfv}$\\Delta_O$\n= +{v-base(d):.0f}", color=ORANGE, fontsize=8, va="center")
    ax2.set_xlabel("number of $d$ electrons of M$^{2+}$")
    ax2.set_ylabel("lattice enthalpy of MO / kJ mol$^{-1}$")
    ax2.set_title("B. S&A Example 20.3")
    ax2.legend(fontsize=7.5, loc="lower right")
    ax2.set_xlim(-0.4, 5.9)
    ax2.set_ylim(3380, 3980)

    ax3 = fig.add_subplot(gs[2])
    # Shannon octahedral radii (pm), recalled; HS unless marked LS
    d2 = {"Ca": (0, 100), "Ti": (2, 86), "V": (3, 79), "Cr": (4, 80), "Mn": (5, 83), "Fe": (6, 78), "Co": (7, 74.5), "Ni": (8, 69), "Cu": (9, 73), "Zn": (10, 74)}
    d3hs = {"Sc": (0, 74.5), "Ti": (1, 67), "V": (2, 64), "Cr": (3, 61.5), "Mn": (4, 64.5), "Fe": (5, 64.5), "Co": (6, 61), "Ni": (7, 60), "Ga": (10, 62)}
    d3ls = {"Mn": (4, 58), "Fe": (5, 55), "Co": (6, 54.5), "Ni": (7, 56)}
    ax3.plot(*zip(*d2.values()), "o-", color=BLUE, mfc="white", ms=6.5, label="M$^{2+}$ high spin")
    ax3.plot(*zip(*d3hs.values()), "s-", color=ORANGE, mfc="white", ms=6, label="M$^{3+}$ high spin")
    ax3.plot(*zip(*d3ls.values()), "s-", color=ORANGE, ms=6, label="M$^{3+}$ low spin")
    ax3.set_xticks(range(11))
    ax3.set_xlabel("number of $d$ electrons")
    ax3.set_ylabel("octahedral ionic radius / pm")
    ax3.set_title("C. Radii: the double dip (Huheey Fig 11.15)")
    ax3.legend(fontsize=7.5, loc="upper right")
    ax3.text(5.2, 56.5, "low spin: $e_g$ stays empty", fontsize=7.5, color=ORANGE)
    save(fig, "fig_ch10_thermo")


# ================================================================== FIG 5  spectrochemical series and f.g
def fig_spectro():
    fig = plt.figure(figsize=(13.6, 5.4))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.05, 1], wspace=0.25)
    ax = fig.add_subplot(gs[0])
    series = [("Br$^-$", 0.72), ("SCN$^-$", 0.73), ("Cl$^-$", 0.78), ("N$_3^-$", 0.83), ("F$^-$", 0.90), ("H$_2$O", 1.00), ("NCS$^-$", 1.02), ("gly", 1.18), ("py", 1.23),
              ("NH$_3$", 1.25), ("en", 1.28), ("bpy", 1.33), ("CN$^-$", 1.70)]
    cols = [ORANGE if f < 1 else (MUTED if f == 1.0 else BLUE) for _, f in series]
    ax.bar(range(len(series)), [f for _, f in series], color=cols, edgecolor=INK, lw=0.5)
    ax.set_xticks(range(len(series)))
    ax.set_xticklabels([s for s, _ in series], rotation=45, ha="right", fontsize=9)
    ax.axhline(1.0, color=INK, lw=0.8)
    for i, (_, f) in enumerate(series):
        ax.text(i, f + 0.02, f"{f:.2f}", ha="center", fontsize=7.5)
    ax.set_ylabel("Jørgensen $f$ (water = 1.00)")
    ax.set_title("A. Spectrochemical series: $\\Delta_O=f\\,g$ (Huheey Table 11.7, eq. 11.5)")
    ax.text(0.2, 1.7, "weak-field → strong-field", fontsize=9, color=MUTED)
    ax.annotate("", (12.2, 1.65), (3.6, 1.65), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.2))
    ax.set_ylim(0, 1.85)
    ax.text(2.4, 1.28, "donor atoms:\nhalides < O < N < C\n($\\pi$-donors low,\n$\\pi$-acceptors high)", fontsize=8, ha="center", color=INK, bbox=dict(boxstyle="round", fc="white", ec=GRID))

    ax2 = fig.add_subplot(gs[1])
    f_lig = {"H2O": 1.00, "en": 1.28, "CN": 1.70, "F": 0.90, "NH3": 1.25}
    g_met = {"Cr3": 17.4, "Co3": 18.2, "Fe3": 14.0, "Rh3": 27.0, "Co2": 9.3}
    obs = [("[Cr(H$_2$O)$_6$]$^{3+}$", "H2O", "Cr3", 17400), ("[Cr(en)$_3$]$^{3+}$", "en", "Cr3", 22300), ("[Cr(CN)$_6$]$^{3-}$", "CN", "Cr3", 26600),
           ("[CrF$_6$]$^{3-}$", "F", "Cr3", 15060), ("[Co(NH$_3$)$_6$]$^{3+}$", "NH3", "Co3", 22870), ("[Co(H$_2$O)$_6$]$^{3+}$", "H2O", "Co3", 20760),
           ("[Co(en)$_3$]$^{3+}$", "en", "Co3", 23160), ("[CoF$_6$]$^{3-}$", "F", "Co3", 13100), ("[Fe(H$_2$O)$_6$]$^{3+}$", "H2O", "Fe3", 14000),
           ("[Fe(CN)$_6$]$^{3-}$", "CN", "Fe3", 35000), ("[Rh(NH$_3$)$_6$]$^{3+}$", "NH3", "Rh3", 34100), ("[Rh(H$_2$O)$_6$]$^{3+}$", "H2O", "Rh3", 27200),
           ("[Co(H$_2$O)$_6$]$^{2+}$", "H2O", "Co2", 9200), ("[Co(NH$_3$)$_6$]$^{2+}$", "NH3", "Co2", 10200)]
    xx = np.linspace(5, 40, 10)
    ax2.fill_between(xx, 0.9 * xx, 1.1 * xx, color=AQUA_LIGHT, alpha=0.7, lw=0, label="±10 %")
    ax2.plot(xx, xx, color=MUTED, lw=1)
    for nm, l, m, o in obs:
        pr = f_lig[l] * g_met[m]
        out = abs(pr - o / 1000) / (o / 1000) > 0.15
        ax2.plot(pr, o / 1000, "o", color=ORANGE if out else BLUE, ms=7, mec=INK, mew=0.5, zorder=3)
        if out or nm.startswith("[Rh(NH") or nm.startswith("[Cr(CN"):
            ax2.annotate(nm, (pr, o / 1000), xytext=(6, -3), textcoords="offset points", fontsize=7.5)
    ax2.set_xlabel("predicted $f\\,g$ / $10^3$ cm$^{-1}$")
    ax2.set_ylabel("observed $\\Delta_O$ / $10^3$ cm$^{-1}$")
    ax2.set_xlim(5, 38)
    ax2.set_ylim(5, 38)
    ax2.set_title("B. How well it works (mean error 7 %; CN$^-$ is the outlier)")
    ax2.legend(loc="upper left", fontsize=8)
    save(fig, "fig_ch10_spectro")


# ================================================================== FIG 6  Jahn-Teller
def fig_jt():
    fig = plt.figure(figsize=(13.6, 5.2))
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.15], wspace=0.28)
    ax = fig.add_subplot(gs[0])
    Q = np.linspace(-2.2, 2.2, 300)
    k, al = 1.0, 1.0
    ax.plot(Q, 0.5 * k * Q**2, color=MUTED, ls="--", lw=1.4, label="no electronic term")
    ax.plot(Q, 0.5 * k * Q**2 - al * np.abs(Q), color=BLUE, lw=2.4, label="occupied branch ($\\frac{1}{2}kQ^2-\\alpha|Q|$)")
    ax.plot(Q, 0.5 * k * Q**2 + al * np.abs(Q), color=ORANGE, lw=2.0, label="empty branch")
    ax.plot([-1, 1], [-0.5, -0.5], "o", color=BLUE, ms=8)
    ax.annotate("$E_{JT}=-\\alpha^2/2k$", (1, -0.5), xytext=(1.0, 1.1), fontsize=9, arrowprops=dict(arrowstyle="->", color=INK))
    ax.set_xlabel("tetragonal distortion $Q$  (+: $z$ elongated, −: $z$ compressed)")
    ax.set_ylabel("energy (arbitrary units)")
    ax.set_title("A. A degenerate $e_g$ state is unstable (S&A p.482)")
    ax.legend(fontsize=7.5, loc="upper center")
    ax.set_ylim(-0.9, 4.3)

    ax2 = fig.add_subplot(gs[1])
    ax2.set_xlim(0, 6)
    ax2.set_ylim(-3.2, 4.2)
    ax2.axis("off")
    ax2.set_title("B. Cu$^{2+}$ ($d^9$): $O_h\\to D_{4h}$ elongation")
    # Oh levels
    for x0, ys, labs, cols in ((0.4, (2.0, -1.3), ("$e_g$", "$t_{2g}$"), (ORANGE, BLUE)),):
        ax2.hlines(2.0, 0.4, 1.4, color=ORANGE, lw=3)
        ax2.hlines(-1.3, 0.4, 1.4, color=BLUE, lw=3)
        ax2.text(0.15, 2.0, "$e_g$", ha="right", va="center", color=ORANGE)
        ax2.text(0.15, -1.3, "$t_{2g}$", ha="right", va="center", color=BLUE)
    # D4h
    d1, d2 = 1.4, 0.5
    ax2.hlines(2.0 + d1 / 2, 4.0, 5.0, color=ORANGE, lw=3); ax2.text(5.1, 2.0 + d1 / 2, r"$d_{x^2-y^2}$", va="center", fontsize=9)
    ax2.hlines(2.0 - d1 / 2, 4.0, 5.0, color=ORANGE, lw=3); ax2.text(5.1, 2.0 - d1 / 2, r"$d_{z^2}$", va="center", fontsize=9)
    ax2.hlines(-1.3 + 2 * d2 / 3, 4.0, 5.0, color=BLUE, lw=3); ax2.text(5.1, -1.3 + 2 * d2 / 3, r"$d_{xy}$", va="center", fontsize=9)
    ax2.hlines(-1.3 - d2 / 3, 4.0, 5.0, color=BLUE, lw=3); ax2.text(5.1, -1.3 - d2 / 3, r"$d_{xz},d_{yz}$", va="center", fontsize=9)
    for (ya, yb) in ((2.0, 2.0 + d1 / 2), (2.0, 2.0 - d1 / 2), (-1.3, -1.3 + 2 * d2 / 3), (-1.3, -1.3 - d2 / 3)):
        ax2.plot([1.4, 4.0], [ya, yb], color=MUTED, lw=0.9)
    # electrons d9
    def pair(x, y, n):
        for dx, up in ((-0.12, True), (0.12, False))[:n]:
            arrow(ax2, x + dx, y, up, h=0.5)
    pair(4.5, 2.0 - d1 / 2, 2); pair(4.5, 2.0 + d1 / 2, 1)
    pair(4.5, -1.3 + 2 * d2 / 3, 2)
    pair(4.25, -1.3 - d2 / 3, 2); pair(4.75, -1.3 - d2 / 3, 2)
    ax2.text(2.7, 3.5, "net gain  $\\delta_1/2$", fontsize=10, ha="center", color=INK)
    ax2.text(2.7, 3.0, "($2\\times(-\\delta_1/2)+1\\times(+\\delta_1/2)$)", fontsize=8, ha="center", color=MUTED)
    ax2.text(4.5, -2.6, "$t_{2g}^6$: no net change", fontsize=8.5, ha="center", color=MUTED)
    ax2.annotate("", (3.55, 2.0 + d1 / 2), (3.55, 2.0 - d1 / 2), arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
    ax2.text(3.45, 2.0, "$\\delta_1$", ha="right", va="center", fontsize=9)

    ax3 = fig.add_subplot(gs[2])
    ax3.set_xlim(0, 11)
    ax3.set_ylim(0, 4)
    ax3.axis("off")
    ax3.set_title("C. Which octahedral configurations distort?")
    cell = {0: "none", 1: "weak", 2: "weak", 3: "none", 4: ("strong", "weak"), 5: ("none", "weak"), 6: ("weak", "none"), 7: ("weak", "strong"), 8: "none", 9: "strong", 10: "none"}
    colmap = {"none": "#e9e8e4", "weak": "#ffd9a8", "strong": "#f08a62"}
    for n in range(0, 11):
        x = 0.1 + n * 0.98
        ax3.text(x + 0.42, 3.45, f"$d^{{{n}}}$", ha="center", fontsize=9.5, fontweight="semibold")
        c = cell[n]
        for r, lab in ((0, "high spin"), (1, "low spin")):
            v = c if isinstance(c, str) else c[r]
            if isinstance(c, str) and r == 1 and n in (1, 2, 3, 8, 9, 10, 0):
                pass
            y = 2.15 - r * 1.15
            ax3.add_patch(Rectangle((x, y), 0.88, 0.95, fc=colmap[v], ec=MUTED, lw=0.6))
            ax3.text(x + 0.44, y + 0.47, v, ha="center", va="center", fontsize=6.5)
    ax3.text(-0.05, 2.62, "HS", fontsize=8, ha="right")
    ax3.text(-0.05, 1.5, "LS", fontsize=8, ha="right")
    ax3.text(5.6, 0.55, "strong: unequal $e_g$ occupation (HS $d^4$, LS $d^7$, $d^9$)\nweak: unequal $t_{2g}$ occupation (lobes point between ligands)\n(for $d^1$–$d^3$, $d^8$–$d^{10}$ and $d^0$ high = low spin: one row only)", fontsize=7.6, ha="center", va="center", color=INK)
    save(fig, "fig_ch10_jt")


# ================================================================== FIG 7  geometry: why Td inverts Oh
def fig_geometry():
    fig = plt.figure(figsize=(12.6, 5.4))
    # octahedron
    for k, (title, ligs, lobes) in enumerate((
        ("octahedral: ligands on the axes", OCT, None),
        ("tetrahedral: ligands on alternate cube corners", TET, None))):
        ax = fig.add_subplot(1, 2, k + 1, projection="3d")
        ax.set_box_aspect((1, 1, 1))
        ax.set_axis_off()
        # cube
        c = np.array(list(itertools.product((-1, 1), repeat=3)), float)
        for a, b in itertools.combinations(range(8), 2):
            if np.sum(np.abs(c[a] - c[b])) == 2:
                ax.plot(*zip(c[a], c[b]), color=GRID, lw=1)
        # axes
        for v, lab in (((1.35, 0, 0), "x"), ((0, 1.35, 0), "y"), ((0, 0, 1.35), "z")):
            ax.plot([-v[0], v[0]], [-v[1], v[1]], [-v[2], v[2]], color=MUTED, lw=0.8)
            ax.text(*(np.array(v) * 1.05), lab, fontsize=9, color=MUTED)
        # lobes
        eg = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]   # face centres (eg)
        t2 = [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0), (1, 0, 1), (1, 0, -1), (-1, 0, 1), (-1, 0, -1), (0, 1, 1), (0, 1, -1), (0, -1, 1), (0, -1, -1)]  # edge midpoints (t2g)
        for v in eg:
            ax.scatter(*np.array(v) * 0.82, s=70, color=ORANGE, alpha=0.9, depthshade=False, edgecolors=INK, linewidths=0.4)
        for v in t2:
            u = np.array(v, float)
            ax.scatter(*(u / np.linalg.norm(u) * 0.82), s=60, color=BLUE, alpha=0.9, depthshade=False, edgecolors=INK, linewidths=0.4)
        # ligands
        L = np.array(ligs, float)
        L = L / np.linalg.norm(L, axis=1, keepdims=True) * 1.15
        ax.scatter(*L.T, s=230, color="#c9d3f0", edgecolors=INK, linewidths=1.0, depthshade=False, zorder=10)
        for p in L:
            ax.plot([0, p[0]], [0, p[1]], [0, p[2]], color=INK, lw=0.9)
        ax.scatter([0], [0], [0], s=90, color=INK)
        ax.set_title(title, fontsize=10)
        ax.view_init(elev=18, azim=-62)
        ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3); ax.set_zlim(-1.3, 1.3)
    fig.text(0.27, 0.06, "orange: $e_g$ lobes (on axes)  ·  blue: $t_{2g}$ lobes (between axes)\nangle lobe–ligand: $e_g$ 0°, $t_{2g}$ 45°  (octahedron)", ha="center", fontsize=9)
    fig.text(0.74, 0.06, "angle lobe–ligand: $t_2$ 35.3° (closer), $e$ 54.7° (farther)\n$\\Rightarrow$ $t_2$ is pushed up, $e$ down: the reverse of $O_h$", ha="center", fontsize=9)
    fig.suptitle("Why the tetrahedral splitting is inverted and smaller", fontsize=12, fontweight="semibold", y=0.97)
    save(fig, "fig_ch10_geometry")


if __name__ == "__main__":
    which = sys.argv[1:] or ["splitting", "spin", "lfse", "thermo", "spectro", "jt", "geometry"]
    for w in which:
        globals()["fig_" + w]()
