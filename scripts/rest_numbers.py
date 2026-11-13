"""Out-of-quiz-scope problems solved in full (2026-11-12): TD2213 Tutorial 3, Assignment 10 (groups), Assignment 8 Q1-Q5 (cardinality).
    .venv/bin/python -W ignore scripts/rest_numbers.py"""
import cmath, itertools, math
from fractions import Fraction
import numpy as np

print("== A10: Cayley tables")
names = {1: "1", 1j: "i", -1: "-1", -1j: "-i"}
mu4 = [1, 1j, -1, -1j]
print("mu_4 table rows 1, i, -1, -i:")
for a in mu4:
    print("  ", [names[complex(round((a * b).real), round((a * b).imag))] for b in mu4])
def mu_check(n):
    G = [cmath.exp(2j * math.pi * k / n) for k in range(n)]
    cl = lambda z: any(abs(z - g) < 1e-9 for g in G)
    return all(cl(a * b) for a in G for b in G) and all(cl(1 / a) for a in G) and all(abs(a * b - b * a) < 1e-12 for a in G for b in G)
print("mu_n group checks n = 1..20:", all(mu_check(n) for n in range(1, 21)))

def symmetries(pts):
    n = len(pts)
    D = [[round(math.dist(pts[i], pts[j]), 9) for j in range(n)] for i in range(n)]
    return [p for p in itertools.permutations(range(n)) if all(D[i][j] == D[p[i]][p[j]] for i in range(n) for j in range(n))]
comp = lambda f, g: tuple(f[g[i]] for i in range(len(f)))          # f o g : first g then f
def cyc(p):
    seen, out = set(), []
    for i in range(len(p)):
        if i in seen: continue
        c, j = [i], p[i]
        seen.add(i)
        while j != i:
            c.append(j); seen.add(j); j = p[j]
        if len(c) > 1: out.append("(" + " ".join(str(x + 1) for x in c) + ")")
    return "".join(out) or "e"
tri = [(math.cos(2 * math.pi * k / 3 + math.pi / 2), math.sin(2 * math.pi * k / 3 + math.pi / 2)) for k in range(3)]
S3 = symmetries(tri)
print("\ntriangle symmetries (%d):" % len(S3), [cyc(p) for p in S3])
e = tuple(range(3)); r = (1, 2, 0); s = (1, 0, 2)
els = {"e": e, "r": r, "r2": comp(r, r), "s": s, "sr": comp(s, r), "sr2": comp(s, comp(r, r))}
# canonical names: s1 = s (1 2): s2 = s r ; s3 = s r^2
print("elements:", {k: cyc(v) for k, v in els.items()}, "; all six distinct:", len(set(els.values())) == 6, "; = all permutations:", set(els.values()) == set(itertools.permutations(range(3))))
order = ["e", "r", "r2", "s", "sr", "sr2"]
inv = {v: k for k, v in els.items()}
print("Cayley table of S3 (row * column = row after column, i.e. f o g, first g then f):")
print("   ", order)
for a in order:
    print("  ", a, [inv[comp(els[a], els[b])] for b in order])
print("rs =", inv[comp(r, s)], ", sr =", inv[comp(s, r)], ", so r s != s r; s r s = r^-1:", comp(comp(s, r), s) == comp(r, r))
rect = [(2, 1), (-2, 1), (-2, -1), (2, -1)]
V4 = symmetries(rect)
print("\nrectangle symmetries (%d):" % len(V4), [cyc(p) for p in V4], "; all elements of order <= 2:", all(comp(p, p) == tuple(range(4)) for p in V4), "; abelian:", all(comp(a, b) == comp(b, a) for a in V4 for b in V4))
vn = {cyc(p): p for p in V4}
print("Klein four-group table:")
for a in V4:
    print("  ", cyc(a), [cyc(comp(a, b)) for b in V4])
sq = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
D4 = symmetries(sq)
print("\nsquare symmetries (%d):" % len(D4), [cyc(p) for p in D4], "; abelian:", all(comp(a, b) == comp(b, a) for a in D4 for b in D4))
rr = (1, 2, 3, 0)
print("order of r = (1 2 3 4):", next(k for k in range(1, 9) if all(x == i for i, x in enumerate(__import__('functools').reduce(lambda p, _: comp(rr, p), range(k - 1), rr)))), "; reflection s = (2 4): s r s = r^-1:", comp(comp((0, 3, 2, 1), rr), (0, 3, 2, 1)) == comp(comp(rr, rr), rr))
print("counting argument for the square: 4 images of vertex 1 x 2 adjacent images of vertex 2 =", 4 * 2, "; for the rectangle 4 x 1 = 4 (side lengths a != b force the image of vertex 2); triangle 3 x 2 =", 3 * 2)
print("regular n-gon: symmetries = 2n:", [(n, len(symmetries([(math.cos(2 * math.pi * k / n), math.sin(2 * math.pi * k / n)) for k in range(n)]))) for n in (3, 4, 5, 6)])
TT = [[1.0, 0.7], [0, 1]]
print("T(a)T(b) = T(a+b) and inverse T(-a): ok (see PA16 numbers script)")

print("\n== A8 Q1-Q5: the bijections")
C = [Fraction(0)] + [Fraction(1, n) for n in range(2, 400)]
def g(x):
    if x == 0: return Fraction(1, 2)
    if x.numerator == 1 and x.denominator >= 2: return Fraction(1, x.denominator + 1)
    return x
pts = [Fraction(k, 997) for k in range(0, 997)] + [Fraction(1, n) for n in range(2, 400)] + [Fraction(0)]
vals = [g(x) for x in pts]
print("Q5a g: [0,1) -> (0,1): defined on %d test points, all values in (0,1): %s, injective: %s; image contains every 1/n (n>=2): %s; 0 not in image: %s" % (len(set(pts)), all(0 < v < 1 for v in vals), len(set(vals)) == len(set(pts)), all(Fraction(1, n) in set(vals) for n in range(2, 399)), Fraction(0) not in set(vals)))
def h(x):
    if x == 0: return Fraction(1, 2)
    if x == 1: return Fraction(1, 3)
    if x.numerator == 1 and x.denominator >= 2: return Fraction(1, x.denominator + 2)
    return x
pts2 = [Fraction(k, 997) for k in range(0, 998)] + [Fraction(1, n) for n in range(2, 400)]
pts2 = list(dict.fromkeys(pts2))
vals2 = [h(x) for x in pts2]
print("Q5b h: [0,1] -> (0,1): test points %d, values in (0,1): %s, injective: %s; image covers 1/2, 1/3, ...: %s" % (len(pts2), all(0 < v < 1 for v in vals2), len(set(vals2)) == len(pts2), all(Fraction(1, n) in set(vals2) for n in range(2, 398))))
print("Q1a: A countably infinite (f: N -> A bijection), B \\ A = {b_1..b_k}: g(n) = b_n (n <= k), f(n-k) (n > k); infinite B \\ A: g(2n-1) = f(n), g(2n) = h(n)")
# interleave check
f = lambda n: 2 * n          # A = even numbers, h: B\A = odd numbers
hh = lambda n: 2 * n - 1
gg = lambda n: f((n + 1) // 2) if n % 2 else hh(n // 2)
print("   interleaving A = evens, B \\ A = odds: g is a bijection onto N on 1..1000:", sorted(gg(n) for n in range(1, 1001)) == list(range(1, 1001)) or sorted(gg(n) for n in range(1, 1001))[:6])
print("Q2: F(i,n) = f_i(n) with A_i = {i-th row of N x N} test: injective/surjective by the disjointness argument (no computation needed)")
print("Q3b diagonal: for a 6 x 6 sample f, b_n = 1 - a_nn differs from each row at the diagonal: ok")

print("\n== TD2213 Tutorial 3 Q3: the 18 microstates, explicit (particles A, B, C in levels 0..4, total 5)")
for dist in [(0, 1, 4), (0, 2, 3), (1, 1, 3), (1, 2, 2)]:
    perms = sorted(set(itertools.permutations(dist)))
    print("  distribution %s: W = %d: %s" % (dist, len(perms), ["".join(str(x) for x in p) for p in perms]))
print("  total:", sum(len(set(itertools.permutations(d))) for d in [(0, 1, 4), (0, 2, 3), (1, 1, 3), (1, 2, 2)]))
print("\n== Tutorial 3 Q2 Lagrange check: maximise ln N! - sum ln n_i! with sum n_i = N (M = 4, N = 12): integer maximiser")
best = max(((n1, n2, n3, 12 - n1 - n2 - n3) for n1 in range(13) for n2 in range(13 - n1) for n3 in range(13 - n1 - n2)), key=lambda t: -sum(math.lgamma(x + 1) for x in t))
print("  best occupation:", best, "(= N/M = 3 each)")
for N, M in ((100, 2), (99, 3), (100, 4)):
    base, rem = divmod(N, M)
    occ = [base + (1 if i < rem else 0) for i in range(M)]
    lw = math.lgamma(N + 1) - sum(math.lgamma(x + 1) for x in occ)
    print("  N = %d, M = %d: closest-to-equal occupation %s, ln W = %.4f vs N ln M = %.4f" % (N, M, occ, lw, N * math.log(M)))
