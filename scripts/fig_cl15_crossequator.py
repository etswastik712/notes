"""CL15 - cross-equatorial low-level flow from a constant meridional pressure gradient on a rotating planet
(Webster & Fasullo 2003, Eqs. 8-10; Suhas 22 Oct p36-39: 'non-rotating vs rotating' panels).

Boundary-layer momentum balance with linear friction (rate alpha):
    du/dt = f v - alpha u ,          dv/dt = G - f u - alpha v ,      G = -(1/rho) dp/dy  (> 0: low pressure to the north)
Steady state:   v = G alpha / (alpha^2 + f^2) ,   u = G f / (alpha^2 + f^2) ,   f = 2 Omega sin(phi).
At the equator f = 0: v = G/alpha, u = 0  (frictional balance, a purely meridional wind).
Illustrative values: 10 hPa over 3000 km, rho = 1.15 kg m-3  ->  G = 2.9e-4 m s-2 ;  alpha = 1/(0.5 day).
"""
from figlib import *

G = 10e2 / (3.0e6 * 1.15)
alpha = 1.0 / (0.5 * 86400)
phi = np.radians(np.linspace(-25, 25, 501))
f = 2 * OMEGA * np.sin(phi)
den = alpha**2 + f**2
v = G * alpha / den
u = G * f / den
print(f"G = {G:.2e} m/s2, alpha = {alpha:.2e} 1/s, v(eq) = {G/alpha:.1f} m/s")
for d in (-20, -10, 0, 10, 20):
    i = np.argmin(abs(np.degrees(phi) - d))
    sp = np.hypot(u[i], v[i])
    ang = (np.degrees(np.arctan2(-u[i], -v[i])) + 360) % 360      # meteorological direction wind blows FROM
    print(f"lat {d:+3d}: u={u[i]:+5.1f} v={v[i]:+5.1f} speed={sp:4.1f} m/s  from {ang:5.1f} deg")

fig, (a, b) = plt.subplots(2, 1, figsize=(7.4, 6.0), gridspec_kw={"height_ratios": [1.2, 1]})
lat = np.degrees(phi)
a.plot(lat, v, color=ORANGE, label="v  (northward)")
a.plot(lat, u, color=BLUE, label="u  (eastward)")
a.axhline(0, color=MUTED, lw=0.8)
a.axvline(0, color=GRID, lw=1)
a.set_ylabel("wind (m s$^{-1}$)")
a.set_title("A steady cross-equatorial flow: south-easterly → southerly → south-westerly", fontsize=10.5)
a.legend(loc="lower right", fontsize=8.5)
a.annotate("friction-dominated:\nflow is purely southerly\n($f\\to0$)", (0, G / alpha), xytext=(-24, 9.2), fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))

b.set_ylim(-1, 1)
b.axis("off")
for d in np.arange(-20, 21, 5):
    i = np.argmin(abs(lat - d))
    b.annotate("", xy=(d + 1.9 * u[i] / 8, 0.0 + 0.55 * v[i] / 12), xytext=(d, 0.0), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.8))
b.text(-24.6, -0.82, "Southern Hemisphere: Coriolis turns the\nflow to the LEFT → south-easterly (trade-like)", fontsize=8.5, va="center")
b.text(24.6, -0.82, "Northern Hemisphere: Coriolis turns the\nflow to the RIGHT → south-westerly monsoon", fontsize=8.5, va="center", ha="right")
b.text(0, 0.88, "equator", ha="center", fontsize=8.5, color=MUTED)
a.set_xlim(-25, 25)
b.set_xlim(-25, 25)
fig.tight_layout()
a.set_xlabel("latitude (°)   [south negative]")
save(fig, "fig_cl15_crossequator")
