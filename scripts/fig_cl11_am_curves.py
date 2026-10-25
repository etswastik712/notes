"""CL11 - angular-momentum-conserving winds: a family of curves, and the 'inertial speed' picture of the ring of air.

(a) u(phi; phi0) = Omega a (cos^2 phi0 - cos^2 phi)/cos phi : the wind a ring needs after moving from rest at phi0 to phi.
(b) For a ring leaving the equator at rest: inertial-frame speed of the ground, Omega a cos(phi), and of the ring, Omega a / cos(phi);
    the gap is the wind u relative to the ground.
"""
from scipy.optimize import brentq

from figlib import *

Oa = OMEGA * R_EARTH
ph = np.radians(np.linspace(0, 60, 601))
deg = np.degrees(ph)

fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 4.3))

a.axhspan(30, 50, color="#eda100", alpha=0.18, lw=0)
a.annotate("observed subtropical jet:\n~30 m/s mean, ~50 m/s instantaneous", (59, 41), ha="right", va="center", fontsize=8.3, color=INK)
cols = {0: ORANGE, 5: BLUE, 10: AQUA, 15: VIOLET}
for p0, c in cols.items():
    u = Oa * (np.cos(np.radians(p0)) ** 2 - np.cos(ph) ** 2) / np.cos(ph)
    m = ph >= np.radians(p0)
    a.plot(deg[m], u[m], color=c, lw=2.0 if p0 == 0 else 1.5, label=f"ring starting at rest at {p0}°" if p0 else "ring starting at rest at the equator")
for U in (30, 50):
    x = np.degrees(brentq(lambda t: Oa * np.sin(t) ** 2 / np.cos(t) - U, 0.01, 1.4))
    a.plot([x], [U], "o", color=ORANGE, ms=5)
    a.annotate(f"{x:.1f}°", (x, U), xytext=(-6, 6), textcoords="offset points", ha="right", fontsize=8.3)
y30 = Oa * np.sin(np.radians(30)) ** 2 / np.cos(np.radians(30))
a.plot([30], [y30], "o", color=ORANGE, ms=6)
a.annotate(f"{y30:.0f} m/s at 30°\n(M&P prints 130)", (30, y30), xytext=(-10, 8), textcoords="offset points", ha="right", fontsize=8.5)
a.set_xlim(0, 60)
a.set_ylim(0, 260)
a.set_xlabel("latitude (°)")
a.set_ylabel("wind needed to conserve $A$  (m s$^{-1}$)")
a.set_title("(a) angular-momentum-conserving wind")
a.legend(loc="upper left", fontsize=8.2)

ground = Oa * np.cos(ph)
ring = Oa / np.cos(ph)
b.plot(deg, ground, color=BLUE, label="ground, $\\Omega a\\cos\\varphi$")
b.plot(deg, ring, color=ORANGE, label="ring from the equator, $\\Omega a/\\cos\\varphi$")
b.fill_between(deg, ground, ring, color=ORANGE, alpha=0.15, lw=0)
i = int(np.argmin(abs(deg - 30)))
b.annotate("the gap is the\nwind $u$ felt\nat the ground", (deg[i], 0.5 * (ground[i] + ring[i])), ha="center", fontsize=8.8)
b.set_xlim(0, 60)
b.set_ylim(150, 950)
b.set_xlabel("latitude (°)")
b.set_ylabel("speed in the inertial frame (m s$^{-1}$)")
b.set_title("(b) the ring spins faster as its circle shrinks")
b.legend(loc="upper left", fontsize=8.3)
fig.tight_layout()
print("ring wind at 10/20/30/45/60 deg:", [round(Oa * np.sin(np.radians(d)) ** 2 / np.cos(np.radians(d)), 1) for d in (10, 20, 30, 45, 60)])
save(fig, "fig_cl11_am_curves")
