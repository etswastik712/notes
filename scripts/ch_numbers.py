"""CH (inorganic chemistry, CH2113) - numbers quoted in chapters CH01..., recomputed.

    .venv/bin/python -W ignore scripts/ch_numbers.py
"""
import itertools
import math

import numpy as np
from scipy import integrate

P = print


def sec(t): P("\n=====", t)


sec("CH01 steric number Z = (V + M + A - C)/2 and shape (VSEPR)")
# V = valence electrons of the central atom, M = monovalent terminal atoms (H, halogens), A = anion charge, C = cation charge
# n = number of terminal atoms (a double-bonded O counts as one region and as 0 for M); lone pairs L = Z - n
species = [  # name, V, M, A, C, n, expected shape
    ("BeH2", 2, 2, 0, 0, 2, "linear"), ("BF3", 3, 3, 0, 0, 3, "trigonal planar"), ("CO3 2-", 4, 0, 2, 0, 3, "trigonal planar"),
    ("COF2", 4, 2, 0, 0, 3, "trigonal planar"), ("NO2 -", 5, 0, 1, 0, 2, "bent"), ("CH4", 4, 4, 0, 0, 4, "tetrahedral"),
    ("NH4 +", 5, 4, 0, 1, 4, "tetrahedral"), ("SO4 2-", 6, 0, 2, 0, 4, "tetrahedral"), ("POCl3", 5, 3, 0, 0, 4, "tetrahedral"),
    ("ClO4 -", 7, 0, 1, 0, 4, "tetrahedral"), ("NH3", 5, 3, 0, 0, 3, "trigonal pyramidal"), ("H3O +", 6, 3, 0, 1, 3, "trigonal pyramidal"),
    ("SO3 2-", 6, 0, 2, 0, 3, "trigonal pyramidal"), ("ClO3 -", 7, 0, 1, 0, 3, "trigonal pyramidal"), ("XeO3", 8, 0, 0, 0, 3, "trigonal pyramidal"),
    ("H2O", 6, 2, 0, 0, 2, "bent"), ("PCl5", 5, 5, 0, 0, 5, "trigonal bipyramidal"), ("SF4", 6, 4, 0, 0, 4, "see-saw"),
    ("ClF3", 7, 3, 0, 0, 3, "T-shaped"), ("XeF2", 8, 2, 0, 0, 2, "linear"), ("I3 -", 7, 2, 1, 0, 2, "linear"),
    ("SF6", 6, 6, 0, 0, 6, "octahedral"), ("BrF5", 7, 5, 0, 0, 5, "square pyramidal"), ("XeOF4", 8, 4, 0, 0, 5, "square pyramidal"),
    ("XeF4", 8, 4, 0, 0, 4, "square planar"), ("ICl4 -", 7, 4, 1, 0, 4, "square planar"), ("IF7", 7, 7, 0, 0, 7, "pentagonal bipyramidal"),
    ("XeF5 -", 8, 5, 1, 0, 5, "pentagonal planar"), ("SeF6 2-", 6, 6, 2, 0, 6, "octahedral (lone pair inert)"),
]
SHAPE = {(2, 0): "linear", (3, 0): "trigonal planar", (3, 1): "bent", (4, 0): "tetrahedral", (4, 1): "trigonal pyramidal", (4, 2): "bent",
         (5, 0): "trigonal bipyramidal", (5, 1): "see-saw", (5, 2): "T-shaped", (5, 3): "linear", (6, 0): "octahedral", (6, 1): "square pyramidal",
         (6, 2): "square planar", (7, 0): "pentagonal bipyramidal", (7, 2): "pentagonal planar", (7, 1): "distorted octahedron (or octahedral if the pair is inert)"}
ok = 0
for nm, V, M, A, C, n, exp in species:
    Z = (V + M + A - C) / 2
    L = int(Z) - n
    got = SHAPE.get((int(Z), L), "?")
    flag = "ok" if got == exp else f"differs: VSEPR gives '{got}'"
    ok += got == exp
    P(f"  {nm:8s} Z = {Z:.0f}, lone pairs = {L}, bonded atoms = {n}: {got:24s} expected {exp:28s} {flag}")
P(f"  agreement: {ok} of {len(species)}")

sec("CH01 90-degree repulsion counts decide where lone pairs go")
def sites_tbp():
    ax = [np.array([0, 0, 1.0]), np.array([0, 0, -1.0])]
    eq = [np.array([math.cos(a), math.sin(a), 0.0]) for a in (0, 2 * math.pi / 3, 4 * math.pi / 3)]
    return ax + eq, ["ax", "ax", "eq", "eq", "eq"]
def sites_oct():
    v = [np.array(x, float) for x in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))]
    return v, ["x", "-x", "y", "-y", "z", "-z"]
def count(vecs, lp):
    ll = lb = 0
    for i, j in itertools.combinations(range(len(vecs)), 2):
        if abs(np.dot(vecs[i], vecs[j])) < 1e-9:       # 90 degrees
            a, b = i in lp, j in lp
            if a and b: ll += 1
            elif a or b: lb += 1
    return ll, lb
for name, (vecs, lab) in (("trigonal bipyramid", sites_tbp()), ("octahedron", sites_oct())):
    for nl in (1, 2, 3):
        if name == "octahedron" and nl == 3: continue
        res = {}
        for lp in itertools.combinations(range(len(vecs)), nl):
            key = tuple(sorted(lab[i] for i in lp)) if name == "trigonal bipyramid" else count(vecs, set(lp))
            res.setdefault(key if name == "trigonal bipyramid" else count(vecs, set(lp)), set()).add(lp)
        if name == "trigonal bipyramid":
            res2 = {}
            for lp in itertools.combinations(range(len(vecs)), nl):
                kind = tuple(sorted(lab[i] for i in lp))
                res2[kind] = count(vecs, set(lp))
            best = min(res2, key=lambda k: res2[k])
            P(f"  {name}, {nl} lone pair(s): " + "; ".join(f"{k}: (lp-lp, lp-bp at 90 deg) = {v}" for k, v in sorted(res2.items())) + f"  -> {best}")
        else:
            best = min(res, key=lambda k: k)
            P(f"  {name}, {nl} lone pair(s): " + "; ".join(f"(lp-lp, lp-bp) = {k}" for k in sorted(res)) + f"  -> fewest lp-lp 90 deg first: {best}")

sec("CH01 Coulson's theorem: cos(theta) = S/(S-1), S = fractional s character of two equivalent hybrids")
S_from = lambda th: math.cos(math.radians(th)) / (math.cos(math.radians(th)) - 1)
th_from = lambda S: math.degrees(math.acos(S / (S - 1)))
for nm, S in (("pure p", 0.0), ("sp3", 0.25), ("sp2", 1 / 3), ("sp", 0.5)):
    P(f"  {nm:7s} S = {S:.4f}: theta = {th_from(S):.2f} deg; hybridisation index n (sp^n) = {(1 - S) / S if S else float('inf'):.3f}")
P("  H2O (lecture): bond angle 104.5 deg -> S_bond =", round(S_from(104.5), 4), "; n =", round((1 - S_from(104.5)) / S_from(104.5), 3))
Sb = S_from(104.5); Sl = (1 - 2 * Sb) / 2
P(f"     exact: S_lone = (1 - 2 S_bond)/2 = {Sl:.4f}; angle between lone-pair hybrids = {th_from(Sl):.2f} deg; p-character bonds {100 * (1 - Sb):.1f} %, lone pairs {100 * (1 - Sl):.1f} %")
Sb2, Sl2 = 0.20, 0.30
P(f"     lecture's rounded 20 % / 30 %: lone-pair angle = {th_from(Sl2):.2f} deg (slide: 115.37)")
for th in (107.0, 107.8):
    Sb = S_from(th); Sl = 1 - 3 * Sb
    P(f"  NH3 (take-home), H-N-H = {th} deg: S_bond = {Sb:.4f} ({100 * Sb:.1f} % s, {100 * (1 - Sb):.1f} % p; sp^{(1 - Sb) / Sb:.2f}); lone pair: {100 * Sl:.1f} % s, {100 * (1 - Sl):.1f} % p (sp^{(1 - Sl) / Sl:.2f})")
for thF in (108.3, 108.5):
    SF = S_from(thF); SH = (1 - 2 * SF) / 2
    P(f"  CH2F2 (take-home), F-C-F = {thF} deg: S_CF = {SF:.4f}, S_CH = {SH:.4f} -> predicted H-C-H = {th_from(SH):.1f} deg (CH4 25 % s; C-F bonds p-rich, C-H bonds s-rich)")
P("  generalisation to unequal hybrids: orthogonality s_a s_b + sqrt(p_a p_b) cos(theta) ... for equal hybrids: S + (1-S) cos(theta) = 0")

sec("CH01 hybrid orbitals: orthonormality and angles")
H3 = 0.5 * np.array([[1, 1, 1, 1], [1, -1, -1, 1], [1, -1, 1, -1], [1, 1, -1, -1]])
P("  sp3 coefficients (s, px, py, pz): H H^T =\n", np.round(H3 @ H3.T, 12), "\n  p-direction vectors and angles:")
dirs = H3[:, 1:]
for i, j in itertools.combinations(range(4), 2):
    c = dirs[i] @ dirs[j] / (np.linalg.norm(dirs[i]) * np.linalg.norm(dirs[j]))
    P(f"    h{i + 1}-h{j + 1}: {math.degrees(math.acos(c)):.2f} deg", end="")
P()
sp2 = np.array([[1 / math.sqrt(3), math.sqrt(2 / 3), 0], [1 / math.sqrt(3), -1 / math.sqrt(6), 1 / math.sqrt(2)], [1 / math.sqrt(3), -1 / math.sqrt(6), -1 / math.sqrt(2)]])
P("  sp2: H H^T = I?", np.allclose(sp2 @ sp2.T, np.eye(3)), "; angles:", [round(math.degrees(math.acos((sp2[i, 1:] @ sp2[j, 1:]) / (np.linalg.norm(sp2[i, 1:]) * np.linalg.norm(sp2[j, 1:])))), 2) for i, j in itertools.combinations(range(3), 3 - 1)])
P("  sp: (s +- pz)/sqrt2: angle 180 deg (cos = -1); s character 50 %")
P("  s character of the TBP dsp3 set: 3 equatorial sp2 hybrids (33.3 % s each, 120 deg) + 2 axial dp hybrids (0 % s, 180 deg): total s = 1")

sec("CH01 valence-bond H2: overlap integral and the normalised Heitler-London function")
def S_closed(R): return math.exp(-R) * (1 + R + R ** 2 / 3)
def S_num(R):
    f = lambda z, rho: (1 / math.pi) * math.exp(-math.hypot(rho, z + R / 2) - math.hypot(rho, z - R / 2)) * 2 * math.pi * rho
    return integrate.dblquad(f, 0, 40, lambda r: -40, lambda r: 40, epsabs=1e-9, epsrel=1e-9)[0]
a0 = 0.529177
for R in (0.0, 1.0, 1.4, 2.0, 4.0):
    P(f"  R = {R} a0 ({R * a0:.3f} A): S closed form {S_closed(R):.6f}" + (f"; numeric integral {S_num(R):.6f}" if R > 0 else ""))
R0 = 0.74 / a0
S0 = S_closed(R0)
P(f"  r_e(H2) = 0.74 A = {R0:.4f} a0: S = {S0:.4f}; N^2 = 1/(2(1+S^2)) = {1 / (2 * (1 + S0 ** 2)):.4f}; N = {1 / math.sqrt(2 * (1 + S0 ** 2)):.4f}")
P(f"  1 eV = 96.485 kJ/mol: 4.5 eV = {4.5 * 96.485:.1f} kJ/mol (slide: 434); 11.4 eV bonding->antibonding = {11.4 * 96.485:.0f} kJ/mol")
P(f"  Z formula check: SO4 2- Z = (6+0+2-0)/2 = {(6 + 2) / 2}; CO3 2- Z = {(4 + 2) / 2}; H2O lone pairs = (6 - 1x2)/2 = {(6 - 2) / 2}")
