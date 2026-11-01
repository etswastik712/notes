"""SM06 (entropy, information, arrow of time) - numbers quoted in the chapter, all recomputed.

    .venv/bin/python -W ignore scripts/sm06_numbers.py
Inputs recalled and flagged in the chapter: S0=1361 W/m2, albedo 0.30, T_sun=5772 K, CMOS switching energies, NPP and Lorenz-cycle power, eta.
"""
import numpy as np
from math import pi, sqrt, log, exp, comb, lgamma
from scipy.special import zeta

kB = 1.380649e-23; hbar = 1.054571817e-34; c = 2.99792458e8; G = 6.67430e-11; sigma = 5.670374419e-8; R = 8.314462618; NA = 6.02214076e23
eV = 1.602176634e-19
P = print
def sec(t): P("\n#####", t)

sec("Boltzmann entropy of macrostates: N = 100 molecules, n in the left half")
N = 100
for n in (50, 55, 60, 70, 100):
    lw = lgamma(N + 1) - lgamma(n + 1) - lgamma(N - n + 1)
    P(f"n = {n:3d}: ln|Gamma_M|/|Gamma| = {lw - N * log(2):9.4f} ; fraction of phase space = {comb(N, n) / 2 ** N:.4e} ; S_B/k = {lw:.3f} (S_B,max/k = {lgamma(N + 1) - 2 * lgamma(N / 2 + 1):.3f} = ln C(100,50))")
P("Gaussian estimate: S_B(n) - S_max = -2 (n - N/2)^2 / N :  n=60 ->", -2 * 100 / 100, " (exact", (lgamma(101) - lgamma(61) - lgamma(41)) - (lgamma(101) - 2 * lgamma(51)), ")")

sec("operational meaning of mixing entropy, Szilard engine, Landauer")
T = 298.15
P("W_max (mixing He+Ar, 1 mol each, semipermeable membranes) = 2 R T ln2 =", 2 * R * T * log(2), "J =", 2 * R * T * log(2) / 1e3, "kJ")
for T_ in (300.0, 77.0, 4.2):
    P(f"T = {T_:6.1f} K: kT ln2 = {kB * T_ * log(2):.4e} J = {kB * T_ * log(2) / eV * 1e3:.3f} meV")
P("1 mol of bits erased at 298.15 K: N_A kT ln2 = R T ln2 =", R * T * log(2), "J ; = T * (R ln2) with R ln2 =", R * log(2), "J/K")
P("erasing 1 GB (8e9 bits) at 300 K: >=", 8e9 * kB * 300 * log(2), "J ; 1 TB:", 8e12 * kB * 300 * log(2), "J")
LB = kB * 300 * log(2)
for E_, lab in ((1e-17, "1e-17 J (order of a modern gate switch, recalled)"), (1e-15, "1e-15 J (older / long wire, recalled)")):
    P(f"{lab}: ratio to the Landauer bound = {E_ / LB:.2e}")
P("Szilard: work per cycle kT ln2 at 300 K =", LB, " ; ln2 in bits = 1 ; D((1,0)||(1/2,1/2)) = ln2 =", log(2))
P("gas confined to half the volume (N_A molecules): availability kT D = RT ln2 =", R * T * log(2), "J")

sec("radiation entropy and the Earth's entropy budget")
a_rad = 4 * sigma / c
P("a = 4 sigma/c =", a_rad, " ; entropy per photon s/n = 2 pi^4/(45 zeta(3)) k =", 2 * pi ** 4 / (45 * zeta(3)), " k ; energy per photon 2.701 kT:", pi ** 4 / (30 * zeta(3)))
S0, alb, Ts, Rearth = 1361.0, 0.30, 5772.0, 6.371e6
J = (1 - alb) * S0 / 4
Te = (J / sigma) ** 0.25
A = 4 * pi * Rearth ** 2
s_in, s_out = 4 / 3 * J / Ts, 4 / 3 * J / Te
P(f"absorbed J = {J:.1f} W/m2 ; T_e = {Te:.1f} K ; entropy flux in (4/3)J/T_sun = {s_in:.4f} W/m2/K ; out (4/3)J/T_e = {s_out:.4f} ; production = {s_out - s_in:.4f} W/m2/K ; whole Earth = {(s_out - s_in) * A:.3e} W/K (A = {A:.3e} m2)")
P(f"photon number ratio out/in = T_sun/T_e = {Ts / Te:.2f} ; entropy ratio out/in = {s_out / s_in:.2f}")
P(f"exergy (available free-energy) flux of the absorbed sunlight relative to T_e: J - T_e s_in = {J - Te * s_in:.1f} W/m2 = Petela psi J with psi = 1 - (4/3)(T_e/T_s) + (1/3)(T_e/T_s)^4 = {1 - 4 / 3 * Te / Ts + (Te / Ts) ** 4 / 3:.4f} -> {J * (1 - 4 / 3 * Te / Ts + (Te / Ts) ** 4 / 3):.1f} W/m2 ; naive Carnot (1 - T_e/T_s) J = {(1 - Te / Ts) * J:.1f}")
ex = J - Te * s_in
P("NPP ~ 130 TW (recalled) =", 130e12 / A, "W/m2 =", 130e12 / A / ex * 100, "% of the exergy flux ; Lorenz cycle ~2.5 W/m2 (recalled) =", 2.5 / ex * 100, "% of exergy")

sec("entropy of the observable Universe's photons and of black holes")
T0 = 2.7255
ngam = 2 * zeta(3) / pi ** 2 * (kB * T0 / (hbar * c)) ** 3
Rc = 4.4e26
V = 4 / 3 * pi * Rc ** 3
Sg = 2 * pi ** 4 / (45 * zeta(3)) * ngam * V
P(f"n_gamma = {ngam:.4e} m^-3 ; V(R=4.4e26 m) = {V:.3e} m3 ; N_gamma = {ngam * V:.3e} ; S_photons = {Sg:.3e} k")
Msun = 1.989e30
def S_bh(M): return 4 * pi * G * M ** 2 / (hbar * c)
P(f"Bekenstein-Hawking S/k = 4 pi G M^2/(hbar c): 1 Msun: {S_bh(Msun):.3e} ; Sgr A* (4.3e6 Msun): {S_bh(4.3e6 * Msun):.3e} ; compare photons {Sg:.2e}")
P("Hawking temperature of 1 Msun: hbar c^3/(8 pi G M k) =", hbar * c ** 3 / (8 * pi * G * Msun * kB), "K")

sec("heat flow entropy production")
P("100 W from 500 K to 300 K: S_dot =", 100 * (1 / 300 - 1 / 500), "W/K ; lost work T0 * S_dot at T0 = 300 K:", 300 * 100 * (1 / 300 - 1 / 500), "W ; Carnot work available at 500/300: ", 100 * (1 - 300 / 500), "W")

sec("von Neumann / entanglement entropy (Page)")
rng = np.random.default_rng(2)
def avg_SA(nq, mA, trials=300):
    dA, dB = 2 ** mA, 2 ** (nq - mA)
    out = []
    for _ in range(trials):
        psi = rng.standard_normal((dA, dB)) + 1j * rng.standard_normal((dA, dB)); psi /= np.linalg.norm(psi)
        s2 = np.linalg.svd(psi, compute_uv=False) ** 2
        s2 = s2[s2 > 1e-14]; out.append(-(s2 * np.log(s2)).sum())
    return np.mean(out), np.std(out)
for nq, mA in ((12, 6), (12, 3), (10, 5), (14, 7), (14, 2)):
    dA, dB = 2 ** mA, 2 ** (nq - mA)
    if dA <= dB: pred = log(dA) - dA / (2 * dB)
    else: pred = log(dB) - dB / (2 * dA)
    m, sd = avg_SA(nq, mA)
    P(f"N={nq} qubits, A={mA}: simulated <S_A> = {m:.4f} (sd {sd:.4f}) ; Page ln d_A - d_A/(2 d_B) = {pred:.4f} ; max ln d_A = {log(min(dA, dB)):.4f}")
P("singlet: reduced state diag(1/2,1/2): S_A = ln2 =", log(2), "= 1 bit")

sec("practice")
P("P2 two-box: probability that all 100 molecules are on one side:", 2 * 0.5 ** 100)
P("P5 Szilard with N=2 molecules?  skip")
P("P6 Landauer: dissipation of a 1 GHz processor erasing 1e9 bits/s at the bound, 300 K:", 1e9 * LB, "W")
P("P7 information entropy of English-like 27 letters uniform: ", log(27) / log(2), "bits")
