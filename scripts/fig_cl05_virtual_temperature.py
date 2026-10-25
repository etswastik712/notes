"""CL05 - why humid air is LIGHT: molar masses (a) and the virtual-temperature excess T_v - T at 1000 hPa (b)."""
from cl06lib import *
from figlib import *

# (a) molar masses
Md = 28.965
Mw = 18.015
x_w = 0.04
M_moist = (1 - x_w) * Md + x_w * Mw
items = [("N$_2$", 28.013, BLUE), ("O$_2$", 32.000, BLUE), ("dry air", Md, INK), ("moist air\n(4 % vapour)", M_moist, ORANGE), ("H$_2$O", Mw, ORANGE)]
print(f"M_moist(4%) = {M_moist:.2f} g/mol; Rm/Rd = {Md/M_moist:.4f}")

fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 4.2), gridspec_kw={"width_ratios": [1, 1.2]})
for i, (n, m, c) in enumerate(items):
    a.bar(i, m, color=c, width=0.62)
    a.annotate(f"{m:.1f}", (i, m), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)
a.set_xticks(range(len(items)))
a.set_xticklabels([n for n, _, _ in items], fontsize=8.5)
a.set_ylabel("molar mass (g mol$^{-1}$)")
a.set_ylim(0, 38)
a.set_title("(a) water vapour is the lightest air molecule", fontsize=10.5)
a.grid(axis="x", visible=False)

# (b) T_v - T at 1000 hPa
Tc = np.linspace(-20, 35, 200)
T = Tc + 273.15
for RH, col, lab in ((1.0, ORANGE, "saturated (RH 100 %)"), (0.5, BLUE, "RH 50 %")):
    e = RH * e_sat(T)
    q = q_from_e(e, 1000.0)
    dTv = virtual_T(T, q) - T
    b.plot(Tc, dTv, color=col, label=lab)
    i = np.argmin(abs(Tc - 30))
    b.plot([30], [dTv[i]], "o", color=col, ms=5)
    b.annotate(f"{dTv[i]:.1f} K at 30 °C", (30, dTv[i]), xytext=(-6, 8), textcoords="offset points", ha="right", fontsize=8.5)
b.set_xlabel("temperature T (°C), p = 1000 hPa")
b.set_ylabel(r"$T_v-T$  (K)")
b.set_ylim(0, 6)
b.legend(loc="upper left", fontsize=8.5)
b.set_title("(b) the correction is a few kelvin, and only in the warm tropics", fontsize=10.5)
fig.tight_layout()
save(fig, "fig_cl05_virtual_temperature")
