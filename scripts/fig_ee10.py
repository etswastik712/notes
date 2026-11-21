#!/usr/bin/env python3
"""EE10 Figure 10.1: directional, stabilizing, disruptive selection acting on a normal trait distribution."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
z = np.linspace(-4, 4, 801); f = np.exp(-z * z / 2) / np.sqrt(2 * np.pi)
modes = {"directional": 1 / (1 + np.exp(-1.6 * (z - 0.3))), "stabilizing": np.exp(-z * z / (2 * 0.8 ** 2)), "disruptive": 1 - 0.95 * np.exp(-z * z / (2 * 0.8 ** 2))}
fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3), sharey=True)
for ax, (name, w) in zip(axs, modes.items()):
    g = f * w; g /= np.trapezoid(g, z)
    m0, m1 = 0.0, np.trapezoid(z * g, z); v1 = np.trapezoid((z - m1) ** 2 * g, z)
    ax.fill_between(z, f, color="0.85", label="before"); ax.plot(z, g, color="#c0392b", lw=2, label="after selection")
    ax.plot(z, 0.42 * w, color="#2471a3", ls="--", lw=1.3, label="fitness w(z) (scaled)")
    ax.set_title(f"{name}\nmean {m0:.2f}→{m1:.2f}, variance 1.00→{v1:.2f}", fontsize=10)
    ax.set_xlabel("trait z (e.g. beak depth, sd units)"); ax.set_yticks([])
axs[0].legend(fontsize=8, frameon=False, loc="upper left")
fig.tight_layout(); fig.savefig("Assets/figures/fig_ee10_selection_modes.png", dpi=150); print("ok")
