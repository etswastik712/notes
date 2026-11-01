"""SM05 (grand canonical ensemble, chemical equilibrium, Saha) - numbers quoted in the chapter, all recomputed.

    .venv/bin/python -W ignore scripts/sm05_numbers.py
"""
import numpy as np
from math import pi, sqrt, exp, log
from scipy import stats, optimize

kB = 1.380649e-23; h = 6.62607015e-34; u = 1.66053906660e-27; me = 9.1093837015e-31; eV = 1.602176634e-19; R = 8.314462618; NA = 6.02214076e23
atm = 101325.0
P = print
def sec(t): P("\n#####", t)

sec("ideal gas in the grand canonical ensemble: Poisson numbers")
for Nm in (3, 10, 30, 100):
    P(f"<N>={Nm:4d}: P(N=0) = {stats.poisson.pmf(0, Nm):.3e}; P(N=<N>) = {stats.poisson.pmf(Nm, Nm):.4f}; Gaussian peak {1 / sqrt(2 * pi * Nm):.4f}; sigma/<N> = {1 / sqrt(Nm):.3f}")
lam = lambda m, T: h / sqrt(2 * pi * m * kB * T)
mN2 = 28.0134 * u
P("N2 300 K 1 atm: z = n lambda^3 =", (atm / (kB * 300)) * lam(mN2, 300) ** 3, " mu/kT = ln z =", log((atm / (kB * 300)) * lam(mN2, 300) ** 3))

sec("number fluctuations and compressibility: Var N / <N> = n kT kappa_T")
n_w = 998.2 / 0.018015 * NA; kap_w = 4.59e-10; T = 293.15
S0 = n_w * kB * T * kap_w
P(f"water 20 C: n = {n_w:.3e} m^-3, kappa_T = {kap_w:.2e} /Pa (recalled): Var N/<N> = {S0:.4f} (ideal gas: 1); in a (1 nm)^3: <N> = {n_w * 1e-27:.1f}, sigma = {sqrt(S0 * n_w * 1e-27):.2f}; in (10 nm)^3: <N> = {n_w * 1e-24:.0f}, sigma/<N> = {sqrt(S0 / (n_w * 1e-24)):.2e}")
P("air STP: kappa_T = 1/P: Var N/<N> = 1 ; ratio water/ideal-gas-at-same-density =", S0)
P("energy fluctuations of the monatomic ideal gas: canonical Var E = (3/2) N (kT)^2 ; grand canonical adds (3kT/2)^2 Var N: total (15/4) N (kT)^2 ; ratio of std devs:", sqrt(15 / 4) / sqrt(3 / 2), " ; relative sigma_E/E: canonical", sqrt(2 / 3), "/sqrt N ; GC", sqrt(15 / 4) / 1.5, "/sqrt N")

sec("Langmuir adsorption, P0 = (kT/lambda^3) exp(-eps/kT)")
def P0(m, T, eps_eV): return kB * T / lam(m, T) ** 3 * exp(-eps_eV * eV / (kB * T))
for eps_eV, Ts in ((0.5, (300, 400, 600)), (0.1, (77, 150, 300))):
    for T_ in Ts:
        p0 = P0(mN2, T_, eps_eV)
        P(f"eps = {eps_eV} eV, T = {T_} K: kT/lambda^3 = {kB * T_ / lam(mN2, T_) ** 3:.3e} Pa ; P0 = {p0:.3e} Pa ; coverage at 1 bar = {1e5 / (1e5 + p0):.4f} ; at 1 Pa = {1 / (1 + p0):.3e}")

sec("single mode: Fermi-Dirac, Bose-Einstein, Maxwell-Boltzmann")
for x in (0.1, 0.5, 1.0, 2.0, 5.0, 10.0):
    P(f"(eps-mu)/kT = {x:5.1f}: FD = {1 / (exp(x) + 1):.5f}  BE = {1 / (exp(x) - 1):.5f}  MB = {exp(-x):.5f}")
P("(eps-mu)/kT = -1 (below mu): FD =", 1 / (exp(-1) + 1), " (BE diverges when mu >= eps)")
P("two-level occupation sums: mean number of 'sites' variance FD: <n>(1-<n>) at x=0:", 0.25)

sec("chemical equilibrium N2O4 <-> 2 NO2 (mass action)")
dG = 4.73e3
K = exp(-dG / (R * 298.15))
P(f"Delta G0 = +4.73 kJ/mol (recalled from tables: 2*51.3 - 97.9 = 4.7): K_p = {K:.4f}")
for Pbar in (10.0, 1.0, 0.1, 0.01):
    a = sqrt(K / (K + 4 * Pbar))
    P(f"P = {Pbar:6.2f} bar: dissociation alpha = {a:.3f}")
P("van 't Hoff: K(350 K) with Delta H = 57.2 kJ/mol (recalled):", K * exp(-57.2e3 / R * (1 / 350 - 1 / 298.15)))

sec("Saha equation for hydrogen")
def Ksaha(T):
    return (2 * pi * me * kB * T / h ** 2) ** 1.5 * exp(-13.605693 * eV / (kB * T))
def frac(T, n):
    K_ = Ksaha(T)
    # x^2/(1-x) n = K, stable root x = 2/(1+sqrt(1+4n/K))
    return 2 / (1 + sqrt(1 + 4 * n / K_)) if K_ > 0 else 0.0
P("prefactor (2 pi m_e kT/h^2)^{3/2} at 5800 K =", (2 * pi * me * kB * 5800 / h ** 2) ** 1.5, " ; exp(-I/kT) =", exp(-13.605693 * eV / (kB * 5800)), " ; K =", Ksaha(5800))
P("Schroeder: n_e = 2e19 m^-3 (photosphere electrons, metals included): n_p/n_H =", Ksaha(5800) / 2e19)
for T_ in (3000, 5800, 8000, 10000, 12000, 15000):
    P(f"T = {T_:6d} K: K = {Ksaha(T_):.3e} m^-3 ; ionised fraction for n_tot = 1e23: {frac(T_, 1e23):.4f} ; 1e20: {frac(T_, 1e20):.4f} ; 1e10: {frac(T_, 1e10):.4f}")
for n_ in (1e23, 1e20, 1e10):
    Th = optimize.brentq(lambda T_: frac(T_, n_) - 0.5, 2000, 40000)
    P(f"half ionisation at n = {n_:.0e}: T = {Th:.0f} K  (k T = {kB * Th / eV:.3f} eV = {kB * Th / eV / 13.6057:.3f} I)")
# recombination of the universe
eta = 6.1e-10; zeta3 = 1.2020569
def n_gamma(T): return 2 * zeta3 / pi ** 2 * (kB * T / (1.054571817e-34 * 2.99792458e8)) ** 3
def x_rec(T): return frac(T, eta * n_gamma(T))
for T_ in (3000, 3500, 3800, 4000, 4500):
    P(f"cosmic: T = {T_} K (z = {T_ / 2.7255 - 1:.0f}): n_gamma = {n_gamma(T_):.3e} m^-3, n_B = {eta * n_gamma(T_):.3e} m^-3, Saha ionised fraction = {x_rec(T_):.4f}")
Tr = optimize.brentq(lambda T_: x_rec(T_) - 0.5, 2500, 6000)
P("Saha half-recombination: T =", Tr, "K, z =", Tr / 2.7255 - 1, " (observed last scattering z ~ 1090, T ~ 2970 K: Saha overestimates because recombination is slower than equilibrium, recalled)")
P("n_gamma today (2.7255 K) =", n_gamma(2.7255), " n_B today =", eta * n_gamma(2.7255))

sec("practice")
P("P2: Poisson P(N=0) for <N>=3:", stats.poisson.pmf(0, 3), " ; P(N>=10) for <N>=3:", stats.poisson.sf(9, 3))
P("P3: kT ln 2 etc not needed")
P("P5 N2O4: at P = 0.5 bar alpha =", sqrt(K / (K + 2.0)))
P("P6: hydrogen at n=1e20 T=10000 K: K =", Ksaha(10000), " x =", frac(10000, 1e20))
P("P7 chemical potential of N2 relative to ideal-gas at 10 atm 300 K: mu - mu(1 atm) =", kB * 300 * log(10) / eV, "eV =", kB * 300 * log(10) * NA / 1e3, "kJ/mol")
