"""CL11 - Held-Hou (1980) model of the Hadley cell: equal-area construction and how the edge scales with rotation.

Setup (small-angle, y = a*phi), following Vallis, AOFD, Ch. 11.2 (derivation re-done in the chapter):
  radiative-equilibrium temperature   theta_E(phi) = theta_E0 - Dtheta * phi^2
  angular-momentum-conserving cell    theta_M(phi) = theta(0) - theta0 * Omega^2 a^2 phi^4 / (2 g H)
  continuity at the edge and no net heating in the cell  =>  phi_H = sqrt(5R/3),  R = g H Dtheta / (theta0 Omega^2 a^2)
Example parameters (Vallis Fig. 11.6): theta_E0 = 303 K, Dtheta = 50 K, theta0 = 300 K, Omega = 7.272e-5, H = 10 km  ->  R = 0.076, phi_H = 20.4 deg.
"""
from scipy.integrate import quad
from scipy.optimize import brentq

from figlib import *

a_, g = R_EARTH, G0
th0, tE0, Dth, Om, H = 300.0, 303.0, 50.0, 7.272e-5, 1.0e4


def solve(H=H, Om=Om, Dth=Dth):
    k = th0 * Om**2 * a_**2 / (2 * g * H)
    thE = lambda x: tE0 - Dth * x**2
    def f(x0):
        t0 = thE(x0) + k * x0**4
        return quad(lambda x: (t0 - k * x**4) - thE(x), 0, x0)[0]
    x = brentq(f, 1e-3, 1.5)
    R = g * H * Dth / (th0 * Om**2 * a_**2)
    return x, np.sqrt(5 * R / 3), R, k


xh, xh_formula, R, k = solve()
t0 = tE0 - Dth * xh**2 + k * xh**4
print(f"R={R:.4f}; numeric edge {np.degrees(xh):.2f} deg; formula sqrt(5R/3) {np.degrees(xh_formula):.2f} deg; theta(0)={t0:.2f} K; "
      f"theta_E0 - 5/18 R Dtheta = {tE0-5/18*R*Dth:.2f} K; u_M(edge) = {Om*a_*xh**2:.1f} m/s")

phi = np.linspace(0, 0.8, 400)
thE = tE0 - Dth * phi**2
thM = t0 - k * phi**4

fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 4.2), gridspec_kw={"width_ratios": [1.15, 1]})
d = np.degrees(phi)
a.plot(d, thE, color=MUTED, ls="--", label="radiative equilibrium $\\theta_E$")
m = phi <= xh
a.plot(d[m], thM[m], color=ORANGE, label="circulation: $\\theta_M$ (angular-momentum conserving)")
a.plot(d[~m], thE[~m], color=ORANGE, lw=2.2)
a.fill_between(d[m], thM[m], thE[m], where=thM[m] >= thE[m], color=RED, alpha=0.25, lw=0)
a.fill_between(d[m], thM[m], thE[m], where=thM[m] <= thE[m], color=BLUE, alpha=0.25, lw=0)
a.axvline(np.degrees(xh), color=MUTED, lw=0.8, ls=":")
a.annotate(f"edge {np.degrees(xh):.1f}°", (np.degrees(xh), thE[m][-1]), xytext=(6, 6), textcoords="offset points", fontsize=9)
a.annotate("equal areas:\ncell neither heats\nnor cools the air", (8, 292), fontsize=8.5, ha="left", va="center")
a.set_xlabel("latitude (°)")
a.set_ylabel("potential temperature (K)")
a.set_title("(a) equal-area construction")
a.legend(loc="lower left", fontsize=8.2)

Oms = np.linspace(0.2, 3.0, 300)
for Hh, c, lab in ((1e4, ORANGE, "H = 10 km"), (1.5e4, BLUE, "H = 15 km")):
    Rr = g * Hh * Dth / (th0 * (Oms * 7.2921159e-5) ** 2 * a_**2)
    edge = np.degrees(np.sqrt(5 * Rr / 3)); edge[edge > 90] = np.nan
    b.plot(Oms, edge, color=c, label=lab)
b.plot([1], [np.degrees(xh_formula)], "o", color=ORANGE, ms=6)
b.annotate("Earth", (1, np.degrees(xh_formula)), xytext=(8, 8), textcoords="offset points", fontsize=9)
b.axhline(90, color=GRID, lw=1)
b.set_ylim(0, 95)
b.set_xlim(0.2, 3.0)
b.set_xlabel("rotation rate  $\\Omega/\\Omega_{\\rm Earth}$")
b.set_ylabel("Hadley-cell edge (°)")
b.set_title("(b) $\\phi_H\\propto 1/\\Omega$: slower rotation, wider cell")
b.legend(loc="upper right", fontsize=8.5)
fig.tight_layout()
save(fig, "fig_cl11_held_hou")
