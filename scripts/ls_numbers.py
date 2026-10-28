"""Landscapes numbers used in LS18 (Deccan Traps) and elsewhere.   .venv/bin/python -W ignore scripts/ls_numbers.py"""
import math
print("== Deccan thickness ==")
V = 617700.0
for A in (500000.0, 380000.0):
    print(f"V/A = {V/A:.2f} km (A={A:.0f} km2); cube side {V**(1/3):.1f} km; Mediterranean fraction {V/3.75e6:.3f}")
print("volumes on slide 5:", 193000 + 439000, "vs slide 2:", 617700, f"difference {(193000+439000-617700)/617700*100:.1f} %")
print("\n== cooling time t ~ h^2/kappa, kappa=1e-6 m2/s ==")
for h in (1, 10, 50, 100):
    t = h * h / 1e-6
    print(f"h={h:4d} m: t={t:.2e} s = {t/86400:.0f} d = {t/3.156e7:.2f} yr")
print("\n== thermal stress ==")
E, alpha, dT, nu = 70e9, 8e-6, 900.0, 0.25
print(f"sigma = E alpha dT/(1-nu) = {E*alpha*dT/(1-nu)/1e6:.0f} MPa; ratio to 12 MPa tensile = {E*alpha*dT/(1-nu)/12e6:.0f}")
print("\n== eastward tilt ==")
print(f"1000 m / 700 km = {1000/700:.2f} m/km = {math.degrees(math.atan(1000/700e3)):.3f} deg")
print(f"west coast: 1000 m / 50-100 km = {1000/100:.0f}-{1000/50:.0f} m/km")
print("\n== escarpment retreat 66 Myr ==")
for d in (50, 100):
    print(f"{d} km / 66 Myr = {d*1e6/66e6:.2f} mm/yr")
print("\n== river squeezed from 200 m to 20 m wide, Q = 400 m3/s, U1=1 m/s at d1=2 m, Manning U ~ d^(2/3) ==")
Q, w2 = 400.0, 20.0
d2 = ((Q / w2) / (2 ** (1 / 3) * 1.0 / 2 ** (2 / 3) * 0 + 1) )  # placeholder
# solve w2 * d * (d/2)^(2/3) = Q
lo, hi = 0.1, 50
for _ in range(100):
    m = 0.5 * (lo + hi)
    f = w2 * m * (m / 2) ** (2 / 3) - Q
    lo, hi = (m, hi) if f < 0 else (lo, m)
d2 = 0.5 * (lo + hi); U2 = (d2 / 2) ** (2 / 3)
print(f"d2 = {d2:.2f} m, U2 = {U2:.2f} m/s, shear stress ratio (tau ~ rho g d S) = {d2/2:.1f}, power ratio tau*U = {d2/2*U2:.1f}")

print("\n== aeolian (LS19) ==")
rho_s, rho, g = 2650.0, 1.2, 9.81
for d in (0.1e-3, 0.25e-3, 1e-3):
    ut = 0.1 * math.sqrt((rho_s - rho) / rho * g * d)
    print(f"threshold shear velocity (A=0.1) d={d*1e3:.2f} mm: u*t = {ut:.2f} m/s")
C, D = 1.8, 0.25e-3
for us in (0.3, 0.5, 0.7):
    q = C * rho / g * math.sqrt(0.25e-3 / D) * us ** 3
    print(f"Bagnold flux d=D=0.25 mm, u*={us}: q = {q:.4f} kg/m/s = {q*86400:.0f} kg/m/day")
q = C * rho / g * 0.5 ** 3
for H in (5, 10, 20):
    c = q / (1600 * H)
    print(f"dune H={H} m, q={q:.4f}: c = {c*3.156e7:.0f} m/yr")
print("angle of repose slip-face: tan(34 deg) =", round(math.tan(math.radians(34)), 2))

print("\n== TopoToolbox grid (LS20) ==")
cs = 2.7778e-4; phi = math.radians(18.5)
dy = cs * 111200; dx = cs * 111320 * math.cos(phi)
print(f"cell: dy={dy:.1f} m, dx={dx:.1f} m, area={dx*dy:.0f} m2")
print(f"3038x1459 cells: {3038*cs:.3f} x {1459*cs:.3f} deg = {3038*dy/1e3:.0f} x {1459*dx/1e3:.0f} km; cells={3038*1459}")
print(f"stream fraction = {408148/4431886*100:.1f} %")
for n in (50, 1000):
    print(f"minarea {n}: {n*dx*dy/1e6:.3f} km2")
print(f"Koyna 2376x2496 at 30 m = {2376*30/1e3:.0f} x {2496*30/1e3:.0f} km")
