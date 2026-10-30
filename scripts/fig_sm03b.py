"""SM03 (deepening) - Brillouin and Langevin magnetisation, Einstein solid and Dulong-Petit, quantum oscillator energy."""
from figlib import *
from math import log, sqrt

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.0))
muB = 9.2740100783e-24; kB = 1.380649e-23
def brill(J, y): a_ = (2 * J + 1) / (2 * J); b_ = 1 / (2 * J); return a_ / np.tanh(a_ * y) - b_ / np.tanh(b_ * y)
a = axes[0]
y = np.linspace(0.02, 14, 600)
a.plot(y, np.tanh(y), color=BLUE, label=r"$J=\frac{1}{2}$: $\tanh y$")
a.plot(y, brill(1.0, y), color=AQUA, label="$J=1$")
a.plot(y, brill(3.5, y), color=ORANGE, label="$J=7/2$ (Gd$^{3+}$)")
a.plot(y, 1 / np.tanh(y) - 1 / y, color=INK, ls="--", lw=1.3, label=r"$J\to\infty$: Langevin $\coth y-1/y$")
yg = 2 * 3.5 * muB * 5 / (kB * 2.0)
a.plot([yg], [brill(3.5, yg)], "o", color=ORANGE, ms=6); a.annotate("Gd$^{3+}$, 5 T, 2 K:\n$y=11.8$, $M/M_s=0.990$\n(Langevin 0.915)", (yg, brill(3.5, yg)), xytext=(5.5, 0.28), fontsize=8.0, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
a.set_xlabel(r"$y=gJ\mu_BB/k_BT$"); a.set_ylabel(r"$M/M_{\rm sat}$"); a.legend(fontsize=8.0, loc="lower right"); a.set_ylim(0, 1.05)
a.set_title("A  Brillouin functions interpolate $\\tanh$ and Langevin", fontsize=10)
b = axes[1]
tt = np.linspace(0.02, 3, 400)
cE = lambda x: x ** 2 * np.exp(x) / (np.exp(x) - 1) ** 2
b.plot(tt, cE(1 / tt), color=BLUE, label="Einstein solid")
b.axhline(1, color=INK, lw=0.9, ls="--"); b.text(2.95, 1.025, "Dulong–Petit $3Nk_B=24.94$ J mol$^{-1}$K$^{-1}$", ha="right", fontsize=8.0)
b.plot([298.15 / 1300], [cE(1300 / 298.15)], "o", color=ORANGE, ms=6)
b.annotate("diamond, 298 K: $\\theta_E\\approx1300$ K (fit)\n$C=6.2$ vs 6.1 measured", (298.15 / 1300, cE(1300 / 298.15)), xytext=(0.6, 0.3), fontsize=8.0, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
b.set_xlabel(r"$T/\theta_E$"); b.set_ylabel(r"$C/3Nk_B$"); b.set_ylim(0, 1.15)
b.set_title("B  equipartition fails when $k_BT<\\hbar\\omega$", fontsize=10)
c = axes[2]
x = np.linspace(0.02, 8, 400)
c.plot(x, x / 2 / np.tanh(x / 2), color=BLUE, label=r"quantum $\langle E\rangle/k_BT=\frac{x}{2}\coth\frac{x}{2}$")
c.plot(x, np.ones_like(x), color=INK, ls="--", lw=1.2, label="classical: 1 (equipartition)")
c.plot(x, x / 2, color=MUTED, ls=":", lw=1.2, label="zero-point $x/2$")
c.set_xlabel(r"$x=\hbar\omega/k_BT$"); c.set_ylabel(r"$\langle E\rangle/k_BT$"); c.set_ylim(0, 4.2); c.legend(fontsize=8.0, loc="upper left")
c.set_title("C  quantum oscillator vs equipartition", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "Computed in scripts/sm_deepen_numbers.py: $C/3Nk_B=0.0045\\,(T=0.1\\theta_E),\\ 0.171\\,(0.2),\\ 0.426\\,(0.3),\\ 0.724\\,(0.5),\\ 0.921\\,(1),\\ 0.979\\,(2)$; $z_q/z_c=1-x^2/24+\\dots$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_sm03b_response")
