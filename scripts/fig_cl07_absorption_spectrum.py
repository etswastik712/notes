"""CL07 - schematic of where the atmospheric gases absorb (band positions rounded from standard tables; ILLUSTRATIVE, not line-by-line)
and the fraction of a 288 K blackbody that lies in each region (numerical integral of the Planck function)."""
from figlib import *

# approximate band ranges in um: (start, end, strength 0-1 used only for shading)
BANDS = {
    "H₂O": [(0.93, 0.97, 0.5), (1.10, 1.16, 0.6), (1.35, 1.45, 0.8), (1.8, 2.0, 0.8), (2.5, 2.9, 0.9), (5.0, 7.5, 1.0), (14, 17, 0.5), (17, 100, 1.0)],
    "CO₂": [(1.95, 2.1, 0.5), (2.65, 2.8, 0.6), (4.2, 4.4, 1.0), (13, 17, 1.0)],
    "O₃": [(0.2, 0.31, 1.0), (0.5, 0.65, 0.3), (9.4, 9.9, 0.9)],
    "CH₄": [(3.2, 3.5, 0.6), (7.3, 8.0, 0.8)],
    "N₂O": [(4.4, 4.6, 0.6), (7.6, 8.0, 0.5), (16.5, 17.5, 0.5)],
    "O₂": [(0.12, 0.24, 1.0), (0.68, 0.70, 0.5), (0.76, 0.77, 0.7)],
}


def planck(lam_m, T):
    return 2 * H_PL * C_LT**2 / (lam_m**5 * np.expm1(H_PL * C_LT / (lam_m * K_B * T)))


lam = np.logspace(-1, 2, 600)
fig = plt.figure(figsize=(9.4, 6.0))
gs = fig.add_gridspec(2, 1, height_ratios=[1.1, 2.3], hspace=0.08)
top = fig.add_subplot(gs[0])
for T, c, lab in [(5772, BLUE, "Sun 5772 K"), (288, ORANGE, "Earth 288 K")]:
    y = planck(lam * 1e-6, T)
    top.plot(lam, y / y.max(), color=c, label=lab)
top.set_xscale("log")
top.set_xlim(0.1, 100)
top.set_ylim(0, 1.15)
top.set_ylabel("spectrum\n(each scaled to peak)")
top.legend(loc="upper left", bbox_to_anchor=(0.27, 1.0), ncol=1, fontsize=8.5)
top.tick_params(labelbottom=False)
top.set_title("Where the gases absorb (schematic: band positions rounded from standard tables)", fontsize=10.5)

bot = fig.add_subplot(gs[1], sharex=top)
names = list(BANDS)
for i, g in enumerate(names):
    y = len(names) - 1 - i
    for a, b, s in BANDS[g]:
        bot.barh(y, b - a if (b - a) > 0.0 else 0.001, left=a, height=0.62, color=BLUE, alpha=0.25 + 0.65 * s, lw=0)
    bot.text(0.105, y, g, va="center", ha="left", fontsize=9.5, fontweight="semibold", color=INK)
bot.axvspan(8, 12, color=AQUA, alpha=0.16, lw=0)
bot.axvspan(0.4, 0.7, color="#eda100", alpha=0.18, lw=0)
bot.annotate("visible\nwindow", (0.53, len(names) - 0.55), ha="center", fontsize=8.5, color=MUTED)
bot.annotate("8–12 µm\nwindow", (10, len(names) - 0.55), ha="center", fontsize=8.5, color=MUTED)
bot.annotate("CO₂ 15 µm", (15, 3.0 - 0.02), xytext=(0, 14), textcoords="offset points", ha="center", fontsize=8, color=MUTED)
bot.set_xscale("log")
bot.set_xlim(0.1, 100)
bot.set_ylim(-0.6, len(names) - 0.05)
bot.set_yticks([])
bot.set_xlabel("wavelength λ (µm)")
bot.grid(axis="y", visible=False)
save(fig, "fig_cl07_absorption_spectrum")

# numbers quoted in the text: fraction of sigma T^4 at 288 K in each region
lam_f = np.logspace(-7, -3, 400001)
B = np.pi * planck(lam_f, 288.0)
tot = SIGMA * 288.0**4
for a, b, n in [(5, 8, "5-8 um (H2O 6.3)"), (8, 12, "8-12 um window"), (13, 17, "13-17 um CO2"), (17, 100, ">17 um rotation")]:
    m = (lam_f >= a * 1e-6) & (lam_f <= b * 1e-6)
    print(f"{n}: {np.trapezoid(B[m], lam_f[m]) / tot:.3f}")
