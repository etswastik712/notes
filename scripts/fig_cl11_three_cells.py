"""CL11 - SCHEMATIC three-cell structure of the zonal-mean meridional circulation (annual-mean-like, equinox symmetric).

Streamfunction is constructed, not measured:  psi(phi,p) = F(phi) sin(pi p / p_s), with F built from sine arcs between 0, 30, 60, 90 degrees:
   Hadley (+, clockwise in NH) 0-30, Ferrel (-, anticlockwise) 30-60, Polar (+) 60-90; Southern Hemisphere = mirror with opposite sign.
Amplitudes 100 / 30 / 6 x 1e9 kg/s are illustrative of the *relative* strengths in Marshall & Plumb Fig. 5.21, not a fit.
The wind field follows from psi (pressure coordinates):  [v] = g/(2 pi a cos phi) dpsi/dp,  [omega] = -g/(2 pi a^2 cos phi) dpsi/dphi.
"""
from figlib import *

ps = 1000.0
phi_deg = np.linspace(-89.5, 89.5, 359)
p = np.linspace(0, ps, 201)
PHI, P = np.meshgrid(phi_deg, p)


def F(ph):
    ph = np.asarray(ph, float)
    s = np.sign(ph)
    x = np.abs(ph)
    f = np.where(x < 30, 100 * np.sin(np.pi * x / 30), np.where(x < 60, -30 * np.sin(np.pi * (x - 30) / 30), 6 * np.sin(np.pi * (x - 60) / 30)))
    return s * f


PSI = F(PHI) * np.sin(np.pi * P / ps)                    # 1e9 kg/s

# winds from psi
phi = np.radians(PHI)
cosphi = np.cos(phi)
dpsi_dp = np.gradient(PSI * 1e9, p * 100.0, axis=0)              # per Pa
dpsi_dphi = np.gradient(PSI * 1e9, phi[0], axis=1)
v = G0 / (2 * np.pi * R_EARTH * cosphi) * dpsi_dp                # m/s
omega = -G0 / (2 * np.pi * R_EARTH**2 * cosphi) * dpsi_dphi      # Pa/s
U = np.degrees(v / R_EARTH)                                       # deg lat per s
Vv = omega / 100.0                                                # hPa per s
print(f"max |v| = {np.abs(v).max():.2f} m/s ; max |omega| = {np.abs(omega).max()*864:.1f} hPa/day (peak ascent)")

fig, ax = plt.subplots(figsize=(9.6, 5.6))
levels = [-100, -60, -30, -15, -6, -2, 2, 6, 15, 30, 60, 100]
cs = ax.contourf(PHI, P, PSI, levels=[-120] + levels + [120], cmap="RdBu", alpha=0.5, extend="neither")
ax.contour(PHI, P, PSI, levels=levels, colors=[MUTED], linewidths=0.5)
ax.streamplot(phi_deg, p, U, Vv, color=INK, density=[1.0, 1.0], linewidth=0.7, arrowsize=1.0)
ax.set_ylim(1000, 0)
ax.set_xlim(-90, 90)
ax.set_xticks(range(-90, 91, 30))
ax.set_xticklabels(["90°S", "60°S", "30°S", "EQ", "30°N", "60°N", "90°N"])
ax.set_ylabel("pressure (hPa)")
ax.grid(False)
for x in (-60, -30, 0, 30, 60):
    ax.axvline(x, color=MUTED, lw=0.6, ls=":")

box = dict(boxstyle="round,pad=0.25", fc=SURFACE, ec="none", alpha=0.9)
for x, txt, y in [(15, "Hadley\n(thermally direct)", 520), (45, "Ferrel\n(thermally\nindirect)", 520), (75, "Polar\n(direct)", 430),
                  (-15, "Hadley", 520), (-45, "Ferrel", 520), (-75, "Polar", 430)]:
    ax.text(x, y, txt, ha="center", va="center", fontsize=9, bbox=box)

# top strip: where air rises/sinks
top = dict(xycoords=("data", "axes fraction"), annotation_clip=False, ha="center", va="bottom", fontsize=8.3)
ax.annotate("ITCZ\n(ascent)", (0, 1.015), **top)
ax.annotate("subtropical highs,\ndeserts (descent)", (30, 1.015), **top)
ax.annotate("subtropical highs,\ndeserts (descent)", (-30, 1.015), **top)
ax.annotate("subpolar lows,\nstorm tracks (ascent)", (60, 1.015), **top)
ax.annotate("subpolar lows,\nstorm tracks (ascent)", (-60, 1.015), **top)
# bottom strip: surface winds, below the tick labels
bot = dict(xycoords=("data", "axes fraction"), annotation_clip=False, ha="center", va="top", fontsize=8.3)
for x0, x1, txt in [(0, 30, "trades (E)"), (30, 60, "westerlies (W)"), (60, 90, "polar easterlies (E)"),
                    (-30, 0, "trades (E)"), (-60, -30, "westerlies (W)"), (-90, -60, "polar easterlies (E)")]:
    ax.annotate(txt, ((x0 + x1) / 2, -0.075), **bot)
ax.annotate("surface winds:", (-90, -0.075), xycoords=("data", "axes fraction"), annotation_clip=False, ha="right", va="top", fontsize=8.3, color=MUTED)
ax.set_title("Zonal-mean overturning: three cells per hemisphere\n(schematic; blue = clockwise, red = anticlockwise)", fontsize=10.5, pad=34)
fig.subplots_adjust(bottom=0.16, top=0.80)
save(fig, "fig_cl11_three_cells")
