"""CL12 - the same free particle seen from the inertial and from the rotating frame (Omega > 0, anticlockwise).

A parcel is launched from the rotation axis at t=0 with velocity v along the rotating x-axis.  With no force
acting it moves in a straight line in the inertial frame; the rotating observer sees a path that curves to the
RIGHT of the motion (clockwise bend), which is the Coriolis deflection in the Northern Hemisphere sense.
"""
from figlib import *

Om, v = 1.0, 1.0
t = np.linspace(0, 2.6, 400)
xi, yi = v * t, 0 * t                                    # inertial: straight
xr = v * t * np.cos(Om * t)                              # rotating coordinates  r_rot = R(-Om t) r_in
yr = -v * t * np.sin(Om * t)

fig, (a, b) = plt.subplots(1, 2, figsize=(9.2, 4.6))
mk = np.arange(0, 400, 50)
for ax, (x, y), title, c in [(a, (xi, yi), "Inertial frame: straight line", BLUE), (b, (xr, yr), "Rotating frame: bends to the right", ORANGE)]:
    ax.plot(x, y, color=c, zorder=3)
    ax.plot(x[mk], y[mk], "o", color=INK, ms=3.5, zorder=4)
    for k in mk[1::2]:
        ax.annotate(f"t={t[k]:.1f}", (x[k], y[k]), xytext=(5, 7), textcoords="offset points", fontsize=7.5, color=MUTED)
    ax.plot([0], [0], "s", color=INK, ms=6, zorder=5)
    ax.set_aspect("equal")
    ax.set_title(title)
    ax.set_xlim(-1.5, 2.9)
    ax.set_ylim(-2.4, 2.4)
    ax.set_xlabel("x")
b.set_ylabel("y")
for th in (0.0, 1.0, 2.0):
    a.plot([0, 2.3 * np.cos(th)], [0, 2.3 * np.sin(th)], color="#c9c8c3", lw=1.2, ls="--", zorder=1)
    a.annotate(f"$x_r$, t={th:.0f}", (2.3 * np.cos(th), 2.3 * np.sin(th)), xytext=(4, -12 if th == 0 else 4),
               textcoords="offset points", fontsize=7.5, color=MUTED, ha="left" if th < 1.5 else "right")
a.annotate("dashed: the rotating $x_r$-axis,\nturning anticlockwise (Ω > 0)", (-1.4, -1.9), fontsize=8, color=MUTED)
b.annotate("deflection is perpendicular to the velocity\nand proportional to $2\\Omega v$", (-1.4, 1.95), fontsize=8.5, color=INK)
fig.tight_layout()
save(fig, "fig_cl12_coriolis_paths")
