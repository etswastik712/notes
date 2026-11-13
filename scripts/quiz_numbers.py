"""Numbers for the three quiz-prep pages (2026-11-12): thermodynamics Tutorials 1-2 variants; proofs Assignments 8-9 checks.
    .venv/bin/python -W ignore scripts/quiz_numbers.py"""
import math
from fractions import Fraction
R = 8.314462618
print("== Thermodynamics: self-test variants")
print("1. dU = -1.8 kJ, P = 1.5 bar const, V 10 L -> 4 L: dH = %.2f kJ" % (-1.8 + 1.5 * (4 - 10) * 0.1))
T1, T2 = 298.15, 400.0
G1, H = -30000.0, -60000.0
gt = G1 / T1 + H * (1 / T2 - 1 / T1)
print("2. dG0(298.15) = -30 kJ, dH0 = -60 kJ const: dG0/T(400 K) = %.2f J/K/mol; dG0(400) = %.2f kJ/mol; K = %.1f; (with 298 and 400: dG/T = %.2f)" % (gt, gt * T2 / 1000, math.exp(-gt * T2 / (R * T2)), -30000 / 298 + H * (1 / 400 - 1 / 298)))
T1b, dHv = 333.15, 30000.0
inv = 1 / T1b - R / dHv * math.log(0.8)
print("3. Tb = 60 C, dHvap = 30 kJ/mol, P -> 0.8 atm: T2 = %.2f K = %.2f C (change %.2f K)" % (1 / inv, 1 / inv - 273.15, 1 / inv - T1b))
print("4. 500 J from 400 K to 250 K: S_gen = %.3f J/K; rate form h = 5 W/K, 450 K and 300 K: Sdot_gen = h dT^2/(Ta Tb) = %.4f W/K" % (500 * (1 / 250 - 1 / 400), 5 * 150 ** 2 / (450 * 300)))
print("5. dH(298) = -92 kJ, dCp = -20 J/K/mol, 500 K: dH(500) = %.2f kJ/mol (298 -> 500 K, dT = 202)" % (-92 + (-0.020) * 202))
dG = -R * 298 * math.log(5.0)
print("6. K = 5.0 at 298 K, dS0 = -20 J/K/mol: dG0 = %.1f J/mol = %.3f kJ/mol; dH0 = dG0 + T dS0 = %.2f kJ/mol" % (dG, dG / 1000, (dG + 298 * (-20)) / 1000))
print("7. Hess: lattice dissociation +2000, solution -100, anion hydration -350 each (2 anions): cation hydration = %.0f kJ/mol" % (-100 - 2000 + 2 * 350))
print("8. Kirchhoff: dH(298) = -40 kJ, dCp = +3 J/K/mol -> 500 K: %.3f kJ/mol" % (-40 + 0.003 * 202))
q = 8.50 * 2.10
n = 0.800 / 180.0
dU = -q / n
print("9. bomb: 0.800 g, M = 180 g/mol, Ccal = 8.50 kJ/K, dT = 2.10 K, dn_g = +1: q = %.2f kJ, n = %.4e mol, dcU = %.1f kJ/mol, dcH = dcU + dn_g R T = %.1f kJ/mol" % (q, n, dU, dU + 1 * R * 298 / 1000))
qq = 150 * 4.18 * 6.0
print("10. 75 mL 1.0 M HCl + 75 mL 1.0 M NaOH, dT = 6.0 K, rho = 1.00 g/mL, c = 4.18: q = %.0f J, n = 0.075 mol, dH_neut = %.1f kJ/mol" % (qq, -qq / 0.075 / 1000))
print("11. Gibbs-Helmholtz sign check: d(G/T)/dT = -H/T^2: dG0/T at higher T is LESS negative for an exothermic reaction with dH = -60 kJ: %.2f -> %.2f J/K/mol (298.15 -> 400)" % (G1 / T1, gt))
print("12. ln K(T2)/K(T1) = -dH/R (1/T2 - 1/T1): dH0 = -60 kJ, 298.15 -> 400: ln ratio = %.3f, K ratio = %.4f" % (-H / R * (1 / T2 - 1 / T1) * -1 * -1, math.exp(-H / R * (1 / T2 - 1 / T1) * -1 * -1) if False else math.exp(-(H / R) * (1 / T2 - 1 / T1))))

print("\n== Proofs: Assignment 8 Q6, Assignment 9")
ok = all(sum(2 * i - 1 for i in range(1, n + 1)) == n * n for n in range(1, 200))
print("A8 Q6a sum of odd numbers = n^2 for n < 200:", ok)
ok = all(sum(i * math.factorial(i) for i in range(1, n + 1)) == math.factorial(n + 1) - 1 for n in range(1, 40))
print("A8 Q6b sum i i! = (n+1)! - 1 for n < 40:", ok)
print("A8 Q6c 6 | n^3 + 5n for n < 500:", all((n ** 3 + 5 * n) % 6 == 0 for n in range(1, 500)), "; inductive-step identity (k+1)^3 + 5(k+1) = k^3 + 5k + 3k(k+1) + 6:", all((k + 1) ** 3 + 5 * (k + 1) == k ** 3 + 5 * k + 3 * k * (k + 1) + 6 for k in range(1, 100)), "; without the +6 it fails at k = 1: %d vs %d" % ((2) ** 3 + 10, 1 + 5 + 6))
print("A8 Q6d 2^n > n^2 first holds for all n from:", [n for n in range(1, 40) if all(2 ** m > m * m for m in range(n, 60))][0], "; failures below 5:", [n for n in range(1, 5) if 2 ** n <= n * n], "(2^2 = 4 = 2^2, 2^3 = 8 < 9, 2^4 = 16 = 4^2); step k^2 - 2k - 1 > 0 for k >= 3")
a = {1: Fraction(1), 2: Fraction(3)}
for n in range(3, 60):
    a[n] = a[n - 1] + a[n - 2]
print("A9 Q1a a_n < (7/4)^n for n <= 59:", all(a[n] < Fraction(7, 4) ** n for n in a), "; base cases 1 < 7/4 = 1.75, 3 < 49/16 = %.4f; step 11/4 = 44/16 < 49/16" % (49 / 16), "; a_3..a_8 =", [int(a[n]) for n in range(3, 9)])
b = {1: 2, 2: 4}
for n in range(3, 40):
    b[n] = 4 * b[n - 1] - 4 * b[n - 2]
print("A9 Q1b b3, b4, b5 =", b[3], b[4], b[5], "; b_n = 2^n for n <= 39:", all(b[n] == 2 ** n for n in b), "; (n 2^n satisfies the recurrence but not b1 = 2: n=1 gives 2? ok b_n = n 2^n gives 2, 8: not 4)")
rep = lambda n: any((n - 5 * y) >= 0 and (n - 5 * y) % 3 == 0 for y in range(n // 5 + 1))
print("A9 Q1c every n in [8, 300] is 3x + 5y:", all(rep(n) for n in range(8, 301)), "; non-representable:", [n for n in range(0, 20) if not rep(n)], "; bases 8 = 3+5, 9 = 3*3, 10 = 5*2; Frobenius number 3*5-3-5 =", 3 * 5 - 3 - 5)
print("A9 Q3a every n in [2, 2000] has a prime divisor:", all(any(n % p == 0 for p in range(2, n + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))) for n in range(2, 2000)))
print("A9 Q3c no p, q with p^2 = 3 q^2 (q <= 3000):", not any(math.isqrt(3 * q * q) ** 2 == 3 * q * q for q in range(1, 3001)))
print("A9 Q4 n^2 + n even for n <= 500:", all((n * n + n) % 2 == 0 for n in range(1, 501)), "; (m-1)^2 + (m-1) = m^2 + m - 2m (same parity as m^2 + m)")
