"""QM07 figures: finite square well (lecture convention: V=0 inside |x|<a, V0 outside, E from the floor).

.venv/bin/python -W ignore scripts/fig_qm07.py
Makes fig_qm07_well, fig_qm07_graphical, fig_qm07_wavefunctions, fig_qm07_tutorial4, fig_qm07_scattering, fig_qm07_limits.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
from qm07_numbers import states, p_out  # noqa

import numpy as np
from matplotlib.patches import Rectangle

PI = math.pi
COL = [BLUE, ORANGE, AQUA, VIOLET, RED]


def psi(par, z, z0, x):
    """Normalised wavefunction (a=1) in lecture convention; x array."""
    ka = math.sqrt(z0 * z0 - z * z)
    if par == "even":
        A = math.cos(z) * math.exp(ka)
        f_in = lambda t: np.cos(z * t)
        norm = 1 + math.sin(2 * z) / (2 * z) + math.cos(z) ** 2 / ka
        sgn_out = 1.0
    else:
        A = math.sin(z) * math.exp(ka)
        f_in = lambda t: np.sin(z * t)
        norm = 1 - math.sin(2 * z) / (2 * z) + math.sin(z) ** 2 / ka
        sgn_out = 1.0
    N = 1 / math.sqrt(norm)
    y = np.where(np.abs(x) <= 1, f_in(x), 0.0)
    out = np.abs(x) > 1
    tail = A * np.exp(-ka * np.abs(x))
    if par == "even":
        y = np.where(out, tail, y)
    else:
        y = np.where(out, np.sign(x) * tail, y)
    return N * y


def fig_well():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.4))
    # A: potential
    a = ax[0]
    xs = np.linspace(-3, 3, 600)
    V = np.where(np.abs(xs) < 1, 0, 1.0)
    a.plot(xs, V, color=INK, lw=2.5)
    a.fill_between(xs, 0, V, where=np.abs(xs) >= 1, color=GRID, alpha=0.8)
    a.axvline(-1, color=MUTED, lw=0.8, ls=":")
    a.axvline(1, color=MUTED, lw=0.8, ls=":")
    for xx, t in ((-2.1, "I\n$V=V_0$"), (0, "II\n$V=0$"), (2.1, "III\n$V=V_0$")):
        a.text(xx, 0.45 if xx == 0 else 1.12, t, ha="center", va="center", fontsize=10)
    a.annotate("", (0.0, 1.0), (0.0, 0.02), arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.6))
    a.text(0.08, 0.72, "$V_0$", color=ORANGE, fontsize=11)
    a.set_xticks([-1, 0, 1]); a.set_xticklabels(["$-a$", "0", "$a$"])
    a.set_ylim(-0.1, 1.45); a.set_yticks([0, 1]); a.set_yticklabels(["0", "$V_0$"])
    a.set_title("A  the well (lecture: floor at zero)")
    a.grid(False)
    a.text(0, -0.03, "width $2a$", ha="center", va="top", fontsize=9, color=MUTED)

    # B: regimes
    b = ax[1]
    b.plot(xs, V, color=INK, lw=2)
    b.axhspan(1, 1.45, color=ORANGE, alpha=0.10)
    b.text(2.6, 1.28, "$E>V_0$: free outside\ncontinuum, $T(E)$", ha="right", fontsize=9)
    for (par, z) in states(3.0):
        E = (z / 3.0) ** 2
        b.hlines(E, -3, 3, color=BLUE, lw=1.2)
        b.text(-2.95, E + 0.025, f"{par}  $E/V_0={E:.2f}$", fontsize=8.5, color=BLUE)
    b.text(0, 0.9, "bound: $0<E<V_0$\n(discrete, $z_0=3$)", ha="center", fontsize=9, color=BLUE)
    b.text(0, -0.08, "$E<0$: no solutions", ha="center", fontsize=9, color=RED)
    b.set_ylim(-0.15, 1.45); b.set_yticks([0, 1]); b.set_yticklabels(["0", "$V_0$"])
    b.set_xticks([]); b.grid(False)
    b.set_title("B  three energy regimes")

    # C: turning points and tails
    c = ax[2]
    z0 = 4.0
    par, z = states(z0)[0]
    xx = np.linspace(-3, 3, 800)
    y = psi(par, z, z0, xx)
    E = (z / z0) ** 2
    c.plot(xx, np.where(np.abs(xx) < 1, 0, 1.0), color=INK, lw=2)
    c.axhline(E, color=MUTED, ls="--", lw=0.8)
    c.plot(xx, E + 0.35 * y, color=BLUE, lw=2.2)
    ka = math.sqrt(z0 * z0 - z * z)
    c.annotate("", (1 + 1 / ka, E + 0.02), (1, E + 0.02), arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.6))
    c.text(1 + 0.5 / ka, E - 0.09, "$d_{pen}=1/\\kappa$", color=ORANGE, ha="center", fontsize=9)
    c.text(-2.95, E + 0.03, "$E$", color=MUTED)
    c.text(0, 0.85, "classical turning\npoints at $x=\\pm a$", ha="center", fontsize=9)
    c.set_xticks([-1, 0, 1]); c.set_xticklabels(["$-a$", "0", "$a$"]); c.set_yticks([])
    c.set_ylim(-0.1, 1.2); c.grid(False)
    c.set_title("C  ground state leaks past the turning points")
    fig.suptitle("QM07 · the finite square well: potential, regimes, penetration", y=1.02, fontsize=11)
    fig.tight_layout()
    save(fig, "fig_qm07_well")


def fig_graphical():
    fig, ax = plt.subplots(1, 4, figsize=(20, 4.8))
    for k, z0 in ((0, 3.0), (1, 7.0)):
        a = ax[k]
        zs = np.linspace(1e-3, z0 * 0.9999, 4000)
        circ = np.sqrt(np.clip(z0 ** 2 - zs ** 2, 0, None))
        ev = zs * np.tan(zs)
        od = -zs / np.tan(zs)
        ev[np.abs(ev) > 3 * z0] = np.nan
        od[np.abs(od) > 3 * z0] = np.nan
        a.plot(zs, ev, color=BLUE, lw=1.8, label="$z\\tan z$ (even)")
        a.plot(zs, od, color=ORANGE, lw=1.8, label="$-z\\cot z$ (odd)")
        zz = np.linspace(0, z0, 400)
        a.plot(zz, np.sqrt(z0 ** 2 - zz ** 2), color=INK, lw=2, ls="--", label=f"$\\sqrt{{z_0^2-z^2}}$, $z_0={z0:g}$")
        for par, z in states(z0):
            a.plot([z], [math.sqrt(z0 ** 2 - z ** 2)], "o", color=BLUE if par == "even" else ORANGE, ms=8, zorder=5)
        a.set_ylim(0, z0 * 1.15); a.set_xlim(0, z0 * 1.02)
        a.set_xticks([m * PI / 2 for m in range(1, int(2 * z0 / PI) + 1)])
        a.set_xticklabels([f"${m}\\pi/2$" if m > 1 else "$\\pi/2$" for m in range(1, int(2 * z0 / PI) + 1)], fontsize=8)
        a.set_xlabel("$z=k_0a$"); a.legend(loc="upper right", fontsize=8)
        a.set_title(("A" if k == 0 else "B") + f"  graphical solution, $z_0={z0:g}$: {len(states(z0))} bound states")
    # C: levels vs z0
    c = ax[2]
    z0s = np.linspace(0.05, 14, 700)
    series = {}
    for z0 in z0s:
        for i, (par, z) in enumerate(states(z0)):
            series.setdefault(i, []).append((z0, (z / z0) ** 2, par))
    for i, pts in series.items():
        xs_ = [p[0] for p in pts]; ys = [p[1] for p in pts]
        c.plot(xs_, ys, color=COL[i % 2] if False else (BLUE if pts[0][2] == "even" else ORANGE), lw=1.6)
    for m in range(1, 9):
        c.axvline(m * PI / 2, color=GRID, lw=0.7)
    c.set_xlabel("$z_0=a\\sqrt{2mV_0}/\\hbar$ (well strength)"); c.set_ylabel("$E_n/V_0$ (from the floor)")
    c.set_title("C  levels vs $z_0$: one more state at each $m\\pi/2$")
    c.set_ylim(0, 1.02)
    # D: wavefunctions for z0 = 4 pi
    d = ax[3]
    z0 = 4 * PI
    xx = np.linspace(-2.2, 2.2, 1200)
    for i, (par, z) in enumerate(states(z0)[:4]):
        E = (z / z0) ** 2
        d.plot(xx, E + 0.07 * psi(par, z, z0, xx) / 1.0, color=COL[i], lw=1.8)
        d.hlines(E, -2.2, 2.2, color=COL[i], lw=0.5, ls=":")
    d.axvline(-1, color=MUTED, ls=":"); d.axvline(1, color=MUTED, ls=":")
    d.set_xlabel("$x/a$"); d.set_ylabel("$E/V_0$ with $\\psi_n$ drawn on each level")
    d.set_title("D  first four states, $z_0=4\\pi$")
    fig.tight_layout()
    save(fig, "fig_qm07_graphical")


def fig_wavefunctions():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    z0 = 5.0
    xx = np.linspace(-2.6, 2.6, 1500)
    a = ax[0]
    for i, (par, z) in enumerate(states(z0)[:3]):
        a.plot(xx, psi(par, z, z0, xx), color=COL[i], lw=2, label=f"$\\psi_{i+1}$ ({par})")
        # box state of width 2a: sin(n pi (x+1)/2)
        n = i + 1
        xb = np.linspace(-1, 1, 400)
        a.plot(xb, math.sin(n * PI / 2) * 0 + np.sin(n * PI * (xb + 1) / 2) / math.sqrt(1.0), color=COL[i], lw=1, ls="--")
    a.axvspan(-2.6, -1, color=GRID, alpha=0.6); a.axvspan(1, 2.6, color=GRID, alpha=0.6)
    a.set_xlabel("$x/a$"); a.set_ylabel("$\\psi\\sqrt{a}$")
    a.set_title("A  $\\psi_{1,2,3}$ ($z_0=5$) vs rigid-box states (dashed)")
    a.legend(fontsize=8, loc="upper right")
    b = ax[1]
    par, z = states(z0)[0]
    y2 = psi(par, z, z0, xx) ** 2
    b.plot(xx, y2, color=BLUE, lw=2)
    b.fill_between(xx, 0, y2, where=np.abs(xx) > 1, color=VIOLET, alpha=0.55)
    b.fill_between(xx, 0, y2, where=np.abs(xx) <= 1, color=BLUE, alpha=0.12)
    b.set_title(f"B  $|\\psi_1|^2$: shaded forbidden area = {100*p_out(par,z,z0):.2f}%")
    b.set_xlabel("$x/a$"); b.set_ylabel("$a|\\psi|^2$")
    c = ax[2]
    z0s = np.linspace(0.05, 12, 600)
    P = [100 * p_out(*states(z0_)[0], z0_) if False else 100 * p_out(states(z0_)[0][0], states(z0_)[0][1], z0_) for z0_ in z0s]
    c.plot(z0s, P, color=BLUE, lw=2, label="ground state")
    P2 = []; Z2 = []
    for z0_ in z0s:
        st = states(z0_)
        if len(st) > 1:
            Z2.append(z0_); P2.append(100 * p_out(st[1][0], st[1][1], z0_))
    c.plot(Z2, P2, color=ORANGE, lw=2, label="first excited")
    c.set_yscale("log"); c.set_ylim(0.05, 110)
    c.set_xlabel("$z_0$"); c.set_ylabel("probability outside $|x|>a$ (%)")
    c.set_title("C  leakage falls as the well gets stronger")
    c.legend(fontsize=8)
    fig.tight_layout()
    save(fig, "fig_qm07_wavefunctions")


def fig_tutorial4():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    z0 = 5.0
    zs = np.linspace(1e-3, z0 * 0.99999, 5000)
    f = np.sqrt(z0 ** 2 / zs ** 2 - 1)
    a = ax[0]
    t = np.tan(zs); t[np.abs(t) > 12] = np.nan
    c_ = -1 / np.tan(zs); c_[np.abs(c_) > 12] = np.nan
    a.plot(zs, t, color=BLUE, lw=1.6, label="$\\tan(k_0a)$ (even)")
    a.plot(zs, c_, color=ORANGE, lw=1.6, label="$-\\cot(k_0a)$ (odd)")
    a.plot(zs, f, color=INK, lw=2.3, label="$\\kappa/k_0=\\sqrt{z_0^2/z^2-1}$")
    for par, z in states(z0):
        a.plot([z], [math.sqrt(z0 ** 2 / z ** 2 - 1)], "o", ms=8, color=BLUE if par == "even" else ORANGE, zorder=5)
    a.axvline(z0, color=MUTED, ls=":"); a.text(z0 - 0.05, 8, "$k_0a=z_0$\n($E=V_0$)", ha="right", fontsize=8)
    a.set_ylim(0, 10); a.set_xlim(0, z0 * 1.05)
    a.set_xlabel("$k_0a$"); a.legend(fontsize=8, loc="upper center")
    a.set_title("A  the lecture's graph, with the exact $\\kappa/k_0$")
    u = np.linspace(0.01, 0.9999, 2000)
    b = ax[1]
    b.plot(u, np.sqrt(1 / u ** 2 - 1), color=INK, lw=2.3)
    b.axvline(math.sqrt(2 / 3), color=RED, ls="--", lw=1)
    b.text(math.sqrt(2 / 3) + 0.01, 3.2, "inflection\n$u=\\sqrt{2/3}=0.816$", color=RED, fontsize=8.5)
    b.text(0.04, 7.5, "pole $\\sim 1/u$", fontsize=9)
    b.text(0.62, 0.3, "vertical tangent at $u=1$\n$\\kappa/k_0\\approx\\sqrt{2(1-u)}$", fontsize=8.5)
    b.set_ylim(0, 8); b.set_xlim(0, 1.02)
    b.set_xlabel("$u=k_0a/z_0=\\sqrt{E/V_0}$")
    b.set_title("B  universal shape (same curve for every well)")
    c = ax[2]
    uu = np.linspace(0.05, 0.995, 800)
    fp = -1 / (uu ** 2 * np.sqrt(1 - uu ** 2))
    fpp = (2 - 3 * uu ** 2) / (uu ** 3 * (1 - uu ** 2) ** 1.5)
    c.plot(uu, fp, color=BLUE, lw=2, label="$f'(u)$: always negative")
    c.plot(uu, fpp, color=ORANGE, lw=2, label="$f''(u)$: + then − after 0.816")
    c.axhline(0, color=INK, lw=0.8); c.axvline(math.sqrt(2 / 3), color=RED, ls="--", lw=1)
    c.set_ylim(-12, 12); c.set_xlabel("$u$"); c.legend(fontsize=8, loc="lower left")
    c.set_title("C  derivatives: decreasing, convex then concave")
    fig.tight_layout()
    save(fig, "fig_qm07_tutorial4")


def Tfun(E, z0):  # E in units of V0
    z = z0 * np.sqrt(E)
    return 1 / (1 + 1 / (4 * E * (E - 1)) * np.sin(2 * z) ** 2)


def fig_scattering():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    a = ax[0]
    E = np.linspace(1.001, 6, 6000)
    for z0, col in ((2.0, BLUE), (5.0, ORANGE), (10.0, AQUA)):
        a.plot(E, Tfun(E, z0), color=col, lw=1.6, label=f"$z_0={z0:g}$")
    a.set_xlabel("$E/V_0$"); a.set_ylabel("transmission $T$"); a.set_ylim(0, 1.05)
    a.axvline(1, color=MUTED, ls=":")
    a.set_title("A  $T(E)$: 0 at threshold, $T=1$ at resonances")
    a.legend(fontsize=8, loc="lower right")
    # B: standing waves at resonance vs off
    b = ax[1]
    z0 = 5.0
    Er = (4 * PI / 2 / z0) ** 2   # n=4: k0 a = 2 pi
    Eoff = (2 * PI + PI / 4) ** 2 / z0 ** 2   # sin^2(2 k0 a)=1
    for E_, col, lab in ((Er, BLUE, f"resonance $E/V_0={Er:.3f}$: $T=1$"), (Eoff, ORANGE, f"anti-resonance $E/V_0={Eoff:.3f}$: $T={Tfun(Eoff,z0):.2f}$")):
        # solve matching numerically (units a=1, V0 given by z0: V0 = z0^2/2)
        V0 = z0 ** 2 / 2
        En = E_ * V0
        k = math.sqrt(2 * (En - V0)); k0 = math.sqrt(2 * En)
        M = np.array([
            [np.exp(1j * k), -np.exp(-1j * k0), -np.exp(1j * k0), 0],
            [-1j * k * np.exp(1j * k), -1j * k0 * np.exp(-1j * k0), 1j * k0 * np.exp(1j * k0), 0],
            [0, np.exp(1j * k0), np.exp(-1j * k0), -np.exp(1j * k)],
            [0, 1j * k0 * np.exp(1j * k0), -1j * k0 * np.exp(-1j * k0), -1j * k * np.exp(1j * k)]], complex)
        rhs = np.array([-np.exp(-1j * k), -1j * k * np.exp(-1j * k), 0, 0], complex)
        B, C, D, F = np.linalg.solve(M, rhs)
        xx = np.linspace(-4, 4, 1600)
        Psi = np.where(xx < -1, np.exp(1j * k * xx) + B * np.exp(-1j * k * xx),
                       np.where(xx <= 1, C * np.exp(1j * k0 * xx) + D * np.exp(-1j * k0 * xx), F * np.exp(1j * k * xx)))
        b.plot(xx, np.abs(Psi) ** 2, color=col, lw=2, label=lab)
    b.axvline(-1, color=MUTED, ls=":"); b.axvline(1, color=MUTED, ls=":")
    b.set_xlabel("$x/a$"); b.set_ylabel("$|\\psi|^2$ (incident amplitude 1)")
    b.set_title("B  resonance: no reflected ripple")
    b.legend(fontsize=8, loc="upper right")
    # C: unified ladder: box levels vs bound/resonance
    c = ax[2]
    z0 = 5.0
    ns = np.arange(1, 9)
    box = (ns * PI / 2 / z0) ** 2
    st = states(z0)
    for n, e in zip(ns, box):
        if e > 1.85:
            continue
        c.hlines(e, 0.05, 0.45, color=MUTED, lw=2)
        c.text(0.02, e, f"{n}", ha="right", va="center", fontsize=8, color=MUTED)
    for i, (par, z) in enumerate(st):
        e = (z / z0) ** 2
        c.hlines(e, 0.55, 0.95, color=BLUE if par == "even" else ORANGE, lw=2.5)
        c.plot([0.45, 0.55], [box[i], e], color=GRID, lw=1)
    for n, e in zip(ns, box):
        if 1 < e <= 1.85:
            c.hlines(e, 0.55, 0.95, color=AQUA, lw=2.5, ls=(0, (2, 1)))
    c.axhline(1, color=ORANGE, ls="--"); c.text(0.5, 1.03, "$E=V_0$ (top of the well)", ha="center", fontsize=8.5, color=ORANGE)
    c.text(0.25, -0.08, "rigid box $2a$", ha="center", fontsize=9); c.text(0.75, -0.08, "finite well", ha="center", fontsize=9)
    c.text(0.75, 1.72, "dashed: $T=1$ resonances at the\nunshifted box energies ($E>V_0$)", ha="center", fontsize=8, color=AQUA)
    c.text(0.75, 0.80, "solid: bound states,\nshifted below the box levels", ha="center", fontsize=8, color=BLUE)
    c.set_xlim(0, 1); c.set_xticks([]); c.set_ylim(-0.12, 1.9)
    c.set_ylabel("$E/V_0$")
    c.set_title("C  bound states below, resonances above")
    c.grid(False)
    fig.tight_layout()
    save(fig, "fig_qm07_scattering")


def fig_limits():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.5))
    z0s = np.linspace(2, 60, 500)
    a = ax[0]
    for n, col in ((1, BLUE), (2, ORANGE), (3, AQUA)):
        r = []; xs_ = []
        for z0 in z0s:
            st = states(z0)
            if len(st) >= n:
                r.append((st[n - 1][1] / (n * PI / 2)) ** 2); xs_.append(z0)
        a.plot(xs_, r, color=col, lw=2, label=f"$n={n}$")
    a.plot(z0s, 1 - 2 / z0s, color=INK, ls="--", lw=1.2, label="$1-2/z_0$")
    a.set_xlabel("$z_0$"); a.set_ylabel("$E_n/E_n^{\\rm box}$"); a.set_ylim(0, 1.02)
    a.set_title("A  deep wide well → rigid box from below")
    a.legend(fontsize=8)
    b = ax[1]
    z0w = np.linspace(0.02, 1.2, 300)
    ka = [math.sqrt(z * z - states(z)[0][1] ** 2) for z in z0w]
    b.plot(z0w, ka, color=BLUE, lw=2, label="exact $\\kappa a$")
    b.plot(z0w, z0w ** 2, color=ORANGE, ls="--", lw=1.6, label="$z_0^2$ (shallow well)")
    b.set_xlabel("$z_0$"); b.set_ylabel("$\\kappa a$")
    b.set_title("B  shallow well: $\\kappa=m\\alpha/\\hbar^2$, $\\alpha=2V_0a$")
    b.legend(fontsize=8)
    c = ax[2]
    # delta limit: fixed alpha, a -> 0: E/(m alpha^2/2hbar^2) -> 1 ; in units hbar=m=1, alpha=1
    al = 1.0
    aa = np.logspace(-3, 0.5, 300)
    ratio = []
    for a_ in aa:
        V0 = al / (2 * a_)
        z0 = a_ * math.sqrt(2 * V0)
        z1 = states(z0)[0][1]
        k = math.sqrt(z0 * z0 - z1 * z1) / a_
        ratio.append(k * k / (2 * (al ** 2 / 2)))  # |E| / (alpha^2/2) with hbar=m=1  => kappa^2/2 / (alpha^2/2)
    c.semilogx(aa, ratio, color=BLUE, lw=2)
    c.axhline(1, color=ORANGE, ls="--"); c.set_xlabel("half-width $a$ (fixed $\\alpha=2V_0a$)")
    c.set_ylabel("$|E|\\,/\\,(m\\alpha^2/2\\hbar^2)$")
    c.set_title("C  delta-function limit: $|E|\\to m\\alpha^2/2\\hbar^2$")
    fig.tight_layout()
    save(fig, "fig_qm07_limits")


if __name__ == "__main__":
    fig_well(); fig_graphical(); fig_wavefunctions(); fig_tutorial4(); fig_scattering(); fig_limits()
