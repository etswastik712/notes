"""CL12 - the same Coriolis physics in the two hemispheres, and how strongly it acts at each latitude.

(a, b) A parcel with no pressure force, launched northward at t=0 on the local tangent plane, obeys
         du/dt = f v,   dv/dt = -f u,     f = 2 Omega sin(phi).
       Northern Hemisphere (f > 0): the path is a clockwise circle, i.e. it bends to the RIGHT of the motion.
       Southern Hemisphere (f < 0): an anticlockwise circle, bends to the LEFT.  Radius U/|f|, period 2 pi/|f|.
       (On the rotating Earth this works because the surface has bulged to cancel the centrifugal force; M&P's
        parabolic rotating table does the same in the lab.)
(c) f(phi) and the inertial period 2 pi/f: at 30 deg the period equals one sidereal day (f = Omega).
"""
from figlib import *

U = 10.0   # m s-1


def path(phi_deg, n=400):
    f = 2 * OMEGA * np.sin(np.radians(phi_deg))
    T = 2 * np.pi / abs(f)
    t = np.linspace(0, T, n)
    # u(0)=0, v(0)=U :  u = U sin(f t), v = U cos(f t)
    x = U / f * (1 - np.cos(f * t))
    y = U / f * np.sin(f * t)
    return t, x / 1e3, y / 1e3, T / 3600


fig, axs = plt.subplots(1, 3, figsize=(11.2, 3.9), gridspec_kw={"width_ratios": [1, 1, 1.15]})
for ax, phi, name, c in [(axs[0], 45, "Northern Hemisphere, 45° N", BLUE), (axs[1], -45, "Southern Hemisphere, 45° S", ORANGE)]:
    t, x, y, Th = path(phi)
    ax.plot(x, y, color=c)
    for k in range(0, len(t), 50):
        ax.plot(x[k], y[k], "o", color=INK, ms=3)
    # velocity arrows along the path
    for k in (30, 130, 230, 330):
        dx, dy = x[k + 1] - x[k - 1], y[k + 1] - y[k - 1]
        ax.annotate("", xy=(x[k] + dx * 3, y[k] + dy * 3), xytext=(x[k], y[k]), arrowprops=dict(arrowstyle="-|>", color=c, lw=1.8))
    ax.plot([0], [0], "s", color=INK, ms=6)
    ax.annotate("start,\nlaunched north", (0, 0), xytext=(8, -20) if phi > 0 else (-8, -20), textcoords="offset points", ha="left" if phi > 0 else "right", fontsize=8)
    ax.set_aspect("equal")
    ax.set_xlim((-30, 225) if phi > 0 else (-225, 30))
    ax.set_ylim(-105, 105)
    ax.set_xlabel("east (km)")
    ax.set_title(name + "\nbends to the " + ("right" if phi > 0 else "left"), fontsize=10)
    ax.annotate(f"period {Th:.1f} h\nradius {U/abs(2*OMEGA*np.sin(np.radians(phi)))/1e3:.0f} km", (0.5, 0.5), xycoords="axes fraction", ha="center", va="center", fontsize=8.5, color=MUTED)
axs[0].set_ylabel("north (km)")

ax = axs[2]
lat = np.linspace(0.5, 90, 300)
f = 2 * OMEGA * np.sin(np.radians(lat))
ax.plot(lat, f * 1e4, color=INK)
ax.set_xlabel("latitude (°)")
ax.set_ylabel(r"Coriolis parameter  $f=2\Omega\sin\varphi$  ($10^{-4}$ s$^{-1}$)")
ax.set_ylim(0, 1.7)
for d in (10, 30, 45, 60, 90):
    ff = 2 * OMEGA * np.sin(np.radians(d))
    ax.plot([d], [ff * 1e4], "o", color=INK, ms=4)
    ax.annotate(f"{2*np.pi/ff/3600:.0f} h", (d, ff * 1e4), xytext=(0, -14), textcoords="offset points", ha="center", fontsize=8, color=MUTED)
ax.annotate("labels: inertial period $2\\pi/f$", (4, 1.52), fontsize=8.5, color=MUTED)
ax.annotate("at 30° $f=\\Omega$: period = one sidereal day", (30, OMEGA * 1e4), xytext=(32, 0.38), textcoords="data", fontsize=8,
            arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
ax.set_title("Weak at the equator, strongest at the poles", fontsize=10)
fig.tight_layout()
save(fig, "fig_cl12_hemispheres")
