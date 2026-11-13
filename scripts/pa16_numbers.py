"""PA16 Peano's axioms, PA17 Binary operations and groups (Assignment 10), Proofs mid-sem 2026: every claim checked by brute force.
    .venv/bin/python -W ignore scripts/pa16_numbers.py
"""
import cmath
import itertools
import math

print("== PA16: Peano arithmetic built from the successor only (numbers are Python ints used only as names of s^k(1))")
N = range(1, 41)
s = lambda n: n + 1                 # the successor; + is NOT used below except through s
one = 1
def add(n, m):                      # n + 1 := s(n);  n + s(m') := s(n + m')   (m = s(m'))
    if m == one:
        return s(n)
    return s(add(n, m - 1))         # m - 1 = the unique predecessor (Lemma 1)
def mul(n, m):                      # n*1 := n;  n*(m'+1) := n*m' + n
    if m == one:
        return n
    return add(mul(n, m - 1), n)
print("  2 + 2 =", add(2, 2), "(= 4); 3 * 4 =", mul(3, 4))
print("  Lemma 1: every n != 1 has exactly one predecessor:", all(sum(1 for m in N if s(m) == n) == 1 for n in range(2, 41)), "; 1 has none:", not any(s(m) == 1 for m in N))
print("  Theorem 3 (1 + n = n + 1):", all(add(1, n) == add(n, 1) for n in N))
print("  Theorem 4 (associativity), all triples up to 15:", all(add(add(a, b), c) == add(a, add(b, c)) for a in range(1, 16) for b in range(1, 16) for c in range(1, 16)))
print("  commutativity, up to 40:", all(add(a, b) == add(b, a) for a in N for b in N))
print("  cancellation a + c = b + c => a = b, up to 25:", all(a == b for a in range(1, 26) for b in range(1, 26) for c in range(1, 26) if add(a, c) == add(b, c)))
less = lambda a, b: any(add(a, x) == b for x in range(1, 80))
print("  Theorem 5 (a < b => a + 1 <= b), up to 40:", all((not less(a, b)) or add(a, 1) <= b for a in N for b in N))
print("  trichotomy (exactly one of <, =, >), up to 30:", all(sum([less(a, b), a == b, less(b, a)]) == 1 for a in range(1, 31) for b in range(1, 31)))
print("  no n < 1:", not any(less(n, 1) for n in N), "; a + z != a for all a, z up to 40:", all(add(a, z) != a for a in N for z in N))
print("  multiplication: n*1 = 1*n:", all(mul(n, 1) == mul(1, n) for n in range(1, 16)), "; a(b+c) = ab + ac, up to 8:", all(mul(a, add(b, c)) == add(mul(a, b), mul(a, c)) for a in range(1, 9) for b in range(1, 9) for c in range(1, 9)),
      "; commutative:", all(mul(a, b) == mul(b, a) for a in range(1, 11) for b in range(1, 11)), "; associative:", all(mul(mul(a, b), c) == mul(a, mul(b, c)) for a in range(1, 7) for b in range(1, 7) for c in range(1, 7)))

print("\n== non-examples (finite): check P1 (1 not in Im s), P2 (s injective), P3 (closure from 1 reaches all)")
def axioms(X, s, one):
    P1 = one not in {s[x] for x in X}
    P2 = len({s[x] for x in X}) == len(X)
    reach, cur = set(), one
    while cur not in reach:
        reach.add(cur)
        cur = s[cur]
    P3 = reach == set(X)
    return P1, P2, P3
print("  X = {1}, s(1) = 1:       (P1, P2, P3) =", axioms([1], {1: 1}, 1))
print("  X = {1,2}, s(1) = 2 = s(2): (P1, P2, P3) =", axioms([1, 2], {1: 2, 2: 2}, 1))
print("  X = {1,2,3}, s = 1->2->3->1: (P1, P2, P3) =", axioms([1, 2, 3], {1: 2, 2: 3, 3: 1}, 1), "(a cycle: P1 fails, so a finite set cannot be a Peano system)")
print("  X = {1,2,3} + a cycle {a,b}, s(1)=2, s(2)=3, s(3)=3?? not used; two-component model (N and a copy N') is infinite: P3 fails because S = N is closed and proper")

print("\n== ZFC model: 0 = emptyset, s(x) = x U {x} (von Neumann naturals)")
zero = frozenset()
nats = [zero]
for _ in range(7):
    x = nats[-1]
    nats.append(x | frozenset([x]))
print("  sizes |s^k(0)| =", [len(x) for x in nats], "; s injective on these:", len({n for n in nats}) == len(nats) and all(nats[i + 1] != nats[j + 1] for i in range(7) for j in range(i)), "; 0 is no successor:", all(nats[i + 1] != zero for i in range(7)))
print("  x in s(x) and x subset s(x) for each:", all(nats[i] in nats[i + 1] and nats[i] <= nats[i + 1] for i in range(7)), "; n < m iff n in m (checked up to 7):", all((i < j) == (nats[i] in nats[j]) for i in range(8) for j in range(8)))

print("\n== PA17: groups")
mu = lambda n: [cmath.exp(2j * math.pi * k / n) for k in range(n)]
close = lambda a, L: any(abs(a - b) < 1e-9 for b in L)
for n in (4, 6, 12):
    G = mu(n)
    print("  mu_%d: closed %s, inverses %s, commutative %s, |mu_n| = %d" % (n, all(close(a * b, G) for a in G for b in G), all(close(1 / a, G) for a in G), all(abs(a * b - b * a) < 1e-12 for a in G for b in G), len(G)))
tab = [[round((a * b).real) + round((a * b).imag) * 1j for b in mu(4)] for a in mu(4)]
print("  mu_4 = {1, i, -1, -i}: multiplication table (rows/columns in this order):")
names = {1: "1", 1j: "i", -1: "-1", -1j: "-i"}
for r in tab:
    print("   ", [names[complex(x)] for x in r])
import random
random.seed(1)
S1 = [cmath.exp(1j * random.uniform(0, 2 * math.pi)) for _ in range(500)]
print("  S^1: |zw| = 1:", all(abs(abs(a * b) - 1) < 1e-12 for a, b in itertools.product(S1[:60], S1[:60])), "; z^{-1} = conj(z):", all(abs(1 / a - a.conjugate()) < 1e-12 for a in S1))
import numpy as np
T = lambda a: np.array([[1.0, a], [0.0, 1.0]])
print("  T: T(a) T(b) = T(a+b):", all(np.allclose(T(a) @ T(b), T(a + b)) for a, b in [(1.3, -0.4), (2, 5), (-7.1, 0.5)]), "; inverse T(-a):", np.allclose(T(2.5) @ T(-2.5), np.eye(2)), "; T(a)T(b) = T(b)T(a):", np.allclose(T(1.3) @ T(-0.4), T(-0.4) @ T(1.3)))

def symmetries(points):
    """vertex permutations preserving all pairwise distances (= rigid symmetries of the polygon with labelled vertices)"""
    n = len(points)
    D = [[round(math.dist(points[i], points[j]), 9) for j in range(n)] for i in range(n)]
    out = []
    for p in itertools.permutations(range(n)):
        if all(D[i][j] == D[p[i]][p[j]] for i in range(n) for j in range(n)):
            out.append(p)
    return out
def compose(f, g):                  # f o g: first g, then f
    return tuple(f[g[i]] for i in range(len(f)))
def info(name, pts):
    G = symmetries(pts)
    closed = all(compose(f, g) in G for f in G for g in G)
    abel = all(compose(f, g) == compose(g, f) for f in G for g in G)
    print("  %-26s |Sym| = %2d, closed %s, abelian %s" % (name, len(G), closed, abel))
    return G
tri = [(math.cos(2 * math.pi * k / 3 + math.pi / 2), math.sin(2 * math.pi * k / 3 + math.pi / 2)) for k in range(3)]
G3 = info("equilateral triangle", tri)
print("    elements (0-based vertex permutations):", G3)
cyc = lambda p: p
rect = [(2, 1), (-2, 1), (-2, -1), (2, -1)]
Gr = info("rectangle (2x1)", rect)
print("    elements:", Gr)
sq = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
Gs = info("square", sq)
print("    elements:", Gs)
print("  S_3 has 6 elements (all of them are symmetries of the triangle); S_4 has 24, of which only %d (rectangle) / %d (square) are symmetries" % (len(Gr), len(Gs)))
f, g = (1, 2, 0), (1, 0, 2)
print("  triangle: f = (1 2 3) (rotation), g = (1 2) (reflection): f.g = %s, g.f = %s -> not commutative" % (compose(f, g), compose(g, f)))
orders = lambda G: sorted(len({tuple(range(len(G[0])))} | {p for k in range(1, 9) for p in [tuple(range(len(G[0])))] if False}) for _ in [0])
print("  order check: rectangle group elements all have order <= 2:", all(compose(p, p) == tuple(range(4)) for p in Gr), "(Klein four-group); square has an element of order 4:", any(compose(compose(p, p), compose(p, p)) == tuple(range(4)) and compose(p, p) != tuple(range(4)) for p in Gs))

print("\n== Mid-sem 2026 (MT2133)")
print("  Q2 truth table P ^ (P=>Q) => Q:", [(P, Q, ((not P) or Q), P and ((not P) or Q), (not (P and ((not P) or Q))) or Q) for P in (True, False) for Q in (True, False)])
print("  Q3(a) 'for all x in R exists y: y^2 = x' false at x = -1 (y^2 >= 0 for sampled y):", all(y * y != -1 for y in np.linspace(-100, 100, 20001)))
print("  Q3(b) x odd => x^2 odd for |x| <= 1000:", all((x * x) % 2 == 1 for x in range(-1000, 1001) if x % 2))
print("  Q4(a) A = {} , B = {1}: A x B == B x A == empty:", list(itertools.product([], [1])) == list(itertools.product([1], [])) == [])
print("  Q4(b) S = {2,3} under divisibility: minimum exists?", [m for m in (2, 3) if all(s % m == 0 for s in (2, 3))], "; minimal elements:", [m for m in (2, 3) if not any(t != m and m % t == 0 for t in (2, 3))])
print("  Q4(c) a = b mod n => a^2 = b^2 mod n (n <= 12, |a|,|b| <= 30):", all((a * a - b * b) % n == 0 for n in range(1, 13) for a in range(-30, 31) for b in range(-30, 31) if (a - b) % n == 0))
U = set(range(0, 12)); A, B, C = set(range(0, 12)), {1, 2, 3, 5}, {2, 4, 6, 7}
print("  Q5 A-(B u C) = (A-B) n (A-C) on a sample:", A - (B | C) == (A - B) & (A - C))
W = range(-60, 61)
An = lambda n: {x for x in W if x % n == 0}
print("  Q6 A_n = nZ on [-60,60]: union over n=1..61 = whole window:", set().union(*[An(n) for n in range(1, 62)]) == set(W), "; intersection over n=1..61 = {0}:", set.intersection(*[An(n) for n in range(1, 62)]) == {0})
print("  Q7(b) 100 = 14*7 + 2, [100] = [2] mod 7:", divmod(100, 7), "; elements near 0:", sorted(x for x in range(-14, 20) if (x - 100) % 7 == 0))
# Q8: lub from glb in a finite poset (divisibility on 1..30), S with an upper bound
from math import gcd
Aset = range(1, 61)
leq = lambda a, b: b % a == 0
def glb(Sub):
    lbs = [x for x in Aset if all(leq(x, y) for y in Sub)]
    g = [x for x in lbs if all(leq(y, x) for y in lbs)]
    return g[0] if g else None
S = [4, 6]
Ub = [g for g in Aset if all(leq(s, g) for s in S)]
alpha = glb(Ub)
print("  Q8 divisibility poset on 1..60, S = {4,6}: U = upper bounds = multiples of 12 ->", Ub[:5], "...; glb(U) =", alpha, "= lub(S) = lcm(4,6) =", 12)
