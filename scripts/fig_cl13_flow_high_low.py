"""CL13 - geostrophic flow around a low and a high, Northern and Southern Hemisphere.

Pressure field p = p0 -/+ A exp(-r^2 / 2 s^2).  Geostrophic wind: u_g = -(1/rho f) dp/dy, v_g = (1/rho f) dp/dx with f = 2 Omega sin(phi)
(f < 0 in the Southern Hemisphere).  At one marked point we draw the force balance: pressure-gradient force (PGF) and Coriolis force (CF).
Checks: CF = -PGF there (geostrophic balance) and the wind has low pressure on its left in the NH, on its right in the SH.
"""
from figlib import *

RHO = 1.2
A, SIG = 2000.0, 900e3          # 20 hPa deep, 900 km wide (synoptic scale)
x = np.linspace(-2.4e6, 2.4e6, 25)
X, Y = np.meshgrid(x, x)
R2 = X**2 + Y**2

fig, axs = plt.subplots(2, 2, figsize=(8.6, 8.3))
cases = [(45, "L", "Northern Hemisphere, low"), (45, "H", "Northern Hemisphere, high"),
         (-45, "L", "Southern Hemisphere, low"), (-45, "H", "Southern Hemisphere, high")]
for ax, (lat, kind, title) in zip(axs.ravel(), cases):
    f = 2 * OMEGA * np.sin(np.radians(lat))
    sgn = -1 if kind == "L" else 1
    P = 101300 + sgn * A * np.exp(-R2 / (2 * SIG**2))
    dpdx = sgn * A * np.exp(-R2 / (2 * SIG**2)) * (-X / SIG**2)
    dpdy = sgn * A * np.exp(-R2 / (2 * SIG**2)) * (-Y / SIG**2)
    ug, vg = -dpdy / (RHO * f), dpdx / (RHO * f)
    cs = ax.contour(X / 1e3, Y / 1e3, P / 100, levels=(np.arange(996, 1013, 4) if kind == 'L' else np.arange(1014, 1031, 4)), colors=MUTED, linewidths=1.0)
    ax.clabel(cs, fmt="%d", fontsize=7)
    ax.quiver(X[::2, ::2] / 1e3, Y[::2, ::2] / 1e3, ug[::2, ::2], vg[::2, ::2], color=BLUE if kind == "L" else ORANGE, width=0.0045, scale=75)
    ax.text(0, 0, kind, ha="center", va="center", fontsize=18, fontweight="bold", color=INK)
    # force balance at a marked point on the east side (x = +900 km, y = 0)
    px, py = 900e3, 0.0
    gx = sgn * A * np.exp(-px**2 / (2 * SIG**2)) * (-px / SIG**2)
    pgf = np.array([-gx / RHO, 0.0])                    # -(1/rho) grad p
    wind = np.array([0.0, gx / (RHO * f)])              # v_g at this point
    cf = np.array([f * wind[1], 0.0])                   # (+f v, -f u) with u=0
    assert abs((pgf + cf)[0]) < 1e-12                   # geostrophic balance
    s = 6.0e5 / abs(pgf[0])
    ax.annotate("", xy=((px + s * pgf[0]) / 1e3, 0), xytext=(px / 1e3, 0), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2))
    ax.annotate("", xy=((px + s * cf[0]) / 1e3, 0), xytext=(px / 1e3, 0), arrowprops=dict(arrowstyle="-|>", color=VIOLET, lw=2))
    ax.plot([px / 1e3], [0], "o", color=INK, ms=5)
    ax.annotate("PGF", ((px + s * pgf[0]) / 1e3, 0), xytext=(0, 9), textcoords="offset points", ha="center", fontsize=9, color=RED, fontweight="bold")
    ax.annotate("CF", ((px + s * cf[0]) / 1e3, 0), xytext=(0, 9), textcoords="offset points", ha="center", fontsize=9, color=VIOLET, fontweight="bold")
    sense = {("L", 45): "anticlockwise (cyclonic)", ("H", 45): "clockwise (anticyclonic)",
             ("L", -45): "clockwise (cyclonic)", ("H", -45): "anticlockwise (anticyclonic)"}[(kind, lat)]
    ax.set_title(f"{title}: {sense}", fontsize=9.5)
    ax.set_xlim(-2400, 2400); ax.set_ylim(-2400, 2400); ax.set_aspect("equal")
    ax.set_xticks([-2000, 0, 2000]); ax.set_yticks([-2000, 0, 2000])
    if ax in axs[1]: ax.set_xlabel("x (km)")
    if ax in axs[:, 0]: ax.set_ylabel("y (km)")
    umax = np.hypot(ug, vg).max()
    print(f"{title}: max geostrophic wind {umax:.1f} m/s, f={f:.2e}")
fig.suptitle("Geostrophic wind runs along the isobars: low on the left in the NH, on the right in the SH", fontsize=11, fontweight="semibold", y=0.995)
fig.tight_layout()
save(fig, "fig_cl13_flow_high_low")
