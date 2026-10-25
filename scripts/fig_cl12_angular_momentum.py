"""CL12 - angular-momentum bookkeeping on the rotating Earth.

(a) eastward speed of the ground, Omega a cos(phi): 464 m/s at the equator, 328 m/s at 45 deg (Suhas 15 Oct p20: 460 / 330).
(b) eastward wind u(phi) = Omega a sin^2(phi)/cos(phi) of a ring of air that starts at rest at the equator and conserves
    absolute angular momentum A = Omega a^2 cos^2(phi) + u a cos(phi)  (Suhas 8 Oct p18; Marshall & Plumb Eq. 8-2).
"""
from figlib import *

phi = np.radians(np.linspace(0, 70, 281))
Oa = OMEGA * R_EARTH
ground = Oa * np.cos(phi)
u = Oa * np.sin(phi) ** 2 / np.cos(phi)

fig, (a, b) = plt.subplots(1, 2, figsize=(9.2, 3.8))
a.plot(np.degrees(phi), ground, color=BLUE)
for d in (0, 45):
    y = Oa * np.cos(np.radians(d))
    a.plot([d], [y], "o", color=BLUE, ms=5)
    a.annotate(f"{y:.0f} m/s", (d, y), xytext=(8, 6), textcoords="offset points", fontsize=8.5)
a.set_xlabel("latitude (°)")
a.set_ylabel("eastward speed of the ground (m s$^{-1}$)")
a.set_title("Ground speed shrinks poleward")
a.set_ylim(0, 520)

b.plot(np.degrees(phi), u, color=ORANGE)
for d in (10, 20, 30, 45):
    y = Oa * np.sin(np.radians(d)) ** 2 / np.cos(np.radians(d))
    b.plot([d], [y], "o", color=ORANGE, ms=5)
    b.annotate(f"{y:.0f}", (d, y), xytext=(7, -12), textcoords="offset points", ha="left", fontsize=8.5)
b.axhline(50, color=MUTED, ls=":", lw=1)
b.annotate("observed jet-stream\nspeeds: ~30–50 m/s", (70, 55), ha="right", va="bottom", fontsize=8.5, color=MUTED)
b.set_xlabel("latitude (°)")
b.set_ylabel("wind needed to conserve A  (m s$^{-1}$)")
b.set_title("A ring from the equator would race ahead")
b.set_ylim(0, 700)
fig.tight_layout()
save(fig, "fig_cl12_angular_momentum")
