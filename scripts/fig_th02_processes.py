"""TH02 - quasi-static processes of 1 mol of ideal gas on a PV diagram, and the path dependence of work and heat."""
from figlib import *

R = 8.314462618; atm = 101325.0
T1 = 300.0; V1 = R * T1 / atm; P1 = atm
Vs = np.linspace(V1, 2 * V1, 300)
fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.1), gridspec_kw=dict(width_ratios=[1.1, 1]))
a = axes[0]
a.plot(Vs * 1e3, R * T1 / Vs / 1e3, color=BLUE, label=r"isotherm: $W=RT\ln2=1729$ J")
a.plot([V1 * 1e3, 2 * V1 * 1e3], [P1 / 1e3] * 2, color=ORANGE, label=r"isobar: $W=P\Delta V=2494$ J")
a.plot(Vs * 1e3, P1 * (V1 / Vs) ** (5 / 3) / 1e3, color=AQUA, label=r"adiabat ($\gamma=5/3$): $W=1385$ J")
a.plot([V1 * 1e3] * 2, [P1 * 2 ** -(5 / 3) / 1e3, P1 / 1e3], color=VIOLET, label="isochor: $W=0$")
a.plot([V1 * 1e3], [P1 / 1e3], "o", color=INK, ms=6)
a.set_xlabel("$V$ (L)"); a.set_ylabel("$P$ (kPa)"); a.legend(fontsize=8.2, loc="upper right"); a.set_xlim(23, 51); a.set_ylim(20, 108)
a.set_title("A  four processes from one state, 1 mol, 300 K", fontsize=10)
a.text(24, 28, "work done by the gas = area under the curve", fontsize=8.2, color=MUTED)
b = axes[1]
Va, Vb, Pa, Pb = 10.0, 20.0, 2 * atm / 1e3, atm / 1e3
b.plot([Va, Va, Vb], [Pa, Pb, Pb], color=BLUE, lw=2.2, label="path 1: isochor, then isobar")
b.plot([Va, Vb, Vb], [Pa, Pa, Pb], color=ORANGE, lw=2.2, label="path 2: isobar, then isochor")
b.fill_between([Va, Vb], [Pb, Pb], color=BLUE, alpha=0.14)
b.fill_between([Va, Vb], [Pa, Pa], color=ORANGE, alpha=0.10)
b.text(15, Pb / 2, "$W_1=1013$ J", ha="center", fontsize=9, color=BLUE)
b.text(15, (Pa + Pb) / 2 + 0.2 * Pb, "$W_2=2026$ J", ha="center", fontsize=9, color=ORANGE)
b.plot([Va, Vb], [Pa, Pb], "o", color=INK, ms=6); b.text(Va - 0.3, Pa + 5, "A", ha="right"); b.text(Vb + 0.3, Pb + 5, "B")
b.set_xlabel("$V$ (L)"); b.set_ylabel("$P$ (kPa)"); b.set_xlim(7, 23); b.set_ylim(0, 250)
b.legend(fontsize=8.2, loc="upper right"); b.set_title(r"B  same endpoints, $\Delta E=0$, different $W$ and $Q$", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "A: curves computed for 1 mol at 300 K, doubling the volume. B: A=(2 atm, 10 L), B=(1 atm, 20 L); $PV$ is equal so $\\Delta E=0$ and $Q=W$ on each path (scripts/th_numbers.py).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_th02_processes")
