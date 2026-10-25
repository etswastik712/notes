"""CL03 - zero-dimensional prediction T_e for the planets vs measured temperatures.

Data: NASA Planetary Fact Sheet (nssdc.gsfc.nasa.gov/planetary/factsheet), fetched 2026-10-23:
  solar irradiance S at the planet, Bond albedo A, and the measured temperature listed there
  (mean surface for rocky planets, 1-bar level for giants).
T_e is recomputed here: T_e = [S(1-A)/(4 sigma)]^(1/4).
"""
from figlib import *

# name, S (W m-2), Bond albedo, measured T (K), low, high of measured (for uncertain entries)
P = [
    ("Mercury", 9082.7, 0.068, 440, 340, 440),   # NASA lists 440 K; other sources quote ~340 K -> shown as a range
    ("Venus",   2601.3, 0.77,  737, 737, 737),
    ("Earth",   1361.0, 0.294, 288, 288, 288),
    ("Mars",     586.2, 0.250, 214, 214, 214),
    ("Jupiter",   50.26, 0.343, 165, 165, 165),   # 1-bar level
    ("Saturn",    14.82, 0.342, 134, 134, 134),
]

names = [p[0] for p in P]
Te = np.array([(p[1] * (1 - p[2]) / (4 * SIGMA)) ** 0.25 for p in P])
Tm = np.array([p[3] for p in P])
print(dict(zip(names, np.round(Te, 1))))

fig, ax = plt.subplots(figsize=(6.6, 4.2))
x = np.arange(len(P))
w = 0.36
ax.bar(x - w / 2, Te, w, color=BLUE, label=r"$T_e$ from energy balance (no atmosphere)")
ax.bar(x + w / 2, Tm, w, color=ORANGE, label="measured (surface / 1 bar)")
for i, p in enumerate(P):
    if p[4] != p[5]:
        ax.plot([i + w / 2] * 2, [p[4], p[5]], color=INK, lw=1.6)
        ax.annotate("sources\ndisagree", (i + w / 2, p[5]), xytext=(14, 6), textcoords="offset points", fontsize=7.5, color=MUTED)
    ax.annotate(f"{Te[i]:.0f}", (i - w / 2, Te[i]), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=8)
    ax.annotate(f"{p[3]:.0f}", (i + w / 2, p[3]), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=8)
ax.set_xticks(x)
ax.set_xticklabels(names)
ax.set_yscale("log")
ax.set_ylim(60, 1300)
ax.set_ylabel("temperature (K), log scale")
ax.set_title("A bare-rock energy balance gets the pattern; atmospheres supply the rest")
ax.legend(loc="upper right", fontsize=8.5)
ax.grid(axis="x", visible=False)
save(fig, "fig_cl03_planets")
