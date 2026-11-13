"""CL24: numbers and figure for the momentum ledger (Joy O3/O4).  .venv/bin/python -I scripts/fig_cl24.py"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa

rho, f0, tau0, g = 1025.0, 1e-4, 0.1, 9.81
YR = 365.25 * 86400
print("Ekman transport tau/(rho f) = %.2f m2/s ; over 50 m: %.1f cm/s" % (tau0 / (rho * f0), 100 * tau0 / (rho * f0) / 50))
print("air/water density %.0f ; rho c v: air %.2e water %.2e ratio %.0f ; heat per m3 per K ratio %.0f" % (1025 / 1.2, 1.2 * 1005 * 10, 1025 * 4000 * 0.1, 1025 * 4000 * 0.1 / (1.2 * 1005 * 10), 1025 * 4000 / (1.2 * 1005)))
a = tau0 / (rho * 50)
print("acceleration tau/(rho H) = %.2e m/s2 ; time to 10 m/s %.0f days ; to 0.1 m/s %.1f h" % (a, 10 / a / 86400, 0.1 / a / 3600))
print("1/f at f=1e-4: %.1f h ; Rossby number 0.1/(f L) with L=1000 km: %.0e ; Re = U L/nu = %.0e" % (1 / f0 / 3600, 0.1 / (f0 * 1e6), 0.1 * 1e6 / 1e-6))
w = tau0 / (rho * f0 * 1.5e6)
print("Ekman pumping scale w = %.2e m/s = %.1f m/yr" % (w, w * YR))
print("geostrophic speed (g/f) slope: 1 m / 1500 km %.1f cm/s ; 1 m / 100 km %.2f m/s" % (100 * g / f0 / 1.5e6, g / f0 / 1e5))
print("Stewart 9.16 Ekman depth D_E = 7.6 U/sqrt(sin phi):", {(U, lat): round(7.6 * U / math.sqrt(math.sin(math.radians(lat)))) for U in (5, 10, 20) for lat in (15, 45)})
print("Chereskin-Roemmich 11N: measured 12.0+-5.5, winds-now 8.8+-1.9, mean winds 13.5+-0.3 Sv (Stewart p.144)")
print("exp(-pi) = %.3f ; ACC 125 Sv = %.2e m3/s" % (math.exp(-math.pi), 125e6))
print("Ekman number at D_E: 1/(2 pi^2) = %.3f" % (1 / (2 * math.pi ** 2)))

fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.5))
# A: idealised wind stress -> transport -> pumping
lat = np.linspace(-60, 60, 601); phi = np.deg2rad(lat); f = 2 * 7.292e-5 * np.sin(phi)
tx = -0.1 * np.cos(3 * phi)                                  # idealised: trades (-) and westerlies (+), zero at 30 degrees
My = np.where(abs(lat) > 6, -tx / (rho * f), np.nan)          # m2/s
dy = np.deg2rad(lat[1] - lat[0]) * 6.371e6
q = tx / (rho * np.where(abs(f) > 1e-5, f, np.nan))
wv = -np.gradient(q, dy) * YR                                 # m/yr, w at base of Ekman layer = curl_z(tau/rho f)
a1 = ax[0]
a1.plot(lat, tx * 10, color=BLUE, lw=2, label="zonal wind stress τₓ (×10, N m⁻²)")
a1.plot(lat, np.clip(My, -4, 4), color=ORANGE, lw=2, label="northward Ekman transport M_y (m² s⁻¹)")
a1.set_ylim(-4, 4); a1.axhline(0, color="#888", lw=.6); a1.set_xlabel("latitude (°)")
a2 = a1.twinx(); a2.plot(lat, np.clip(wv, -80, 80), color=AQUA, lw=2, label="Ekman pumping w (m yr⁻¹)"); a2.set_ylim(-80, 80); a2.set_ylabel("w (m yr⁻¹)", color=AQUA)
h1, l1 = a1.get_legend_handles_labels(); h2, l2 = a2.get_legend_handles_labels(); a1.legend(h1 + h2, l1 + l2, fontsize=7.2, frameon=False, loc="upper left")
a1.set_title("A  idealised winds → transport → pumping", fontsize=9.8)
# B: Ekman spiral hodograph
b = ax[1]
Dz = 1.0; az = math.pi / Dz
z = np.linspace(0, Dz, 400)
u = np.exp(-az * z) * np.cos(math.pi / 4 - az * z); v = np.exp(-az * z) * np.sin(math.pi / 4 - az * z)   # z = depth below surface; wind blows to +y (north); Stewart 9.9 with z_up = -z
b.plot(u, v, color=BLUE, lw=2)
for k in (0, 100, 200, 300):
    b.annotate("", xy=(u[k], v[k]), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.0))
Mx, My_ = np.trapezoid(u, z) * az, np.trapezoid(v, z) * az   # M a / V0
b.annotate("", xy=(Mx * 1.0, My_ * 1.0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2))
b.annotate("", xy=(0, 1.0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.0))
b.text(0.03, 0.93, "wind stress", fontsize=8.5); b.text(Mx * 0.55, -0.12, "net transport (90° right)", fontsize=8.5, color=ORANGE, ha="center")
b.text(0.5, 0.78, "surface current,\n45° right of wind", fontsize=8.2, color=BLUE)
b.text(0.55, 0.10, "turns right,\nweakens with depth", fontsize=8, color=BLUE)
b.set_aspect("equal"); b.set_xlim(-0.35, 1.0); b.set_ylim(-0.15, 1.1); b.set_xlabel("eastward"); b.set_ylabel("northward")
b.set_title("B  Ekman spiral (constant viscosity), N. hemisphere", fontsize=9.8)
print("hodograph check: net transport angle from wind = %.1f deg to the right; |M| = %.3f V0/a (exact value over the full depth 1/sqrt2 = 0.707; the 0.03 excess is the cut-off at D_E)" % (math.degrees(math.atan2(Mx, My_)), math.hypot(Mx, My_)))
# C: geostrophic speed
c = ax[2]
s = np.logspace(-8.2, -3.3, 200)
for lat0, col in ((15, AQUA), (35, BLUE), (60, ORANGE)):
    c.loglog(s, g / (2 * 7.292e-5 * math.sin(math.radians(lat0))) * s, color=col, lw=2, label="%d° latitude" % lat0)
c.plot([1 / 1.5e6], [g / f0 / 1.5e6], "o", color=INK); c.text(1.2 / 1.5e6, g / f0 / 1.5e6 * 0.55, "1 m over 1,500 km\n≈ 7 cm/s (gyre interior)", fontsize=8)
c.plot([1 / 1e5], [g / f0 / 1e5], "o", color=INK); c.text(0.25 / 1e5, g / f0 / 1e5 * 1.5, "1 m over 100 km\n≈ 1 m/s (Gulf Stream)", fontsize=8)
c.set_xlabel("sea-surface slope"); c.set_ylabel("surface geostrophic speed u = (g/f) slope  (m s⁻¹)"); c.legend(fontsize=8, frameon=False, loc="upper left")
c.set_title("C  steep slopes ⇒ fast, narrow currents", fontsize=9.8)
fig.subplots_adjust(wspace=0.32)
save(fig, "fig_cl24_momentum")
