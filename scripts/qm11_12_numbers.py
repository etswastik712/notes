#!/usr/bin/env python3
"""Numbers for QM11 (2D problems, angular momentum, circular well, 2D oscillator) and QM12 (hydrogen). Added 2026-11-21.
Run: .venv/bin/python -I scripts/qm11_12_numbers.py
"""
import numpy as np
import sympy as sp
from scipy.special import jn_zeros, jv
from scipy.linalg import eigh_tridiagonal
from scipy import constants as K
from scipy.integrate import quad

print("=== QM11 polar Laplacian (Tutorial VII Q1), symbolic check")
r, th = sp.symbols("r theta", positive=True)
x, y = r * sp.cos(th), r * sp.sin(th)
X, Y = sp.symbols("X Y")
for f in [X**3 * Y - 2 * Y**2, sp.exp(-(X**2 + Y**2)) * X, sp.sin(X) * sp.cos(2 * Y)]:
    cart = sp.diff(f, X, 2) + sp.diff(f, Y, 2)
    g = f.subs({X: x, Y: y})
    polar = sp.diff(g, r, 2) + sp.diff(g, r) / r + sp.diff(g, th, 2) / r**2
    print("  f =", f, " difference:", sp.simplify(polar - cart.subs({X: x, Y: y})))
# L = x p_y - y p_x = -i hbar d/dtheta
g = sp.Function("g")(X, Y)
Lcart = X * sp.diff(g, Y) - Y * sp.diff(g, X)
f = X**2 * Y + Y**3 * X
print("  x d/dy - y d/dx vs d/dtheta:", sp.simplify((X * sp.diff(f, Y) - Y * sp.diff(f, X)).subs({X: x, Y: y}) - sp.diff(f.subs({X: x, Y: y}), th)))

print("=== QM11 circular infinite well: E = j_{l,n}^2 in units hbar^2/(2 m a^2)")
lev = []
for l in range(0, 6):
    for n, j in enumerate(jn_zeros(l, 4), start=1):
        lev.append((j * j, n, l, j))
lev.sort()
for E, n, l, j in lev[:12]:
    print(f"  n={n} l={l}: j={j:.4f}  E={E:.3f}  degeneracy {'1' if l == 0 else '2 (±l)'}")
print(f"  compare square box side 2a (same width) ground: pi^2/4 * 2 = {np.pi**2/2:.3f}; disc of area pi a^2 vs square of same area side sqrt(pi) a: 2 pi^2/pi = {2*np.pi:.3f}")
for n, l in [(1, 0), (2, 1), (1, 3)]:
    j = jn_zeros(l, n)[-1]
    N2 = 1 / (np.pi * jv(l + 1, j) ** 2)
    val = quad(lambda rr: N2 * jv(l, j * rr) ** 2 * rr * 2 * np.pi, 0, 1)[0]
    print(f"  normalisation check n={n} l={l}: {val:.6f}")
# radial nodes: n-1 interior zeros
print("  ground state peak density at centre (l=0): |psi(0)|^2 a^2 =", f"{1/(np.pi*jv(1, jn_zeros(0,1)[0])**2):.4f}")

print("=== QM11 2D oscillator (Tutorial VII Q2): radial equation by finite differences, hbar=m=omega=1")
def radial2d(l, N=1500, rmax=9.0, V=lambda r: 0.5 * r * r):
    # flux-conservative scheme on r_i = (i - 1/2) h:  -(1/2)(1/r)(r R')' + [V + l^2/(2 r^2)] R = E R
    # multiplied by r_i -> symmetric S R = E W R (handles r = 0 for l = 0, unlike the u = sqrt(r) R form)
    from scipy.linalg import eigh
    h = rmax / N; ri = h * (np.arange(1, N + 1) - 0.5); rp = ri + h / 2; rm = ri - h / 2
    S = np.diag((rp + rm) / (2 * h * h) + ri * (V(ri) + l * l / (2 * ri**2)))
    off = -rp[:-1] / (2 * h * h); S += np.diag(off, 1) + np.diag(off, -1)
    return eigh(S, np.diag(ri), eigvals_only=True, subset_by_index=[0, 3])
for l in range(0, 4):
    print(f"  l=±{l}: E =", " ".join(f"{E:.4f}" for E in radial2d(l)), f"(theory 2n_r+{l}+1)")
from collections import Counter
deg = Counter()
for nx in range(6):
    for ny in range(6):
        deg[nx + ny] += 1
print("  Cartesian count of states with nx+ny=N:", [deg[N] for N in range(5)], "-> degeneracy N+1")

print("=== QM11 radial probability density (Tutorial VII Q3)")
# 2D Gaussian ground state psi = exp(-r^2/2)/sqrt(pi): P(r) = 2 pi r |psi|^2 = 2 r e^{-r^2}, peak at 1/sqrt2
rr = np.linspace(0, 4, 400001); P = 2 * rr * np.exp(-rr**2)
print(f"  2D oscillator ground state: P(r) = 2 r e^(-r^2), integral {np.trapezoid(P, rr):.5f}, peak r = {rr[P.argmax()]:.4f} (1/sqrt2 = {1/np.sqrt(2):.4f})")

print("=== QM12 hydrogen scales")
me, e, eps0, hbar = K.m_e, K.e, K.epsilon_0, K.hbar
Eh = me / hbar**2 * (e**2 / (4 * np.pi * eps0)) ** 2
a0 = hbar**2 * 4 * np.pi * eps0 / (me * e**2)
print(f"  m e^4/(hbar^2 (4 pi eps0)^2) = {Eh/e:.4f} eV = 2 x {Eh/e/2:.4f} eV;  a0 = {a0*1e10:.5f} Angstrom")
for n in range(1, 5):
    print(f"  E_{n} = {-Eh/2/n**2/e:.4f} eV, degeneracy n^2 = {n*n} (2n^2 = {2*n*n} with spin)")
mu = me * K.m_p / (me + K.m_p)
print(f"  reduced-mass correction: E1 = {-Eh/2*mu/me/e:.4f} eV (factor {mu/me:.6f})")
for (n1, n2, name) in [(1, 2, "Lyman alpha"), (2, 3, "Balmer alpha (H-alpha)"), (2, 4, "Balmer beta")]:
    dE = Eh / 2 * (1 / n1**2 - 1 / n2**2); lam = K.h * K.c / dE
    print(f"  {name}: {dE/e:.3f} eV, lambda = {lam*1e9:.1f} nm")

print("=== QM12 radial functions (units a = 1)")
R10 = lambda r: 2 * np.exp(-r)
R20 = lambda r: (1 / np.sqrt(2)) * (1 - r / 2) * np.exp(-r / 2)   # = (1/sqrt2)(1/a)^{3/2}(1 - r/2a) e^{-r/2a}
R21 = lambda r: (1 / np.sqrt(24)) * r * np.exp(-r / 2)
for nm, R in [("R10", R10), ("R20", R20), ("R21", R21)]:
    print(f"  int R^2 r^2 dr for {nm} = {quad(lambda r: R(r)**2 * r * r, 0, np.inf)[0]:.6f}")
print("  [verify] the notes print R20 = (1/sqrt2)(1/a)^{3/2}(2 - r/a)e^{-r/2a}; with (2 - r/a) the norm is",
      f"{quad(lambda r: (1/np.sqrt(2)*(2-r)*np.exp(-r/2))**2*r*r, 0, np.inf)[0]:.4f} -> Griffiths' form uses 1/(2 sqrt2): (1/(2 sqrt2))(2-r/a)")
r = np.linspace(0, 20, 2000001)
for nm, R in [("1s", R10), ("2s", R20), ("2p", R21)]:
    P = r * r * R(r) ** 2
    print(f"  {nm}: radial density P(r) = r^2 R^2 peaks at r = {r[P.argmax()]:.4f} a;  <r> = {np.trapezoid(r*P, r):.4f} a")
print("  1s: P(r) = 4 r^2 e^{-2r}; dP/dr = 0 -> r = a (the notes' question)")
print("  2s node at r =", 2.0, "a")

print("=== QM12 radial equation by finite differences (Coulomb, units hbar=m=e^2/4pi eps0=1 -> E in Hartree)")
def radial3d(l, N=6000, rmax=80.0):
    h = rmax / (N + 1); rr = h * np.arange(1, N + 1)
    d = 1 / h**2 - 1 / rr + l * (l + 1) / (2 * rr**2); e_ = -0.5 / h**2 * np.ones(N - 1)
    return eigh_tridiagonal(d, e_, select="i", select_range=(0, 2))[0]
for l in range(0, 3):
    Es = radial3d(l)
    print(f"  l={l}: E (Hartree) =", " ".join(f"{E:.5f}" for E in Es), " -> n =", " ".join(f"{1/np.sqrt(-2*E):.3f}" for E in Es))
print("=== associated Legendre table check (P_l^m with Condon-Shortley phase, scipy)")
from scipy.special import lpmv
xx = 0.3
for (l, m, ref) in [(1, 1, -np.sqrt(1 - xx**2)), (2, 0, 0.5 * (3 * xx**2 - 1)), (2, 1, -3 * xx * np.sqrt(1 - xx**2)), (2, 2, 3 * (1 - xx**2))]:
    print(f"  P_{l}^{m}(0.3): scipy {lpmv(m, l, xx):.6f}  notes {ref:.6f}")
