"""Checks for GT03, GT04, GT06-GT09 and the Advanced chapters.   .venv/bin/python -W ignore scripts/gt_numbers2.py"""
import itertools, math
from collections import Counter
from gt_numbers import compose, inv, order, generate, cycle_type, is_subgroup, conj_classes

def perm_closure_subgroups(G, n, maxgens=2):
    subs = set()
    els = sorted(G)
    for r in range(1, maxgens + 1):
        for gens in itertools.combinations(els, r):
            subs.add(frozenset(generate(list(gens), n)))
    return subs
def commutator(a, b): return compose(compose(inv(a), inv(b)), compose(a, b))
def derived(G, n): return generate([commutator(a, b) for a in G for b in G], n)
def center(G): return {z for z in G if all(compose(z, g) == compose(g, z) for g in G)}
def sym(n): return set(itertools.permutations(range(n)))
def alt(n): return {p for p in sym(n) if sum(1 for i in range(n) for j in range(i+1, n) if p[i] > p[j]) % 2 == 0}
def normaliser(H, G): return {g for g in G if {compose(compose(g, h), inv(g)) for h in H} == set(H)}
def centraliser(H, G): return {g for g in G if all(compose(g, h) == compose(h, g) for h in H)}
def is_normal(H, G): return all(compose(compose(g, h), inv(g)) in H for g in G for h in H)

if __name__ == "__main__":
    print("== GT03: cyclic groups ==")
    n = 12; print("  C12: elements of order d:", {d: sum(1 for k in range(n) if n // math.gcd(k, n) == d) for d in (1, 2, 3, 4, 6, 12)}, " phi sum", sum(math.gcd(k, 12) == 1 for k in range(12)))
    print("  sum_{d|n} phi(d) = n for n=36:", sum(sum(1 for k in range(1, d+1) if math.gcd(k, d) == 1) for d in range(1, 37) if 36 % d == 0))
    print("== structure theorem: #x with x^2=1 in C8, C4xC2, C2^3 ==")
    def cnt(mods, p): return sum(1 for t in itertools.product(*[range(m) for m in mods]) if all((p*x) % m == 0 for x, m in zip(t, mods)))
    for mods in ([8], [4, 2], [2, 2, 2]): print("   ", mods, [cnt(mods, p) for p in (2, 4, 8)])
    def partitions(k, m=None):
        m = m or k
        if k == 0: yield (); return
        for i in range(min(k, m), 0, -1):
            for rest in partitions(k - i, i): yield (i,) + rest
    for N, fac in [(72, {2: 3, 3: 2}), (36, {2: 2, 3: 2}), (16, {2: 4}), (1000, {2: 3, 5: 3})]:
        c = 1
        for e in fac.values(): c *= len(list(partitions(e)))
        print(f"  abelian groups of order {N}:", c)
    print("== Aut(C_n) = (Z/n)^x ==")
    for n in (6, 8, 10, 12):
        auts = [k for k in range(1, n) if math.gcd(k, n) == 1]; print(f"  |Aut(C{n})| = {len(auts)}  (phi); group (Z/{n})^x cyclic? {any(all(pow(g, e, n) != 1 for e in range(1, len(auts))) and pow(g, len(auts), n) == 1 for g in auts)}")
    V4 = {(0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0)}
    print("  |Aut(V4)| =", sum(1 for im in itertools.permutations(sorted(V4 - {(0,1,2,3)})) if all(compose(im[i], im[j]) == (0,1,2,3) if i == j else True for i in range(3) for j in range(3))), "(= |S3| = 6)")
    p = 13; print(f"  (Z/{p})^x cyclic of order {p-1}: element orders", Counter(len({pow(g, k, p) for k in range(p-1)}) for g in range(1, p)))
    print("== GT04: derived series ==")
    S4 = sym(4); A4 = alt(4); D1 = derived(S4, 4); D2 = derived(D1, 4); D3 = derived(D2, 4)
    print("  S4 > S4' > S4'' > S4''' orders:", len(S4), len(D1), len(D2), len(D3), "(24, 12, 4, 1)")
    A5 = alt(5); print("  A5' =", len(derived(A5, 5)), "(perfect); S5' =", len(derived(sym(5), 5)), "; S3' =", len(derived(sym(3), 3)))
    print("== A_n simple proof: normal closure of any non-identity element of A5, A6 is everything ==")
    for n in (5, 6):
        An = alt(n); e = tuple(range(n)); ok = True
        for s in An:
            if s == e: continue
            cl = generate([compose(compose(g, s), inv(g)) for g in An], n)
            if len(cl) != len(An): ok = False; break
        print(f"  A{n}: all normal closures = A{n}:", ok)
    print("  3-cycles in A5 (all conjugate in A5):", [len(c) for c in conj_classes(A5) if cycle_type(next(iter(c))) == (3, 1, 1)])
    print("== commutator computations used in the proof (cases) ==")
    def cyc(*pts, n=8):
        p = list(range(n))
        for i in range(len(pts)): p[pts[i]] = pts[(i+1) % len(pts)]
        return tuple(p)
    a1, a2, a3, a4, a5, a6 = 0, 1, 2, 3, 4, 5
    comm = lambda s, r: compose(compose(s, r), compose(inv(s), inv(r)))
    s = cyc(a1, a2, a3, a4); r = cyc(a1, a2, a3); print("  case1 [sigma,rho] = (a1 a4 a2)?", comm(s, r) == cyc(a1, a4, a2))
    s = compose(cyc(a1, a2, a3), cyc(a4, a5, a6)); r = cyc(a1, a2, a4); print("  case2 [sigma,rho] = (a1 a4 a3 a5 a2)?", comm(s, r) == cyc(a1, a4, a3, a5, a2))
    s = cyc(a1, a2, a3); print("  case3 sigma^2 = (a1 a3 a2)?", compose(s, s) == cyc(a1, a3, a2))
    s = compose(cyc(a1, a2), cyc(a3, a4)); r = cyc(a1, a2, a3); c = comm(s, r); print("  case4 [sigma,rho] = (a1 a3)(a2 a4)?", c == compose(cyc(a1, a3), cyc(a2, a4)))
    psi = cyc(a1, a3, a5); c2 = compose(compose(psi, c), inv(psi)); print("       c * psi c psi^-1 = (a1 a3 a5)?", compose(c, c2) == cyc(a1, a3, a5))
    print("== composition series factors ==")
    print("  S4: orders of the chain 1<Z2<V4<A4<S4: 1,2,4,12,24 -> factors 2,2,3,2")
    print("== GT06: permutation groups ==")
    D4 = generate([(1,2,3,0),(0,3,2,1)], 4)
    print("  D4 on square vertices: transitive:", len({g[0] for g in D4}) == 4, "; block system {0,2},{1,3} preserved:", all({g[0], g[2]} in ({0,2},{1,3}) for g in D4))
    for nm, G, n in [("S4", sym(4), 4), ("A4", alt(4), 4), ("S5", sym(5), 5), ("A5", alt(5), 5)]:
        k2 = len({(g[0], g[1]) for g in G}); print(f"  {nm} on {n} points: pairs reached {k2} of {n*(n-1)} -> 2-transitive: {k2 == n*(n-1)}", end="; ")
        k3 = len({(g[0], g[1], g[2]) for g in G}); print(f"triples {k3} of {n*(n-1)*(n-2)}")
    print("  Frobenius groups: S3 on 3 points, A4 on 4 points, F20 = C5 x| C4 on 5 points")
    def frob(G, n):
        fixed = {g: sum(1 for i in range(n) if g[i] == i) for g in G}
        ok = all(fixed[g] <= 1 for g in G if g != tuple(range(n))); K = {g for g in G if fixed[g] == 0} | {tuple(range(n))}
        return ok, len(K), is_subgroup(K, G)
    print("   S3:", frob(sym(3), 3), " A4:", frob(alt(4), 4))
    F20 = generate([(1,2,3,4,0), (0,2,4,1,3)], 5); print("   F20: order", len(F20), frob(F20, 5), "(order 20, kernel 5)")
    print("   S4 on 4 points is NOT Frobenius:", frob(sym(4), 4))
    # primitivity: stabiliser maximal
    def maximal(H, G):
        subs = perm_closure_subgroups(G, len(next(iter(G))), 2)
        return not any(set(H) < s < set(G) for s in subs)
    S4 = sym(4); stab = {g for g in S4 if g[0] == 0}
    print("  S4: point stabiliser S3 is maximal (primitive):", maximal(stab, S4))
    D4stab = {g for g in D4 if g[0] == 0}; print("  D4: point stabiliser maximal?", maximal(D4stab, D4), "(False: imprimitive)")
    print("== wreath products ==")
    print("  |C2 wr C2| = 2^2 * 2 = 8; |S2 wr S2| =", 2**2*2, "= Sylow 2 of S4 (8): D4 == S2 wr S2:", len(D4) == 8)
    print("  |S3 wr S2| =", 6**2*2, "= stabiliser of a 3+3 partition in S6 (72); |S2 wr S3| =", 2**3*6, " in S6; p=3: |C3 wr C3| =", 3**3*3, "= Sylow 3 of S9 (3^4=81)")
    print("  v_3(9!) =", sum(9 // 3**k for k in range(1, 3)), " (=4)")
    print("== GT07: nilpotent groups, upper central series ==")
    def ucs(G, n):
        Z = {tuple(range(n))}; chain = [len(Z)]
        while True:
            Zn = {g for g in G if all(commutator(g, h) in Z for h in G)}
            if len(Zn) == len(Z): break
            Z = Zn; chain.append(len(Z))
            if len(Z) == len(G): break
        return chain
    D8 = generate([(1,2,3,4,5,6,7,0), (0,7,6,5,4,3,2,1)], 8)
    Q8 = None
    print("  D4 (order 8) upper central series orders:", ucs(D4, 4), " D8 (order 16):", ucs(D8, 8), " S3:", ucs(sym(3), 3), " A4:", ucs(alt(4), 4), " S4:", ucs(S4, 4))
    # element order statistics: D4 vs Q8 (Q8 as permutations on 8 points)
    i = (1,0,3,2,5,4,7,6); # build Q8 via regular rep: elements 1,i,j,k,-1,-i,-j,-k
    names = ["1","i","j","k","-1","-i","-j","-k"]
    def qmul(a, b):
        sa = -1 if a.startswith("-") else 1; sb = -1 if b.startswith("-") else 1; a = a.lstrip("-"); b = b.lstrip("-")
        tab = {("1","1"):"1",("1","i"):"i",("1","j"):"j",("1","k"):"k",("i","1"):"i",("j","1"):"j",("k","1"):"k",("i","i"):"-1",("j","j"):"-1",("k","k"):"-1",
               ("i","j"):"k",("j","k"):"i",("k","i"):"j",("j","i"):"-k",("k","j"):"-i",("i","k"):"-j"}
        r = tab[(a, b)]; s = sa*sb*(-1 if r.startswith("-") else 1); r = r.lstrip("-"); return ("-" if s == -1 else "") + r
    def qperm(g): return tuple(names.index(qmul(g, h)) for h in names)
    Q8 = {qperm(g) for g in names}; print("  Q8 order", len(Q8), "element orders", sorted(Counter(order(p, tuple(range(8))) for p in Q8).items()), " D4:", sorted(Counter(order(p, tuple(range(4))) for p in D4).items()))
    print("  Q8 upper central series:", ucs(Q8, 8))
    print("  Fitting subgroup F(S4) = V4? centraliser of V4 in S4 =", len(centraliser({(0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0)}, S4)))
    print("  Frattini: D4 maximal subgroups intersect in:", len(set.intersection(*[set(s) for s in perm_closure_subgroups(D4, 4, 2) if len(s) == 4])))
    print("  groups of order 8 by element orders: C8, C4xC2, C2^3, D4, Q8 -> 5")
    print("== GT08: solvable, semidirect products ==")
    def mkgroup(mul, elems): return mul, elems
    def orders_of(elems, mul, e):
        out = Counter()
        for g in elems:
            k, x = 1, g
            while x != e: x = mul(g, x); k += 1
            out[k] += 1
        return dict(sorted(out.items()))
    C12 = orders_of(range(12), lambda a, b: (a+b) % 12, 0)
    C6C2 = orders_of([(a, b) for a in range(6) for b in range(2)], lambda x, y: ((x[0]+y[0]) % 6, (x[1]+y[1]) % 2), (0, 0))
    A4o = {k: v for k, v in sorted(Counter(order(p, (0,1,2,3)) for p in alt(4)).items())}
    D6 = orders_of([(a, b) for a in range(6) for b in range(2)], lambda x, y: ((x[0] + (-1)**x[1]*y[0]) % 6, (x[1]+y[1]) % 2), (0, 0))
    Dic3 = orders_of([(a, b) for a in range(3) for b in range(4)], lambda x, y: ((x[0] + (-1)**x[1]*y[0]) % 3, (x[1]+y[1]) % 4), (0, 0))
    for nm, o in [("C12", C12), ("C6xC2", C6C2), ("A4", A4o), ("D6", D6), ("Dic3 = C3 x| C4", Dic3)]: print(f"  order-12 group {nm}: {o}")
    print("  all five distinct:", len({tuple(o.items()) for o in (C12, C6C2, A4o, D6, Dic3)}) == 5)
    print("  A4 = V4 x| C3: complements of V4 in A4:", sum(1 for H in perm_closure_subgroups(A4, 4, 1) if len(H) == 3 and not (H & V4 - {(0,1,2,3)})), "(4 Sylow 3-subgroups, all conjugate)")
    print("  Z4 has no complement to {0,2}: elements of order 2 outside {0,2}:", [x for x in range(4) if x not in (0, 2) and (2*x) % 4 == 0])
    print("  S3 = A3 x| C2, S4 = V4 x| S3, D_n = C_n x| C2, F20 = C5 x| C4")
    print("== Schur-Zassenhaus proof: d(T1,T2) cocycle on a small case (N = V4 normal in A4) ==")
    N = V4; cos = {}
    for g in A4: cos.setdefault(frozenset(compose(g, x) for x in N), g)
    reps = list(cos.values())
    import random; random.seed(1)
    def rand_T(): return [random.choice(sorted({compose(r, x) for x in N})) for r in reps]
    def d(T1, T2): 
        r = tuple(range(4))
        for t, u in zip(T1, T2): r = compose(r, compose(t, inv(u)))
        return r
    T1, T2, T3 = rand_T(), rand_T(), rand_T()
    print("  d(T1,T2) d(T2,T3) = d(T1,T3):", compose(d(T1, T2), d(T2, T3)) == d(T1, T3), "; d(T,T) = e:", d(T1, T1) == tuple(range(4)))
    print("  n -> n^m bijective on N when gcd(|N|,m)=1: m=3, |N|=4:", len({compose(x, compose(x, x)) for x in N}) == 4)
    print("  subnormal: <(12)(34)> in S4 subnormal not normal:", is_normal({(0,1,2,3),(1,0,3,2)}, S4), "(False=not normal); V4 normal in S4:", is_normal(V4, S4))
    print("== GT09: transfer ==")
    def transfer(G, H, n, Hder):
        # right cosets H t_i ; V(g) = prod h_i mod H'
        reps = []; seen = set()
        for g in sorted(G):
            c = frozenset(compose(h, g) for h in H)
            if c not in seen: seen.add(c); reps.append(g)
        def coset_index(x):
            for i, t in enumerate(reps):
                if compose(x, inv(t)) in H: return i
        def V(g, T=reps):
            res = []
            for t in T:
                tg = compose(t, g); j = coset_index(tg); h = compose(tg, inv(reps[j] if T is reps else T[j])); res.append(h)
            return res
        return reps, V
    S3 = sym(3); P = {(0,1,2),(1,0,2)}
    reps, V = transfer(S3, P, 3, {(0,1,2)})
    def Vval(g):
        hs = V(g); r = (0,1,2)
        for h in hs: r = compose(r, h)
        return r
    homo = all(Vval(compose(a, b)) == compose(Vval(a), Vval(b)) for a in S3 for b in S3)
    print("  S3 -> P=C2 transfer is a homomorphism:", homo, "; kernel orders:", len([g for g in S3 if Vval(g) == (0,1,2)]), "(kernel = A3, normal 2-complement)")
    A4g = alt(4); reps, V = transfer(A4g, V4, 4, {(0,1,2,3)})
    def VvalA(g):
        hs = V(g); r = (0,1,2,3)
        for h in hs: r = compose(r, h)
        return r
    print("  A4 -> V4 transfer homomorphism:", all(VvalA(compose(a, b)) == compose(VvalA(a), VvalA(b)) for a in A4g for b in A4g), "; image size", len({VvalA(g) for g in A4g}), " (V4 not in the centre of its normaliser: no normal 2-complement)")
    print("  Burnside criterion: P <= Z(N_G(P)):")
    for nm, G, nn, Pp in [("S3, p=2", S3, 3, P), ("A4, p=2", A4g, 4, V4), ("A4, p=3", A4g, 4, generate([(1,2,0,3)], 4)), ("S4, p=3", S4, 4, generate([(1,2,0,3)], 4)), ("S4, p=2", S4, 4, D4)]:
        N_ = normaliser(Pp, G); Zn = center(N_); print(f"   {nm}: |N_G(P)| = {len(N_)}, P <= Z(N_G(P))? {set(Pp) <= Zn}")
    print("  A4 has normal 3-complement (V4)?  A4 p=3: P=C3, N_G(P)=C3, central: normal 3-complement V4 ✓ (Burnside)")
    print("  Cayley: element of order 2 in regular representation of S3 (|G|=6) is a product of 3 transpositions -> odd")
    def regular(G):
        L = sorted(G); return {g: tuple(L.index(compose(g, x)) for x in L) for g in G}
    R = regular(S3); print("   signs of the regular representation of S3 on elements of order 2:", [ (-1) ** sum(1 for i in range(6) for j in range(i+1, 6) if R[g][i] > R[g][j]) for g in S3 if order(g, (0,1,2)) == 2])
    print("== Advanced ==")
    A5 = alt(5); subs = perm_closure_subgroups(A5, 5, 2); print("  subgroup orders of A5:", sorted({len(s) for s in subs}), " -> no Hall {2,5} (order 20) or {3,5} (order 15) subgroup; A5 not solvable")
    print("  F*(S5): O_p(S5) trivial; E(S5) = A5; C_S5(A5) =", len(centraliser(A5, sym(5))))
    print("  maximal subgroups of S4: orders", sorted({len(s) for s in perm_closure_subgroups(S4, 4, 2) if not any(set(s) < set(t) < set(S4) for t in perm_closure_subgroups(S4, 4, 2)) and len(s) < 24}))
