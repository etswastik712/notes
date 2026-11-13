"""CH2113 redox class notes (OneNote pages 1-4, 5-14 Oct 2026): every equation balanced and every number recomputed.
    .venv/bin/python -W ignore scripts/ch09_onenote_numbers.py"""
import math
import re

F, R = 96485.332, 8.314462618

def parse(f):
    el = {}
    for m, n in re.findall(r"([A-Z][a-z]?)(\d*)", f):
        el[m] = el.get(m, 0) + (int(n) if n else 1)
    return el
def side(terms):
    tot, q = {}, 0
    for coef, f, ch in terms:
        for e, n in parse(f).items():
            tot[e] = tot.get(e, 0) + coef * n
        q += coef * ch
    return tot, q
def check(name, L, Rr):
    a, qa = side(L); b, qb = side(Rr)
    ok = a == b and qa == qb
    print("  %-62s atoms %s, charge %+d -> %+d : %s" % (name, "equal" if a == b else "DIFFER %s vs %s" % (a, b), qa, qb, "balanced" if ok else "NOT balanced"))
    return ok

print("== Page 1: the balancing exercises")
check("2 NO + O2 -> 2 NO2", [(2, "NO", 0), (1, "O2", 0)], [(2, "NO2", 0)])
check("2 C4H10 + 13 O2 -> 8 CO2 + 10 H2O", [(2, "C4H10", 0), (13, "O2", 0)], [(8, "CO2", 0), (10, "H2O", 0)])
check("Fe3+ + Cr2+ -> Fe2+ + Cr3+", [(1, "Fe", 3), (1, "Cr", 2)], [(1, "Fe", 2), (1, "Cr", 3)])
check("3 CH3CH2OH + 2 CrO4^2- + 10 H+ -> 3 CH3CHO + 2 Cr3+ + 8 H2O", [(3, "C2H6O", 0), (2, "CrO4", -2), (10, "H", 1)], [(3, "C2H4O", 0), (2, "Cr", 3), (8, "H2O", 0)])
check("... the same with Cr2+ as written (reading of the handwriting)", [(3, "C2H6O", 0), (2, "CrO4", -2), (10, "H", 1)], [(3, "C2H4O", 0), (2, "Cr", 2), (8, "H2O", 0)])
check("LiCoO2 + C -> Li@C + CoO2", [(1, "LiCoO2", 0), (1, "C", 0)], [(1, "LiC", 0), (1, "CoO2", 0)])
check("Mn4(V,IV,IV,IV) + 2 H2O -> Mn4(IV,III,III,III) + 4 H+ + O2 (atoms, charge: Mn4 cluster charge bookkeeping +4)", [(1, "Mn4", 0), (2, "H2O", 0)], [(1, "Mn4", -4), (4, "H", 1), (1, "O2", 0)])
print("  oxidation numbers of Mn4: V+IV+IV+IV = %d -> IV+III+III+III = %d: the cluster takes up 4 e-, supplied by 2 H2O -> O2 + 4 H+ + 4 e-" % (5 + 12, 4 + 9))

print("\n== Pages 2-3: potentials, Nernst, water")
RTF = R * 298.15 / F
print("  RT/F = %.5f V at 298.15 K; Nernst slope (RT/F) ln10 = %.5f V per decade (the notes' 0.059)" % (RTF, RTF * math.log(10)))
sl = RTF * math.log(10)
print("  O2 + 4H+ + 4e- <-> 2H2O (OER): E = 1.229 - %.4f pH; HER (2H+ + 2e- -> H2): E = 0 - %.4f pH; window width %.3f V at every pH; pH 7: OER %.3f V, HER %.3f V" % (sl, sl, 1.229, 1.229 - 7 * sl, -7 * sl))
print("  the notes write E = 1.23 V - 0.059 V x pH and E = -0.059 V x pH (matches)")
print("  Daniell cell: E0 = 0.34 - (-0.76) = %.2f V; Delta G0 = -nFE0 = %.1f kJ/mol; K = exp(nFE0/RT) = %.2e" % (1.10, -2 * F * 1.10 / 1000, math.exp(2 * F * 1.10 / (R * 298.15))))
print("  Co3+ + e- -> Co2+: 1.92 V; versus O2/H2O at pH 0 (1.229 V): E0_cell = %.2f V (the notes: 'E0_cell = 0.6.' read as 0.69), Delta G0 for 4 Co3+ + 2 H2O -> 4 Co2+ + O2 + 4 H+: -nFE = %.1f kJ per mole of O2; thermodynamically favourable, kinetically slow (O-O bond formation)" % (1.92 - 1.229, -4 * F * (1.92 - 1.229) / 1000))
for name, E in (("Ce4+/Ce3+", 1.76), ("MnO4-/Mn2+", 1.51), ("Cr2O7 2-/Cr3+ (notes: 1.38; usual table value 1.33, recalled)", 1.38)):
    print("  %-62s E0 = %.2f V; driving force against O2/H2O at pH 0: %.2f V" % (name, E, E - 1.229))

print("\n== Page 4: complexation and Cu(I)")
for lab, Em, EML in (("Fe(III)/Fe(II): [Fe(H2O)6]3+/2+ 0.77 vs [Fe(CN)6]3-/4-", 0.77, 0.36), ("Ru(III)/Ru(II): [Ru(H2O)6]3+/2+ 0.25 vs [Ru(CN)6]3-/4-", 0.25, 0.85)):
    d = Em - EML
    r = math.exp(d / RTF)
    print("  %-62s E0(M) - E0(ML) = %+.2f V = (RT/F) ln(K_ox/K_red) -> K_ox/K_red = %.2e (%s binds the %s state more strongly)" % (lab, d, r, "CN-" , "oxidised (III)" if r > 1 else "reduced (II)"))
E1, E2 = 0.52, 0.16
Ed = E1 - E2
print("  Cu: E0(Cu+/Cu) = +0.52, E0(Cu2+/Cu+) = +0.16; 2 Cu+ -> Cu + Cu2+: E0 = %.2f V, Delta G0 = %.1f kJ/mol, K = %.2e" % (Ed, -F * Ed / 1000, math.exp(F * Ed / (R * 298.15))))

print("\n== Li-ion battery (page 2): capacities, per mass (n F / (3.6 M) in mAh/g)")
def cap(n, M):
    return n * F / 3.6 / M
Mw = {"Li": 6.94, "Na": 22.990, "Ca": 40.078, "Zn": 65.38, "LiCoO2": 6.94 + 58.933 + 2 * 15.999, "C6": 6 * 12.011}
print("  metal anodes (theoretical, n e- per atom): Li %.0f, Na %.0f, Ca %.0f, Zn %.0f mAh/g" % (cap(1, Mw["Li"]), cap(1, Mw["Na"]), cap(2, Mw["Ca"]), cap(2, Mw["Zn"])))
print("  graphite LiC6 (1 Li per C6): %.0f mAh/g of C6; LiCoO2 (full delithiation, 1 e-): %.0f mAh/g; practical x = 0.5: %.0f mAh/g" % (cap(1, Mw["C6"]), cap(1, Mw["LiCoO2"]), cap(0.5, Mw["LiCoO2"])))
print("  molar masses used: Li 6.94, Na 22.990, Ca 40.078, Zn 65.38, Co 58.933, O 15.999, C 12.011 g/mol (standard atomic weights)")
print("  standard potentials of the notes: Li+/Li -3.04, Na+/Na -2.71, Ca2+/Ca -2.84, H+/H2 0, Cu2+/Cu +0.34, F2/F- +2.87 V: span Li to F2 = %.2f V; Li vs Ca differ by %.2f V" % (2.87 + 3.04, 3.04 - 2.84))
