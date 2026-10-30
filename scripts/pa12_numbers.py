"""PA12 Separation, Countability and Local Compactness: numbers quoted in the chapter, recomputed.

    .venv/bin/python -W ignore scripts/pa12_numbers.py
"""
import numpy as np

# 1. One-point compactification of R^2 = S^2 (stereographic projection from the north pole N = (0, 0, 1)) -----------------
def sigma_inv(w):
    """Inverse stereographic projection R^2 -> S^2 \\ {N}."""
    w = np.asarray(w, float)
    r2 = float(w @ w)
    return np.array([2 * w[0], 2 * w[1], r2 - 1.0]) / (r2 + 1.0)


N = np.array([0.0, 0.0, 1.0])
print("distance on S^2 from sigma^{-1}(w) to the north pole N, |w| = R along the x-axis:")
for R in (1, 10, 100, 1000):
    p = sigma_inv([R, 0])
    print("  R = %-5d |p| = %.12f  |p - N| = %.3e   2/sqrt(1+R^2) = %.3e" % (R, np.linalg.norm(p), np.linalg.norm(p - N), 2 / np.sqrt(1 + R * R)))
# a compact set K = closed disc of radius R misses a neighbourhood of N: the complements of compacta are the neighbourhoods of infinity

# 2. Local finiteness depends on the ambient space ----------------------------------------------------------------------
# family F = { (1/(n+2), 1/n) : n >= 1 }.  In X = (0,1) it is locally finite; in [0,1) it is not (at 0).
def meets(n, x, r):
    lo, hi = 1 / (n + 2), 1 / n
    return not (hi <= x - r or lo >= x + r)


print("members of F meeting the ball B(x, r), n up to 10^6:")
for x, r in ((0.5, 0.01), (0.05, 0.01), (0.001, 0.0005), (0.0, 0.01), (0.0, 0.001)):
    cnt = sum(meets(n, x, r) for n in range(1, 10 ** 6))
    print("  x = %-6g r = %-7g -> %d members" % (x, r, cnt))
print("  (at x = 0 EVERY member with n >= 1/r - 1 meets the ball, so infinitely many: the count above is only my cutoff n < 10^6;\n   in (0,1) every x > 0 has a ball meeting finitely many)")
