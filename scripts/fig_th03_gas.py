"""TH03 - adiabatic compression heating and the speed of sound in air."""
from figlib import *

R = 8.314462618; M = 28.97e-3
fig, axes = plt.subplots(1, 3, figsize=(11.8, 3.8))
a = axes[0]
r = np.linspace(1, 20, 200)
for g, c, lab in ((5 / 3, BLUE, r"$\gamma=5/3$ (monatomic)"), (1.4, ORANGE, r"$\gamma=7/5$ (air)"), (4 / 3, AQUA, r"$\gamma=4/3$ (polyatomic)")):
    a.plot(r, 300 * r ** (g - 1), color=c, label=lab)
a.plot([15], [300 * 15 ** 0.4], "o", color=INK, ms=6); a.annotate("ratio 15, air:\n886 K, 44 atm", (15, 886), xytext=(9, 950), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
a.set_xlabel("volume compression ratio $V_1/V_2$"); a.set_ylabel(r"$T_2$ (K) from $T_1=300$ K"); a.legend(fontsize=8.2, loc="upper left")
a.set_title(r"A  $TV^{\gamma-1}$ = const", fontsize=10); a.set_ylim(250, 1500)
b = axes[1]
T = np.linspace(200, 330, 200)
b.plot(T, np.sqrt(1.4 * R * T / M), color=BLUE, label=r"adiabatic: $\sqrt{\gamma RT/M}$")
b.plot(T, np.sqrt(R * T / M), color=ORANGE, ls="--", label=r"isothermal (Newton): $\sqrt{RT/M}$")
b.plot([293.15], [343.2], "o", color=INK, ms=6); b.annotate("343 m/s at 20 °C", (293.15, 343.2), xytext=(222, 360), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.set_xlabel("$T$ (K)"); b.set_ylabel("speed of sound (m/s)"); b.legend(fontsize=8.2, loc="lower right"); b.set_title(r"B  $c=\sqrt{\gamma RT/M}$, factor $\sqrt{\gamma}=1.18$", fontsize=10)
c = axes[2]
f = np.arange(3, 11)
c.plot(f, 1 + 2 / f, "o-", color=BLUE)
for ff, lab, dx, dy in ((3, "monatomic (He, Ar)", 0.35, 0.03), (5, "diatomic (N$_2$, O$_2$)", 0.4, 0.07), (6, "polyatomic", 0.4, 0.07)):
    c.annotate(lab + f": {1 + 2 / ff:.3f}", (ff, 1 + 2 / ff), xytext=(ff + dx, 1 + 2 / ff + dy), fontsize=8.2, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
c.set_xlabel("active degrees of freedom $f$"); c.set_ylabel(r"$\gamma=C_P/C_V=1+2/f$"); c.set_ylim(1.1, 1.9); c.set_title("C  equipartition sets $\\gamma$", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.04, "A: reversible adiabats. B: Laplace's correction to Newton's isothermal estimate. C: $C_V=(f/2)R$, $C_P=C_V+R$ (Mayer). All from scripts/th_numbers.py.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_th03_gas")
