"""CL06 - p(z) = p0 exp(-z/H) for isothermal atmospheres vs the US Standard Atmosphere (a), and the scale height H = R_d T / g (b)."""
from cl06lib import *
from figlib import *

z = np.linspace(0, 60, 601)
Tstd, pstd = std_atm(z)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 4.8), gridspec_kw={"width_ratios": [1.15, 1]})
for T, col, lab in ((220, BLUE, "T = 220 K,  H = 6.4 km"), (255, AQUA, "T = 255 K,  H = 7.5 km"), (288, ORANGE, "T = 288 K,  H = 8.4 km")):
    H = RD * T / G0 / 1e3
    a.plot(P0 * np.exp(-z / H), z, color=col, lw=1.6, label=lab)
a.plot(pstd, z, color=INK, lw=2.2, label="US Standard Atmosphere")
a.set_xscale("log")
a.set_xlim(0.1, 1300)
a.set_ylim(0, 60)
for zz, txt in ((5.5, "half the mass below 5.5 km"), (11.0, "tropopause (11 km)"), (8.848, "Everest")):
    pz = float(std_atm(zz)[1][0])
    a.plot([pz], [zz], "o", color=INK, ms=5, zorder=5)
a.annotate("tropopause 11 km", (float(std_atm(11.0)[1][0]), 11.0), xytext=(420, 24), textcoords="data", ha="left", fontsize=8.5,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
a.annotate("Everest 8.85 km", (float(std_atm(8.848)[1][0]), 8.848), xytext=(420, 17), textcoords="data", ha="left", fontsize=8.5,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
a.annotate("5.5 km: 500 hPa,\nhalf the mass", (float(std_atm(5.5)[1][0]), 5.5), xytext=(70, 3), textcoords="data", ha="right", fontsize=8.5,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
a.set_xlabel("pressure (hPa), log scale")
a.set_ylabel("height (km)")
a.set_title("(a) Straight lines on a log axis: pressure falls exponentially", fontsize=10)
a.legend(loc="upper right", fontsize=8.5)

T = np.linspace(180, 320, 200)
b.plot(T, RD * T / G0 / 1e3, color=INK)
b.axhspan(7, 8.5, color="#eda100", alpha=0.18, lw=0)
b.annotate("observed range 7–8.5 km", (184, 7.75), fontsize=8.5, va="center", color=MUTED)
for Tv, lab, dy in ((255, "255 K (the slides)", -18), (288, "288 K (surface)", -18), (220, "220 K (tropopause)", -18)):
    H = RD * Tv / G0 / 1e3
    b.plot([Tv], [H], "o", color=ORANGE, ms=6)
    b.annotate(f"{lab}: {H:.2f} km", (Tv, H), xytext=(6, dy), textcoords="offset points", fontsize=8.5)
b.set_xlabel("temperature T (K)")
b.set_ylabel("scale height H (km)")
b.set_xlim(180, 350)
b.set_ylim(5, 10)
b.set_title(r"(b) $H=R_dT/g$ is proportional to $T$", fontsize=10)
fig.tight_layout()
save(fig, "fig_cl06_pressure_profiles")
print("p at 11 km (std):", float(std_atm(11)[1][0]), " Everest std:", float(std_atm(8.848)[1][0]))
