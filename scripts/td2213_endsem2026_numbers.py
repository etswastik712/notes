#!/usr/bin/env python3
"""Solutions (numbers) for the TD2213 End-Semester Examination, 2026 January semester (29 April 2026; photos of the paper
moved from ~/Downloads into physics/thermodynamics-stat-mech/lecture-notes-slides/ on 2026-11-21).
Data and constants are the paper's own (Data 1-4, Table 1).  Run: .venv/bin/python -I scripts/td2213_endsem2026_numbers.py"""
import numpy as np
from itertools import product
from math import factorial, log, exp, sqrt, pi
from scipy.optimize import brentq
from scipy.integrate import quad

R = 8.314; kB = 1.38e-23; h = 6.626e-34; cal = 4.1858; atm = 1.01325e5; NA = 6.022e23
T = {"methane": dict(M=16.04, Tc=191.1, Pc=45.8, w=0.011, A=4.75, B=1.2e-2, C=0.303e-5, D=-2.63e-9, Tb=-161.5),
     "propane": dict(M=44.09, Tc=370.0, Pc=42.0, w=0.153, A=-0.966, B=7.279e-2, C=-3.755e-5, D=7.58e-9, Tb=-41.97),
     "water": dict(M=18.02, Tc=647.4, Pc=218.3, w=0.344, A=7.7, B=0.04594e-2, C=0.2521e-5, D=-0.8587e-9, Tb=100.0)}

print("=== Q1 heat flow A -> B")
print("  dS_A/dt = -Qdot/T_A, dS_B/dt = +Qdot/T_B, Qdot = k (T_A - T_B); total = k (T_A-T_B)^2/(T_A T_B) >= 0")

print("=== Q2 propane: vapour pressure at 45 C from Tb and the acentric factor (Clausius-Clapeyron through two points)")
p = T["propane"]; Tc, Pc, w = p["Tc"], p["Pc"], p["w"]
T1, P1 = p["Tb"] + 273.15, 1.0                  # atm
T2, P2 = 0.7 * Tc, Pc * 10 ** (-1.0 - w)         # omega definition
B_ = np.log(P2 / P1) / (1 / T1 - 1 / T2); A_ = np.log(P1) + B_ / T1
for TC in (25, 45):
    P = exp(A_ - B_ / (TC + 273.15))
    print(f"  T={TC} C: Psat = {P:.2f} atm = {P*1.01325:.2f} bar   (points: Tb={T1:.2f} K at 1 atm; 0.7Tc={T2:.1f} K at {P2:.3f} atm; slope B={B_:.1f} K)")
# cross-check with Lee-Kesler correlation
def lee_kesler(Tr, w):
    f0 = 5.92714 - 6.09648 / Tr - 1.28862 * log(Tr) + 0.169347 * Tr**6
    f1 = 15.2518 - 15.6875 / Tr - 13.4721 * log(Tr) + 0.43577 * Tr**6
    return exp(f0 + w * f1)
for TC in (25, 45):
    print(f"  Lee-Kesler check T={TC} C: {Pc*lee_kesler((TC+273.15)/Tc, w):.2f} atm")

print("=== Q3 methane Cp, Cv; Redlich-Kwong correction")
m = T["methane"]; T0 = 298.15
Cp_cal = m["A"] + m["B"] * T0 + m["C"] * T0**2 + m["D"] * T0**3
Cp = Cp_cal * cal; Cv = Cp - R
print(f"  (a) Cp0 = {Cp_cal:.4f} cal/mol/K = {Cp:.3f} J/mol/K   (b) Cv0 = Cp0 - R = {Cv:.3f} J/mol/K")
Rl = 0.08206  # L atm / mol K for a, b
a = 0.42748 * Rl**2 * m["Tc"]**2.5 / m["Pc"]; b = 0.08664 * Rl * m["Tc"] / m["Pc"]
print(f"  RK a = {a:.3f} L^2 atm K^0.5 mol^-2, b = {b:.5f} L/mol")
V = 0.2111
dCv = 3 * a / (4 * b * T0**1.5) * log(1 + b / V)        # in L atm / mol / K
dCv_J = dCv * 101.325                                    # 1 L atm = 101.325 J
print(f"  (c) (dCv/dV)_T = T (d2P/dT2)_V = -(3a/4) T^-1.5 / [V(V+b)]")
print(f"  (d) Cv(100 bar) - Cv(0) = (3a/4bT^1.5) ln(1 + b/V) = {dCv_J:.3f} J/mol/K  -> Cv(100 bar) = {Cv+dCv_J:.3f} J/mol/K")
# numerical check of the integral
num = quad(lambda v: -(3 * a / 4) * T0**-1.5 / (v * (v + b)), np.inf, V)[0] * 101.325 if False else -quad(lambda v: -(3 * a / 4) * T0**-1.5 / (v * (v + b)), V, np.inf)[0] * 101.325
print(f"      numerical integral check: {num:.3f}")
# RK pressure at V to confirm 100 bar
Pchk = Rl * T0 / (V - b) - a / (sqrt(T0) * V * (V + b))
print(f"      RK P at V=0.2111 L/mol, 25 C: {Pchk:.2f} atm = {Pchk*1.01325:.1f} bar (paper: 100 bar)")

print("=== Q4 steam 30 bar, 550 C -> 7 bar, reversible adiabatic, ideal gas, Cp = 40")
T1 = 823.15; T2 = T1 * (7 / 30) ** (R / 40)
print(f"  T2 = T1 (P2/P1)^(R/Cp) = {T2:.1f} K = {T2-273.15:.1f} C")
wv = T["water"]
aw = 0.42748 * Rl**2 * wv["Tc"]**2.5 / wv["Pc"]; bw = 0.08664 * Rl * wv["Tc"] / wv["Pc"]
def Vrk(Tk, Patm):
    f = lambda v: Rl * Tk / (v - bw) - aw / (sqrt(Tk) * v * (v + bw)) - Patm
    return brentq(f, bw * 1.0001 + 1e-9, 50 * Rl * Tk / Patm + 10)
def SR(Tk, Patm):  # residual entropy S - S_ig(T,P), J/mol/K, RK
    v = Vrk(Tk, Patm); Z = Patm * v / (Rl * Tk)
    return R * (log(Z * (v - bw) / v) - aw / (2 * bw * Rl * Tk**1.5) * log((v + bw) / v))
P1, P2 = 30 / 1.01325, 7 / 1.01325
S1 = SR(T1, P1)
f = lambda T2r: (40 * log(T2r / T1) - R * log(P2 / P1)) + SR(T2r, P2) - S1
T2r = brentq(f, 500, 900)
print(f"  RK real-gas estimate (residual entropies): S_R(T1,P1) = {S1:.3f}, T2 = {T2r:.1f} K = {T2r-273.15:.1f} C (vs ideal {T2-273.15:.1f} C)")

print("=== Q5 Hess")
print(f"  2S + 2O2 -> 2SO2: -793 - (-200) = -593 kJ; per mol SO2: {-593/2} kJ/mol")

print("=== Q6 chlorine isotopes")
pa, pb = 0.76, 0.24
print(f"  35Cl2 {pa*pa:.4f}, 37Cl2 {pb*pb:.4f}, 35Cl37Cl {2*pa*pb:.4f} (sum {pa*pa+pb*pb+2*pa*pb:.1f})")

print("=== Q7 2H -> H2, Kirchhoff")
g = lambda Tk: -20000 + 6.0 * (Tk - 298) + 1.0e-3 * (Tk**2 - 298**2)
Tz = brentq(g, 298, 10000)
print(f"  dH(T) = -20000 + 6(T-298) + 1e-3(T^2-298^2) = 0 at T = {Tz:.1f} K")

print("=== Q8 F2 vibration")
nu = 2.676e13; th = h * nu / kB; q = 1 / (1 - exp(-th / 298.15))
print(f"  Theta_vib = h nu/k = {th:.1f} K; q_vib(298.15 K) = {q:.5f}")
print(f"  (wavenumber {nu/3e10:.0f} cm^-1; note the data sheet's handwritten '1 Hz = 3e10 cm^-1' should read 1 cm^-1 = 3e10 Hz)")

print("=== Q10 D2 translation, 100 cm^3, 25 C")
mD2 = 2 * 2.014 * 1.6605e-27; Vv = 100e-6; Tk = 298.15
Lam = h / sqrt(2 * pi * mD2 * kB * Tk); qt = Vv / Lam**3
print(f"  thermal wavelength {Lam*1e10:.4f} A; q_trans = V/Lambda^3 = {qt:.3e}")
print(f"  U = (3/2) R T = {1.5*R*Tk:.1f} J/mol  (one molecule: {1.5*kB*Tk:.3e} J)")
Sm = R * (log(qt / NA) + 2.5)
print(f"  S (one mole in 100 cm^3, Sackur-Tetrode) = R[ln(q/N_A) + 5/2] = {Sm:.2f} J/mol/K")
print(f"  S (one molecule, distinguishable, S = k(ln q + 3/2)) = {kB*(log(qt)+1.5):.3e} J/K")

print("=== Q11 four distinguishable particles, levels 0..5, total energy 5")
dists = []
for occ in product(range(5), repeat=6):
    if sum(occ) == 4 and sum(i * n for i, n in enumerate(occ)) == 5:
        W = factorial(4)
        for n in occ: W //= factorial(n)
        dists.append((occ, W))
dists.sort(key=lambda x: -x[1])
tot = sum(Wi for _, Wi in dists)
for occ, Wi in dists:
    print(f"  occupation n0..n5 = {occ}  W = {Wi}")
print(f"  {len(dists)} distributions, total microstates {tot} (= C(8,3) = {factorial(8)//(factorial(3)*factorial(5))})")
avg = [sum(occ[i] * Wi for occ, Wi in dists) / tot for i in range(6)]
print("  average occupation of each level over all microstates:", [round(x, 3) for x in avg])
r = [avg[i + 1] / avg[i] for i in range(4)]
print("  successive ratios n(i+1)/n(i):", [round(x, 3) for x in r], " -> roughly geometric (Boltzmann-like), beta*eps ~", round(-log(np.mean(r[:3])), 3))
