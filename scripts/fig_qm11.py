#!/usr/bin/env python3
"""QM11 figures: Bessel functions and the circular-well spectrum; densities as rings (e^{il theta}) and lobes (cos l theta)."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy.special import jv, jn_zeros
fig = plt.figure(figsize=(12, 7.2))
ax = fig.add_subplot(2, 3, (1, 2)); x = np.linspace(0, 12, 1200)
for l, c in zip(range(4), ["#1f4e79", "#c0392b", "#117a65", "#7d3c98"]):
    ax.plot(x, jv(l, x), color=c, lw=2, label=f"$J_{l}$")
    z = jn_zeros(l, 3); ax.plot(z, 0 * z, "o", color=c, ms=5)
    ax.annotate(f"{z[0]:.3f}", (z[0], 0), (z[0] - 0.3, 0.12 + 0.07 * l), fontsize=8, color=c)
ax.axhline(0, color="0.5", lw=0.8); ax.set_xlabel("$x=ka$"); ax.legend(ncol=4, fontsize=9, frameon=False)
ax.set_title("A. Bessel functions: the allowed $k_{n,l}a$ are the zeros $j_{l,n}$ (dots)", fontsize=10)
ax = fig.add_subplot(2, 3, 3)
for l in range(5):
    for n, j in enumerate(jn_zeros(l, 3), 1):
        E = j * j
        if E < 110: ax.plot([l - 0.35, l + 0.35], [E, E], color="k", lw=2); ax.text(l + 0.38, E, f"{n},{l}" + ("" if l == 0 else " ×2"), fontsize=7, va="center")
ax.set_xticks(range(5)); ax.set_xlabel("$|l|$"); ax.set_ylabel(r"$E\ /\ (\hbar^2/2ma^2)$"); ax.set_title("B. spectrum ($n,l$); $l\\ne0$ doubly degenerate", fontsize=10); ax.set_xlim(-0.6, 5.2)
g = np.linspace(-1, 1, 401); XX, YY = np.meshgrid(g, g); RR, TT = np.hypot(XX, YY), np.arctan2(YY, XX)
for k, (n, l, mode, ttl) in enumerate([(2, 1, "exp", "C. $n=2,l=1$: $|J_1e^{i\\theta}|^2$ (ring)"), (2, 1, "cos", "D. same level, $\\cos\\theta$ form (2 lobes)"), (1, 3, "cos", "E. $n=1,l=3$, $\\cos3\\theta$ (6 lobes)")]):
    j = jn_zeros(l, n)[-1]; P = jv(l, j * RR) ** 2 / (np.pi * jv(l + 1, j) ** 2)
    if mode == "cos": P = P * 2 * np.cos(l * TT) ** 2
    P[RR > 1] = np.nan; a = fig.add_subplot(2, 3, 4 + k); a.imshow(P, extent=[-1, 1, -1, 1], origin="lower", cmap="viridis")
    t = np.linspace(0, 2 * np.pi, 200); a.plot(np.cos(t), np.sin(t), "w", lw=1); a.set_title(ttl, fontsize=9.5); a.set_xticks([]); a.set_yticks([])
fig.tight_layout(); fig.savefig("Assets/figures/fig_qm11_circular_well.png", dpi=140); print("ok")
