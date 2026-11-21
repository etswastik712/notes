#!/usr/bin/env python3
"""Numbers for the 2022 EC2223 'Landscapes and Their Evolution' mid-sem and quizzes (found on Drive 2026-11-21).
Run: .venv/bin/python -I scripts/ls_pastpapers_2022_numbers.py"""
import numpy as np
from math import pi, log, exp
G = 6.7e-11; g0 = 9.8
print("=== Quiz 1 (paper's numbers: R=6400 km, r_c=3000 km, rho=5000, rho_c=10000, G=6.7e-11)")
w = 2 * pi / 86164.0
print(f"Q1 omega = 2pi/sidereal day = {w:.3e} rad/s  (2pi/86400 = {2*pi/86400:.3e})")
R, rc, rho, rhoc = 6.4e6, 3.0e6, 5000.0, 1.0e4
g = 4 / 3 * pi * G * rho * R
print(f"Q2 g(equator) from the numbers = {g:.2f} m/s^2; omega^2 R / g = {w*w*R/g:.3e} (with g = 9.8: {w*w*R/9.8:.3e} = 1/{9.8/(w*w*R):.0f}); at the pole 0")
f_now = 0.00335
print(f"Q3 f scales as omega^2: (24/19)^2 = {(24/19)**2:.3f}; f then = {f_now*(24/19)**2:.5f} = 1/{1/(f_now*(24/19)**2):.0f}"
      f"; slide formula rho_bar w^2 R/(2 g rho_s) with rho_s = 2700: now {rho*w*w*R/(2*g*2700):.5f}, then {rho*(w*24/19)**2*R/(2*g*2700):.5f}")
gc = 4 / 3 * pi * G * rhoc * rc
qc = w * w * rc / gc
print(f"Q4 core: g_c = {gc:.2f} m/s^2, q_c = w^2 r_c / g_c = {qc:.3e}; slide formula (homogeneous core, rho_bar = rho_s) f_c = q_c/2 = {qc/2:.2e};"
      f" Maclaurin homogeneous fluid f = 5q/4 = {1.25*qc:.2e}")
print("=== Quiz 2")
rc_, rm = 2.5, 3.0
fb = 1 - rc_ / rm
T1, T2 = 1 / fb, 0.5 / fb            # thicknesses (in units of h) of blocks with freeboard h and h/2
T1e = T1 - 0.5
print(f"Q1 freeboard fraction {fb:.4f}; thicknesses {T1:.2f}h, {T2:.2f}h; after eroding h/2: freeboard {T1e*fb:.4f}h; final difference {T1e*fb-0.5:.4f}h = 5h/12 = {5/12:.4f}h")
print("Q2 1 m cube, 6 m^2; 5 parallel cuts (6 slabs): 6+10 = 16 m^2 -> x2.67; cuts 1 + 2 in two directions (2x3 blocks): 6+6 = 12 m^2 -> x2.00")
lam = 0.693 / 6930
for label, off in [("reservoir age = residence time", 1000.0), ("well-mixed box, N_ocean = N_atm/(1+lam*tau)", log(1 + lam * 1000) / lam)]:
    print(f"Q3 {label}: offset {off:.0f} yr; apparent age {5000+off:.0f} yr; ratio {(5000+off)/5000:.3f}")
U, D, L = 1e-4, 0.005, 100.0
print(f"Q4 steady h = U(L^2-x^2)/(2D): relief = U L^2/(2D) = {U*L*L/(2*D):.1f} m")
print("=== Mid-sem")
print("Q3 unit cube: sigma_n on the 45-degree diagonal = sigma1 + dsigma/2, tau = dsigma/2 (Mohr circle, 2theta = 90)")
for H in (35e3,):
    thick = 0.03 * H / 200e3
    print(f"Q4 thickening = v H / W = 0.03 m/yr x 35 km / 200 km = {thick*100:.3f} cm/yr; isostatic surface uplift x(1 - rho_c/rho_m) = x{1-2.7/3.3:.3f} -> {thick*(1-2.7/3.3)*1000:.2f} mm/yr")
for rho_i, rho_m in ((917, 3300), (1000, 3300)):
    print(f"Q6b rebound = (rho_i/rho_m) x 2.5 km with rho_i={rho_i}: {rho_i/rho_m*2.5:.2f} km")
mu, rho_r, h, A, slip = 0.05, 2700, 8e3, 100e3 * 50e3, 2.0
sn = rho_r * g0 * h
F = mu * sn * A
print(f"Q7 sigma_n = rho g h = {sn:.3e} Pa; A = {A:.1e} m^2; F = mu sigma_n A = {F:.2e} N; E = F x slip = {F*slip:.2e} J")
print(f"   instructor's rough sheet: 500e6 m^2 -> F = {mu*sn*5e8:.1e} N, E = {mu*sn*5e8*2:.1e} J (area off by 10)")
Mw = 7.8
Es = 10 ** (1.5 * Mw + 4.8)
print(f"   radiated seismic energy for Mw 7.8 (Gutenberg-Richter log E = 1.5M + 4.8): {Es:.1e} J -> fraction of frictional heat {Es/(F*slip):.2f}")
for rho_a, depth in ((5000, 2.9e6), (5000, 3.0e6), (4500, 2.9e6)):
    print(f"Q8b P = rho g h, rho={rho_a}, h={depth/1e3:.0f} km: {rho_a*g0*depth/1e9:.0f} GPa (PREM: 136 GPa)")
