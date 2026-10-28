"""QM08 figures: step, barrier, tunnelling, Gamow, double barrier, Kronig-Penney (units hbar^2/2m = 1).
.venv/bin/python -W ignore scripts/fig_qm08.py
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
from qm08_numbers import tmat, barrier_T, HBARC  # noqa

import numpy as np


def profile(E, layers, edges, xs, V_left=0.0):
    """|psi|^2 on xs for unit incident wave from the left through layers (V list) with interfaces at edges."""
    Vs = [V_left] + list(layers) + [V_left]
    ks = [np.sqrt(complex(E - v)) for v in Vs]
    # cumulative matrices
    Ms = [np.eye(2, dtype=complex)]
    for j, x in enumerate(edges):
        k1, k2 = ks[j], ks[j + 1]
        L = np.array([[np.exp(1j * k1 * x), np.exp(-1j * k1 * x)], [1j * k1 * np.exp(1j * k1 * x), -1j * k1 * np.exp(-1j * k1 * x)]])
        R = np.array([[np.exp(1j * k2 * x), np.exp(-1j * k2 * x)], [1j * k2 * np.exp(1j * k2 * x), -1j * k2 * np.exp(-1j * k2 * x)]])
        Ms.append(np.linalg.solve(R, L) @ Ms[-1])
    r = -Ms[-1][1, 0] / Ms[-1][1, 1]
    y = np.zeros(len(xs), complex)
    for i, x in enumerate(xs):
        j = int(np.searchsorted(edges, x))
        A, B = Ms[j] @ np.array([1.0, r])
        y[i] = A * np.exp(1j * ks[j] * x) + B * np.exp(-1j * ks[j] * x)
    return np.abs(y) ** 2


def fig_step_barrier():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    xs = np.linspace(-8, 6, 1400)
    a = ax[0]
    for E, col, lab in ((2.0, BLUE, "$E=2V_0$: partial reflection, ripples"), (0.5, ORANGE, "$E=0.5V_0$: total reflection, evanescent tail")):
        a.plot(xs, profile(E, [1.0], [0.0, 400.0], xs), color=col, lw=2, label=lab)
    a.axvline(0, color=INK, lw=1.2); a.axvspan(0, 6, color=GRID, alpha=0.6)
    a.set_ylim(0, 4.2); a.set_xlabel("$x$ (units $\\hbar/\\sqrt{2mV_0}$)"); a.set_ylabel("$|\\psi|^2$")
    a.legend(fontsize=8, loc="upper left"); a.set_title("A  step potential: $|\\psi|^2$")
    b = ax[1]
    E = np.linspace(1.0001, 6, 400)
    k1, k2 = np.sqrt(E), np.sqrt(E - 1)
    T = 4 * k1 * k2 / (k1 + k2) ** 2
    b.plot(E, T, color=BLUE, lw=2, label="$T=4k_1k_2/(k_1+k_2)^2$")
    b.plot(E, 1 - T, color=ORANGE, lw=2, label="$R=((k_1-k_2)/(k_1+k_2))^2$")
    b.plot([0, 1], [0, 0], color=BLUE, lw=2); b.plot([0, 1], [1, 1], color=ORANGE, lw=2)
    b.axvline(1, color=MUTED, ls=":"); b.set_xlim(0, 6)
    b.set_xlabel("$E/V_0$"); b.set_ylim(-0.02, 1.05); b.legend(fontsize=8, loc="center right")
    b.set_title("B  step: $T$ rises from 0 at $E=V_0$, $R+T=1$")
    c = ax[2]
    En = np.linspace(0.01, 3.0, 3000)
    for L, col in ((1.0, BLUE), (2.0, ORANGE), (4.0, AQUA)):
        c.semilogy(En, [barrier_T(e, 1.0, L) for e in En], color=col, lw=1.8, label=f"$L={L:g}$ (V$_0$=1)")
    c.axvline(1, color=MUTED, ls=":")
    c.set_ylim(1e-6, 1.5); c.set_xlabel("$E/V_0$"); c.set_ylabel("$T$"); c.legend(fontsize=8, loc="lower right")
    c.set_title("C  barrier: $T>0$ below the top (tunnelling), $T=1$ resonances above")
    fig.tight_layout()
    save(fig, "fig_qm08_step_barrier")


def fig_tunnelling():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    a = ax[0]
    xs = np.linspace(-8, 11, 1800)
    E, L = 0.5, 3.0
    y = profile(E, [1.0], [0.0, L], xs)
    a.plot(xs, y, color=BLUE, lw=2)
    a.axvspan(0, L, color=GRID, alpha=0.7)
    a.text(L / 2, 2.6, f"barrier $V_0$\n$T={barrier_T(E,1.0,L):.3f}$", ha="center", fontsize=9)
    a.set_ylim(0, 4.2); a.set_xlabel("$x$"); a.set_ylabel("$|\\psi|^2$")
    a.set_title("A  $E=0.5V_0$, $L=3$: decay inside, flat beyond")
    b = ax[1]
    Ls = np.linspace(0, 8, 400)
    for E, col in ((0.2, BLUE), (0.5, ORANGE), (0.8, AQUA)):
        b.semilogy(Ls, [barrier_T(E, 1.0, l) for l in Ls], color=col, lw=2, label=f"$E/V_0={E}$, slope $-2\\kappa=-{2*math.sqrt(1-E):.2f}$")
    b.set_xlabel("barrier width $L$ ($\\hbar/\\sqrt{2mV_0}$)"); b.set_ylabel("$T$"); b.set_ylim(1e-8, 2)
    b.legend(fontsize=8); b.set_title("B  $\\ln T$ is linear in $L$ with slope $-2\\kappa$")
    c = ax[2]
    # Gamow: U-238 alpha, Coulomb barrier
    E_ = 4.267; Rc = 90 * 2 * 1.439964 / E_; R = 1.2 * (234 ** (1 / 3) + 4 ** (1 / 3))
    r = np.linspace(R, 140, 600)
    V = 90 * 2 * 1.439964 / r
    c.plot(r, V, color=INK, lw=2)
    c.fill_between(r, E_, V, where=V > E_, color=VIOLET, alpha=0.35)
    c.hlines(E_, 0, Rc, color=ORANGE, lw=2)
    c.plot([0, R, R], [-8, -8, 90 * 2 * 1.439964 / R], color=INK, lw=2)
    c.text(0.5 * (R + Rc), E_ + 8, "tunnelled region\n$2G=88$, $e^{-2G}=6\\times10^{-39}$", ha="center", fontsize=8.5)
    c.text(R, -20, f"$R={R:.1f}$ fm", ha="center", fontsize=8.5); c.text(Rc, -20, f"$R_c={Rc:.1f}$ fm", ha="center", fontsize=8.5)
    c.text(2, E_ + 3, "$E_\\alpha=4.27$ MeV", color=ORANGE, fontsize=9)
    c.set_xlim(0, 120); c.set_ylim(-28, 60); c.set_xlabel("$r$ (fm)"); c.set_ylabel("$V(r)$ (MeV)")
    c.set_title("C  $\\alpha$ decay of $^{238}$U: Coulomb barrier")
    fig.tight_layout()
    save(fig, "fig_qm08_tunnelling")


def fig_resonant_bands():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))
    V0, b, w = 1.0, 1.0, 2.0
    layers = [V0, 0.0, V0]; edges = [0.0, b, b + w, 2 * b + w]
    a = ax[0]
    Es = np.linspace(0.01, 0.99, 6000)
    Td = [tmat(e, layers, edges)[0] for e in Es]
    Ts = [barrier_T(e, V0, b) for e in Es]
    a.semilogy(Es, Td, color=BLUE, lw=2, label="double barrier")
    a.semilogy(Es, Ts, color=ORANGE, lw=1.8, ls="--", label="single barrier")
    a.set_ylim(1e-5, 2); a.set_xlabel("$E/V_0$"); a.set_ylabel("$T$"); a.legend(fontsize=8, loc="lower right")
    a.set_title("A  resonant tunnelling: $T=1$ at the quasi-bound level")
    bb = ax[1]
    Er = Es[int(np.argmax(Td))]
    xs = np.linspace(-4, 8, 1800)
    bb.plot(xs, profile(Er, layers, edges, xs), color=BLUE, lw=2, label=f"on resonance $E/V_0={Er:.3f}$")
    bb.plot(xs, profile(0.3, layers, edges, xs), color=ORANGE, lw=1.6, label="off resonance $E/V_0=0.3$")
    for lo, hi in ((0, b), (b + w, 2 * b + w)):
        bb.axvspan(lo, hi, color=GRID, alpha=0.7)
    bb.set_xlabel("$x$"); bb.set_ylabel("$|\\psi|^2$"); bb.legend(fontsize=8, loc="upper right")
    bb.set_title("B  on resonance the well fills up")
    c = ax[2]
    P = 3.0
    y = np.linspace(1e-6, 4 * math.pi, 40000)
    f = np.cos(y) + P * np.sin(y) / y
    ok = np.abs(f) <= 1
    qa = np.arccos(np.clip(f, -1, 1))
    E_ = (y / math.pi) ** 2
    c.plot(qa[ok] / math.pi, E_[ok], ".", ms=1.5, color=BLUE)
    c.plot(-qa[ok] / math.pi, E_[ok], ".", ms=1.5, color=BLUE)
    qq = np.linspace(-1, 1, 200)
    c.plot(qq, qq ** 2, color=ORANGE, lw=1.4, ls="--", label="free particle $E\\propto q^2$")
    c.set_ylim(0, 12); c.set_xlim(-1.05, 1.05)
    c.set_xlabel("$qa/\\pi$ (first Brillouin zone)"); c.set_ylabel("$E/(\\hbar^2\\pi^2/2ma^2)$")
    c.legend(fontsize=8, loc="upper center")
    c.set_title("C  delta comb ($P=3$): bands and gaps")
    fig.tight_layout()
    save(fig, "fig_qm08_resonant_bands")


if __name__ == "__main__":
    fig_step_barrier(); fig_tunnelling(); fig_resonant_bands()
