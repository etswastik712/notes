"""CL06 - how the mass of the atmosphere is distributed with height.

(a) fraction of the total mass below height z = 1 - p(z)/p0 (isothermal H = 7.5, 8.4 km and the Standard Atmosphere);
(b) fraction of the mass in each successive scale height: (1-1/e)=63 %, then 23 %, 8.6 %, ... (W&H Ex. 1.4).
"""
from cl06lib import *
from figlib import *

z = np.linspace(0, 50, 501)
_, pstd = std_atm(z)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 4.4), gridspec_kw={"width_ratios": [1.25, 1]})
a.plot(z, 100 * (1 - np.exp(-z / 7.5)), color=AQUA, label="isothermal, H = 7.5 km")
a.plot(z, 100 * (1 - np.exp(-z / 8.4)), color=ORANGE, label="isothermal, H = 8.4 km")
a.plot(z, 100 * (1 - pstd / P0), color=INK, lw=2.2, label="Standard Atmosphere")
for zz, txt, dx, dy in ((5.5, "50 % at 5.5 km", 12, -14), (11.0, "tropopause: 78 % of the mass", 10, -26), (20.0, "95 % below 20 km", 8, -22)):
    f = 100 * (1 - float(std_atm(zz)[1][0]) / P0)
    a.plot([zz], [f], "o", color=INK, ms=5, zorder=5)
    a.annotate(txt, (zz, f), xytext=(dx, dy), textcoords="offset points", fontsize=8.5)
    print(f"mass below {zz} km: {f:.1f} %")
a.axhline(50, color=GRID, lw=1)
a.set_xlabel("height (km)")
a.set_ylabel("percent of the atmosphere's mass below this height")
a.set_ylim(0, 102)
a.set_xlim(0, 50)
a.legend(loc="lower right", fontsize=8.5)
a.set_title("(a) Most of the air is close to the ground", fontsize=10)

n = np.arange(1, 7)
frac = np.exp(-(n - 1)) - np.exp(-n)
b.bar(n, 100 * frac, color=BLUE, width=0.62)
for ni, f in zip(n, frac):
    b.annotate(f"{100*f:.1f} %", (ni, 100 * f), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=8.5)
b.set_xlabel("n-th scale height above the ground")
b.set_ylabel("percent of the mass in that layer")
b.set_ylim(0, 72)
b.set_title("(b) Each scale height holds 1/e of the previous", fontsize=10)
b.grid(axis="x", visible=False)
fig.tight_layout()
save(fig, "fig_cl06_mass_fraction")
