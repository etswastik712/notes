"""SM04 (kinetic theory) - numbers quoted in the chapter, all recomputed.

    .venv/bin/python -W ignore scripts/sm04_numbers.py
Measured transport coefficients are recalled standard-table values (CRC / NIST, 300 K, 1 atm, good to ~1 %); they are inputs, flagged as such.
"""
import os, sys
import numpy as np
from math import pi, sqrt, log, exp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sm04_sims as sims

kB = 1.380649e-23; NA = 6.02214076e23; h = 6.62607015e-34; u = 1.66053906660e-27; R = 8.314462618; atm = 101325.0
P = print


def sec(t): P("\n#####", t)


sec("time scales of an air-like gas (BBGKY ordering)")
T = 300.0; d = 3.7e-10; m = 28.0134 * u
n = atm / (kB * T)
vbar = sqrt(8 * kB * T / (pi * m)); vrms = sqrt(3 * kB * T / m)
lam = 1 / (sqrt(2) * n * pi * d ** 2)
tau_c = d / vbar; tau_x = lam / vbar
P(f"n = {n:.3e} m^-3 ; vbar = {vbar:.1f} m/s ; lambda = {lam * 1e9:.1f} nm = {lam / d:.0f} d ; n d^3 = {n * d ** 3:.2e}")
P(f"tau_c = d/vbar = {tau_c:.2e} s ; tau_x = lambda/vbar = {tau_x:.2e} s ; ratio = {tau_c / tau_x:.2e} (compare n d^3 = {n * d ** 3:.2e}) ; collision rate = {1 / tau_x:.2e} /s")
for L, name in ((1e-3, "1 mm"), (1.0, "1 m")):
    P(f"tau_U = L/vbar for L = {name}: {L / vbar:.2e} s")
P("dimensional estimate (Kardar): v=100 m/s, d=1e-10, n=1e26: tau_c =", 1e-10 / 100, " tau_x = 1/(n v d^2) =", 1 / (1e26 * 100 * 1e-20), " n d^3 =", 1e26 * 1e-30)

sec("Knudsen number")
for Lname, L in (("1 um channel", 1e-6), ("1 cm", 1e-2), ("10 cm vessel at 1 atm", 0.1), ("10 cm vessel at 0.068 Pa", 0.1)):
    lam_ = lam if "0.068" not in Lname else lam * atm / 0.068
    P(f"{Lname:26s} lambda = {lam_:.3e} m   Kn = {lam_ / L:.3e}")
P("air at 10 km: lambda = 191 nm (TH06); 100 km altitude: n ~ 1.2e19 m^-3 -> lambda ~", 1 / (sqrt(2) * 1.2e19 * pi * d ** 2), "m")

sec("viscosity: mean-free-path estimate versus the Chapman-Enskog hard-sphere value")
def eta_ce(m, T, d): return 5 / 16 * sqrt(m * kB * T / pi) / d ** 2
def eta_crude(m, T, d): return 2 / (3 * pi) * sqrt(m * kB * T / pi) / d ** 2     # (1/3) n m vbar lambda
mair = 28.9647 * u
P(f"air (m = 28.96 u, d = 3.7 A, 300 K): crude (1/3) n m vbar lambda = {eta_crude(mair, 300, d) * 1e6:.2f} uPa s ; Chapman-Enskog first approx = {eta_ce(mair, 300, d) * 1e6:.2f} uPa s ; measured ~ 18.5 uPa s (recalled)")
P("crude / exact =", 2 / (3 * pi) / (5 / 16), "  (coefficient 0.2122 vs 0.3125)")
P("Maxwell's result: eta independent of density: (1/3) n m vbar lambda with lambda = 1/(sqrt2 n sigma) -> n cancels; eta = (2/3pi) sqrt(m k T/pi)/d^2")

sec("noble gases: viscosity gives the diameter, the diameter then predicts nothing new; conductivity from viscosity is the test")
data = {  # name: (mass u, eta uPa s, kappa W/m/K) at 300 K, 1 atm (recalled CRC/NIST)
    "He": (4.0026, 19.9, 0.1560), "Ne": (20.180, 31.8, 0.0493), "Ar": (39.948, 22.7, 0.01772), "Kr": (83.798, 25.6, 0.00949), "Xe": (131.29, 23.2, 0.00569)}
for name, (mu, eta_u, kap) in data.items():
    mm = mu * u; eta = eta_u * 1e-6
    dd = sqrt(5 / 16 * sqrt(mm * kB * 300 / pi) / eta)
    kpred = 15 / 4 * kB / mm * eta
    Pr = 5 / 2 * kB / mm * eta / kap
    P(f"{name}: d from eta = {dd * 1e10:.2f} A ; kappa_pred = (15/4)(k/m) eta = {kpred:.5f} vs measured {kap:.5f} (ratio {kpred / kap:.3f}) ; Prandtl = c_p eta/kappa = {Pr:.3f} (monatomic exact 2/3 = {2 / 3:.3f})")
P("BGK / single-time approximation: kappa = (5/2)(k/m) eta  -> Pr = 1 ; exact first approx: (15/4)(k/m) eta -> Pr = 2/3")

sec("diatomic (modified Eucken) and air")
M = 0.0280134; cv = 5 / 2 * R / M; eta = 17.9e-6
P(f"N2: kappa_Eucken = eta (c_v + 9R/4M) = {eta * (cv + 9 * R / (4 * M)):.4f} W/m/K (measured 0.0260) ; modified Eucken/measured = {eta * (cv + 9 * R / (4 * M)) / 0.0260:.3f}; naive eta c_v-like with (15/4): {15 / 4 * R / M * eta:.4f}")
rho_air = atm * 0.0289647 / (R * 300)
eta_a = 18.5e-6
P(f"air at 300 K: rho = {rho_air:.3f} kg/m3 ; nu = eta/rho = {eta_a / rho_air:.3e} m2/s ; D_self = (6/5) nu = {1.2 * eta_a / rho_air:.3e} m2/s ; thermal diffusivity kappa/(rho c_p) = {0.0262 / (rho_air * 1005):.3e} m2/s ; Pr = {1005 * eta_a / 0.0262:.3f}")
P(f"time for a 1 cm shear (momentum) perturbation to diffuse: L^2/nu = {1e-4 / (eta_a / rho_air):.2f} s ; for 1 m: {1.0 / (eta_a / rho_air):.3e} s")

sec("speed of sound from the Euler equations")
for name, g, Mm in (("He", 5 / 3, 4.0026e-3), ("Ar", 5 / 3, 39.948e-3), ("N2", 1.4, 28.0134e-3), ("air", 1.4, 28.9647e-3)):
    P(f"{name:3s} c = sqrt(gamma R T/M) at 293.15 K = {sqrt(g * R * 293.15 / Mm):.1f} m/s")
P("ratio of mean molecular speed to sound speed (monatomic): vbar/c =", sqrt(8 / pi) / sqrt(5 / 3), " ; vrms/c =", sqrt(3 / (5 / 3)))

sec("Boltzmann H and the Sackur-Tetrode entropy (analytic check)")
m_He = 4.002602 * u
T = 298.15; Pp = 1e5; nn = Pp / (kB * T); lamHe = h / sqrt(2 * pi * m_He * kB * T)
S_per_N = -log(nn * lamHe ** 3) + 2.5
P("S/Nk = -ln(n lambda^3) + 5/2 =", S_per_N, " -> S =", S_per_N * R, "J/(mol K) (Sackur-Tetrode, He 1 bar 298.15 K; measured 126.15)")
P("equilibrium H per volume with f = n (2 pi m kT)^-3/2 exp(-p^2/2mkT): <ln(h^3 f)>_f = ln(n lambda^3) - 3/2 ; S = -k int f (ln h^3 f - 1) = N k (-ln n lambda^3 + 5/2)")

sec("Kac ring")
for N, k_, steps in ((400, 80, 120), (10000, 1000, 60)):
    m_ = sims.kac_ring(N, k_, steps, seed=3)
    mu_ = k_ / N
    th = (1 - 2 * mu_) ** np.arange(steps + 1)
    P(f"N={N}, k={k_}, mu={mu_}: m(0)={m_[0]:.3f}  m(5)={m_[5]:.3f} (Stosszahl {th[5]:.3f})  m(10)={m_[10]:.3f} ({th[10]:.3f})  m(20)={m_[20]:.3f} ({th[20]:.3f})  noise 1/sqrt(N)={1 / sqrt(N):.3f}")
m_ = sims.kac_ring(400, 80, 800, seed=3)
P("N=400, k=80 (even): rms of m(t) for 15<=t<=300 =", float(np.sqrt(np.mean(m_[15:301] ** 2))), " (theory ~ sqrt(2.1/N)=%.3f)" % np.sqrt(2.1 / 400), " ; m(t=400) =", m_[400], " m(t=800) =", m_[800], " ; first return of m to 1 at t =", int(np.argmax(m_[1:] == 1.0)) + 1)
m_ = sims.kac_ring(101, 21, 250, seed=5)
P("N=101, k=21 (odd): m(101) =", m_[101], " m(202) =", m_[202])
P("Poincare recurrence time of the ring is N (k even) or 2N (k odd): for N=10^4: 1e4 steps; for N = 1e23 sites: absurd; relaxation takes ~ 1/(2 mu) steps")

sec("Kac velocity model (N = 1e5, uniform start)")
res = sims.kac_model()
t = np.array(res["t"]); kurt = np.array(res["kurt"]); Hh = np.array(res["H"])
for tt in (0, 1, 2, 4, 8, 12, 20):
    P(f"t = {tt:2d}: excess kurtosis = {kurt[tt]:+.4f} (theory -1.2 exp(-t/4) = {-1.2 * exp(-tt / 4):+.4f}) ; H = {Hh[tt]:+.4f}")
P("H_infinity (Gaussian, unit variance) = -1/2 ln(2 pi e) =", -0.5 * log(2 * pi * np.e), " ; H_0 (uniform on [-sqrt3,sqrt3]) = -ln(2 sqrt3) =", -log(2 * sqrt(3)))
P("fraction of H-steps that increased H by more than the noise 0.003:", np.mean(np.diff(Hh) > 0.003))
P("analytic rate: d m4/dt = -(1/4)(m4 - 3 sigma^4) per unit time with one collision per particle")

sec("practice-problem numbers")
P("P1 BGK eta = n k T tau: air, tau = tau_x =", tau_x, "s -> eta =", n * kB * 300 * tau_x * 1e6, "uPa s (order of magnitude; exact 18.5)")
P("P2 mean free path at 1 Pa, 300 K:", kB * 300 / (sqrt(2) * pi * d ** 2 * 1.0), "m ; Kn for 10 cm vessel:", kB * 300 / (sqrt(2) * pi * d ** 2 * 1.0) / 0.1)
v1 = (1.0, 0.0); v2 = (0.0, 0.0)
P("P4 Kac collision invariance check: v1^2+v2^2 under rotation by 0.7 rad:", (np.cos(.7) * 3 + np.sin(.7) * 4) ** 2 + (-np.sin(.7) * 3 + np.cos(.7) * 4) ** 2, "vs 25")
P("P5 mean free time in He at 300 K, 1 atm (d = 2.2 A):", 1 / (sqrt(2) * (atm / (kB * 300)) * pi * (2.2e-10) ** 2 * sqrt(8 * kB * 300 / (pi * m_He))), "s")
P("P6 sound speed in He at 293 K:", sqrt(5 / 3 * R * 293.15 / 4.0026e-3), "m/s")
P("P7 Prandtl number of air (0.71) vs monatomic 2/3: c_p eta/kappa =", 1005 * 18.5e-6 / 0.0262)

sec("extra numbers for SM04 problems and examples")
mHe = 4.002602 * u; dHe = 2.2e-10; nHe = atm / (kB * 300)
lamHe = 1 / (sqrt(2) * nHe * pi * dHe ** 2); vHe = sqrt(8 * kB * 300 / (pi * mHe))
P(f"P1 He 300 K 1 atm (d=2.2 A): lambda = {lamHe * 1e9:.0f} nm, vbar = {vHe:.0f} m/s, tau_x = {lamHe / vHe:.2e} s, n d^3 = {nHe * dHe ** 3:.2e}, tau_c/tau_x = {(dHe / vHe) / (lamHe / vHe):.2e}")
P("P2 pressure for lambda = 1 cm (N2, 300 K, d=3.7 A):", kB * 300 / (sqrt(2) * pi * d ** 2 * 1e-2), "Pa")
P("P3 collision frequency per molecule sqrt2 n sigma vbar (N2 300 K 1 atm):", sqrt(2) * n * pi * d ** 2 * vbar, "/s ; per m^3 per second (n * rate / 2):", n * sqrt(2) * n * pi * d ** 2 * vbar / 2)
dM = 3e-3; vrim = 400.0
P(f"P4 UF6 centrifuge: ln alpha = dM v^2/(2RT) = {dM * vrim ** 2 / (2 * R * 300):.4f}  alpha = {exp(dM * vrim ** 2 / (2 * R * 300)):.4f} ; effusion: sqrt(352/349) = {sqrt(352 / 349):.4f}  ln = {log(sqrt(352 / 349)):.5f} ; ratio of ln alpha: {dM * vrim ** 2 / (2 * R * 300) / log(sqrt(352 / 349)):.1f}")
P("P6 Kac ring: t to reach |m| = 1e-2 for mu = 0.1:", log(100) / -log(0.8), " ; for mu=0.2:", log(100) / -log(0.6))
P("P7 Kac model: t for excess kurtosis -1.2 -> -0.012 :", 4 * log(100))
nu = 1.572e-5; DT = 2.216e-5
k1 = 2 * pi / 1e-2
P(f"P11 shear damping rate nu k^2 for 1 cm wavelength: {nu * k1 ** 2:.2f} /s -> tau = {1 / (nu * k1 ** 2):.3f} s ; heat: D_T k^2 = {DT * k1 ** 2:.2f} /s -> tau = {1 / (DT * k1 ** 2):.3f} s")
c_air = 343.2; omega = 2 * pi * 1000
Gam = 0.5 * (4 / 3 * nu + 0.4 * DT)
alpha = Gam * omega ** 2 / c_air ** 3
P(f"classical sound absorption of air at 1 kHz: Gamma = {Gam:.3e} m2/s ; alpha = Gamma omega^2/c^3 = {alpha:.3e} Np/m = {alpha * 8.686:.3e} dB/m (measured ~5e-3 dB/m, dominated by O2/N2 relaxation; recalled)")
P(f"P12 Re = U L / nu for U=10 m/s, L=1 m: {10 * 1 / nu:.3e} ; Ma = U/c = {10 / c_air:.3f} ; Kn = lambda/L = {lam / 1:.2e}")
P("Knudsen thermos: lambda = 1 cm at P =", kB * 300 / (sqrt(2) * pi * d ** 2 * 1e-2), "Pa")
P("Gaussian moments used for transport: <c^2 c_a c_b> = 5 (kT/m)^2 delta ; <c^4 c_a c_b> = 35 (kT/m)^3 delta ; check numerically:")
rng = np.random.default_rng(11); c3 = rng.standard_normal((2000000, 3)); c2 = (c3 ** 2).sum(axis=1)
P("   <c^2 c_x c_x> =", (c2 * c3[:, 0] ** 2).mean(), " (5) ; <c^4 c_x c_x> =", (c2 ** 2 * c3[:, 0] ** 2).mean(), " (35) ; <c_x^2 c_y^2> =", (c3[:, 0] ** 2 * c3[:, 1] ** 2).mean(), " (1)")
