"""CL10 - top-of-atmosphere daily-mean insolation: latitude profiles (left) and latitude-season map (right).

Exact orbital calculation (cl10lib.py): S = 1361 W m-2, obliquity 23.44 deg, eccentricity 0.0167, perihelion ~3 Jan.
Compare Fig. 5.2 of Marshall & Plumb and 7 Oct slide 8.
"""
from cl10lib import *
from figlib import *

lat = np.linspace(-90, 90, 721)
phi = np.radians(lat)

Qno = S0 / np.pi * np.cos(phi)
Qjun = daily_insolation(phi, np.pi / 2)
Qdec = daily_insolation(phi, 3 * np.pi / 2)
Qann = annual_mean(phi)
S2 = legendre_p2_coeff()
Qp2 = S0 / 4 * (1 + S2 * p2(np.sin(phi)))
print(f"S2 = {S2:.4f}  (analytic (5/4)<P2(sin delta)> = {1.25*0.5*(1.5*np.sin(OBL)**2-1):.4f})")
print(f"Q max Dec solstice = {Qdec.max():.0f} at {lat[Qdec.argmax()]:.0f} deg;  Jun = {Qjun.max():.0f} at {lat[Qjun.argmax()]:.0f} deg")
print(f"annual mean: equator {annual_mean(0.0):.0f}, pole {annual_mean(np.pi/2):.0f}, ratio {annual_mean(0.0)/annual_mean(np.pi/2):.2f}; global mean {np.trapezoid(Qann*np.cos(phi),phi)/2:.1f}")
print(f"untilted: S/pi = {S0/np.pi:.0f}")

fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.5), gridspec_kw={"width_ratios": [1.0, 1.15]})
a.axhline(S0 / 4, color=GRID, lw=1.2, label="global mean S/4 = 340")
a.plot(lat, Qno, color=MUTED, ls="--", lw=1.4, label=r"no tilt: $(S/\pi)\cos\varphi$")
a.plot(lat, Qjun, color=ORANGE, label="21 June")
a.plot(lat, Qdec, color=BLUE, label="21 December")
a.plot(lat, Qann, color=INK, lw=2.6, label="annual mean")
a.plot(lat, Qp2, color=AQUA, ls=":", lw=2.2, label=r"$\frac{S}{4}[1+S_2P_2(\sin\varphi)]$, $S_2=-0.477$")
a.plot([lat[Qdec.argmax()]], [Qdec.max()], "o", color=BLUE, ms=5)
a.plot([lat[Qjun.argmax()]], [Qjun.max()], "o", color=ORANGE, ms=5)
a.annotate("summer pole: 559", (-90, Qdec.max()), xytext=(6, 8), textcoords="offset points", fontsize=8, color=INK)
a.annotate("524", (90, Qjun.max()), xytext=(-4, 7), textcoords="offset points", fontsize=8, color=INK, ha="right")
a.annotate("polar night", (88, 15), color=MUTED, fontsize=8, ha="right")
a.set_xlim(-90, 90)
a.set_ylim(0, 700)
a.set_xticks(range(-90, 91, 30))
a.set_xlabel("latitude (°)")
a.set_ylabel("daily-mean insolation  (W m$^{-2}$)")
a.set_title("Insolation by latitude")
a.legend(loc="upper center", fontsize=7.6, ncol=2, columnspacing=1.0, handlelength=1.8)

# right: latitude-season map
days = np.arange(0, 365)
lam = lam_from_day(days)
LL, PP = np.meshgrid(lam, np.radians(np.linspace(-90, 90, 181)))
Qmap = daily_insolation(PP, LL)
cs = b.contourf(days, np.linspace(-90, 90, 181), Qmap, levels=np.arange(0, 600, 40), cmap="YlOrRd", extend="max")
cl = b.contour(days, np.linspace(-90, 90, 181), Qmap, levels=[100, 200, 300, 400, 500], colors=INK, linewidths=0.6)
b.clabel(cl, fmt="%d", fontsize=7)
b.contour(days, np.linspace(-90, 90, 181), Qmap, levels=[0.5], colors=INK, linewidths=1.4, linestyles="--")
b.set_xticks([15, 74, 166, 258, 349])
b.set_xticklabels(["Jan", "Mar 20", "Jun 21", "Sep 22", "Dec 21"], fontsize=8)
b.set_yticks(range(-90, 91, 30))
b.set_ylabel("latitude (°)")
b.set_title("Season × latitude: polar night (dashed) and midnight sun")
b.grid(False)
cb = fig.colorbar(cs, ax=b, pad=0.02, fraction=0.05)
cb.set_label("W m$^{-2}$")
fig.tight_layout()
save(fig, "fig_cl10_insolation")
