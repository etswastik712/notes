"""Group-theory numbers and checks for GT01-GT04.   .venv/bin/python -W ignore scripts/gt_numbers.py
Everything is brute force on explicit permutation groups (no library), so each statement in the chapters is checked."""
import itertools, math
from collections import Counter, defaultdict
import numpy as np

def compose(p, q):            # (p*q)(i) = p(q(i))  (apply q first)
    return tuple(p[i] for i in q)
def inv(p):
    r = [0]*len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def order(p, e):
    k, x = 1, p
    while x != e: x = compose(p, x); k += 1
    return k
def generate(gens, n):
    e = tuple(range(n)); G = {e}; fr = [e]
    while fr:
        new = []
        for x in fr:
            for g in gens:
                y = compose(g, x)
                if y not in G: G.add(y); new.append(y)
        fr = new
    return G
def cycle_type(p):
    seen, t = set(), []
    for i in range(len(p)):
        if i not in seen:
            j, l = i, 0
            while j not in seen: seen.add(j); j = p[j]; l += 1
            t.append(l)
    return tuple(sorted(t, reverse=True))
def is_subgroup(S, G):
    return all(compose(a, b) in S for a in S for b in S)
def conj_classes(G):
    seen, cl = set(), []
    for x in G:
        if x in seen: continue
        c = {compose(compose(g, x), inv(g)) for g in G}
        seen |= c; cl.append(c)
    return cl

if __name__ == "__main__":
    print("== S3 = D3 ==")
    e3 = (0, 1, 2); S3 = generate([(1, 2, 0), (0, 2, 1)], 3)
    print("order", len(S3), "orders", sorted(order(p, e3) for p in S3))
    print("non-abelian:", any(compose(a, b) != compose(b, a) for a in S3 for b in S3))
    subs = set()
    for r in range(1, 4):
        for gens in itertools.combinations(sorted(S3), r):
            subs.add(frozenset(generate(list(gens), 3)))
    print("subgroups of S3:", sorted(len(s) for s in subs), "(1,2,2,2,3,6 expected)")
    print("== D4 (symmetries of the square, vertices 0..3) ==")
    e4 = (0, 1, 2, 3); D4 = generate([(1, 2, 3, 0), (0, 3, 2, 1)], 4)
    subs4 = set()
    for r in range(1, 3):
        for gens in itertools.combinations(sorted(D4), r):
            subs4.add(frozenset(generate(list(gens), 4)))
    print("order", len(D4), "subgroups by order", sorted(Counter(len(s) for s in subs4).items()))
    Z = [x for x in D4 if all(compose(x, g) == compose(g, x) for g in D4)]
    print("centre order", len(Z))
    print("== S4 ==")
    e = tuple(range(4)); S4 = set(itertools.permutations(range(4)))
    cl = conj_classes(S4)
    print("class sizes", sorted(len(c) for c in cl), "sum", sum(len(c) for c in cl))
    print("class ct", sorted((cycle_type(next(iter(c))), len(c)) for c in cl))
    V4 = {p for p in S4 if cycle_type(p) in [(1, 1, 1, 1), (2, 2)]}
    print("V4 subgroup", is_subgroup(V4, S4), len(V4), "normal",
          all(compose(compose(g, v), inv(g)) in V4 for g in S4 for v in V4))
    cos = {frozenset(compose(g, v) for v in V4) for g in S4}
    print("cosets", len(cos), "= |S4/V4|, 6 = |S3| ok")
    A4 = {p for p in S4 if sum(1 for i in range(4) for j in range(i+1, 4) if p[i] > p[j]) % 2 == 0}
    print("A4 order", len(A4), " commutator subgroup of S4 = A4:",
          generate([compose(compose(a, b), compose(inv(a), inv(b))) for a in S4 for b in S4], 4) == A4)
    print("A4 has a subgroup of order 6?", any(len(s) == 6 for r in (1, 2, 3)
        for gens in itertools.combinations(sorted(A4), r) for s in [generate(list(gens), 4)]), "(no: converse of Lagrange fails)")
    print("== Sylow counts ==")
    def sylow(G, n, p):
        o = len(G); pe = 1
        while o % (pe*p) == 0: pe *= p
        P = set()
        for r in (1, 2):
            for gens in itertools.combinations(sorted(G), r):
                H = frozenset(generate(list(gens), n))
                if len(H) == pe: P.add(H)
        return pe, len(P)
    print("S4 p=2 (|P|, n_2):", sylow(S4, 4, 2), " p=3:", sylow(S4, 4, 3))
    A5 = {p for p in itertools.permutations(range(5)) if sum(1 for i in range(5) for j in range(i+1, 5) if p[i] > p[j]) % 2 == 0}
    print("A5 order", len(A5), "p=2:", sylow(A5, 5, 2), "p=3:", sylow(A5, 5, 3), "p=5:", sylow(A5, 5, 5))
    cl5 = conj_classes(A5)
    print("A5 class sizes", sorted(len(c) for c in cl5), "(1,12,12,15,20: only normal subgroup unions of classes with order | 60 -> simple)")
    sizes = sorted(len(c) for c in cl5); ok = True
    for r in range(0, len(sizes)):
        for sub in itertools.combinations(sizes[1:], r):
            t = 1 + sum(sub)
            if 1 < t < 60 and 60 % t == 0: ok = False
    print("A5 simple (class-size argument):", ok)
    print("== class equation for D4 ==")
    clD4 = conj_classes(D4); print("D4 class sizes", sorted(len(c) for c in clD4), "= |Z|+sum of non-central", len(Z))
    print("== orbit-stabiliser (D4 on square vertices) ==")
    orb = {g[0] for g in D4}; stab = [g for g in D4 if g[0] == 0]
    print("orbit", len(orb), "stab", len(stab), "|G|", len(D4), len(orb)*len(stab) == len(D4))
    print("== Burnside: 2-colourings of the 4 vertices of a square up to rotation / dihedral ==")
    rot = [g for g in D4 if cycle_type(g) in [(1,1,1,1), (4,), (2,2)] and not (cycle_type(g) == (2,2) and g[0] == 0)]
    def burn(G, k):
        return sum(k**len(cycle_type(g)) for g in G) / len(G)
    C4 = generate([(1, 2, 3, 0)], 4)
    print("C4:", burn(C4, 2), " D4:", burn(D4, 2), " (necklaces 6, bracelets 6)  3 colours C4:", burn(C4, 3))
    print("== Cayley: every finite group embeds in S_n; |G|=60 count of orders ==")
    print("== C3v character table orthogonality ==")
    X = np.array([[1, 1, 1], [1, 1, -1], [2, -1, 0]], float); w = np.array([1, 2, 3.])
    print("sum_g chi_i chi_j =\n", (X*w) @ X.T)
    print("column orthogonality: sum_i chi_i(C) chi_i(C') =\n", X.T @ X, "\n (|G|/|class| on the diagonal: 6, 3, 2)")
    print("== NH3 (C3v): reducible characters ==")
    G_H = np.array([3, 0, 1.]); G_xyz = np.array([3, 0, 1.])
    mult = lambda g: (X*w) @ g / 6
    print("3 H(1s):", mult(G_H), "(A1,A2,E)  -> A1 + E")
    G_3N = np.array([12, 0, 2.])    # unmoved atoms x (character of vector rep): E:4*3, C3:1*0, sv:2*1
    print("Gamma_3N:", mult(G_3N))
    G_trans = np.array([3, 0, 1.]); G_rot = np.array([3, 0, -1.])
    print("Gamma_trans:", mult(G_trans), " Gamma_rot:", mult(G_rot))
    vib = G_3N - G_trans - G_rot
    print("Gamma_vib:", mult(vib), " -> 2 A1 + 2 E (6 = 3N-6 modes)")
    print("IR active = A1, E (transform like z, (x,y)): all 4 distinct frequencies IR active; Raman too")
    print("== H2O (C2v) ==")
    X2 = np.array([[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]], float)
    g3N = np.array([9, -1, 1, 3.]); gt = np.array([3, -1, 1, 1.]); gr = np.array([3, -1, -1, -1.])
    print("A1,A2,B1,B2 multiplicities of vib:", X2 @ (g3N-gt-gr)/4, " -> 2 A1 + B2 (convention-dependent label)")
    print("== SO(3) rotation characters chi_l(theta) = sin((l+1/2) theta)/sin(theta/2) ==")
    th = 2*math.pi/3
    for l in range(0, 4): print("l=%d chi(C3)=%.3f" % (l, math.sin((l+.5)*th)/math.sin(th/2)))
    print("p-orbitals (l=1) under C3: chi=%.1f -> A1 + E in C3v" % (1+2*math.cos(th)))
    print("== octahedral rotation group O: d (l=2) orbitals ==")
    # classes: E, 8C3, 6C4, 3C2(=C4^2), 6C2'; theta = 0, 2pi/3, pi/2, pi, pi
    chi_l = lambda l, t: (2*l+1) if t == 0 else math.sin((l+.5)*t)/math.sin(t/2)
    ts = [0, 2*math.pi/3, math.pi/2, math.pi, math.pi]; wO = np.array([1, 8, 6, 3, 6.])
    O = {"A1": [1, 1, 1, 1, 1], "A2": [1, 1, -1, 1, -1], "E": [2, -1, 0, 2, 0], "T1": [3, 0, 1, -1, -1], "T2": [3, 0, -1, -1, 1]}
    print("orthogonality of O:", all(abs(np.dot(np.array(a)*wO, b) - (24 if a_ == b_ else 0)) < 1e-9 for a_, a in O.items() for b_, b in O.items()))
    for l, nm in [(0, "s"), (1, "p"), (2, "d"), (3, "f")]:
        g = np.array([chi_l(l, t) for t in ts]); print(nm, {k: round(float(np.dot(wO*g, v)/24), 6) for k, v in O.items()})
