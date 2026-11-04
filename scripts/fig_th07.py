"""TH07 figure: Hess cycle, Kirchhoff, bomb-calorimeter curve (illustrative), Delta n_g RT."""
from figlib import *
R = 8.314462618
fig, axes = plt.subplots(2, 2, figsize=(10.4, 7.8))

# A  Hess cycle MgCl2
a = axes[0, 0]
lev = {"MgCl$_2$(s)": 0.0, "Mg$^{2+}$(aq) + 2Cl$^-$(aq)": -155.0, "Mg$^{2+}$(g) + 2Cl$^-$(g)": 2526.0, "Mg$^{2+}$(aq) + 2Cl$^-$(g)": 2526 - 1919.0}
a.hlines(list(lev.values()), [0.3, 2.3, 0.3, 1.3], [1.7, 3.7, 1.7, 2.7], color=INK, lw=2)
a.text(1.0, 120, "MgCl$_2$(s)", ha="center", fontsize=9); a.text(3.0, -330, "Mg$^{2+}$(aq) + 2Cl$^-$(aq)", ha="center", fontsize=9)
a.text(1.0, 2526 + 110, "Mg$^{2+}$(g) + 2Cl$^-$(g)", ha="center", fontsize=9); a.text(2.0, 607 + 120, "Mg$^{2+}$(aq) + 2Cl$^-$(g)", ha="center", fontsize=9)
def arr(x, y0, y1, col, txt, dx=0.06, ha="left", ty=None):
    a.annotate("", xy=(x, y1), xytext=(x, y0), arrowprops=dict(arrowstyle="-|>", color=col, lw=1.6))
    a.text(x + dx, (y0 + y1) / 2 if ty is None else ty, txt, color=col, fontsize=8.6, va="center", ha=ha)
arr(0.55, 0, 2526, ORANGE, "lattice\ndissociation\n+2526", dx=0.07)
arr(1.5, 2526, 607, BLUE, "hydration of Mg$^{2+}$\n$x=-1919$", dx=0.07)
arr(2.5, 607, -155, BLUE, "hydration of\n2Cl$^-$: $2(-381)$\n$=-762$", dx=0.07)
arr(3.62, 0, -155, AQUA, "solution\n$-155$", dx=0.08, ha="left", ty=360)
a.set_xlim(0, 4.3); a.set_ylim(-600, 2900); a.set_xticks([]); a.set_ylabel("enthalpy / kJ mol$^{-1}$")
a.set_title("A  Hess's law: a closed cycle for MgCl$_2$ (Tutorial 2, Q3)", fontsize=10)

# B  Kirchhoff
b = axes[0, 1]
T = np.linspace(298.15, 420, 100)
for dCp, col, lab in ((25.0, ORANGE, "HCl formation, $\\Delta C_p=+25$"), (15.85, BLUE, "C + H$_2$O(g) $\\to$ CO + H$_2$, $+15.85$"), (0.0, MUTED, "$\\Delta C_p=0$"), (-5.48, AQUA, "N$_2$ + 3H$_2$ $\\to$ 2NH$_3$, $-5.48$")):
    b.plot(T, dCp * (T - 298.15) / 1000, color=col, label=lab)
b.plot([350], [1.3], "o", color=ORANGE); b.annotate("350 K: $+1.30$ kJ", (350, 1.3), (371, 2.35), fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED))
b.plot([378], [15.85 * 79.85 / 1000], "o", color=BLUE); b.annotate("378 K: $+1.27$ kJ", (378, 1.265), (383, 0.15), fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED))
b.set_xlabel("$T$ / K"); b.set_ylabel(r"$\Delta H(T)-\Delta H(298\ \mathrm{K})$ / kJ mol$^{-1}$"); b.legend(fontsize=8, loc="upper left", framealpha=0.9)
b.set_title("B  Kirchhoff: the slope of $\\Delta H(T)$ is $\\Delta C_p$", fontsize=10)

# C  bomb calorimeter: illustrative heating curve with the standard extrapolation
c = axes[1, 0]
t = np.linspace(0, 30, 900)
T0 = 25.000; ign = 8.0; dT_true = 1.50; k = 0.045; drift_pre = 0.002; Tj = 25.02
pre = lambda tt: T0 + drift_pre * tt
Tpeak_ideal = pre(ign) + dT_true
post = lambda tt: Tj + (Tpeak_ideal - Tj) * np.exp(-k * (tt - ign))
rise = 1 - np.exp(-(t - ign) / 0.8)
Tfun = np.where(t < ign, pre(t), pre(ign) + (post(t) - pre(ign)) * np.clip(rise, 0, 1))
c.plot(t, Tfun, color=BLUE, lw=2)
c.plot(t[t >= 0], pre(t), color=MUTED, ls="--", lw=1)
tt = np.linspace(ign - 0.0, 30, 100); c.plot(tt, post(tt), color=MUTED, ls="--", lw=1)
c.plot([ign, ign], [pre(ign), post(ign)], color=ORANGE, lw=2.2)
c.axvline(ign, color=MUTED, lw=0.8, ls=":")
c.text(0.3, 26.45, "corrected $\\Delta T=1.50$ K:\nextrapolate both straight\nstretches to the ignition time", color=ORANGE, ha="left", fontsize=8.4, va="center")
c.text(ign + 0.4, 24.97, "ignition", fontsize=8.5, color=MUTED)
c.text(11, 25.28, "$q=C\\Delta T=10.0\\times1.50=15.0$ kJ\n$\\Delta_cU=-q/n=-3.66\\times10^3$ kJ mol$^{-1}$", fontsize=8.8, color=INK)
c.set_xlabel("time / min"); c.set_ylabel("calorimeter temperature / °C"); c.set_ylim(24.95, 26.7)
c.set_title("C  Bomb calorimeter (illustrative curve, not data)", fontsize=10)

# D  Delta n_g R T
d = axes[1, 1]
RT = R * 298.15 / 1000
items = [("N$_2$+3H$_2$→2NH$_3$", -2), ("CH$_4$+2O$_2$→CO$_2$+2H$_2$O(l)", -2), ("benzoic acid\ncombustion", -0.5), ("glucose\ncombustion", 0), ("C+H$_2$O(g)→CO+H$_2$", 1), ("H$_2$O(l)→H$_2$O(g)\n(at 298 K)", 1)]
vals = [n * RT for _, n in items]
cols = [BLUE if v < 0 else (MUTED if v == 0 else ORANGE) for v in vals]
d.barh(range(len(items)), vals, color=cols)
d.set_yticks(range(len(items))); d.set_yticklabels([n for n, _ in items], fontsize=8)
for i, v in enumerate(vals): d.text(v + (0.12 if v >= 0 else -0.12), i, f"{v:+.2f}", va="center", ha="left" if v >= 0 else "right", fontsize=8.5)
d.axvline(0, color=INK, lw=0.8); d.invert_yaxis(); d.set_xlim(-6.4, 4.4)
d.set_xlabel(r"$\Delta H-\Delta U=\Delta n_g RT$ / kJ mol$^{-1}$ (298 K)")
d.set_title("D  Enthalpy and internal energy differ by gas moles", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.012, "Computed in scripts/th_tutorial_numbers.py (data: Schroeder pp. 404-405 and the tutorial). Panel C is an illustrative Newton-cooling model with the tutorial's $C$, $\\Delta T$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_th07_thermochemistry")
