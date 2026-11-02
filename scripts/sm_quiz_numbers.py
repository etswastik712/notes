"""Numbers quoted in the Statistical Mechanics Quiz Prep page (recomputed).  .venv/bin/python -W ignore scripts/sm_quiz_numbers.py"""
import numpy as np
from math import log, exp, sqrt, pi, comb, lgamma
from scipy import stats, special
kB = 1.380649e-23; u = 1.66053906660e-27; g0 = 9.80665; R = 8.314462618; h = 6.62607015e-34
P = print
P("Stirling ln 100! =", lgamma(101), "; crude N ln N - N =", 100 * log(100) - 100, "; relative error", (lgamma(101) - (100 * log(100) - 100)) / lgamma(101))
P("Landauer kT ln2 at 300 K =", kB * 300 * log(2), "J =", kB * 300 * log(2) / 1.602176634e-19, "eV")
P("scale height air 288.15 K, 28.97 u:", kB * 288.15 / (28.97 * u * g0), "m ; CO2 44.01 u:", kB * 288.15 / (44.01 * u * g0))
N = 100; m = 0.6
I = log(2) + m * log(m) + (1 - m) * log(1 - m)
P(f"coin N={N}: I(0.6)={I:.6f}, Chernoff e^-NI={exp(-N * I):.4f}, exact P(X>=60)={stats.binom.sf(59, N, 0.5):.4f}")
N = 1000; P(f"coin N=1000: e^-NI={exp(-N * I):.3e}, exact P(X>=600)={stats.binom.sf(599, N, 0.5):.3e}")
P("two-level x=0.25: S/Nk =", -(0.25 * log(0.25) + 0.75 * log(0.75)), "; kT/eps =", 1 / log(3))
P("mixing 1 mol A + 1 mol B: 2 R ln2 =", 2 * R * log(2), "J/K; same gas: 0")
P("Poisson lambda=10: P(N<=5) =", stats.poisson.cdf(5, 10), "; P(N=0) for <N>=10:", exp(-10))
P("photon entropy per photon: 2 pi^4/(45 zeta3) =", 2 * pi ** 4 / (45 * special.zeta(3)), "; energy per photon / kT = pi^4/(30 zeta3) =", pi ** 4 / (30 * special.zeta(3)))
P("T_sun/T_e = 5772/254.6 =", 5772 / 254.6)
P("canonical Gamma law skewness sqrt(8/3N): N=100:", sqrt(8 / 300), " ; relative width sqrt(2/3N) N=100:", sqrt(2 / 300), " N=1e23:", sqrt(2 / 3e23))
P("hydrogen virial: K=13.606, V=-27.211, E=-13.606")
P("N=3,g=10: 220, 120, 166.7; ratios", 220 / (1000 / 6), 120 / (1000 / 6))
P("x=2 oscillator <E>/kT = x/2 coth x/2 =", 1 / np.tanh(1.0), " ; x=0.5:", 0.25 / np.tanh(0.25))
P("adiabatic demag: Tf = Ti Bf/Bi = 1 K * 0.01/1 =", 0.01)
P("Langmuir theta at P=3 P0:", 3 / 4, " ; P/P0 for theta=0.9:", 0.9 / 0.1)
P("equilibrium of Fermi function at eps-mu=kT: 1/(e+1) =", 1 / (np.e + 1), " ; BE 1/(e-1) =", 1 / (np.e - 1), "; MB e^-1 =", np.exp(-1))
