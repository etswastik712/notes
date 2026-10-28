"""QM07 numbers: finite square well, Tutorial IV shape of kappa/k0, scattering (E>V0), real-world examples.

.venv/bin/python -W ignore scripts/qm07_numbers.py

Two conventions are used and cross-checked:
  L  (lecture, Finite_well.pdf): V=0 for |x|<a, V=V0 outside; energy E measured from the well floor, 0<E<V0 bound.
     k0=sqrt(2mE)/hbar, kappa=sqrt(2m(V0-E))/hbar, z=k0 a, z0=a sqrt(2mV0)/hbar, kappa a = sqrt(z0^2-z^2).
  G  (Griffiths): V=-V0 inside, 0 outside; bound -V0<E<0.   E_G = E_L - V0.
"""
import math

import numpy as np
from scipy.optimize import brentq

HBAR = 1.054571817e-34
ME = 9.1093837015e-31
EV = 1.602176634e-19
HBARC = 197.3269804  # MeV fm


def states(z0):
    """Bound states of the symmetric well: list of (parity, z) sorted by z (lecture variables)."""
    out = []
    # even: z tan z = sqrt(z0^2 - z^2) on (k pi, k pi + pi/2) ; odd: -z cot z = sqrt(z0^2 - z^2) on (k pi + pi/2, (k+1) pi)
    eps = 1e-12
    for k in range(0, int(z0 / math.pi) + 2):
        lo, hi = k * math.pi + eps, min(k * math.pi + math.pi / 2 - eps, z0 - eps)
        if lo < hi:
            f = lambda z: z * math.tan(z) - math.sqrt(max(z0 * z0 - z * z, 0))
            if f(lo) * f(hi) < 0:
                out.append(("even", brentq(f, lo, hi, xtol=1e-14)))
        lo, hi = k * math.pi + math.pi / 2 + eps, min((k + 1) * math.pi - eps, z0 - eps)
        if lo < hi:
            f = lambda z: -z / math.tan(z) - math.sqrt(max(z0 * z0 - z * z, 0))
            if f(lo) * f(hi) < 0:
                out.append(("odd", brentq(f, lo, hi, xtol=1e-14)))
    return sorted(out, key=lambda t: t[1])


def p_out(par, z, z0):
    ka = math.sqrt(z0 * z0 - z * z)
    if par == "even":
        c = math.cos(z) ** 2 / ka
        return c / (1 + math.sin(2 * z) / (2 * z) + c)
    s = math.sin(z) ** 2 / ka
    return s / (1 - math.sin(2 * z) / (2 * z) + s)


def sec(t):
    print("\n=== " + t + " ===")


def main():
    sec("number of bound states: N = ceil(2 z0/pi)  (the floor+1 formula fails at exact multiples of pi/2)")
    for z0 in (0.5, 1.0, math.pi / 2, 2.0, 3.0, math.pi, 4.0, 2 * math.pi, 7.0, 8.0, 10.0, 4 * math.pi):
        n = len(states(z0))
        print(f"z0={z0:7.4f}  solved N={n}  ceil(2z0/pi)={math.ceil(2*z0/math.pi - 1e-12)}  floor(2z0/pi)+1={math.floor(2*z0/math.pi + 1e-12)+1}")

    sec("reference table (lecture variables): ground state, penetration, P_out")
    print("z0      N  z1      kappa1*a  E1/V0(L)=z1^2/z0^2  E1/V0(G)  d_pen/a   P_out")
    for z0 in (1.0, 2.0, math.pi, 4.0, 2 * math.pi, 8.0, 10.0):
        st = states(z0)
        par, z1 = st[0]
        ka = math.sqrt(z0 * z0 - z1 * z1)
        print(f"{z0:6.3f} {len(st):2d} {z1:7.4f} {ka:8.4f}  {z1**2/z0**2:8.4f}          {z1**2/z0**2-1:8.4f}  {1/ka:7.4f}  {100*p_out(par,z1,z0):6.2f}%")

    sec("figure A/B numbers (z0=3 and z0=7)")
    for z0 in (3.0, 7.0, 5.0):
        print(z0, [(p, round(z, 4)) for p, z in states(z0)], " P_out:", [round(100 * p_out(p, z, z0), 2) for p, z in states(z0)])

    sec("GaAs / Al0.3Ga0.7As quantum well: m*=0.067 me, V0=0.30 eV, a=5 nm")
    m, V0, a = 0.067 * ME, 0.30 * EV, 5e-9
    z0 = a * math.sqrt(2 * m * V0) / HBAR
    print("z0 =", round(z0, 4))
    for par, z in states(z0):
        E_L = 0.30 * (z / z0) ** 2
        ka = math.sqrt(z0 * z0 - z * z)
        print(f"  {par:4s} z={z:.4f}  E_floor={E_L*1000:7.2f} meV  E_G={E_L-0.30:+.4f} eV  d_pen={a/ka*1e9:.3f} nm  P_out={100*p_out(par,z,z0):.2f}%")
    st = states(z0)
    dE = 0.30 * ((st[1][1] / z0) ** 2 - (st[0][1] / z0) ** 2)
    print(f"  1->2 transition {dE*1000:.1f} meV -> lambda = {1.239842/dE:.2f} um")

    sec("deuteron (3D s-wave = odd branch): mu=469.1 MeV, V0=35 MeV, a=2.05 fm")
    mu, V0, a = 469.1, 35.0, 2.05
    z0 = a / HBARC * math.sqrt(2 * mu * V0)
    print("z0 =", round(z0, 4), " pi/2 =", round(math.pi / 2, 4))
    odd = [s for s in states(z0) if s[0] == "odd"]
    z = odd[0][1]
    Ekin = (HBARC * z / a) ** 2 / (2 * mu)
    B = V0 - Ekin
    kap = math.sqrt(2 * mu * B) / HBARC
    print(f"  z={z:.4f}  Ekin={Ekin:.2f} MeV  B={B:.3f} MeV (exp 2.2246)  kappa={kap:.4f}/fm  d_pen={1/kap:.2f} fm  P_out={100*p_out('odd',z,z0):.1f}%")
    print("  states in 3D (odd only):", len(odd))
    print("  threshold depth for 3D binding: V0 > pi^2 hbar^2/(8 mu a^2) =", round(math.pi ** 2 * HBARC ** 2 / (8 * mu * a * a), 2), "MeV")

    sec("electron, width 1 nm (a=0.5 nm), V0=5 eV")
    m, V0, a = ME, 5 * EV, 0.5e-9
    z0 = a * math.sqrt(2 * m * V0) / HBAR
    print("z0 =", round(z0, 4))
    for par, z in states(z0):
        E_L = 5 * (z / z0) ** 2
        ka = math.sqrt(z0 * z0 - z * z)
        print(f"  {par:4s} z={z:.4f}  E_floor={E_L:.4f} eV  E_G={E_L-5:+.4f} eV  d_pen={a/ka*1e9:.3f} nm  P_out={100*p_out(par,z,z0):.2f}%")
    print("  infinite-box ground state:", round(math.pi ** 2 * HBAR ** 2 / (2 * m * (2 * a) ** 2) / EV, 4), "eV")

    sec("deep-well correction: E_n ~ E_box (1 - 2/z0) (check at z0 = 10, 20, 50)")
    for z0 in (10, 20, 50):
        st = states(z0)
        z1 = st[0][1]
        print(f"z0={z0}: exact z1={z1:.5f}  (pi/2)(1-1/z0)={math.pi/2*(1-1/z0):.5f}  ratio E/Ebox exact={(z1/(math.pi/2))**2:.5f}  approx 1-2/z0={1-2/z0:.5f}")

    sec("weak well: kappa = m alpha/hbar^2, E = -m alpha^2/(2 hbar^2), alpha=2 V0 a; compare to exact")
    for z0 in (0.05, 0.1, 0.3):
        st = states(z0)
        z1 = st[0][1]
        ka_exact = math.sqrt(z0 * z0 - z1 * z1)
        print(f"z0={z0}: exact kappa a={ka_exact:.5f}  approx z0^2={z0**2:.5f}   E/V0 exact (L)={(z1/z0)**2:.5f}")

    sec("Tutorial IV: f(z)=kappa/k0=sqrt(z0^2/z^2-1)")
    z0 = 5.0
    f = lambda z: math.sqrt(z0 ** 2 / z ** 2 - 1)
    fp = lambda z: -z0 ** 2 / (z ** 2 * math.sqrt(z0 ** 2 - z ** 2))
    fpp = lambda z: z0 ** 2 * (2 * z0 ** 2 - 3 * z ** 2) / (z ** 3 * (z0 ** 2 - z ** 2) ** 1.5)
    print("z/z0    f       f'        f''")
    for r in (0.05, 0.2, 0.5, 0.8, 0.8165, 0.9, 0.99, 0.999):
        z = r * z0
        print(f"{r:6.4f} {f(z):9.4f} {fp(z):10.4f} {fpp(z):10.4f}")
    print("inflection at z = z0 sqrt(2/3) =", round(z0 * math.sqrt(2 / 3), 4), "(f'' = 0)")
    print("limits: z->0+: f ~ z0/z (hyperbola, pole at 0); z->z0-: f ~ sqrt(2(z0-z)/z0) (vertical tangent, f'->-inf)")
    # tan(z) branches intersect f: first intersection for z0=5:
    print("intersections (even: tan z = f ; odd: -cot z = f) for z0=5:", [(p, round(z, 4)) for p, z in states(5.0)])

    sec("scattering E>V0 (lecture convention): T = 1/(1 + V0^2/(4E(E-V0)) sin^2(2 k0 a))")
    def T(E, V0, k0a_per_sqrtE):  # k0 a = z0 sqrt(E/V0)
        return None
    z0 = 5.0
    for r in (1.001, 1.1, 1.5, 2.0, 4.0, 10.0):  # E/V0
        z = z0 * math.sqrt(r)
        Tn = 1 / (1 + 1 / (4 * r * (r - 1)) * math.sin(2 * z) ** 2)
        print(f"E/V0={r:6.3f}  k0 a={z:7.4f}  T={Tn:.4f}")
    print("resonances T=1 at k0 a = n pi/2 -> E_n = (n pi/2)^2 V0/z0^2 (infinite-well levels of width 2a), only those with E>V0 (n pi/2 > z0)")
    print("z0=5: n >", math.ceil(2 * 5 / math.pi), "->", [round((n * math.pi / 2 / 5) ** 2, 3) for n in range(7, 12)], "(E/V0)")
    # check T + R = 1 numerically by solving the matching equations directly
    def TR(E, V0, a, m=1.0, hbar=1.0):
        k = math.sqrt(2 * m * (E - V0)) / hbar
        k0 = math.sqrt(2 * m * E) / hbar
        # unknowns B,C,D,F with A=1: matching at x=-a and x=a
        M = np.array([
            [np.exp(1j * k * a), -np.exp(-1j * k0 * a), -np.exp(1j * k0 * a), 0],
            [-1j * k * np.exp(1j * k * a), -1j * k0 * np.exp(-1j * k0 * a), 1j * k0 * np.exp(1j * k0 * a), 0],
            [0, np.exp(1j * k0 * a), np.exp(-1j * k0 * a), -np.exp(1j * k * a)],
            [0, 1j * k0 * np.exp(1j * k0 * a), -1j * k0 * np.exp(-1j * k0 * a), -1j * k * np.exp(1j * k * a)],
        ], complex)
        rhs = np.array([-np.exp(-1j * k * a), -1j * k * np.exp(-1j * k * a), 0, 0], complex)
        B, C, D, F = np.linalg.solve(M, rhs)
        return abs(F) ** 2, abs(B) ** 2
    for E in (1.2, 2.0, 3.7):
        Tn, Rn = TR(E, 1.0, 5.0 / math.sqrt(2.0))
        z = 5.0 * math.sqrt(E)
        form = 1 / (1 + 1 / (4 * E * (E - 1)) * math.sin(2 * z) ** 2)
        print(f"  E/V0={E}: matching T={Tn:.6f} R={Rn:.6f} T+R={Tn+Rn:.6f} formula T={form:.6f}")

    sec("Ramsauer-Townsend scale: first resonance of a well width 2a, E=(pi hbar/(2a))^2/(2m)")
    for nm, w in (("2a = 0.5 nm", 0.5e-9), ("2a = 0.2 nm", 0.2e-9)):
        E = (math.pi * HBAR / w) ** 2 / (2 * ME) / EV
        print(f"  {nm}: E_1 = {E:.2f} eV (+ shifts by the floor V0 if measured from the outside)")

    sec("Griffiths convention dictionary")
    print("z = l a (G) = k0 a (L), z0 same, kappa same; E_G = E_L - V0; E_G in (-V0, 0) <-> E_L in (0, V0); G scattering E>0 <-> L E>V0")


if __name__ == "__main__":
    main()
