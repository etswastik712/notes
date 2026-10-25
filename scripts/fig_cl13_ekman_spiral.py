"""CL13 (extra, beyond) - the Ekman layer: wind profile in a boundary layer with constant eddy viscosity K.

Steady, linear: f(v - v_g) + K u'' = 0,  -f(u - u_g) + K v'' = 0, with no-slip at z = 0 and u -> (u_g, 0) aloft.
Solution:  u = u_g [1 - e^{-z/D} cos(z/D)],  v = u_g e^{-z/D} sin(z/D),  D = sqrt(2K/f).
The surface wind is turned 45 deg to the left of V_g (toward low pressure); the wind first points along V_g at z = pi D.
K = 5 m2/s is illustrative; real PBL angles are 10-30 deg because of the surface layer.
"""
from figlib import *

f, K, Ug = 1.03e-4, 5.0, 10.0
D = np.sqrt(2 * K / f)
z = np.linspace(0, 3.2 * D, 300)
u = Ug * (1 - np.exp(-z / D) * np.cos(z / D))
v = Ug * np.exp(-z / D) * np.sin(z / D)
print(f"D = {D:.0f} m, pi D = {np.pi*D:.0f} m; surface wind angle = {np.degrees(np.arctan2(v[1], u[1])):.1f} deg; speed at z=pi D: {np.hypot(u,v)[np.argmin(abs(z-np.pi*D))]:.2f} m/s")

fig, (a, b) = plt.subplots(1, 2, figsize=(9.2, 4.2), gridspec_kw={"width_ratios": [1, 1.05]})
a.plot(u, v, color=BLUE)
for zz in (0.5, 1.0, np.pi / 2, 2.0, np.pi):
    i = np.argmin(abs(z - zz * D))
    a.plot([u[i]], [v[i]], "o", color=BLUE, ms=4.5)
    a.annotate(f"{z[i]:.0f} m", (u[i], v[i]), xytext=(5, 5), textcoords="offset points", fontsize=8)
a.annotate("", xy=(Ug, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.2, ls="--"))
a.annotate("$V_g$", (Ug, 0), xytext=(2, -12), textcoords="offset points", fontsize=9, color=MUTED)
a.set_xlabel("u, along the isobars (m s$^{-1}$)"); a.set_ylabel("v, toward low pressure (m s$^{-1}$)")
a.set_title("Hodograph: the Ekman spiral", fontsize=10)
a.set_aspect("equal"); a.set_xlim(-1, 15); a.set_ylim(-1, 8)
b.plot(np.hypot(u, v), z, color=ORANGE, label="speed")
b.plot(u, z, color=BLUE, ls="--", label="u (along isobars)")
b.plot(v, z, color=AQUA, ls=":", label="v (cross-isobar)")
b.axhline(np.pi * D, color=MUTED, lw=0.8, ls=":")
b.annotate(f"top of the layer ≈ πD = {np.pi*D:.0f} m", (0.2, np.pi * D), xytext=(0, 6), textcoords="offset points", fontsize=8.5)
b.axvline(Ug, color=GRID, lw=1)
b.set_xlabel("wind component (m s$^{-1}$)"); b.set_ylabel("height z (m)")
b.set_title("Speed is sub-geostrophic, then overshoots", fontsize=10)
b.legend(loc="lower right", fontsize=8.5)
fig.tight_layout()
save(fig, "fig_cl13_ekman_spiral")
