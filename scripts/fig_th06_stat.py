"""TH06 - Maxwell speed distribution, oscillator heat capacity (Einstein) and the Schottky two-level heat capacity."""
from figlib import *
from math import pi
kB = 1.380649e-23; u = 1.66053906660e-27
fig, axes = plt.subplots(1, 3, figsize=(11.8, 3.9))
a = axes[0]
v = np.linspace(0, 2500, 800)
def fv(v, m, T): return 4 * pi * (m / (2 * pi * kB * T)) ** 1.5 * v ** 2 * np.exp(-m * v ** 2 / (2 * kB * T))
for m, T, c, lab in ((28.0134 * u, 300, BLUE, "N$_2$, 300 K"), (28.0134 * u, 600, ORANGE, "N$_2$, 600 K"), (4.0026 * u, 300, AQUA, "He, 300 K")):
    a.plot(v, fv(v, m, T) * 1e3, color=c, label=lab)
m, T = 28.0134 * u, 300
vm, vb, vr = np.sqrt(2 * kB * T / m), np.sqrt(8 * kB * T / (pi * m)), np.sqrt(3 * kB * T / m)
for x, lab, yy in ((vm, "$v_{mp}$ 422", 2.62), (vb, r"$\langle v\rangle$ 476", 2.43), (vr, "$v_{rms}$ 517", 2.24)):
    a.axvline(x, color=BLUE, lw=0.7, ls=":"); a.text(x + 130, yy, lab, fontsize=8.0, color=BLUE, ha="left"); a.plot([x, x + 120], [yy + 0.03, yy + 0.03], color=BLUE, lw=0.5)
a.set_xlabel("speed (m/s)"); a.set_ylabel("$f(v)$ (10$^{-3}$ s/m)"); a.legend(fontsize=8.2, loc="upper right"); a.set_ylim(0, 2.8)
a.set_title("A  Maxwell speed distribution", fontsize=10)
b = axes[1]
x = np.linspace(0.05, 8, 400)
b.plot(x, x ** 2 * np.exp(x) / (np.exp(x) - 1) ** 2, color=BLUE, label=r"oscillator, $C/k_B$")
xs = np.linspace(0.05, 8, 400)
b.plot(xs, 2.0 * 0 + xs ** 2 * np.exp(xs) / (np.exp(xs) + 1) ** 2, color=ORANGE, label=r"two-level, $C/k_B$ ($x=\varepsilon/k_BT$)")
b.axhline(1, color=MUTED, lw=0.7, ls=":"); b.text(7.9, 1.03, "equipartition limit", fontsize=8.0, ha="right", color=MUTED)
b.plot([3.33], [0.4265], "o", color=INK, ms=6); b.annotate("CO$_2$ bend,\n288 K: $x=3.33$", (3.33, 0.4265), xytext=(0.3, 0.12), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.set_xlabel(r"$x=\hbar\omega/k_BT$ or $\varepsilon/k_BT$"); b.set_ylabel(r"$C/k_B$"); b.legend(fontsize=8.2, loc="upper right", bbox_to_anchor=(1.0, 0.86)); b.set_ylim(0, 1.15)
b.set_title("B  modes freeze out at $x\\gg1$", fontsize=10)
c = axes[2]
x = np.linspace(0.02, 12, 400)
n = 1 / (np.exp(x) - 1)
c.semilogy(x, n, color=BLUE, label=r"mean occupation $\langle n\rangle=1/(e^x-1)$")
c.semilogy(x, np.exp(-x), color=ORANGE, ls="--", label=r"Boltzmann $e^{-x}$")
c.semilogy(x, 1 / x, color=MUTED, ls=":", label=r"classical $1/x$")
c.set_xlabel(r"$x=\hbar\omega/k_BT$"); c.set_ylim(1e-5, 60); c.legend(fontsize=8.0, loc="lower left"); c.set_title("C  the Planck factor", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "Computed from the formulas in the chapter (scripts/th_numbers.py): N$_2$: $v_{mp},\\langle v\\rangle,v_{rms}=422,\\ 476,\\ 517$ m/s at 300 K; two-level $C$ peaks at $k_BT=0.417\\varepsilon$ ($C=0.439k_B$).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_th06_stat")
