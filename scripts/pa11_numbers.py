"""PA11 Subspaces, Products and Quotients: numbers quoted in the chapter, recomputed.

    .venv/bin/python -W ignore scripts/pa11_numbers.py
"""
import itertools

import numpy as np


# 1. Finite topologies: the product of two Sierpinski spaces ------------------------------------------------------------
def generated_topology(points, basis):
    """All unions of members of `basis` (plus the empty set); `points` is only used to add the whole space check."""
    basis = [frozenset(b) for b in basis]
    opens = {frozenset()}
    for r in range(1, len(basis) + 1):
        for combo in itertools.combinations(basis, r):
            opens.add(frozenset().union(*combo))
    return opens


S = frozenset({0, 1})
S_opens = {frozenset(), frozenset({1}), S}                       # Sierpinski space {0,1}, open sets: {}, {1}, {0,1}
pts = {(a, b) for a in S for b in S}
basis = [frozenset((a, b) for a in U for b in V) for U in S_opens for V in S_opens]
prod = generated_topology(pts, basis)
print("Sierpinski x Sierpinski: %d products U x V, %d distinct open sets" % (len({b for b in basis}), len(prod)))
print("  open sets:", sorted(sorted(o) for o in prod))
# subspace topology of {0,1} x {1} inside S x S  (a copy of S)
A = {(0, 1), (1, 1)}
sub = {frozenset(o & A) for o in prod}
print("subspace topology on %s has %d open sets" % (sorted(A), len(sub)))

# 2. Gluing a square: vertices, edges, faces and Euler characteristic ---------------------------------------------------


def euler_characteristic(word):
    """word: list of (letter, sign) read around the boundary of ONE polygon; returns (V, E, F, chi)."""
    n = len(word)
    parent = list(range(n))                     # polygon corner i is the start of edge i; corner (i+1) % n is its end

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)

    seen = {}
    for i, (c, sgn) in enumerate(word):
        tail, head = (i, (i + 1) % n) if sgn > 0 else ((i + 1) % n, i)
        if c in seen:
            t0, h0 = seen[c]
            union(tail, t0)
            union(head, h0)
        else:
            seen[c] = (tail, head)
    V = len({find(i) for i in range(n)})
    E = len(seen)
    return V, E, 1, V - E + 1


words = {
    "sphere  a a^-1 b b^-1": [("a", 1), ("a", -1), ("b", 1), ("b", -1)],
    "torus   a b a^-1 b^-1": [("a", 1), ("b", 1), ("a", -1), ("b", -1)],
    "Klein   a b a^-1 b": [("a", 1), ("b", 1), ("a", -1), ("b", 1)],
    "RP^2    a b a b": [("a", 1), ("b", 1), ("a", 1), ("b", 1)],
}
for name, w in words.items():
    V, E, F, chi = euler_characteristic(w)
    print("%-24s V=%d E=%d F=%d  chi=%d" % (name, V, E, F, chi))

# 3. The figure-eight curve beta(t) = (sin 2t, sin t) on (-pi, pi) (Lee Example 4.19) ------------------------------------
t = np.linspace(-np.pi + 1e-6, np.pi - 1e-6, 400001)
x, y = np.sin(2 * t), np.sin(t)
# injectivity: sort by (x, y), look at neighbouring image points that come from far-apart parameters
order = np.lexsort((y, x))
xs, ys, ts = x[order], y[order], t[order]
close = (np.abs(np.diff(xs)) < 1e-9) & (np.abs(np.diff(ys)) < 1e-9) & (np.abs(np.diff(ts)) > 1e-3)
print("figure-eight: pairs of distinct parameters with the same image on the grid:", int(close.sum()))
for d in (1e-1, 1e-2, 1e-3):
    tt = np.pi - d
    print("  t = pi - %.0e: beta(t) = (%.6f, %.6f), |beta(t) - beta(0)| = %.2e, but |t - 0| = %.4f"
          % (d, np.sin(2 * tt), np.sin(tt), np.hypot(np.sin(2 * tt), np.sin(tt)), tt))

# 4. [0,1) -> S^1, t -> e^{2 pi i t}: a continuous bijection that is not a homeomorphism --------------------------------
for d in (1e-1, 1e-2, 1e-3):
    t1 = 1 - d
    p = np.exp(2j * np.pi * t1)
    print("  t = 1 - %.0e: |e^{2 pi i t} - 1| = %.2e, but |t - 0| = %.3f" % (d, abs(p - 1), t1))

# 5. RP^n: the relation {(x, y): y = +-x} is closed (checked on random sequences) --------------------------------------
rng = np.random.default_rng(0)
x0 = rng.normal(size=4)
x0 /= np.linalg.norm(x0)
seq = [(x0 + 1e-3 * k * rng.normal(size=4), -(x0 + 1e-3 * k * rng.normal(size=4))) for k in range(1, 4)]
print("antipodal relation: distance of (x, -x') from the relation shrinks with the perturbation:",
      [round(float(np.linalg.norm(a + b)), 5) for a, b in seq])
