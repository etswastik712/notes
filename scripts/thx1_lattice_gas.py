"""THX1 (added 2026-11-12): the FHP lattice gas of MIT 12.086 (Rothman), isotropy of the lattice tensors, separation of scales.
    .venv/bin/python -W ignore scripts/thx1_lattice_gas.py"""
import itertools
import math

import numpy as np

rng = np.random.default_rng(12)
c = np.array([[math.cos(math.pi * i / 3), math.sin(math.pi * i / 3)] for i in range(6)])     # c_i, i = 0..5

print("== 1. The six velocities and their moments")
print("  sum c_i = %s; sum c_i c_i^T = %s (= 3 I); mean speed^2 = 1" % (np.round(c.sum(0), 12), np.round(c.T @ c, 12).tolist()))
T4 = np.einsum("ia,ib,ic,id->abcd", c, c, c, c)
d = np.eye(2)
iso = np.einsum("ab,cd->abcd", d, d) + np.einsum("ac,bd->abcd", d, d) + np.einsum("ad,bc->abcd", d, d)
A = T4[0, 0, 0, 0] / 3
print("  4th-order tensor sum c_a c_b c_c c_d: T_xxxx = %.6f, T_xxyy = %.6f, T_yyyy = %.6f; isotropic form A(dd+dd+dd) with A = %.6f; max deviation = %.2e" % (T4[0, 0, 0, 0], T4[0, 0, 1, 1], T4[1, 1, 1, 1], A, np.abs(T4 - A * iso).max()))

def deviation(N, phase=0.0):
    ang = phase + 2 * math.pi * np.arange(N) / N
    v = np.stack([np.cos(ang), np.sin(ang)], 1)
    T2 = np.einsum("ia,ib->ab", v, v)
    T4_ = np.einsum("ia,ib,ic,id->abcd", v, v, v, v)
    A2 = np.trace(T2) / 2
    A4 = T4_[0, 0, 0, 0] / 3
    return np.abs(T2 - A2 * d).max(), np.abs(T4_ - A4 * iso).max() if A4 > 0 else np.nan
print("  N equally spaced unit vectors: deviation of the 2nd-rank tensor and of the 4th-rank tensor from isotropy")
for N in (1, 2, 3, 4, 5, 6, 8):
    d2, d4 = deviation(N)
    print("    N = %d: 2nd-rank %.2e, 4th-rank %.2e   (4th-rank isotropy needs N not dividing 4: here %s)" % (N, d2, d4, "isotropic" if d4 < 1e-12 else "NOT isotropic"))
print("  square lattice (N = 4, c = +-x, +-y): sum c_a c_b = 2 I (isotropic, enough for the lattice random walk) but sum c_x^4 = 2 while sum c_x^2 c_y^2 = 0 (isotropy would need T_xxxx = 3 T_xxyy): NOT isotropic at 4th order")
print("  triangular lattice N = 6 contains +-c: the smallest symmetric set with a 4th-order isotropic tensor (N = 3 works for the tensor alone but has no c_i and -c_i pairs)")

print("\n== 2. The collision rules conserve mass and momentum (all 2^6 = 64 states)")
def collide(n, choice=0):
    n = list(n)
    on = [i for i in range(6) if n[i]]
    # three-body: {0,2,4} <-> {1,3,5}
    if set(on) == {0, 2, 4}:
        return (0, 1, 0, 1, 0, 1)
    if set(on) == {1, 3, 5}:
        return (1, 0, 1, 0, 1, 0)
    # two-body head-on {i, i+3} -> {i+1, i+4} (choice 0) or {i-1, i+2} (choice 1)
    for i in range(3):
        if set(on) == {i, i + 3}:
            out = [0] * 6
            j = (i + 1) % 6 if choice == 0 else (i - 1) % 6
            out[j] = 1; out[(j + 3) % 6] = 1
            return tuple(out)
    return tuple(n)
changed = 0
bad = 0
for n in itertools.product((0, 1), repeat=6):
    for ch in (0, 1):
        m = collide(n, ch)
        if m != n:
            changed += 1 if ch == 0 else 0
        if sum(m) != sum(n) or np.abs(np.array(m) @ c - np.array(n) @ c).max() > 1e-12:
            bad += 1
print("  states changed by a collision: %d of 64 (2 three-body + 3 head-on pairs); violations of mass or momentum conservation: %d" % (changed, bad))
def delta3(n, i):
    nb = [1 - x for x in n]
    return n[(i + 1) % 6] * n[(i + 3) % 6] * n[(i + 5) % 6] * nb[i] * nb[(i + 2) % 6] * nb[(i + 4) % 6] - n[i] * n[(i + 2) % 6] * n[(i + 4) % 6] * nb[(i + 1) % 6] * nb[(i + 3) % 6] * nb[(i + 5) % 6]
ok = True
nz = 0
for n in itertools.product((0, 1), repeat=6):
    dl = np.array([delta3(n, i) for i in range(6)])
    if dl.any():
        nz += 1
    ok &= abs(dl.sum()) < 1e-12 and np.abs(dl @ c).max() < 1e-12
print("  the notes' Delta^(3)_i: nonzero only for %d states ({0,2,4} and {1,3,5}); sum_i Delta_i = 0 and sum_i c_i Delta_i = 0 for all 64 states: %s" % (nz, ok))

print("\n== 3. Equation of state of the lattice gas at rest and a conservation test on a periodic triangular lattice")
rho = 0.7
print("  <n_i> = rho/6 for all i: momentum flux Pi_ab = sum <n_i> c_ia c_ib = (rho/6)*3 delta_ab = (rho/2) delta_ab, so p0 = rho/2 (c_s^2 = 1/2); rho = %.1f: p0 = %.3f" % (rho, rho / 2))
L = 64
dens = 0.25
state = (rng.random((6, L, L)) < dens).astype(np.int8)          # axial coordinates (q, r); direction i moves by shift[i]
shift = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]    # (dq, dr): real vector q*(1,0) + r*(1/2, sqrt3/2)
def totals(s):
    m = s.sum()
    p = np.einsum("ixy,ia->a", s.astype(float), c)
    return int(m), p
m0, p0 = totals(state)
def step(s):
    n = s.copy()
    on = s.sum(0)
    # three-body
    A = ((s[0] & s[2] & s[4]) & (1 - s[1]) & (1 - s[3]) & (1 - s[5])) == 1
    B = ((s[1] & s[3] & s[5]) & (1 - s[0]) & (1 - s[2]) & (1 - s[4])) == 1
    # two-body head-on, random rotation sense
    coin = rng.random((L, L)) < 0.5
    out = n.copy()
    for k in range(3):
        mask = ((s[k] & s[k + 3]) == 1) & (on == 2)
        for sense in (0, 1):
            msk = mask & (coin if sense == 0 else ~coin)
            j = (k + 1) % 6 if sense == 0 else (k - 1) % 6
            out[k][msk] = 0; out[k + 3][msk] = 0
            out[j][msk] = 1; out[(j + 3) % 6][msk] = 1
    for k in range(6):
        out[k][A] = 1 if k in (1, 3, 5) else 0
        out[k][B] = 1 if k in (0, 2, 4) else 0
    for k in range(6):
        out[k] = np.roll(np.roll(out[k], shift[k][0], axis=0), shift[k][1], axis=1)
    return out
s = state
for t in range(300):
    s = step(s)
m1, p1 = totals(s)
print("  64 x 64 periodic triangular lattice, 6 links per site, occupation %.2f, 300 FHP steps: mass %d -> %d, momentum (%.4f, %.4f) -> (%.4f, %.4f): conserved exactly (the collision rules conserve them and streaming only moves particles)" % (dens, m0, m1, *p0, *p1))
print("  fraction of sites changed by a collision per step in the initial state: three-body %.4f, head-on pairs %.4f (consistent with random states: 2 p^3 (1-p)^3 = %.4f, 3 p^2 (1-p)^4 = %.4f)" % (
    float(((state[0] & state[2] & state[4] & (1 - state[1]) & (1 - state[3]) & (1 - state[5])) + (state[1] & state[3] & state[5] & (1 - state[0]) & (1 - state[2]) & (1 - state[4]))).mean()),
    float(sum(((state[k] & state[k + 3]) & (state.sum(0) == 2)).astype(float).mean() for k in range(3))), 2 * dens ** 3 * (1 - dens) ** 3, 3 * dens ** 2 * (1 - dens) ** 4))

print("\n== 4. Separation of scales: fluctuations of the coarse-grained density fall like 1/sqrt(N)")
S0 = (rng.random((6, 512, 512)) < dens).astype(float).sum(0)
for R in (1, 2, 4, 8, 16, 32):
    blk = S0.reshape(512 // R, R, 512 // R, R).sum((1, 3))
    N = 6 * R * R
    print("  box %2d x %2d sites (N = %5d links): relative s.d. of the box mass = %.4f; theory sqrt((1-p)/(N p)) = %.4f" % (R, R, N, blk.std() / blk.mean(), math.sqrt((1 - dens) / (N * dens))))
kB, Tm, P = 1.380649e-23, 300.0, 101325.0
n = P / (kB * Tm)
print("  air at 1 atm, 300 K: n = P/kT = %.3e m^-3; box of side L has N = n L^3 molecules, fluctuation 1/sqrt(N):" % n)
for Lb in (1e-9, 1e-8, 1e-7, 1e-6, 1e-5):
    N = n * Lb ** 3
    print("    L = %7.1e m: N = %.2e, relative fluctuation %.2e" % (Lb, N, 1 / math.sqrt(N)))
dmol = 3.7e-10
lam = 1 / (math.sqrt(2) * math.pi * dmol ** 2 * n)
print("  mean free path lambda = 1/(sqrt2 pi d^2 n) with d = 0.37 nm (recalled, N2-like) = %.2e m; L_hydro >> lambda holds for a 1 mm flow (ratio %.1e)" % (lam, 1e-3 / lam))
