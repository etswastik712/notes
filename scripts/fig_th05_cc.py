"""TH05 - Clausius-Clapeyron for water: integrating dP/dT = L P/(R_v T^2) with constant L, and the choice of L."""
from figlib import *

Rv = 461.5; Ptp, Ttp = 611.657, 273.16; Pb, Tb = 101325.0, 373.15
Leff = Rv * np.log(Pb / Ptp) / (1 / Ttp - 1 / Tb)
T = np.linspace(253.15, 373.15, 300)
fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.0))
a = axes[0]
a.semilogy(T - 273.15, Ptp * np.exp(-(Leff / Rv) * (1 / T - 1 / Ttp)), color=BLUE, label=r"$L_{\rm eff}=2.40\times10^6$ J/kg (two anchors)")
a.semilogy(T - 273.15, Pb * np.exp(-(2.257e6 / Rv) * (1 / T - 1 / Tb)), color=ORANGE, ls="--", label=r"$L(100\,^\circ$C$)=2.257\times10^6$ only")
pts = [(0.01, 611.657), (10, 1228), (20, 2339), (30, 4246), (40, 7384), (100, 101325)]
a.semilogy([p[0] for p in pts], [p[1] for p in pts], "o", color=INK, ms=5, label="tabulated values (recalled)")
a.set_xlabel("temperature (°C)"); a.set_ylabel("saturation vapour pressure (Pa)"); a.legend(fontsize=8.0, loc="lower right"); a.set_title("A  constant $L$ integrates to an exponential", fontsize=10)
b = axes[1]
Tk = np.linspace(260, 320, 100)
b.plot(Tk - 273.15, 100 * Leff / (Rv * Tk ** 2), color=BLUE)
b.plot([15], [100 * Leff / (Rv * 288.0 ** 2)], "o", color=INK, ms=6); b.annotate("6.3 % per K at 15 °C", (15, 6.28), xytext=(-8, 5.35), fontsize=8.6, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.set_xlabel("temperature (°C)"); b.set_ylabel(r"$\mathrm{d}\ln P_s/\mathrm{d}T=L/R_vT^2$ (% per K)"); b.set_title("B  saturation pressure rises ~6–7 % per kelvin", fontsize=10); b.set_ylim(4.5, 8.5)
fig.tight_layout()
fig.text(0.5, -0.03, "$L_{\\rm eff}$ is fitted so the curve passes through the triple point (611.657 Pa, 273.16 K) and the boiling point (101,325 Pa, 373.15 K): $-4\\%$ at 20 °C, $-5\\%$ at 40 °C. Tabulated points are values recalled from standard tables.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_th05_cc")
