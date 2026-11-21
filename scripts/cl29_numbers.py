#!/usr/bin/env python3
"""Numbers for CL26 addendum (O6 notes questions) and CL29 (O7: ENSO, carbon). Added 2026-11-21.  .venv/bin/python -I scripts/cl29_numbers.py"""
import numpy as np
print("=== O6 Q2: deep-ocean volume from turnover x sinking rate")
yr = 3.156e7
for Sv in (15, 20, 25, 30):
    V = Sv * 1e6 * 1000 * yr
    print(f"  {Sv} Sv x 1000 yr = {V:.2e} m^3 = {V/1.3e18:.0%} of the ocean")
print("=== O6 Q3: Joy's dimensionless Stommel, y|1-y| = E (on state y<1/2, overturning 1-y)")
for E in (0.15, 0.2, 0.24, 0.25):
    y_on = (1 - np.sqrt(1 - 4 * E)) / 2; y_un = (1 + np.sqrt(1 - 4 * E)) / 2; y_rev = (1 + np.sqrt(1 + 4 * E)) / 2
    print(f"  E={E}: on y={y_on:.3f} (q={1-y_on:.3f}), unstable y={y_un:.3f}, reversed y={y_rev:.3f} (q={1-y_rev:.3f})")
print("  drop approaching the edge 0.82 -> 0.50; jump at the edge 0.50 -> -0.21")
print("=== O6 §6: Stewart's Atlantic heat sum")
rc = 1025 * 3990
print(f"  14 Sv x (18-2) K x rho c_p = {14e6*16*rc/1e15:.2f} PW (Stewart ~0.9; careful estimate 1.2 +/- 0.2)")
print("  mean deep flow for a 1000-yr round trip of ~30,000 km:", f"{3e7/(1000*yr)*1e3:.2f} mm/s (Stewart ~1 mm/s)")
print("=== O7 Q1: white noise moving average")
rng = np.random.default_rng(0); x = rng.standard_normal(10000)
for w in (25, 50, 100, 200, 400):
    m = np.convolve(x, np.ones(w) / w, mode="valid")
    print(f"  window {w}: std {m.std():.4f} (1/sqrt(w) = {1/np.sqrt(w):.4f})")
print("=== O7 Q2: energy of a 5 K anomaly over 1000 km x 1000 km")
A = 1e12
for H in (20, 100):
    E = rc * H * A * 5
    print(f"  H={H} m: {E:.2e} J")
S = 400 * A * 30 * 86400
print(f"  sunlight absorbed in a month at ~400 W/m^2 (tropical surface mean, assumed): {S:.2e} J  -> ratios {rc*20*A*5/S:.2f}, {rc*100*A*5/S:.2f}")
print("=== O7 carbon budget (GCB 2025, 1750-2024)")
tot = 752
for name, v in (("air", 312), ("ocean", 210), ("land", 190)):
    print(f"  {name}: {v} GtC = {v/tot:.0%}")
print(f"  fossil+cement {505} + land use {248} = {505+248}; remainder {tot-312-210-190} GtC = {(tot-712)/tot:.0%}")
print(f"  ppm: 312 GtC / 2.124 = {312/2.124:.0f} ppm above 280 -> {280+312/2.124:.0f} ppm")
