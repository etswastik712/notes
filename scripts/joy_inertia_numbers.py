"""Numbers behind Joy's O2/O3 'how much of the surface feels the weather' lectures (CL23).
   .venv/bin/python -I scripts/joy_inertia_numbers.py"""
import gzip
import json
import math
import os

import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DAY, YR = 86400.0, 365.25 * 86400.0
RHOC_S, RHOC_W = 2.0e6, 4.2e6      # moist soil / water, J m-3 K-1 (slide: moist soil ~2e6)

print("=== conduction depth d = sqrt(2 kappa / omega); slab equivalent C = rho c d / sqrt(2) in metres of water")
for per, nm in ((DAY, "day"), (YR, "year")):
    om = 2 * math.pi / per
    row = []
    for kap in (0.3e-6, 0.5e-6, 1.0e-6):
        d = math.sqrt(2 * kap / om)
        slab_w = RHOC_S * d / math.sqrt(2) / RHOC_W
        row.append("kappa=%.1e: d=%.3g m, slab=%.3g m water" % (kap, d, slab_w))
    print(nm, " | ".join(row))
    d = math.sqrt(2 * 1.4e-7 / om); print("   still water kappa=1.4e-7:", "d=%.3g m, slab=%.3g m water" % (d, RHOC_W * d / math.sqrt(2) / RHOC_W))
print("Hartmann (4.10) without the factor 2: day %.1f cm year %.2f m (kappa 0.5e-6)" % (100 * math.sqrt(0.5e-6 / (2 * math.pi / DAY)), math.sqrt(0.5e-6 / (2 * math.pi / YR))))
print("sqrt(365) = %.1f" % math.sqrt(365))

print("=== eddy-diffusive reach below the mixed layer d = sqrt(2K/omega), K = 1e-5 / 1e-4 m2/s")
for yrs in (1, 10, 100):
    om = 2 * math.pi / (yrs * YR)
    print("%3d yr: %.0f m / %.0f m" % (yrs, math.sqrt(2 * 1e-5 / om), math.sqrt(2 * 1e-4 / om)))

print("=== tau = C / lambda, lambda = 3.8 (Planck, Argha) ; C in metres of water")
for lab, m in (("land (year swing)", 1.0), ("whole atmosphere", 2.4), ("mixed layer", 50.0), ("full ocean", 4000.0)):
    t = m * RHOC_W / 3.8
    print("%-18s %6.1f m water: tau = %.1f d = %.2f yr" % (lab, m, t / DAY, t / YR))
b = 2.09
CL, CM, CD, GAM = 1.0e7, 4.2e6 * 75, 4.2e9, 0.7
print("app values (b=2.09): tau_land %.1f d, tau_mixed %.2f yr, tau_deep %.0f yr ; C_m/C_L = %.1f -> (C_m/C_L)^2 = %.0f" % (CL / b / DAY, CM / b / YR, CD / GAM / YR, CM / CL, (CM / CL) ** 2))
print("   bend period 2 pi tau: land %.2f yr, mixed %.1f yr ; deep period %.0f yr" % (2 * math.pi * CL / b / YR, 2 * math.pi * CM / b / YR, 2 * math.pi * CD / GAM / YR))

print("=== weather-kicked slab: |T|^2/|F|^2 = 1/|Z|^2 ; ratios mixed/land and deep/land at several periods (white forcing, b=2.09)")
def Zland(om): return 1j * om * CL + b
def Zmix(om): return 1j * om * CM + b
def Zdeep(om):  # mixed layer losing heat to a deep reservoir: gamma * i om Cd / (i om Cd + gamma)
    return 1j * om * CM + b + GAM * (1j * om * CD) / (1j * om * CD + GAM)
for per_yr in (0.1, 0.5, 1, 2, 6, 30, 100, 300, 1000):
    om = 2 * math.pi / (per_yr * YR)
    rl = abs(Zland(om)) ** 2 / abs(Zmix(om)) ** 2
    rd = abs(Zland(om)) ** 2 / abs(Zdeep(om)) ** 2
    print("period %7.1f yr: P_mixed/P_land = %.4f (1/%.0f) ; P_deep/P_land = %.2f" % (per_yr, rl, 1 / rl, rd))
print("slow limit deep/land = (b/(b+gamma))^2 = %.2f" % ((b / (b + GAM)) ** 2))

print("=== seasonal swing of a slab driven by +-30% sun (Q=342*1.05=359.1): amplitude F/|Z|, phase lag atan(omega C / b)")
om = 2 * math.pi / YR
Q = 342 * 1.05
for lab, C, A in (("land", CL, 0.32), ("mixed layer (alone)", CM, 0.28)):
    F = 0.3 * Q * (1 - A)
    Z = complex(b, om * C)
    print("%-20s F=%.1f W/m2, range (peak to peak) %.1f K, lag %.1f deg = %.1f months" % (lab, F, 2 * F / abs(Z), math.degrees(math.atan(om * C / b)), math.degrees(math.atan(om * C / b)) / 360 * 12))

print("=== observed seasonal range of surface T from CERES upwelling LW (2010-2024 climatology on the 2-degree grid; Joy used 2010-2020)")
D = os.path.join(ROOT, "earth-and-climate/climate/lecture-notes-slides/joy_intro_climate_science/tutorials/ceres-energy-budget/assets/data")
meta = json.load(open(f"{D}/meta.json")); lat = np.array(meta["lat"]); lon = np.array(meta["lon"])
def clim(b):
    raw = gzip.decompress(open(f"{D}/ceres.zarr/clim/{b}/c/0/0/0", "rb").read())
    a = np.frombuffer(raw, dtype="<i2").reshape(12, 90, 180).astype(float); a[a == -32768] = np.nan
    return a * 0.1
Ts = (clim("sfc_lw_up_all") / 5.670374e-8) ** 0.25
def cell(la, lo): return int(round((la + 89) / 2)), int(round(((lo % 360) - 1) / 2))
def box(la0, la1, lo0, lo1):
    i0, j0 = cell(la0, lo0); i1, j1 = cell(la1, lo1); return Ts[:, i0:i1 + 1, j0:j1 + 1].mean((1, 2))
for nm, (la, lo), joy in (("Yakutsk", (62.0, 129.7), 57), ("Almaty", (43.2, 76.9), 35), ("Delhi", (28.6, 77.2), 23), ("Pune", (18.5, 73.9), 9), ("Mumbai", (19.1, 72.9), 5)):
    i, j = cell(la, lo); s = Ts[:, i, j]; print("%-9s %.0f K (slide %d K)" % (nm, s.max() - s.min(), joy))
s = box(10, 20, 60, 70); print("Arabian Sea box 10-20N 60-70E: %.1f K (slide 5 K); warmest month %d, coldest %d" % (s.max() - s.min(), int(s.argmax()) + 1, int(s.argmin()) + 1))
s = box(-2, 2, 180, 270); print("Equatorial Pacific box (2S-2N, 180-270E): %.1f K (slide 2 K)" % (s.max() - s.min()))
s = box(10, 20, 60, 70); print("Arabian Sea monthly mean T (C):", np.round(s - 273.15, 1))
