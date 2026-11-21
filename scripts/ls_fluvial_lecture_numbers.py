#!/usr/bin/env python3
"""Numbers for the l_fluvial.pdf lecture additions (LS22, LS23; added 2026-11-21).

Q2/Q3 of slide 43, checked numerically:
  * steady profile of  dz/dt = U - k rho g Q(x) S,  S = -dz/dx,  Q = c x^n  (x from the divide, downstream)
    analytic: S(x) = U/(k rho g c) x^-n   ->   z(x) = z_out + U/(k rho g c (1-n)) (L^(1-n) - x^(1-n))
    checked against a time-stepped upwind run started from a flat plateau.
  * waterfall (step) speed with Q const: an upwind run of dz/dt = -C S, C = k rho g Q, measures C.
Bengal Fan: volume -> mass -> years of Ganga-Brahmaputra supply.
"""
import numpy as np

rho, g = 1000.0, 9.81

# ---------- Q2: steady profile, finite-difference check
L, N = 50e3, 500                       # 50 km river, grid
x = np.linspace(1e3, L, N)             # start 1 km below the divide (channel head)
dx = x[1] - x[0]
n_exp, c = 1.0, 2e-4                   # Q = c x^n  (m^3/s with x in m): Q(50 km) = 10 m^3/s
k = 1e-6                               # erodibility, (m/yr) per (kg m^-3 m s^-2 m^3 s^-1); illustrative, chosen so S(50 km) ~ 0.01; width absorbed
U = 1e-3                               # 1 mm/yr uplift
Q = c * x**n_exp
C = k * rho * g * Q                    # m/yr, the local wave speed
S_an = U / (k * rho * g * c) * x**(-n_exp)
z_an = np.concatenate([[0.0], np.cumsum(0.5 * (S_an[1:] + S_an[:-1]) * dx)])  # integrate upstream from x[0]
z_an = z_an[-1] - z_an                 # z(L) = 0 at the outlet

z = np.zeros(N)                        # flat plateau at base level, then uplift switches on
dt = 0.5 * dx / C.max()
t = 0.0
for _ in range(400000):
    S = np.zeros(N)
    S[:-1] = -(z[1:] - z[:-1]) / dx    # downstream difference (information travels upstream)
    znew = z + dt * (U - C * S)
    znew[-1] = 0.0                     # outlet fixed (base level)
    if np.max(np.abs(znew - z)) < 1e-12 * dt:
        break
    z, t = znew, t + dt
err = np.max(np.abs(z[1:-1] - z_an[1:-1])) / z_an.max()
print(f"Q2 steady profile n=1: relief {z_an.max():.1f} m, max rel. error FD vs analytic {err:.2%}, t_run {t/1e6:.2f} Myr")
print(f"   slope at 5 km {S_an[np.searchsorted(x,5e3)]:.4f}, at 50 km {S_an[-1]:.5f} (ratio {S_an[np.searchsorted(x,5e3)]/S_an[-1]:.1f} = 10^n)")
# inverting for U from a measured slope: U = k rho g Q S
print(f"   inversion check: U = k rho g Q S at 25 km = {k*rho*g*c*25e3*S_an[np.searchsorted(x,25e3)]*1e3:.3f} mm/yr")

# ---------- Q3: waterfall speed with constant Q
Qc = 10.0
Cc = k * rho * g * Qc                  # predicted speed, m/yr
xs = np.linspace(0, 20e3, 4001); dxs = xs[1] - xs[0]
zs = np.where(xs < 15e3, 50.0, 0.0) + 1e-4 * (20e3 - xs)   # 50 m fall at 15 km (x downstream), tiny background slope
pos0 = xs[np.argmax(-np.diff(zs))]
dts = 0.5 * dxs / Cc; T = 0.0
while T < 2e4:
    S = np.zeros_like(zs); S[:-1] = -(zs[1:] - zs[:-1]) / dxs
    zs = zs - dts * Cc * S; zs[-1] = 0.0; T += dts
mid = 0.5 * (zs.max() + zs.min())
pos1 = xs[np.argmin(np.abs(zs[:3000] - (zs[0] + zs[3000]) / 2))]
print(f"Q3 C = k rho g Q = {Cc*1e3:.1f} mm/yr; step moved {(pos0-pos1):.0f} m upstream in {T/1e3:.0f} kyr -> {(pos0-pos1)/T*1e3:.1f} mm/yr")

# ---------- Bengal Fan (slide 29)
V = 12.5e6 * 1e9                       # 12.5 million km^3 in m^3
for rho_b in (1800.0, 2200.0):         # bulk density of compacted fan sediment (assumption)
    M = V * rho_b
    for flux in (700e9, 1e12):         # kg/yr: 700 Mt/yr (slide) and 1 Gt/yr
        print(f"Bengal Fan: rho_b {rho_b:.0f} kg/m^3, mass {M:.2e} kg, at {flux/1e9:.0f} Mt/yr -> {M/flux/1e6:.0f} Myr")
A_fan = 3e6 * 1e6
print(f"   mean thickness = V/A = {V/A_fan/1e3:.1f} km")
