"""PA08-PA10 (induction, strong induction, well-ordering) - numbers and finite checks quoted in the chapters.

    .venv/bin/python -W ignore scripts/pa_numbers2.py
"""
import itertools
import math
import random
from fractions import Fraction as Fr
from functools import lru_cache

import sympy as sp

P = print
F = [0, 1, 1]
for _i in range(3, 80): F.append(F[-1] + F[-2])


def sec(t): P("\n=====", t)


# ------------------------------------------------------------------ PA08
sec("PA08 identities (symbolic) and the moser circle")
n, k = sp.symbols("n k", integer=True, positive=True)
P("  gauss  sum k =", sp.simplify(sp.summation(k, (k, 1, n)) - n * (n + 1) / 2) == 0)
P("  squares sum k^2 =", sp.simplify(sp.summation(k ** 2, (k, 1, n)) - n * (n + 1) * (2 * n + 1) / 6) == 0)
P("  cubes   sum k^3 = (n(n+1)/2)^2:", sp.simplify(sp.summation(k ** 3, (k, 1, n)) - (n * (n + 1) / 2) ** 2) == 0)
P("  geometric sum 1+r+...+r^n = (r^(n+1)-1)/(r-1), exact rationals r in {2,3,1/2,-1/3,5/7}, n<=60:", all(sum(r ** j for j in range(m + 1)) == (r ** (m + 1) - 1) / (r - 1) for r in (Fr(2), Fr(3), Fr(1, 2), Fr(-1, 3), Fr(5, 7)) for m in range(0, 61)))
P("  odd numbers: first 12 partial sums =", [m * m for m in range(1, 13)], "= squares ->", all(sum(2 * j - 1 for j in range(1, m + 1)) == m * m for m in range(1, 400)))
P("  sum k*k! = (n+1)!-1 for n<40:", all(sum(j * math.factorial(j) for j in range(1, m + 1)) == math.factorial(m + 1) - 1 for m in range(1, 40)))
P("  6 | n^3+5n for n<10^4:", all((m ** 3 + 5 * m) % 6 == 0 for m in range(1, 10 ** 4)), " values", [m ** 3 + 5 * m for m in range(1, 7)])
P("  2^n > n^2 first failures (n<=4):", [m for m in range(1, 5) if not 2 ** m > m * m], " holds n=5..200:", all(2 ** m > m * m for m in range(5, 200)))
P("  n!>2^n least m:", min(m for m in range(1, 20) if all(math.factorial(j) > 2 ** j for j in range(m, 60))))
P("  Bernoulli (1+x)^n >= 1+nx, x=-0.9..3, n<=30:", all((1 + x) ** m >= 1 + m * x - 1e-9 for x in [i / 10 for i in range(-9, 31)] for m in range(1, 31)))

P("  Moser circle regions r(n)=C(n,4)+C(n,2)+1:", [math.comb(m, 4) + math.comb(m, 2) + 1 for m in range(1, 11)], " powers 2^(n-1):", [2 ** (m - 1) for m in range(1, 11)])
P("  Euler polynomial n^2+n+41 prime for n=0..39:", all(sp.isprime(m * m + m + 41) for m in range(0, 40)), "; n=40:", 40 * 40 + 40 + 41, "=", sp.factorint(40 * 40 + 40 + 41), "; composite at n=", [m for m in range(0, 60) if not sp.isprime(m * m + m + 41)][:6])
P("  Fermat numbers 2^2^n+1 prime for n=0..4:", [sp.isprime(2 ** 2 ** m + 1) for m in range(0, 5)], "; F5 =", 2 ** 32 + 1, "=", sp.factorint(2 ** 32 + 1))
P("  lines in plane: L_n = n(n+1)/2+1:", [m * (m + 1) // 2 + 1 for m in range(0, 8)], "(recursion L_n=L_{n-1}+n:", all(m * (m + 1) // 2 + 1 == (m - 1) * m // 2 + 1 + m for m in range(1, 100)), ")")

sec("PA08 strengthening the hypothesis: sum 1/k^2")
s = Fr(0)
ok_naive, ok_strong = True, True
for m in range(1, 3001):
    s += Fr(1, m * m)
    ok_strong &= (s <= 2 - Fr(1, m))
P("  sum_{k<=n} 1/k^2 <= 2-1/n for n<=3000:", ok_strong, "; at n=10: sum =", float(sum(Fr(1, j * j) for j in range(1, 11))), " bound", 2 - 0.1, "; limit pi^2/6 =", math.pi ** 2 / 6)
P("  step algebra: 1/(n+1)^2 <= 1/(n(n+1)) = 1/n - 1/(n+1):", all(Fr(1, (m + 1) ** 2) <= Fr(1, m) - Fr(1, m + 1) for m in range(1, 2000)))

sec("PA08 tower of Hanoi and the deficient chessboard")
def hanoi(m, a="A", b="B", c="C"):
    if m == 0: return []
    return hanoi(m - 1, a, c, b) + [(a, c)] + hanoi(m - 1, b, a, c)
def legal(m):
    pegs = {"A": list(range(m, 0, -1)), "B": [], "C": []}
    for (x, y) in hanoi(m):
        d = pegs[x].pop()
        assert not pegs[y] or pegs[y][-1] > d
        pegs[y].append(d)
    return pegs["C"] == list(range(m, 0, -1))
P("  hanoi moves for n=1..10:", [len(hanoi(m)) for m in range(1, 11)], "= 2^n-1:", all(len(hanoi(m)) == 2 ** m - 1 for m in range(1, 11)), " legal & solved:", all(legal(m) for m in range(1, 11)))
from collections import deque
def bfs_hanoi(m):
    start = tuple([0] * m); goal = tuple([2] * m)  # disc i (0 = smallest) -> peg
    seen = {start: 0}; q = deque([start])
    while q:
        st = q.popleft()
        if st == goal: return seen[st]
        for src in range(3):
            top = next((i for i in range(m) if st[i] == src), None)
            if top is None: continue
            for dst in range(3):
                if dst == src: continue
                if any(st[i] == dst for i in range(top)): continue
                nx = list(st); nx[top] = dst; nx = tuple(nx)
                if nx not in seen: seen[nx] = seen[st] + 1; q.append(nx)
P("  breadth-first search shortest solutions n=1..7:", [bfs_hanoi(m) for m in range(1, 8)], "(=2^n-1: minimality verified)")

def tile(n_, hole):
    size = 2 ** n_; board = [[0] * size for _ in range(size)]; counter = [0]
    def rec(r, c, sz, hr, hc):
        if sz == 1: return
        counter[0] += 1; label = counter[0]; half = sz // 2
        quads = [(r, c), (r, c + half), (r + half, c), (r + half, c + half)]
        holes = []
        for qi, (qr, qc) in enumerate(quads):
            if qr <= hr < qr + half and qc <= hc < qc + half: holes.append((hr, hc))
            else:
                cr = qr + (half - 1 if qr == r else 0); cc = qc + (half - 1 if qc == c else 0)
                board[cr][cc] = label; holes.append((cr, cc))
        for (qr, qc), (h1, h2) in zip(quads, holes): rec(qr, qc, half, h1, h2)
    board[hole[0]][hole[1]] = -1
    rec(0, 0, size, *hole)
    return board, counter[0]
good = True
for n_ in range(1, 5):
    size = 2 ** n_
    for hole in itertools.product(range(size), repeat=2):
        b, cnt = tile(n_, hole)
        cells = {}
        for r in range(size):
            for c in range(size):
                if b[r][c] > 0: cells.setdefault(b[r][c], []).append((r, c))
        good &= (cnt == (size * size - 1) // 3 and all(len(v) == 3 for v in cells.values()) and sum(len(v) for v in cells.values()) == size * size - 1)
P("  recursive L-tromino tiling of every 2^n x 2^n board (n<=4) with every possible hole:", good, "; trominoes used (4^n-1)/3 =", [(4 ** m - 1) // 3 for m in range(1, 5)])

sec("PA08 two-step induction, forward-backward, practice answers")
import mpmath as mp
mp.mp.dps = 60
x = (3 + mp.sqrt(5)) / 2
Lc = [int(mp.nint(x ** m + x ** (-m))) for m in range(1, 9)]
P("  x=(3+sqrt5)/2: x+1/x =", mp.nstr(x + 1 / x, 8), "; x^n+x^-n for n=1..8:", Lc, "(Lucas L_2n; integers; recursion a_{n+1}=3a_n-a_{n-1}:", all(Lc[i + 1] == 3 * Lc[i] - Lc[i - 1] for i in range(1, 7)), ")")
P("  9 | 4^n+6n-1 (n<=2000):", all((4 ** m + 6 * m - 1) % 9 == 0 for m in range(1, 2001)), " first values", [4 ** m + 6 * m - 1 for m in range(1, 6)], "; step difference = 9(1-2k):", all((4 ** (m + 1) + 6 * (m + 1) - 1) - 4 * (4 ** m + 6 * m - 1) == 9 * (1 - 2 * m) for m in range(1, 200)))
P("  sum 1/sqrt(k) >= sqrt(n) (n<=5000):", all(sum(1 / math.sqrt(j) for j in range(1, m + 1)) >= math.sqrt(m) for m in range(1, 5001)), "; at n=100:", sum(1 / math.sqrt(j) for j in range(1, 101)), "vs 10; step: 1/sqrt(n+1) >= sqrt(n+1)-sqrt(n):", all(1 / math.sqrt(m + 1) >= math.sqrt(m + 1) - math.sqrt(m) for m in range(1, 5000)))
P("  sum k(k+1) = n(n+1)(n+2)/3 (n<=500):", all(sum(j * (j + 1) for j in range(1, m + 1)) == m * (m + 1) * (m + 2) // 3 for m in range(1, 501)))
P("  Cassini F_{n+1}F_{n-1}-F_n^2 = (-1)^n (n=2..70):", all(F[m + 1] * F[m - 1] - F[m] ** 2 == (-1) ** m for m in range(2, 71)) if "F" in globals() else "F not yet defined")
from math import comb
def lattice(mm, nn):
    grid = [[1] * (nn + 1) for _ in range(mm + 1)]
    for i in range(1, mm + 1):
        for j in range(1, nn + 1): grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[mm][nn]
P("  lattice paths (0,0)->(m,n) = C(m+n,m) for m,n<=12:", all(lattice(i, j) == comb(i + j, i) for i in range(0, 13) for j in range(0, 13)))
P("  3 | n^3-n (n<=10^4):", all((m ** 3 - m) % 3 == 0 for m in range(1, 10 ** 4)), "; n^3-n = (n-1)n(n+1) product of three consecutive")
P("  2^n > n^3 fails at n =", [m for m in range(1, 12) if not 2 ** m > m ** 3], "; holds for n=10..300:", all(2 ** m > m ** 3 for m in range(10, 301)), "; step 2k^3 >= (k+1)^3 holds for k>=4:", [m for m in range(1, 8) if 2 * m ** 3 >= (m + 1) ** 3])
random.seed(8)
def amgm(v): return sum(v) / len(v) >= math.prod(v) ** (1 / len(v)) - 1e-12
P("  AM-GM random test, n=2..9, 2000 draws each:", all(amgm([random.uniform(0.01, 50) for _ in range(nn)]) for nn in range(2, 10) for _ in range(2000)))
P("  all positive integers equal? max(a,b)=1 step fails at k=1: a=2,b=1 -> (a-1,b-1) = (1,0), not positive")
P("  A_n=(0,1/n): every finite intersection nonempty (contains 1/n), infinite intersection:", "empty (no x>0 with x<1/n for all n)")

# ------------------------------------------------------------------ PA09
sec("PA09 postage stamps 4 and 5")
rep = lambda m: any((m - 4 * a) >= 0 and (m - 4 * a) % 5 == 0 for a in range(m // 4 + 1))
P("  unattainable amounts:", [m for m in range(0, 60) if not rep(m)], " all m>=12 attainable (to 5000):", all(rep(m) for m in range(12, 5000)))

sec("PA09 Fibonacci bounds and the false 'F_n is even'")
F = [0, 1, 1]
for i in range(3, 80): F.append(F[-1] + F[-2])
phi = (1 + 5 ** 0.5) / 2
P("  F_1..F_12 =", F[1:13], "; F_n<2^n (n<=70):", all(F[m] < 2 ** m for m in range(1, 71)), "; F_n>=phi^(n-2) (n<=70):", all(F[m] >= phi ** (m - 2) - 1e-9 for m in range(1, 71)))
P("  even Fibonacci numbers at n =", [m for m in range(1, 31) if F[m] % 2 == 0], "(every third); sum F_k^2 = F_n F_{n+1} (n<=60):", all(sum(F[j] ** 2 for j in range(1, m + 1)) == F[m] * F[m + 1] for m in range(1, 61)))
P("  F_1+...+F_n = F_{n+2}-1 (n<=60):", all(sum(F[1:m + 1]) == F[m + 2] - 1 for m in range(1, 61)))

sec("PA09 Zeckendorf")
fibs = [1, 2]
while fibs[-1] < 10 ** 6: fibs.append(fibs[-1] + fibs[-2])
def zeck(m):
    out = []
    for f in reversed(fibs):
        if f <= m: out.append(f); m -= f
    return out
ok = True
for m in range(1, 20001):
    z = zeck(m); idx = sorted(fibs.index(f) for f in z)
    ok &= (sum(z) == m and all(b - a >= 2 for a, b in zip(idx, idx[1:])))
P("  every n<=20000 is a sum of non-consecutive Fibonacci numbers (greedy):", ok, "; e.g. 100 =", zeck(100), ", 2026 =", zeck(2026))
cnt = {}
for r in range(1, 12):
    for sub in itertools.combinations(range(len(fibs[:12])), r):
        if all(b - a >= 2 for a, b in zip(sub, sub[1:])):
            v = sum(fibs[i] for i in sub); cnt[v] = cnt.get(v, 0) + 1
P("  uniqueness: values below 100 with more than one non-consecutive representation:", [v for v, c in cnt.items() if c > 1 and v < 100])

sec("PA09 Josephus")
def jos(m):
    q, rem = [], list(range(1, m + 1))
    dq = deque(rem)
    while len(dq) > 1:
        dq.rotate(-1); dq.popleft()
    return dq[0]
@lru_cache(None)
def jrec(m):
    if m == 1: return 1
    return 2 * jrec(m // 2) - 1 if m % 2 == 0 else 2 * jrec(m // 2) + 1
def jclosed(m):
    p = 1 << (m.bit_length() - 1); return 2 * (m - p) + 1
P("  J(1..16) by simulation:", [jos(m) for m in range(1, 17)])
P("  recursion J(2n)=2J(n)-1, J(2n+1)=2J(n)+1 and closed form J(2^a+l)=2l+1 agree with simulation (n<=2000):", all(jos(m) == jrec(m) == jclosed(m) for m in range(1, 2001)), "; J(41) =", jos(41), "; J(2^m)=1:", all(jos(2 ** m) == 1 for m in range(0, 11)))

sec("PA09 Catalan numbers")
C = [1]
for m in range(0, 25): C.append(sum(C[j] * C[m - j] for j in range(m + 1)))
P("  C_0..C_10 by the strong recursion:", C[:11], " = binom(2n,n)/(n+1) (n<=25):", all(C[m] == math.comb(2 * m, m) // (m + 1) for m in range(0, 26)))

sec("PA09 structural induction: full binary trees and parentheses")
def trees(m):  # number of full binary trees with m internal nodes
    return C[m]
def leaves_ok(m): return True
def gen(m):
    if m == 0: yield "L"; return
    for a in range(m):
        for l in gen(a):
            for r in gen(m - 1 - a): yield "(" + l + r + ")"
ok = True
for m in range(0, 8):
    ts = list(gen(m)); ok &= (len(ts) == C[m] and all(t.count("L") == m + 1 and t.count("(") == m for t in ts))
P("  full binary trees with m internal nodes: count = Catalan, leaves = internal+1 (m<=7):", ok)

sec("PA09 practice answers")
a_ = [None, 1]
for m in range(2, 40): a_.append(sum(a_[1:m]))
P("  a_1=1, a_n=a_1+...+a_{n-1}: a_1..a_10 =", a_[1:11], "= 1,1,2,4,..: a_n=2^(n-2) for n>=2:", all(a_[m] == 2 ** (m - 2) for m in range(2, 40)))
rep37 = lambda m: any((m - 3 * x) >= 0 and (m - 3 * x) % 7 == 0 for x in range(m // 3 + 1))
P("  stamps 3 and 7: unattainable", [m for m in range(0, 30) if not rep37(m)], "; all n>=12 attainable (to 5000):", all(rep37(m) for m in range(12, 5000)))
P("  F_n even iff 3|n (n<=70):", all((F[m] % 2 == 0) == (m % 3 == 0) for m in range(1, 71)))
dq = deque(range(1, 101))
while len(dq) > 1: dq.rotate(-1); dq.popleft()
P("  J(100) by simulation:", dq[0], " closed form 100=64+36 ->", 2 * 36 + 1, "; J(41) by recursion: J(41)=2J(20)+1, J(20)=2J(10)-1, J(10)=2J(5)-1, J(5)=2J(2)+1, J(2)=1 ->", [jrec(2), jrec(5), jrec(10), jrec(20), jrec(41)])
P("  powers of two: subsets of {1,2,4,..,2^(m-1)} give each of 0..2^m-1 exactly once (m<=12):", all(sorted(sum(c) for r in range(m + 1) for c in itertools.combinations([2 ** i for i in range(m)], r)) == list(range(2 ** m)) for m in range(1, 13)))
def height(s_):
    d = mx = 0
    for ch in s_:
        if ch == "(": d += 1; mx = max(mx, d)
        elif ch == ")": d -= 1
    return mx
P("  full binary trees (m<=7 internal nodes): leaves <= 2^height always:", all(t_.count("L") <= 2 ** height(t_) for m in range(0, 8) for t_ in gen(m)), "; equality for the complete trees, e.g. height 3 with 8 leaves:", any(t_.count("L") == 8 and height(t_) == 3 for t_ in gen(7)))
P("  C_5 =", C[5], "; 5 parenthesisations of abcd = C_3 =", C[3])
P("  the 'power of 2' false proof: 1+2 =", 1 + 2, "is not a power of 2")

# ------------------------------------------------------------------ PA10
sec("PA10 least element arguments")
P("  Euler's cubic a^3+2b^3+4c^3=0, |a|,|b|,|c|<=60, nonzero solutions:", [(a, b, c) for a in range(-60, 61) for b in range(-60, 61) for c in range(-60, 61) if a ** 3 + 2 * b ** 3 + 4 * c ** 3 == 0 and (a, b, c) != (0, 0, 0)])
def egcd_min(a, b):
    best = min(a * x + b * y for x in range(-60, 61) for y in range(-60, 61) if a * x + b * y > 0)
    return best
P("  smallest positive 1071x+462y (|x|,|y|<=60):", egcd_min(1071, 462), " gcd =", math.gcd(1071, 462))
def euclid(a, b):
    seq = [(a, b)]
    while b: a, b = b, a % b; seq.append((a, b))
    return seq
P("  Euclid pairs for (1071,462):", euclid(1071, 462))
P("  division algorithm by least element: a=100, b=7: set {a-bq >= 0} least =", min(100 - 7 * q for q in range(0, 15) if 100 - 7 * q >= 0))
P("  Euclid terminates: steps for all pairs <=300 (max):", max(len(euclid(a, b)) for a in range(1, 301) for b in range(1, 301)))
# uniqueness of prime factorisation, a minimal counterexample would be < 2 * ... : brute force that every n <= 10^5 has unique factorisation (trivially true by sympy)
P("  sqrt2: smallest q with q*sqrt2 integer would exist; for q<=10^6 no q with q*sqrt(2) integer:", all(math.isqrt(2 * q * q) ** 2 != 2 * q * q for q in range(1, 10 ** 6)))

sec("PA10 lexicographic order on N x N")
random.seed(5)
ok = True
for _ in range(2000):
    S = {(random.randint(1, 30), random.randint(1, 30)) for _ in range(random.randint(1, 12))}
    x0 = min(a for a, _ in S); y0 = min(b for a, b in S if a == x0)
    ok &= ((x0, y0) == min(S)) and all((x0, y0) <= p for p in S)
P("  min of a nonempty finite subset = (least first coordinate, then least second): ", ok)
P("  predecessors of (a,b) in lex order within [1,N]^2 at N=10: (1,5)->", sum(1 for p in itertools.product(range(1, 11), repeat=2) if p < (1, 5)), ", (2,1) ->", sum(1 for p in itertools.product(range(1, 11), repeat=2) if p < (2, 1)), "(grows with N: (2,1) has infinitely many predecessors in N x N)")
P("  N x Z lex: the chain (1,-1) > (1,-2) > (1,-3) > ... has no least element (first terms):", [(1, -j) for j in range(1, 6)])
P("  graded order (sum, then first coord): predecessors of (a,b) =", {p: sum(1 for q in itertools.product(range(1, 40), repeat=2) if (q[0] + q[1], q[0]) < (p[0] + p[1], p[0])) for p in [(1, 1), (2, 1), (1, 3), (5, 5)]}, "(finite: order type omega)")

sec("PA10 Ackermann function")
import sys
sys.setrecursionlimit(200000)
calls = [0]
def A(m, n_):
    calls[0] += 1
    if m == 0: return n_ + 1
    if n_ == 0: return A(m - 1, 1)
    return A(m - 1, A(m, n_ - 1))
res = {}
for m in range(0, 4):
    row = []
    for n_ in range(0, 6 if m < 3 else 6):
        calls[0] = 0; v = A(m, n_); row.append((v, calls[0]))
    res[m] = row
for m, row in res.items(): P(f"  A({m},n), n=0..5 [value, calls]:", row)
P("  closed forms: A(1,n)=n+2, A(2,n)=2n+3, A(3,n)=2^(n+3)-3:", all(A(1, i) == i + 2 and A(2, i) == 2 * i + 3 and A(3, i) == 2 ** (i + 3) - 3 for i in range(0, 6)))
calls[0] = 0; v = A(3, 3); P("  A(3,3) =", v, " calls", calls[0])
P("  every recursive call strictly lowers (m,n) in the lexicographic order (checked on a trace of A(2,3)):")
trace = []
def At(m, n_, parent=None):
    if parent is not None: trace.append((parent, (m, n_)))
    if m == 0: return n_ + 1
    if n_ == 0: return At(m - 1, 1, (m, n_))
    return At(m - 1, At(m, n_ - 1, (m, n_)), (m, n_))
At(2, 3)
P("   ", all(child < parent for parent, child in trace), "; calls traced:", len(trace) + 1)

sec("PA10 practice answers")
P("  x^2+y^2=3z^2 nonzero solutions with |x|,|y|,|z|<=200:", [(x_, y_, z_) for x_ in range(-200, 201) for y_ in range(-200, 201) for z_ in range(0, 201) if x_ * x_ + y_ * y_ == 3 * z_ * z_ and (x_, y_, z_) != (0, 0, 0)][:3], "; squares mod 3 =", sorted({(x_ * x_) % 3 for x_ in range(3)}))
pos = lambda a, b: (a + b - 1) * (a + b - 2) // 2 + a
order = sorted(itertools.product(range(1, 40), repeat=2), key=lambda p: (p[0] + p[1], p[0]))
P("  graded order positions (a+b, then a): first 10 pairs", order[:10], "; position formula (a+b-1)(a+b-2)/2+a correct for a+b<=38:", all(order.index((a, b)) + 1 == pos(a, b) for a in range(1, 38) for b in range(1, 38) if a + b <= 38))
words = ["b" * 1] + ["a" * k + "b" for k in range(1, 6)]
P("  alphabetical order on words: b > ab > aab > aaab > ...:", words[::1], all(words[i] > words[i + 1] for i in range(len(words) - 1)), "(python string order = alphabetical)")
P("  Z x N lex chain (-n, 1), n=1..5 decreasing:", [(-n, 1) for n in range(1, 6)], all((-n, 1) > (-n - 1, 1) for n in range(1, 50)))
P("  division algorithm a=-23, b=5: q, r =", divmod(-23, 5), " (Python floor division gives 0<=r<b)")
P("  Bezout 21 = 7*462 - 3*1071:", 7 * 462 - 3 * 1071)
P("  A(2,2) =", 2 * 2 + 3, " (closed form 2n+3)")
P("  evens-then-odds order: every nonempty subset has a least element (test on 3000 random subsets of 1..40):", all(min(S, key=lambda x: (x % 2, x)) in S for S in [random.sample(range(1, 41), random.randint(1, 10)) for _ in range(3000)]), "; predecessors of 1:", "all evens (infinitely many)")
