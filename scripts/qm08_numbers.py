"""QM08 numbers: step, barrier, delta, double barrier, WKB/Gamow, Kronig-Penney. Units: hbar^2/2m = 1 unless stated.

.venv/bin/python -W ignore scripts/qm08_numbers.py
Everything analytic is cross-checked against a generic piecewise-constant transfer-matrix solver (tmat).
"""
import math

import numpy as np

HBARC = 197.3269804   # MeV fm
HBAR2_2ME = 3.80998   # eV Angstrom^2  (hbar^2/2m_e)
K0 = 5.1231           # nm^-1 eV^-1/2: sqrt(2 m_e eV)/hbar


def tmat(E, layers, x_edges, V_left=0.0, V_right=None):
    """Transmission/reflection for a piecewise-constant potential.
    layers: list of V values for the interior regions; x_edges: positions of the interfaces (len = len(layers)+1).
    Left and right outer regions have potentials V_left, V_right (default = V_left). Units hbar^2/2m=1 (k^2 = E - V)."""
    if V_right is None:
        V_right = V_left
    Vs = [V_left] + list(layers) + [V_right]
    ks = [np.sqrt(complex(E - v)) for v in Vs]
    n = len(Vs)
    # unknown coefficients (A_j, B_j) for psi_j = A_j e^{i k x} + B_j e^{-i k x}; propagate with interface matching
    M = np.eye(2, dtype=complex)
    for j, x in enumerate(x_edges):
        k1, k2 = ks[j], ks[j + 1]
        # [e^{ik1x} e^{-ik1x}; i k1 e^{ik1x} -i k1 e^{-ik1x}] [A1;B1] = same with k2 [A2;B2]
        L = np.array([[np.exp(1j * k1 * x), np.exp(-1j * k1 * x)], [1j * k1 * np.exp(1j * k1 * x), -1j * k1 * np.exp(-1j * k1 * x)]])
        Rm = np.array([[np.exp(1j * k2 * x), np.exp(-1j * k2 * x)], [1j * k2 * np.exp(1j * k2 * x), -1j * k2 * np.exp(-1j * k2 * x)]])
        M = np.linalg.solve(Rm, L) @ M
    # [A_N, B_N] = M [A_0, B_0]; B_N = 0, A_0 = 1
    r = -M[1, 0] / M[1, 1]
    t = M[0, 0] + M[0, 1] * r
    kL, kR = ks[0], ks[-1]
    T = (abs(t) ** 2 * kR.real / kL.real) if kR.real > 0 else 0.0
    R = abs(r) ** 2
    return T, R


def sec(t):
    print("\n=== " + t + " ===")


def barrier_T(E, V0, L):
    if E < V0:
        kap = math.sqrt(V0 - E)
        return 1 / (1 + V0 ** 2 * math.sinh(kap * L) ** 2 / (4 * E * (V0 - E)))
    k2 = math.sqrt(E - V0)
    return 1 / (1 + V0 ** 2 * math.sin(k2 * L) ** 2 / (4 * E * (E - V0)))


def main():
    sec("step potential V=0 (x<0), V0 (x>0): T = 4 k1 k2/(k1+k2)^2, R = ((k1-k2)/(k1+k2))^2")
    V0 = 1.0
    for E in (1.001, 1.2, 2.0, 4.0, 10.0):
        k1, k2 = math.sqrt(E), math.sqrt(E - V0)
        Tf = 4 * k1 * k2 / (k1 + k2) ** 2
        Rf = ((k1 - k2) / (k1 + k2)) ** 2
        # tmat with a very thick layer is not needed: use tmat with 0-width: emulate single interface using one layer of length ~0
        Tn, Rn = tmat(E, [V0], [0.0, 1e-9], V_left=0.0, V_right=V0)
        print(f"E/V0={E:6.3f}: T={Tf:.6f} R={Rf:.6f} T+R={Tf+Rf:.6f} | transfer matrix T={Tn:.6f} R={Rn:.6f}")
    print("E<V0: total reflection R=1; evanescent decay kappa = sqrt(V0-E); penetration depth 1/kappa")
    print("electron, E=1 eV vs V0=2 eV: kappa =", round(K0 * math.sqrt(1), 3), "nm^-1 -> 1/kappa =", round(1 / (K0 * 1.0), 4), "nm")

    sec("rectangular barrier: exact vs thick-barrier approx vs transfer matrix (units hbar^2/2m=1, V0=1)")
    for E, L in ((0.5, 1.0), (0.5, 3.0), (0.2, 4.0), (0.9, 2.0), (0.5, 8.0)):
        kap = math.sqrt(1 - E)
        Te = barrier_T(E, 1.0, L)
        Ta = 16 * (E / 1.0) * (1 - E / 1.0) * math.exp(-2 * kap * L)
        Tn, Rn = tmat(E, [1.0], [0.0, L])
        print(f"E={E} L={L}: kappa L={kap*L:6.3f} exact T={Te:.6e}  tm T={Tn:.6e}  approx 16(E/V0)(1-E/V0)e^(-2 kappa L)={Ta:.6e}  WKB e^(-2kL)={math.exp(-2*kap*L):.3e}")
    sec("E>V0 over a barrier (resonances at k2 L = n pi)")
    for E, L in ((2.0, math.pi / 1.0), (2.0, 2.5)):
        print(f"E={E}, L={L:.4f}: T={barrier_T(E, 1.0, L):.6f}  (k2 L = {math.sqrt(E-1)*L:.4f})")

    sec("physical numbers: electron through a rectangular barrier")
    for nm, E_eV, V_eV, L_nm in (("E=1, V0=2, L=0.5 nm", 1, 2, 0.5), ("E=1, V0=2, L=1.0 nm", 1, 2, 1.0), ("E=4 eV, V0=5 eV, L=0.3 nm (STM-like)", 4, 5, 0.3)):
        kap = K0 * math.sqrt(V_eV - E_eV)     # nm^-1
        T = 1 / (1 + V_eV ** 2 * math.sinh(kap * L_nm) ** 2 / (4 * E_eV * (V_eV - E_eV)))
        print(f"{nm}: kappa={kap:.3f} nm^-1  kappa L={kap*L_nm:.3f}  T={T:.4e}  e^(-2kL)={math.exp(-2*kap*L_nm):.3e}")
    print("proton (m=1836 m_e) same barrier E=1, V0=2 eV, L=0.5 nm: kappa = 5.1231*sqrt(1836)=", round(K0 * math.sqrt(1836), 1), "nm^-1 -> T ~ e^(-2 kappa L) =", f"{math.exp(-2*K0*math.sqrt(1836)*0.5):.2e}")
    print("STM: phi = 4 eV work function: kappa = K0 sqrt(4) =", round(K0 * 2, 3), "nm^-1; current ~ e^(-2 kappa d): factor per 0.1 nm =", round(math.exp(2 * K0 * 2 * 0.1), 2))

    sec("delta barrier: T = 1/(1 + m alpha^2/(2 hbar^2 E)) (units hbar^2/2m=1 -> m/hbar^2 = 1/2): T = 1/(1 + alpha^2/(4E))")
    alpha = 2.0
    for E in (0.1, 1.0, 4.0, 25.0):
        Tf = 1 / (1 + alpha ** 2 / (4 * E))
        # thin tall barrier: width w, height alpha/w
        w = 1e-5
        Tn, _ = tmat(E, [alpha / w], [0.0, w])
        print(f"E={E}: T formula={Tf:.6f}  thin tall barrier tm={Tn:.6f}")
    print("same alpha well: bound state kappa = m alpha/hbar^2 = alpha/2 (hbar^2/2m=1), E = -alpha^2/4;  T and bound state share the pole at E = -alpha^2/4 (analytic continuation)")

    sec("double barrier (resonant tunnelling): two barriers V0=1, width 1, well width 2, units hbar^2/2m=1")
    V0, b, w = 1.0, 1.0, 2.0
    Es = np.linspace(0.01, 0.99, 98001)
    Ts = np.array([tmat(E, [V0, 0.0, V0], [0.0, b, b + w, 2 * b + w])[0] for E in Es[::20]])
    Es2 = Es[::20]
    idx = [i for i in range(1, len(Ts) - 1) if Ts[i] > Ts[i - 1] and Ts[i] > Ts[i + 1] and Ts[i] > 0.05]
    for i in idx:
        print(f"  resonance near E/V0={Es2[i]:.4f}: T={Ts[i]:.4f}")
    single = tmat(0.1, [V0], [0.0, b])[0]
    print("single barrier at E=0.1:", f"{single:.4e}", " double barrier off-resonance min:", f"{Ts.min():.3e}")
    # quasi-bound states of the isolated well of width w with walls V0: lecture convention with half-width a=w/2
    a = w / 2
    z0 = a * math.sqrt(V0)
    print(f"isolated well half-width a={a}: z0 = {z0:.4f}")
    import importlib.util, os
    spec = importlib.util.spec_from_file_location("q7", os.path.join(os.path.dirname(os.path.abspath(__file__)), "qm07_numbers.py"))
    q7 = importlib.util.module_from_spec(spec); spec.loader.exec_module(q7)
    print("  bound states of the isolated well E/V0 = (z/z0)^2:", [round((z / z0) ** 2, 4) for _, z in q7.states(z0)])

    sec("Gamow factor: U-238 alpha decay (Coulomb barrier), E_alpha = 4.267 MeV, daughter Z=90")
    E = 4.267
    Zd, Za = 90, 2
    ke2 = 1.439964  # MeV fm
    mu = 3727.379 * 234.04 / (234.04 + 4.0026) * 1.0    # MeV (alpha-Th234 reduced mass approx)
    mu = 3727.379 * (234.04 / (234.04 + 4.0026))
    Rc = Zd * Za * ke2 / E
    R = 1.2 * (234 ** (1 / 3) + 4 ** (1 / 3))
    x = R / Rc
    G = math.sqrt(2 * mu * E) / HBARC * Rc * (math.acos(math.sqrt(x)) - math.sqrt(x * (1 - x)))
    v = math.sqrt(2 * E / mu) * 2.99792458e23   # fm/s  (c = 2.998e23 fm/s)
    nu = v / (2 * R)
    lam = nu * math.exp(-2 * G)
    t_half = math.log(2) / lam
    print(f"R_c = {Rc:.2f} fm, R = {R:.2f} fm, x=R/R_c={x:.4f}, G={G:.3f}, 2G={2*G:.2f}, e^-2G={math.exp(-2*G):.2e}")
    print(f"v(outside)={v/2.998e23:.4f} c, nu = v/2R = {nu:.2e} s^-1, T_1/2 = {t_half:.2e} s = {t_half/3.156e7:.2e} yr (measured 4.468e9 yr)")
    # Th-232: E=4.012 MeV Z_d=88
    for nm, E_, Zd_, A_ , meas in (("U-238 -> Th-234", 4.267, 90, 234, 4.468e9), ("Th-232 -> Ra-228", 4.012, 88, 228, 1.405e10), ("Po-212 -> Pb-208", 8.954, 82, 208, 2.99e-7 / 3.156e7)):
        Rc_ = Zd_ * 2 * ke2 / E_
        R_ = 1.2 * (A_ ** (1 / 3) + 4 ** (1 / 3))
        mu_ = 3727.379 * A_ / (A_ + 4.0026)
        x_ = R_ / Rc_
        G_ = math.sqrt(2 * mu_ * E_) / HBARC * Rc_ * (math.acos(math.sqrt(x_)) - math.sqrt(x_ * (1 - x_)))
        v_ = math.sqrt(2 * E_ / mu_) * 2.99792458e23
        th = math.log(2) / (v_ / (2 * R_) * math.exp(-2 * G_)) / 3.156e7
        print(f"{nm}: 2G={2*G_:.1f}  estimated T1/2 = {th:.2e} yr  measured {meas:.2e} yr  ratio est/meas = {th/meas:.2e}")
    print("Geiger-Nuttall: log10 T ~ a Z/sqrt(E) + b: 2G ~ 2 pi Z_d Z_a e^2/(4 pi eps0 hbar v) for x->0 =", round(2 * math.pi * Zd * Za * ke2 / (HBARC * math.sqrt(2 * E / mu)), 2))

    sec("Kronig-Penney (delta comb): cos(qa) = cos(y) + P sin(y)/y, y = ka, P = m alpha a/hbar^2")
    for P in (0.0, 1.0, 3.0, 10.0):
        ys = np.linspace(1e-6, 4 * math.pi, 200001)
        f = np.cos(ys) + P * np.sin(ys) / ys
        allowed = np.abs(f) <= 1
        # band edges
        edges = np.where(np.diff(allowed.astype(int)) != 0)[0]
        be = [round(float(ys[i] / math.pi), 4) for i in edges]
        print(f"P={P}: band edges in units of pi (y/pi): {be}")
    print("P->inf: bands shrink to y = n pi (box of width a); P=0: free particle, no gaps")
    print("lowest band width in y/pi for P=3:", end=" ")
    ys = np.linspace(1e-6, math.pi, 200001); f = np.cos(ys) + 3 * np.sin(ys) / ys
    inside = ys[np.abs(f) <= 1]
    print(round(float(inside.min() / math.pi), 4), "to", round(float(inside.max() / math.pi), 4), "(top edge y=pi; bottom edge where f=1)")

    sec("probability current and transmission (check j_t/j_i = T)")
    E = 2.0
    k1, k2 = math.sqrt(E), math.sqrt(E - 1)
    t = 2 * k1 / (k1 + k2)
    print(f"step E=2V0: amplitude t={t:.4f}, |t|^2={t*t:.4f} (not T!), T = |t|^2 k2/k1 = {t*t*k2/k1:.4f}, R = {((k1-k2)/(k1+k2))**2:.4f}, T+R={t*t*k2/k1+((k1-k2)/(k1+k2))**2:.4f}")


if __name__ == "__main__":
    main()
