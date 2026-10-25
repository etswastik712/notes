"""Eco-evo problem bank: every answer quoted in `02-Eco-Evo/Eco-Evo Problem Bank.md` is computed here.

    .venv/bin/python -W ignore scripts/ee_problem_bank.py
Sections A-G follow the page (A structured populations, B dynamics, C competition, D predation, E lakes, F conservation, G mixed).
"""
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import solve_ivp

np.set_printoptions(precision=4, suppress=True)
P = lambda *a: print(*a)


def sec(t):
    P("\n" + "=" * 8, t)


# ---------------------------------------------------------------- A
sec("A1 life table")
x = np.arange(4); n = np.array([1000, 600, 300, 100]); m = np.array([0, 1.5, 2.0, 1.0])
l = n / n[0]; R0 = (l * m).sum(); G = (x * l * m).sum() / R0
r_ap = np.log(R0) / G
r_ex = brentq(lambda r: (l * m * np.exp(-r * x)).sum() - 1, -1, 3)
P("l_x", l, "R0", R0, "G", round(G, 4), "r~lnR0/G", round(r_ap, 4), "r exact", round(r_ex, 4), "lambda", round(np.exp(r_ex), 4))
P("q_x (per-class mortality)", np.round(1 - n[1:] / n[:-1], 3))

sec("A2 Leslie")
L = np.array([[0, 1.5, 1.0], [0.6, 0, 0], [0, 0.5, 0]])
ev, V = np.linalg.eig(L); i = ev.real.argmax(); lam = ev[i].real
w = V[:, i].real; w /= w.sum()
evT, VT = np.linalg.eig(L.T); j = evT.real.argmax(); v = VT[:, j].real; v /= v[0]
P("lambda", round(lam, 4), "SAD", np.round(w, 4), "reproductive value (v0=1)", np.round(v, 4))
R0b = 1.5 * 0.6 + 1.0 * 0.6 * 0.5
P("R0 = F1 s0 + F2 s0 s1 =", R0b, "; lambda>1 iff R0>1")
nt = np.array([100.0, 0, 0])
for t in range(1, 7):
    nt = L @ nt
    P("t", t, np.round(nt, 1), "total", round(nt.sum(), 1))
P("char. poly lambda^3 - 0.9 lambda - 0.3 at lambda: ", round(lam ** 3 - 0.9 * lam - 0.3, 8))
# harvest 30% of age-0 each step
L2 = L.copy(); L2[1, 0] = 0.6 * 0.7
P("if 30% of newborn-class survivors are removed (s0 0.6->0.42): lambda =", round(max(np.linalg.eigvals(L2).real), 4))

sec("A3 stage matrix")
A = np.array([[0.30, 0.0, 2.0], [0.20, 0.50, 0.0], [0.0, 0.20, 0.70]])
ev, V = np.linalg.eig(A); i = ev.real.argmax(); lam = ev[i].real
w = V[:, i].real; w /= w.sum()
evT, VT = np.linalg.eig(A.T); v = VT[:, evT.real.argmax()].real
S = np.outer(v, w) / (v @ w)
E = A / lam * S
P("lambda", round(lam, 4), "w", np.round(w, 4), "v", np.round(v / v[0], 4))
P("sensitivity\n", np.round(S, 3)); P("elasticity (nonzero entries)\n", np.round(E, 3), "sum", round(E.sum(), 4))
P("stage-sums of elasticity (columns = what stage i does):", np.round(E.sum(0), 3))
names = {(0, 0): "P1 (juv stay)", (1, 0): "G1 (juv->sub)", (1, 1): "P2 (sub stay)", (2, 1): "G2 (sub->adult)", (2, 2): "P3 (adult stay)", (0, 2): "F3 (fecundity)"}
for (i1, j1), nm in names.items():
    def lam_with(d):
        B = A.copy(); B[i1, j1] += d; return max(np.linalg.eigvals(B).real)
    d_need = brentq(lambda d: lam_with(d) - 1, 0, 5)
    P(f"  {nm}: A_ij={A[i1, j1]}, sensitivity {S[i1, j1]:.3f}, elasticity {E[i1, j1]:.3f}; absolute rise needed for lambda=1: +{d_need:.3f} (to {A[i1, j1] + d_need:.3f}){'  [impossible: survival > 1]' if A[i1, j1] + d_need > 1 and nm[0] in 'PG' else ''}")
    B = A.copy(); B[i1, j1] *= 1.10
    P(f"      +10% of it: dlam/lam = {(max(np.linalg.eigvals(B).real) / lam - 1) * 100:.2f}% (elasticity x 10% = {E[i1, j1] * 10:.2f}%)")
P("years to lose 90%:", round(np.log(0.1) / np.log(lam), 1), "; to halve:", round(np.log(0.5) / np.log(lam), 1))
# survival of adults 0.70 -> 0.75 and sub stay etc; egg protection analogue: raise F3 by 25%
B = A.copy(); B[0, 2] *= 1.25; P("fecundity +25% only: lambda =", round(max(np.linalg.eigvals(B).real), 4))
B = A.copy(); B[0, 2] *= 2.0; P("fecundity doubled: lambda =", round(max(np.linalg.eigvals(B).real), 4))
B = A.copy(); B[1, 0] += 0.1; B[2, 1] += 0.1; P("G1 and G2 each +0.1: lambda =", round(max(np.linalg.eigvals(B).real), 4))
B = A.copy(); B[2, 2] += 0.05; P("adult stay +0.05: lambda =", round(max(np.linalg.eigvals(B).real), 4))

sec("A4 growth rate")
r = 0.012
P("1.2%/yr: doubling", round(np.log(2) / r, 1), "yr; x after 50 yr", round(np.exp(r * 50), 3), "; lambda = e^r =", round(np.exp(r), 5))

# ---------------------------------------------------------------- B
sec("B1 logistic")
r, K, N0 = 0.4, 500.0, 20.0
P("t(K/2) = ln((K-N0)/N0)/r =", round(np.log((K - N0) / N0) / r, 3))
P("N(10) =", round(K / (1 + (K - N0) / N0 * np.exp(-r * 10)), 2), "; N(5) =", round(K / (1 + (K - N0) / N0 * np.exp(-r * 5)), 2))
P("max rate rK/4 =", r * K / 4, "at N=K/2 =", K / 2)
for H in (20, 40, 50, 55):
    disc = K * K / 4 - H * K / r
    P(f"  harvest H={H}: ", "equilibria", [round(K / 2 - np.sqrt(disc), 1), round(K / 2 + np.sqrt(disc), 1)] if disc >= 0 else "none (collapse)")
P("relaxation time 1/r =", 1 / r)
g = lambda N: N * np.exp(r * (1 - N / K))

sec("B2 Ricker, K=100")
def ricker_orbit(rr, K=100.0, N0=20.0, burn=2000, keep=600):
    N = N0
    for _ in range(burn): N = N * np.exp(rr * (1 - N / K))
    out = []
    for _ in range(keep):
        N = N * np.exp(rr * (1 - N / K)); out.append(N)
    return np.array(out)
def period(o, tol=1e-6):
    for p in (1, 2, 4, 8, 16, 32):
        if np.max(np.abs(o[p:] - o[:-p])) < tol * 100: return p
    return None
for rr in (0.8, 1.5, 2.2, 2.6, 2.8, 3.0):
    o = ricker_orbit(rr)
    p = period(o)
    P(f"  r={rr}: g'(K)=1-r={1 - rr:+.2f}  period={p}  values={np.round(np.unique(np.round(o[-(p or 8):], 2)), 2) if p else 'aperiodic'}  range {o.min():.1f}-{o.max():.1f}")
def lyap(rr, K=100.0, N0=20.0, n=20000):
    N = N0; s = 0
    for _ in range(500): N = N * np.exp(rr * (1 - N / K))
    for _ in range(n):
        s += np.log(abs(1 - rr * N / K)); N = N * np.exp(rr * (1 - N / K))
    return s / n
P("Lyapunov r=3.0:", round(lyap(3.0), 3), " r=2.8:", round(lyap(2.8), 3), " r=2.2:", round(lyap(2.2), 3))

sec("B3 Hassell")
fp = lambda lam_, b: 1 - b * (1 - lam_ ** (-1 / b))
for lam_ in (4, 20):
    P(f"  lambda={lam_}: f'(N*) for beta=1,2,6,50,1000:", [round(fp(lam_, b), 3) for b in (1, 2, 6, 50, 1000)], " limit beta->inf: 1-ln(lambda) =", round(1 - np.log(lam_), 3))
bc = brentq(lambda b: fp(20, b) + 1, 1.0001, 1000)
P("lambda=20: f'=-1 at beta_c =", round(bc, 3), "; lambda must exceed e^2 =", round(np.exp(2), 3), "for any beta to destabilise")
P("beta=1 (Beverton-Holt/Hassell): f' =", fp(20, 1), "never negative")

sec("B4 forecast horizon")
Lam = 0.39
P("horizon ln(range/delta0)/Lambda: range 100, delta0 0.01:", round(np.log(100 / 0.01) / Lam, 1), "; delta0 = 1e-4:", round(np.log(100 / 1e-4) / Lam, 1), "; gain from 100x precision:", round(np.log(100) / Lam, 1))

# ---------------------------------------------------------------- C
sec("C1 L-V competition")
def lv(K1, K2, a12, a21, r=0.5):
    d = 1 - a12 * a21
    n1, n2 = (K1 - a12 * K2) / d, (K2 - a21 * K1) / d
    s1 = K1 > K2 / a21 and K1 / a12 > K2
    s2 = K2 > K1 / a12 and K2 / a21 > K1
    co = K1 < K2 / a21 and K2 < K1 / a12
    pr = K1 > K2 / a21 and K2 > K1 / a12
    kind = "1 wins" if s1 else "2 wins" if s2 else "coexist" if co else "priority" if pr else "?"
    ev = None
    if n1 > 0 and n2 > 0:
        J = np.array([[-r * n1 / K1, -r * a12 * n1 / K1], [-r * a21 * n2 / K2, -r * n2 / K2]]); ev = np.round(np.linalg.eigvals(J), 4)
    P(f"  K1={K1} K2={K2} a12={a12} a21={a21}: product {a12 * a21:.2f}; thresholds a12<{K1 / K2:.3f}, a21<{K2 / K1:.3f}; interior ({n1:.1f},{n2:.1f}); {kind}; eig {ev}")
lv(200, 150, 0.6, 0.9); lv(200, 150, 0.6, 0.5); lv(200, 150, 1.6, 0.9); lv(200, 150, 1.0, 0.7)

sec("C2 R*")
m = 0.1
for nm, mu, k in (("A", 1.5, 8.0), ("B", 0.9, 1.0)):
    P(f"  {nm}: R*={m * k / (mu - m):.4f}  growth at R=20: {mu * 20 / (k + 20):.4f}; at R=1: {mu * 1 / (k + 1):.4f}")
P("  crossing R where growth equal:", round(brentq(lambda R: 1.5 * R / (8 + R) - 0.9 * R / (1 + R), 0.01, 100), 3))
P("  B alone at R_in=20 (yield 1): N*=", 20 - 0.125)

sec("C3 alpha from overlap")
for a in (0.5, 0.25, 0.1):
    P(f"  alpha={a}: d/sigma = {2 * np.sqrt(-np.log(a)):.3f}")
for ds in (0.5, 1, 1.5, 2, 3):
    P(f"  d/sigma={ds}: alpha={np.exp(-ds ** 2 / 4):.3f}")

# ---------------------------------------------------------------- D
sec("D1 L-V predator-prey")
r_, p_, a_, m_ = 0.8, 0.01, 0.4, 0.6
P("H*=m/(ap)=", m_ / (a_ * p_), "P*=r/p=", r_ / p_, "period small cycle 2pi/sqrt(rm)=", round(2 * np.pi / np.sqrt(r_ * m_), 3))
d = 0.2
P(f"pesticide delta={d} on both: H*=", (m_ + d) / (a_ * p_), "P*=", (r_ - d) / p_)
# doubling r
P("double r: H* unchanged", m_ / (a_ * p_), "P* =", 2 * r_ / p_)
sol = solve_ivp(lambda t, y: [r_ * y[0] - p_ * y[0] * y[1], a_ * p_ * y[0] * y[1] - m_ * y[1]], (0, 60), [100, 40], rtol=1e-10, atol=1e-10, dense_output=True)
tt = np.linspace(0, 60, 60001); Y = sol.sol(tt)
P("orbit from (100,40): H range", round(Y[0].min(), 1), round(Y[0].max(), 1), "P range", round(Y[1].min(), 1), round(Y[1].max(), 1))
V = lambda H, Pp: a_ * p_ * H - m_ * np.log(H) + p_ * Pp - r_ * np.log(Pp)
P("V conserved: V(0)=", round(V(100, 40), 5), " V(max t)=", round(V(Y[0][-1], Y[1][-1]), 5))

sec("D2 logistic prey")
K = 300.0
Hs = m_ / (a_ * p_); Ps = (r_ / p_) * (1 - Hs / K)
J = np.array([[-r_ * Hs / K, -p_ * Hs], [a_ * p_ * Ps, 0]])
ev = np.linalg.eigvals(J)
P("P*=", Ps, "J=", J.tolist(), "eig", np.round(ev, 4), "period", round(2 * np.pi / abs(ev[0].imag), 2), "e-fold time", round(1 / abs(ev[0].real), 2))
P("needs K > m/(ap) =", Hs)

sec("D3 Holling II")
a, h = 0.05, 0.2
for N in (2, 10, 40, 100, 400):
    f = a * N / (1 + a * h * N)
    P(f"  N={N}: eaten per predator per day {f:.4f}; fraction of the prey density {f / N:.4f}")
P("  max 1/h =", 1 / h, "; half-saturation 1/(ah) =", 1 / (a * h))
P("  type I (linear aN) at N=100:", a * 100, "vs type II", round(a * 100 / (1 + a * h * 100), 3))

sec("D4 Levins")
c, e = 0.5, 0.2
P("p* = 1-e/c =", 1 - e / c)
for e2 in (0.2, 0.3, 0.4, 0.5):
    P(f"  e={e2}: p*={max(0, 1 - e2 / c):.3f}")
for D in (0.2, 0.4, 0.6):
    P(f"  destroyed fraction D={D}: p*={max(0, 1 - D - e / c):.3f}")
P("  threshold D=1-e/c =", 1 - e / c)

# ---------------------------------------------------------------- E
sec("E1 Vollenweider")
PL = lambda Pin, tau: 1.55 * (Pin / (1 + np.sqrt(tau))) ** 0.82
cls = lambda p: "ultra-oligo" if p < 5 else "oligo" if p < 10 else "meso" if p < 30 else "eu" if p < 100 else "hyper"
for tau in (0.5, 4, 25):
    for Pin in (60, 30):
        P(f"  tau_w={tau} yr, P_in={Pin}: P_L={PL(Pin, tau):.2f} ({cls(PL(Pin, tau))})")
P("  halving P_in multiplies P_L by 0.5^0.82 =", round(0.5 ** 0.82, 4))
P("  P_in needed for P_L=10 at tau=4:", round(((10 / 1.55) ** (1 / 0.82)) * (1 + np.sqrt(4)), 2), "; at tau=0.5:", round(((10 / 1.55) ** (1 / 0.82)) * (1 + np.sqrt(0.5)), 2))

sec("E2 Box 1 model")
b, r, h, p = 1.0, 1.4, 1.0, 8
f = lambda x: x ** p / (x ** p + h ** p)
fpx = lambda x: p * x ** (p - 1) * h ** p / (x ** p + h ** p) ** 2
xs = np.linspace(0.001, 4, 400000)
roots = xs[np.where(np.diff(np.sign(b - r * fpx(xs))))[0]]
a_of = lambda x: b * x - r * f(x)
alo, ahi = sorted([a_of(roots[0]), a_of(roots[1])])
P("folds x", np.round(roots, 4), "a window", round(alo, 4), round(ahi, 4), "cut needed ", round(100 * (1 - alo / ahi), 1), "%")
def equilibria(a):
    g = lambda x: a - b * x + r * f(x)
    xx = np.linspace(0, 4, 40001); s = np.sign(g(xx)); idx = np.where(np.diff(s) != 0)[0]
    return [round(float(brentq(g, xx[i], xx[i + 1])), 3) for i in idx]
for a_ in (0.03, 0.05, 0.2, 0.35, 0.5, 0.63, 0.7, 0.9):
    P(f"  a={a_}: equilibria {equilibria(a_)}")
def settle(a, x0):
    s = solve_ivp(lambda t, x: a - b * x + r * f(x), (0, 600), [x0], rtol=1e-10); return round(float(s.y[0][-1]), 3)
P("  a=0.5 start clear x=0.5 ->", settle(0.5, 0.5), " ; start turbid x=2 ->", settle(0.5, 2.0))
P("  raise a to 0.7 from clear:", settle(0.7, equilibria(0.5)[0]), "; then back to 0.5:", settle(0.5, settle(0.7, equilibria(0.5)[0])), "; back to 0.2:", settle(0.2, settle(0.7, equilibria(0.5)[0])), "; back to 0.03:", settle(0.03, settle(0.7, equilibria(0.5)[0])))
eq35 = equilibria(0.35)
P("  a=0.35 equilibria", eq35, "-> unstable middle =", eq35[1], ": biomanipulation must push x below it (a drop of", round(100 * (1 - eq35[1] / eq35[2]), 1), "% of turbid x)")
P("  settle a=0.35 from x=eq_mid-0.05 ->", settle(0.35, eq35[1] - 0.05), " from eq_mid+0.05 ->", settle(0.35, eq35[1] + 0.05))

# ---------------------------------------------------------------- F
sec("F1 extinction of founders")
bb, dd = 1.2, 1.0
for n0 in (1, 2, 5, 10, 25, 26, 30):
    P(f"  N0={n0}: P_ext={(dd / bb) ** n0:.4f}")
P("  founders for P_ext<1%:", np.log(0.01) / np.log(dd / bb), "-> ", int(np.ceil(np.log(0.01) / np.log(dd / bb))), "; for <5%:", int(np.ceil(np.log(0.05) / np.log(dd / bb))))
for bb_ in (1.05, 1.1, 1.5, 2.0):
    P(f"  b={bb_}: founders for <1%: {int(np.ceil(np.log(0.01) / np.log(1 / bb_)))}")

sec("F2 Allee + harvest")
r, A, K = 0.5, 20.0, 100.0
f = lambda N: r * N * (N / A - 1) * (1 - N / K)
Nm = ((A + K) + np.sqrt((A + K) ** 2 - 3 * A * K)) / 3
P("max sustainable harvest = max f =", round(f(Nm), 3), "at N=", round(Nm, 2))
for H in (10, 20, 30, 35):
    g = lambda N: f(N) - H
    NN = np.linspace(1, 100, 100001); s = np.sign(g(NN)); idx = np.where(np.diff(s) != 0)[0]
    P(f"  H={H}: equilibria {[round(float(brentq(g, NN[i], NN[i + 1])), 2) for i in idx]}")
P("  growth rate of 10 individuals:", round(f(10), 3), "(negative; per capita", round(f(10) / 10, 3), ")")

sec("F3 mark-recapture")
for M, n, mm in ((80, 60, 12), (80, 60, 4)):
    LP = M * n / mm; ch = (M + 1) * (n + 1) / (mm + 1) - 1
    var = (M + 1) * (n + 1) * (M - mm) * (n - mm) / ((mm + 1) ** 2 * (mm + 2))
    P(f"  M={M} n={n} m={mm}: LP={LP:.1f} Chapman={ch:.1f} SE={np.sqrt(var):.1f} CI95 {ch - 1.96 * np.sqrt(var):.0f}-{ch + 1.96 * np.sqrt(var):.0f}")

sec("F4 camera traps")
for pp, k, C in ((0.15, 8, 44), (0.05, 8, 44), (0.15, 30, 44)):
    ps = 1 - (1 - pp) ** k; P(f"  p={pp} per occasion, K={k}: p*={ps:.4f}; C={C} -> N_hat={C / ps:.1f}")

sec("F5 drift and Ne")
Nm_, Nf_ = 5, 45
Ne = 4 * Nm_ * Nf_ / (Nm_ + Nf_)
P("Ne =", Ne, "census", Nm_ + Nf_, "; H after 20 gen:", round((1 - 1 / (2 * Ne)) ** 20, 4), "; census-based:", round((1 - 1 / (2 * (Nm_ + Nf_))) ** 20, 4), "; half-life gens", round(np.log(2) / -np.log(1 - 1 / (2 * Ne)), 1))
P("Ne for 25 M + 25 F:", 4 * 25 * 25 / 50, "; for 1 M + 49 F:", round(4 * 49 / 50, 2))

sec("F6 tigers")
P("2011->2018 growth", round(np.log(2967 / 1706) / 7, 4), "doubling", round(np.log(2) / (np.log(2967 / 1706) / 7), 1), "yr;  2008->2018 growth", round(np.log(2967 / 1411) / 10, 4), "per yr")
P("2018 CI relative half-width +/-", round(100 * (3346 - 2603) / 2 / 2967, 1), "% ; 2011 vs CI lower bound 2603: increase at least x", round(2603 / 1706, 2))

# ---------------------------------------------------------------- G
sec("G1 lake decision (Box 1 numbers above)")
sec("G2 harvesting a chaotic Ricker population")
rr = 2.8
hc = 1 - np.exp(2 - rr)
P("threshold harvest fraction h > 1 - e^(2-r) =", round(hc, 4))
for hh in (0.0, 0.3, 0.5, 0.55, 0.6, 0.7):
    Nstar = 100 * (1 + np.log(1 - hh) / rr); gp = 1 - rr * Nstar / 100
    N = 30.0
    for _ in range(3000): N = (1 - hh) * N * np.exp(rr * (1 - N / 100))
    orb = []
    for _ in range(40):
        N = (1 - hh) * N * np.exp(rr * (1 - N / 100)); orb.append(N)
    yld = hh * np.mean([o / (1 - hh) for o in orb])
    P(f"  h={hh}: N*={Nstar:.1f}, g'={gp:+.3f}, orbit tail={np.round(orb[-4:], 1)}, mean catch ~ {hh * np.mean([o / (1 - hh) for o in orb]):.1f}")
P("equilibrium catch h N*/(1-h) at h=0.7:", round(0.7 * 100 * (1 + np.log(0.3) / rr) / 0.3, 1))
