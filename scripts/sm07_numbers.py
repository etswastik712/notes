"""SM07 (equipartition, virial theorem, magnetic systems) - numbers quoted in the chapter, all recomputed.

    .venv/bin/python -W ignore scripts/sm07_numbers.py
Recalled inputs (flagged in the chapter): JANAF Cp of N2, vibrational/rotational temperatures, <r^2> of helium, solar M, R, L, noble-gas susceptibilities (Schwabl Table 6.1).
"""
import numpy as np
from math import pi, sqrt, log, exp, cosh, tanh
from scipy import integrate

kB = 1.380649e-23; h = 6.62607015e-34; hbar = 1.054571817e-34; c = 2.99792458e8; G = 6.67430e-11; NA = 6.02214076e23; R = 8.314462618
muB = 9.2740100783e-24; me = 9.1093837015e-31; mp = 1.67262192369e-27; mH = 1.6735575e-27; a0 = 5.29177210903e-11; e = 1.602176634e-19; eps0 = 8.8541878128e-12
P = print
def sec(t): P("\n#####", t)

sec("generalised equipartition <x dH/dx> = kT : numerical check for V = a|q|^s")
for s in (1, 2, 4, 6):
    L = 12.0 if s >= 2 else 60.0
    num = integrate.quad(lambda q: abs(q) ** s * np.exp(-abs(q) ** s), -L, L, limit=400, points=[0.0])[0]
    den = integrate.quad(lambda q: np.exp(-abs(q) ** s), -L, L, limit=400, points=[0.0])[0]
    P(f"s = {s}: <V>/kT = {num / den:.5f} (1/s = {1 / s:.5f})")
P("gravity V = m g z (z>0): <m g z> = kT -> <z> = kT/(m g): for air at 288.15 K =", kB * 288.15 / (28.9647 * 1.66053906660e-27 * 9.80665), "m (scale height of SM03)")
P("ultrarelativistic: <p c> = kT per component -> E = 3NkT, P V = E/3 ; gamma =", 4 / 3)
for f_, name in ((3, "monatomic"), (5, "diatomic rigid"), (6, "nonlinear polyatomic rigid")):
    P(f"{name}: f = {f_}: C_V = {f_ / 2:.1f} R = {f_ / 2 * R:.2f} J/molK ; gamma = {1 + 2 / f_:.4f}")

sec("diatomic heat capacity: rotation (quantum rotor) and vibration (Einstein); N2")
def cvib(x): return x ** 2 * np.exp(x) / (np.exp(x) - 1) ** 2
th_vib = 2358.6 * 1.438777                        # cm^-1 -> K
P("theta_vib(N2) from omega_e = 2358.6 cm^-1:", th_vib, "K")
janaf = {298.15: 29.124, 500: 29.580, 1000: 32.697, 2000: 35.971}   # recalled JANAF Cp (J/mol/K)
for T, cp in janaf.items():
    pred = 3.5 * R + R * cvib(th_vib / T)
    P(f"T = {T:7.2f} K: Cp(pred) = 7/2 R + R f_vib(x={th_vib / T:.3f} -> {cvib(th_vib / T):.4f}) = {pred:.3f} ; recalled JANAF {cp:.3f} ; diff {pred - cp:+.3f} ({(pred - cp) / cp * 100:+.2f} %)")
P("N2 gamma at 300 K:", (3.5 * R) / (2.5 * R), " ; at 2000 K: ", (3.5 * R + R * cvib(th_vib / 2000)) / (2.5 * R + R * cvib(th_vib / 2000)))
# heteronuclear rotor
def c_rot(t):    # t = T/theta_r
    J = np.arange(0, 200)
    E = J * (J + 1.0); g = 2 * J + 1
    w = g * np.exp(-E / t); Z = w.sum(); E1 = (w * E).sum() / Z; E2 = (w * E ** 2).sum() / Z
    return (E2 - E1 ** 2) / t ** 2
for t in (0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 5.0, 20.0):
    P(f"rigid rotor T/theta_r = {t:5.1f}: C_rot/k = {c_rot(t):.4f}")
ts = np.linspace(0.2, 5, 2000); cr = np.array([c_rot(t) for t in ts])
P("rotor maximum:", cr.max(), "k at T/theta_r =", ts[cr.argmax()], "(overshoots the equipartition value 1 and then approaches it from above)")
P("theta_rot (recalled): H2 85.3 K, N2 2.88 K, O2 2.07 K, CO 2.77 K ; theta_vib: H2 6215 K, N2 3374 K (3393 from omega_e), O2 2256 K, CO2 bend 960 K")
x = 960 / 288.15
P("CO2 bend at 288.15 K: x =", x, " C/k =", cvib(x))

sec("virial theorem")
P("hydrogen atom: <K> = -E = 13.606 eV, <V> = 2E = -27.2 eV (s=-1: 2<K> = -<V>)")
Msun, Rsun, Lsun = 1.989e30, 6.957e8, 3.828e26
mu = 0.6
GM2R = G * Msun ** 2 / Rsun
P(f"G M^2/R (Sun) = {GM2R:.4e} J ; uniform-sphere U = -(3/5) G M^2/R = {-0.6 * GM2R:.4e} J ; thermal energy K = |U|/2 = {0.3 * GM2R:.4e} J")
Nsun = Msun / (mu * mH)
P(f"virial mean temperature: 3 N k T = |U|/... -> T_bar = (1/5) G M mu m_H/(k R) = {G * Msun * mu * mH / (5 * kB * Rsun):.3e} K ; (N = {Nsun:.3e} particles)")
P(f"Kelvin-Helmholtz time G M^2/(R L) = {GM2R / Lsun:.3e} s = {GM2R / Lsun / 3.156e7:.3e} yr ; with only half the released energy radiated: {GM2R / Lsun / 2 / 3.156e7:.3e} yr")
P(f"heat capacity of a virialised star C = -(3/2) N k = {-1.5 * Nsun * kB:.3e} J/K")
P("wall virial: <sum q.p_dot> = -3 P V ; with <sum q dH/dq> = 3 N k T -> P V = N k T ; check V=-2K: K = 3/2 N k T")

sec("magnetic thermodynamics: spin-1/2 paramagnet")
def S_over_Nk(x): return log(2 * cosh(x)) - x * tanh(x)
for B, T in ((1.0, 300.0), (1.0, 4.2), (1.0, 1.0), (1.0, 0.1), (0.01, 1.0)):
    xx = muB * B / (kB * T)
    P(f"B = {B} T, T = {T} K: x = {xx:.4f}, S/Nk = {S_over_Nk(xx):.4f} (ln2 = {log(2):.4f}), M/Nmu = {tanh(xx):.4f}")
x1 = muB * 1.0 / (kB * 1.0)
P(f"isothermal magnetisation at 1 K from 0 to 1 T: Delta S/Nk = {S_over_Nk(x1) - log(2):.4f} ; heat released per mole = T R |Delta S/Nk| = {1.0 * R * (log(2) - S_over_Nk(x1)):.3f} J/mol")
P("adiabatic demagnetisation (ideal paramagnet, S = S(B/T)): T_f = T_i B_f/B_i : from 1 K, 1 T to 0.01 T:", 1.0 * 0.01 / 1.0, "K ; from 2 K, 5 T to 0.05 T:", 2 * 0.05 / 5, "K")
P("(dT/dB)_S = T/B for the ideal paramagnet; entropy S/Nk at x = 0.5:", S_over_Nk(0.5), " (two-level value at eps/kT=1: 0.5822)")
P("negative temperature: reversing B flips E -> -E at fixed populations: x -> -x ; S unchanged ; T -> -T")

sec("Bohr-van Leeuwen and diamagnetism")
re_cgs = 2.8179403262e-13
sum_r2_He = 2 * 1.1935 * (a0 * 100) ** 2                      # cm^2, <r^2> per electron 1.1935 a0^2 (recalled)
chi_He = -NA * re_cgs * sum_r2_He / 6
P(f"Langevin diamagnetism of He: chi_mol = -N_A r_e <sum r^2>/6 = {chi_He:.3e} cm^3/mol (measured -1.9e-6, Schwabl Table 6.1) ; <sum r^2> = {sum_r2_He:.3e} cm^2")
P("Bohr-radius estimate (Schwabl): chi ~ -3e-6 cm^3/mol per atom with <r^2> ~ a0^2 and Z=2-ish")
C_cgs = 0.3751
P(f"Curie spin-1/2 (g=2) chi_mol at 300 K = {C_cgs / 300:.3e} cm^3/mol -> ratio to He diamagnetism: {C_cgs / 300 / abs(chi_He):.0f}")
tab = {"He": -1.9, "Ne": -7.2, "Ar": -15.4, "Kr": -28.0, "Xe": -43.0}
P("noble gases (Schwabl Table 6.1, 1e-6 cm^3/mol):", tab)
P("classical statistical mechanics: chi = 0 identically (Bohr-van Leeuwen); the cyclotron frequency at 1 T: omega_c =", e * 1.0 / me, "rad/s ; hbar omega_c / kT at 300 K:", hbar * e / me / (kB * 300))

sec("practice")
P("P2 virial for V ~ r^s: s=2 -> <K>=<V>; s=-1 -> E = -K = V/2; s=4 -> 2<K>=4<V>")
P("P6 Jeans-type: Sun potential energy in eV per particle: |U|/N =", 0.6 * GM2R / Nsun / e / 1e3, "keV (vs kT_bar =", kB * G * Msun * mu * mH / (5 * kB * Rsun) / e / 1e3, "keV)")
P("P9 Curie constant per mole 0.3751 emu K/mol: chi_mol(1 K) =", C_cgs, "cm^3/mol ; (note that this is a high-T result: at B=1 T it saturates)")
