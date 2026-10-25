"""CL13 - force balance in the free atmosphere (two-way, geostrophic) and in the planetary boundary layer (three-way, with friction).

NH, low pressure to the north (top).  PGF points north.  Free atmosphere: V_g flows east, Coriolis (to the right = south) cancels the PGF.
PBL: friction F = -kappa V_s opposes the wind.  Steady balance PGF + CF + F = 0 gives tan(psi) = kappa/f and |V_s| = |V_g| cos(psi):
the wind is subgeostrophic and blows across the isobars toward low pressure at angle psi.
"""
from figlib import *

f = 2 * OMEGA * np.sin(np.radians(45))
P = 1.11e-3                       # PGF per unit mass, m s-2 (4 hPa per 300 km at rho = 1.2)
psi = np.radians(30)
kappa = f * np.tan(psi)
Vg = P / f
Vs = Vg * np.cos(psi)
V = Vs * np.array([np.cos(psi), np.sin(psi)])
pgf = np.array([0, P])
cf = f * Vs * np.array([np.sin(psi), -np.cos(psi)])          # f k x V -> to the right of V
fr = -kappa * V
print(f"V_g = {Vg:.2f} m/s, V_s = {Vs:.2f} m/s ({Vs/Vg:.3f} V_g), kappa = {kappa:.2e} s-1, cross-isobar component = {Vs*np.sin(psi):.2f} m/s")
print("closure |PGF+CF+F| =", np.hypot(*(pgf + cf + fr)))
assert np.hypot(*(pgf + cf + fr)) < 1e-12

fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 4.6))
sc = 1.0 / P


def arrow(ax, v, c, lab, off=(6, 0), ls="-", lw=2.4, origin=(0, 0), ha="left"):
    ax.annotate("", xy=(origin[0] + v[0] * sc, origin[1] + v[1] * sc), xytext=origin, arrowprops=dict(arrowstyle="-|>", color=c, lw=lw, ls=ls, shrinkA=0, shrinkB=0))
    ax.annotate(lab, (origin[0] + v[0] * sc, origin[1] + v[1] * sc), xytext=off, textcoords="offset points", fontsize=9, color=INK, ha=ha, va="center")


for ax in (a, b):
    for yy in (-1.2, -0.6, 0.6, 1.2):           # isobars (straight, east-west)
        ax.axhline(yy, color=GRID, lw=1.6, zorder=0)
    ax.text(-1.4, 1.3, "low pressure", fontsize=8.5, color=MUTED)
    ax.text(-1.4, -1.38, "high pressure", fontsize=8.5, color=MUTED)
    ax.plot([0], [0], "o", color=INK, ms=6, zorder=5)
    ax.set_xlim(-1.5, 1.6); ax.set_ylim(-1.5, 1.5); ax.set_aspect("equal"); ax.axis("off")

a.set_title("Free atmosphere: PGF and Coriolis balance", fontsize=10)
arrow(a, pgf, RED, "PGF\n(toward low)", off=(8, 0))
arrow(a, np.array([0, -P]), VIOLET, "Coriolis", off=(8, 0))
a.annotate("", xy=(1.3, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.6, shrinkA=0, shrinkB=0))
a.annotate("geostrophic wind $V_g$\n(low on the left)", (1.3, 0), xytext=(0, 12), textcoords="offset points", ha="center", fontsize=9)

b.set_title("Boundary layer: three-way balance with friction", fontsize=10)
arrow(b, pgf, RED, "PGF", off=(8, 0))
arrow(b, cf, VIOLET, "Coriolis", off=(8, 0))
arrow(b, fr, ORANGE, "friction", off=(-6, -8), ha="right")
Wv = 1.3 * (Vs / Vg) * np.array([np.cos(psi), np.sin(psi)])
b.annotate("", xy=(Wv[0], Wv[1]), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.6, shrinkA=0, shrinkB=0))
b.annotate("wind $V_s<V_g$,\nacross the isobars\ntoward low pressure", (Wv[0], Wv[1]), xytext=(6, 6), textcoords="offset points", fontsize=8.5)
b.annotate("", xy=(Vg * sc * 0 + 1.3, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.2, ls="--", shrinkA=0, shrinkB=0))
b.annotate("$V_g$ (dashed)", (1.3, 0), xytext=(0, -14), textcoords="offset points", ha="center", fontsize=8.5, color=MUTED)
arc = np.linspace(0, psi, 30)
b.plot(0.55 * np.cos(arc), 0.55 * np.sin(arc), color=INK, lw=1)
b.annotate("ψ ≈ 30°", (0.62, 0.12), fontsize=8.5)
fig.suptitle("NH, low pressure to the north: friction turns the wind toward low pressure and slows it", fontsize=11, fontweight="semibold", y=1.0)
fig.tight_layout()
save(fig, "fig_cl13_force_triangles")
