"""CL14 - how jet strength scales with the temperature contrast (thermal wind) and with latitude (1/f).

u_jet ~ (g H / (f T)) (Delta T / L):  (a) vs Delta T for three jet widths L;  (b) vs latitude for a fixed contrast, showing
why geostrophic jets cannot be computed near the equator (f -> 0) and why a given gradient gives a weaker jet poleward.
"""
from figlib import *

H = 10e3          # depth of the shear layer (m)
T0 = 250.0
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 4.0))

lat = 35.0
f = 2 * OMEGA * np.sin(np.radians(lat))
dT = np.linspace(0, 30, 100)
for L, col in [(1.5e6, BLUE), (2.0e6, ORANGE), (3.0e6, AQUA)]:
    a.plot(dT, G0 * H / (f * T0 * L) * dT, color=col, label=f"L = {L/1e3:.0f} km")
a.axhline(30, color=MUTED, lw=0.8, ls=":")
a.annotate("observed annual-mean jet ≈ 30 m/s", (0.4, 30.8), fontsize=8.5, color=INK, bbox=dict(fc=SURFACE, ec="none", alpha=0.9, pad=1.5))
a.axhline(20, color=MUTED, lw=0.8, ls=":")
a.annotate("weaker (summer-hemisphere) jet ≈ 20 m/s", (0.4, 20.8), fontsize=8.5, color=INK, bbox=dict(fc=SURFACE, ec="none", alpha=0.9, pad=1.5))
for dTx, uy in [(30 * 2.0e6 / (G0 * H / (f * T0)), 30), (20 * 2.0e6 / (G0 * H / (f * T0)), 20)]:
    a.plot([dTx], [uy], "o", color=ORANGE, ms=6)
    a.annotate(f"ΔT ≈ {dTx:.1f} K", (dTx, uy), xytext=(8, -14), textcoords="offset points", fontsize=8.5)
    print(f"L=2000 km, 35 deg: u={uy} m/s needs dT = {dTx:.1f} K")
a.set_xlabel("temperature contrast ΔT across the jet (K)")
a.set_ylabel("jet speed at 10 km (m s$^{-1}$)")
a.set_title("(a) Double the contrast, double the jet", fontsize=10.5)
a.legend(loc="upper left", fontsize=8.5, bbox_to_anchor=(0.0, 0.8))
a.set_ylim(0, 65)

lats = np.linspace(8, 80, 300)
fl = 2 * OMEGA * np.sin(np.radians(lats))
b.plot(lats, G0 * H / (fl * T0 * 2.0e6) * 13.0, color=ORANGE, lw=2.2)
b.axvspan(0, 12, color=GRID, alpha=0.9, lw=0)
b.annotate("geostrophy\nbreaks down\n(f → 0)", (1.0, 38), fontsize=8.5, color=MUTED)
b.set_xlabel("latitude (°)")
b.set_ylabel("jet speed for ΔT = 13 K, L = 2000 km (m s$^{-1}$)")
b.set_title("(b) Same contrast, weaker jet poleward ($\\propto1/\\sin\\varphi$)", fontsize=10.5)
b.set_xlim(0, 80)
b.set_ylim(0, 60)
fig.tight_layout()
save(fig, "fig_cl14_jet_scaling")
