"""TD2213 Tutorial 3 (probability and microstates): every number recomputed.   .venv/bin/python -W ignore scripts/th_t3_numbers.py"""
import itertools
import math
from fractions import Fraction

print("== Q1: two distinguishable dice")
S = list(itertools.product(range(1, 7), repeat=2))
A = [s for s in S if s[0] % 2 == 0 and s[1] % 2 == 1]
B = [s for s in S if s[0] == 2 or s[1] == 5]
C = [s for s in S if (s[0] % 2 == 0 and s[1] % 2 == 1) or s[0] == s[1]]
print("  (a) even AND odd: %d/36 = %s; (b) red 2 OR blue 5: %d/36 (inclusion-exclusion 6+6-1 = 11); (c) %d/36 = %s = %.4f" % (len(A), Fraction(len(A), 36), len(B), len(C), Fraction(len(C), 36), len(C) / 36))
print("  overlap of the two events in (c): %d outcomes; (a) as a product (1/2)(1/2) = %.2f; P(red even OR blue odd) = %d/36" % (len([s for s in A if s[0] == s[1]]), 0.25, len([s for s in S if s[0] % 2 == 0 or s[1] % 2 == 1])))

print("\n== Q2: W_MPD for a two-, three- and M-level system with no energy constraint")
def lnW(N, M):
    return math.lgamma(N + 1) - M * math.lgamma(N / M + 1)
for N in (10, 100, 1000, 10 ** 6):
    lw = lnW(N, 2)
    print("  M = 2, N = %7d: ln W_MPD = %.4f, N ln 2 = %.4f, difference %.4f (Stirling: -1/2 ln(pi N/2) = %.4f); W_MPD/2^N = %.5f (sqrt(2/(pi N)) = %.5f)" % (
        N, lw, N * math.log(2), lw - N * math.log(2), -0.5 * math.log(math.pi * N / 2), math.exp(lw - N * math.log(2)), math.sqrt(2 / (math.pi * N))))
for N in (30, 300, 3000, 300000):
    lw = lnW(N, 3)
    print("  M = 3, N = %6d: ln W_MPD = %.4f, N ln 3 = %.4f, ratio ln W_MPD / ln W_total = %.6f; W_MPD/3^N = %.3e (3 sqrt3/(2 pi N) = %.3e)" % (
        N, lw, N * math.log(3), lw / (N * math.log(3)), math.exp(lw - N * math.log(3)), 3 * math.sqrt(3) / (2 * math.pi * N)))
for M, N in ((6, 600), (10, 1000)):
    lw = lnW(N, M)
    print("  M = %2d, N = %5d: ln W_MPD = %.3f, N ln M = %.3f; W_MPD/M^N = %.3e (M^{M/2}/(2 pi N)^{(M-1)/2} = %.3e)" % (M, N, lw, N * math.log(M), math.exp(lw - N * math.log(M)), M ** (M / 2) / (2 * math.pi * N) ** ((M - 1) / 2)))
print("  check of the two-level maximum: ln W(N1) with N = 100: argmax over integer N1 = %d; second derivative d2(lnW)/dN1^2 = -N/(N1 (N-N1)) = %.4f at N1 = 50" % (max(range(0, 101), key=lambda n: math.lgamma(101) - math.lgamma(n + 1) - math.lgamma(101 - n)), -100 / (50 * 50)))
print("  the sheet says N must be EVEN for an M-level system: the correct condition is that N is divisible by M (e.g. N = 9, M = 3 works, N = 8, M = 4 works, N = 10, M = 4 does not)")

print("\n== Q3: three distinguishable particles, five equally spaced levels E = 0..4, total energy 5")
assign = [t for t in itertools.product(range(5), repeat=3) if sum(t) == 5]
from collections import Counter
dist = Counter(tuple(sorted(t)) for t in assign)
print("  ordered assignments with sum 5: %d (= total microstates); distributions (multisets of levels): %d" % (len(assign), len(dist)))
for k, v in sorted(dist.items()):
    occ = tuple(k.count(i) for i in range(5))
    print("    levels %s  occupations (n0..n4) = %s  W = 3!/prod n_i! = %d  (enumeration %d)" % (k, occ, math.factorial(3) // math.prod(math.factorial(x) for x in occ), v))
print("  total W = %d" % sum(dist.values()))
print("  identical bosons: %d microstates (one per distribution); identical fermions (all levels distinct): %d microstates %s" % (len(dist), sum(1 for k in dist if len(set(k)) == 3), [k for k in dist if len(set(k)) == 3]))
print("  Boltzmann (classical, indistinguishable, dilute) count would be W/N! = %d/6 = %.2f (an integer by coincidence; it lies between the fermion count 2 and the boson count 4)" % (sum(dist.values()), sum(dist.values()) / 6))
print("  most probable distribution: %s with W = %d of 18 = %.3f" % (max(dist.items(), key=lambda kv: kv[1] if True else 0)[0], max(dist.values()), max(dist.values()) / 18))
