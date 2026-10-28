"""Concept maps (SVG + Excalidraw) for chapters that had only a one-sentence story.   .venv/bin/python scripts/diagrams_maps.py [name-substring]
Each chapter gets one 'Map' diagram: the dependency of ideas, drawn with scripts/diagrams.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagrams import excalidraw, svg

SPECS = {
    "QM07 Finite Well Map": dict(
        size=(1000, 600),
        nodes={
            "w": dict(x=170, y=100, w=280, h=100, text="The well\nV = 0 for |x| < a, V0 outside\nenergy from the floor, 0 < E < V0", color="blue"),
            "m": dict(x=500, y=100, w=280, h=100, text="Match psi and psi' at x = a\nparity: even cos, odd sin\noutside: exp(-kappa|x|)", color="orange"),
            "q": dict(x=830, y=100, w=290, h=100, text="Quantisation\nkappa/k0 = tan(k0 a)  (even)\nkappa/k0 = -cot(k0 a)  (odd)", color="aqua"),
            "g": dict(x=170, y=290, w=280, h=110, text="Graph (Tutorial IV)\nkappa/k0 = sqrt(z0^2/z^2 - 1)\nintersect tan / -cot branches\nN = ceil(2 z0/pi)", color="aqua"),
            "l": dict(x=500, y=290, w=290, h=110, text="Limits\ndeep: box, E (1 - 2/z0)\nshallow: always one state\ndelta: kappa = m alpha/hbar^2", color="grey"),
            "p": dict(x=830, y=290, w=290, h=110, text="Penetration\nd = 1/kappa, P_out > 0\nwider effective box,\nlevels below the box levels", color="blue"),
            "s": dict(x=330, y=480, w=330, h=110, text="E > V0: scattering\nA e^{ikx} + B e^{-ikx} ... F e^{ikx}\nT = 1/(1 + V0^2 sin^2(2 k0 a)/4E(E-V0))", color="orange"),
            "r": dict(x=700, y=480, w=330, h=110, text="Resonances\nT = 1 at 2 k0 a = n pi\n(box energies); T -> 0 at E = V0\nT + R = 1", color="red"),
        },
        arrows=[("w", "m", ""), ("m", "q", ""), ("q", "g", ""), ("g", "l", ""), ("q", "p", ""), ("w", "s", ""), ("s", "r", ""), ("p", "l", "")],
        title="QM07: the finite square well in one page",
        footer="Finite_well.pdf pp.2-13 (instructor), Tutorial IV; Griffiths 2.6, Sakurai 2.5 for the extras",
    ),
    "QM08 Tunnelling Map": dict(
        size=(1000, 600),
        nodes={
            "st": dict(x=170, y=100, w=280, h=100, text="Step potential\nE > V0: R = ((k1-k2)/(k1+k2))^2\nE < V0: total reflection,\nevanescent tail", color="blue"),
            "ba": dict(x=500, y=100, w=290, h=100, text="Rectangular barrier\nE < V0: T = 1/(1 + V0^2 sinh^2(kappa L)/4E(V0-E))\ntunnelling", color="orange"),
            "tl": dict(x=830, y=100, w=290, h=100, text="Thick barrier\nT ~ 16 (E/V0)(1-E/V0) e^(-2 kappa L)\nexponentially small", color="red"),
            "cu": dict(x=170, y=290, w=280, h=110, text="Probability current\nj = (hbar/m) Im(psi* psi')\nR + T = 1 from conservation", color="aqua"),
            "wk": dict(x=500, y=290, w=290, h=110, text="WKB / Gamow\nT ~ exp(-2 int kappa(x) dx)\nsmooth barriers", color="aqua"),
            "ap": dict(x=830, y=290, w=290, h=110, text="Applications\nalpha decay, STM,\ntunnel diode, fusion in stars", color="grey"),
            "de": dict(x=330, y=480, w=300, h=100, text="Delta barrier / well\nT = 1/(1 + m alpha^2/(2 hbar^2 E))\nbound state kappa = m alpha/hbar^2", color="blue"),
            "tm": dict(x=700, y=480, w=320, h=100, text="Transfer matrix and bands\nperiodic wells: Kronig-Penney\ncos(qL) = cos(kL) + (m alpha/hbar^2 k) sin(kL)", color="orange"),
        },
        arrows=[("st", "ba", ""), ("ba", "tl", ""), ("st", "cu", ""), ("ba", "wk", ""), ("tl", "ap", ""), ("wk", "ap", ""), ("cu", "de", ""), ("de", "tm", "")],
        title="QM08: scattering and tunnelling in one page",
        footer="QM07 solved the well; here the particle comes from outside: step, barrier, delta, WKB, bands",
    ),
    "Dirac Algebra Map": dict(
        size=(1000, 600),
        nodes={
            "k": dict(x=170, y=100, w=270, h=100, text="Kets |alpha>\nabstract state space\nsuperposition, null ket", color="blue"),
            "b": dict(x=500, y=100, w=290, h=100, text="Bras <alpha|, inner product\n<a|b> = <b|a>*\nSchwarz inequality", color="orange"),
            "o": dict(x=830, y=100, w=290, h=100, text="Operators\nX|alpha>, |b><a| outer product\ncommutator [A,B]", color="aqua"),
            "h": dict(x=170, y=290, w=280, h=110, text="Adjoint, Hermitian\nreal eigenvalues\northogonal eigenkets", color="aqua"),
            "c": dict(x=500, y=290, w=290, h=110, text="Completeness\nsum |a><a| = 1\nmatrix elements, change of basis", color="grey"),
            "r": dict(x=830, y=290, w=290, h=110, text="x and p representations\npsi(x) = <x|alpha>\np = -i hbar d/dx, plane waves", color="blue"),
            "u": dict(x=330, y=480, w=300, h=110, text="Unitary operators\ntranslation T = e^(-i p l/hbar)\n[x,p] = i hbar", color="orange"),
            "m": dict(x=700, y=480, w=330, h=110, text="Measurement + dynamics\nP = |<a|alpha>|^2, Robertson DA DB >= |<[A,B]>|/2\nU = e^(-iHt/hbar), Heisenberg picture", color="red"),
        },
        arrows=[("k", "b", ""), ("b", "o", ""), ("b", "h", ""), ("o", "c", ""), ("h", "c", ""), ("c", "r", ""), ("c", "u", ""), ("u", "m", ""), ("r", "m", "")],
        title="Dirac algebra: from kets to measurement and time evolution",
        footer="Sakurai Ch.1 and 2.1: the same state in energy, position and momentum language",
    ),
    "CH02 Molecular Orbital Theory Diatomics": dict(
        size=(1000, 600),
        nodes={
            "a": dict(x=170, y=100, w=280, h=100, text="Orbital approximation\npsi = psi(1) psi(2) ...\none-electron MOs", color="blue"),
            "b": dict(x=500, y=100, w=290, h=100, text="LCAO\npsi = cA chiA + cB chiB\nN AOs -> N MOs", color="orange"),
            "c": dict(x=830, y=100, w=290, h=100, text="in phase: bonding\nout of phase: node = antibonding\nH2: 11.4 eV, 4.5 eV", color="aqua"),
            "d": dict(x=170, y=290, w=290, h=110, text="Homonuclear\n4 sigma + 4 pi from 4+4 AOs\nbond order (nb - na)/2", color="blue"),
            "e": dict(x=500, y=290, w=290, h=110, text="s-p mixing\nLi2-N2: pi_u below sigma_g\nO2, F2: sigma_g below pi_u", color="red"),
            "f": dict(x=830, y=290, w=290, h=110, text="Magnetism\nO2: 2 unpaired (triplet)\nB2 para, C2 dia", color="grey"),
            "g": dict(x=330, y=480, w=320, h=110, text="Heteronuclear\nEN atom dominates bonding MO\nCO 1070 vs N2 946 kJ/mol", color="aqua"),
            "h": dict(x=700, y=480, w=330, h=110, text="HF: 2 e- in the bond, 6 on F\nCO: HOMO 3sigma, LUMO 2pi on C\nsigma-donation + pi-back-donation", color="orange"),
        },
        arrows=[("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", ""), ("e", "f", ""), ("c", "g", ""), ("g", "h", "")],
        title="CH02: molecular orbital theory of diatomics in one page",
        footer="CH-2113 slides 27-39; S&A Ch.2",
    ),
    "CH03 Molecular Orbital Theory Polyatomics": dict(
        size=(1000, 600),
        nodes={
            "a": dict(x=170, y=100, w=280, h=100, text="N AOs -> N MOs\nrules: nodes = energy,\nlow AOs -> low MOs", color="blue"),
            "b": dict(x=500, y=100, w=290, h=100, text="H3: linear vs triangle\n1/2, 1/sqrt2, 1/2\nelectron count decides", color="orange"),
            "c": dict(x=830, y=100, w=290, h=100, text="symmetry labels\na, b non-degenerate,\ne double, t triple", color="aqua"),
            "d": dict(x=330, y=290, w=330, h=110, text="Ligand-group orbitals\nn_i = (1/h) sum chi_G chi_i\nonly same-symmetry mix", color="blue"),
            "e": dict(x=700, y=290, w=330, h=110, text="Fill from the bottom\nbonding, nonbonding, antibonding\nHOMO = lone pair", color="grey"),
            "f": dict(x=170, y=480, w=290, h=110, text="NH3 (C3v): a1 + e\n1a1^2 1e^4 2a1^2\nPES 11, 16 eV", color="orange"),
            "g": dict(x=500, y=480, w=290, h=110, text="SF6 (Oh): a1g + eg + t1u\n8 e- in bonding MOs\nbond order 0.67, no d", color="red"),
            "h": dict(x=830, y=480, w=290, h=110, text="H2O (C2v): a1 + b1\n2a1 1b1 3a1 1b2\ntwo different lone pairs", color="aqua"),
        },
        arrows=[("a", "b", ""), ("a", "c", ""), ("c", "d", ""), ("d", "e", ""), ("e", "f", ""), ("e", "g", ""), ("e", "h", "")],
        title="CH03: molecular orbital theory of polyatomics in one page",
        footer="CH-2113 slides 40-52; S&A Ch.2; point groups from the Group Theory notes",
    ),
    "CH04 Acid-Base Concepts": dict(
        size=(1000, 560),
        nodes={
            "a": dict(x=170, y=100, w=280, h=100, text="Arrhenius\nH+ / OH- in water\nKw = 1e-14", color="blue"),
            "b": dict(x=500, y=100, w=290, h=100, text="Bronsted-Lowry\nproton donor / acceptor\nconjugate pairs, pKa + pKb = 14", color="orange"),
            "c": dict(x=830, y=100, w=290, h=100, text="Lewis\nelectron-pair acceptor / donor\nHOMO -> LUMO adduct", color="aqua"),
            "d": dict(x=330, y=290, w=320, h=100, text="Lux-Flood\nO2- donor = base\nCaO + SiO2 -> CaSiO3", color="red"),
            "e": dict(x=700, y=290, w=320, h=100, text="Solvent system\ncation / anion of solvent\nNH4+ / NH2-, BrF2+ / BrF4-", color="grey"),
            "f": dict(x=500, y=470, w=480, h=100, text="Generalised: acidity = positive character,\nbasicity = negative character: strength follows charge density", color="blue"),
        },
        arrows=[("a", "b", ""), ("b", "c", ""), ("d", "c", ""), ("e", "c", ""), ("c", "f", "")],
        title="CH04: the acid-base definitions in one page",
        footer="CH-2113 slides 53-65",
    ),
    "CH05 Acid Strength Lewis Acidity and Reactions": dict(
        size=(1000, 600),
        nodes={
            "a": dict(x=170, y=100, w=280, h=100, text="Bronsted acid classes\naqua, hydroxo, oxo", color="blue"),
            "b": dict(x=500, y=100, w=290, h=100, text="Aqua: charge/size + covalency\npKa = 13.1 - 0.62 Z^2/r\nHg2+ and Cu2+ exceptions", color="orange"),
            "c": dict(x=830, y=100, w=290, h=100, text="Oxo: pKa = 8 - 5n\ninductive: x79, x2951, x12882\nH3PO3 = HP(O)(OH)2", color="aqua"),
            "d": dict(x=170, y=290, w=290, h=110, text="Lewis acid: 5 kinds\nincomplete octet, cation,\nrearrangement, shell expansion, pi*/sigma*", color="blue"),
            "e": dict(x=500, y=290, w=290, h=110, text="BX3: BF3 < BCl3 < BBr3\npi back-donation\nAl2Cl6, Friedel-Crafts", color="red"),
            "f": dict(x=830, y=290, w=290, h=110, text="SiX4: SiI4 < ... < SiF4\nSnCl3-, SbF5, SO2/SO3,\nI2 colour, I3-", color="grey"),
            "g": dict(x=330, y=480, w=320, h=100, text="Reaction types\nadduct, displacement,\nmetathesis (Me3SiI + AgBr)", color="orange"),
            "h": dict(x=700, y=480, w=320, h=100, text="Superacids\nSbF5 + HSO3F: Lewis acid\nmakes a Bronsted superacid", color="aqua"),
        },
        arrows=[("a", "b", ""), ("a", "c", ""), ("d", "e", ""), ("e", "f", ""), ("f", "g", ""), ("f", "h", ""), ("c", "h", "")],
        title="CH05: acid strength and Lewis acidity in one page",
        footer="CH-2113 slides 66-77; S&A Ch.4",
    ),
    "CH06 Hard and Soft Acids and Bases": dict(
        size=(1000, 600),
        nodes={
            "a": dict(x=170, y=100, w=280, h=100, text="Empirical rule\nKf order with halides reverses\nclass A / class B", color="blue"),
            "b": dict(x=500, y=100, w=290, h=100, text="Hard acid: small, high charge,\nfew valence electrons\nHard base: O, N, F", color="orange"),
            "c": dict(x=830, y=100, w=290, h=100, text="Soft acid: large, low charge,\nd10 / many d electrons\nSoft base: S, P, I, C", color="aqua"),
            "d": dict(x=330, y=290, w=320, h=110, text="hard-hard: electrostatic\nMadelung energy\nlarge HOMO-LUMO gap", color="blue"),
            "e": dict(x=700, y=290, w=320, h=110, text="soft-soft: covalent\npi back-donation, London\nsmall HOMO-LUMO gap", color="red"),
            "f": dict(x=170, y=480, w=290, h=100, text="Pearson eta = (I - A)/2\nAl3+ 45.8, Au+ 5.6 eV\nF 7.0, I 3.7 eV", color="grey"),
            "g": dict(x=500, y=480, w=290, h=100, text="Ores: lithophile (O, silicates)\nvs chalcophile (S)", color="aqua"),
            "h": dict(x=830, y=480, w=290, h=100, text="SCN-: N to hard, S to soft\nAgI2- ok, AgF2- not\nmetathesis direction", color="orange"),
        },
        arrows=[("a", "b", ""), ("a", "c", ""), ("b", "d", ""), ("c", "e", ""), ("d", "f", ""), ("e", "f", ""), ("f", "g", ""), ("g", "h", "")],
        title="CH06: hard and soft acids and bases in one page",
        footer="CH-2113 slides 78-89; Tutorial 3; Pearson 1988",
    ),
    "CH07 Main Group Cages and Clusters": dict(
        size=(1000, 600),
        nodes={
            "a": dict(x=170, y=100, w=280, h=100, text="Group 13: B electron deficient\nB-Si diagonal, Tl+ inert pair", color="blue"),
            "b": dict(x=500, y=100, w=290, h=100, text="B2H6: 12 e-\n4 terminal 2c-2e\n2 bridging 3c-2e", color="orange"),
            "c": dict(x=830, y=100, w=290, h=100, text="3c-2e MO: alpha +- sqrt2 beta, alpha\nB-B and B-B-B bonds too\nstyx numbers", color="aqua"),
            "d": dict(x=330, y=290, w=330, h=110, text="Deltahedra\nclosed, triangular faces\nE = 3n - 6, F = 2n - 4", color="blue"),
            "e": dict(x=700, y=290, w=330, h=110, text="Wade: BH = 2 e-, extra H = 1\nclosos n+1, nido n+2,\narachno n+3, hypho n+4", color="red"),
            "f": dict(x=170, y=480, w=290, h=100, text="Zintl ions: g - 2n\nSn5(2-) closo, Sn9(4-) nido,\nBi8(2+) arachno", color="grey"),
            "g": dict(x=500, y=480, w=290, h=100, text="P4: 6 edges, 60 degrees\nP4O6, P4O10, P4S3, P4S10", color="aqua"),
            "h": dict(x=830, y=480, w=290, h=100, text="2Ca3(PO4)2 + 6SiO2 + 10C\n-> P4 + 10CO + 6CaSiO3", color="orange"),
        },
        arrows=[("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", ""), ("e", "f", ""), ("a", "g", ""), ("g", "h", "")],
        title="CH07: cages and clusters in one page",
        footer="CH-2113 slides 90-108; Tutorial 4 Q1-Q4; Wade 1971",
    ),
    "CH08 Main Group Rings and Polymers": dict(
        size=(1000, 560),
        nodes={
            "a": dict(x=170, y=100, w=280, h=100, text="Inorganic heterocycles\nS8, cyclosilanes, (RAs)n\n(NPCl2)3 1834, borazine 1926", color="blue"),
            "b": dict(x=500, y=100, w=290, h=100, text="Borazine B3N3H6\nisoelectronic with benzene\nB-N 1.436 A, order ~ 1.3", color="orange"),
            "c": dict(x=830, y=100, w=290, h=100, text="polar pi: B 0.23, N 1.77\nadds HCl, Br2\n(benzene does not)", color="aqua"),
            "d": dict(x=170, y=290, w=290, h=110, text="B-N polymer\ndehydropolymerisation (80 C)\nMw ~ 7600, ~97 rings", color="blue"),
            "e": dict(x=500, y=290, w=290, h=110, text="pyrolysis 1200 C\nwhite BN, 85-93 %\n(max 92.5 %)", color="grey"),
            "f": dict(x=830, y=290, w=290, h=110, text="(NPCl2)3: equal short P-N\nDewar islands\npi-d overlap, node at P", color="red"),
            "g": dict(x=330, y=470, w=320, h=100, text="substitution\nNaF, RONa, RNH2, RMgX", color="orange"),
            "h": dict(x=700, y=470, w=320, h=100, text="ring opening 210-250 C\n[NPCl2]n -> [NPR2]n\npolyphosphazenes", color="aqua"),
        },
        arrows=[("a", "b", ""), ("b", "c", ""), ("b", "d", ""), ("d", "e", ""), ("a", "f", ""), ("f", "g", ""), ("f", "h", "")],
        title="CH08: rings and polymers in one page",
        footer="CH-2113 slides 109-119; Tutorial 4 Q5-Q10",
    ),
    "CH09 Redox": dict(
        size=(1000, 600),
        nodes={
            "a": dict(x=170, y=100, w=280, h=100, text="Half-reactions\nbalance O, H, charge\nOx + e- -> Red", color="blue"),
            "b": dict(x=500, y=100, w=290, h=100, text="DG0 = -nu F E0 = -RT ln K\n59.16 mV per decade\n+-2 V = 1e+-34", color="orange"),
            "c": dict(x=830, y=100, w=290, h=100, text="Electrochemical series\nreduced form reduces\nthe couples above it", color="aqua"),
            "d": dict(x=170, y=290, w=290, h=110, text="Trends in E0\ncycle: sublimation, ionisation,\nhydration (Li -3.04 V)", color="blue"),
            "e": dict(x=500, y=290, w=290, h=110, text="Nernst\nE = E0 - (RT/nuF) ln Q\npH slope -(m/n) 59 mV", color="red"),
            "f": dict(x=830, y=290, w=290, h=110, text="Water: window -0.059 pH\nto 1.23 - 0.059 pH\nO2 oxidises Fe2+, Cu", color="grey"),
            "g": dict(x=330, y=480, w=320, h=100, text="Disproportionation\nE0(to lower) > E0(from upper)\nCu+, HClO, Mn(VI)", color="orange"),
            "h": dict(x=700, y=480, w=320, h=100, text="Complexation\nE0(ML) = E0(M) - 0.059 log(Kox/Kred)\nCN-: Fe(III) x1e7, Ru(II)", color="aqua"),
        },
        arrows=[("a", "b", ""), ("b", "c", ""), ("b", "d", ""), ("c", "e", ""), ("e", "f", ""), ("c", "g", ""), ("e", "h", "")],
        title="CH09: redox in one page",
        footer="Shriver and Atkins Ch.5 pp.147-161 (Quiz 2 scope)",
    ),

}

if __name__ == "__main__":
    pat = sys.argv[1] if len(sys.argv) > 1 else ""
    for nm, sp in SPECS.items():
        if pat in nm:
            svg(nm, sp)
            excalidraw(nm, sp)
            print("built", nm)
