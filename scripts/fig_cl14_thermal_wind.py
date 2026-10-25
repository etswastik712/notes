"""CL14 - thermal-wind balance: a warm-tropics / cold-pole temperature contrast tilts the pressure surfaces more and more
with height, so the geostrophic westerly wind must increase with height.

(a) schematic (vertical scale and temperature contrast exaggerated; pressure-surface heights from the hypsometric equation
    z_n(y) = (R T(y)/g) ln(p0/p_n));  (b) the resulting wind profile for the winter / summer contrasts used in the chapter.
"""
from figlib import *

Rd = 287.0
fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.6), gridspec_kw={"width_ratios": [1.25, 1]})

# ---------------- (a) schematic
y = np.linspace(0, 1, 200)                         # equator (0) -> pole (1), arbitrary units
T = 300 - 70 * y                                    # exaggerated mean-layer temperature
p0 = 1000.0
levels = [1000, 700, 500, 300]
cols = {1000: INK, 700: MUTED, 500: MUTED, 300: INK}
Z = {p: Rd * T / G0 * np.log(p0 / p) / 1e3 for p in levels}   # km
zt = Z[300]
a.fill_between(y, 0, zt, color=ORANGE, alpha=0.10, lw=0)
for k in range(10):
    a.fill_between(y[k * 20:(k + 1) * 20 + 1], 0, zt[k * 20:(k + 1) * 20 + 1], color=(0.2 + 0.0 * k, 0.45, 0.85), alpha=0.01 * (k + 1) * 1.6, lw=0)
for p in levels:
    a.plot(y, Z[p], color=cols[p], lw=1.8 if p in (1000, 300) else 1.2)
    a.annotate(f"{p} hPa", (1.0, Z[p][-1]), xytext=(5, 0), textcoords="offset points", va="center", fontsize=8.5)
a.annotate("warm, thick column", (0.02, 0.35), fontsize=9, color=RED)
a.annotate("cold, thin column", (0.62, 0.35), fontsize=9, color=BLUE)
# pressure-gradient and Coriolis forces (upper troposphere, between the 500 and 300 hPa surfaces)
zf = 6.9
a.annotate("", xy=(0.74, zf), xytext=(0.56, zf), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2))
a.annotate("pressure-gradient force", (0.65, zf), xytext=(0, -16), textcoords="offset points", fontsize=8.5, ha="center")
a.annotate("", xy=(0.26, zf), xytext=(0.44, zf), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.2))
a.annotate("Coriolis force", (0.35, zf), xytext=(0, -16), textcoords="offset points", fontsize=8.5, ha="center")
# westerly wind symbols (out of the page): bigger with height
for p, ms in [(850, 7), (600, 12), (400, 18)]:
    zz = Rd * T[24] / G0 * np.log(p0 / p) / 1e3
    a.plot([0.12], [zz], marker="o", mfc=SURFACE, mec=INK, ms=ms, mew=1.4, ls="none")
    a.plot([0.12], [zz], marker=".", color=INK, ms=3, ls="none")
a.annotate("westerly wind $u_g$ (out of the page),\nstronger with height", (0.15, 4.3), xytext=(6, 0), textcoords="offset points", fontsize=8.5, va="center")
a.set_xlim(0, 1.18)
a.set_ylim(0, 10.5)
a.set_xticks([0, 1])
a.set_xticklabels(["equator", "pole"])
a.set_ylabel("height (km)  [not to scale]")
a.set_title("(a) Pressure surfaces fan out upward", fontsize=10.5)
a.grid(False)

# ---------------- (b) profile
lat = 35.0
f = 2 * OMEGA * np.sin(np.radians(lat))
zk = np.linspace(0, 12, 100)
L = 2.0e6
T0 = 250.0
for dT, col, name in [(14.5, ORANGE, "winter: 14.5 K per 2000 km"), (8.5, BLUE, "summer: 8.5 K per 2000 km")]:
    u = G0 / (f * T0) * (dT / L) * zk * 1e3
    b.plot(u, zk, color=col, lw=2.2, label=name)
    b.plot([u[np.argmin(abs(zk - 10))]], [10], "o", color=col, ms=6)
    print(name, "u(10 km) = %.1f m/s" % u[np.argmin(abs(zk - 10))], " shear %.2f m/s per km" % (G0 / (f * T0) * (dT / L) * 1e3))
b.set_xlabel("geostrophic westerly wind relative to the surface  (m s$^{-1}$)")
b.set_ylabel("height (km)")
b.set_title("(b) $u_g(z)=\\dfrac{g}{fT}\\left|\\dfrac{\\partial T}{\\partial y}\\right| z$ at 35°", fontsize=10.5)
b.legend(loc="lower right", fontsize=8.5)
b.set_xlim(0, 45)
b.set_ylim(0, 12)
fig.tight_layout()
save(fig, "fig_cl14_thermal_wind")
