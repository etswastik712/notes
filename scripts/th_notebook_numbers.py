"""Examples from the post-midsem notebook that were not yet in the vault (TH07, TH09, TH10): every number recomputed.
    .venv/bin/python -W ignore scripts/th_notebook_numbers.py"""
import itertools, math
from math import comb, factorial, log
R = 8.314462618
print("== Hess / combustion of propene (pp. 21-22)")
d1, d2, d3 = -121.0, -2220.0, +286.0
print("  propene + H2 -> propane (%+.0f), propane + 5 O2 -> 3 CO2 + 4 H2O (%+.0f), H2O(l) -> H2 + 1/2 O2 (%+.0f): sum = %.0f kJ/mol (notebook: 286 - 121 - 2220 = 165 - 2220 = -2055)" % (d1, d2, d3, d1 + d2 + d3))
print("  atom check of the sum: C3H6 + H2 + C3H8 + 5 O2 + H2O  ->  C3H8 + 3 CO2 + 4 H2O + H2 + 1/2 O2: net C3H6 + 9/2 O2 -> 3 CO2 + 3 H2O (H: 6+2+8+2 = 18 -> 8+8+2 = 18 ok)")
print("\n== Calorimetry with a hot copper block (p. 23)")
mw, cw, dTw = 150.0, 4.18, 5.0
q = mw * cw * dTw
print("  150 g water 25 -> 30 C: q = m c dT = %.0f J (the notebook 3135 J)" % q)
mCu, cCu = 120.0, 0.39
T2 = 30.0 + q / (mCu * cCu)
print("  120 g Cu (c = 0.39 J/g/K) cools to 30 C: -q = m c (30 - T2): T2 = 30 + %.0f/(120 x 0.39) = %.2f C (notebook 96.98 C)" % (q, T2))
print("\n== Water-gas shift CO + H2O <=> CO2 + H2 with dG0(1100 K) = 0, so K = 1 and the pressure drops out (Delta nu = 0) (pp. 17-18)")
for lab, n0 in (("1 mol CO + 1 mol H2O", (1, 1)), ("1 mol CO + 2 mol H2O (the side calculation)", (1, 2))):
    # K = e^2/((n0a - e)(n0b - e)) = 1  ->  e = n0a n0b/(n0a + n0b)
    a, b = n0
    e = a * b / (a + b)
    print("  %-46s: e^2 = (%d - e)(%d - e) => e = %d/%d = %.4f" % (lab, a, b, a * b, a + b, e))
print("\n== Mixing from dG = V dP at constant T (pp. 12-14): 80 % N2 + 20 % O2 at 1 atm, 300 K")
x = (0.8, 0.2)
s = -R * sum(xi * log(xi) for xi in x)
print("  Delta G_A = int_P^{P_A} RT/P dP = RT ln(P_A/P) = RT ln x_A; Delta G_mix per mole = RT sum x ln x = %.1f J/mol = %.3f kJ/mol; Delta S_mix = %.3f J/mol/K (%.4f R); T Delta S = %.1f J/mol" % (R * 300 * sum(xi * log(xi) for xi in x), R * 300 * sum(xi * log(xi) for xi in x) / 1000, s, s / R, 300 * s))
print("  per mole of N2: RT ln 0.8 = %.1f J; per mole of O2: RT ln 0.2 = %.1f J" % (R * 300 * log(0.8), R * 300 * log(0.2)))
print("\n== Clausius-Clapeyron at 0.7 atm (p. 8: 'for 0.7 atm = P2, P1 = 1 atm'), water, dHvap = 40.66 kJ/mol (recalled), T1 = 373.15 K")
dH = 40660.0
T1 = 373.15
T2c = 1 / (1 / T1 - R / dH * log(0.7))
print("  1/T2 = 1/T1 - (R/dH) ln(P2/P1): T2 = %.2f K = %.2f C (a boiling point about %.1f K lower)" % (T2c, T2c - 273.15, T1 - T2c))
print("\n== Three distinguishable particles, levels 0,1,2,3, total energy 3 (p. 28)")
asg = [t for t in itertools.product(range(4), repeat=3) if sum(t) == 3]
from collections import Counter
dist = Counter(tuple(sorted(t)) for t in asg)
print("  ordered assignments with sum 3: %d (= W_tot); distributions: %s" % (len(asg), {k: v for k, v in sorted(dist.items())}))
tot = len(asg)
for lvl in range(4):
    p = sum(sum(1 for e in t if e == lvl) for t in asg) / (3 * tot)
    print("  P(a given particle is in level %d) = %d/30 = %.3f (%s)" % (lvl, round(p * 30), p, {0: "2/3 x 3/10 + 1/3 x 6/10 = 12/30 = 4/10", 1: "1/3 x 6/10 + 3/3 x 1/10 = 9/30 = 3/10", 2: "1/3 x 6/10 = 6/30 = 2/10", 3: "1/3 x 3/10 = 3/30 = 1/10"}[lvl]))
print("  P_A = %d/%d, P_B = %d/%d, P_C = %d/%d" % (dist[(0, 0, 3)], tot, dist[(0, 1, 2)], tot, dist[(1, 1, 1)], tot))
print("\n== Eight distinguishable particles in two levels (p. 27): W(k) = C(8,k), total 2^8")
print("  W =", [comb(8, k) for k in range(9)], "; total", 2 ** 8, "; W_MPD = %d, fraction %.4f (= %d/256); ln W_MPD = %.4f vs N ln 2 = %.4f" % (comb(8, 4), comb(8, 4) / 256, comb(8, 4), log(comb(8, 4)), 8 * log(2)))
print("  probabilities k = 0..8: %s /256" % [comb(8, k) for k in range(9)])
