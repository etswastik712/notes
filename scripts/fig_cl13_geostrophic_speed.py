"""CL13 - how strong is the geostrophic wind?  (a) V_g vs isobar spacing for 4 hPa isobars, several latitudes (surface, rho = 1.2).
(b) V_g = (1/rho f)|grad p| at fixed gradient vs latitude: it diverges as f -> 0, so geostrophy fails near the equator
(shaded: latitudes where Ro = U/(fL) > 0.3 for a 1000 km system with U = 10 m/s).
"""
from figlib import *

RHO = 1.2
fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.9))
spac = np.linspace(100, 800, 200)                       # km between 4 hPa isobars
for lat, c in [(20, BLUE), (45, ORANGE), (70, AQUA)]:
    f = 2 * OMEGA * np.sin(np.radians(lat))
    V = (400.0 / (spac * 1e3)) / (RHO * f)
    a.plot(spac, V, color=c, label=f"{lat}°")
    k = np.argmin(abs(spac - 300))
    a.plot([300], [V[k]], "o", color=c, ms=4.5)
    print(f"lat {lat}: V_g at 300 km spacing = {V[k]:.1f} m/s")
a.set_xlabel("spacing between 4 hPa isobars (km)")
a.set_ylabel("geostrophic wind (m s$^{-1}$)")
a.set_title("Closer isobars, stronger wind; weaker $f$, stronger wind", fontsize=10)
a.set_ylim(0, 60)
a.legend(title="latitude", fontsize=8.5, title_fontsize=8.5, loc="upper right")
a.annotate("10.8 m/s at 45°N,\n300 km spacing", (300, 10.8), xytext=(380, 30), fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))

lat = np.linspace(2, 80, 400)
f = 2 * OMEGA * np.sin(np.radians(lat))
grad = 400.0 / 3e5
b.plot(lat, grad / (RHO * f), color=INK)
Ro = 10.0 / (f * 1e6)
b.axvspan(0, np.degrees(np.arcsin(10.0 / (0.3 * 1e6) / (2 * OMEGA))), color=RED, alpha=0.12, lw=0)
lim = np.degrees(np.arcsin(10.0 / (0.3 * 1e6) / (2 * OMEGA)))
print(f"Ro>0.3 for latitude < {lim:.1f} deg (U=10 m/s, L=1000 km)")
b.annotate(f"Ro > 0.3:\ngeostrophy\nunreliable\n(< {lim:.0f}°)", (lim / 2, 55), ha="center", fontsize=8.5, color=INK)
b.set_ylim(0, 70); b.set_xlim(0, 80)
b.set_xlabel("latitude (°)")
b.set_ylabel("$V_g$ for 4 hPa per 300 km (m s$^{-1}$)")
b.set_title("The $1/\\sin\\varphi$ blow-up at the equator", fontsize=10)
fig.tight_layout()
save(fig, "fig_cl13_geostrophic_speed")
