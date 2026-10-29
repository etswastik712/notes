"""Numbers for the 'rigour layer' added to existing Landscapes chapters (2026-10-29): LS14 ice-sheet profiles and abrasion.

    .venv/bin/python -W ignore scripts/ls_rigour_numbers.py
"""
import math

import numpy as np
from scipy import integrate

G, RHO_I = 9.81, 917.0
YR = 365.25 * 86400.0


def ok(name, cond):
    print(("  ok   " if cond else "  FAIL ") + name)
    assert cond, name


print("=" * 90 + "\nLS14 rigour layer: ice-sheet profiles and glacial abrasion (A&A Ch. 8, printed pp.234-235, 246-248)\n" + "=" * 90)
# --- plastic ice sheet: tau_b = rho g H dH/dx = C
C = 1e5
k = 2 * C / (RHO_I * G)
print(f"plastic ice sheet: H = sqrt(2 C x/(rho_i g)) = sqrt({k:.2f} m * x): H(100 km) = {math.sqrt(k*1e5):.0f} m, H(400 km) = {math.sqrt(k*4e5):.0f} m, H(750 km) = {math.sqrt(k*7.5e5):.0f} m, H(1500 km) = {math.sqrt(k*1.5e6):.0f} m")
for Hh in (100, 1000, 3000):
    print(f"   surface slope at thickness {Hh} m: dH/dx = C/(rho g H) = {C/(RHO_I*G*Hh):.4f} ({math.degrees(math.atan(C/(RHO_I*G*Hh))):.2f} deg)")
x = np.linspace(1e3, 1e6, 2000)
H = np.sqrt(k * x)
tau = RHO_I * G * H * np.gradient(H, x)
ok("plastic profile has constant basal shear stress C", np.abs(tau[10:-10] / C - 1).max() < 5e-3)
# --- Vialov profile for Glen's law
def vialov(n, A, a, L):
    Gam = 2 * A * (RHO_I * G) ** n / (n + 2)
    H0 = (2 * (a / Gam) ** (1 / n) * L ** ((n + 1) / n)) ** (n / (2 * n + 2))
    return Gam, H0
n, A, a, L = 3, 1e-24, 0.3 / YR, 800e3
Gam, H0 = vialov(n, A, a, L)
print(f"Vialov profile (Glen n=3, A=1e-24 Pa^-3 s^-1, accumulation 0.3 m/yr, half-width 800 km): H0 = {H0:.0f} m; H ~ L^(1/2): H0(L = 200 km) = {vialov(n, A, a, 200e3)[1]:.0f} m")
xs = np.linspace(0.0, L * 0.999, 4001)
Hs = H0 * (1 - (xs / L) ** ((n + 1) / n)) ** (n / (2 * n + 2))
dH = np.gradient(Hs, xs)
q = Gam * Hs ** (n + 2) * np.abs(dH) ** n
resid = np.abs(q[200:-200] / (a * xs[200:-200]) - 1).max()
print(f"   flux balance q = Gam H^(n+2)|H'|^n against a x: max relative residual {resid:.2e} (interior)")
ok("Vialov profile satisfies the flux balance", resid < 2e-3)
for nn in (3, 5, 10, 50):
    r = 0.5
    print(f"   n = {nn:3d}: H/H0 at x/L = 0.5 : {(1 - r ** ((nn + 1) / nn)) ** (nn / (2 * nn + 2)):.4f} (plastic limit sqrt(1-x/L) = {math.sqrt(1 - r):.4f})")
ok("n -> infinity recovers the plastic parabola", abs((1 - 0.5 ** (51 / 50)) ** (50 / 102) - math.sqrt(0.5)) < 0.01)
# --- effective viscosity of ice (Glen): eta = 1/(2 A tau^(n-1))
A0 = 2.4e-24
for t_ in (5e4, 1e5, 2e5):
    print(f"   Glen effective viscosity at tau = {t_/1e3:.0f} kPa (A = 2.4e-24): eta = 1/(2 A tau^2) = {1/(2*A0*t_**2):.2e} Pa s (water: 1e-3)")
# --- Hallet abrasion
for U in (10, 50, 200):
    print(f"   abrasion ~ U_slide^2: relative rate for U = {U} m/yr compared with 50 m/yr: {(U/50)**2:.2f}")
print("\nall checks passed")
