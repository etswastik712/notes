"""QM10 figures: the finite barrier (lecture convention, barrier on [-a,a]) and Tutorial V.
.venv/bin/python -W ignore scripts/fig_qm10.py     (units hbar^2/2m = 1)
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
from qm10_numbers import solve_barrier, T_barrier, well_bound, double_well_levels  # noqa

import numpy as np
from scipy.linalg import eigh_tridiagonal


def barrier_psi(E, V0, a, xs):
    k, kap = math.sqrt(E), math.sqrt(V0 - E)
    B, C, D, F = solve_barrier(E, V0, a)
    out = np.zeros(len(xs), complex)
    for i, x in enumerate(xs):
        if x < -a:
            out[i] = np.exp(1j * k * x) + B * np.exp(-1j * k * x)
        elif x <= a:
            out[i] = C * np.exp(kap * x) + D * np.exp(-kap * x)
        else:
            out[i] = F * np.exp(1j * k * x)
    return out


def fig_barrier():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    V0, a = 1.0, 1.0
    xs = np.linspace(-9, 7, 1600)
    A = ax[0]
    for E, col in ((0.5, BLUE), (0.2, ORANGE)):
        T = T_barrier(E, V0, a)
        A.plot(xs, np.abs(barrier_psi(E, V0, a, xs)) ** 2, color=col, lw=2, label=f"$E={E}V_0$: $T={T:.3f}$, $R={1-T:.3f}$")
    A.axvspan(-a, a, color=GRID, alpha=0.7)
    A.text(0, 3.6, "barrier\n$V_0$", ha="center", fontsize=9)
    A.set_ylim(0, 4.3); A.set_xlabel("$x$ (units $\\hbar/\\sqrt{2mV_0}$)"); A.set_ylabel("$|\\psi|^2$ (incident $|A|^2=1$)")
    A.legend(fontsize=8, loc="upper left"); A.set_title("A  $E<V_0$: ripples, decay inside, small flat tail")
    B = ax[1]
    En = np.linspace(0.005, 3.0, 3000)
    for aa, col in ((0.5, BLUE), (1.0, ORANGE), (2.0, AQUA)):
        B.semilogy(En, [T_barrier(e, 1.0, aa) for e in En], color=col, lw=1.9, label=f"$2a={2*aa:g}$")
    B.axvline(1, color=MUTED, ls=":")
    B.set_ylim(1e-7, 1.5); B.set_xlabel("$E/V_0$"); B.set_ylabel("$T$"); B.legend(fontsize=8, loc="lower right", title="$V_0=1$ ($\\hbar^2/2m=1$)", title_fontsize=8)
    B.set_title("B  $T(E)$: smooth through $E=V_0$, $T=1$ resonances above")
    C = ax[2]
    aas = np.linspace(0.02, 4, 400)
    for E, col in ((0.2, BLUE), (0.5, ORANGE), (0.8, AQUA)):
        kap = math.sqrt(1 - E)
        C.semilogy(2 * aas, [T_barrier(E, 1.0, x) for x in aas], color=col, lw=2, label=f"$E/V_0={E}$")
        C.semilogy(2 * aas, [16 * E * (1 - E) * math.exp(-4 * kap * x) for x in aas], color=col, lw=1.2, ls="--")
    C.set_ylim(1e-8, 2); C.set_xlabel("barrier width $2a$"); C.set_ylabel("$T$"); C.legend(fontsize=8, loc="lower left")
    C.set_title("C  width: exact (solid) vs $16\\frac{E}{V_0}(1-\\frac{E}{V_0})e^{-4\\kappa a}$ (dashed)")
    fig.tight_layout()
    save(fig, "fig_qm10_barrier")


def dw_psi(V0, w, d, n=2):
    L = d / 2 + w + 6
    N = 6000
    x = np.linspace(-L, L, N)
    h = x[1] - x[0]
    V = np.where((np.abs(x) < d / 2) | (np.abs(x) > d / 2 + w), V0, 0.0)
    diag = 2 / h ** 2 + V
    off = -np.ones(N - 1) / h ** 2
    E, Ψ = eigh_tridiagonal(diag, off, select="i", select_range=(0, n - 1))
    for j in range(n):
        Ψ[:, j] /= math.sqrt(np.trapezoid(Ψ[:, j] ** 2, x))
        if Ψ[np.argmax(np.abs(Ψ[:, j])), j] < 0:
            Ψ[:, j] *= -1
    return x, V, E, Ψ


def well_scatter(Er, V0=1.0, z0=5.0):
    a = z0 / math.sqrt(V0)
    E = Er * V0
    k, k0 = math.sqrt(E - V0), math.sqrt(E)
    M = np.array([
        [np.exp(1j * k * a), -np.exp(-1j * k0 * a), -np.exp(1j * k0 * a), 0],
        [-1j * k * np.exp(1j * k * a), -1j * k0 * np.exp(-1j * k0 * a), 1j * k0 * np.exp(1j * k0 * a), 0],
        [0, np.exp(1j * k0 * a), np.exp(-1j * k0 * a), -np.exp(1j * k * a)],
        [0, 1j * k0 * np.exp(1j * k0 * a), -1j * k0 * np.exp(-1j * k0 * a), -1j * k * np.exp(1j * k * a)],
    ], dtype=complex)
    rhs = np.array([-np.exp(-1j * k * a), -1j * k * np.exp(-1j * k * a), 0, 0], dtype=complex)
    B, C, D, F = np.linalg.solve(M, rhs)
    xs = np.linspace(-3.2 * a, 3.2 * a, 1800)
    ps = np.where(xs < -a, np.exp(1j * k * xs) + B * np.exp(-1j * k * xs), np.where(xs <= a, C * np.exp(1j * k0 * xs) + D * np.exp(-1j * k0 * xs), F * np.exp(1j * k * xs)))
    return a, xs, ps, abs(F) ** 2


def fig_tutorial():
    fig, ax = plt.subplots(2, 3, figsize=(15.5, 8.4))
    # A: three bound states, z0 = 3.3 (a=1, V0 = z0^2)
    A = ax[0, 0]
    z0 = 3.3
    V0 = z0 ** 2
    xs = np.linspace(-3, 3, 1200)
    ev, od = well_bound(z0, "even"), well_bound(z0, "odd")
    states = sorted([(r, "e") for r in ev] + [(r, "o") for r in od])
    for (r, par), col in zip(states, (BLUE, ORANGE, AQUA)):
        kap = math.sqrt(z0 ** 2 - r ** 2)
        ins = np.cos(r * xs) if par == "e" else np.sin(r * xs)
        edge = math.cos(r) if par == "e" else math.sin(r)
        psi = np.where(np.abs(xs) <= 1, ins, np.sign(xs) ** (0 if par == "e" else 1) * edge * np.exp(-kap * (np.abs(xs) - 1)))
        if par == "o":
            psi = np.where(np.abs(xs) <= 1, ins, np.sign(xs) * edge * np.exp(-kap * (np.abs(xs) - 1)))
        norm = math.sqrt(np.trapezoid(psi ** 2, xs))
        E = r ** 2
        A.plot(xs, E + 3.0 * psi / norm, color=col, lw=2, label=f"$E={E/V0:.3f}V_0$, $k_0a={r:.3f}$")
        A.axhline(E, color=col, lw=0.6, ls=":")
    A.plot([-3, -1, -1, 1, 1, 3], [V0, V0, 0, 0, V0, V0], color=INK, lw=1.4)
    A.set_ylim(-1, V0 + 1.5); A.set_xlabel("$x/a$"); A.set_ylabel("$E$ (levels) + $\\psi$"); A.legend(fontsize=8, loc="center right")
    A.set_title("A  Q1: three bound states ($z_0=3.3>\\pi$)")
    # B: double well d << w
    V0d, w = 20.0, 1.0
    for axx, d, ttl in ((ax[0, 1], 0.1, "B  Q2(a): $d\\ll w$ (here $d=0.1w$)"), (ax[0, 2], 3.0, "C  Q2(b): $d\\gg w$ (here $d=3w$)")):
        x, V, E, Ψ = dw_psi(V0d, w, d)
        sc = 6.0
        axx.plot(x, V, color=INK, lw=1.3)
        axx.plot(x, E[0] + sc * Ψ[:, 0], color=BLUE, lw=2.2, label=f"ground state, $E_0={E[0]:.3f}$")
        axx.axhline(E[0], color=BLUE, lw=0.6, ls=":")
        sgn = -1 if Ψ[np.argmax(np.abs(Ψ[:, 1])), 1] < 0 else 1
        if d > 1:
            axx.plot(x, E[1] + sc * Ψ[:, 1], color=ORANGE, lw=1.6, ls="--", label=f"first excited (odd), $E_1={E[1]:.3f}$")
        axx.set_xlim(-(d / 2 + w + 2.5), d / 2 + w + 2.5); axx.set_ylim(-1.5, 12)
        axx.set_xlabel("$x/w$"); axx.set_ylabel("$E$ + $\\psi$ ($V_0=20$, $\\hbar^2/2m=1$)"); axx.legend(fontsize=8, loc="upper center"); axx.set_title(ttl)
    # D: splitting vs d
    D = ax[1, 0]
    ds = np.linspace(0.05, 5.0, 60)
    sp = []
    for d in ds:
        lv = double_well_levels(V0d, w, d)
        sp.append(lv["odd"][0] - lv["even"][0])
    D.semilogy(ds, sp, color=BLUE, lw=2, label="exact $E_1-E_0$")
    kap = math.sqrt(V0d - 4.589981)
    D.semilogy(ds, [sp[-1] * math.exp(-kap * (d - ds[-1])) for d in ds], color=ORANGE, ls="--", lw=1.6, label="$\\propto e^{-\\kappa d}$, $\\kappa=3.93$")
    D.set_xlabel("barrier width $d/w$"); D.set_ylabel("splitting $E_1-E_0$"); D.legend(fontsize=8)
    D.set_title("D  Q2: the splitting falls as $e^{-\\kappa d}$")
    # E, F: scattering
    for axx, Er, ttl in ((ax[1, 1], (2 * math.pi / 5) ** 2, "E  Q3: $T=1$ ($E=1.579V_0$, $2k_0a=4\\pi$)"), (ax[1, 2], 2.0, "F  Q3: $T<1$ ($E=2V_0$)")):
        a, xs, ps, T = well_scatter(Er)
        axx.plot(xs / a, ps.real, color=BLUE, lw=1.6, label="Re $\\psi$")
        axx.plot(xs / a, np.abs(ps) ** 2, color=ORANGE, lw=2, label="$|\\psi|^2$")
        axx.axvspan(-1, 1, color=GRID, alpha=0.6)
        axx.set_xlabel("$x/a$"); axx.set_ylim(-2.1, 3.4); axx.legend(fontsize=8, loc="upper right"); axx.set_title(ttl + f", $T={T:.3f}$")
    fig.tight_layout()
    save(fig, "fig_qm10_tutorial")


if __name__ == "__main__":
    fig_barrier()
    fig_tutorial()
