"""CL12 - why only the *local vertical* part of the Earth's rotation turns horizontal motion.

At latitude phi the rotation vector Omega (parallel to the axis) has, in the local frame (east, north, up),
   vertical component   Omega sin(phi)   -> spins horizontal flow (sets f = 2 Omega sin phi)
   northward component  Omega cos(phi)   -> tilts the effect into the vertical plane (2 Omega cos phi, negligible at large scale)
Left: the geometry.  Right: the two components as a function of latitude.
"""
from figlib import *

phi = np.radians(40)
fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 4.4), gridspec_kw={"width_ratios": [1.1, 1]})

# ---- geometry in the meridional plane (x = distance from axis, y = along axis)
th = np.linspace(-np.pi / 2, np.pi / 2, 300)
a.plot(np.cos(th), np.sin(th), color=MUTED, lw=1.4)
a.plot([0, 0], [-0.1, 1.7], color=INK, lw=1, ls="-.")
a.annotate("rotation axis", (0.03, 1.62), fontsize=9)
P = np.array([np.cos(phi), np.sin(phi)])
a.plot(*P, "o", color=INK, ms=6, zorder=6)
up = P / np.linalg.norm(P)
north = np.array([-np.sin(phi), np.cos(phi)])
L = 0.85
def arrow(v, c, lw=2.4, ls="-", **kw):
    a.annotate("", xy=P + v, xytext=P, arrowprops=dict(arrowstyle="-|>", color=c, lw=lw, ls=ls, shrinkA=0, shrinkB=0, **kw), zorder=5)
Om = np.array([0.0, 1.0]) * L
cu, cn = Om @ up, Om @ north
# local axes (thin grey), the two components (coloured) and the projection guides (dotted)
arrow(up * 1.05, GRID, lw=1.2)
arrow(north * 1.05, GRID, lw=1.2)
arrow(up * cu, ORANGE, lw=2.6)
arrow(north * cn, BLUE, lw=2.6)
arrow(Om, INK, lw=2.8)
a.plot([P[0] + Om[0], P[0] + up[0] * cu], [P[1] + Om[1], P[1] + up[1] * cu], color=MUTED, lw=0.9, ls=":")
a.plot([P[0] + Om[0], P[0] + north[0] * cn], [P[1] + Om[1], P[1] + north[1] * cn], color=MUTED, lw=0.9, ls=":")
a.annotate(r"$\vec{\Omega}$  (parallel to the axis)", P + Om, xytext=(8, 2), textcoords="offset points", fontsize=9.5)
a.annotate("vertical part  $\\Omega\\sin\\varphi$\n(turns horizontal flow)", P + up * cu, xytext=(10, -26), textcoords="offset points", fontsize=9, va="center", color=INK)
a.annotate("northward part  $\\Omega\\cos\\varphi$", P + north * cn, xytext=(-8, 6), textcoords="offset points", fontsize=9, ha="right", color=INK)
a.annotate("local up", P + up * 1.05, xytext=(6, -4), textcoords="offset points", fontsize=8.5, color=MUTED)
a.annotate("local north", P + north * 1.05, xytext=(-4, 6), textcoords="offset points", fontsize=8.5, color=MUTED, ha="right")
a.annotate(r"$\varphi=40^\circ$", (0.32, 0.12), fontsize=9)
a.plot([0, 1], [0, 0], color=GRID, lw=1.1)
a.plot([0, P[0]], [0, P[1]], color=GRID, lw=1.1)
a.set_aspect("equal")
a.set_xlim(-0.55, 2.2)
a.set_ylim(-0.1, 1.75)
a.axis("off")
a.set_title("Splitting Ω in the local frame (meridional plane)", fontsize=10)

# ---- components vs latitude
lat = np.linspace(0, 90, 200)
b.plot(lat, np.sin(np.radians(lat)), color=ORANGE, label=r"vertical $\sin\varphi$  → $f$")
b.plot(lat, np.cos(np.radians(lat)), color=BLUE, label=r"northward $\cos\varphi$  → $2\Omega\cos\varphi$")
b.axvline(40, color=GRID, lw=1.1)
b.set_xlabel("latitude (°)")
b.set_ylabel(r"component / $\Omega$")
b.set_title("At the equator all of Ω is horizontal", fontsize=10)
b.legend(loc="center left", fontsize=8.5)
fig.tight_layout()
save(fig, "fig_cl12_omega_components")
