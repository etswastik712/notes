#!/usr/bin/env python3
"""Numbers for EE08 (evolution intro), EE09 (Hardy-Weinberg), EE10 (selection). Added 2026-11-21.
Every printed value in those chapters comes from here.  Run: .venv/bin/python -I scripts/ee08_10_numbers.py
"""
import numpy as np
from math import sqrt, exp
from scipy.stats import chi2 as CHI2


def hw_test(obs, label):
    """obs = (n_AA, n_Aa, n_aa) counts; returns p, expected, chi2, P (1 df)."""
    nAA, nAa, naa = obs
    N = nAA + nAa + naa
    p = (2 * nAA + nAa) / (2 * N); q = 1 - p
    exp_ = np.array([p * p, 2 * p * q, q * q]) * N
    x2 = float(((np.array(obs) - exp_) ** 2 / exp_).sum())
    P = 1 - CHI2.cdf(x2, 1)
    print(f"{label}: N={N} P,Q,R=({nAA/N:.3f},{nAa/N:.3f},{naa/N:.3f}) p={p:.4f} q={q:.4f} "
          f"exp=({exp_[0]:.2f},{exp_[1]:.2f},{exp_[2]:.2f}) chi2={x2:.3f} P={P:.3f}")
    return p, exp_, x2, P


print("=== EE09 lecture examples")
hw_test((83, 46, 11), "Pueblo MN (lecture slide 7, Templeton Box 2.1)")
hw_test((298, 489, 213), "British MN (Hartl & Clark p.81)")
for P_, Q_, R_ in [(0.3, 0.6, 0.1), (0.2, 0.8, 0.0)]:
    p = P_ + Q_ / 2
    print(f"parents {P_}:{Q_}:{R_} -> p={p:.2f}, progeny {p*p:.2f}:{2*p*(1-p):.2f}:{(1-p)**2:.2f}")
# heterozygote maximum and rare alleles
ps = np.linspace(0, 1, 100001); H = 2 * ps * (1 - ps)
print(f"max 2pq = {H.max():.3f} at p = {ps[H.argmax()]:.3f}")
for q in (0.1, 0.01, 0.001):
    print(f"q={q}: carriers/affected = 2pq/q^2 = {2*(1-q)*q/(q*q):.0f}; share of the rare allele in heterozygotes = {(1-q)*q/((1-q)*q+q*q):.3f}")
# multi-allele acid phosphatase
g = dict(AA=9.6, AB=48.3, BB=34.3, AC=2.8, BC=5.0, CC=0.0)
pA = (g["AA"] + (g["AB"] + g["AC"]) / 2) / 100; pB = (g["BB"] + (g["AB"] + g["BC"]) / 2) / 100; pC = ((g["AC"] + g["BC"]) / 2 + g["CC"]) / 100
print(f"acid phosphatase: pA={pA:.4f} pB={pB:.4f} pC={pC:.4f}; expected CC in 178 = {pC*pC*178:.2f} (P(no CC) = {(1-pC*pC)**178:.2f})")
for lab, f in [("PKU 1/11000", 1 / 11000), ("albinism 1/10000", 1 / 10000)]:
    q = sqrt(f); print(f"{lab}: q={q:.4f}, carriers 2pq={2*q*(1-q):.4f} = 1/{1/(2*q*(1-q)):.0f}")
q = sqrt(0.30); print(f"PTC non-taster 30%: q={q:.4f}")

print("=== EE09 practice set (PopgenPracticeProblem)")
for reg, n, neg in [("Norbotten", 139, 44.60), ("Stockholm", 509, 42.24), ("Malmohus/Kristianstad", 293, 45.05)]:
    q = sqrt(neg / 100); p = 1 - q
    print(f"Gm {reg}: q={q:.4f} p={p:.4f} heterozygotes 2pq={2*p*q:.4f} (~{2*p*q*n:.0f} of {n})")
q = 1 / 16; p = 1 - q
print(f"sheep: q={q:.4f}, carriers overall 2pq={2*p*q:.4f}, among normal 2pq/(1-q^2)={2*p*q/(1-q*q):.4f} = {2*p*q/(1-q*q)*1024*(1-q*q):.0f} of {1024*(1-q*q):.0f} normal sheep")
hw_test((1430, 1130, 260), "Shorthorn red:roan:white")
q = sqrt(0.30); p = 1 - q
pTt = 2 * p * q / (p * p + 2 * p * q)
print(f"PTC 70% tasters: p={p:.4f} q={q:.4f} TT={p*p:.4f} Tt={2*p*q:.4f} tt={q*q:.4f}; P(Tt|taster)={pTt:.4f}; "
      f"P(non-taster child | taster x taster) = {pTt**2/4:.4f}  (= q^2/(1+q)^2 = {q*q/(1+q)**2:.4f})")
MM, MN, NN = 0.2838, 0.4957, 0.2205
pM = MM + MN / 2
e = np.array([pM * pM, 2 * pM * (1 - pM), (1 - pM) ** 2])
print(f"MN %: pM={pM:.4f} qN={1-pM:.4f} expected %=({e[0]*100:.2f},{e[1]*100:.2f},{e[2]*100:.2f})")
for N in (100, 1000, 10000):
    obs = np.array([MM, MN, NN]) * N; x2 = float(((obs - e * N) ** 2 / (e * N)).sum())
    print(f"   if N={N}: chi2={x2:.4f} P={1-CHI2.cdf(x2,1):.3f}")

print("=== EE09 extra: unequal allele frequencies in the sexes (Hartl Problem 3.3)")
pm, pf = 0.9, 0.3
g1 = (pm * pf, pm * (1 - pf) + (1 - pm) * pf, (1 - pm) * (1 - pf)); pbar = (pm + pf) / 2
print(f"pm={pm} pf={pf}: gen1 genotypes {tuple(round(x,4) for x in g1)}, HW would be {(round(pbar**2,4), round(2*pbar*(1-pbar),4), round((1-pbar)**2,4))}; gen2 = HW at p={pbar}")

print("=== EE08 extra: blending vs Mendelian inheritance (Jenkin 1867)")
rng = np.random.default_rng(1)
N, G = 20000, 8
x = rng.normal(0, 1, N); V0 = x.var()
blend = [V0]
for t in range(G):
    m = rng.permutation(N); x = 0.5 * (x + x[m]); blend.append(x.var())
print("blending variance by generation:", " ".join(f"{v/V0:.3f}" for v in blend), "(theory 0.5^t)")
L = 20  # additive loci, Mendelian, random mating
geno = rng.random((N, L, 2)) < 0.5
z = geno.sum(axis=(1, 2)).astype(float); Vm = [z.var()]
for t in range(G):
    mom = geno[rng.permutation(N)]; dad = geno[rng.permutation(N)]
    pick_m = rng.random((N, L)) < 0.5; pick_d = rng.random((N, L)) < 0.5
    a1 = np.where(pick_m, mom[:, :, 0], mom[:, :, 1]); a2 = np.where(pick_d, dad[:, :, 0], dad[:, :, 1])
    geno = np.stack([a1, a2], axis=2); z = geno.sum(axis=(1, 2)).astype(float); Vm.append(z.var())
print("Mendelian (20 loci) variance:", " ".join(f"{v/Vm[0]:.3f}" for v in Vm))

print("=== EE10 one-locus selection")
def traj(w11, w12, w22, p0=0.01, pend=0.99, gmax=200000):
    p, t = p0, 0
    while p < pend and t < gmax:
        q = 1 - p; wbar = p * p * w11 + 2 * p * q * w12 + q * q * w22
        p = (p * p * w11 + p * q * w12) / wbar; t += 1
    return t
s = 0.1
for lab, w in [("additive (h=1/2)", (1, 1 - s / 2, 1 - s)), ("A dominant (favoured allele dominant)", (1, 1, 1 - s)), ("A recessive", (1, 1 - s, 1 - s))]:
    print(f"s={s} {lab}: generations p 0.01 -> 0.99 = {traj(*w)}")
s_, t_ = 0.2, 0.1   # heterozygote advantage: w11 = 1-s, w12 = 1, w22 = 1-t
pstar = t_ / (s_ + t_)
print(f"overdominance w=(1-{s_},1,1-{t_}): p* = t/(s+t) = {pstar:.4f}")
p = 0.9
for _ in range(500):
    q = 1 - p; wb = p*p*(1-s_) + 2*p*q + q*q*(1-t_); p = (p*p*(1-s_) + p*q)/wb
print(f"   from p=0.9 after 500 gen: p={p:.4f}")
p = 0.5
for _ in range(500):
    q = 1 - p; wb = p*p*1.0 + 2*p*q*0.9 + q*q*1.0; p = (p*p + p*q*0.9)/wb
print(f"underdominance w=(1,0.9,1): p=0.5 is unstable; from 0.5 exactly stays {p:.3f}; from 0.51 ->", end=" ")
p = 0.51
for _ in range(500):
    q = 1 - p; wb = p*p + 2*p*q*0.9 + q*q; p = (p*p + p*q*0.9)/wb
print(f"{p:.4f}")
h2 = 0.65
for S in (0.25, 0.5):
    print(f"breeder's equation R = h^2 S: h^2={h2} (Keller et al., F&H p.85), S={S} mm (illustrative) -> R={h2*S:.3f} mm")
print(f"1983 rain / 1977 rain = {1359/24:.1f} (F&H p.88 says 'almost 57 times')")
