"""PR (probability, MT2113) - numbers quoted in chapters PR01-PR06, recomputed (exact where possible, Monte Carlo as a check).

    .venv/bin/python -W ignore scripts/pr_numbers.py
"""
import itertools
import math
from fractions import Fraction as Fr

import numpy as np
from scipy import stats, integrate, special

rng = np.random.default_rng(2113)
C = math.comb
P = print


def sec(t): P("\n=====", t)


sec("PR01 counting")
P("antennas n=10, m=3 defective, none adjacent: C(n-m+1,m) =", C(8, 3), "of", C(10, 3), "->", C(8, 3) / C(10, 3))
P("stars and bars n=10 balls, k=4 boxes: any:", C(13, 3), " at least one each:", C(9, 3))
P("12 people into 2,5,5:", math.factorial(12) // (2 * 120 * 120) // 2, " ; into 4,4,4:", math.factorial(12) // 24 ** 3 // 6)
P("full house:", 13 * C(4, 3) * 12 * C(4, 2), "/", C(52, 5), "=", 13 * C(4, 3) * 12 * C(4, 2) / C(52, 5), " straight flush (incl. royal):", 40, "/", C(52, 5), "=", 40 / C(52, 5))
P("10 time slots, 3 courses: P(>=2 same) =", 1 - 10 * 9 * 8 / 1000)
P("Gimli & Legolas, row of 12:", 22 * math.factorial(10) / math.factorial(12), " circle:", 2 / 11)
for n in (3, 4, 5, 10):
    d = sum((-1) ** i / math.factorial(i) for i in range(n + 1))
    P(f"  derangement probability n={n}: {d:.6f}  (at least one match {1 - d:.6f}); 1/e = {1 / math.e:.6f}")
P("elevator: 3 people, floors 2-10, three consecutive distinct floors:", 7 * 6, "/", 9 ** 3, "=", 42 / 729)
P("3 eldest of 3 boys+3 girls are girls:", 1 / C(6, 3))
P("North+South have 8 spades -> East has 3:", C(5, 3) * C(21, 10) / C(26, 13))
num = math.factorial(4) * math.factorial(48) // (math.factorial(12) ** 4)
den = math.factorial(52) // (math.factorial(13) ** 4)
P("four piles each with exactly one ace:", num / den)
# Monte Carlo checks
N = 200000
d = np.array([rng.permutation(52) for _ in range(20000)])
aces = d < 4
piles = aces.reshape(20000, 4, 13).sum(2)
P("  MC four piles one ace each:", np.mean((piles == 1).all(1)))
P("inclusion-exclusion check n=3 events: P(A or B or C) with fair die A=even,B=div by 3,C=<=2:", len({2, 4, 6} | {3, 6} | {1, 2}) / 6)
P("continuity: P(E_n) for E_n=(0,1/n) under Uniform(0,1) tends to", 0)

sec("PR02 conditional probability")
def bayes(prior, like, fp):
    return like * prior / (like * prior + fp * (1 - prior))
P("disease (class): 95% sens, 1% false pos, 0.5% prevalence:", bayes(0.005, 0.95, 0.01))
P("disease (sheet): 95% / 95%, prevalence 1%:", bayes(0.01, 0.95, 0.05))
P("same test, prevalence 10%:", bayes(0.10, 0.95, 0.05), " 50%:", bayes(0.5, 0.95, 0.05))
P("smokers: P(smoker | lung cancer) =", 23 * 0.216 / (23 * 0.216 + 0.784))
P("coins: P(fair | HHH) =", Fr(1, 2) * Fr(1, 8) / (Fr(1, 2) * Fr(1, 8) + Fr(1, 2) * Fr(27, 64)), "=", float(Fr(8, 35)))
b1 = 0.2
P(f"plane: beta1={b1}: P(region1 | fail in 1) = {b1 / (b1 + 2):.4f} ; regions 2,3: {1 / (b1 + 2):.4f}")
p_, m_ = 0.6, 4
P("test: knew | correct, p=0.6, m=4:", p_ / (p_ + (1 - p_) / m_))
P("insurance: accident-prone | accident:", 0.4 * 0.3 / (0.4 * 0.3 + 0.2 * 0.7))
P("inspector: P(guilty | characteristic):", 0.6 / (0.6 + 0.4 * 0.2))
# Monty Hall MC
wins_switch = 0; M = 100000
for _ in range(M):
    car = rng.integers(3); pick = rng.integers(3)
    opts = [i for i in range(3) if i != pick and i != car]; opened = rng.choice(opts)
    sw = [i for i in range(3) if i != pick and i != opened][0]
    wins_switch += sw == car
P("Monty Hall MC switch:", wins_switch / M)
P("urn: b=5,w=3: P(B then W) =", 5 / 8 * 3 / 7, " P(W then B) =", 3 / 8 * 5 / 7)
P("urn: draw n=4 from b=5,w=3, k=2 black: P(first black | k) = k/n =", 2 / 4)
b, w, n, k = 5, 3, 4, 2
Pk = C(b, k) * C(w, n - k) / C(b + w, n); PBk = (b / (b + w)) * (C(b - 1, k - 1) * C(w, n - k) / C(b + w - 1, n - 1)); P("  via Bayes:", PBk / Pk)
P("independence: two coins, A=H1, B=H2, C=same: P(ABC)=", 1 / 4, "vs product", 1 / 8, " pairwise P(AC)=", 1 / 4, "=P(A)P(C)=", 1 / 2 * 1 / 2)
P("overbooking 110 booked, p=0.9, 100 seats: P(X<=100) =", stats.binom.cdf(100, 110, 0.9))
P("gambler's ruin (fair), start i=3 target 10: P(reach 10) =", 3 / 10)
r_ = 0.4 / 0.6
P("gambler's ruin p=0.6, i=3, n=10: P(bankrupt) =", (r_ ** 3 - r_ ** 10) / (1 - r_ ** 10), " P(win) =", (1 - r_ ** 3) / (1 - r_ ** 10))
P("  p=0.4 (unfavourable), i=3, n=10: P(bankrupt) =", ((1.5) ** 3 - (1.5) ** 10) / (1 - (1.5) ** 10))
P("marble: green added, green drawn -> other green:", Fr(1, 1) * Fr(2, 3), "=", 2 / 3)
P("5 before 7 with two dice: P(5)=4/36, P(7)=6/36 -> P(A)/(P(A)+P(B)) =", 4 / 10)
r, w = 1.0, 1.0
P("weighted urn 8 red, 4 white, both red; equal weights:", 8 / 12 * 7 / 11, "; r=2,w=1:", (16 / 20) * (14 / 18), " ; r=1,w=3:", (8 / 20) * (7 / 19))
P("dice: A=first die is a given face, B=second is that face, C=same: P(ABC)=1/36, product =", 1 / 216, "; pairs: P(AC)=1/36 = P(A)P(C) =", 1 / 6 * 1 / 6)
P("P(A and C) with A first die=6 given C 'same':", 1 / 6)
P("plane 3 regions equal prior, beta=(0.2,0.5,0.9): P(region1|fail1) =", 0.2 / (0.2 + 2), " region 2:", 1 / (0.2 + 2), " region 3:", 1 / (0.2 + 2))
P("two children: P(both boys | at least one boy) =", 1 / 3, " ; P(both boys | older is boy) =", 1 / 2)
# Monty Hall exact
P("Monty Hall: switch wins 2/3, stay 1/3; with n=100 doors, host opens 98: switch wins", 99 / 100)
P("independent trials: P(no 5, no 7 for n-1 trials, then 5): sum_n (1-10/36)^(n-1)*(4/36) =", (4 / 36) / (10 / 36))

sec("PR03 discrete distributions")
for nm, d in (("Bin(10,0.3)", stats.binom(10, 0.3)), ("Geom(0.25)", stats.geom(0.25)), ("Poisson(3.2)", stats.poisson(3.2)), ("NegBin: trials to 3rd success p=0.4", None)):
    if d is not None:
        P(f"  {nm}: mean {d.mean():.4f}, var {d.var():.4f}")
P("Poisson(3.2): P(X<=2) =", stats.poisson.cdf(2, 3.2), " ; Bin(100, 0.032):", stats.binom.cdf(2, 100, 0.032), " Bin(1000,0.0032):", stats.binom.cdf(2, 1000, 0.0032))
P("Poisson normalising c: p(i)=c lam^i/i! -> c = e^-lam ; lam=2: P(X=0) =", math.exp(-2), " P(X>2) =", 1 - stats.poisson.cdf(2, 2))
P("buses: E[X] = (36^2+40^2+44^2)/120 =", (36 ** 2 + 40 ** 2 + 44 ** 2) / 120, " vs plain average of bus sizes", (36 + 40 + 44) / 3)
P("hypergeometric w=10, b=15, n=5: pmf", np.round(stats.hypergeom(25, 10, 5).pmf(range(6)), 4), " mean", stats.hypergeom(25, 10, 5).mean(), "= n w/(w+b) =", 5 * 10 / 25)
P("  binomial(5, 0.4) pmf", np.round(stats.binom(5, 0.4).pmf(range(6)), 4))
P("slips: 5 of 100 drawn, X = # >= 80: with replacement Bin(5,0.21) P(X=0) =", 0.79 ** 5, "; without: ", C(80, 5) / C(100, 5))
P("two dice: P(sum=7, max=5) =", 2 / 36)
# max of 5 slips from 100 (prizes): P(X = x) = C(x-1,4)/C(100,5)
P("max of 5 of 100: E[X] =", 5 * 101 / 6)
P("fixed points distribution of random permutation: mean 1, var 1; MC n=10:")
fp = np.array([(rng.permutation(10) == np.arange(10)).sum() for _ in range(100000)]); P("  mean", fp.mean(), "var", fp.var(), " P(0)", (fp == 0).mean(), " Poisson(1):", math.exp(-1))
# coupons
for Nn in (6, 10, 50):
    H = sum(1 / i for i in range(1, Nn + 1)); P(f"  coupon collector N={Nn}: E[T] = N H_N = {Nn * H:.3f}")
Nn, nn = 10, 20
P(f"  expected number of distinct types after n={nn} draws, N={Nn}: N(1-(1-1/N)^n) = {Nn * (1 - (1 - 1 / Nn) ** nn):.4f}")
tt = []
for _ in range(20000):
    seen = set(); t = 0
    while len(seen) < 6: seen.add(rng.integers(6)); t += 1
    tt.append(t)
P("  MC coupon N=6: mean", np.mean(tt), " var", np.var(tt), " exact var:", sum((1 - i / 6) / (i / 6) ** 2 for i in range(6)) if False else sum((i / 6) / ((6 - i) / 6) ** 2 for i in range(6)))

sec("PR03 addenda (28 Aug sheet and class problems)")
P("20 balls, draw 3, win if some ball >= 17: 1 - C(16,3)/C(20,3) =", 1 - C(16, 3) / C(20, 3))
q_ = 1 - 0.3
P("coin until head or n=5 flips, p=0.3: pmf", [round(0.3 * q_ ** (k - 1), 4) for k in range(1, 5)], "+ P(X=5) =", q_ ** 4, " E[X] =", sum(k * 0.3 * q_ ** (k - 1) for k in range(1, 5)) + 5 * q_ ** 4, "=(1-q^5)/p =", (1 - q_ ** 5) / 0.3)
P("sheet 1: slips >=80 are 21 of 100; with replacement P(100 at least once) =", 1 - 0.99 ** 5, "; without:", 5 / 100)
P("  with replacement pmf of X ~ Bin(5, 0.21):", np.round(stats.binom(5, 0.21).pmf(range(6)), 4), " without Y ~ Hypergeom(100, 21, 5):", np.round(stats.hypergeom(100, 21, 5).pmf(range(6)), 4))
# sheet 2: 3 white, 3 red, 5 black, draw 3, winnings W - R
from collections import Counter
cnt = Counter()
balls = ["w"] * 3 + ["r"] * 3 + ["b"] * 5
for comb in itertools.combinations(range(11), 3):
    s = sum(1 if balls[i] == "w" else -1 if balls[i] == "r" else 0 for i in comb); cnt[s] += 1
tot = sum(cnt.values()); P("sheet 2: winnings pmf (x: count/165):", {k: f"{v}/{tot}" for k, v in sorted(cnt.items())}, " E =", sum(k * v for k, v in cnt.items()) / tot)
# coupon pmf P(T>n) = sum_i (-1)^{i+1} C(N,i)(1-i/N)^n
def PTgt(N, n): return sum((-1) ** (i + 1) * C(N, i) * (1 - i / N) ** n for i in range(1, N + 1))
P("coupon N=3: P(T>n) n=3..6:", [round(PTgt(3, n), 4) for n in range(3, 7)], " pmf P(T=3) =", 1 - PTgt(3, 3), " via 6/27 =", 6 / 27, "; E[T] =", sum(PTgt(3, n) for n in range(0, 400)), "= 3*H_3 =", 5.5)
P("  N=6: E[T] via the tail sum sum_n P(T>n):", sum(PTgt(6, n) for n in range(1, 800)) + 1.0, " vs 6 H_6 =", 6 * sum(1 / i for i in range(1, 7)))
P("two coins 0.6, 0.7: P(X=1) =", 0.6 * 0.3 + 0.4 * 0.7, " E =", 1.3, " pmf", [0.4 * 0.3, 0.6 * 0.3 + 0.4 * 0.7, 0.6 * 0.7])
pm = {0: .5, 1: .1, 2: .2, 3: .1, 3.5: .1}
P("sheet 7: pmf from cdf:", pm, " E[X] =", sum(k * v for k, v in pm.items()))
# quiz show: attempt order
for p1, p2, V1, V2 in ((0.8, 0.5, 100, 400), (0.5, 0.8, 100, 400)):
    e12 = p1 * (V1 + p2 * V2); e21 = p2 * (V2 + p1 * V1); P(f"quiz p=({p1},{p2}) V=({V1},{V2}): 1 first {e12:.1f}, 2 first {e21:.1f}; indices V p/(1-p):", V1 * p1 / (1 - p1), V2 * p2 / (1 - p2))
P("Poisson E[X] = lam: check lam=3.2:", float((np.arange(80) * stats.poisson(3.2).pmf(np.arange(80))).sum()))
P("geometric mean via first-step: E = p + q(1+E) -> 1/p = ", 1 / 0.25, "; sum check", float((np.arange(1, 400) * stats.geom(0.25).pmf(np.arange(1, 400))).sum()))
P("negative binomial pmf (trials to k=3rd success, p=0.4): P(N=3), P(N=4), P(N=5):", [C(n - 1, 2) * 0.4 ** 3 * 0.6 ** (n - 3) for n in (3, 4, 5)])
P("Poisson from binomial: n=1000, c=3.2 at k=3:", stats.binom.pmf(3, 1000, 3.2 / 1000), " vs Poisson", stats.poisson.pmf(3, 3.2))

sec("PR04 joint, expectation, variance")
dice = np.array(list(itertools.product(range(1, 7), repeat=2)))
S2 = dice.sum(1); M2 = dice.max(1)
P("sum of two dice: mean", S2.mean(), " var", S2.var(), " = 35/6 =", 35 / 6, "; max: mean", M2.mean(), "=161/36=", 161 / 36, " var", M2.var())
P("cov(sum,max) =", np.cov(S2, M2, bias=True)[0, 1], " -> not independent")
P("Var(Binomial) np(1-p):", 10 * 0.3 * 0.7, "; Var(Geom(p)) (1-p)/p^2 at p=0.25:", 0.75 / 0.0625, "; NegBin(3,0.4) mean 3/0.4 =", 7.5, " var 3*0.6/0.16 =", 3 * 0.6 / 0.16)
lam = 2.0
P("Poisson(2): E X^3 = lam^3+3 lam^2+lam =", lam ** 3 + 3 * lam ** 2 + lam, " ; recursion E[X^3]=lam E[(X+1)^2] =", lam * (lam ** 2 + lam + 2 * lam + 1 + 0) if False else lam * (stats.poisson(lam).moment(2) + 2 * lam + 1))
x = np.arange(0, 80)
P("  MC-free check E[X^3]:", float((x ** 3 * stats.poisson(lam).pmf(x)).sum()))
P("random walk: Y = 2X - n, X~Bin(n,p): n=10,p=0.6: E Y =", 10 * (2 * 0.6 - 1), " Var Y =", 4 * 10 * 0.6 * 0.4)
P("variance of sum of independent: Var(aX+b)=a^2 Var X; e.g. 2X+3 with X=die: Var=", 4 * 35 / 12)
P("typos: n=100, p1=0.7, p2=0.6: caught by at least one ~ Bin(n, 1-(1-p1)(1-p2)) = Bin(100, 0.88): mean", 88, " P(all caught) =", 0.88 ** 100)

sec("PR04 addenda (4, 12, 17 Sep sheets)")
xs_ = np.arange(0, 400)
for nm, d in (("Poisson(3.2)", stats.poisson(3.2)), ("Binomial(10,0.3)", stats.binom(10, 0.3))):
    m1 = float((xs_ * d.pmf(xs_)).sum()); m2 = float((xs_ ** 2 * d.pmf(xs_)).sum()); fm2 = float((xs_ * (xs_ - 1) * d.pmf(xs_)).sum())
    P(f"  {nm}: E[X]={m1:.4f} E[X^2]={m2:.4f} E[X(X-1)]={fm2:.4f} Var={m2 - m1 ** 2:.4f}")
g_ = stats.geom(0.25); xs1 = np.arange(1, 600)
P("Geometric(0.25): E[X(X-1)] =", float((xs1 * (xs1 - 1) * g_.pmf(xs1)).sum()), " = 2q/p^2 =", 2 * 0.75 / 0.0625, " Var =", g_.var(), " = q/p^2 =", 0.75 / 0.0625)
r_k, p_k = 3, 0.4; nn_ = np.arange(r_k, 800); pm_ = np.array([math.comb(int(n) - 1, r_k - 1) * p_k ** r_k * (1 - p_k) ** (n - r_k) for n in nn_])
P("NegBin(3,0.4) trials: sum pmf", pm_.sum(), " mean", (nn_ * pm_).sum(), " var", (nn_ ** 2 * pm_).sum() - (nn_ * pm_).sum() ** 2, " = r q/p^2 =", 3 * 0.6 / 0.16)
lam = 2.0; Xp = stats.poisson(lam)
P("Poisson(2): E[X^3] =", float((xs_ ** 3 * Xp.pmf(xs_)).sum()), " lam^3+3lam^2+lam =", lam ** 3 + 3 * lam ** 2 + lam, " lam E[(X+1)^2] =", lam * float(((xs_ + 1) ** 2 * Xp.pmf(xs_)).sum()))
P("binomial mode (n=10,p=0.3): argmax =", int(np.argmax(stats.binom(10, 0.3).pmf(range(11)))), " floor((n+1)p) =", math.floor(11 * 0.3), "; n=9,p=0.5 (two modes):", np.round(stats.binom(9, 0.5).pmf([4, 5]), 5), " Poisson(3.2) mode:", int(np.argmax(stats.poisson(3.2).pmf(range(20)))), " Poisson(3) modes:", np.round(stats.poisson(3).pmf([2, 3]), 5))
n_, p_ = 10, 0.3; P("E[1/(X+1)] Bin(10,0.3):", float((1 / (xs_[:11] + 1) * stats.binom(10, 0.3).pmf(range(11))).sum()), " (1-(1-p)^(n+1))/((n+1)p) =", (1 - (1 - p_) ** (n_ + 1)) / ((n_ + 1) * p_))
# family birth rank, 4 Sep sheet problem 8
fam = {1: 30, 2: 50, 3: 20}
pa = {r: sum(f * (1 / k) for k, f in fam.items() if k >= r) / 100 for r in (1, 2, 3)}
pb = {r: sum(f for k, f in fam.items() if k >= r) / sum(k * f for k, f in fam.items()) for r in (1, 2, 3)}
P("family birth rank: family-first pmf", {k: round(v, 4) for k, v in pa.items()}, " E =", round(sum(k * v for k, v in pa.items()), 4), "; child-first pmf", {k: round(v, 4) for k, v in pb.items()}, " E =", round(sum(k * v for k, v in pb.items()), 4))
P("amoeba: E = (0+1+2)/3 =", 1.0, "; fixed points E = 1; E[#distinct types] N=10,n=20:", 10 * (1 - (0.9) ** 20))
P("typos: X ~ Bin(n, 1-(1-0.7)(1-0.6)=0.88), n=100: mean", 88, " var", 100 * 0.88 * 0.12)
P("prizes: max of 5 of 100: E=", 5 * 101 / 6, " P(X=100) =", 5 / 100, " P(max=96)=", math.comb(95, 4) / math.comb(100, 5))
P("17 Sep (9): cdf jumps P(X=1) =", 0.5 - 0.25, " P(X=2) =", 11 / 12 - 0.75, " P(X=3) =", 1 - 11 / 12)
P("17 Sep (10): P(Liberal | voted) =", 0.30 * 0.62 / (0.46 * 0.35 + 0.30 * 0.62 + 0.24 * 0.58))
P("17 Sep (7): salesman E[X]: each appointment: 0.3*750 + 0.6*750 =", 0.3 * 750 + 0.6 * 750)
P("17 Sep (11): c(1-x^2) on (-1,1): c = 3/4:", 1 / integrate.quad(lambda x: 1 - x * x, -1, 1)[0])
P("corr(sum,max) of two dice =", 2.9166667 / math.sqrt(35 / 6 * 1.9714506))
# variance of sum of dice via indicators/covariance check
P("Var(sum of 10 dice) = 10*35/12 =", 10 * 35 / 12, " MC:", np.var(rng.integers(1, 7, size=(200000, 10)).sum(1)))
def p1wins(perm):
    best = perm[0]; w = 0
    for v in perm[1:]:
        if best == perm[0]: pass
        break
    # sequential: winner so far vs next
    cur = max(perm[0], perm[1]); k = int(perm[0] > perm[1])
    for v in perm[2:]:
        if cur == perm[0] and perm[0] > v: k += 1
        cur = max(cur, v)
    return k
res = Counter(p1wins(rng.permutation(5)) for _ in range(120000))
P("17 Sep (8): P(X=k) exact", [round(1 / (k + 1) - 1 / (k + 2), 4) for k in range(4)] + [0.2], " MC", [round(res[k] / 120000, 4) for k in range(5)])
# two-stage random-walk position
P("walk 6 steps p=0.6: P(Y=2) =", stats.binom.pmf(4, 6, 0.6), " E Y =", 2 * 3.6 - 6)

sec("PR05 continuous")
F_ray = lambda x: 1 - np.exp(-x ** 2 / 2)
P("Rayleigh f=x e^{-x^2/2}: P(1<X<3) =", math.exp(-0.5) - math.exp(-4.5), " quartiles:", [math.sqrt(-2 * math.log(1 - q)) for q in (0.25, 0.5, 0.75)], " mean sqrt(pi/2) =", math.sqrt(math.pi / 2), " var 2 - pi/2 =", 2 - math.pi / 2)
P("  check numerically:", integrate.quad(lambda x: x * np.exp(-x ** 2 / 2), 1, 3)[0], integrate.quad(lambda x: x * x * np.exp(-x ** 2 / 2), 0, np.inf)[0])
P("circle R~U(0,1), A=pi R^2: E A = pi/3 =", math.pi / 3, " E A^2 = pi^2/5, Var = 4 pi^2/45 =", 4 * math.pi ** 2 / 45, " F_A(a)=sqrt(a/pi) on [0,pi]")
R_ = rng.random(1000000); A_ = math.pi * R_ ** 2
P("  MC:", A_.mean(), A_.var())
pp = 0.5
P("stick: E[X] = 1/2 + p - p^2; p=0.5:", 0.5 + pp - pp ** 2, " max at p=1/2; MC:", end=" ")
u_ = rng.random(1000000); X_ = np.where(u_ > pp, u_, 1 - u_); P(X_.mean())
for c in (0.0, 1.0, -1.0, 2.0):
    P(f"  E[max(Z-c,0)] c={c}: phi(c) - c(1-Phi(c)) = {stats.norm.pdf(c) - c * stats.norm.sf(c):.5f} ; numeric {integrate.quad(lambda z: (z - c) * stats.norm.pdf(z), c, np.inf)[0]:.5f}")
P("normal: P(|Z|<1,2,3) =", [round(float(stats.norm.cdf(k) - stats.norm.cdf(-k)), 4) for k in (1, 2, 3)])
P("inflection of phi: phi''(x)=(x^2-1)phi(x)=0 at x=±1; N(mu,sigma^2): mu±sigma")
P("integral of e^{-x^2/2} =", integrate.quad(lambda x: math.exp(-x * x / 2), -np.inf, np.inf)[0], " sqrt(2 pi) =", math.sqrt(2 * math.pi))
P("uniform(a,b): var (b-a)^2/12; a=0,b=1:", 1 / 12, " ; logistic Var = pi^2/3 =", math.pi ** 2 / 3, " MC", np.var(rng.logistic(size=1000000)))
P("E Y = int P(Y>y) dy for Y=X^2 with X~U(0,1): ", integrate.quad(lambda y: 1 - math.sqrt(y), 0, 1)[0], " = E X^2 = 1/3")
P("LOTUS: E[Z^2] =", integrate.quad(lambda z: z * z * stats.norm.pdf(z), -np.inf, np.inf)[0])

sec("PR06 addenda (symbolic MGF checks, Chebyshev, CLT distances)")
import sympy as sp
t_, lam_, p_s, n_s, mu_s, sg_s = sp.symbols("t lambda p n mu sigma", positive=True)
q_s = 1 - p_s
def mom(M, k): return sp.simplify(sp.diff(M, t_, k).subs(t_, 0))
M_pois = sp.exp(lam_ * (sp.exp(t_) - 1)); M_bin = (q_s + p_s * sp.exp(t_)) ** n_s
M_geo = p_s * sp.exp(t_) / (1 - q_s * sp.exp(t_)); M_nrm = sp.exp(mu_s * t_ + sg_s ** 2 * t_ ** 2 / 2)
M_exp = lam_ / (lam_ - t_); M_uni = (sp.exp(t_) - 1) / t_
P("Poisson MGF: E X =", mom(M_pois, 1), " E X^2 =", sp.expand(mom(M_pois, 2)), " E X^3 =", sp.expand(mom(M_pois, 3)), " Var =", sp.simplify(mom(M_pois, 2) - mom(M_pois, 1) ** 2))
P("Binomial MGF: E X =", sp.simplify(mom(M_bin, 1)), " Var =", sp.factor(sp.simplify(mom(M_bin, 2) - mom(M_bin, 1) ** 2)))
P("Geometric MGF: E X =", sp.simplify(mom(M_geo, 1)), " Var =", sp.simplify(mom(M_geo, 2) - mom(M_geo, 1) ** 2))
P("Normal MGF: E X =", mom(M_nrm, 1), " Var =", sp.simplify(mom(M_nrm, 2) - mom(M_nrm, 1) ** 2), " E[(X-mu)^4] =", sp.simplify(sp.diff(sp.exp(sg_s ** 2 * t_ ** 2 / 2), t_, 4).subs(t_, 0)))
P("Exp MGF: E X^k = k!/lam^k for k=1..4:", [sp.simplify(mom(M_exp, k)) for k in range(1, 5)])
P("Uniform(0,1) MGF series (e^t-1)/t at t->0 moments E X^k=1/(k+1):", [sp.limit(sp.diff(M_uni, t_, k), t_, 0) for k in range(1, 5)])
P("N(0,1) even moments E Z^(2k) = (2k)!/(2^k k!):", [math.factorial(2 * k) // (2 ** k * math.factorial(k)) for k in range(1, 6)])
P("excess kurtosis: Uniform", stats.uniform.stats(moments="k"), " Poisson(3.2):", stats.poisson(3.2).stats(moments="k"), " Exp:", stats.expon.stats(moments="k"), " Bernoulli(0.5):", stats.bernoulli(0.5).stats(moments="k"))
P("Binomial(n,c/n) MGF -> Poisson: (1 + c(e^t-1)/n)^n at t=0.7, c=3.2, n=10^2,10^4,10^6:", [round((1 + 3.2 * (math.exp(0.7) - 1) / nn) ** nn, 4) for nn in (100, 10 ** 4, 10 ** 6)], " limit", round(math.exp(3.2 * (math.exp(0.7) - 1)), 4))
for k in (2, 3):
    P(f"Chebyshev k={k}: bound {1 / k ** 2:.4f}; normal tail {2 * stats.norm.sf(k):.4f}; Exp(1) P(|X-1|>={k}) = {math.exp(-(1 + k)):.4f} ; uniform(0,1) P(|X-.5|>={k}/sqrt(12)) = {max(0.0, 1 - 2 * k / math.sqrt(12)):.4f}")
P("Markov: P(X>=a) <= E[X]/a: Exp(1), a=3: bound", 1 / 3, " exact", math.exp(-3))
P("Weak LLN, die means: P(|mean of n dice - 3.5| > 0.25): Chebyshev bound (35/12)/(n 0.0625) and MC for n=100:", 35 / 12 / (100 * 0.0625), float(np.mean(np.abs(rng.integers(1, 7, size=(200000, 100)).mean(1) - 3.5) > 0.25)))
for n in (1, 5, 30, 100, 1000):
    xs_g = np.linspace(-6, 6, 4001)
    F = stats.gamma.cdf(n + xs_g * math.sqrt(n), a=n)
    P(f"CLT: sum of n={n} Exp(1): sup|F_n - Phi| = {np.max(np.abs(F - stats.norm.cdf(xs_g))):.4f};  Edgeworth leading term skew/(6 sqrt(2 pi n)) = {2 / (6 * math.sqrt(2 * math.pi * n)):.4f}")
P("normal approx binomial: n=100,p=0.5: P(X<=45) exact", stats.binom.cdf(45, 100, 0.5), " corrected", stats.norm.cdf((45.5 - 50) / 5), " uncorrected", stats.norm.cdf((45 - 50) / 5))
P("Poisson(100) P(X<=90): exact", stats.poisson.cdf(90, 100), " normal corrected", stats.norm.cdf((90.5 - 100) / 10))
P("Cauchy: P(|X|>3) =", 2 * stats.cauchy.sf(3), " Pareto(alpha=1.5) mean xm*alpha/(alpha-1) =", 1.5 / 0.5, " var infinite")

sec("PR06 MGFs, limits")
P("Poisson skewness 1/sqrt(lam) at lam=3.2:", 1 / math.sqrt(3.2), " excess kurtosis 1/lam:", 1 / 3.2)
P("Exp(1): skew", stats.expon.stats(moments="s"), " excess kurt", stats.expon.stats(moments="k"))
P("Binomial(30,0.3): P(X<=10) exact", stats.binom.cdf(10, 30, 0.3), " normal approx with continuity:", stats.norm.cdf((10.5 - 9) / math.sqrt(30 * 0.3 * 0.7)), " without:", stats.norm.cdf((10 - 9) / math.sqrt(30 * 0.3 * 0.7)))
P("Binomial(n,c/n) -> Poisson(c): total variation distance n=100, 1000, 10000 for c=3.2:",
  [round(0.5 * float(np.abs(stats.binom.pmf(np.arange(60), nn, 3.2 / nn) - stats.poisson.pmf(np.arange(60), 3.2)).sum()), 5) for nn in (100, 1000, 10000)])
P("MGF check: Bin(10,0.3) M'(0) = np =", 3.0, " M''(0)-M'(0)^2 = np(1-p) = 2.1 (derived symbolically in the chapter)")
t = 0.7; xs = np.arange(0, 60)
P("Poisson(3.2) M(0.7) numeric vs e^{lam(e^t-1)}:", float((np.exp(t * xs) * stats.poisson.pmf(xs, 3.2)).sum()), math.exp(3.2 * (math.exp(t) - 1)))
P("normal M(t)=exp(mu t + sigma^2 t^2/2): mu=1, sigma=2, t=0.3:", math.exp(0.3 + 4 * 0.09 / 2), " numeric:", integrate.quad(lambda x: math.exp(0.3 * x) * stats.norm.pdf(x, 1, 2), -40, 40)[0])
P("Cauchy has no mean: sample means of 10^5 draws vary:", [round(float(np.mean(rng.standard_cauchy(100000))), 3) for _ in range(5)])
P("exponential memoryless: P(X>s+t | X>s) = P(X>t): lam=0.5, s=2, t=3:", math.exp(-0.5 * 3))


sec("PR05/PR06 update: Week 2 and Week 3 handwritten lectures (folded normal, exponential, median/mode, MGFs)")
import sympy as sp_
# --- Week 2: folded normal
Z_ = stats.norm
P("folded normal |Z|: E =", integrate.quad(lambda y: y * 2 * Z_.pdf(y), 0, np.inf)[0], " sqrt(2/pi) =", math.sqrt(2 / math.pi),
  " ; E[X^2] =", integrate.quad(lambda y: y ** 2 * 2 * Z_.pdf(y), 0, np.inf)[0], " ; Var =", 1 - 2 / math.pi, " (", round(1 - 2 / math.pi, 5), ")")
zs = np.abs(rng.standard_normal(2_000_000))
P(f"  Monte Carlo: mean {zs.mean():.5f}, var {zs.var():.5f}; cdf at 1: {np.mean(zs <= 1):.5f} vs 2Phi(1)-1 = {2 * Z_.cdf(1) - 1:.5f}")
# --- Week 2: exponential
lam_ = 0.7
P("Exponential: I_n = int_0^inf lam x^n e^{-lam x} dx = n!/lam^n, n=0..5:", [round(integrate.quad(lambda x, n=n: lam_ * x ** n * math.exp(-lam_ * x), 0, np.inf)[0], 6) for n in range(6)], [round(math.factorial(n) / lam_ ** n, 6) for n in range(6)])
P("  Var = 2/lam^2 - 1/lam^2 = 1/lam^2:", 2 / lam_ ** 2 - 1 / lam_ ** 2, 1 / lam_ ** 2)
# geometric -> exponential: P(G >= k) = q^k with q = 1 - lam h, k = x/h
for h_ in (0.5, 0.1, 0.01, 0.001):
    P(f"  h = {h_}: (1 - lam h)^(x/h) at lam=0.5, x=2: {(1 - 0.5 * h_) ** (2 / h_):.6f}  -> e^-1 = {math.exp(-1):.6f}")
# memoryless
P("  memoryless: P(X>=t+s | X>=s) vs P(X>=t), lam=0.5, s=2, t=3:", math.exp(-0.5 * 5) / math.exp(-0.5 * 2), math.exp(-0.5 * 3))
P("  uniform(0,1) is NOT memoryless: P(X>=0.5+0.25 | X>=0.25) =", (1 - 0.75) / (1 - 0.25), " vs P(X>=0.5) =", 0.5)
P("  discrete memoryless: Geom(failures, q=0.6): P(G>=m+n | G>=m) vs P(G>=n) for m=2,n=3:", 0.6 ** 5 / 0.6 ** 2, 0.6 ** 3)
# HW2
P("HW2 Q1: lam = 1/2: P(T>2) =", math.exp(-1), "; P(T>=10 | T>9) = P(T>=1) =", math.exp(-0.5))
P("HW2 Q2: Gumbel cdf exp(-e^{-y}); P(M_n - ln n <= y) = (1 - e^{-y}/n)^n; y = 0.5:", [round((1 - math.exp(-0.5) / n) ** n, 6) for n in (1, 2, 5, 20, 200, 10 ** 4)], " limit:", round(math.exp(-math.exp(-0.5)), 6))
mx = np.max(rng.exponential(size=(20000, 200)), axis=1) - math.log(200)
P(f"  Monte Carlo n=200: P(M_n - ln n <= 0.5) = {np.mean(mx <= 0.5):.4f}; mean of M_n - ln n = {mx.mean():.4f} (Gumbel mean = Euler gamma = {np.euler_gamma:.4f}); var {mx.var():.4f} (pi^2/6 = {math.pi ** 2 / 6:.4f})")
gum = -np.log(rng.exponential(size=1_000_000))
P(f"  -log X, X~Expo(1): mean {gum.mean():.4f}, var {gum.var():.4f}; P(<= 0.5) = {np.mean(gum <= 0.5):.4f} vs exp(-e^-0.5) = {math.exp(-math.exp(-0.5)):.4f}")
for nm, d in (("normal", stats.norm()), ("exponential(1)", stats.expon()), ("Rayleigh sigma=1", stats.rayleigh()), ("uniform(2,5)", stats.uniform(2, 3))):
    xs_ = d.rvs(size=1_000_000, random_state=11)
    P(f"HW2 Q3: E[F(X)] for {nm}: {d.cdf(xs_).mean():.5f} (exact 1/2); E[F(X)^2] = {np.mean(d.cdf(xs_) ** 2):.5f} (1/3)")
# --- Week 3: median / mode
P("Median of fair die (discrete): P(X<=3) =", 0.5, ", P(X>=4) = 0.5 -> every c in [3,4] is a median (the unified definition)")
P("Uniform(a,b): median (a+b)/2; mode = every point. Expo(lam): median ln2/lam =", math.log(2) / 0.7, "for lam=0.7; mode 0 (sup of f at the boundary)")
P("Pareto(a): F = 1 - x^-a, median 2^(1/a): a=2:", 2 ** 0.5, " a=1:", 2.0, " ; mode 1; mean a/(a-1) for a>1: a=2:", 2.0, " ; scipy:", stats.pareto(2).median(), stats.pareto(2).mean())
P("Expo skewness = 2 (any lam):", [round(float(stats.expon(scale=1 / l).stats(moments='s')), 6) for l in (0.5, 1, 3)], " ; excess kurtosis 6:", round(float(stats.expon().stats(moments='k')), 6))
# Uniform MGF Taylor (the lecture's printed denominator slip)
tt = sp_.symbols("t"); a_, b_ = sp_.symbols("a b", positive=True)
Mu = (sp_.exp(tt * b_) - sp_.exp(tt * a_)) / (tt * (b_ - a_))
ser = sp_.series(Mu, tt, 0, 5).removeO()
for m in range(4):
    cm = sp_.simplify(ser.coeff(tt, m) * sp_.factorial(m))
    true = sp_.simplify((b_ ** (m + 1) - a_ ** (m + 1)) / ((m + 1) * (b_ - a_)))
    P(f"  Uniform(a,b) E[X^{m}] = {sp_.factor(cm)}  (= (b^(m+1)-a^(m+1))/((m+1)(b-a)): {sp_.simplify(cm - true) == 0}); the lecture's printed '/m' would give {sp_.simplify((sum(b_ ** (m - j) * a_ ** j for j in range(m + 1))) / m) if m > 0 else 'undefined (division by 0)'}")
# N(mu, sigma^2) MGF sign
mu_, sg_, t0 = 1.0, 2.0, 0.3
P(f"N(1,4) MGF at t=0.3: numeric {integrate.quad(lambda x: math.exp(t0 * x) * stats.norm.pdf(x, mu_, sg_), -50, 50)[0]:.5f}; exp(mu t + sigma^2 t^2/2) = {math.exp(mu_ * t0 + sg_ ** 2 * t0 ** 2 / 2):.5f}; the page's minus-sign version exp(mu t - sigma^2 t^2/2) = {math.exp(mu_ * t0 - sg_ ** 2 * t0 ** 2 / 2):.5f} (< e^(mu t) = {math.exp(mu_ * t0):.5f}, impossible by Jensen)")
# HW3 Q4: two dice
Md = sum(sp_.exp(k * tt) for k in range(1, 7)) / 6
M2 = sp_.simplify(Md ** 2)
P("HW3 Q4: M_{X+Y}(t) = ((e^t+...+e^{6t})/6)^2; mean M'(0) =", sp_.simplify(sp_.diff(M2, tt).subs(tt, 0)), " ; Var =", sp_.simplify(sp_.diff(M2, tt, 2).subs(tt, 0) - sp_.diff(M2, tt).subs(tt, 0) ** 2), "(7, 35/6)")
# HW3 Q5: Geom (failures) via MGF
p_, q_ = sp_.symbols("p q", positive=True)
Mg = p_ / (1 - (1 - p_) * sp_.exp(tt))
m1 = sp_.simplify(sp_.diff(Mg, tt).subs(tt, 0)); m2 = sp_.simplify(sp_.diff(Mg, tt, 2).subs(tt, 0))
P("HW3 Q5: M(t) = p/(1-(1-p)e^t): E[X] =", sp_.simplify(m1), " ; E[X^2] =", sp_.factor(m2), " ; Var =", sp_.simplify(sp_.factor(m2 - m1 ** 2)), " (q/p, q/p^2 with q=1-p)")
P("  trials convention X' = X + 1: M' = e^t M = p e^t/(1-q e^t): mean 1/p:", sp_.simplify(sp_.diff(sp_.exp(tt) * Mg, tt).subs(tt, 0)))
# HW3 Q6: folded normal MGF
t1 = 0.7
P(f"HW3 Q6: M_Y(t) = int_0^inf e^{{ty}} 2 phi(y) dy = int e^{{t|z|}} phi(z) dz; at t={t1}: {integrate.quad(lambda y: math.exp(t1 * y) * 2 * stats.norm.pdf(y), 0, np.inf)[0]:.6f}; "
  f"{integrate.quad(lambda z: math.exp(t1 * abs(z)) * stats.norm.pdf(z), -np.inf, np.inf)[0]:.6f}; closed form 2 e^(t^2/2) Phi(t) = {2 * math.exp(t1 ** 2 / 2) * stats.norm.cdf(t1):.6f}")
# MGF = EGF of moments; Bernoulli moments; N(0,1) even moments
P("Bernoulli(p): M = q + p e^t: E[X^n] = p for n>=1; Binomial MGF (q+pe^t)^n; N(0,1) E[Z^{2k}] = (2k)!/(k! 2^k):", [math.factorial(2 * k) // (math.factorial(k) * 2 ** k) for k in range(6)])
P("Expo MGF lam/(lam - t) = sum (t/lam)^n = sum E[X^n] t^n / n! with E[X^n] = n!/lam^n; radius of convergence |t| < lam")
