"""CH02-CH09 numbers: every figure and number quoted in the inorganic-chemistry chapters CH02-CH09.

.venv/bin/python -W ignore scripts/ch0209_numbers.py            (prints all sections)
Literature inputs marked  # recalled  are from memory of standard tables (CRC, Pearson 1988, Martell-Smith) and are
flagged [verify] in the chapters.
"""
import itertools
import math

import numpy as np

F = 96485.332      # C/mol
R = 8.314462       # J/(mol K)
T = 298.15
LN10 = math.log(10)


def sec(t):
    print("\n=== " + t + " ===")


# ------------------------------------------------------------------ CH02
def ch02():
    sec("CH02 H2 LCAO: bonding vs antibonding with overlap")
    for S in (0.0, 0.3, 0.7534):
        print(f"S={S:.4f}: antibonding rise / bonding drop = (1+S)/(1-S) = {(1+S)/(1-S):.3f}")
    print("H2 sigma_g: psi+ = (1sA+1sB)/sqrt(2(1+S)), psi- = (1sA-1sB)/sqrt(2(1-S)); at S=0.7534 N+=%.4f N-=%.4f"
          % (1/math.sqrt(2*(1+0.7534)), 1/math.sqrt(2*(1-0.7534))))
    print("midpoint amplitude check: |psi+|^2 at midpoint ~ (2*phi)^2*N+^2 enhanced; interference term 2cAcB chiA chiB > 0 for +")

    sec("CH02 homonuclear diatomics: fill MOs, bond order, unpaired electrons")
    order_B = ["1sg", "1su", "1pu", "2sg", "1pg", "2su"]          # N2-type (s-p mixing) Li2-N2
    order_A = ["1sg", "1su", "2sg", "1pu", "1pg", "2su"]          # O2/F2-type
    cap = {"1sg": 2, "1su": 2, "1pu": 4, "2sg": 2, "1pg": 4, "2su": 2}
    bonding = {"1sg", "1pu", "2sg"}

    def fill(nel, order):
        occ = {}
        left = nel
        for o in order:
            k = min(cap[o], left)
            occ[o] = k
            left -= k
        return occ

    def props(nel, order):
        occ = fill(nel, order)
        nb = sum(v for k, v in occ.items() if k in bonding)
        na = sum(v for k, v in occ.items() if k not in bonding)
        unp = 0
        for o, v in occ.items():
            if cap[o] == 4:
                unp += 2 * v - 4 if v > 2 else v if v <= 2 else 0
                if v > 2:
                    unp = unp  # handled below
        # Hund: degenerate pi pair (cap 4): v electrons -> unpaired = v if v<=2 else 4-v
        unp = 0
        for o, v in occ.items():
            if cap[o] == 4:
                unp += v if v <= 2 else 4 - v
            else:
                unp += v % 2
        return (nb - na) / 2, unp

    rows = [("Li2", 2, order_B), ("Be2", 4, order_B), ("B2", 6, order_B), ("C2", 8, order_B), ("N2", 10, order_B),
            ("O2", 12, order_A), ("F2", 14, order_A), ("Ne2", 16, order_A),
            ("N2+", 9, order_B), ("O2+", 11, order_A), ("O2-", 13, order_A), ("O2 2-", 14, order_A),
            ("NO", 11, order_A), ("CO", 10, order_B), ("CN-", 10, order_B), ("C2 2-", 10, order_B)]
    # valence electrons counted from the 2s,2p shell (core excluded): Li2 uses 1s-like pair, as in the lecture's ladder
    for nm, n, o in rows:
        n_eff = n
        # first-row: Li2/Be2 use 2s: shift labels: 1sg=2sg of the lecture ladder; here treat the lowest two as 2s sigma_g,u
        bo, unp = props(n_eff, o)
        print(f"{nm:5s} valence e={n:2d}  bond order={bo:.1f}  unpaired={unp}")
    print("(NO, CO, CN- use the homonuclear ladder as a first approximation)")

    sec("CH02 s-p mixing: B2 paramagnetic only if pi_u below sigma_g(2p)")
    print("B2 with N2-type order (1pu below 2sg): pi_u^2 -> 2 unpaired (para, observed); with O2-type order: 2sg^2 -> 0 unpaired")
    for nm, n, o in (("B2 N2-type", 6, order_B), ("B2 O2-type", 6, order_A), ("C2 N2-type", 8, order_B), ("C2 O2-type", 8, order_A)):
        bo, unp = props(n, o)
        print(f"{nm}: bond order {bo}, unpaired {unp}")

    sec("CH02 heteronuclear: HF 2x2 secular problem (overlap neglected, beta illustrative)")
    aH, aF, beta = -13.6, -18.65, -3.0   # eV; AO energies recalled (Miessler & Tarr)
    mid = (aH + aF) / 2
    half = abs(aH - aF) / 2
    d = math.sqrt(half ** 2 + beta ** 2)
    Eb, Ea = mid - d, mid + d
    cF2 = 0.5 * (1 + half / d)
    print(f"E_bond={Eb:.2f} eV, E_anti={Ea:.2f} eV, c_F^2 (bonding MO)={cF2:.3f}, c_H^2={1-cF2:.3f}; antibonding: F {1-cF2:.3f}, H {cF2:.3f}")
    print("same beta, equal energies (H2-like): c^2 = 0.5 each")
    print("CO bond enthalpy 1070 vs N2 946 kJ/mol (slide); ratio", round(1070/946, 3))

    sec("CH02 CO/N2 AO energy gaps (eV, recalled)")
    ao = {"C2s": -19.43, "C2p": -10.66, "N2s": -25.56, "N2p": -13.18, "O2s": -32.38, "O2p": -15.85, "F2s": -40.17, "F2p": -18.65, "H1s": -13.61}
    print("O2s-C2s gap", round(ao["O2s"] - ao["C2s"], 2), "| O2p-C2p gap", round(ao["O2p"] - ao["C2p"], 2),
          "| s-p gap C", round(ao["C2s"] - ao["C2p"], 2), "N", round(ao["N2s"] - ao["N2p"], 2),
          "O", round(ao["O2s"] - ao["O2p"], 2), "F", round(ao["F2s"] - ao["F2p"], 2))


# ------------------------------------------------------------------ CH03
def ch03():
    sec("CH03 Hueckel H3: linear and triangular")
    beta = -1.0
    lin = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], float)
    tri = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]], float)
    for nm, M in (("linear", lin), ("triangle", tri)):
        w, v = np.linalg.eigh(M)
        order = np.argsort(-w)  # most bonding first (beta<0 -> E = alpha + w*beta)
        print(nm, "E-alpha in |beta|:", [round(-w[i], 4) for i in order][::-1], "(bonding = most negative)")
        for i in order:
            c = v[:, i]
            c = c / np.sign(c[0] if abs(c[0]) > 1e-9 else 1)
            print("  coeffs", np.round(c, 4), " (E-alpha)/beta =", round(w[i], 4))
    print("slide 41 linear 1sigma = chiA + sqrt2 chiB + chiC  ->  (1, 1.4142, 1)/2 =", np.round(np.array([1, 2 ** .5, 1]) / 2, 4))
    # total pi-like electron energies
    for nm, n_e in (("H3+ (2e)", 2), ("H3 (3e)", 3), ("H3- (4e)", 4)):
        lin_E = sorted([-math.sqrt(2), 0, math.sqrt(2)])   # in |beta|, bonding first
        tri_E = sorted([-2, 1, 1])
        def tot(levels):
            e, left = 0.0, n_e
            for L in levels:
                k = min(2, left)
                e += k * L
                left -= k
                if left == 0:
                    break
            return e
        print(f"{nm}: linear {tot(lin_E):+.3f} |beta|, triangle {tot(tri_E):+.3f} |beta|  (lower = more stable)")

    sec("CH03 NH3: orbital count, electron fill, PES")
    print("N: 2s(a1), 2pz(a1), 2px,2py(e); H3 LGOs: a1 + e. Six AOs-ish basis -> 7 MOs: 1a1, 2a1, 3a1, 1e (x2), 2e (x2). 8 valence electrons: 1a1^2 1e^4 2a1^2 -> 4 occupied levels.")
    print("PES (21.2 eV He I): bands at ~11 eV (2a1, lone pair) and ~16 eV (1e); 1a1 ~27 eV out of range: 21.2 - 27 < 0")
    print("N-H bond order from MO count: bonding electrons 1a1^2 + 1e^4 = 6 over 3 bonds -> 1 each; lone pair 2a1 nearly nonbonding")

    sec("CH03 SF6: LGO count and electron book-keeping")
    print("LGOs of 6 F sigma: a1g + eg + t1u (dimension 1+2+3=6). S 3s -> a1g, 3p -> t1u, eg: S d (not used in the lecture) -> nonbonding.")
    print("MOs: 1a1g 1t1u (bonding) 1eg (nonbonding, F-centred) then 2a1g, 2t1u, antibonding. 12 e = 2+6+4")
    bonding_e = 2 + 6
    print(f"bonding electrons {bonding_e} -> pairs {bonding_e//2} for 6 S-F bonds -> S-F bond order {bonding_e/2/6:.3f}")
    print("Valence count: S 6 + 6 F x 1 = 12; Lewis octet-expanded would put 12 e in 6 bonds (order 1).")

    sec("CH03 H2O: C2v reduction and orbital ordering")
    chars = {"A1": (1, 1, 1, 1), "A2": (1, 1, -1, -1), "B1": (1, -1, 1, -1), "B2": (1, -1, -1, 1)}
    # operations E, C2, sigma(xz), sigma'(yz); molecule in xz plane (slide 47-48)
    # H 1s pair: E:2, C2:0, sigma(xz):2, sigma'(yz):0
    gam = (2, 0, 2, 0)
    for k, ch in chars.items():
        n = sum(a * b for a, b in zip(gam, ch)) / 4
        print(f"  n({k}) = {n:.2f}")
    print("-> Gamma(H1s) = A1 + B1.  O: 2s A1, 2pz A1, 2px B1 (in plane), 2py B2 (out of plane).")
    print("MOs: 2a1 (O2s+LGO a1), 1b1 (px + LGO b1), 3a1 (pz + s + LGO a1), 1b2 (py nonbonding), 4a1*, 2b1*. 8 e -> 2a1^2 1b1^2 3a1^2 1b2^2")
    print("Vertical IEs (eV, recalled): 1b2 12.6, 3a1 14.7, 1b1 18.6, 2a1 32.2")
    print("O-H bond order: bonding electrons 2a1^2+1b1^2+(3a1 part) ~ 4-6 over 2 bonds; two lone pairs: 1b2 (pure p) and 3a1 (s-p hybrid-like)")
    print("two different lone pairs: 12.6 vs 14.7 eV; the 'rabbit-ear' equivalent lone pairs of VSEPR are a mixture of 3a1 and 1b2: PES shows two bands")


# ------------------------------------------------------------------ CH04 / CH05
def ch04():
    sec("CH04 water autoprotolysis (slide 56 table)")
    data = [(0, 0.112), (25, 1.023), (50, 5.495), (75, 19.95), (100, 56.23)]
    for t, k in data:
        pkw = -math.log10(k * 1e-14)
        print(f"{t:3d} C  Kw={k}e-14  pKw={pkw:.2f}  neutral pH={pkw/2:.2f}")
    print("van't Hoff slope: d(ln Kw)/d(1/T) -> dH =", end=" ")
    ts = np.array([t + 273.15 for t, _ in data])
    ks = np.array([k * 1e-14 for _, k in data])
    sl = np.polyfit(1 / ts, np.log(ks), 1)[0]
    print(f"{-sl*R/1000:.1f} kJ/mol (literature ~ 55.8)")
    print("1 in 1e7 molecules ionised: [H3O+] = 1e-7 M = 1e-7/55.5 = %.2e fraction" % (1e-7 / 55.5))
    print("so about 1 in %.1e water molecules (slide says 1 in 10^7: it is 1 in 5.5e8)" % (55.5 / 1e-7))
    sec("CH04 conjugate pairs: pKa + pKb = pKw")
    for nm, pka in (("NH4+", 9.25), ("CH3COOH", 4.76), ("HF", 3.17), ("HCN", 9.21)):
        print(f"{nm}: pKa {pka}  conjugate base pKb {14 - pka:.2f}")
    sec("CH04 Lux-Flood/solvent system")
    print("Solvent system: 2 H2O <-> H3O+ + OH-; 2 NH3 <-> NH4+ + NH2- (pK ~ 27-33 at -50 C?); 2 BrF3 <-> BrF2+ + BrF4-")


def ch05():
    sec("CH05 Pauling's rules for oxo acids: pKa ~ 8 - 5n, n = non-protonated O")
    acids = [("HOCl", 0, 7.5), ("H3BO3", 0, 9.2), ("HClO2", 1, 1.96), ("H3PO4", 1, 2.15), ("H3PO3", 1, 1.3), ("H2CO3(true)", 1, 3.6),
             ("HNO3", 2, -1.4), ("HClO3", 2, -1.0), ("H2SO4", 2, -3.0), ("HClO4", 3, -8.0), ("HNO2", 1, 3.3), ("HIO4", 3, -1)]
    for nm, n, pka in acids:
        print(f"{nm:12s} n={n}  rule {8-5*n:+d}  observed {pka:+.2f}  diff {pka-(8-5*n):+.1f}")
    print("successive pKa step ~ +5: H3PO4 2.15, 7.20, 12.35 -> steps", round(7.20 - 2.15, 2), round(12.35 - 7.20, 2))
    print("H3PO3 = HP(O)(OH)2: n=1 -> predicted 3 (obs 1.3, 6.7); two acidic H only, third H on P; H3PO2 = H2P(O)OH: monoprotic pKa 1.2")

    sec("CH05 inductive effect: chloroacetic acids")
    ca = [("CH3COOH", 4.76), ("ClCH2COOH", 2.86), ("Cl2CHCOOH", 1.29), ("Cl3CCOOH", 0.65)]
    for i, (nm, p) in enumerate(ca):
        print(f"{nm}: pKa {p}  Ka={10**-p:.3g}  (x{10**(ca[0][1]-p):.0f} vs acetic)")
    print("average drop per Cl: %.2f pKa units" % ((4.76 - 0.65) / 3))

    sec("CH05 aqua acids: pKa vs Z^2/r (Shannon CN6 radii pm, recalled)")
    ions = [("Na+", 1, 102, 14.2), ("Mg2+", 2, 72, 11.4), ("Zn2+", 2, 74, 9.0), ("Fe2+", 2, 78, 9.5), ("Cu2+", 2, 73, 7.5),
            ("Al3+", 3, 53.5, 5.0), ("Cr3+", 3, 61.5, 4.0), ("Fe3+", 3, 64.5, 2.2), ("Hg2+", 2, 102, 3.4)]
    x = np.array([z * z / r * 100 for _, z, r, _ in ions[:-1]])
    y = np.array([p for *_, p in ions[:-1]])
    m, c = np.polyfit(x, y, 1)
    r_ = np.corrcoef(x, y)[0, 1]
    print(f"fit pKa = {c:.2f} {m:+.4f} (Z^2/r in 100/pm), r = {r_:.3f}, excluding Hg2+")
    for nm, z, r, p in ions:
        print(f"{nm:5s} Z^2/r={z*z/r*100:6.2f}  pKa obs {p:5.1f}  fit {c+m*z*z/r*100:5.1f}")
    print("Hg2+ (r=102 pm) obs 3.4 vs fit", round(c + m * 4 / 102 * 100, 1), "-> covalency makes it far more acidic (slide: 'with increasing covalency aqua acids increase in strength')")

    sec("CH05 BX3 acidity: B-X pi back-donation (qualitative) and numbers")
    print("B-F bond 1.31 A (BF3) vs sum of single-bond radii 1.52 A -> shortening ~0.2 A = pi bonding (recalled)")
    print("BF3 + NMe3 ... ordering of adduct stability BF3 < BCl3 < BBr3 (slide 72)")
    sec("CH05 SiX4 and Lewis acid reactions")
    print("SiF4 + 2HF -> [SiF6]2- + 2H+: Si CN 4 -> 6; fluoride affinity; glass etching SiO2 + 4HF -> SiF4 + 2H2O")
    print("I2 + I- <-> I3- (K ~ 700 in water at 298 K, recalled): fraction I3- at [I-]=0.1 M ->", round(700 * 0.1 / (1 + 700 * 0.1), 3))


# ------------------------------------------------------------------ CH06
def ch06():
    sec("CH06 Pearson absolute hardness eta=(I-A)/2 from ionisation energies (eV, CRC/NIST)")
    # (species, I_next (eV, of the acceptor ion), I_prev) ; acid M^(n+): eta = (I_{n+1} - I_n)/2
    cat = [("Al3+", 119.99, 28.45), ("Li+", 75.64, 5.392), ("Mg2+", 80.14, 15.035), ("Na+", 47.286, 5.139), ("Ca2+", 50.91, 11.872),
           ("K+", 31.63, 4.341), ("Fe3+", 54.8, 30.65), ("Zn2+", 39.72, 17.96), ("Fe2+", 30.65, 16.19), ("Hg2+", 34.2, 18.76),
           ("Ag+", 21.48, 7.576), ("Cu+", 20.29, 7.726), ("Au+", 20.5, 9.226)]
    out = []
    for nm, i2, i1 in cat:
        out.append((nm, (i2 - i1) / 2))
    out.sort(key=lambda t: -t[1])
    for nm, e in out:
        print(f"{nm:5s} eta = {e:5.1f} eV")
    print("halogen atoms as bases (I, A in eV): eta=(I-A)/2, chi=(I+A)/2")
    hal = {"F": (17.4228, 3.4012), "Cl": (12.9676, 3.6127), "Br": (11.8138, 3.3636), "I": (10.4513, 3.0590)}
    for k, (i, a) in hal.items():
        print(f"{k}: eta={(i-a)/2:.2f}  chi={(i+a)/2:.2f}  softness 1/(2 eta)={1/(i-a):.3f} eV^-1")
    print("Pearson: electron transfer between A and B: dN = (chi_A - chi_B)/(2(eta_A+eta_B)); energy lowering dE = -(chi_A - chi_B)^2/(4(eta_A+eta_B))")
    # example Ag+ with I- vs F-: use Mulliken for ion acid: chi_Ag+ = (I2+I1)/2? as acid: chi=(21.48+7.576)/2
    chiAg = (21.48 + 7.576) / 2
    etaAg = (21.48 - 7.576) / 2
    for k in ("F", "I"):
        i, a = hal[k]
        chiB, etaB = (i + a) / 2, (i - a) / 2
        dN = (chiAg - chiB) / (2 * (etaAg + etaB))
        dE = -(chiAg - chiB) ** 2 / (4 * (etaAg + etaB))
        print(f"Ag+ + {k}-(as atom): dN={dN:+.3f}, dE={dE:.2f} eV")
    chiAl = (119.99 + 28.45) / 2
    etaAl = (119.99 - 28.45) / 2
    for k in ("F", "I"):
        i, a = hal[k]
        chiB, etaB = (i + a) / 2, (i - a) / 2
        dN = (chiAl - chiB) / (2 * (etaAl + etaB))
        print(f"Al3+ + {k}: dN={dN:+.3f}  (small transfer = ionic bond; hard-hard)")
    sec("CH06 Kf data (log K1, 298 K, recalled)")
    for ion, d in {"Fe3+": dict(F=6.04, Cl=1.48, Br=0.6, I=None), "Hg2+": dict(F=1.03, Cl=6.74, Br=8.94, I=12.87), "Ag+": dict(F=-0.4, Cl=3.0, Br=4.3, I=6.6)}.items():
        print(ion, d)
    sec("CH06 hard-hard: Madelung/Coulomb energy for ion pairs (kJ/mol): E = -N_A e^2/(4 pi eps0 d) * z1 z2")
    ke = 1389.35   # kJ mol^-1 A (e^2/(4 pi eps0) N_A)
    for nm, z, rc, ra in (("LiF", 1, 0.76, 1.33), ("NaI", 1, 1.02, 2.20), ("AgI", 1, 1.15, 2.20), ("AgF", 1, 1.15, 1.33), ("MgO", 2, 0.72, 1.40)):
        d = rc + ra
        print(f"{nm}: d={d:.2f} A  Coulomb pair energy {-ke*z*z/d:.0f} kJ/mol")
    sec("CH06 Goldschmidt: oxide vs sulfide formation")
    print("2 CuS vs CuO etc. not computed; lithophile Al: Al2O3 dG_f -1582 kJ/mol; chalcophile Hg: HgS dGf -50.6 vs HgO -58.5 (recalled)")


# ------------------------------------------------------------------ CH07
def wade(formula_elements, extra_H=0, charge=0, n_vertices=None, ligand_atoms=None):
    raise NotImplementedError


def ch07():
    sec("CH07 Wade/Mingos counting")
    # borane BnHm^q-: skeletal pairs = (2n + (m-n) - q)/2  where q = anionic charge; each BH gives 2, each extra H gives 1
    def borane(n, m, q=0):
        sk_e = 2 * n + (m - n) + q          # q = anionic charge (positive = extra electrons)
        pairs = sk_e / 2
        d = pairs - n
        cls = {1: "closo", 2: "nido", 3: "arachno", 4: "hypho"}.get(d, "?")
        return pairs, d, cls
    for nm, n, m, q in (("B6H6 2-", 6, 6, 2), ("B12H12 2-", 12, 12, 2), ("B2H6", 2, 6, 0), ("B5H9", 5, 9, 0), ("B10H14", 10, 14, 0),
                        ("B4H10", 4, 10, 0), ("B5H11", 5, 11, 0), ("B6H10", 6, 10, 0), ("B5H12 -", 5, 12, 1), ("B5H13", 5, 13, 0),
                        ("B4H4", 4, 4, 0), ("B5H5 2-", 5, 5, 2), ("B10H10 2-", 10, 10, 2), ("B11H11 2-", 11, 11, 2), ("B3H8 -", 3, 8, 1)):
        p, d, c = borane(n, m, q)
        print(f"{nm:10s} n={n:2d} skeletal pairs {p:5.1f} = n+{d:+.1f} -> {c}")
    sec("CH07 Zintl: g - 2n")
    zint = [("Sn5 2-", 5, 4, 2), ("Bi5 3+", 5, 5, -3), ("Sn6 2-", 6, 4, 2), ("Sn9 4-", 9, 4, 4), ("Bi9 5+", 9, 5, -5), ("Bi8 2+", 8, 5, -2),
            ("Pb5 2-", 5, 4, 2), ("Ge9 4-", 9, 4, 4), ("Sn9 3-", 9, 4, 3), ("Sb4 2-?", 4, 5, 2)]
    for nm, n, v, q in zint:
        g = n * v + q
        sk = g - 2 * n
        pairs = sk / 2
        d = pairs - n
        print(f"{nm:8s} g={g:3d}  g-2n={sk:3d}  pairs={pairs:5.1f} -> n+{d:+.1f}  "
              + {1: "closo", 2: "nido", 3: "arachno", 4: "hypho"}.get(round(d, 3), "(not a Wade count)" if d not in (1, 2, 3, 4) else ""))
    print("As2B4Cl4: B atoms carry Cl (1 e per B-Cl), As atoms lone pair: g=2*5+4*3+4*1=26 ; g-2n=14 =2n+2 closo")

    sec("CH07 deltahedra: faces/edges/vertices (Euler V - E + F = 2) and triangulated sphere: E=3V-6, F=2V-4")
    names = {4: "tetrahedron", 5: "trigonal bipyramid", 6: "octahedron", 7: "pentagonal bipyramid", 8: "dodecahedron(bisdisphenoid)",
             9: "tricapped trigonal prism", 10: "bicapped square antiprism", 11: "octadecahedron", 12: "icosahedron"}
    for v, nm in names.items():
        print(f"n={v:2d} {nm:28s} E={3*v-6:2d} F={2*v-4:2d}  closo pairs {v+1}  nido {v+2}(n-1 cage)  B_nH_n^2-")
    print("nido B5H9 = octahedron minus 1 vertex: square pyramid, 4 basal B-H-B bridges (+4 H) -> BnHn+4: 5 BH (10e)+4 H = 14 e = 7 pairs = n+2 OK")

    sec("CH07 diborane geometry check")
    d, ang = 1.31, 83.0
    bb = 2 * d * math.sin(math.radians(ang / 2))
    print(f"B...B = 2 x 1.31 x sin(41.5 deg) = {bb:.3f} A (exp 1.77);  H_b-B-H_b = 360/2 - 83 = {180-83} deg; sum of rhombus angles {2*(97+83)}")
    print("12 valence e: 8 e in 4 terminal 2c-2e B-H; 4 e in 2 bridge 3c-2e; each bridge B-H bond order 1/2")
    print("Hueckel 3-centre: [[a_B, b, 0],[b, a_H, b],[0, b, a_B]] with a_B=a_H=0:")
    w = np.linalg.eigvalsh(np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], float))
    print("  levels (in b):", np.round(w, 4), "bonding -sqrt2 |b| for 2 e: stabilisation = 2 x 1.414 |b| = 2.83 |b| vs one 2c-2e B-H pair 2|b|")
    print("  two 2c-2e B-H bonds (4 e) would need 4 e... here 2 e hold both bonds: electron-deficient bonding")

    sec("CH07 phosphorus cages: formulas, masses, mass fractions")
    mP, mO, mS = 30.9738, 15.999, 32.06
    for nm, (np_, no, ns) in {"P4": (4, 0, 0), "P4O6": (4, 6, 0), "P4O10": (4, 10, 0), "P4S3": (4, 0, 3), "P4S10": (4, 0, 10)}.items():
        M = np_ * mP + no * mO + ns * mS
        print(f"{nm:6s} M={M:7.2f} g/mol  P fraction={np_*mP/M*100:5.1f}%")
    print("P4: 6 P-P edges, P-P-P 60 deg vs 109.5 (p-orbital angle 90): strain ~ 6 x ... ; P4O6: P4 tetrahedron with 6 O inserted on edges: 10 atoms adamantane-like; P4O10: +4 terminal P=O")
    print("P4 + 3 O2 -> P4O6;  P4O6 + 2 O2 -> P4O10;  P4O10 + 6 H2O -> 4 H3PO4;  P4O6 + 6 H2O -> 4 H3PO3")
    print("mass of H3PO4 from 1 g P4O10: ", round(4 * 97.994 / 283.89, 4), "g")
    print("Ca3(PO4)2 route (slide 104): 2 Ca3(PO4)2 + 6 SiO2 + 10 C -> P4 + 10 CO + 6 CaSiO3 ; atoms check P:4=4, Ca:6=6, Si:6=6, O:16+12=28 vs 10+18=28, C 10=10")


# ------------------------------------------------------------------ CH08
def ch08():
    sec("CH08 Hueckel pi: benzene vs borazine")
    def run(hB, hN, kBN, nm):
        n = 6
        H = np.zeros((n, n))
        sites = ["B", "N"] * 3
        for i in range(n):
            H[i, i] = hB if sites[i] == "B" else hN
        for i in range(n):
            j = (i + 1) % n
            H[i, j] = H[j, i] = kBN
        # energies E = alpha + x beta, beta < 0: more positive x = more bonding
        w, v = np.linalg.eigh(H)
        idx = np.argsort(-w)            # most bonding first
        w, v = w[idx], v[:, idx]
        nocc = 3 if nm.startswith("benzene") else 3          # 6 pi electrons -> 3 occupied MOs
        q = 2 * (v[:, :nocc] ** 2).sum(axis=1)
        P = np.zeros((n, n))
        for i in range(n):
            j = (i + 1) % n
            P[i, j] = 2 * (v[i, :nocc] * v[j, :nocc]).sum()
        gap = w[nocc - 1] - w[nocc]
        return w, q, P, gap
    w, q, P, gap = run(0, 0, 1, "benzene")
    print("benzene x levels:", np.round(w, 3), " HOMO-LUMO gap (|beta|):", round(gap, 3), " pi bond order", round(P[0, 1], 3), " pi charge", np.round(q, 2))
    for hB, hN, k in ((-1.0, 1.5, 0.8), (-0.5, 1.0, 0.9), (-1.0, 2.0, 0.8)):
        w2, q2, P2, g2 = run(hB, hN, k, "borazine")
        print(f"borazine (hB={hB}, hN={hN}, k={k}): levels {np.round(w2,3)}  gap {g2:.3f}|beta|  pi bond orders {np.round([P2[i,(i+1)%6] for i in range(6)],3)}  pi charge B {q2[0]:.2f}, N {q2[1]:.2f}")
    print("borazine's larger HOMO-LUMO gap -> colourless, chemically more reactive?  (polar B-N pi: attack at B by nucleophiles)")
    sec("CH08 bond length / order (Pauling): d(n) = d(1) - c log10 n")
    d1, d2, dobs = 1.51, 1.31, 1.436
    lin = (d1 - dobs) / (d1 - d2)
    print(f"linear interpolation: fractional double-bond character {lin:.2f} -> bond order {1+lin:.2f}")
    for c in (0.60, 0.71):
        n = 10 ** ((d1 - dobs) / c)
        print(f"Pauling c={c}: bond order {n:.2f}")
    print("c from the two end points: c = (1.51-1.31)/log10(2) =", round((d1 - d2) / math.log10(2), 3))
    c = (d1 - d2) / math.log10(2)
    print("   then 1.436 -> n =", round(10 ** ((d1 - dobs) / c), 3), " (ideal 6 e delocalised would give pi order 1/3 per B-N if equal sharing: n=1.33)")
    sec("CH08 slide data check: benzene C-C")
    print("benzene C-C = 1.397 A (slide says 1.42 A, graphite value: flag). B-N 1.436 A (borazine, exp 1.44).")
    sec("CH08 rings: counting electrons for ring-pi systems")
    print("B3N3H6: 6 pi e (from 3 N lone pairs); 6 atoms -> 4n+2 with n=1")
    print("(NPCl2)3: 3 N (1 pi e each? or 2) and 3 P: all P-N 1.58 A equal (recalled) vs single P-N 1.77 A")
    print("S4N4: 8-atom cage, 'cradle'; S8: crown ring, S-S 2.05 A, angle 108 deg, dihedral 98 deg")
    print("Dewar island: pi systems over N-P-N: 3 three-centre bonds; Craig: d-orbital stabilised 'homomorphic' delocalisation")
    sec("CH08 polymer mass: polyaminoborazylene Mw 7600")
    unit = 3 * 10.811 + 3 * 14.007 + 4 * 1.008      # (B3N3H4) repeating unit if two H lost per borazine ring
    print(f"B3N3H4 unit mass {unit:.2f}; Mw 7600 -> about {7600/unit:.0f} borazine units; BN formula mass {10.811+14.007:.3f}")
    sec("CH08 polyphosphazene: ring-opening of (NPCl2)3")
    print("N3P3Cl6 M =", round(3 * 14.007 + 3 * 30.974 + 6 * 35.45, 2), "g/mol; polymer (NPCl2)n repeat 115.9; Mw 1e6 -> n ~", int(1e6 / 115.86))
    print("Substitution: P3N3Cl6 + 6 RONa -> P3N3(OR)6 + 6 NaCl. Tutorial 9: with NaF/MeCN: P3N3F6 (halide exchange)")


# ------------------------------------------------------------------ CH09
def ch09():
    sec("CH09 E degrees and K, DG")
    for E in (0.1, 0.5, 1.0, 1.10, 2.0):
        lg = 1 * F * E / (R * T * LN10)
        print(f"E={E:.2f} V, nu=1: log10K={lg:6.2f}, DG={-F*E/1000:8.1f} kJ/mol")
    print("RT/F =", round(R * T / F * 1000, 3), "mV; (RT/F) ln10 =", round(R * T / F * LN10 * 1000, 2), "mV per decade")
    print("Cu-Zn cell: E=0.34-(-0.76)=1.10 V, nu=2: DG =", round(-2 * F * 1.10 / 1000, 1), "kJ/mol; log K =", round(2 * F * 1.10 / (R * T * LN10), 2))
    print("Zn2+/Zn from DG=-147: E =", round(-147000 / (2 * F), 3), "V")
    print("H2/O2 cell: DfG(H2O,l) = -237.13 -> E =", round(237130 / (2 * F), 3), "V (nu=2 for H2 + 1/2 O2)")
    print("range -2 to 2 V -> K spans 10^-34 .. 10^34 = 68 orders:", round(2 * F * 2 / (R * T * LN10) , 1))

    sec("CH09 half-reaction balancing MnO4- + 5 Fe2+")
    print("MnO4- + 8H+ + 5e- -> Mn2+ + 4H2O ;  5 Fe2+ -> 5 Fe3+ + 5 e- ; E(cell) = 1.51 - 0.77 =", round(1.51 - 0.77, 2), "V")
    print("log K = 5 x 0.74 /0.05916 =", round(5 * 0.74 / 0.05916, 1))
    print("Zn + MnO4-: 2 MnO4- + 16 H+ + 5 Zn -> 2 Mn2+ + 8 H2O + 5 Zn2+ ; E = 1.51+0.76 =", round(1.51 + 0.76, 2), "V")
    print("Self-test 5.2: Cu + H+: E = 0 - 0.34 = -0.34 V -> no. Cu oxidised by HCl? no (E<0); needs O2: E(O2/H2O)=1.23 -> +0.89 V")
    print("Self-test 5.3: Cr2O7 2- (1.38) vs Fe3+/Fe2+ (0.77): E=+0.61 V yes. vs Cl2/Cl- (1.36): E = +0.02 V ~ K = 10^(6*0.02/0.05916) =", round(10 ** (6 * 0.02 / 0.05916), 1), "(marginal; kinetically slow, side reaction in conc. HCl)")
    print("Ce4+ (1.76) can oxidise Cl-, Fe2+, Mn2+? Mn2+ -> MnO4-: reverse: E = 1.76 - 1.51 = +0.25 V yes")
    sec("CH09 Nernst")
    def E_nernst(E0, nu, Q):
        return E0 - (R * T / (nu * F)) * math.log(Q)
    for Q in (1, 10, 100, 1e-3):
        print(f"Daniell E = 1.10 - (0.05916/2) log Q: Q={Q:g}: {E_nernst(1.10, 2, Q):.4f} V")
    print("equilibrium Q=K: E=0; K =", f"{10**(2*1.10/0.05916):.2e}")
    print("Q for E_cell=0.5 V (nu=2): log Q =", round((1.10 - 0.5) * 2 / 0.05916, 2))
    print("MnO4-/Mn2+ vs pH: E = 1.51 - (8/5)(0.05916) pH =", round(8 / 5 * 0.05916, 4), "V per pH unit; at pH 7:", round(1.51 - 8 / 5 * 0.05916 * 7, 3))
    print("O2/H2O: E = 1.229 - 0.05916 pH : at pH 7", round(1.229 - 0.05916 * 7, 3))
    print("H+/H2: E = -0.05916 pH ; pH 7 -> ", round(-0.05916 * 7, 3))
    sec("CH09 temperature dependence (eq 5.7)")
    print("dE/dT = DS/(nu F). Zn/H+ cell: DS(298) via standard entropies Zn 41.6, H2 130.7, Zn2+ -112.1, H+ 0 J/(mol K) -> DS =", end=" ")
    DS = (-112.1 + 130.7) - (41.6 + 0)
    print(round(DS, 1), "J/(mol K); dE/dT =", round(DS / (2 * F) * 1000, 3), "mV/K")
    sec("CH09 thermodynamic cycle for M+/M (Table 5.1)")
    tab = {"Li": (161, 526, -520, 16, -3.04), "Na": (109, 502, -406, 22, -2.71), "Cs": (79, 382, -264, 34, -2.92), "Ag": (284, 735, -468, 29, 0.80)}
    dfH_H = 218 + 1312 - 1085
    print("DfH(H+,aq) absolute =", dfH_H, "kJ/mol")
    for nm, (sub, I, hyd, TdS, E) in tab.items():
        s = sub + I + hyd
        dH = s - dfH_H
        dG = dH - TdS
        print(f"{nm}: sub+I+hyd={s:4d}  DH(M+H+->M++1/2H2)={dH:5d}  DG={dG:5d}  E=DG/F={dG/F*1000/1000*1:6.3f}... -> {dG*1000/F:+.2f} V (table {E})")
    sec("CH09 Frost diagram data for Mn in acid (Latimer, V: S&A Resource 3, recalled)")
    lat = [("MnO4-", 7), ("MnO4 2-", 6), ("MnO2", 4), ("Mn3+", 3), ("Mn2+", 2), ("Mn", 0)]
    steps = [0.56, 2.26, 0.95, 1.51, -1.18]
    nE = {"Mn": 0.0}
    Nn = [0, 2, 3, 4, 6, 7]
    # build from Mn upward: nE(N) cumulative
    names = ["Mn", "Mn2+", "Mn3+", "MnO2", "MnO4 2-", "MnO4-"]
    # step from Mn to Mn2+ is E(Mn2+/Mn) = -1.18 with 2e ; Mn3+/Mn2+ 1.51 (1e); MnO2/Mn3+ 0.95(1e); MnO4 2-/MnO2 2.26 (2e); MnO4-/MnO4 2- 0.56 (1e)
    seq = [(-1.18, 2), (1.51, 1), (0.95, 1), (2.26, 2), (0.56, 1)]
    cur = 0.0
    nE_list = [0.0]
    for E, n in seq:
        cur += n * E
        nE_list.append(cur)
    for nm, N, e in zip(names, Nn, nE_list):
        print(f"{nm:8s} N={N}  nE={e:+.2f} V")
    print("check MnO4-/Mn2+ = (nE(MnO4-) - nE(Mn2+))/5 =", round((nE_list[5] - nE_list[1]) / 5, 3), "(table 1.51)")
    print("Mn3+ disproportionation: E = 1.51 - 0.95 =", round(1.51 - 0.95, 2), "V; K = 10^%.1f" % (0.56 / 0.05916))
    print("MnO4 2- disproportionation in acid: 2.26 - 0.56 =", round(2.26 - 0.56, 2), "V")


if __name__ == "__main__":
    for f in (ch02, ch03, ch04, ch05, ch06, ch07, ch08, ch09):
        f()
