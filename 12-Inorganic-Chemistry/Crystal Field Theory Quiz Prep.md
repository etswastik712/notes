---
title: Crystal Field Theory Quiz Prep
aliases: [CFT quiz prep, Quiz 3 prep, CH2113 Quiz 3, crystal field formula sheet, CFT self-test]
subject: chemistry
type: moc
scope: [taught]
by: [book, own-notes]
status: draft
tags: [subject/chemistry, type/moc, taught, src/book, src/own-notes, status/draft]
---
# Crystal Field Theory Quiz Prep (CH2113 Quiz 3)

◀ [[Inorganic Chemistry - Course Map|Course Map]] · chapter [[CH10 Crystal Field Theory]] · concepts: [[Crystal Field Theory]] · [[Crystal Field Splitting Parameter]] · [[Spectrochemical Series]] · [[Ligand Field Stabilization Energy]] · [[High-Spin and Low-Spin Complexes]] · [[Jahn-Teller Effect]] · [[Tetrahedral Crystal Field]] · [[Square-Planar Complexes]] · [[Octahedral Site Preference Energy]]

> [!info] The quiz
> **Tuesday 10 Nov 2026, TA session 12–1 pm.** Syllabus: crystal field theory and related, **not** molecular orbital theory. Lectures 2 Nov, 4 Nov, 9 Nov and the TA session of 3 Nov. Reading: S&A pp.473–483, Huheey pp.394–413. *I do not have the lecture notes of those sessions: compare this page against them and add anything the instructor stressed.*

> [!tip] How to use it
> 1. Read §1 once and be able to **write it from memory**. 2. Do §3 with the page covered. 3. Do §4 in one sitting, timed (about 35 minutes), then compare. 4. Anything missed twice goes on a card.

## 1. The formulas and tables that carry the topic
> [!key] Core
> - **Octahedral:** $e_g=+\frac35\Delta_O=+6Dq$, $t_{2g}=-\frac25\Delta_O=-4Dq$; $\Delta_O=10Dq$. **Tetrahedral:** $e=-\frac35\Delta_T$, $t_2=+\frac25\Delta_T$, $\Delta_T=\frac49\Delta_O$. **Barycentre fixed.**
> - **LFSE (oct):** $(-0.4\,n_t+0.6\,n_e)\Delta_O+(\text{extra pairs})P$; high spin never has a $P$ term.
> - **Spin state:** low spin iff $\Delta_O>P$ (for $d^4$, $d^5$, $d^6$ and $d^7$ alike).
> - **Moment:** $\mu=\sqrt{N(N+2)}\,\mu_B$: 1.73, 2.83, 3.87, 4.90, 5.92.
> - **Units:** $1\ \mathrm{cm^{-1}}=0.011963\ \mathrm{kJ\,mol^{-1}}=1.2398\times10^{-4}$ eV; $\lambda/\mathrm{nm}=10^7/(\tilde\nu/\mathrm{cm^{-1}})$.
> - **Anchor numbers:** $[\mathrm{Ti(OH_2)_6}]^{3+}$ 20 300 cm$^{-1}$ (493 nm, 243 kJ mol$^{-1}$, purple); $[\mathrm{Cr(OH_2)_6}]^{3+}$ 17 400; $[\mathrm{Co(NH_3)_6}]^{3+}$ 22 870; $[\mathrm{Fe(CN)_6}]^{3-}$ 35 000.

> [!key] LFSE table (octahedral, in $\Delta_O$)
> | $d^n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | high spin | 0 | 0.4 | 0.8 | 1.2 | 0.6 | 0 | 0.4 | 0.8 | 1.2 | 0.6 | 0 |
> | low spin | | | | | 1.6−$P$ | 2.0−2$P$ | 2.4−2$P$ | 1.8−$P$ | | | |
> | tetrahedral (in $\Delta_T$) | 0 | 0.6 | 1.2 | 0.8 | 0.4 | 0 | 0.6 | 1.2 | 0.8 | 0.4 | 0 |
> | unpaired $N$ (HS / LS) | 0 | 1 | 2 | 3 | 4 / 2 | 5 / 1 | 4 / 0 | 3 / 1 | 2 | 1 | 0 |

> [!key] Series to memorise
> - **Ligands:** $\mathrm{I^-<Br^-<Cl^-<F^-<OH^-<H_2O<NH_3<en<bpy<NO_2^-<CN^-<CO}$ (halides low, $\pi$-acceptors high).
> - **Metals:** $\mathrm{Mn^{2+}<Ni^{2+}<Co^{2+}<Fe^{2+}<V^{2+}<Fe^{3+}<Co^{3+}<Mo^{3+}<Rh^{3+}<Ru^{3+}<Pd^{4+}<Ir^{3+}<Pt^{4+}}$.
> - **Irving–Williams:** $\mathrm{Ba<Sr<Ca<Mg<Mn<Fe<Co<Ni<Cu>Zn}$.
> - **Jahn–Teller strong:** HS $d^4$, LS $d^7$, $d^9$. **Weak:** $d^1$, $d^2$, LS $d^4$, LS $d^5$, HS $d^6$, HS $d^7$.
> - **Square planar:** $d^8$, strong field or $4d/5d$. **OSPE largest:** $d^3$, $d^8$ ($0.844\Delta_O$). **None:** $d^0$, HS $d^5$, $d^{10}$.

## 2. Twelve traps
> [!pitfall] Traps
> 1. **$e_g$ is up in an octahedron, $e$ is *down* in a tetrahedron.** The tetrahedral $t_2$ lobes are closer to the ligands ($35.3^\circ$ vs $54.7^\circ$).
> 2. **$\Delta_T=\frac49\Delta_O$**, not $\frac94$. Use $\frac94$ the other way round (from a tetrahedral value to the octahedral one).
> 3. **No pairing energy for high spin.** For low-spin $d^6$ the term is $2P$ (three pairs minus the one already there in the free ion).
> 4. **Weak field = high spin = small $\Delta_O$**: $\mathrm{F^-}$, $\mathrm{Cl^-}$, $\mathrm{I^-}$. Strong field = low spin: $\mathrm{CN^-}$, $\mathrm{CO}$, en, bpy.
> 5. **$d^1$–$d^3$ and $d^8$–$d^{10}$ have no high/low spin** in an octahedron.
> 6. **$4d$/$5d$ are low spin** even with $\mathrm{Cl^-}$ ($[\mathrm{RuCl_6}]^{2-}$ is $t_{2g}^4$).
> 7. **Colour is the complementary colour of the absorbed light** and $d^0$/$d^{10}$ are colourless (no $d$–$d$).
> 8. **Spin-only fails for low-spin $d^5$ and HS $d^6$, $d^7$** (orbital contribution); it is a *lower bound* there.
> 9. **Square planar $\ne$ tetrahedral $d^8$**: $[\mathrm{Ni(CN)_4}]^{2-}$ diamagnetic square planar; $[\mathrm{NiCl_4}]^{2-}$ paramagnetic tetrahedral.
> 10. **Jahn–Teller predicts instability, not the shape**; elongation is commoner than compression.
> 11. **The series is not electrostatic:** $\mathrm{OH^-}<\mathrm{H_2O}$ and $\mathrm{NH_3}>\mathrm{H_2O}$; do *not* explain it with CFT point charges.
> 12. **Sign convention of LFSE:** S&A write positive stabilisation numbers, "LFSE $=0.4\Delta_O$" = 0.4$\Delta_O$ **below** the barycentre. Say "stabilisation".

## 3. Derivations to be able to reproduce
> [!derivation] (a) Barycentre rule → $\frac35,\frac25$ → and $\frac49$
> Octahedron: $2x-3y=0$, $x+y=\Delta_O$ ⇒ $x=\frac35\Delta_O$, $y=\frac25\Delta_O$. Tetrahedron: same algebra with $e$ below, $t_2$ above. Size: sum over ligands of $X_4=x^4+y^4+z^4-\frac35$: octahedron $6\times\frac25=\frac{12}5$; tetrahedron $4\times(-\frac4{15})=-\frac{16}{15}$; ratio $-\frac49$ (S&A: "$\Delta_T\approx\frac49\Delta_O$").
> (b) **Crossover:** $E_{LS}-E_{HS}=-n\Delta_O+nP$ with $n=1$ ($d^4,d^7$) or $2$ ($d^5,d^6$): zero at $\Delta_O=P$.
> (c) **$d^9$ Jahn–Teller:** $2(-\delta_1/2)+(+\delta_1/2)=-\delta_1/2$.
> (d) **Why OSPE peaks at $d^3,d^8$:** $\mathrm{LFSE}_{oct}=1.2\Delta_O$, $\mathrm{LFSE}_{tet}=0.8\Delta_T=0.356\Delta_O$, difference $0.844\Delta_O$.
> (e) **Hydration enthalpy:** subtract $\mathrm{LFSE}\times\Delta_O$ (in kJ) from the observed $-\Delta_{hyd}H$ and the double hump becomes smooth.

## 4. Self-test (35 minutes)
1. **(4)** Draw the splitting for an octahedral and a tetrahedral complex of the same metal and ligand and give the relation between $\Delta_T$ and $\Delta_O$.
2. **(5)** For each of $[\mathrm{Mn(OH_2)_6}]^{2+}$, $[\mathrm{Mn(CN)_6}]^{4-}$, $[\mathrm{Ni(OH_2)_6}]^{2+}$, $[\mathrm{Fe(CN)_6}]^{4-}$, $[\mathrm{CoF_6}]^{3-}$ give the configuration, $N$, $\mu_{so}$ and LFSE.
3. **(3)** $[\mathrm{Fe(OH_2)_6}]^{3+}$ has $\Delta_O=14\,000$ cm$^{-1}$ and $[\mathrm{Fe(CN)_6}]^{3-}$ 35 000. Free-ion $P=29\,900$. Predict the spin states and the magnetic moments.
4. **(3)** A complex absorbs at 530 nm. Give $\tilde\nu$ and the energy in kJ mol$^{-1}$ and say what colour it is.
5. **(3)** Explain why $\mathrm{Cu^{2+}}$ complexes are tetragonally elongated, sketching the splitting and the net gain.
6. **(3)** Why is $[\mathrm{PtCl_4}]^{2-}$ square planar whereas $[\mathrm{NiCl_4}]^{2-}$ is tetrahedral?
7. **(3)** Account for the double-humped hydration enthalpies of $\mathrm{M^{2+}}$ in the first row.
8. **(3)** Predict normal or inverse: $\mathrm{Mn_3O_4}$, $\mathrm{Fe_3O_4}$, $\mathrm{NiFe_2O_4}$.
9. **(2)** Why do anionic ligands such as $\mathrm{OH^-}$ lie *below* water in the spectrochemical series, and what does this say about the model?
10. **(2)** Using $\Delta_O=f\,g$ with $f(\mathrm{NH_3})=1.25$, $g(\mathrm{Co^{III}})=18.2$ kK, estimate $\Delta_O$ of $[\mathrm{Co(NH_3)_6}]^{3+}$ and compare with 22 870.

> [!example]- Answers
> 1. $O_h$: $t_{2g}$ ($-0.4\Delta_O$) below $e_g$ ($+0.6\Delta_O$); $T_d$: $e$ ($-0.6\Delta_T$) below $t_2$ ($+0.4\Delta_T$); $\Delta_T=\frac49\Delta_O$ (fewer ligands, none pointing at an orbital).
> 2. $\mathrm{Mn^{2+}}$ ($d^5$) aqua: $t_{2g}^3e_g^2$, $N=5$, 5.92, LFSE 0. $[\mathrm{Mn(CN)_6}]^{4-}$: $t_{2g}^5$, $N=1$, 1.73, LFSE $2.0\Delta_O-2P$. $\mathrm{Ni^{2+}}$ ($d^8$): $t_{2g}^6e_g^2$, $N=2$, 2.83, $1.2\Delta_O$. $[\mathrm{Fe(CN)_6}]^{4-}$ ($d^6$ LS): $t_{2g}^6$, $N=0$, 0, $2.4\Delta_O-2P$. $[\mathrm{CoF_6}]^{3-}$ ($d^6$ HS): $t_{2g}^4e_g^2$, $N=4$, 4.90, $0.4\Delta_O$.
> 3. $14\,000<29\,900$: **high spin**, $t_{2g}^3e_g^2$, $\mu=5.92\,\mu_B$ (S&A: 5.9 observed). $35\,000>29\,900$: **low spin**, $t_{2g}^5$, $\mu\approx1.73\,\mu_B$ spin-only, observed 2.3 (orbital contribution).
> 4. $\tilde\nu=10^7/530=18\,900$ cm$^{-1}$; $E=18\,900\times0.011963=226$ kJ mol$^{-1}$; absorbs green, appears **magenta/purple-red**.
> 5. $d^9=t_{2g}^6e_g^3$ has a degenerate $e_g$ with 3 electrons; elongation lowers $d_{z^2}$ and raises $d_{x^2-y^2}$ by $\delta_1/2$ each; $2(-\delta_1/2)+(+\delta_1/2)=-\delta_1/2$; $t_{2g}^6$ no net change.
> 6. $5d^8$, large $\Delta$ and small $P$: a large gap puts the empty $d_{x^2-y^2}$ far above the filled orbitals so square planar is stabilised; $3d^8$ with small $\Delta$ (and steric repulsion of four chlorides) stays tetrahedral.
> 7. Hydration enthalpy rises with decreasing radius, plus the LFSE (0 for $d^0,d^5,d^{10}$, maximal for $d^3$, $d^8$); two humps; subtracting the LFSE gives a smooth curve (S&A Fig. 20.7).
> 8. $\mathrm{Mn_3O_4}$ normal ($\mathrm{Mn^{3+}}$ OSPE 106 kJ vs 0); $\mathrm{Fe_3O_4}$ inverse ($\mathrm{Fe^{2+}}$ ≈15 vs $\mathrm{Fe^{3+}}$ 0); $\mathrm{NiFe_2O_4}$ inverse ($\mathrm{Ni^{2+}}$ 86 vs 0).
> 9. A negative point charge should split more than a neutral dipole; the series is not electrostatic, it needs $\sigma$ and $\pi$ bonding (ligand-field theory), so pure CFT is incomplete.
> 10. $1.25\times18.2=22.75$ kK $=22\,750$ cm$^{-1}$ vs 22 870: within 1 %.

## 5. Check against the lectures
> [!todo] Things to confirm when the lecture notes of 2, 3, 4 and 9 Nov are available
> - which sign convention for LFSE the lectures used, and whether "CFSE" or "LFSE";
> - whether tetragonal distortion and the **Jahn–Teller effect**, **Irving–Williams** and **spinels** were reached (S&A covers them; the announcement's range ends p.483);
> - whether **Tanabe–Sugano** or **electronic spectra** were mentioned (S&A §20.3–20.4): excluded by the announcement, but check;
> - any **TA-session problems** (3 Nov): add them to [[CH10 Crystal Field Theory]] under Practice with provenance, following the vault's new-material rule.
