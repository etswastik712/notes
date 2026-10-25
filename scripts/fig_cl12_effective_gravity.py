"""CL12 - why the Earth is oblate: true gravity + centrifugal force = effective gravity, which is the normal
to the (nearly equipotential) surface.  Schematic; the centrifugal term is exaggerated ~120x so the tilt is visible.

At latitude phi on a sphere of radius a:
  true gravity g*  points to the centre,           |g*| = g
  centrifugal      points away from the axis,      Omega^2 a cos(phi)
     vertical (outward) part       Omega^2 a cos^2(phi)
     horizontal (equatorward) part Omega^2 a sin(phi) cos(phi)
"""
from figlib import *

phi = np.radians(42)
P = np.array([np.cos(phi), np.sin(phi)])                 # x = distance from axis, y = along axis
gstar = -P * 0.55
k = 0.55 * 120 * (OMEGA**2 * R_EARTH / G0)                # exaggerated centrifugal length at the equator
cf = np.array([1.0, 0.0]) * k * np.cos(phi)
geff = gstar + cf
vert = P * (cf @ P)

fig, ax = plt.subplots(figsize=(6.4, 6.0))
th = np.linspace(-np.pi / 2, np.pi / 2, 300)
ax.plot(np.cos(th), np.sin(th), color=MUTED, lw=1.4)
ax.plot([0, 0], [-0.1, 1.2], color=INK, lw=1, ls="-.")
ax.annotate("rotation axis Ω", (0.02, 1.13), fontsize=9)
ax.annotate("equator", (1.02, -0.07), fontsize=9, color=MUTED)
ax.plot([0, P[0]], [0, P[1]], color=GRID, lw=1.2)
ax.plot([0, 1], [0, 0], color=GRID, lw=1.2)
ax.plot(*P, "o", color=INK, ms=6, zorder=6)


def arrow(v, c, lw=2.4, ls="-", **kw):
    ax.annotate("", xy=P + v, xytext=P, arrowprops=dict(arrowstyle="-|>", color=c, lw=lw, ls=ls, shrinkA=0, shrinkB=0, **kw), zorder=5)


arrow(gstar, BLUE)
arrow(cf, ORANGE)
arrow(geff, INK)
ax.annotate("true gravity $\\mathbf{g}^*$\n(towards the centre)", P + gstar, xytext=(-8, -4), textcoords="offset points", ha="right", va="top", fontsize=9.5)
ax.annotate("centrifugal $\\Omega^2\\mathbf{R}$\n(away from the axis)", P + cf, xytext=(8, 2), textcoords="offset points", ha="left", va="center", fontsize=9.5)
ax.annotate("effective gravity\n$\\mathbf{g}=\\mathbf{g}^*+\\Omega^2\\mathbf{R}$", P + geff, xytext=(6, -8), textcoords="offset points", ha="left", va="top", fontsize=9.5)
# decomposition of the centrifugal vector into vertical and horizontal parts
ax.annotate("", xy=P + vert, xytext=P, arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.1, ls="--", shrinkA=0, shrinkB=0), zorder=4)
ax.annotate("", xy=P + cf, xytext=P + vert, arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.1, ls="--", shrinkA=0, shrinkB=0), zorder=4)
ax.annotate("vertical part Ω²a cos²φ\n(partly cancels gravity)", P + vert, xytext=(6, 14), textcoords="offset points", fontsize=8, color=MUTED)
ax.annotate("horizontal part\nΩ²a sinφ cosφ\n(equatorward)", P + vert + (cf - vert) * 0.5, xytext=(16, -18), textcoords="offset points", fontsize=8, color=MUTED, va="top")
# local level surface = perpendicular to g_eff
n = geff / np.linalg.norm(geff)
lvl = np.array([-n[1], n[0]])
A, B = P - 0.30 * lvl, P + 0.30 * lvl
ax.plot([A[0], B[0]], [A[1], B[1]], color=RED, lw=1.8, ls="--", zorder=2)
ax.annotate("level surface\n(perpendicular to g,\ntilted off the sphere)", A, xytext=(-6, 4), textcoords="offset points", fontsize=8.5, color=RED, ha="right")
ax.set_aspect("equal")
ax.set_xlim(-0.2, 1.65)
ax.set_ylim(-0.12, 1.25)
ax.axis("off")
ax.set_title("Force balance on a parcel at rest on the rotating Earth\n(centrifugal term exaggerated ~120×)")
save(fig, "fig_cl12_effective_gravity")
