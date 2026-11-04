"""QM10 numbers: the finite barrier on [-a,a] (E<V0 and E>V0), Tutorial V (three bound states, double well, well scattering).
Units hbar^2/2m = 1 unless stated.   .venv/bin/python -W ignore scripts/qm10_numbers.py
Every closed form is checked against a direct solve of the four matching equations (lecture eqs 1-4) and, where relevant, tmat of qm08_numbers.
"""
import math
import os
import sys

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qm08_numbers import tmat  # noqa

K0 = 5.1231  # nm^-1 eV^-1/2


def sec(t):
    print("\n=== " + t + " ===")


def solve_barrier(E, V0, a):
    """Solve the four matching equations for the barrier (E<V0), A=1. Returns (B,C,D,F)."""
    k, kap = math.sqrt(E), math.sqrt(V0 - E)
    # unknowns B,C,D,F ; eqs at x=-a (psi, psi') and x=a (psi, psi')
    M = np.array([
        [np.exp(1j * k * a), -np.exp(-kap * a), -np.exp(kap * a), 0],
        [-1j * k * np.exp(1j * k * a), -kap * np.exp(-kap * a), kap * np.exp(kap * a), 0],
        [0, np.exp(kap * a), np.exp(-kap * a), -np.exp(1j * k * a)],
        [0, kap * np.exp(kap * a), -kap * np.exp(-kap * a), -1j * k * np.exp(1j * k * a)],
    ], dtype=complex)
    rhs = np.array([-np.exp(-1j * k * a), -1j * k * np.exp(-1j * k * a), 0, 0], dtype=complex)
    return np.linalg.solve(M, rhs)


def T_barrier(E, V0, a):
    if E < V0:
        k, kap = math.sqrt(E), math.sqrt(V0 - E)
        return 1 / (1 + (k * k + kap * kap) ** 2 * math.sinh(2 * kap * a) ** 2 / (4 * k * k * kap * kap))
    k2 = math.sqrt(E - V0)
    k = math.sqrt(E)
    return 1 / (1 + V0 ** 2 * math.sin(2 * k2 * a) ** 2 / (4 * E * (E - V0)))


def well_bound(z0, parity):
    """roots k0 a of the well with floor 0: even tan(z)=sqrt(z0^2/z^2-1), odd -cot(z)=sqrt(z0^2/z^2-1)."""
    out = []
    n = int(2 * z0 / math.pi) + 2
    for j in range(n):
        lo, hi = j * math.pi / 2 + 1e-9, (j + 1) * math.pi / 2 - 1e-9
        if lo >= z0:
            break
        hi = min(hi, z0 - 1e-12)
        if (j % 2 == 0) != (parity == "even"):
            continue
        g = (lambda z: math.tan(z) - math.sqrt(z0 ** 2 / z ** 2 - 1)) if parity == "even" else (lambda z: -1 / math.tan(z) - math.sqrt(z0 ** 2 / z ** 2 - 1))
        try:
            if g(lo) * g(hi) < 0:
                out.append(brentq(g, lo, hi, xtol=1e-14))
        except ValueError:
            pass
    return sorted(out)


def double_well_levels(V0, w, d):
    """Lowest even and odd level of the symmetric double well: barrier |x|<d/2 (V0), wells d/2<|x|<d/2+w (0), V0 outside (units hbar^2/2m=1)."""
    def f(E, par):
        k, kap = math.sqrt(E), math.sqrt(V0 - E)
        psi = math.cos(k * w) + kap / k * math.sin(k * w)
        dpsi = k * math.sin(k * w) - kap * math.cos(k * w)
        L = kap * (math.tanh(kap * d / 2) if par == "even" else 1 / math.tanh(kap * d / 2))
        return dpsi - L * psi
    out = {}
    for par in ("even", "odd"):
        Es = np.linspace(1e-6, V0 - 1e-6, 4000)
        vals = [f(e, par) for e in Es]
        roots = []
        for i in range(len(Es) - 1):
            if vals[i] * vals[i + 1] < 0 and abs(vals[i]) < 50 and abs(vals[i + 1]) < 50:
                roots.append(brentq(lambda e: f(e, par), Es[i], Es[i + 1], xtol=1e-13))
        out[par] = roots
    return out


def single_well(V0, width, n=0):
    z0 = math.sqrt(V0) * width / 2  # a = width/2, hbar^2/2m=1 -> z0 = a sqrt(V0)
    roots = sorted(well_bound(z0, "even") + well_bound(z0, "odd"))
    return (roots[n] / (width / 2)) ** 2


def main():
    sec("Lecture: C, D, B and F/A against the direct solve (E<V0), units hbar^2/2m=1, V0=1")
    for E, a in ((0.5, 0.5), (0.2, 1.0), (0.8, 0.7)):
        V0 = 1.0
        k, kap = math.sqrt(E), math.sqrt(V0 - E)
        B, C, D, F = solve_barrier(E, V0, a)
        C_f = (kap + 1j * k) / (2 * kap) * np.exp(-(kap - 1j * k) * a) * F
        D_f = (kap - 1j * k) / (2 * kap) * np.exp((kap + 1j * k) * a) * F
        eps = (kap ** 2 - k ** 2) / (k * kap)
        eta = (kap ** 2 + k ** 2) / (k * kap)
        FA = np.exp(-2j * k * a) / (math.cosh(2 * kap * a) + 1j * eps / 2 * math.sinh(2 * kap * a))
        B_f = -1j * eta / 2 * math.sinh(2 * kap * a) * F
        T = abs(F) ** 2
        R = abs(B) ** 2
        print(f"E={E} a={a}: |C-Cf|={abs(C-C_f):.1e} |D-Df|={abs(D-D_f):.1e} |F-F/A|={abs(F-FA):.1e} |B-Bf|={abs(B-B_f):.1e}; "
              f"T={T:.6f} formula {T_barrier(E,V0,a):.6f} tmat {tmat(E,[V0],[-a,a])[0]:.6f}; R={R:.6f} T+R={T+R:.9f}")
        print(f"   eps={eps:.4f} eta={eta:.4f}; 1+eps^2/4 = eta^2/4 : {1+eps**2/4:.6f} vs {eta**2/4:.6f}; phase arg(F/A)+2ka = {np.angle(FA*np.exp(2j*k*a)):.5f} vs -atan(eps/2 tanh2ka)={-math.atan(eps/2*math.tanh(2*kap*a)):.5f}")

    sec("physical barrier: electron E=1 eV, V0=2 eV, width 2a = 0.5 nm (QM08 gave T=0.0235 for L=0.5 nm)")
    E, V0 = 1.0, 2.0
    kap = K0 * math.sqrt(V0 - E)
    k = K0 * math.sqrt(E)
    for a in (0.25, 0.5, 0.1):
        T = 1 / (1 + (k * k + kap * kap) ** 2 * math.sinh(2 * kap * a) ** 2 / (4 * k * k * kap * kap))
        Tt = 16 * (E / V0) * (1 - E / V0) * math.exp(-4 * kap * a)
        print(f"a={a} nm: kappa={kap:.4f}/nm, 2*kappa*a={2*kap*a:.4f}; T={T:.6g}; thick estimate={Tt:.6g}; e^(-4 kappa a)={math.exp(-4*kap*a):.4g}")

    sec("thin barrier / limits: T(E) for V0=1, a=0.5 and the E>V0 continuation")
    for E in (0.1, 0.5, 0.9, 0.999, 1.001, 1.5, 2.0, 3.0):
        print(f"E/V0={E}: T={T_barrier(E,1.0,0.5):.6f}   tmat={tmat(E,[1.0],[-0.5,0.5])[0]:.6f}")
    # over-barrier resonances 2*k2*a = n pi: a=0.5, V0=1 -> k2 = n pi
    for n in (1, 2):
        E = 1 + (n * math.pi) ** 2
        print(f"resonance n={n}: E/V0={E:.4f}, T={T_barrier(E,1.0,0.5):.9f}")

    sec("Tutorial V Q1: three bound states: z0 > pi (V0 a^2 > pi^2 hbar^2/2m)")
    for z0 in (3.0, math.pi - 1e-6, 3.3, 4.0, 5.0):
        ev, od = well_bound(z0, "even"), well_bound(z0, "odd")
        print(f"z0={z0:.6f}: even roots {[round(x,5) for x in ev]}, odd {[round(x,5) for x in od]}, N={len(ev)+len(od)}, ceil(2 z0/pi)={math.ceil(2*z0/math.pi)}")
    hb2m = 3.80998e-2  # eV nm^2 (hbar^2/2m_e)
    print(f"pi^2 hbar^2/2m_e = {math.pi**2*hb2m:.4f} eV nm^2 = {math.pi**2*hb2m*100:.2f} eV Angstrom^2")
    for a in (0.2, 0.5, 1.0):
        print(f"  a={a} nm: V0_min = {math.pi**2*hb2m/a**2:.4f} eV")
    z0 = 3.3
    ev, od = well_bound(z0, "even"), well_bound(z0, "odd")
    print(f"z0=3.3: E/V0 = {[ (r/z0)**2 for r in sorted(ev+od)]}")
    # nodes of 3rd state: cos(k0 x) has zeros at k0 x = pi/2 -> x/a = pi/(2 k0 a)
    r3 = sorted(ev + od)[2]
    print(f"3rd state k0a={r3:.5f}: node at |x|/a = {math.pi/(2*r3):.4f}")

    sec("Tutorial V Q2: double well, V0=20, w=1 (units hbar^2/2m=1): levels vs d")
    V0, w = 20.0, 1.0
    E1w = single_well(V0, w)
    E2w = single_well(V0, 2 * w)
    print(f"single well width w=1: E0 = {E1w:.6f}; single well width 2w: E0 = {E2w:.6f}; kappa(E1w) = {math.sqrt(V0-E1w):.4f}")
    for d in (0.0001, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 3.0, 5.0):
        lv = double_well_levels(V0, w, d)
        e0, e1 = lv["even"][0], lv["odd"][0]
        print(f"d={d:7.4f}: E_even={e0:.6f} E_odd={e1:.6f} splitting={e1-e0:.3e}  (E_even-E_single(w)={e0-E1w:+.4f})  ln split = {math.log(e1-e0):.3f}")
    # exponential law
    ds = np.array([2.0, 3.0, 4.0, 5.0])
    sp = np.array([double_well_levels(V0, w, d)["odd"][0] - double_well_levels(V0, w, d)["even"][0] for d in ds])
    print("slope of ln(splitting) vs d:", np.polyfit(ds, np.log(sp), 1)[0], " -kappa =", -math.sqrt(V0 - E1w))

    sec("Tutorial V Q3: well, E>V0 (floor 0, walls V0): lecture eqs (4)-(7) solved directly")
    V0 = 1.0
    z0 = 5.0
    a = z0 / math.sqrt(V0)
    for Er in (1.001, 1.579, 2.0, 4.0, 10.0):
        E = Er * V0
        k, k0 = math.sqrt(E - V0), math.sqrt(E)
        M = np.array([
            [np.exp(-1j * k * a), -np.exp(-1j * k0 * a), -np.exp(1j * k0 * a), 0],
            [-1j * k * np.exp(-1j * k * a), -1j * k0 * np.exp(-1j * k0 * a), 1j * k0 * np.exp(1j * k0 * a), 0],
            [0, np.exp(1j * k0 * a), np.exp(-1j * k0 * a), -np.exp(1j * k * a)],
            [0, 1j * k0 * np.exp(1j * k0 * a), -1j * k0 * np.exp(-1j * k0 * a), -1j * k * np.exp(1j * k * a)],
        ], dtype=complex)
        # unknowns A? we want F/A with A=1: move A col to rhs: unknowns B,C,D,F
        M2 = np.array([
            [np.exp(1j * k * a), -np.exp(-1j * k0 * a), -np.exp(1j * k0 * a), 0],
            [-1j * k * np.exp(1j * k * a), -1j * k0 * np.exp(-1j * k0 * a), 1j * k0 * np.exp(1j * k0 * a), 0],
            [0, np.exp(1j * k0 * a), np.exp(-1j * k0 * a), -np.exp(1j * k * a)],
            [0, 1j * k0 * np.exp(1j * k0 * a), -1j * k0 * np.exp(-1j * k0 * a), -1j * k * np.exp(1j * k * a)],
        ], dtype=complex)
        rhs = np.array([-np.exp(-1j * k * a), -1j * k * np.exp(-1j * k * a), 0, 0], dtype=complex)
        B, C, D, F = np.linalg.solve(M2, rhs)
        F_f = 4 * k * k0 * np.exp(-2j * k * a) / ((k + k0) ** 2 * np.exp(-2j * k0 * a) - (k - k0) ** 2 * np.exp(2j * k0 * a))
        T9 = 1 / (1 + V0 ** 2 / (4 * E * (E - V0)) * math.sin(2 * a * math.sqrt(E)) ** 2)
        print(f"E/V0={Er}: |F-F_eq8|={abs(F-F_f):.1e}  T=|F|^2={abs(F)**2:.6f}  eq9={T9:.6f}  R={abs(B)**2:.6f} sum={abs(F)**2+abs(B)**2:.9f}")
    print("resonance E/V0 (n k0 a = n pi/2 ...): (2 pi / 5)^2 =", (2 * math.pi / 5) ** 2, " first resonance above V0 for z0=5: 2 k0 a = n pi with k0 a = n pi/2 -> n=4 (k0a=2pi=6.283>5)")
    print("T at E/V0=2: reflection |B/A|^2 =", 1 - T_barrier(2.0, 1.0, 1.0) if False else "see above")


if __name__ == "__main__":
    main()
