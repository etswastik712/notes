"""CH10 (crystal field theory, inorganic chemistry, CH2113 Quiz 3) - every number quoted in the chapter, recomputed.

    .venv/bin/python -W ignore scripts/ch10_numbers.py

Inputs taken from the two assigned book ranges are marked (S&A = Shriver and Atkins 5th ed., pp.473-483;
H = Huheey, Keiter and Keiter 4th ed., pp.394-413).  Values recalled from elsewhere are flagged `recalled`.
"""
import itertools
import math

import numpy as np
from scipy.optimize import brentq
from scipy import integrate
from scipy.special import sph_harm_y

P = print
CM_TO_KJ = 0.0119627  # 1 cm^-1 = 0.0119627 kJ/mol
HC = 1.0e7  # lambda/nm = 1e7 / (nu/cm^-1)


def sec(t):
    P("\n=====", t)


# ---------------------------------------------------------------------------------------------
sec("A. Point-charge crystal field from first principles: the splitting patterns (H Table 11.5, S&A Figs 20.2, 20.8, 20.10)")
# Potential of unit point charges at R_i acting on a d electron at r < R:
#   V(r) = sum_i sum_l (r^l / R^{l+1}) * 4pi/(2l+1) * sum_m Y_lm(R_i)* Y_lm(r)
# l = 0 shifts all five d orbitals equally (the 'spherical' part, the barycentre rise); l = 2, 4 split them.
# Matrix elements <d_a| Y_lm |d_b> are angular integrals; we evaluate them on a Gauss grid on the sphere.
th, wth = np.polynomial.legendre.leggauss(40)
phi = np.linspace(0, 2 * np.pi, 80, endpoint=False)
TH, PH = np.meshgrid(np.arccos(th), phi, indexing="ij")
W = (wth[:, None] * np.ones_like(PH)) * (2 * np.pi / len(phi))
X, Y, Z = np.sin(TH) * np.cos(PH), np.sin(TH) * np.sin(PH), np.cos(TH)
c = math.sqrt(15 / (4 * math.pi))
D = {  # real normalised d orbitals (angular parts)
    "z2": math.sqrt(5 / (16 * math.pi)) * (3 * Z**2 - 1),
    "x2-y2": 0.5 * c * (X**2 - Y**2),
    "xy": c * X * Y, "xz": c * X * Z, "yz": c * Y * Z,
}
names = list(D)


def real_Y(l, m, th_, ph_):
    """Real spherical harmonic."""
    if m == 0:
        return sph_harm_y(l, 0, th_, ph_).real
    y = sph_harm_y(l, abs(m), th_, ph_)
    return (math.sqrt(2) * (-1) ** m * (y.real if m > 0 else y.imag))


def angular_matrix(l, ligands):
    """sum_i 4pi/(2l+1) sum_m Y_lm(R_i) <d_a|Y_lm|d_b>  for unit-direction ligands."""
    M = np.zeros((5, 5))
    for m in range(-l, l + 1):
        Ylm = real_Y(l, m, TH, PH)
        S = sum(real_Y(l, m, math.acos(np.clip(v[2], -1, 1)), math.atan2(v[1], v[0])) for v in ligands)
        for a, na in enumerate(names):
            for b, nb in enumerate(names):
                M[a, b] += 4 * math.pi / (2 * l + 1) * S * np.sum(W * D[na] * Ylm * D[nb])
    return M


def unit(v):
    v = np.array(v, float)
    return v / np.linalg.norm(v)


geoms = {
    "octahedral": [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)],
    "tetrahedral": [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)],
    "cubic (8)": list(itertools.product((1, -1), repeat=3)),
    "square planar": [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)],
    "linear (z)": [(0, 0, 1), (0, 0, -1)],
}
M4 = {g: angular_matrix(4, [unit(v) for v in L]) for g, L in geoms.items()}
M2 = {g: angular_matrix(2, [unit(v) for v in L]) for g, L in geoms.items()}
# scale: choose the l = 4 radial factor so that octahedral Delta_O = 10 Dq = 10  (Dq = 1)
eo4 = np.sort(np.linalg.eigvalsh(M4["octahedral"]))
scale4 = 10.0 / (eo4[-1] - eo4[0])
P(f"octahedral (l=4 part only; l=2 part vanishes by symmetry): eigenvalues scaled to Dq=1: {np.round(eo4*scale4,3)} -> t2g/eg split = {(eo4[-1]-eo4[0])*scale4:.3f} Dq")
P("  -> the same calculation also gives the barycentre rule: trace of every l=2,4 matrix is 0 (see below)")
for g in ("octahedral", "tetrahedral", "cubic (8)"):
    ev = np.sort(np.linalg.eigvalsh(M4[g] * scale4))
    P(f"{g:12s} d-orbital energies / Dq (l=4 only, same M-L distance, same radial integral): {np.round(ev,2)}   sum={ev.sum():+.3f}")
to = np.sort(np.linalg.eigvalsh(M4["tetrahedral"]))
P(f"Delta_T/Delta_O (tetrahedral, same R, same ligands) = {(to[-1]-to[0])/(eo4[-1]-eo4[0]):.4f}   (book: 4/9 = {4/9:.4f})")
tc = np.sort(np.linalg.eigvalsh(M4["cubic (8)"]))
P(f"Delta_cubic/Delta_O = {(tc[-1]-tc[0])/(eo4[-1]-eo4[0]):.4f}  (book: 8/9 = {8/9:.4f}; the tetrahedron is half the cube so Delta_T = 4/9 Delta_O)")
# square planar needs the l=2 term as well (Ds in the book): the l=2 part is diagonal in the real d basis, so
# E_a(s) = E4_a + s * E2_a.  Fix the single weight s by one orbital (dz2 = -4.28 Dq, H Table 11.5) and TEST the other three.
e4 = np.diag(scale4 * M4["square planar"]); e2 = np.diag(M2["square planar"])
iz = names.index("z2")
s_fit = (-4.28 - e4[iz]) / e2[iz]
E = e4 + s_fit * e2
book = {"z2": -4.28, "x2-y2": 12.28, "xy": 2.28, "xz": -5.14, "yz": -5.14}
P("square planar, l=4 part only (Dq units):", dict(zip(names, np.round(e4, 2))))
P(f"l=2 weight fixed by dz2 = -4.28: s = {s_fit:.2f}")
P("  orbital   computed   H Table 11.5")
for i, n_ in enumerate(names):
    P(f"  {n_:7s}   {E[i]:+7.2f}    {book[n_]:+7.2f}")
P(f"  trace = {E.sum():+.3f} (barycentre kept); the other three orbitals are REPRODUCED by one fitted number.")
P("  (the book's OCR row lost dxy = +2.28; the zero trace of the row fixes it: -4.28+12.28+2.28+2(-5.14) = 0)")
P(f"  square-planar splittings: dx2-y2 above dxy {E[1]-E[2]:.2f} Dq ; dxy above dz2 {E[2]-E[0]:.2f} Dq ; dz2 above dxz,dyz {E[0]-E[3]:.2f} Dq ; total spread {E[1]-E[3]:.2f} Dq = {(E[1]-E[3])/10:.2f} Delta_O")

# ---------------------------------------------------------------------------------------------
sec("B. LFSE tables: octahedral high/low spin and tetrahedral (S&A Tables 20.2, 20.4; H Table 11.3)")
# octahedral: n_t2g, n_eg given by Hund / low-spin filling.  LFSE/Delta = 0.4 nt - 0.6 ne ; pairing cost counted as
# the number of EXTRA pairs relative to the spherical (free-ion, Hund) configuration (S&A convention).


def free_ion_pairs(n):
    return max(0, n - 5)


def oct_config(n, spin):
    if spin == "high":
        nt = min(n, 3) + max(0, min(n - 5, 3)) if n <= 5 else 3 + (n - 5) - 0
        # fill: t2g(3) , eg(2) singly, then pair t2g, then pair eg
        nt, ne = 0, 0
        order = ["t", "t", "t", "e", "e", "t", "t", "t", "e", "e"]
        for i in range(n):
            if order[i] == "t":
                nt += 1
            else:
                ne += 1
        return nt, ne
    order = ["t", "t", "t", "t", "t", "t", "e", "e", "e", "e"]
    nt = sum(1 for i in range(n) if order[i] == "t")
    return nt, n - nt


def pairs(nt, ne):
    """number of electron pairs in a configuration of t2g^nt eg^ne (Hund within each set)"""
    return max(0, nt - 3) + max(0, ne - 2)


def unpaired(nt, ne):
    return (nt if nt <= 3 else 6 - nt) + (ne if ne <= 2 else 4 - ne)


rows = []
P("n  | HS config  N  LFSE/Do | LS config  N  LFSE/Do")
for n in range(0, 11):
    th_, eh = oct_config(n, "high")
    tl, el = oct_config(n, "low")
    lh = 0.4 * th_ - 0.6 * eh
    ll = 0.4 * tl - 0.6 * el
    extra = pairs(tl, el) - pairs(th_, eh)
    rows.append((n, th_, eh, tl, el, lh, ll, extra))
    s_hs = f"t2g^{th_} eg^{eh}  {unpaired(th_,eh)}  {lh:+.1f}"
    s_ls = f"t2g^{tl} eg^{el}  {unpaired(tl,el)}  {ll:+.1f} - {extra}P" if extra else "(same)"
    P(f"d{n:<2d}| {s_hs:22s} | {s_ls}")
P("S&A Table 20.2 for comparison: d4 0.6 / 1.6-P; d5 0 / 2.0-2P; d6 0.4 / 2.4-2P; d7 0.8 / 1.8-P  -> reproduced")

P("\nlow-spin minus high-spin energy, E_LS - E_HS = (LFSE_LS - LFSE_HS) Delta_O - (extra pairs) P  (negative = low spin wins):")
for n in (4, 5, 6, 7):
    r = rows[n]
    dD = r[6] - r[5]
    P(f"  d{n}: E_LS - E_HS = -{dD:.1f} Delta_O + {r[7]} P ;  crossover Delta_O/P = {r[7]/dD:.2f}   (low spin iff Delta_O > P)")

P("\ntetrahedral (e fills first; e = -3/5 Dt, t2 = +2/5 Dt; always high spin):")
for n in range(0, 11):
    order = ["e", "e", "t", "t", "t", "e", "e", "t", "t", "t"]
    ne_ = nt_ = 0
    for i in range(n):
        if order[i] == "e":
            ne_ += 1
        else:
            nt_ += 1
    lf = 0.6 * ne_ - 0.4 * nt_
    P(f"  d{n:<2d} e^{ne_} t2^{nt_}  LFSE = {lf:+.1f} Dt = {lf*4/9:+.3f} Do")

# ---------------------------------------------------------------------------------------------
sec("C. Spin-only magnetic moments (S&A eq. 20.2, Table 20.3, Example 20.2 and Self-test 20.2)")
mu = lambda N: math.sqrt(N * (N + 2))
for N in range(0, 6):
    P(f"N={N}: S={N/2:.1f}  mu_so = {mu(N):.2f} mu_B")
P("Table 20.3: Ti3+ 1.73, V3+ 2.83, Cr3+ 3.87, Mn3+(HS) 4.90, Fe3+(HS) 5.92  -> reproduced")
P("Example 20.2: mu = 4.0 for Co(II): HS d7 (N=3, 3.87) vs LS d7 (N=1, 1.73) -> high spin")
P(f"Self-test 20.2: mu = 6.06 for [Mn(NCS)6]4-: Mn(II) d5 -> HS t2g^3 eg^2 (N=5, {mu(5):.2f}); the 0.14 excess is orbital/ measurement")
P(f"S&A: [Fe(CN)6]3-, mu = 2.3 lies between N=1 ({mu(1):.2f}) and N=2 ({mu(2):.2f}): orbital contribution (t2g^5 low-spin d5)")
P("Hill: HS d6: N=4 -> 4.90 ; LS d6: 0.")

# ---------------------------------------------------------------------------------------------
sec("D. Energies, colours and units (H p.399, S&A p.474)")
for nu, lab in ((20300, "[Ti(OH2)6]3+  (S&A Fig 20.3, H Fig 11.8)"), (32500, "ReF6  (H p.399)")):
    P(f"{lab}: {nu} cm-1 = {nu*CM_TO_KJ:.1f} kJ/mol = {nu*1.23984e-4:.3f} eV ; lambda = {HC/nu:.0f} nm")
P("  -> Huheey prints 338 kJ/mol for 32,500 cm-1: that is a typo for 389 (digits transposed) [verify against the book]")
P("  -> the d-d absorption of [Ti(OH2)6]3+ at 493 nm removes blue-green light: transmitted violet-purple (complementary colour)")
P("Colour wheel check, [CoX(NH3)5]n+ (S&A p.475): I- purple (absorbs yellow-green) ... Cl- pink (absorbs green) ... NH3 yellow (absorbs violet): Delta_O increases I-<Br-<Cl-<H2O<NH3")

# ---------------------------------------------------------------------------------------------
sec("E. Tetrahedral Delta_T = (4/9) Delta_O and the Jorgensen f.g rule (H eq. 11.5, Tables 11.6, 11.7; S&A Table 20.5)")
P(f"Delta_T/Delta_O: point-charge 4/9 = {4/9:.3f}; observed for the same ligand: [Co(NH3)4]2+ 5900 vs [Co(NH3)6]2+ 10,200 (H Table 11.6) -> {5900/10200:.2f} (H: 'only about 50 %'); S&A Table 20.5: [CoCl4]2- 3300 / [CoBr4]2- 2900 / [CoI4]2- 2700, VCl4 9010 (H Table 11.6 reads 7900 for VCl4: the two books differ)")
f_lig = {"Br-": 0.72, "SCN-": 0.73, "Cl-": 0.78,  # Cl- value garbled in the OCR (recalled)
  "N3-": 0.83, "F-": 0.9, "H2O": 1.00, "NCS-": 1.02, "gly": 1.18, "py": 1.23, "NH3": 1.25, "en": 1.28, "bpy": 1.33, "CN-": 1.7}
g_met = {"Mn(II)": 8.0, "Ni(II)": 8.7, "Co(II)": 9.3, "V(II)": 12.0, "Fe(III)": 14.0, "Cr(III)": 17.4, "Co(III)": 18.2, "Ru(II)": 20.0, "Mn(IV)": 23.0, "Mo(III)": 24.6, "Rh(III)": 27.0, "Ir(III)": 32.0}
# Table 11.7 as OCR'd: f values listed for F- = 0.9, ox 0.99 etc. (OCR of 'ox 0.9' read as 0.99 here: verify); g in kK
obs = [("[Cr(H2O)6]3+", "H2O", "Cr(III)", 17400), ("[Cr(en)3]3+", "en", "Cr(III)", 22300), ("[Cr(CN)6]3-", "CN-", "Cr(III)", 26600),
       ("[CrF6]3-", "F-", "Cr(III)", 15060), ("[Co(NH3)6]3+", "NH3", "Co(III)", 22870), ("[Co(H2O)6]3+", "H2O", "Co(III)", 20760),
       ("[Co(en)3]3+", "en", "Co(III)", 23160), ("[CoF6]3-", "F-", "Co(III)", 13100), ("[Fe(H2O)6]3+", "H2O", "Fe(III)", 14000),
       ("[Fe(CN)6]3-", "CN-", "Fe(III)", 35000), ("[Rh(NH3)6]3+", "NH3", "Rh(III)", 34100), ("[Rh(H2O)6]3+", "H2O", "Rh(III)", 27200),
       ("[Co(H2O)6]2+", "H2O", "Co(II)", 9200), ("[Co(NH3)6]2+", "NH3", "Co(II)", 10200)]
P("complex          f     g(kK)   f*g (cm-1)   observed   error")
errs = []
for nm, l, m, o in obs:
    pred = f_lig[l] * g_met[m] * 1000
    errs.append((pred - o) / o)
    P(f"{nm:15s} {f_lig[l]:5.2f}  {g_met[m]:5.1f}   {pred:8.0f}    {o:7d}   {100*(pred-o)/o:+.0f} %")
P(f"mean |error| = {100*np.mean(np.abs(errs)):.0f} %; the rule is good to 5-10 % for N/O donors and fails for CN- (pi-acceptor, a ligand-field/MO effect, not electrostatics)")

# ---------------------------------------------------------------------------------------------
sec("F. Spin state from Delta_O and P (H Tables 11.4, 11.6; S&A Table 20.1)")
Ptab = {"Cr2+ d4": 244.3, "Mn3+ d4": 301.6, "Mn2+ d5": 285.0, "Fe3+ d5": 357.4, "Fe2+ d6": 174.2, "Co3+ d6": 229.1}
P("P(total) = P(coulomb) + P(exchange), kJ/mol (and cm-1) for free ions, H Table 11.4:")
chk = {"Cr2+ d4": (71.2, 173.1), "Mn2+ d5": (91.0, 194.0), "Fe3+ d5": (120.2, 237.1), "Fe2+ d6": (73.5, 100.6), "Co3+ d6": (89.2, 139.8)}
for k, (a, b) in chk.items():
    P(f"  {k}: {a}+{b} = {a+b:.1f} (table total {Ptab[k]})  = {Ptab[k]/CM_TO_KJ:.0f} cm-1")
cases = [("Fe3+ d5", "[Fe(H2O)6]3+", 14000, "high"), ("Fe3+ d5", "[Fe(CN)6]3-", 35000, "low"),
         ("Fe2+ d6", "[Fe(H2O)6]2+", 10400, "high"), ("Fe2+ d6", "[Fe(CN)6]4-", 32200, "low"),
         ("Co3+ d6", "[CoF6]3-", 13100, "high"), ("Co3+ d6", "[Co(H2O)6]3+", 20760, "low"), ("Co3+ d6", "[Co(NH3)6]3+", 22870, "low"),
         ("Mn2+ d5", "[Mn(H2O)6]2+", 8500, "high")]
P("ion    complex          Delta_O  P(free ion)  Delta/P  predicted   observed")
for ion, nm, d, ob in cases:
    Pc = Ptab[ion] / CM_TO_KJ
    pr = "low" if d > Pc else "high"
    P(f"{ion:8s}{nm:15s} {d:7d}  {Pc:9.0f}  {d/Pc:6.2f}   {pr:5s}      {ob}   {'OK' if pr==ob else 'MISMATCH'}")
P("(P in complexes is 15-30% smaller than the free-ion value, H Table 11.4 footnote, which shifts the borderline Co(H2O)6 3+ case: 20,760 vs 19,150 free -> LS.)")

# ---------------------------------------------------------------------------------------------
sec("G. Hydration enthalpies of M2+ and the LFSE saw-tooth (S&A Fig 20.7, Table 20.1; H p.409)")
hyd = {"Ca": 2468, "V": 2814, "Cr": 2799, "Mn": 2743, "Fe": 2843, "Co": 2904, "Ni": 2986, "Cu": 2989, "Zn": 2936}  # -DhydH, kJ/mol, read off S&A Fig 20.7
n_d = {"Ca": 0, "V": 3, "Cr": 4, "Mn": 5, "Fe": 6, "Co": 7, "Ni": 8, "Cu": 9, "Zn": 10}
# hexaaqua Delta_O (cm-1): S&A Table 20.1 for Mn2+, Fe2+, Ni2+; H Table 11.6 for Co2+ (9,200); V2+, Cr2+, Cu2+ recalled
dO = {"V": 12400, "Cr": 13900, "Mn": 8500, "Fe": 10400, "Co": 9200, "Ni": 8500, "Cu": 12600}
lfse = {"V": 1.2, "Cr": 0.6, "Mn": 0.0, "Fe": 0.4, "Co": 0.8, "Ni": 1.2, "Cu": 0.6}
corr = {}
for k in hyd:
    if k in dO:
        corr[k] = hyd[k] - lfse[k] * dO[k] * CM_TO_KJ
    else:
        corr[k] = hyd[k]
P("ion  n  -DhydH(obs)  LFSE (kJ/mol)  corrected  line(Ca-Zn)  residual")
x = np.array([n_d[k] for k in hyd], float)
slope = (hyd["Zn"] - hyd["Ca"]) / 10.0
for k in hyd:
    L = lfse.get(k, 0) * dO.get(k, 0) * CM_TO_KJ
    line = hyd["Ca"] + slope * n_d[k]
    P(f"{k:3s} {n_d[k]:2d}   {hyd[k]:6d}      {L:6.1f}        {corr[k]:7.1f}     {line:7.1f}    {corr[k]-line:+6.1f}")
xs = np.array([n_d[k] for k in hyd], float)
yc = np.array([corr[k] for k in hyd]); yo = np.array([hyd[k] for k in hyd])
cf = np.polyfit(xs, yc, 2); res_c = yc - np.polyval(cf, xs)
co = np.polyfit(xs, yo, 2); res_o = yo - np.polyval(co, xs)
P(f"quadratic fit to the CORRECTED values: rms residual {np.sqrt(np.mean(res_c**2)):.1f} kJ/mol, max {np.max(np.abs(res_c)):.1f}; to the RAW values: rms {np.sqrt(np.mean(res_o**2)):.1f}, max {np.max(np.abs(res_o)):.1f}")
P("corrected values increase monotonically (Ca->Zn):", bool(np.all(np.diff(yc) > 0)), "; successive steps per electron (kJ/mol):", np.round(np.diff(yc) / np.diff(xs), 1))
P("raw values are NOT monotonic (Cr, Mn dip; Cu, Zn dip): the saw-tooth. The book's 'straight line' is the smooth, slightly concave trend of the filled circles (S&A Fig 20.7).")
P(f"worked check: Ni2+ LFSE = 1.2 * 8500 cm-1 = {1.2*8500*CM_TO_KJ:.0f} kJ/mol (S&A: 'little more than 10 per cent of the overall M-L interaction')")

P("\nExample 20.3, oxides MO (lattice enthalpy, kJ/mol): CaO 3460, TiO 3878, VO 3913, MnO 3810")
step = (3810 - 3460) / 5
pred_TiO, pred_VO = 3460 + 2 * step, 3460 + 3 * step
P(f"  linear Ca->Mn step = {step:.0f}; predicted TiO {pred_TiO:.0f}, VO {pred_VO:.0f}; excess TiO {3878-pred_TiO:.0f} (0.8 Delta_O), VO {3913-pred_VO:.0f} (1.2 Delta_O)  [book: 278, 243]")
P(f"  implied Delta_O: TiO {(3878-pred_TiO)/0.8/CM_TO_KJ:.0f} cm-1, VO {(3913-pred_VO)/1.2/CM_TO_KJ:.0f} cm-1: not equal, so the straight line is only a rough baseline (the book's own 'we can ascribe')")
P("Self-test 20.3 fluorides: MnF2 2780, FeF2 2926, CoF2 2976, NiF2 3060, ZnF2 2985")
Fl = {"Mn": 2780, "Fe": 2926, "Co": 2976, "Ni": 3060, "Zn": 2985}
st = (Fl["Zn"] - Fl["Mn"]) / 5
for i, k in enumerate(("Fe", "Co", "Ni"), 1):
    pr = Fl["Mn"] + i * st
    P(f"  {k}F2: baseline {pr:.0f} observed {Fl[k]}  excess {Fl[k]-pr:+.0f}  LFSE/Delta_O = {[0.4,0.8,1.2][i-1]}  excess per 0.4 Delta_O = {(Fl[k]-pr)/[1,2,3][i-1]:.0f}")
P("  -> excesses 105 : 114 : 157 are positive and largest for Ni2+ (d8, LFSE 1.2) as predicted, but are not in the 1:2:3 ratio: the baseline Mn->Zn is not exactly a straight line")

# ---------------------------------------------------------------------------------------------
sec("H. Octahedral site preference energy and spinels (H Table 11.9 and p.412; S&A pp.482-483)")
# OSPE = LFSE_oct(HS) - LFSE_tet, with Delta_T = 4/9 Delta_O and the same ligands.


def ospe(nt, ne, n):
    order = ["e", "e", "t", "t", "t", "e", "e", "t", "t", "t"]
    ne_ = sum(1 for i in range(n) if order[i] == "e")
    nt_ = n - ne_
    lf_t = (0.6 * ne_ - 0.4 * nt_) * 4 / 9
    return (0.4 * nt - 0.6 * ne) - lf_t


aq = {("Ni2+", 8): 8500, ("Cr3+", 3): 17400, ("Mn3+", 4): 21000, ("Co2+", 7): 9200, ("Fe2+", 6): 10400, ("Fe3+", 5): 14000, ("Mn2+", 5): 8500, ("Zn2+", 10): 0}
quoted = {"Ni2+": 86, "Cr3+": 176, "Mn3+": 106, "Co2+": 29.3, "Fe2+": 15}
P("ion  d^n  OSPE/Delta_O  Delta_O(cm-1)  OSPE (kJ/mol)  book")
for (ion, n), d in aq.items():
    nt, ne = oct_config(n, "high")
    o = ospe(nt, ne, n)
    P(f"{ion:5s} d{n:<2d}  {o:6.3f}       {d:6d}        {o*d*CM_TO_KJ:6.1f}      {quoted.get(ion,'-')}")
P("  => Ni2+, Cr3+ (d8, d3) have the largest OSPE (0.844 Delta_O); d0, d5(HS), d10 have none")
P("Spinels AB2O4 (A2+, B3+): normal (A tet, B oct) if OSPE(B3+) > OSPE(A2+) ; inverse if OSPE(A2+) > OSPE(B3+)")
sp = [("MgAl2O4", None, None, "normal (no CFSE for either)"), ("Fe3O4: Fe2+ 15 vs Fe3+ 0", 15, 0, "inverse"),
      ("NiFe2O4: Ni2+ 86 vs Fe3+ 0", 86, 0, "inverse"), ("Mn3O4: Mn2+ 0 vs Mn3+ 106", 0, 106, "normal"),
      ("Co3O4: Co2+ 29.3 vs LS Co3+ (large)", 29.3, 190, "normal")]
for nm, a, b, res in sp:
    P(f"  {nm:40s} -> {res}")
nt, ne = 6, 0
lfse_ls = 0.4 * 6 * 20760 * CM_TO_KJ - 2 * 0
P(f"  LS Co3+ in oxide: LFSE oct = 2.4 Delta_O ; with Delta_O ~ 20,760 cm-1 (aqua) the gain is {2.4*20760*CM_TO_KJ:.0f} kJ/mol before pairing cost 2P (P~229 kJ/mol for free Co3+) -> uses the low-spin state (S&A: Co3O4 normal because LS d6 Co(III) strongly favours oct)")
P("S&A Fig 20.13 (LFSE/Delta_O vs n): oct HS peaks 1.2 at d3, d8; tet (4/9) peaks 0.533 at d2, d7 -> max OSPE 0.844 at d3, d8")
dd = [(n, 0.4*oct_config(n,'high')[0]-0.6*oct_config(n,'high')[1], None) for n in range(11)]
P("OSPE/Delta_O by n:", [round(ospe(*oct_config(n, 'high'), n), 3) for n in range(11)])

# ---------------------------------------------------------------------------------------------
sec("I. Jahn-Teller: why d9, HS d4, LS d7 distort strongly (S&A Figs 20.11-20.12, H Fig 11.12)")
# E(Q) = 1/2 k Q^2 +/- alpha Q for the doubly degenerate eg^1 state; the lower branch has its minimum at Q0 = alpha/k.
k, al = 1.0, 1.0
Q0 = al / k
E0 = -al**2 / (2 * k)
P(f"model: E(Q) = k Q^2/2 +/- alpha Q ; lower branch minimum at Q0 = alpha/k with E_JT = -alpha^2/(2k) (k=alpha=1: Q0={Q0}, E_JT={E0})")
P("eg splitting under tetragonal elongation: dz2 goes down by d1/2, dx2-y2 up by d1/2; t2g: (dxz,dyz) down d2/3, dxy up 2 d2/3 (barycentre preserved)")
P("  d9: t2g^6 (net 0) + eg^3 = 2(-d1/2) + 1(+d1/2) = -d1/2   -> stabilised by d1/2")
P("  HS d4: t2g^3 eg^1 : net -d1/2 ; LS d7: t2g^6 eg^1 : net -d1/2")
P("  d1 t2g^1: net -d2/3 (one electron in the lower dxz,dyz pair) : weak, since d2 << d1 (the t2g orbitals do not point at the ligands)")
for nm, n_t, n_e in (("t2g^1", 1, 0), ("t2g^2", 2, 0), ("t2g^3 eg^1 (HS d4)", 3, 1), ("t2g^6 eg^3 (d9)", 6, 3)):
    P(f"  {nm:20s}: eg degenerate? {'yes' if n_e in (1, 3) else 'no'};  t2g degenerate and asymmetric? {'yes' if n_t in (1, 2, 4, 5) else 'no'}")
P("Jahn-Teller-active (S&A p.482): oct eg-type (strong): HS d4, LS d7, d9 ; t2g-type (weak): d1, d2, LS d4, LS d5, HS d6, HS d7")
P("[Cu(OH2)6]2+: S&A: static distortion below 20 K, dynamic above (EPR)")

# ---------------------------------------------------------------------------------------------
sec("J. Square planar vs tetrahedral for d8 (S&A p.481, H p.404)")
spread = lambda s_: (lambda E_: E_.max() - E_.min())(e4 + s_ * e2)
s13 = brentq(lambda s_: spread(s_) - 13.0, 0, 12)
P(f"square-planar total spread dx2-y2 -> dxz,dyz (S&A's Delta_SP, the sum of the three splittings): l=4 only {spread(0)/10:.2f} Delta_O ; with Huheey's l=2 weight s=12 {spread(s_fit)/10:.2f} Delta_O ; S&A's 'simple theory' 1.3 Delta_O needs s = {s13:.1f}")
P("  -> Delta_SP/Delta_O is model dependent (it depends on the ratio of the <r^2> and <r^4> radial integrals); quote 1.3 as S&A's rule of thumb, not as a derived constant")
P("d8, strong field: dxz,dyz,dz2,dxy filled (8 e-), dx2-y2 empty, so low-spin square planar if Delta_SP-induced gain > pairing + sterics")
P("  3d8 [NiX4]2- (X = halide): tetrahedral (small Delta, steric); [Ni(CN)4]2-: square planar; 4d8/5d8 (Rh(I), Ir(I), Pd(II), Pt(II), Au(III)): square planar (large Delta, small P)")

# ---------------------------------------------------------------------------------------------
sec("K. Ionic radii double dip (H Fig 11.15, caption data from Shannon-Prewitt) and Co(III) stability (H eq. 11.6-11.12)")
P("Divalent ions HS octahedral: radius falls d0->d3 (t2g filling), rises at d4 and d5 (eg filling points at ligands), falls again d6->d8, rises at d9, d10")
P("Co(II)/Co(III) couples (H): E(oxidation, V): aqua -1.83 ; ox -0.57 ; phen -0.42 ; edta -0.37 ; en -0.18 ; NH3 -0.11 ; CN(H2O) +0.83")
P("  as reduction potentials: E(Co3+/Co2+, aqua) = +1.83 V ; with en/NH3 ~ +0.18/+0.11 V ; the order follows the spectrochemical series (H p.411)")
P(f"  stabilisation of Co(III) by en vs aqua: {(1.83-0.18):.2f} V -> factor of {10**((1.83-0.18)/0.05916):.1e} in K_ox/K_red (one-electron couple, 25 degC)")
P("  CFSE argument: Co2+ HS d7 0.8 Delta_O -> Co3+ LS d6 2.4 Delta_O: gain 1.6 Delta_O (before pairing), H writes 1.8 -> 2.4 for the removal step")

# ---------------------------------------------------------------------------------------------
sec("L. Why the order inverts: angle between an orbital lobe and the nearest ligand (H p.401, S&A Fig 20.9)")
def ang(u, v):
    u, v = unit(u), unit(v)
    return math.degrees(math.acos(np.clip(u @ v, -1, 1)))
P("octahedron: ligand on +x.  eg lobe (dx2-y2 / dz2) along +x : %.1f deg ; t2g lobe (dxy, between +x and +y): %.1f deg" % (ang((1, 0, 0), (1, 0, 0)), ang((1, 1, 0), (1, 0, 0))))
P("tetrahedron: ligand along (1,1,1).  e lobe (along +x, face centre of the cube): %.1f deg ; t2 lobe (dxy, edge midpoint (1,1,0)): %.1f deg" % (ang((1, 0, 0), (1, 1, 1)), ang((1, 1, 0), (1, 1, 1))))
P("  -> t2 lobes are CLOSER to the ligands (35.3 deg) than e lobes (54.7 deg): t2 up, e down in a tetrahedron, the reverse of the octahedron")
P("  distance from lobe tip (distance 1) to the ligand (distance 1): oct t2g %.3f, tet t2 %.3f, tet e %.3f"
  % (2 * math.sin(math.radians(45) / 2), 2 * math.sin(math.radians(35.264) / 2), 2 * math.sin(math.radians(54.736) / 2)))
