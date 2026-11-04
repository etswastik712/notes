"""TH09: microstates, macrostates, multiplicity - every number in the chapter recomputed.
    .venv/bin/python -W ignore scripts/th09_numbers.py
"""
import itertools
import numpy as np
from math import comb, lgamma, log, exp, sqrt, pi, factorial
from scipy import stats, optimize

kB = 1.380649e-23; NA = 6.02214076e23; R = 8.314462618
P = print
def sec(t): P("\n#####", t)
def lnC(n, k): return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)

sec("dice and coins: microstates against macrostates")
P("two dice: 36 microstates, 11 macrostates (sums); multiplicity of sum s:", [6 - abs(s - 7) for s in range(2, 13)], "; P(7) = 1/6, P(2) = 1/36")
P("four coins: Omega(k heads) =", [comb(4, k) for k in range(5)], "; N=10:", [comb(10, k) for k in range(11)])
for N in (10, 100, 1000, 10000):
    sd = sqrt(N) / 2
    k = np.arange(N + 1); p = stats.binom.pmf(k, N, 0.5)
    P(f"N={N}: sigma_k = {sd:.2f}, fractional width 1/sqrt(N) = {1 / sqrt(N):.4f}; P(k=N/2) = {stats.binom.pmf(N // 2, N, 0.5):.5f}; "
      f"P(|k/N-1/2|<=0.01) = {stats.binom.cdf(int(0.51 * N), N, 0.5) - stats.binom.cdf(int(np.ceil(0.49 * N)) - 1, N, 0.5):.5f}; P(|k/N-1/2|<=0.05) = {stats.binom.cdf(int(0.55 * N), N, 0.5) - stats.binom.cdf(int(np.ceil(0.45 * N)) - 1, N, 0.5):.5f}")
P(f"N=100: Omega(50) = {comb(100, 50):.4e}, 2^100 = {2 ** 100:.4e}, ratio = {comb(100, 50) / 2 ** 100:.5f}; P(k>=60) = {stats.binom.sf(59, 100, 0.5):.5f}; P(k=100) = {2.0 ** -100:.3e}")
for N in (100, 300, 1000):
    P(f"all N={N} in the left half: 2^-N = 10^{-N * log(2) / log(10):.2f}")
P("N = 1 mol: 2^-N = 10^(-1.81e23); free expansion S = N k ln2 =", R * log(2), "J/K")
d = 1e-9; P(f"1 mol, probability that the left half holds more than (1/2+{d}) N: ~ exp(-2 N d^2) = exp(-{2 * NA * d * d:.3e})")

sec("two Einstein solids: the standard small table (N_A = N_B = 3, q = 6)")
NA_, NB_, q = 3, 3, 6
rows = [(qa, comb(qa + NA_ - 1, qa), comb(q - qa + NB_ - 1, q - qa)) for qa in range(q + 1)]
tot = sum(a * b for _, a, b in rows)
for qa, a, b in rows: P(f"q_A={qa}: Omega_A={a:3d} Omega_B={b:3d} product={a * b:4d} prob={a * b / tot:.4f}")
P("total =", tot, " = C(q+N_tot-1, q) =", comb(q + NA_ + NB_ - 1, q))

sec("two Einstein solids: N_A=300, N_B=200, q=100")
NA_, NB_, q = 300, 200, 100
lnOm = np.array([lnC(qa + NA_ - 1, qa) + lnC(q - qa + NB_ - 1, q - qa) for qa in range(q + 1)])
lnTot = lnC(q + NA_ + NB_ - 1, q)
p = np.exp(lnOm - lnTot)
qa = np.arange(q + 1); mean = (p * qa).sum(); sd = sqrt((p * qa ** 2).sum() - mean ** 2)
P(f"peak q_A = {qa[p.argmax()]} (q N_A/N = {q * NA_ / (NA_ + NB_)}), P(peak) = {p.max():.4f}, <q_A> = {mean:.3f}, sigma = {sd:.3f}, ln Omega_tot = {lnTot:.3f}, ln Omega(peak) = {lnOm.max():.3f}")
P(f"P(q_A=100) = {p[100]:.3e} ; P(q_A=0) = {p[0]:.3e} ; P(q_A = 80) = {p[80]:.3e}; P(|q_A-60|<=5) = {p[55:66].sum():.4f}; P(|q_A-60|<=10) = {p[50:71].sum():.4f}")
P(f"S/k at peak = {lnOm.max():.3f}; S/k at q_A=100 = {lnOm[100]:.3f}; S/k at q_A=80 = {lnOm[80]:.3f}")
TA = lambda qq: 1 / log(1 + NA_ / qq); TB = lambda qq: 1 / log(1 + NB_ / qq)
P(f"q_A=80: kT_A/eps = {TA(80):.4f}, kT_B/eps = {TB(20):.4f}; dS per quantum A->B = (1/T_B-1/T_A) = {1 / TB(20) - 1 / TA(80):.4f} k ; exact ln Om(79)-ln Om(80) = {lnOm[79] - lnOm[80]:.4f}")
P(f"q_A=60: kT_A = {TA(60):.4f}, kT_B = {TB(40):.4f}")
for Nn in (10, 100, 1000, 10000):
    qq = 2 * Nn
    l = np.array([lnC(a + Nn - 1, a) + lnC(qq - a + Nn - 1, qq - a) for a in range(qq + 1)]); pp = np.exp(l - lnC(qq + 2 * Nn - 1, qq)); a = np.arange(qq + 1)
    m = (pp * a).sum(); s = sqrt((pp * a ** 2).sum() - m ** 2)
    P(f"N_A=N_B={Nn}, q=2N: <q_A>={m:.2f}, sigma={s:.3f}, sigma/mean={s / m:.4f}, sqrt-law: 1/sqrt(N)={1 / sqrt(Nn):.4f}")

sec("large Einstein solid: S(U), T(U), C")
for r in (0.1, 0.5, 1.0, 2.0, 5.0):
    x = log(1 + 1 / r)
    P(f"q/N = {r}: kT/eps = {1 / x:.4f}; C/(N k) = x^2 e^x/(e^x-1)^2 = {x ** 2 * exp(x) / (exp(x) - 1) ** 2:.4f}; S/(Nk) = (1+r) ln(1+r) - r ln r = {(1 + r) * log(1 + r) - r * log(r):.4f}")
P("high-T: S/(Nk) -> ln(e q/N) + ...; q/N=5:", log(np.e * 5))

sec("ideal gas macrostates: number of particles in the left half")
for N in (100, 1000, 10000):
    P(f"N={N}: P(|n_L/N-1/2|<=0.01) = {stats.binom.cdf(int(0.51 * N), N, 0.5) - stats.binom.cdf(int(np.ceil(0.49 * N)) - 1, N, 0.5):.5f}")
P(f"N=100: P(45<=n_L<=55) = {stats.binom.cdf(55, 100, 0.5) - stats.binom.cdf(44, 100, 0.5):.5f}")
P("ideal gas Omega ~ V^N U^(3N/2): dS = N k ln(V2/V1) + (3/2) N k ln(U2/U1); 1 mol: doubling V gives", R * log(2), "J/K ; doubling T at constant V gives", 1.5 * R * log(2), "J/K")

sec("simulation: random exchange of quanta between solids A (300) and B (200), q = 100, all quanta initially in A")
rng = np.random.default_rng(20261104)
NA_, NB_, q = 300, 200, 100
N = NA_ + NB_
osc = np.zeros(N, dtype=int)
for _ in range(q): osc[rng.integers(0, NA_)] += 1           # all quanta start in A
steps = 600000
qA = np.empty(steps + 1, dtype=int); qA[0] = osc[:NA_].sum()
hist = np.zeros(q + 1); occ = np.zeros(60); samples = 0
# symmetric proposal: pick two oscillators i, j uniformly; if i holds a quantum move it to j.  The proposal (i->j) and its reverse
# (j->i) have the same probability 1/N^2, so every microstate is equally likely in the stationary state (detailed balance).
ii = rng.integers(0, N, size=steps); jj = rng.integers(0, N, size=steps)
cur = int(qA[0])
for t in range(1, steps + 1):
    a, b = ii[t - 1], jj[t - 1]
    if osc[a] > 0 and a != b:
        osc[a] -= 1; osc[b] += 1
        cur += (1 if b < NA_ else 0) - (1 if a < NA_ else 0)
    qA[t] = cur
    if t > 40000 and t % 20 == 0:
        hist[cur] += 1; samples += 1
        np.add.at(occ, np.minimum(osc, 59), 1)
lnOm = lambda a: lnC(a + NA_ - 1, a) + lnC(q - a + NB_ - 1, q - a)
P(f"initial q_A = {qA[0]}; q_A at steps 10, 100, 1000, 10000, 100000: {[int(qA[k]) for k in (10, 100, 1000, 10000, 100000)]}")
P(f"time average of q_A after step 40000: {qA[40000:].mean():.3f} (exact 60) ; std = {qA[40000:].std():.3f} (exact {sd:.3f})")
P(f"S/k at start: {lnOm(qA[0]):.2f}, at step 1000: {lnOm(int(qA[1000])):.2f}, mean over the run {np.mean([lnOm(a) for a in qA[40000::200]]):.3f}")
hist /= samples
Pexact = np.exp(np.array([lnOm(a) for a in range(q + 1)]) - lnC(q + N - 1, q))
P(f"max |histogram - exact| = {np.abs(hist - Pexact).max():.4f} over {samples} samples (exact peak {Pexact.max():.4f})")
occ /= occ.sum()
x = q / (q + N); geo = (1 - (q / N) / (1 + q / N)) * ((q / N) / (1 + q / N)) ** np.arange(8)
P("single-oscillator occupation P(n=0..7): sim", occ[:8].round(4), " geometric with <n>=0.2:", geo.round(4))
P("(the exact weight: P(n) = C(q-n+N-2, q-n)/C(q+N-1, q); n=0..3:", [round(comb(q - n + N - 2, q - n) / comb(q + N - 1, q), 4) for n in range(4)], ")")

sec("most probable distribution: N particles over levels eps = 0..4 with total energy E = N")
def occupancies(N, E, L=5):
    out = []
    def rec(i, n_left, e_left, cur):
        if i == L - 1:
            if e_left == (L - 1) * n_left: out.append(cur + [n_left]) if False else None
            return
    for n4 in range(0, N + 1):
        for n3 in range(0, N + 1 - n4):
            for n2 in range(0, N + 1 - n4 - n3):
                for n1 in range(0, N + 1 - n4 - n3 - n2):
                    n0 = N - n1 - n2 - n3 - n4
                    if n1 + 2 * n2 + 3 * n3 + 4 * n4 == E: out.append((n0, n1, n2, n3, n4))
    return out
def boltz_frac(mean_e, L=5):
    eps = np.arange(L); f = lambda b: (eps * np.exp(-b * eps)).sum() / np.exp(-b * eps).sum() - mean_e
    b = optimize.brentq(f, 1e-6, 20); w = np.exp(-b * eps); return b, w / w.sum()
b, fb = boltz_frac(1.0)
P(f"Boltzmann for <eps>=1 on 5 levels: beta = {b:.4f} ; fractions = {fb.round(4)}")
for N in (10, 30, 60, 120):
    occ_list = occupancies(N, N)
    lnW = np.array([lgamma(N + 1) - sum(lgamma(n + 1) for n in v) for v in occ_list])
    W = np.exp(lnW - lnW.max()); w = W / W.sum()
    mean = (w[:, None] * np.array(occ_list)).sum(0) / N
    peak = np.array(occ_list[int(lnW.argmax())]) / N
    P(f"N={N}: {len(occ_list)} occupancy vectors; microstates {np.exp(lnW.max()) * W.sum():.3e}; most probable {peak.round(3)}; mean {mean.round(4)}; max|mean-Boltzmann| = {np.abs(mean - fb).max():.4f}; ln W_max = {lnW.max():.2f}")

sec("Fermi and Bose counting from the same postulate: 6 levels (eps = 0..5), degeneracy g each")
def counts(Nn, E, g, kind, L=6):
    tot = 0.0; avg = np.zeros(L)
    def rec(i, n_left, e_left, cur, lnw):
        nonlocal tot, avg
        if i == L - 1:
            n = n_left
            if n * i != e_left: return
            if kind == "F" and n > g: return
            l = lnw + (lnC(g, n) if kind == "F" else lnC(n + g - 1, n))
            w = exp(l - 30.0); tot += w; avg += w * np.array(cur + [n]); return
        for n in range(0, min(n_left, e_left // max(i, 1) if i > 0 else n_left) + 1):
            if kind == "F" and n > g: break
            l = lnC(g, n) if kind == "F" else lnC(n + g - 1, n)
            rec(i + 1, n_left - n, e_left - i * n, cur + [n], lnw + l)
    rec(0, Nn, E, [], 0.0)
    return avg / tot
for Nn, E, g in ((16, 24, 8), (32, 48, 16), (64, 96, 32)):
  for kind, name in (("F", "Fermi"), ("B", "Bose")):
      avg = counts(Nn, E, g, kind)
      f = avg / g
      eps = np.arange(6)
      sgn = 1 if kind == "F" else -1
      def eqs(v):
          a, bt = v; occ = 1 / (np.exp(a + bt * eps) + sgn); return [g * occ.sum() - Nn, g * (eps * occ).sum() - E]
      a, bt = optimize.least_squares(eqs, [0.3 if kind == 'B' else -1.0, 0.4], bounds=([0.01, 0.0] if kind == 'B' else [-50, 0.0], [20, 5] if kind == 'B' else [50, 5])).x
      th = 1 / (np.exp(a + bt * eps) + sgn)
      P(f"{name}: N={Nn}, E={E}, g={g}: <n_i>/g exact enumeration = {f.round(4)} ; 1/(e^(a+b eps) {'+' if sgn == 1 else '-'} 1) with a={a:.3f}, b={bt:.3f}: {th.round(4)} ; max diff = {np.abs(f - th).max():.4f}")
