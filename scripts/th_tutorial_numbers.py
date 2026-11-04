"""Numbers for TH07/TH08 and the TD2213 tutorials 1 and 2 (all recomputed).

Data (Schroeder, An Introduction to Thermal Physics, 'Thermodynamic Properties of Selected Substances', pp. 404-405,
298 K, 1 bar): C(graphite) dfH 0, S 5.74, Cp 8.53; CO(g) -110.53, dfG -137.17, S 197.67, Cp 29.14; H2(g) 0, S 130.68, Cp 28.82;
H2O(g) -241.82, dfG -228.57, S 188.83, Cp 33.58; H2O(l) -285.83, dfG -237.13, S 69.91, Cp 75.29; CH4(g) -74.81; CO2(g) -393.51;
C(diamond) +1.895; NH3(g) -46.11, dfG -16.45, S 192.45; N2(g) S 191.61, Cp 29.12.
    .venv/bin/python -W ignore scripts/th_tutorial_numbers.py
"""
import numpy as np
from math import log, exp
from scipy import integrate, optimize

R = 8.314462618; P = print
def sec(t): P("\n#####", t)

sec("Tutorial 1 Q1: Delta H at constant pressure")
dU = 2500.0; Pext = 2.0e5; dV = (8.0 - 3.0) * 1e-3
P(f"P dV = {Pext * dV:.1f} J ; Delta H = Delta U + P Delta V = {dU + Pext * dV:.1f} J")

sec("Tutorial 1 Q2: Gibbs-Helmholtz, Delta G/T at 500 C")
for T1, T2 in ((298.15, 773.15), (298.0, 773.0)):
    G1, H = -50e3, -80e3
    g2 = G1 / T1 + H * (1 / T2 - 1 / T1)
    S = (H - G1) / T1
    P(f"T1={T1}, T2={T2}: dG/T(T1) = {G1 / T1:.3f} J/K/mol ; dG/T(T2) = {g2:.4f} J/K/mol ; dG(T2) = {g2 * T2:.1f} J/mol ; implied dS = {S:.2f} J/K/mol ; check -dS = {-S:.2f}, H - T2 dS = {H - T2 * S:.1f}")

sec("Tutorial 1 Q3: boiling point at higher pressure (Clausius-Clapeyron, constant dHvap)")
T1 = 80 + 273.15; dH = 40e3
for ratio in (1.25,):
    invT2 = 1 / T1 - R / dH * log(ratio)
    T2 = 1 / invT2
    P(f"exact: T2 = {T2:.3f} K = {T2 - 273.15:.2f} C ; shift = {T2 - T1:.3f} K")
    P(f"linearised: dT = R T1^2 ln(p2/p1)/dH = {R * T1 ** 2 * log(ratio) / dH:.3f} K")
    P(f"dP/dT at T1 = dH P/(R T^2) -> dT/dlnP = {R * T1 ** 2 / dH:.3f} K")
P(f"Trouton: dSvap = dHvap/Tb = {dH / T1:.2f} J/K/mol (typical 85-88; water 109)")
Tw = 373.15; Lw = 40.66e3
for name, p in (("Everest summit 33.7 kPa (recalled)", 33.7 / 101.325), ("3000 m, 70 kPa (recalled)", 70 / 101.325)):
    T2w = 1 / (1 / Tw - R / Lw * log(p)); P(f"water at {name}: Tb = {T2w - 273.15:.2f} C")

sec("Tutorial 1 Q4: entropy generation when A loses heat to B")
for TA, TB, Q in ((500, 300, 1000.0),):
    P(f"reservoirs {TA} K -> {TB} K, Q = {Q} J: dS_A = {-Q / TA:.4f}, dS_B = {Q / TB:.4f}, S_gen = {Q / TB - Q / TA:.4f} J/K ; lost work at T_C: T_C S_gen = {TB * (Q / TB - Q / TA):.1f} J")
for CA, CB, TA, TB in ((1000., 1000., 500., 300.), (1000., 3000., 500., 300.), (1000., 1000., 400., 399.)):
    Tf = (CA * TA + CB * TB) / (CA + CB)
    S = CA * log(Tf / TA) + CB * log(Tf / TB)
    P(f"bodies C_A={CA}, C_B={CB} J/K, T_A={TA}, T_B={TB}: T_f = {Tf:.3f} K ; S_gen = {S:.5f} J/K")

sec("Tutorial 2 Q1: Kirchhoff, HCl")
dH298 = -120e3; dCp = 25.0
P(f"Delta H(350) = {dH298 + dCp * (350 - 298):.1f} J/mol = {(dH298 + dCp * 52) / 1e3:.3f} kJ/mol ; correction = {dCp * 52:.1f} J/mol")

sec("Tutorial 2 Q2: ATPase")
for T in (298.0, 298.15):
    K = 0.295; dS = -45.0
    dG = -R * T * log(K); dHr = dG + T * dS
    P(f"T={T}: dG0 = -RT ln K = {dG:.1f} J/mol ; T dS = {T * dS:.1f} J/mol ; dH0 = dG0 + T dS0 = {dHr:.1f} J/mol = {dHr / 1e3:.2f} kJ/mol")

sec("Tutorial 2 Q3: Born-Haber / Hess for hydration of Mg2+")
lat, sol, hyd_cl = 2526.0, -155.0, -381.0
P(f"hyd(Mg2+) = sol - lat - 2 hyd(Cl-) = {sol - lat - 2 * hyd_cl:.1f} kJ/mol")

sec("Tutorial 2 Q4: C(graphite) + H2O(g) -> CO(g) + H2(g)  (Schroeder table; the tutorial gives no data)")
fH = {"C": 0.0, "H2O": -241.82, "CO": -110.53, "H2": 0.0}; fG = {"C": 0.0, "H2O": -228.57, "CO": -137.17, "H2": 0.0}
S = {"C": 5.74, "H2O": 188.83, "CO": 197.67, "H2": 130.68}; Cp = {"C": 8.53, "H2O": 33.58, "CO": 29.14, "H2": 28.82}
dH = fH["CO"] + fH["H2"] - fH["C"] - fH["H2O"]
dG = fG["CO"] + fG["H2"] - fG["C"] - fG["H2O"]
dS = S["CO"] + S["H2"] - S["C"] - S["H2O"]
dCp = Cp["CO"] + Cp["H2"] - Cp["C"] - Cp["H2O"]
P(f"dH298 = {dH:.2f} kJ ; dG298 = {dG:.2f} kJ (from dfG) ; dS298 = {dS:.2f} J/K ; dH - T dS = {dH - 298.15 * dS / 1e3:.2f} kJ ; dCp = {dCp:.2f} J/K")
P(f"dH(378) = {dH + dCp * 80 / 1e3:.3f} kJ/mol ;  dH(373.15 K) = {dH + dCp * 75 / 1e3:.3f}")
Tstar0 = dH * 1e3 / dS
dHT = lambda T: dH * 1e3 + dCp * (T - 298.15)
dST = lambda T: dS + dCp * log(T / 298.15)
dGT = lambda T: dHT(T) - T * dST(T)
Tstar1 = optimize.brentq(dGT, 500, 2000)
P(f"dG = 0 at T* = {Tstar0:.1f} K (constant dH, dS) ; with dCp: T* = {Tstar1:.1f} K ; dG(1000 K): const {dH * 1e3 - 1000 * dS:.0f} J, corrected {dGT(1000):.0f} J")
for T in (298.15, 600, 800, 1000, 1200):
    K0 = exp(-(dH * 1e3 - T * dS) / (R * T)); K1 = exp(-dGT(T) / (R * T))
    P(f"T={T:7.1f}: dG(const) = {(dH * 1e3 - T * dS) / 1e3:8.2f} kJ  dG(corr) = {dGT(T) / 1e3:8.2f} kJ  K(const) = {K0:.3g}  K(corr) = {K1:.3g}")

sec("Tutorial 2 Q5: bomb calorimeter")
m, M, C, dT, dng = 0.500, 122.12, 10.0e3, 1.50, -0.5
q = C * dT; n = m / M
dcU = -q / n; dcH = dcU + dng * R * 298.0
P(f"q = {q:.1f} J ; n = {n * 1e3:.4f} mmol ; dcU = {dcU / 1e3:.2f} kJ/mol ; dn_g R T = {dng * R * 298.0:.1f} J ; dcH = {dcH / 1e3:.2f} kJ/mol ; per gram {q / m / 1e3:.2f} kJ/g")

sec("Tutorial 2 Q6: constant-pressure calorimeter (neutralisation)")
mass = 100.0; c = 4.18; dT = 31.7 - 25.0
q = mass * c * dT; n = 0.0500 * 1.00
P(f"q = {q:.1f} J = {q / 1e3:.3f} kJ ; n = {n:.4f} mol ; dH = {-q / n / 1e3:.2f} kJ/mol")

sec("Extra examples for TH07")
P(f"CH4 + 2 O2 -> CO2 + 2 H2O(l): dcH = {-393.51 + 2 * (-285.83) + 74.81:.2f} kJ/mol ; dn_g = -2: dcU = {(-393.51 + 2 * -285.83 + 74.81) - (-2) * R * 298.15 / 1e3:.2f}")
P(f"N2 + 3 H2 -> 2 NH3: dH = {2 * -46.11:.2f} kJ ; dG = {2 * -16.45:.2f} kJ ; dn_g = -2: dH - dU = {-2 * R * 298.15 / 1e3:.3f} kJ")
P(f"C(graphite) -> C(diamond): dH = 1.895 kJ/mol ; dG = 2.900 kJ/mol")
a, b, cc = 16.86, 4.77e-3, 8.54e5
Cpg = lambda T: a + b * T - cc / T ** 2
Hint = integrate.quad(Cpg, 298.0, 500.0)[0]
P(f"graphite Cp(298) = {Cpg(298.0):.3f} (table 8.53) ; Cp(500) = {Cpg(500.0):.3f} ; H(500)-H(298) = {Hint:.1f} J/mol ; with constant Cp=8.53: {8.53 * 202:.1f}")
P(f"enthalpy of vaporisation of water at 298 K from the table: {-241.82 + 285.83:.2f} kJ/mol (at 373 K: 40.66 recalled)")
P(f"boiling 1 mol water at 1 atm: dH = 40.66 kJ, dU = dH - RT = {40.66 - R * 373.15 / 1e3:.2f} kJ")

sec("Extra examples for TH08: ammonia, van 't Hoff, G(xi)")
dHn, dGn, T0 = -92.22e3, -32.90e3, 298.15
K298 = exp(-dGn / (R * T0)); P(f"NH3: K(298) = {K298:.3e} (ln K = {-dGn / (R * T0):.3f}), dS = {(dHn - dGn) / T0:.2f} J/K")
for T in (500.0, 773.15):
    lnK = -dGn / (R * T0) - dHn / R * (1 / T - 1 / T0)
    P(f"K({T}) with constant dH: {exp(lnK):.3e} (ln K = {lnK:.3f})")
P(f"van 't Hoff slope dH/R = {dHn / R:.1f} K")
# G(xi) for A <-> B with K = exp(-dG0/RT): G/RT = (1-x) ln(1-x) + x ln x + x dG0/RT  (mixing of ideal gases, A->B)
for K in (0.1, 1.0, 10.0):
    x = K / (1 + K); P(f"K = {K}: equilibrium extent xi = K/(1+K) = {x:.4f}")
P("entropy generation of a reaction at fixed T,P: S_gen = -dG/T; e.g. water-gas at 1000 K (corrected dG = %.0f J): per mole of forward extent S_gen = %.2f J/K" % (dGT(1000.0), -dGT(1000.0) / 1000.0))

sec("More TH07 practice numbers")
RT = R * 298.15 / 1e3
dH_NH3 = -92.22; P(f"NH3 synthesis: dU = dH - dn_g RT = {dH_NH3 - (-2) * RT:.2f} kJ (dH - dU = {-2 * RT:.3f} kJ; {(-2 * RT) / dH_NH3 * 100:.1f} % of dH)")
dcH_CH4 = -393.51 + 2 * -285.83 + 74.81
P(f"CH4: dcH = {dcH_CH4:.2f} kJ/mol ; per gram (16.043 g/mol) = {dcH_CH4 / 16.043:.2f} kJ/g")
dcH_gl = 6 * -393.51 + 6 * -285.83 - (-1268)
P(f"glucose: dcH = {dcH_gl:.2f} kJ/mol ; per gram (180.16 g/mol) = {dcH_gl / 180.16:.2f} kJ/g ; kcal per gram = {dcH_gl / 180.16 / 4.184:.2f}")
P(f"electrical calibration: 50 W x 120 s = {50 * 120} J ; DeltaT = 0.83 K -> C = {50 * 120 / 0.83:.0f} J/K")
P(f"water boiling: dvapH = 40.66, dvapU = {40.66 - R * 373.15 / 1e3:.2f}, RT = {R * 373.15 / 1e3:.3f} kJ")
P(f"water-gas dH(1000 K), constant dCp: {131.29 + 15.85 * (1000 - 298.15) / 1e3:.2f} kJ/mol")
a, b, cc = 16.86, 4.77e-3, 8.54e5
P(f"graphite integral pieces: a dT = {a * 202:.1f} ; b/2 (T2^2 - T1^2) = {b / 2 * (500 ** 2 - 298 ** 2):.1f} ; c (1/T2 - 1/T1) = {cc * (1 / 500 - 1 / 298):.1f}")
P(f"HCl check: dH at 298 per mole of HCl = -60 kJ; 2 HCl formation at 350 K as written: {-120 + 25 * 52 / 1e3:.3f} kJ")
P(f"bomb: kJ per gram {15.0 / 0.500:.2f}; real certified benzoic acid 26.43 kJ/g (recalled) -> molar {26.43 * 122.12:.0f} kJ")

sec("More TH08 numbers")
R_ = R
dG1 = -50e3; T1 = 298.15
P(f"Tutorial 1 Q2 reaction: K(298.15) = exp(50000/RT) = {exp(50000 / (R_ * T1)):.3e}; at 773.15 K dG = -2205.3 J: K = {exp(2205.3 / (R_ * 773.15)):.3f}")
# ammonia with dCp
dHn, dGn, dCpn = -92.22e3, -32.90e3, -5.48
dSn = (dHn - dGn) / 298.15
for T in (500.0, 773.15):
    dHn_T = dHn + dCpn * (T - 298.15); dSn_T = dSn + dCpn * log(T / 298.15)
    P(f"NH3 K({T}): constant dH {exp(-(dHn - T * dSn) / (R_ * T)):.3e} ; with dCp = -5.48: {exp(-(dHn_T - T * dSn_T) / (R_ * T)):.3e}; dG = {(dHn_T - T * dSn_T) / 1e3:.2f} kJ")
# ATP
K = 0.295; Kp = K / 1e-7
P(f"ATP: K' at pH 7 = K/[H+] = {Kp:.3e}; dG0' = -RT ln K' = {-R_ * 298.15 * log(Kp) / 1e3:.2f} kJ/mol ; RT = {R_ * 298.15 / 1e3:.4f} kJ")
P(f"dG for Q = 0.1 K at 298.15 K: RT ln(Q/K) = {R_ * 298.15 * log(0.1) / 1e3:.3f} kJ/mol ; Q = 10 K: {R_ * 298.15 * log(10) / 1e3:.3f}")
P(f"Trouton for water: {40.66e3 / 373.15:.2f} J/K/mol ; the Q3 compound: {40e3 / 353.15:.2f}")
P(f"Q3 compound with 40 kJ: at 1.25 atm; slope dT/dlnP = {R_ * 353.15 ** 2 / 40e3:.3f} K ; ln1.25 = {log(1.25):.5f}")
P(f"water-gas entropy generation at 1000 K: {-dGT(1000.0) / 1000:.2f} J/K per mole of extent ; at 800 K (forward ΔG>0, reaction runs backwards): {-dGT(800.0) / 800:.2f}")
P(f"S_gen identity check: dS_univ = dS_sys - dH/T = {(133.78 + 15.85 * log(1000 / 298.15)) - dHT(1000.0) / 1000:.2f} J/K ; -dG/T = {-dGT(1000.0) / 1000:.2f}")
P(f"two equal bodies (C = 1000 J/K each), 500 K and 300 K: S_gen = {1000 * log(400 ** 2 / (500 * 300)):.3f} J/K ; W_lost at T0=300 K = {300 * 1000 * log(400 ** 2 / (500 * 300)):.0f} J")
P(f"dT_f for 1 J step from A (400 K) to B (399 K) = 1/T_B - 1/T_A = {1 / 399 - 1 / 400:.3e} J/K per joule")
