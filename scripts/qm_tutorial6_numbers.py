"""PH2113 Tutorial VI (Ehrenfest equations from the TDSE; barrier for E > V0) and the Ehrenfest/probability-current notes: every number recomputed.
    .venv/bin/python -W ignore scripts/qm_tutorial6_numbers.py"""
import math

import numpy as np

print("== 1. Ehrenfest equations checked on a numerical solution of the TDSE (hbar = m = 1, split-step Fourier)")
N, Lx = 4096, 60.0
x = np.linspace(-Lx / 2, Lx / 2, N, endpoint=False)
dx = x[1] - x[0]
k = 2 * np.pi * np.fft.fftfreq(N, dx)
def run(V, Vp, x0, sig, T=2.0, dt=0.0005, save=10):
    psi = np.exp(-(x - x0) ** 2 / (4 * sig ** 2)).astype(complex)
    psi /= math.sqrt((abs(psi) ** 2).sum() * dx)
    half = np.exp(-0.5j * V(x) * dt)
    kin = np.exp(-0.5j * k ** 2 * dt)
    rec = []
    for n in range(int(T / dt) + 1):
        if n % save == 0:
            rho = abs(psi) ** 2
            dpsi = np.fft.ifft(1j * k * np.fft.fft(psi))
            p = (psi.conj() * (-1j) * dpsi).sum().real * dx
            j = (psi.conj() * dpsi).imag
            rec.append((n * dt, (x * rho).sum() * dx, p, (Vp(x) * rho).sum() * dx, rho.copy(), j.copy()))
        psi = half * np.fft.ifft(kin * np.fft.fft(half * psi))
    return rec
rec = run(lambda x: x ** 4 / 4, lambda x: x ** 3, 1.5, 0.5)
t = np.array([r[0] for r in rec]); X = np.array([r[1] for r in rec]); Pm = np.array([r[2] for r in rec]); Fm = np.array([r[3] for r in rec])
dX = np.gradient(X, t); dP = np.gradient(Pm, t)
print("  V = x^4/4, Gaussian packet x0 = 1.5, sigma = 0.5, p0 = 0:")
print("    max |d<x>/dt - <p>/m| over 0 < t < 2: %.2e (first Ehrenfest equation)" % np.abs(dX - Pm)[2:-2].max())
print("    max |d<p>/dt + <V'>| over 0 < t < 2: %.2e (second equation, V' = x^3)" % np.abs(dP + Fm)[2:-2].max())
print("    at t = 0: <V'> = <x^3> = x0^3 + 3 x0 sigma^2 = %.4f (numeric %.4f); the 'classical' force V'(<x>) = <x>^3 = %.4f: <V'> != V'(<x>), the packet does not follow the classical orbit" % (1.5 ** 3 + 3 * 1.5 * 0.25, Fm[0], X[0] ** 3))
print("    d<p>/dt at t = 0 by finite difference: %.4f (= -<V'> = %.4f); classical orbit would start with -V'(x0) = %.4f" % (dP[0], -Fm[0], -(1.5 ** 3)))
# continuity at one time
i = 100
rho0, j0 = rec[i][4], rec[i][5]
drho = (rec[i + 1][4] - rec[i - 1][4]) / (rec[i + 1][0] - rec[i - 1][0])
djdx = np.real(np.fft.ifft(1j * k * np.fft.fft(rec[i][5])))
print("    continuity d rho/dt + d j/dx = 0 at t = %.2f: max |residual| = %.2e (compared with max |d rho/dt| = %.2e)" % (rec[i][0], np.abs(drho + djdx).max(), np.abs(drho).max()))
print("    first Ehrenfest equation via the current: d<x>/dt = int j dx = %.5f vs <p>/m = %.5f at t = %.2f" % (rec[i][5].sum() * dx, rec[i][2], rec[i][0]))
rec2 = run(lambda x: x ** 2 / 2, lambda x: x, 1.5, 0.5)
t2 = np.array([r[0] for r in rec2]); X2 = np.array([r[1] for r in rec2])
print("  V = x^2/2 (k = m = 1): <x>(t) vs x0 cos t: max deviation %.2e (exact for every state)" % np.abs(X2 - 1.5 * np.cos(t2)).max())

print("\n== 2. Barrier V0 for |x| < a with E > V0: matching conditions solved exactly (hbar^2/2m = 1)")
def solve(E, V0, a):
    k0, kk = math.sqrt(E), math.sqrt(E - V0)
    # unknowns A, B, C, D with F = 1
    M = np.array([
        [np.exp(-1j * k0 * a), np.exp(1j * k0 * a), -np.exp(-1j * kk * a), -np.exp(1j * kk * a)],
        [k0 * np.exp(-1j * k0 * a), -k0 * np.exp(1j * k0 * a), -kk * np.exp(-1j * kk * a), kk * np.exp(1j * kk * a)],
        [0, 0, np.exp(1j * kk * a), np.exp(-1j * kk * a)],
        [0, 0, kk * np.exp(1j * kk * a), -kk * np.exp(-1j * kk * a)]], dtype=complex)
    rhs = np.array([0, 0, np.exp(1j * k0 * a), k0 * np.exp(1j * k0 * a)], dtype=complex)
    A, B, C, D = np.linalg.solve(M, rhs)
    return A, B, C, D, k0, kk
V0, a = 1.0, 1.0
print("  V0 = %g, a = %g: columns E/V0, k0, k, T (matching), T (formula 1/(1 + V0^2 sin^2(2ka)/(4E(E-V0)))), R = |B/A|^2, R + T" % (V0, a))
for E in (1.001, 1.5, 2.0, 4.0, 10.0):
    A, B, C, D, k0, kk = solve(E, V0, a)
    T = 1 / abs(A) ** 2
    Tf = 1 / (1 + V0 ** 2 * math.sin(2 * kk * a) ** 2 / (4 * E * (E - V0)))
    print("    %6.3f  k0 = %.4f  k = %.4f  T = %.6f  formula %.6f  R = %.6f  R+T = %.12f" % (E, k0, kk, T, Tf, abs(B / A) ** 2, T + abs(B / A) ** 2))
A, B, C, D, k0, kk = solve(2.0, 1.0, 1.0)
F = 1.0
print("  closed forms for E = 2V0: C = (1 + k0/k) F e^{i(k0-k)a}/2 = %.6f %+.6fj (matching %.6f %+.6fj); D = (1 - k0/k) F e^{i(k0+k)a}/2 = %.6f %+.6fj (matching %.6f %+.6fj)" % (
    *(lambda z: (z.real, z.imag))(0.5 * (1 + k0 / kk) * np.exp(1j * (k0 - kk) * 1.0)), C.real, C.imag, *(lambda z: (z.real, z.imag))(0.5 * (1 - k0 / kk) * np.exp(1j * (k0 + kk) * 1.0)), D.real, D.imag))
print("  k < k0 for E > V0: k0^2 - k^2 = V0 (in these units) = %.4f; wavelength inside / outside = k0/k = %.4f at E = 2 V0; E -> V0: k -> 0, wavelength -> infinity (E = 1.001: k0/k = %.1f); E >> V0: ratio -> 1 (E = 100: %.4f)" % (k0 ** 2 - kk ** 2, k0 / kk, math.sqrt(1.001 / 0.001), math.sqrt(100 / 99)))
print("  T = 1 at 2ka = n pi: E/V0 = 1 + (n pi/(2a))^2/V0: n = 1: %.4f, n = 2: %.4f (a = 1, V0 = 1); T min between the resonances; in the limit a -> 0 or V0 -> 0, T -> 1" % (1 + (math.pi / 2) ** 2, 1 + math.pi ** 2))
