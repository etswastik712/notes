"""CL06 - the hypsometric equation: thickness of the 1000-500 hPa layer is proportional to its mean virtual temperature.

(a) Delta Z = (R_d/g0) ln2 * T_v-mean = 20.3 m/K * T  with three reference temperatures;
(b) a warm and a cold column with the same surface pressure: the pressure surfaces are farther apart in the warm one,
    so the 500 hPa height is higher over warm air.  (Illustrative mean temperatures, linear in x.)
"""
from cl06lib import *
from figlib import *

coef = RD / G0 * np.log(2)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 4.6), gridspec_kw={"width_ratios": [1, 1.2]})
T = np.linspace(230, 300, 100)
a.plot(T, coef * T / 1e3, color=INK)
for Tm, lab, dx, dy in ((242, "polar winter column", 10, -34), (266.15, "the 5400 m line\n(rain/snow rule of thumb)", 12, -42), (286, "tropical column", -12, 8)):
    a.plot([Tm], [coef * Tm / 1e3], "o", color=ORANGE, ms=6)
    a.annotate(f"{lab}\n$\\bar T_v$ = {Tm:.0f} K → {coef*Tm:.0f} m", (Tm, coef * Tm / 1e3), xytext=(dx, dy), textcoords="offset points",
               ha="left" if dx > 0 else "right", fontsize=8.5)
    print(f"Tm={Tm} K -> thickness {coef*Tm:.0f} m")
a.set_xlabel(r"layer-mean virtual temperature $\bar T_v$ (K)")
a.set_ylabel("thickness of the 1000–500 hPa layer (km)")
a.set_title(f"(a) Thickness = {coef:.2f} m per kelvin × $\\bar T_v$", fontsize=10)
a.set_xlim(230, 300)

x = np.linspace(-1, 1, 200)
Tbar = 246 + 20 * (x + 1)          # 246 K (cold column) ... 286 K (warm column): a 40 K contrast, like equator vs pole
zs = {}
for p, col in ((1000, MUTED), (850, BLUE), (700, AQUA), (500, ORANGE), (300, RED)):
    zz = RD * Tbar / G0 * np.log(1000 / p) / 1e3
    zs[p] = zz
    b.plot(x, zz, color=col, lw=2.2 if p == 500 else 1.4)
    b.annotate(f"{p} hPa", (-1.0, zz[0]), xytext=(-6, 0), textcoords="offset points", ha="right", va="center", fontsize=8.5, color=INK)
for yv in (zs[500][0], zs[500][-1]):
    b.plot([1.0, 1.12], [yv, yv], color=MUTED, lw=0.8)
b.annotate("", xy=(1.12, zs[500][-1]), xytext=(1.12, zs[500][0]), arrowprops=dict(arrowstyle="<->", color=INK, lw=1.0))
b.annotate(f"{1e3*(zs[500][-1]-zs[500][0]):.0f} m", (1.12, 0.5 * (zs[500][-1] + zs[500][0])), xytext=(6, 0), textcoords="offset points", va="center", fontsize=8.5)
b.annotate("cold column", (-1, 0.15), ha="left", va="bottom", fontsize=9, color=BLUE)
b.annotate("warm column", (1, 0.15), ha="right", va="bottom", fontsize=9, color=RED)
b.set_xlim(-1.35, 1.4)
b.set_ylim(0, 10.6)
b.set_xlabel("horizontal position (cold → warm)")
b.set_ylabel("height above the 1000 hPa surface (km)")
b.set_xticks([])
b.set_title("(b) Warm air is fluffier: isobars spread apart", fontsize=10)
b.grid(axis="x", visible=False)
fig.tight_layout()
save(fig, "fig_cl06_thickness")
