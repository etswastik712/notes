#!/usr/bin/env python3
"""QM12 figures: hydrogen levels with degeneracies; radial functions; radial probability densities."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, 3, figsize=(12.5, 4.0))
ax = axs[0]
for n in range(1, 6):
    E = -13.6057 / n**2
    for l in range(n): ax.plot([l - 0.35, l + 0.35], [E, E], color="k", lw=2)
    if n <= 3: ax.text(n - 0.3, E - 0.55 if n == 3 else E + 0.25, f"n={n}: {E:.2f} eV, $n^2$={n*n}", fontsize=8)
ax.text(1.2, -0.25, "n = 4, 5, … crowd toward 0 (ionisation)", fontsize=8, color="0.3")
ax.set_xticks(range(5)); ax.set_xticklabels(["s", "p", "d", "f", "g"]); ax.set_ylabel("E (eV)"); ax.set_title("A. $E_n=-13.6\\,\\mathrm{eV}/n^2$, independent of $l$", fontsize=10); ax.set_ylim(-14.5, 0.5)
r = np.linspace(0, 20, 2000)
R = {"1s": 2 * np.exp(-r), "2s": (1 / np.sqrt(2)) * (1 - r / 2) * np.exp(-r / 2), "2p": r * np.exp(-r / 2) / np.sqrt(24),
     "3s": 2 / (3 * np.sqrt(3)) * (1 - 2 * r / 3 + 2 * r * r / 27) * np.exp(-r / 3)}
cols = {"1s": "#1f4e79", "2s": "#c0392b", "2p": "#117a65", "3s": "#7d3c98"}
for k, v in R.items(): axs[1].plot(r, v, color=cols[k], lw=2, label=k); axs[2].plot(r, r * r * v * v, color=cols[k], lw=2, label=k)
axs[1].axhline(0, color="0.5", lw=0.8); axs[1].set_xlim(0, 15); axs[1].set_xlabel("r / a"); axs[1].set_title("B. radial functions $R_{nl}$ ($a^{-3/2}$)", fontsize=10); axs[1].legend(frameon=False)
axs[2].axvline(1, color="#1f4e79", ls=":", lw=1); axs[2].text(1.1, 0.5, "1s peak at r = a", color="#1f4e79", fontsize=8.5)
axs[2].set_xlim(0, 20); axs[2].set_xlabel("r / a"); axs[2].set_title("C. radial probability $P(r)=r^2R^2$", fontsize=10); axs[2].legend(frameon=False)
fig.tight_layout(); fig.savefig("Assets/figures/fig_qm12_hydrogen.png", dpi=140); print("ok")
