"""CL05 - composition of dry air by volume (mole fraction) and each gas's contribution to the mean molar mass M_d.

Mole fractions: Wallace & Hobbs Table 1.1 (2006); CO2, CH4, N2O updated to ~2023 surface values (NOAA GML, approximate).
M_d = sum(x_i M_i): the arithmetic that gives 28.97 g/mol and hence R_d = R*/M_d = 287 J kg-1 K-1.
"""
from figlib import *

# name, mole fraction, molar mass (g/mol), is_greenhouse
G = [
    ("N$_2$", 0.7808, 28.013, False), ("O$_2$", 0.2095, 32.000, False), ("Ar", 0.0093, 39.95, False),
    ("CO$_2$", 420e-6, 44.01, True), ("Ne", 18e-6, 20.18, False), ("He", 5.2e-6, 4.00, False),
    ("CH$_4$", 1.9e-6, 16.04, True), ("Kr", 1.1e-6, 83.80, False), ("H$_2$", 0.55e-6, 2.02, False),
    ("N$_2$O", 0.34e-6, 44.01, True), ("O$_3$ (surface)", 0.03e-6, 48.00, True),
]
tot = sum(x for _, x, _, _ in G)
Md = sum(x * m for _, x, m, _ in G) / tot
Rd = 1000 * 8.314462618 / Md
print(f"sum x = {tot:.6f}, M_d = {Md:.3f} g/mol, R_d = {Rd:.2f} J/kg/K")
for n, x, m, _ in G[:4]:
    print(f"  {n}: x*M = {x*m/tot:.4f} g/mol")

fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 4.6), gridspec_kw={"width_ratios": [1.5, 1]})
names = [g[0] for g in G][::-1]
xs = np.array([g[1] for g in G])[::-1]
gh = [g[3] for g in G][::-1]
y = np.arange(len(G))
a.barh(y, xs, color=[ORANGE if h else BLUE for h in gh], height=0.62)
for yi, x in zip(y, xs):
    txt = f"{x*100:.2f} %" if x > 1e-3 else (f"{x*1e6:.3g} ppm" if x >= 1e-6 else f"{x*1e6:.2f} ppm")
    a.annotate(txt, (x, yi), xytext=(5, 0), textcoords="offset points", va="center", fontsize=8.5)
# water vapour range
yw = len(G) + 0.2
a.barh([yw], [5e-2 - 1e-5], left=[1e-5], color="none", edgecolor=ORANGE, hatch="////", height=0.62)
a.annotate("0.001–5 %  (very variable)", (5e-2, yw), xytext=(6, 0), textcoords="offset points", ha="left", va="center", fontsize=8.5)
a.set_yticks(list(y) + [yw])
a.set_yticklabels(names + ["H$_2$O vapour"])
a.set_xscale("log")
a.set_xlim(1e-8, 40)
a.set_xlabel("mole fraction (fraction by volume), log scale")
a.set_title("(a) What dry air is made of", fontsize=10.5)
a.grid(axis="y", visible=False)
from matplotlib.patches import Patch
a.legend(handles=[Patch(color=BLUE, label="not an infrared absorber"), Patch(color=ORANGE, label="greenhouse gas")], loc="lower right", fontsize=8.5)

labs = ["N$_2$", "O$_2$", "Ar", "all others"]
vals = [G[0][1] * G[0][2] / tot, G[1][1] * G[1][2] / tot, G[2][1] * G[2][2] / tot, sum(x * m for _, x, m, _ in G[3:]) / tot]
b.barh(range(4)[::-1], vals, color=[BLUE, BLUE, BLUE, MUTED], height=0.6)
for i, v in zip(range(4)[::-1], vals):
    b.annotate(f"{v:.2f}", (v, i), xytext=(5, 0), textcoords="offset points", va="center", fontsize=9)
b.set_yticks(range(4)[::-1])
b.set_yticklabels(labs)
b.set_xlim(0, 26)
b.set_xlabel("contribution $x_iM_i$ to $M_d$  (g mol$^{-1}$)")
b.set_title(f"(b) $M_d=\\sum x_iM_i={Md:.2f}$ g/mol  →  $R_d={Rd:.0f}$ J/kg/K", fontsize=10.5)
b.grid(axis="y", visible=False)
fig.tight_layout()
save(fig, "fig_cl05_composition")
