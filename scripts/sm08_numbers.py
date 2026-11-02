"""SM08 (quantum ensembles, density matrix, identical particles) - numbers quoted in the chapter, all recomputed.

    .venv/bin/python -W ignore scripts/sm08_numbers.py
"""
import itertools
import numpy as np
from math import comb, exp, log, pi, sqrt, factorial
from scipy import integrate, special

kB = 1.380649e-23; h = 6.62607015e-34; u = 1.66053906660e-27; muB = 9.2740100783e-24; me = 9.1093837015e-31; atm = 101325.0
P = print
def sec(t): P("\n#####", t)

sec("density matrix of a spin 1/2 (thermal) : Bloch vector")
for B, T in ((1.0, 1.0), (1.0, 4.2), (1.0, 300.0)):
    x = muB * B / (kB * T); r = np.tanh(x)
    lam = np.array([(1 + r) / 2, (1 - r) / 2])
    S = -(lam * np.log(lam)).sum()
    P(f"B={B} T, T={T} K: x={x:.4f} |r|=tanh x={r:.4f} ; eigenvalues {lam.round(4)} ; purity Tr rho^2=(1+r^2)/2={(1 + r * r) / 2:.4f} ; S={S:.4f} (SM07: 0.5099 at 1 K)")
P("pure state: |r|=1, S=0, purity 1 ; maximally mixed: r=0, S=ln2=", log(2), ", purity 1/2")

sec("counting states of N identical particles in g single-particle states")
for N, g in ((2, 3), (3, 3), (3, 10), (3, 100), (10, 1000), (10, 100)):
    dist = g ** N; bos = comb(N + g - 1, N); fer = comb(g, N) if g >= N else 0
    P(f"N={N}, g={g}: distinguishable {dist} ; bosons {bos} ; fermions {fer} ; classical g^N/N! = {dist / factorial(N):.1f} ; bosons/classical {bos / (dist / factorial(N)):.4f} ; fermions/classical {fer / (dist / factorial(N)):.4f}")
N, g = 2, 3
P("N=2, g=3: probability that both particles are in the same single-particle state: distinguishable (each state equally likely) 3/9 =", 3 / 9, "; bosons 3/6 =", 3 / 6, "; fermions 0/3 =", 0)

sec("exact Z_N by enumeration vs the recursion Z_N = (1/N) sum_l (+-)^{l-1} Z_1(l beta) Z_{N-l}")
levels = np.arange(0, 12)       # harmonic-like levels eps_k = k (units k_BT*beta = b)
b = 0.7
def Z1(bb): return np.exp(-bb * levels).sum()
def brute(N, stat):
    tot = 0.0
    for occ in itertools.product(range(N + 1 if stat == "B" else 2), repeat=len(levels)):
        if sum(occ) != N: continue
        tot += np.exp(-b * sum(o * e for o, e in zip(occ, levels)))
    return tot
def recursion(N, stat):
    Z = [1.0]
    for n in range(1, N + 1):
        s = 0.0
        for l in range(1, n + 1):
            sign = 1.0 if stat == "B" else (-1.0) ** (l - 1)
            s += sign * Z1(l * b) * Z[n - l]
        Z.append(s / n)
    return Z[N]
for N in (2, 3):
    for stat in ("B", "F"):
        P(f"N={N} {'bosons' if stat == 'B' else 'fermions'}: brute force {brute(N, stat):.8f}  recursion {recursion(N, stat):.8f}")

sec("pair correlation g(r) = 1 +- exp(-2 pi r^2 / lambda^2)")
for rl in (0.0, 0.25, 0.5, 0.75, 1.0, 1.5):
    e = exp(-2 * pi * rl ** 2)
    P(f"r/lambda = {rl:4.2f}: exp = {e:.4f}  bosons g = {1 + e:.4f}  fermions g = {1 - e:.4f}")
lam = lambda m, T: h / sqrt(2 * pi * m * kB * T)
P("N2, 300 K: lambda =", lam(28.0134 * u, 300) * 1e9, "nm ; mean spacing n^{-1/3} =", (atm / (kB * 300)) ** (-1 / 3) * 1e9, "nm ; ratio spacing/lambda =", (atm / (kB * 300)) ** (-1 / 3) / lam(28.0134 * u, 300), " exchange factor exp(-2 pi (d/lambda)^2) ~ 10^", -2 * pi * ((atm / (kB * 300)) ** (-1 / 3) / lam(28.0134 * u, 300)) ** 2 / log(10))
P("Cu electrons 300 K: lambda = 4.30 nm, spacing (8.5e28)^(-1/3) =", (8.5e28) ** (-1 / 3) * 1e9, "nm : spacing/lambda =", (8.5e28) ** (-1 / 3) / 4.3e-9)

sec("two particles in an infinite well (L = 1), states 1 and 2: <(x1-x2)^2>")
x = np.linspace(0, 1, 200001)
phi = lambda n: np.sqrt(2) * np.sin(n * pi * x)
x1 = integrate.simpson(phi(1) * x * phi(1), x=x); x2 = integrate.simpson(phi(2) * x * phi(2), x=x)
xx1 = integrate.simpson(phi(1) ** 2 * x ** 2, x=x); xx2 = integrate.simpson(phi(2) ** 2 * x ** 2, x=x)
x12 = integrate.simpson(phi(1) * x * phi(2), x=x)
dist = xx1 + xx2 - 2 * x1 * x2
P(f"<x>_1 = {x1:.4f}, <x>_2 = {x2:.4f}; <x^2>_1 = {xx1:.4f}, <x^2>_2 = {xx2:.4f}; <1|x|2> = {x12:.5f} (-16/(9 pi^2) = {-16 / (9 * pi ** 2):.5f})")
P(f"distinguishable: {dist:.4f} ; bosons (symmetric): {dist - 2 * x12 ** 2:.4f} ; fermions (antisymmetric): {dist + 2 * x12 ** 2:.4f} ; ratio F/B = {(dist + 2 * x12 ** 2) / (dist - 2 * x12 ** 2):.2f}")

sec("ideal quantum gas: P/(n k T) = f_{5/2}(z)/f_{3/2}(z), n lambda^3 / g = f_{3/2}(z)")
def f(nu, z, sign):          # sign=+1 FD, -1 BE ; f_nu(z) = (1/Gamma(nu)) int x^{nu-1}/(z^-1 e^x + sign) dx
    val = integrate.quad(lambda t: t ** (nu - 1) / (np.exp(t) / z + sign), 0, 80 if True else 0, limit=400)[0]
    return val / special.gamma(nu)
def series(nu, z, sign, terms=200):
    k = np.arange(1, terms + 1)
    return ((-sign) ** (k + 1) * z ** k / k ** nu).sum() if False else sum(((-1) ** (kk + 1) if sign == 1 else 1) * z ** kk / kk ** nu for kk in range(1, terms + 1))
for z in (0.01, 0.05, 0.1, 0.3, 0.6):
    for sign, name in ((1, "FD"), (-1, "BE")):
        n3 = f(1.5, z, sign); p5 = f(2.5, z, sign)
        P(f"z = {z:5.2f} {name}: n lambda^3/g = {n3:.5f}, P/(nkT) = {p5 / n3:.5f}, first-order estimate 1 {'+' if sign == 1 else '-'} n lambda^3/(g 2^(5/2)) = {1 + sign * n3 / 2 ** 2.5:.5f}")
P("2^{5/2} =", 2 ** 2.5, "; 1/2^{5/2} =", 2 ** -2.5, "; zeta(3/2) =", special.zeta(1.5))
nl3_He4 = 0.1349
nl3_He3 = nl3_He4 * (4.002602 / 3.0160293) ** 1.5
P(f"He-4 gas at 4.2 K, 1 atm: n lambda^3 = {nl3_He4} -> boson correction -n lambda^3/2^(5/2) = {-nl3_He4 / 2 ** 2.5:.4f} ; He-3 (lighter, g=2): n lambda^3 = {nl3_He3:.4f} -> +n lambda^3/(g 2^(5/2)) = {nl3_He3 / 2 / 2 ** 2.5:+.4f}")
P("exchange count correction: bosons/classical ~ 1 + N(N-1)/(2g): N=10, g=1000:", 1 + 45 / 1000, " (exact 1.0459); fermions ~ 1 - N(N-1)/(2g):", 1 - 45 / 1000, " (exact 0.9559)")

sec("Wigner-Kirkwood first quantum correction check with the oscillator")
for x in (0.1, 0.5, 1.0, 2.0):
    P(f"x = hbar omega/kT = {x}: z_q/z_c = {x / 2 / np.sinh(x / 2):.5f} ; 1 - x^2/24 = {1 - x ** 2 / 24:.5f}")
P("general: Z = Z_cl [1 - (beta^2 hbar^2 / 24 m) sum_i <(grad_i V)^2> + ...] ; oscillator: <(V')^2> = m w^2 kT -> -beta hbar^2 w^2/24 /kT*kT = -x^2/24")

sec("practice")
P("P3: bosons/fermions in 2 levels N=2: Z_2(bosons)=e0^2+e0 e1+e1^2 : at b: ", sum(np.exp(-b * np.array(c)).prod() for c in [(0, 0), (0, 1), (1, 1)]), " fermions: ", np.exp(-b * 0) * np.exp(-b * 1))
P("P5 degeneracy parameter at which g(r)-1 at r=lambda/2: ", exp(-2 * pi * 0.25))

sec("when is statistics quantum: lambda and n lambda^3 table (chapter section 1)")
mHe4, mHe3 = 4.002602 * u, 3.0160293 * u
def row(name, m, T, n, g=1):
    l = lam(m, T); P(f"{name}: lambda = {l * 1e9:.4f} nm, n = {n:.4g} m^-3, n lambda^3 = {n * l ** 3:.4g}, spacing/lambda = {n ** (-1 / 3) / l:.4g}")
row("N2 300 K 1 atm", 28.0134 * u, 300, atm / (kB * 300))
row("He 300 K 1 atm", mHe4, 300, atm / (kB * 300))
row("He 4.2 K 1 atm (ideal gas)", mHe4, 4.2, atm / (kB * 4.2))
row("liquid He-4 2.17 K (rho = 145 kg/m3, recalled)", mHe4, 2.17, 145.0 / mHe4)
row("Cu electrons 300 K (n = 8.5e28 recalled, m = m_e)", me, 300, 8.5e28)
P("Cu: n lambda^3 / g_s =", 8.5e28 * lam(me, 300) ** 3 / 2, "; exchange factor at d = 0.053 lambda: 1 - 2 pi d^2 =", 1 - 2 * pi * 0.0529 ** 2)

sec("practice 9 (infinite geometric series) and practice 1")
b = 0.7
z1b = 1 / (1 - exp(-b)); z12b = 1 / (1 - exp(-2 * b))
P(f"Z1(b)={z1b:.4f}, Z1(2b)={z12b:.4f}, Z1^2={z1b ** 2:.4f}: bosons {(z1b ** 2 + z12b) / 2:.4f}, fermions {(z1b ** 2 - z12b) / 2:.4f}")
x_ = np.arctanh(sqrt(0.1)); P(f"purity 0.55: r={sqrt(0.1):.4f}, x={x_:.4f}, T={0.6717 / x_:.3f} K (mu_B B/kB = {muB / kB:.4f} K/T)")
P("oscillator: exact x/2/sinh(x/2) at 1, 2:", 0.5 / np.sinh(0.5), 1 / np.sinh(1.0))
