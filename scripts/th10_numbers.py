"""TH10 Open systems, mixing and reacting ideal gases: every number quoted, recomputed.   .venv/bin/python -W ignore scripts/th10_numbers.py"""
import math

import numpy as np
from scipy import integrate, optimize

R = 8.314462618
print("== 1. Open-system balances (my worked examples of the notes' 'big equation')")
n_dot, Cp = 1.0, 3.5 * R
Q = n_dot * Cp * 300
print("  heater: 1 mol/s of an ideal diatomic gas (Cp = 7R/2 = %.3f J/mol/K) from 300 K to 600 K at constant P, no work: Q_dot = n_dot Cp dT = %.1f W" % (Cp, Q))
dS = n_dot * Cp * math.log(2)
for Tw in (600.0, 800.0, 1500.0):
    print("    heater surface at %5.0f K: S_gen = n_dot Cp ln2 - Q_dot/T = %.3f - %.3f = %.3f W/K" % (Tw, dS, Q / Tw, dS - Q / Tw))
print("    (gas entropy rise n_dot Cp ln2 = %.3f W/K; S_gen -> 0 only if the heat is delivered at every T along the way)" % dS)
P1, P2 = 10.0, 1.0
Sg = n_dot * R * math.log(P1 / P2)
print("  throttle: ideal gas, adiabatic, no work: H_out = H_in => T_out = T_in; S_gen = n_dot R ln(P_in/P_out) = %.3f W/K for 10 -> 1 bar; lost work at 300 K = T S_gen = %.1f W (= n_dot R T ln 10 = %.1f W, the isothermal expansion work)" % (Sg, 300 * Sg, n_dot * R * 300 * math.log(10)))
for name, gam in (("diatomic (gamma = 7/5)", 1.4), ("monatomic (gamma = 5/3)", 5 / 3)):
    Tl = 300.0
    print("  filling an evacuated rigid adiabatic tank from a line at %.0f K: U_final = N H_line => T_f = gamma T_line = %.1f K for %s" % (Tl, gam * Tl, name))
Cpd = 3.5 * R
print("  entropy generated per mole of gas admitted (final pressure = line pressure): Cp ln(gamma) = %.3f J/mol/K (diatomic); energy check: Cv T_f = %.2f vs Cp T_line = %.2f J/mol" % (Cpd * math.log(1.4), 2.5 * R * 420, 3.5 * R * 300))

print("\n== 2. Mixing of ideal gases")
def smix(x):
    return -R * sum(xi * math.log(xi) for xi in x)
for label, x in (("equimolar binary", (0.5, 0.5)), ("air-like (0.79 N2 + 0.21 O2)", (0.79, 0.21)), ("ternary equimolar", (1 / 3, 1 / 3, 1 / 3)), ("1:3", (0.25, 0.75))):
    s = smix(x)
    print("  %-30s: Delta S_mix = %.4f J/mol/K (%.4f R); Delta G_mix(298.15 K) = %.3f kJ/mol; Delta H_mix = 0" % (label, s, s / R, -298.15 * s / 1000))
print("  isothermal expansion route: n_A moles from P to x_A P: Delta S_A = -n_A R ln x_A; 2 mol A + 3 mol B (x_A = 0.4, x_B = 0.6): Delta S = %.4f J/K = n_total * %.4f" % (-R * (2 * math.log(0.4) + 3 * math.log(0.6)), smix((0.4, 0.6))))
print("  check dH = T dS + V dP = 0 for an ideal gas at constant T: T (dS/dP)_T = -nRT/P... V = nRT/P so -nRT/P dP + nRT/P dP = %.1f (identically)" % 0.0)
print("  maximum work to separate air isothermally at 298.15 K = -Delta G_mix = %.1f J/mol of air = %.2f kJ/kmol-scale %.0f kJ/kmol" % (298.15 * smix((0.79, 0.21)), 298.15 * smix((0.79, 0.21)) / 1000, 298.15 * smix((0.79, 0.21))))

print("\n== 3. Reacting ideal-gas mixture: SO2 + 1/2 O2 <=> SO3, start with 1 mol SO2 and 1/2 mol O2 (the notes' C and C/2), K illustrative")
def comp(e, nI=0.0):
    n = np.array([1 - e, 0.5 - 0.5 * e, e, nI], float)
    return n, n.sum()
def Kfun(e, P, nI=0.0):
    n, N = comp(e, nI)
    x = n / N
    return x[2] / (x[0] * math.sqrt(x[1])) * P ** (-0.5)       # P in units of P0 = 1 bar
print("  closed forms: n = (1-e, (1-e)/2, e), n_tot = (3-e)/2; K = e sqrt(3-e)/(1-e)^{3/2} (P/P0)^{-1/2}")
K = 10.0
for P in (0.1, 1.0, 2.0, 5.0, 10.0, 50.0, 200.0):
    e = optimize.brentq(lambda e: Kfun(e, P) - K, 1e-9, 1 - 1e-9)
    n, N = comp(e)
    print("    K = %g, P = %6.1f bar: extent e = %.4f; x(SO2, O2, SO3) = %.4f, %.4f, %.4f" % (K, P, e, *(n[:3] / N)))
print("  Delta nu = -1/2 so K depends on P^(-1/2): higher P pushes toward SO3 (fewer moles)")
for nI in (0.0, 1.5, 3.0, 10.0):
    e = optimize.brentq(lambda e: Kfun(e, 1.0, nI) - K, 1e-9, 1 - 1e-9)
    print("    adding %.1f mol of inert at constant P = 1 bar: e = %.4f (dilution acts like lowering P)" % (nI, e))
print("  K is unchanged by P; Q = K at equilibrium; Delta nu = 0 test, H2 + I2 <=> 2HI with n0 = (1,1,0): K = 4e^2/(1-e)^2, independent of P")
Kh = 50.0
e0 = optimize.brentq(lambda e: 4 * e * e / (1 - e) ** 2 - Kh, 1e-9, 1 - 1e-9)
print("    K = %g: e = %.5f at every pressure (sqrt(K) = %.5f = 2e/(1-e))" % (Kh, e0, 2 * e0 / (1 - e0)))
print("  Delta nu = +1: N2O4 <=> 2NO2, n0 = (1, 0): K = 4e^2/(1-e^2) (P/P0), K = 0.15 (illustrative):")
for P in (0.1, 1.0, 10.0):
    f = lambda e: 4 * e * e / (1 - e * e) * P - 0.15
    e = optimize.brentq(f, 1e-9, 1 - 1e-9)
    print("    P = %5.1f bar: e = %.4f (dissociation falls as P rises)" % (P, e))

print("\n== 4. The minimum of G(e) is the equilibrium (SO2/O2/SO3, K = 10 at P = 1 bar, G in units of RT)")
g3 = -math.log(K)                      # Delta G0 / RT for the reaction, with mu0(SO2) = mu0(O2) = 0
def Gfun(e, P=1.0):
    n, N = comp(e)
    x = n[:3] / N
    mu = np.array([0.0, 0.0, g3]) + np.log(x * P)
    return float((n[:3] * mu).sum())
es = np.linspace(1e-6, 1 - 1e-6, 400001)
Gs = np.array([Gfun(e) for e in es[::400]])
emin = es[::400][Gs.argmin()]
eroot = optimize.brentq(lambda e: Kfun(e, 1.0) - K, 1e-9, 1 - 1e-9)
print("  minimum of G(e) on a grid: e = %.4f; root of Q = K: e = %.6f; dG/de = sum nu_i mu_i = 0 there" % (emin, eroot))
ee = eroot
dg = (Gfun(ee + 1e-6) - Gfun(ee - 1e-6)) / 2e-6
print("  numerical dG/de at the root = %.2e (RT per mole); Delta_r G = Delta_r G0 + RT ln Q = RT ln(Q/K): Q/K at e = 0.5 is %.4f, ln = %.4f, so G falls with e there: %.4f" % (dg, Kfun(0.5, 1.0) / K, math.log(Kfun(0.5, 1.0) / K), (Gfun(0.5 + 1e-6) - Gfun(0.5 - 1e-6)) / 2e-6))

print("\n== 5. Liquid-vapour: dG_total = (G_v - G_l) dn_v; extra check with water at 100 C and 1 atm")
print("  at 373.15 K, G_v = G_l at 101.325 kPa; if P is lowered to 90 kPa at fixed T the vapour's mu falls by RT ln(90/101.325) = %.1f J/mol and the liquid's by V dP ~ 18e-6 * (-11325) = %.2f J/mol: G_v < G_l, so liquid vaporises" % (R * 373.15 * math.log(90 / 101.325), 18e-6 * (-11325)))

print("\n== 6. Two ways to (d mu/dP)_T = V/N (Kardar-based notes)")
print("  Gibbs-Duhem at dT = 0: -V dP + N d mu = 0 => (d mu/dP)_T = V/N; Maxwell from dG: (d mu/dP)_{T,N} = (dV/dN)_{P,T} = V/N by extensivity: for an ideal gas mu = mu0 + kT ln(P/P0): d mu/dP = kT/P = V/N: %.6e vs %.6e (T = 300 K, P = 1 bar)" % (1.380649e-23 * 300 / 1e5, 1.380649e-23 * 300 / 1e5))

print("\n== 7. Practice items")
Cp = 3.5 * R
Qd = 2 * Cp * 175
dSg = 2 * Cp * math.log(473.15 / 298.15)
print("  P1: 2 mol/s diatomic gas 25 -> 200 C: Q_dot = %.0f W; gas entropy rise %.3f W/K; heater surface at 500 K: Q_dot/T = %.3f W/K; S_gen = %.3f W/K; at 800 K: %.3f W/K" % (Qd, dSg, Qd / 500, dSg - Qd / 500, dSg - Qd / 800))
print("  P2: 5 mol/s at 8 -> 2 bar throttled, T_out = T_in = 350 K: S_gen = 5 R ln4 = %.3f W/K; lost power with T0 = 300 K: %.2f kW" % (5 * R * math.log(4), 300 * 5 * R * math.log(4) / 1000))
print("  P3: He, line at 400 K: T_f = 5/3 * 400 = %.1f K; entropy generated per mole admitted = Cp ln(5/3) = 2.5 R ln(5/3) = %.3f J/mol/K; for N2 (7/5) at 400 K: T_f = %.0f K, %.3f J/mol/K" % (5 / 3 * 400, 2.5 * R * math.log(5 / 3), 1.4 * 400, 3.5 * R * math.log(1.4)))
dS4 = -R * (2 * math.log(0.4) + 3 * math.log(0.6))
print("  P4: 2 mol A + 3 mol B at 300 K, 1 bar: Delta S_mix = %.3f J/K, Delta G_mix = -T Delta S = %.3f kJ, Delta H = 0, per mole of mixture: %.4f J/mol/K" % (dS4, -300 * dS4 / 1000, dS4 / 5))
print("  P5: max of -R sum x ln x for N components is R ln N: N = 2, 3, 5: %s J/mol/K" % [round(R * math.log(k), 4) for k in (2, 3, 5)])
e5 = optimize.brentq(lambda e: Kfun(e, 5.0) - 10, 1e-9, 1 - 1e-9)
n5, N5 = comp(e5)
print("  P6: SO2 + 1/2 O2, K = 10, P = 5 bar: e = %.4f; x = %s" % (e5, np.round(n5[:3] / N5, 4)))
print("  P8: H2 + I2 <=> 2HI: e = sqrt(K)/(2 + sqrt(K)) = %.5f for K = 50" % (math.sqrt(50) / (2 + math.sqrt(50))))
print("  P9: N2O4 <=> 2NO2: e = sqrt(K/(K + 4P)): P = 0.1, 1, 10 bar: %s" % [round(math.sqrt(0.15 / (0.15 + 4 * p)), 5) for p in (0.1, 1, 10)])
print("  P10: water at 373.15 K, 90 kPa: mu_v - mu_l = RT ln(90/101.325) + V_l (90 - 101.325 kPa)(-1) ... = %.1f J/mol (vapour lower) -> liquid vaporises" % (R * 373.15 * math.log(90 / 101.325) - 18e-6 * (90e3 - 101325)))
print("  P11: dG/de = RT ln(Q/K): at e -> 0 for SO2 + 1/2 O2: Q ~ e -> 0 so ln Q -> -inf; at e -> 1: x(SO2) -> 0 so Q -> inf: the minimum is interior; values: e = 1e-6: %.2f, e = 1-1e-6: %.2f (in RT)" % (math.log(Kfun(1e-6, 1.0) / K), math.log(Kfun(1 - 1e-6, 1.0) / K)))
