#!/usr/bin/env python3
"""Tutorial VI, Problem 2(b): sketch of Re(psi) for the barrier |x|<a, V=V0, with E>V0 (hbar^2/2m = 1, V0 = a = 1).
Solves the four matching equations of part (a) exactly for B, C, D, F (A = 1).
Run from anywhere:  .venv/bin/python scripts/fig_tutorial6.py
Writes Assets/figures/fig_tutorial6_barrier_above.png
"""
import os
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "Assets", "figures"); os.makedirs(OUT, exist_ok=True)
BL, RD, GR, VI, OR, GY = "#1f4e79", "#c0392b", "#117a65", "#7d3c98", "#d35400", "0.5"
V0, a = 1.0, 1.0

def solve(E):
    k0, k = np.sqrt(E), np.sqrt(E - V0)
    M = np.zeros((4, 4), dtype=complex); rhs = np.zeros(4, dtype=complex)
    # unknowns [B, C, D, F]; A = 1.   rows: psi and psi' continuous at x=-a and x=+a
    # x = -a, psi:   e^{-i k0 a} + B e^{+i k0 a} = C e^{-i k a} + D e^{+i k a}
    M[0] = [np.exp(1j * k0 * a), -np.exp(-1j * k * a), -np.exp(1j * k * a), 0]; rhs[0] = -np.exp(-1j * k0 * a)
    # x = -a, psi':  k0 (e^{-i k0 a} - B e^{+i k0 a}) = k (C e^{-i k a} - D e^{+i k a})
    M[1] = [-k0 * np.exp(1j * k0 * a), -k * np.exp(-1j * k * a), k * np.exp(1j * k * a), 0]; rhs[1] = -k0 * np.exp(-1j * k0 * a)
    # x = +a, psi:   C e^{i k a} + D e^{-i k a} = F e^{i k0 a}
    M[2] = [0, np.exp(1j * k * a), np.exp(-1j * k * a), -np.exp(1j * k0 * a)]
    # x = +a, psi':  k (C e^{i k a} - D e^{-i k a}) = k0 F e^{i k0 a}
    M[3] = [0, k * np.exp(1j * k * a), -k * np.exp(-1j * k * a), -k0 * np.exp(1j * k0 * a)]
    B, C, D, F = np.linalg.solve(M, rhs)
    return k0, k, B, C, D, F

def psi(x, E):
    k0, k, B, C, D, F = solve(E)
    return np.where(x < -a, np.exp(1j * k0 * x) + B * np.exp(-1j * k0 * x),
           np.where(x <= a, C * np.exp(1j * k * x) + D * np.exp(-1j * k * x), F * np.exp(1j * k0 * x)))

cases = [(1.001, r"$E\to V_0^+$"), (1.5, r"$E=1.5\,V_0$"), (1 + np.pi**2 / 4, r"$2ka=\pi$: resonance"), (4.0, r"$E=4\,V_0$")]
x = np.linspace(-8, 8, 4000)
fig, axs = plt.subplots(2, 2, figsize=(11.5, 6.6), sharex=True)
for ax, (E, lab) in zip(axs.ravel(), cases):
    k0, k, B, C, D, F = solve(E)
    T = abs(F)**2; R = abs(B)**2
    ps = psi(x, E)
    ax.axvspan(-a, a, color=OR, alpha=0.10)
    ax.plot(x, ps.real, color=BL, lw=2, label=r"Re $\psi$")
    ax.plot(x, np.abs(ps), color=GY, lw=1, ls="--", label=r"$|\psi|$")
    ax.axhline(0, color="0.7", lw=0.8)
    ax.text(0, 2.0, "barrier", color=OR, ha="center", fontsize=8)
    ax.set_ylim(-2.2, 2.3); ax.set_xlim(-8, 8)
    ax.set_title(f"{lab},  $E/V_0={E:.3f}$:  $T={T:.3f}$, $R={R:.3f}$", fontsize=10)
    ax.text(-7.8, -1.95, rf"$k_0={k0:.2f}$, $\lambda_0=2\pi/k_0={2*np.pi/k0:.2f}$", fontsize=8, color=BL)
    ax.text(0, -1.95, rf"$k={k:.2f}$, $\lambda=2\pi/k={2*np.pi/k:.2f}$", fontsize=8, color=OR, ha="center")
    ax.text(7.8, -1.95, rf"$k/k_0={k/k0:.3f}$", fontsize=8, color=GY, ha="right")
    print("E/V0=%.4f: k0=%.4f k=%.4f  T(matching)=%.6f  T(formula)=%.6f  R+T=%.12f  lam_in/lam_out=k0/k=%.3f" %
          (E, k0, k, T, 1 / (1 + V0**2 / (4 * E * (E - V0)) * np.sin(2 * k * a)**2), R + T, k0 / k))
axs[0, 0].legend(frameon=False, fontsize=8, loc="upper left")
for ax in axs[1]: ax.set_xlabel("x / a")
fig.suptitle(r"Tutorial VI Q2(b): $\mathrm{Re}\,\psi$ for the barrier with $E>V_0$ ($A=1$; $k<k_0$, so the wavelength inside is longer)", fontsize=11)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig_tutorial6_barrier_above.png"), dpi=140); plt.close(fig)
print("ok")
