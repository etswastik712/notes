"""SM (statistical mechanics, Part II of the thermodynamics subject) - numbers quoted in SM01-SM03, all recomputed.

    .venv/bin/python -W ignore scripts/sm_numbers.py
"""
import numpy as np
from math import lgamma, log, log2, pi, sqrt, exp, comb
from scipy.special import gammaln, erfc, erf
from scipy import stats

R = 8.314462618; kB = 1.380649e-23; NA = 6.02214076e23; h = 6.62607015e-34; hb = h / (2 * pi)
u = 1.66053906660e-27; atm = 101325.0; eV = 1.602176634e-19; me = 9.1093837015e-31; muB = 9.2740100783e-24
a0 = 5.29177210903e-11
P = print


def sec(t): P("\n#####", t)


# ------------------------------------------------------------------ SM01
sec("SM01 binomial vs Gaussian")
N = 100
P("P(exactly 50 up of 100) exact  =", comb(N, 50) / 2 ** N)
P("Gaussian approx 1/sqrt(2 pi N/4) =", 1 / sqrt(2 * pi * N / 4))
P("P(|n-50|<=5) exact =", sum(comb(N, k) for k in range(45, 56)) / 2 ** N, " Gaussian (+-5.5, continuity corrected) =", erf(5.5 / (sqrt(2) * 5)))
P("sigma of n =", sqrt(N) / 2, " ; relative sigma/mean =", (sqrt(N) / 2) / (N / 2))

sec("SM01 Stirling")
for n in (1, 5, 10, 50, 100, 1000):
    ex = gammaln(n + 1)
    s1 = n * log(n) - n
    s2 = s1 + 0.5 * log(2 * pi * n)
    s3 = s2 + 1 / (12 * n)
    P(f"N={n:5d} ln N!={ex:12.5f}  N lnN-N={s1:12.5f} (err {ex - s1:8.4f})  +1/2 ln2piN={s2:12.5f} (err {ex - s2:8.5f}, N! rel err {1 - exp(s2 - ex):.4%})  +1/12N err {ex - s3:.2e}")

sec("SM01 density fluctuations in air at STP (0 C, 1 atm)")
n_air = atm / (kB * 273.15)
P("n =", n_air, " m^-3 (Loschmidt 2.687e25)")
for name, V in (("1 cm^3", 1e-6), ("1 um^3", 1e-18), ("(100 nm)^3", 1e-21), ("(10 nm)^3", 1e-24), ("(1 nm)^3", 1e-27)):
    Nn = n_air * V
    P(f"{name:11s} <N> = {Nn:.3e}   relative sd 1/sqrt(N) = {1 / sqrt(Nn):.2e}")
P("relative density variance for an ideal gas = kB T kappa_T / V -> kappa_T = 1/P :", kB * 273.15 / (atm * 1e-18), "for 1 um^3 (=1/N)")

sec("SM01 large deviations: coin, P(heads >= 60%)")
def I(m):
    return log(2) + m * log(m) + (1 - m) * log(1 - m)
for Nn in (100, 1000):
    k0 = int(0.6 * Nn)
    exact = stats.binom.sf(k0 - 1, Nn, 0.5)
    g = stats.norm.sf((k0 - 0.5 - Nn / 2) / (sqrt(Nn) / 2))
    ld = exp(-Nn * I(0.6))
    # refined: includes the Gaussian prefactor of the local limit
    pref = 1 / sqrt(2 * pi * Nn * 0.6 * 0.4)
    refined = ld * pref / (1 - exp(-log(0.6 / 0.4)))   # geometric sum of the tail terms
    P(f"N={Nn:5d} exact P(>=60%) = {exact:.4e}  Gaussian = {g:.4e}  exp(-N I) = {ld:.4e} (I(0.6) = {I(0.6):.5f})  with prefactor and geometric tail = {refined:.4e}")
P("I(m) quadratic approximation 2 (m-1/2)^2 at m=0.6 =", 2 * 0.1 ** 2, " vs exact", I(0.6))

sec("SM01 Cauchy: mean of N samples")
rng = np.random.default_rng(7)
for Nn in (1, 10, 100, 10000):
    x = rng.standard_cauchy((2000, Nn)).mean(axis=1)
    P(f"N={Nn:6d} median |mean| = {np.median(np.abs(x)):.3f} (Cauchy: 1.000 for every N) ; fraction |mean|>10 = {np.mean(np.abs(x) > 10):.3f} (theory 0.0635)")
P("exact fraction |x|>10 for standard Cauchy =", 1 - 2 / pi * np.arctan(10))

sec("SM01 Shannon entropy")
def H(p, base=2):
    p = np.array([q for q in p if q > 0]); return -(p * np.log(p)).sum() / log(base)
P("fair coin", H([.5, .5]), "bits; p=0.1 coin", H([.1, .9]), "bits;  fair die", H([1 / 6] * 6), "(log2 6 =", log2(6), ")")
P("p=0.1, N=1000 flips: typical sequences ln g = N H_nats =", 1000 * H([.1, .9], np.e), " (vs N ln 2 =", 1000 * log(2), ") ; ln C(1000,100) exact =", gammaln(1001) - gammaln(101) - gammaln(901))
q = np.array([.25, .25, .25, .25]); p = np.array([.5, .25, .125, .125])
P("KL D(p||q) =", (p * np.log(p / q)).sum() / log(2), "bits; log2(4) - H(p) =", 2 - H(p))

# ------------------------------------------------------------------ SM02
sec("SM02 hypersphere and the ideal-gas entropy: exact microcanonical vs Sackur-Tetrode")
def lnOmega_exact(Nn, V, E, m):
    """ln of V^N (2 pi m E)^{3N/2} / (N! Gamma(3N/2+1) h^{3N})  (cumulative phase-space volume / N! h^3N)."""
    return (Nn * log(V) + 1.5 * Nn * log(2 * pi * m * E) - gammaln(Nn + 1) - gammaln(1.5 * Nn + 1) - 3 * Nn * log(h))
def S_ST_over_k(Nn, V, T, m):
    return Nn * (log(V / Nn * (2 * pi * m * kB * T / h ** 2) ** 1.5) + 2.5)
m_He = 4.002602 * u; T = 300.0
for Nn in (10, 100, 1000, 10 ** 5):
    V = Nn * kB * T / atm
    E = 1.5 * Nn * kB * T
    ex = lnOmega_exact(Nn, V, E, m_He)
    st = S_ST_over_k(Nn, V, T, m_He)
    P(f"N={Nn:7d} ln Omega_cum = {ex:14.4f}  S_ST/k = {st:14.4f}  difference = {ex - st:8.4f}   -ln(pi sqrt6 N) = {-log(pi * sqrt(6) * Nn):.4f}   shell(delta=E) adds ln(3N/2): net {log(1.5 * Nn) - log(pi * sqrt(6) * Nn):.4f} = ln(3/(2 pi sqrt6)) = {log(3 / (2 * pi * sqrt(6))):.4f}")
P("exact algebra: ln Omega_cum = S_ST/k - ln(pi sqrt6 N) (from Stirling for N! and Gamma(3N/2+1)); the ln N pieces are irrelevant against N")

sec("SM02 Gibbs paradox")
P("mixing entropy, 1 mol A + 1 mol B at equal T, P:", 2 * R * log(2), "J/K  (= 2 R ln 2)")
P("without 1/N!, S(2V,2N) - 2 S(V,N) = 2 N k ln 2 ; for N = N_A :", 2 * NA * kB * log(2), "J/K")
P("Sackur-Tetrode, He 1 bar 298.15 K:", R * (log((kB * 298.15 / 1e5) * (2 * pi * m_He * kB * 298.15 / h ** 2) ** 1.5) + 2.5), "J/(mol K)")

sec("SM02 two-level system, E = n_up * eps")
def s_two(x): return -(x * log(x) + (1 - x) * log(1 - x))
for x in (0.1, 0.25, 0.5, 0.75, 0.9):
    kT_over_eps = 1 / log((1 - x) / x) if x != 0.5 else float('inf')
    P(f"x = n_up/N = {x:4.2f}  s/k = {s_two(x):.4f}  kT/eps = {kT_over_eps:.4f}  (T<0 for x>1/2)")
P("N=100, exactly 25 up: ln Omega =", gammaln(101) - gammaln(26) - gammaln(76), " ; N s(0.25) =", 100 * s_two(.25), " ; difference (Stirling prefactor) =", gammaln(101) - gammaln(26) - gammaln(76) - 100 * s_two(.25), " ; -0.5 ln(2 pi N x(1-x)) =", -0.5 * log(2 * pi * 100 * .25 * .75))
P("negative-temperature spin system: Purcell & Pound 1951 reversed field on LiF nuclei - quoted as history, not computed here")

sec("SM02 Einstein solids in contact (Schroeder-style): N_A=300, N_B=200, q=100")
NA_, NB_, q = 300, 200, 100
def lnW(Nn, qq): return gammaln(qq + Nn) - gammaln(qq + 1) - gammaln(Nn)
qa = np.arange(0, q + 1)
lw = np.array([lnW(NA_, a) + lnW(NB_, q - a) for a in qa])
i = lw.argmax()
P("peak at q_A =", qa[i], " ln Omega_tot(peak) =", lw[i], " log10 =", lw[i] / log(10), "  ln Omega_tot(all) =", lnW(NA_ + NB_, q), "  log10 =", lnW(NA_ + NB_, q) / log(10))
p = np.exp(lw - lw.max()); p /= p.sum()
mean = (qa * p).sum(); sd = sqrt(((qa - mean) ** 2 * p).sum())
P(f"<q_A> = {mean:.3f}  sd = {sd:.3f}   P(peak) = {p.max():.4f}   P(q_A = 0) = {p[0]:.2e}  P(q_A=100)= {p[-1]:.2e}")
sig2 = 1 / (NA_ / (60 * 360) + NB_ / (40 * 240))
P("Gaussian-width formula sigma^2 = 1/[N_A/(q_A(q_A+N_A)) + N_B/(q_B(q_B+N_B))] =", sig2, " sigma =", sqrt(sig2))
for Nn in (10, 100, 10 ** 4, 10 ** 6, 10 ** 22):
    P(f"N_A=N_B={Nn:.0e}, q=2N (q_A=N): sigma = sqrt(N) = {sqrt(Nn):.3g}, relative sigma/q_A = {1 / sqrt(Nn):.2e}")
P("temperature: kT/eps = 1/ln((q+N)/q): N=300,q=60 :", 1 / log((60 + 300) / 60), "; N=200,q=40:", 1 / log((40 + 200) / 40))

sec("SM02 phase-space area conservation (pendulum), numerical")
from scipy.integrate import solve_ivp
def rhs(t, y): return [y[1], -np.sin(y[0])]
th = np.linspace(0, 2 * pi, 400, endpoint=False)
blob0 = np.c_[1.6 + 0.35 * np.cos(th), 0.0 + 0.35 * np.sin(th)]
def area(poly): x, y = poly[:, 0], poly[:, 1]; return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))
for tf in (0, 4, 8, 16, 32):
    pts = np.array([solve_ivp(rhs, [0, tf], b, rtol=1e-11, atol=1e-12).y[:, -1] if tf > 0 else b for b in blob0])
    P(f"t={tf:3d}  polygon area = {area(pts):.5f}   (initial pi*0.35^2 = {pi * 0.35 ** 2:.5f}; polygon of 400 vertices undercounts slightly)")

# ------------------------------------------------------------------ SM03
sec("SM03 thermal wavelength and the classical criterion n lambda^3 << 1")
def lam(m, T): return h / sqrt(2 * pi * m * kB * T)
for name, m, T, nn in (("N2, 300 K, 1 atm", 28.0134 * u, 300, atm / (kB * 300)), ("He gas, 300 K, 1 atm", m_He, 300, atm / (kB * 300)),
                       ("He gas, 4.2 K, 1 atm", m_He, 4.2, atm / (kB * 4.2)), ("liquid He-4, 2.17 K (n = 2.18e28)", m_He, 2.17, 2.18e28),
                       ("electrons in Cu (n = 8.5e28), 300 K", me, 300, 8.5e28), ("H2 gas, 20 K, 1 atm", 2.016 * u, 20, atm / (kB * 20))):
    L = lam(m, T)
    P(f"{name:38s} lambda = {L * 1e9:9.4f} nm   n lambda^3 = {nn * L ** 3:.3e}")

sec("SM03 canonical ideal gas energy ~ Gamma(3N/2, kT)")
for Nn in (10, 100, 1000, 10 ** 23):
    kk = 1.5 * Nn
    P(f"N={Nn:.0e}: mean = {kk:.3g} kT, sd = {sqrt(kk):.4g} kT, rel sd = {1 / sqrt(kk):.3e}, skewness = {2 / sqrt(kk):.3e}, excess kurtosis = {6 / kk:.3e}")
Nn = 100; kk = 150; mean = kk; sd = sqrt(kk)
P("N=100: P(E > mean + 3 sd) Gamma =", stats.gamma.sf(mean + 3 * sd, kk), " Gaussian =", stats.norm.sf(3), " ; P(E < mean - 3 sd) Gamma =", stats.gamma.cdf(mean - 3 * sd, kk), " Gaussian =", stats.norm.cdf(-3))
Nn = 10; kk = 15; mean = kk; sd = sqrt(kk)
P("N=10: P(E > mean + 3 sd) Gamma =", stats.gamma.sf(mean + 3 * sd, kk), " Gaussian =", stats.norm.sf(3))
P("equipartition check: <E> = -d ln Z/d beta = (3N/2) kT, Var E = kT^2 C_V = (3N/2)(kT)^2 -> sd/mean = sqrt(2/(3N)); N=100:", sqrt(2 / 300))

sec("SM03 barometric formula (isothermal atmosphere), scale height kT/mg")
m_air = 28.9647 * u; g = 9.80665
for T in (288.15, 255.0, 220.0):
    H = kB * T / (m_air * g)
    P(f"T = {T:6.2f} K  H = kT/(m g) = {H:.1f} m ;  p(5.5 km)/p0 = {exp(-5500 / H):.4f} ; p(10 km)/p0 = {exp(-10000 / H):.4f} ; z at p0/2 = {H * log(2):.0f} m")
# ICAO standard atmosphere (troposphere, 6.5 K/km)
def p_std(z): return 101325 * (1 - 0.0065 * z / 288.15) ** 5.25588
P("standard atmosphere p(5.5 km) =", p_std(5500) / 1e3, "kPa, p(10 km) =", p_std(10000) / 1e3, "kPa ; isothermal 288.15 K:", 101.325 * exp(-5500 / (kB * 288.15 / (m_air * g))), "kPa and", 101.325 * exp(-10000 / (kB * 288.15 / (m_air * g))), "kPa")
P("heavier molecules: H(CO2, 288 K) =", kB * 288.15 / (44.0095 * u * g), " m ; H(H2) =", kB * 288.15 / (2.016 * u * g), " m ; H(He)=", kB * 288.15 / (4.0026 * u * g))
P("density ratio of two gases at height z: exp(-(m1-m2) g z/kT): O2 vs N2 at 100 km in a *mixed-isothermal* column would be exp(-(31.998-28.013) u g z / kT), z=100 km, T=288:", exp(-(31.998 - 28.013) * u * g * 1e5 / (kB * 288.15)))

sec("SM03 spin-1/2 paramagnet, M = N mu tanh(beta mu B)")
for B, T in ((1.0, 300.0), (1.0, 4.2), (1.0, 1.0), (1.0, 0.1), (5.0, 0.5)):
    x = muB * B / (kB * T)
    P(f"B={B} T, T={T:6.1f} K: x = mu_B B/kT = {x:.5f}, M/(N mu) = tanh x = {np.tanh(x):.5f}, Curie approx x = {x:.5f}")
P("molar saturation magnetisation N_A mu_B =", NA * muB, "J/(T mol)")
Cc = 4e-7 * pi * NA * muB ** 2 / kB
P("Curie constant per mole (SI), C = mu0 N_A mu_B^2 / k_B =", Cc, "K m^3/mol ; chi_mol(300 K) =", Cc / 300, "m^3/mol ; in CGS", Cc / (4 * pi * 1e-6), "emu K/mol (0.375 for g=2, S=1/2)")
P("Schottky maximum: C/k = 0.4392 at x = eps/kT =", 2.3994, "so kT = ", 1 / 2.3994, "eps ; with eps = 2 mu_B B and B=1 T:", 2 * muB * 1.0 / kB / 2.3994, "K")
x = np.linspace(0.01, 8, 200000); c = x ** 2 * np.exp(x) / (np.exp(x) + 1) ** 2
P("numerical Schottky peak: x* =", x[c.argmax()], " C*/k =", c.max())

sec("SM03 hydrogen atom: the partition function diverges")
E1 = 13.605693 * eV
def Zn(T, nmax):
    n = np.arange(1, nmax + 1, dtype=float)
    return (2 * n ** 2 * np.exp(-(E1 - E1 / n ** 2) / (kB * T))).sum()   # energies measured from the ground state
for T in (5800.0, 10000.0):
    P(f"T = {T:.0f} K (kT = {kB * T / eV:.3f} eV) partial sums Z(n_max) relative to ground state weight 2:",
      [(nm, float(f"{Zn(T, nm):.4g}")) for nm in (1, 2, 5, 45, 1000, 10000, 100000)])
x2 = exp(-(E1 * 0.75) / (kB * 5800)); P("population ratio n=2 : n=1 at 5800 K (8 states / 2 states) = 4 exp(-10.2 eV/kT) =", 4 * x2)
nH = 1e20; rsep = nH ** (-1 / 3); nmax = sqrt(rsep / (2 * a0))
P(f"plasma density {nH:.0e} m^-3: mean spacing {rsep:.3e} m, cutoff n_max ~ sqrt(r/2a0) = {nmax:.1f}")

sec("SM03 Gibbs canonical ensemble: volume fluctuations of an ideal gas")
P("relative sd of V = sqrt(kT kappa_T / <V>) with kappa_T = 1/P : = 1/sqrt(N) ; N = 100 ->", 1 / 10, "; N=1e23 ->", 1e23 ** -0.5)


# ------------------------------------------------------------------ practice-problem checks (SM01-SM03)
def Hent(pp_, base=2):
    pp_ = np.array([q_ for q_ in pp_ if q_ > 0]); return -(pp_ * np.log(pp_)).sum() / log(base)


sec("PRACTICE SM01")
n288 = atm / (kB * 288.15)
P("P3: n(288.15 K, 1 atm) =", n288, " N(1 um^3) =", n288 * 1e-18, " rel sd =", 1 / sqrt(n288 * 1e-18), " ; 100 molecules -> V =", 100 / n288, " r =", (3 * 100 / n288 / (4 * pi)) ** (1 / 3))
P("P4: 10^23 : N(ln N - 1) =", 1e23 * (log(1e23) - 1), " ; 0.5 ln(2 pi N) =", 0.5 * log(2 * pi * 1e23))
P("P5a: 2^-100 =", 2.0 ** -100, " ; P5b: I(0.7) =", I(0.7), " exp(-100 I) =", exp(-100 * I(0.7)), " exact tail (>=70) =", stats.binom.sf(69, 100, .5),
  " refined =", exp(-100 * I(0.7)) / sqrt(2 * pi * 100 * .7 * .3) / (1 - 0.3 / 0.7))
from math import factorial
for Nn in (10,):
    ex = factorial(Nn) ** 2 / factorial(2 * Nn + 1); sp_ = 4.0 ** (-Nn) * sqrt(pi / (4 * Nn))
    P(f"P6: N={Nn}: exact Beta = {ex:.4e}, saddle = {sp_:.4e}, ratio {sp_ / ex:.4f}")
P("P7: P(|mean|>10a) =", 1 - 2 / pi * np.arctan(10))
P("P8: H(0.1) bits =", Hent([.1, .9]), "; 1e6 flips ->", 1e6 * Hent([.1, .9]), "bits;  loaded die H =", Hent([.5, .25, .125, .125]), "D =", 2 - Hent([.5, .25, .125, .125]))
P("P9: beta eps = ln 4 =", log(4), " kT/eps =", 1 / log(4))
P("P10: excess kurtosis of spin sum = -2/N =", -2 / 100, " ; Gamma 6/k, k=150:", 6 / 150)

sec("PRACTICE SM02")
P("P2: ln C(100,25) =", gammaln(101) - gammaln(26) - gammaln(76), " Omega =", exp(gammaln(101) - gammaln(26) - gammaln(76)), " dS/dE discrete (n=25->26) = ln(75/26) =", log(75 / 26), " kT/eps =", 1 / log(75 / 26), " continuum =", 1 / log(3))
P("P3: x=0.9 -> kT/eps =", 1 / log(0.1 / 0.9))
P("P4: sigma_E/E_A, N_A=N_B=N/2:  2/sqrt(6N) with N=1e23 =", 2 / sqrt(6e23), " ; 0.816/sqrt N =", 0.816 / sqrt(1e23))
P("P5c: mixing 0.75/0.25 : -R(sum x ln x) =", -R * (0.75 * log(.75) + .25 * log(.25)), " per mole;  x4 mol =", -4 * R * (0.75 * log(.75) + .25 * log(.25)), " ; air 0.21/0.79:", -R * (0.21 * log(.21) + .79 * log(.79)), " R ln2 =", R * log(2))
tot = [comb(q_ + 2, 2) * comb(6 - q_ + 2, 2) for q_ in range(7)]
P("P6: products =", tot, " sum =", sum(tot), " C(11,6) =", comb(11, 6), " P(q_A=3) =", tot[3] / sum(tot), " P(q_A>4) =", (tot[5] + tot[6]) / sum(tot), " P(q_A>=4)=", sum(tot[4:]) / sum(tot))
NA_, NB_, qq = 300, 200, 100
lw2 = np.array([lnW(NA_, a_) + lnW(NB_, qq - a_) for a_ in range(qq + 1)]); pp = np.exp(lw2 - lw2.max()); pp /= pp.sum()
P("P7: exact P(q_A<=50) =", pp[:51].sum(), " Gaussian Phi(-1.77) =", stats.norm.cdf((50.5 - 60) / 5.3666), " (sigma 5.3666)")
Nn = 1e6
P("P9: N=1e6: P(|m-1/2|>1e-3) Gaussian two-sided =", 2 * stats.norm.sf(1e-3 * Nn / (sqrt(Nn) / 2)), " ; N=1e10: N*I =", 1e10 * 2 * (1e-3) ** 2, " log10 P ~", -1e10 * 2 * 1e-6 / log(10))
Tn = 300.0; En = 1.5 * kB * Tn; Vn = 1e-3
Nst = 4 * pi / 3 * Vn * (2 * m_He * En) ** 1.5 / h ** 3
P("P10: 2mE =", 2 * m_He * En, " (2mE)^1.5 =", (2 * m_He * En) ** 1.5, " N_states =", Nst, " V/lambda^3 =", Vn / lam(m_He, Tn) ** 3, " ratio =", Nst / (Vn / lam(m_He, Tn) ** 3), " (4pi/3)(3/2pi)^1.5 =", 4 * pi / 3 * (3 / (2 * pi)) ** 1.5)

sec("PRACTICE SM03")
x = 0.5
P("P1: paramagnet x=0.5: tanh =", np.tanh(x), " S/Nk =", log(2 * np.cosh(x)) - x * np.tanh(x), " C/Nk = x^2 sech^2 =", x ** 2 / np.cosh(x) ** 2, " ; two-level at eps/kT=1: S =", log(1 + exp(-1)) + 1 / (np.e + 1), " C =", np.e / (np.e + 1) ** 2)
P("P3: Everest 8849 m, isothermal 255 K: p/p0 =", exp(-8849 / (kB * 255 / (m_air * g))), " -> ", 101.325 * exp(-8849 / (kB * 255 / (m_air * g))), "kPa ; 288.15 K:", 101.325 * exp(-8849 / (kB * 288.15 / (m_air * g))), " ; standard atm:", p_std(8849) / 1e3, "; H(N2, 288.15 K) =", kB * 288.15 / (28.0134 * u * g))
nl3 = (atm / (kB * 300)) * lam(28.0134 * u, 300) ** 3
P("P4: n lambda^3 (N2, 300 K, 1 atm) =", nl3, " mu/kT =", log(nl3), " mu = ", kB * 300 * log(nl3) / eV, "eV =", kB * 300 * log(nl3) * NA / 1e3, "kJ/mol")
P("P5: Gibbs ensemble rel sd of V, N=1000: 1/sqrt(N+1) =", 1 / sqrt(1001))
kT_ = kB * 10000 / eV
Zc = Zn(10000.0, 45); p2 = 8 * exp(-10.2 / kT_) / Zc
P("P6: kT(1e4 K) =", kT_, " eV ; Z_cut(45) =", Zc, " ; p(n=2) =", p2, " ; ground-state fraction =", 2 / Zc)
P("P7: Schottky peak in T for B=1 T (eps=2 mu_B B): T* =", 2 * muB * 1.0 / kB / 2.3994, "K ; for B=5 T:", 2 * muB * 5.0 / kB / 2.3994)
P("P9: 1-D classical oscillator energy is exponential: P(E>3kT) =", exp(-3), " ; 3-D (Gamma(3)) P(E>3kT) =", stats.gamma.sf(3, 3))
P("P10: Gamma(3N/2) : ln Gamma(k) vs k ln k - k + 0.5 ln(2 pi/k), k=150:", gammaln(150), 150 * log(150) - 150 + 0.5 * log(2 * pi / 150))
