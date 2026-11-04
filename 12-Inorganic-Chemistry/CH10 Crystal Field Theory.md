---
title: CH10 Crystal Field Theory
aliases: [CH10, crystal field theory, CFT, ligand field splitting, d-orbital splitting, LFSE, CFSE, spectrochemical series, Jahn-Teller, CH2113 Quiz 3, Shriver Atkins Chapter 20.1]
subject: chemistry
type: chapter
chapter: 10
part: III
scope: [taught, extra-beyond]
by: [book]
status: draft
prereq: ["[[CH02 Molecular Orbital Theory Diatomics]]", "[[CH09 Redox]]"]
tags: [subject/chemistry, type/chapter, taught, extra/beyond, src/book, src/own-notes, status/draft]
---
# CH10 · Crystal Field Theory

◀ [[CH09 Redox]] · [[Inorganic Chemistry - Course Map|Course Map]] · revision: [[Crystal Field Theory Quiz Prep]]

<span class="scope-taught">taught · in syllabus (Quiz 3)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: Quiz 3, Tuesday 10 Nov 2026, 12–1 pm (TA session)
> The announcement (NB, 2026-11-04): **Crystal Field Theory and related, *not* molecular orbital theory**; content from the lectures of **2 Nov, the TA session of 3 Nov, 4 Nov and 9 Nov**. Reading: **Shriver and Atkins 5th ed., pp. 473–483** ([[Shriver and Atkins Inorganic Chemistry 5th Ed.pdf#page=500|PDF pp.500–510]]; printed page = PDF − 27) and **Huheey, Keiter and Keiter 4th ed., pp. 394–413** ([[7_Inorganic_Chemistry_by_Huheey_E_Keiter_and_R_Keiter.pdf#page=411|PDF pp.411–430]]; printed page = PDF − 17).
>
> 🟢 **Taught / in the reading range** (no slides or lecture notes of these four sessions are in the folder yet; the scope below is the assigned book pages)
> - §1–2 the electrostatic model, the five $d$ orbitals, **octahedral splitting** $t_{2g}/e_g$, $\Delta_O=10Dq$, the barycentre rule, $[\mathrm{Ti(OH_2)_6}]^{3+}$ (S&A §20.1a; Huheey pp.394–399)
> - §3 factors fixing $\Delta_O$: **spectrochemical series**, metal series, oxidation state, 3d<4d<5d, Jørgensen $f\,g$ (S&A p.475; Huheey pp.404–408)
> - §4 **LFSE**, pairing energy, **high spin / low spin**, Tables 20.2 and 11.3–11.4 (S&A §20.1b; Huheey pp.399–402)
> - §5 **magnetic moments**, spin-only formula, orbital contribution (S&A §20.1c)
> - §6 **tetrahedral** complexes, $\Delta_T\approx\frac49\Delta_O$ (S&A §20.1e; Huheey pp.401–403)
> - §7 **square planar** and tetragonal complexes; other geometries, Huheey Table 11.5 (S&A §20.1f; Huheey pp.403–405)
> - §8 **Jahn–Teller effect** (S&A §20.1g)
> - §9 **applications**: hydration and lattice enthalpies, ionic radii, Irving–Williams series, stability of oxidation states (Co(III)), octahedral vs tetrahedral preference, **spinels** (S&A §20.1d,h,i; Huheey pp.408–413)
> - §10 limits of CFT: the **nephelauxetic effect** and the pointer to ligand-field theory (S&A §20.2 opening; Huheey p.413)
>
> 🔵 **Extra · beyond** (my additions; all numbers in `scripts/ch10_numbers.py`)
> - §2 the point-charge splitting **computed from first principles** (the harmonic $x^4+y^4+z^4$ argument, and a numerical calculation that reproduces Huheey's Table 11.5 rows for octahedral, tetrahedral, cubic, square planar and linear fields)
> - §3 the Jørgensen rule **tested on 14 complexes**; §4 the crossover $\Delta_O=P$ derived for all of $d^4$–$d^7$ and tested on 8 complexes
> - §9 hydration enthalpies **recomputed**, the oxide and fluoride lattice-enthalpy examples, OSPE reproduced to the book's numbers
>
> **Not covered, by the announcement:** molecular orbital (ligand-field) theory of complexes, SALCs, $\pi$-bonding, electronic spectra and Tanabe–Sugano diagrams (S&A §20.2 onward).

> [!warning] What is and is not in the sources
> I have the two books but **not the lecture notes of 2, 4 and 9 Nov or the TA session of 3 Nov**; the quiz will follow those. Everything here is built from the assigned pages. Where the lectures may differ (notation $\Delta_O$ vs $10Dq$, how much of $\S$7 and $\S$10 was shown), the tags are `[verify]`. Two **book slips** found while recomputing: Huheey p.399 prints "338 kJ mol$^{-1}$" for 32,500 cm$^{-1}$ (it is **389**), and Huheey's Table 11.6 gives 7900 cm$^{-1}$ for VCl$_4$ where S&A Table 20.5 gives 9010.

> [!key] After this chapter you can
> - draw the $d$-orbital splitting for **octahedral, tetrahedral, square planar and tetragonally distorted** complexes and say which orbitals go up and why (lobes pointing at, or between, the ligands),
> - state and use the **barycentre rule** to get $\pm\frac35\Delta_O$, $\mp\frac25\Delta_O$ and the tetrahedral $\Delta_T=\frac49\Delta_O$,
> - compute the **LFSE** of any $d^n$ (oct high/low spin, tet), including pairing terms, and predict **high or low spin** from $\Delta_O$ versus $P$,
> - rank ligands (**spectrochemical series**) and metal ions, and explain why $\Delta_O$ rises with oxidation state and down a group,
> - predict **magnetic moments** (spin-only $\sqrt{N(N+2)}\,\mu_B$) and say when orbital angular momentum spoils them,
> - explain **Jahn–Teller** distortions, the double-humped **hydration/lattice enthalpy** curves, the **Irving–Williams series**, **spinel** site preferences, and why Co(III) is stable only with strong-field ligands,
> - say what crystal-field theory **cannot** explain and why one needs ligand-field theory.

> [!intuition] The one-sentence story
> A free ion has five equal $d$ orbitals; put negative charges around it and the orbitals that point **at** the charges are pushed up more than the ones that point **between** them. The resulting small splitting (about 10 % of the bonding energy) decides colour, magnetism, geometry and a surprising amount of thermodynamics.

> [!intuition] Why this is the right level of model
> The metal–ligand bond is mostly "stability from attraction between opposite charges". The $d$ orbitals are **non-bonding-ish** electrons sitting in that field. CFT ignores overlap entirely and still gets the **pattern** of properties right, because the pattern is dictated by **symmetry**, which the point-charge model and the full MO model share (Huheey p.395). That is why it is both wrong in detail and indispensable.

---

## 1. The five d orbitals and the electrostatic model

In **crystal-field theory** a ligand lone pair is replaced by a **point negative charge** (or the negative end of a dipole) which repels the metal $d$ electrons (S&A p.473). Only the **differential** repulsion of the five $d$ orbitals matters.

![[sa_fig20_1_d_orbitals_in_octahedron.png]]
*Figure CH10.1 (book crop). S&A Fig. 20.1: the five $d$ orbitals in an octahedron of six ligands (black dots). The two $e_g$ orbitals ($d_{z^2}$, $d_{x^2-y^2}$) point **at** the ligands; the three $t_{2g}$ orbitals ($d_{xy},d_{yz},d_{zx}$) point **between** them.*

![[huheey_fig11_3_d_orbitals.png]]
*Figure CH10.2 (book crop). Huheey Fig. 11.3: the five $d$ orbitals with the lobes drawn on the axes. Note the "doughnut" (collar) of $d_{z^2}$ in the $xy$ plane, often forgotten.*

> [!key] The $d_{z^2}$ orbital is a mixture (Huheey p.395)
> There are six four-lobed wavefunctions ($d_{xy},d_{yz},d_{zx},d_{x^2-y^2},d_{y^2-z^2},d_{z^2-x^2}$) but only five independent orbitals. The $d_{z^2}$ orbital stands for $d_{2z^2-x^2-y^2}$, the combination of $d_{z^2-x^2}$ and $d_{z^2-y^2}$: lobes on the $z$ axis plus a torus in the $xy$ plane.

> [!example] Spherical field first
> In a hypothetical **spherical shell** of charge all five orbitals rise by the same amount (repulsion) and stay degenerate. Real ligands sit at points, break the spherical symmetry, and **split** the set without changing the average energy: the **barycentre rule** below.

> [!pitfall] The repulsion is not the whole story
> The splitting is only about 10 % of the total metal–ligand energy (S&A p.474): most of the stability comes from the attraction. Subtracting the "spherical" rise is why the diagrams show only relative energies.

---

## 2. The octahedral field

Put six ligands on $\pm x,\pm y,\pm z$. Group theory ([[Symmetry Labels a b e t]], the $O_h$ character table; Huheey p.398) shows that $d_{z^2},d_{x^2-y^2}$ transform as $E_g$ and $d_{xy},d_{yz},d_{zx}$ as $T_{2g}$: **2 + 3**, which is why the orbitals split into a doubly degenerate **$e_g$** set (up) and a triply degenerate **$t_{2g}$** set (down). Symmetry says *that* they split, not *which way*; the electrostatics says $e_g$ is higher because those lobes point at the charges.

![[fig_ch10_splitting.png]]
*Figure CH10.3. A: the point-charge energies in units of $Dq$ for octahedral, tetrahedral and square-planar fields, **computed** (the square-planar column and the right panel reproduce Huheey Table 11.5 and Fig. 11.12). B: the continuous path from the octahedron to the square-planar limit as the two trans ligands are removed.*

### 2.1 The splitting parameter and the barycentre

$$\Delta_O\;(=10\,Dq)\;=\;E(e_g)-E(t_{2g}).$$

> [!derivation] Why $+\tfrac35\Delta_O$ and $-\tfrac25\Delta_O$
> The average energy of the five orbitals is unchanged by redistributing the ligand charge from a sphere to six points (the **barycentre rule**, valid for every geometry; Huheey p.398, S&A Fig. 20.2). With $e_g$ at $+x$ and $t_{2g}$ at $-y$:
> $$2x+3(-y)=0,\qquad x-(-y)=\Delta_O\;\Rightarrow\; x=\tfrac35\Delta_O,\; y=\tfrac25\Delta_O.$$
> In $Dq$: $e_g=+6\,Dq$, $t_{2g}=-4\,Dq$.

> [!derivation] Where the numbers come from, from first principles (🔵)
> Expand the potential of point charges at $\mathbf R_i$ in spherical harmonics. The $l=0$ term shifts all five orbitals together; $l=2$ and $l=4$ do the splitting. For a **cubic** arrangement ($O_h$, $T_d$, cube) the $l=2$ term vanishes and the splitting is proportional to $\sum_i X_4(\hat R_i)$ with $X_4=x^4+y^4+z^4-\tfrac35$ on the unit sphere.
> - octahedron (6 vertices $(\pm1,0,0)$…): $X_4=1-\tfrac35=+\tfrac25$ each, sum $=+\tfrac{12}{5}$
> - cube (8 corners $(\pm1,\pm1,\pm1)/\sqrt3$): $X_4=\tfrac13-\tfrac35=-\tfrac4{15}$ each, sum $=-\tfrac{32}{15}$, ratio to the octahedron $=-\tfrac89$
> - tetrahedron (4 of the 8 corners): sum $=-\tfrac{16}{15}$, ratio $=-\tfrac49$.
>
> Hence **$\Delta_T=\tfrac49\Delta_O$ with inverted order** (§6). A numerical angular integration over the $d$ orbitals gives exactly $[-4,-4,-4,+6,+6]$ for $O_h$, $[-2.67,-2.67,+1.78,+1.78,+1.78]$ for $T_d$ and $[-5.33,\,3.56]$ for the cube $Dq$ values of the book's table.

### 2.2 $d^1$: reading $\Delta_O$ off a spectrum

For one electron the energy of the transition $e_g\leftarrow t_{2g}$ **is** $\Delta_O$. $[\mathrm{Ti(OH_2)_6}]^{3+}$ ($d^1$) absorbs at $\tilde\nu_{\max}=20\,300\ \mathrm{cm^{-1}}$ ($\lambda=493$ nm).

![[sa_fig20_3_ti_spectrum.png]]
![[huheey_fig11_8_ti_spectrum.png]]
*Figure CH10.4 (book crops). The absorption of $[\mathrm{Ti(OH_2)_6}]^{3+}$, S&A Fig. 20.3 (left) and Huheey Fig. 11.8 (right, with the colour scale). The band (with a shoulder, a hint of the Jahn–Teller distortion of the excited state) removes blue–green light, so the ion looks **purple** (the complementary colour).*

> [!example] Unit conversions (computed)
> $20\,300\ \mathrm{cm^{-1}}=\mathbf{243}\ \mathrm{kJ\,mol^{-1}}=2.52$ eV, $\lambda=10^7/20\,300=493$ nm (rule: $1\ \mathrm{cm^{-1}}=0.011963$ kJ mol$^{-1}$). For $\mathrm{ReF_6}$ (also $d^1$), $32\,500\ \mathrm{cm^{-1}}=\mathbf{389}$ kJ mol$^{-1}$ ($\lambda=308$ nm, ultraviolet) — Huheey prints 338, a transposed digit `[verify]`. Both are "of the same order as a chemical bond".

![[sa_fig20_2_octahedral_levels.png]]
![[huheey_fig11_7_octahedral_splitting.png]]
*Figure CH10.5 (book crops). The octahedral level diagram: S&A Fig. 20.2 (left) and Huheey Fig. 11.7 (right; the dashed line is the spherical-field level, the dotted one the barycentre).*

> [!pitfall] $\Delta_O$ for $d^n$, $n>1$ is not simply a transition energy
> With more than one electron the absorption energies also contain electron–electron repulsion (S&A §20.4, outside the quiz). The values in Table 20.1 come from that fuller analysis. Only $d^1$ (and $d^9$) give $\Delta_O$ directly.

---

## 3. What decides $\Delta_O$

![[fig_ch10_spectro.png]]
*Figure CH10.6. A: Jørgensen's ligand factors $f$ (Huheey Table 11.7, water = 1.00). B: the rule $\Delta_O=f\,g$ against observed values for 14 complexes (computed; the orange points are more than 15 % off).*

### 3.1 The ligand: the spectrochemical series

Ordering ligands by the energy of the first $d$–$d$ transition gives the same order for every metal (S&A p.475):

$$\mathrm{I^-<Br^-<S^{2-}<SCN^-<Cl^-<ONO^-<N_3^-<F^-<OH^-<C_2O_4^{2-}<O^{2-}<H_2O<NCS^-<MeCN<py<NH_3<en<bpy<phen<NO_2^-<PPh_3<CN^-<CO}$$

(the book underlines the donor atom of an ambidentate ligand: $\mathrm{SCN^-}$ is S-bonded, $\mathrm{NCS^-}$ N-bonded, $\mathrm{ONO^-}$ (nitrito) O-bonded but $\mathrm{NO_2^-}$ (nitro) N-bonded, the latter far higher; see [[Ambidentate Ligand]] and [[Linkage Isomerism]]). Huheey (p.405) gives a slightly different overlapping list (to $\mathrm{CO}$ at the top). **Weak-field** = low in the series ($\mathrm{I^-}$, $\mathrm{Br^-}$, $\mathrm{Cl^-}$, $\mathrm{F^-}$), **strong-field** = high ($\mathrm{CN^-}$, $\mathrm{CO}$).

> [!example] The colours of $[\mathrm{CoX(NH_3)_5}]^{n+}$ (S&A p.475)
> $\mathrm X=\mathrm I^-$: purple; $\mathrm{Cl^-}$: pink; … $\mathrm{NH_3}$: yellow (the book's series $\mathrm X=\mathrm I^-,\mathrm{Br^-},\mathrm{Cl^-},\mathrm{H_2O},\mathrm{NH_3}$). The lowest absorption moves from the red/green into the blue as $\mathrm X$ goes up the series: $\Delta_O$ increases and the **complementary colour** shifts from purple to yellow.

### 3.2 The metal

S&A p.475: $\mathrm{Mn^{2+}<Ni^{2+}<Co^{2+}<Fe^{2+}<V^{2+}<Fe^{3+}<Co^{3+}<Mo^{3+}<Rh^{3+}<Ru^{3+}<Pd^{4+}<Ir^{3+}<Pt^{4+}}$. Three rules:
- **oxidation state:** $\Delta_O$ rises with charge (smaller ion, shorter M–L, stronger interaction): $[\mathrm{Ru(OH_2)_6}]^{2+}$ 19 800 → $[\mathrm{Ru(OH_2)_6}]^{3+}$ 28 600 cm$^{-1}$ (Huheey Table 11.6); $\mathrm{Fe^{2+}}$ 10 400 → $\mathrm{Fe^{3+}}$ 14 300 (S&A Table 20.1);
- **down a group:** $3d<4d<5d$, by up to 50 % from $3d$ to $4d$ and ~25 % more to $5d$ (larger orbitals overlap better): $\mathrm{Co^{3+}}$ 20 700, $\mathrm{Rh^{3+}}$ 27 000 for $\mathrm{H_2O}$; **so $4d$/$5d$ complexes are almost always low spin**;
- **number of ligands:** $\Delta_T\approx\frac49\Delta_O$ (§6).

> [!key] Jørgensen's $\Delta_O=f\,g$ (Huheey eq. 11.5, Tables 11.7)
> $f$ (ligand, water = 1.00) from 0.72 ($\mathrm{Br^-}$) to 1.70 ($\mathrm{CN^-}$); $g$ (metal ion) from 8.0 ($\mathrm{Mn^{2+}}$) to 36 kK ($\mathrm{Pt^{4+}}$) ($1\ \mathrm{kK}=1000\ \mathrm{cm^{-1}}$). **Computed test (🔵):** over 14 complexes the mean error is **7 %**: $[\mathrm{Cr(OH_2)_6}]^{3+}$ $1.00\times17.4=17\,400$ (obs. 17 400), $[\mathrm{Cr(en)_3}]^{3+}$ $1.28\times17.4=22\,270$ (22 300), $[\mathrm{Co(NH_3)_6}]^{3+}$ $1.25\times18.2=22\,750$ (22 870), $[\mathrm{Rh(NH_3)_6}]^{3+}$ 33 750 (34 100); the failures are **$[\mathrm{Fe(CN)_6}]^{3-}$ (−32 %)** and $[\mathrm{CoF_6}]^{3-}$ (+25 %). `[verify]` the $f$ for $\mathrm{Cl^-}$ and $g$ for $\mathrm{Co^{2+}}$ were garbled in the OCR of the table.

### 3.3 What crystal-field theory cannot explain

If the splitting were purely electrostatic, **anions** should split most. Instead (Huheey p.407): most anionic ligands lie at the **low** end; $\mathrm{OH^-}$ lies **below** neutral $\mathrm{H_2O}$; $\mathrm{NH_3}$ splits more than $\mathrm{H_2O}$ although $\mu(\mathrm{H_2O})=6.17\times10^{-30}$ C m exceeds $\mu(\mathrm{NH_3})=4.90\times10^{-30}$ C m; and for strong-field ligands such as $\mathrm{CN^-}$, $\Delta_O$ barely changes within a group. These facts need **covalency, $\sigma$ donation and $\pi$ donation/acceptance**: ligand-field theory (S&A §20.2, outside this quiz).

---

## 4. Filling the orbitals: LFSE, pairing and spin state

For $d^1$–$d^3$ the electrons go singly into $t_{2g}$ with parallel spins. For $d^4$ there is a choice, between

- **$t_{2g}^3e_g^1$** (high spin): pay $\Delta_O$ to avoid pairing, and
- **$t_{2g}^4$** (low spin): pay the **pairing energy $P$**.

$$\text{high spin if }\Delta_O<P\ (\text{weak field}),\qquad \text{low spin if }\Delta_O>P\ (\text{strong field}).$$

> [!key] The pairing energy (Huheey p.401)
> $P$ has two parts: the **Coulomb repulsion** of two electrons in one orbital (smaller for the larger $4d$/$5d$ orbitals) and the **loss of exchange energy** when parallel spins are forced antiparallel (largest for $d^5$, which has the most parallel pairs). Free-ion values (Huheey Table 11.4, kJ mol$^{-1}$ / cm$^{-1}$, $P=P_c+P_e$): $\mathrm{Cr^{2+}}$ ($d^4$) 244 / 20 400, $\mathrm{Mn^{2+}}$ ($d^5$) 285 / 23 800, $\mathrm{Fe^{3+}}$ ($d^5$) 357 / 29 900, $\mathrm{Fe^{2+}}$ ($d^6$) 174 / 14 600, $\mathrm{Co^{3+}}$ ($d^6$) 229 / 19 200 (sums verified). In complexes $P$ is 15–30 % **smaller** (nephelauxetic effect, §10). That is why **$d^5$ ions ($\mathrm{Mn^{2+}}$, $\mathrm{Fe^{3+}}$) are usually high spin**.

### 4.1 Ligand-field stabilisation energy

Each $t_{2g}$ electron contributes $-0.4\Delta_O$, each $e_g$ $+0.6\Delta_O$:
$$\mathrm{LFSE}=(-0.4\,n_{t}+0.6\,n_{e})\Delta_O+(\text{extra pairs})\,P.$$
**Only the pairing in excess of the spherical (Hund) configuration is counted** (S&A p.477), so high-spin complexes carry no $P$ term.

![[fig_ch10_spin.png]]
*Figure CH10.7. A: the two ground states of $d^4$–$d^7$ with the LFSE of S&A Table 20.2. B: $E_{LS}-E_{HS}$ against $\Delta_O/P$ for all four: **every line crosses zero at $\Delta_O=P$**. C: the free-ion $\Delta_O$ versus $P$ criterion against the observed spin states of eight complexes (eight of eight correct).*

| $d^n$ | high spin | $N$ | LFSE/$\Delta_O$ | low spin | $N$ | LFSE/$\Delta_O$ |
|---|---|---|---|---|---|---|
| $d^1$ | $t_{2g}^1$ | 1 | −0.4 | — | | |
| $d^2$ | $t_{2g}^2$ | 2 | −0.8 | — | | |
| $d^3$ | $t_{2g}^3$ | 3 | −1.2 | — | | |
| $d^4$ | $t_{2g}^3e_g^1$ | 4 | −0.6 | $t_{2g}^4$ | 2 | −1.6 + $P$ |
| $d^5$ | $t_{2g}^3e_g^2$ | 5 | 0 | $t_{2g}^5$ | 1 | −2.0 + 2$P$ |
| $d^6$ | $t_{2g}^4e_g^2$ | 4 | −0.4 | $t_{2g}^6$ | 0 | −2.4 + 2$P$ |
| $d^7$ | $t_{2g}^5e_g^2$ | 3 | −0.8 | $t_{2g}^6e_g^1$ | 1 | −1.8 + $P$ |
| $d^8$ | $t_{2g}^6e_g^2$ | 2 | −1.2 | — | | |
| $d^9$ | $t_{2g}^6e_g^3$ | 1 | −0.6 | — | | |
| $d^{10}$ | $t_{2g}^6e_g^4$ | 0 | 0 | — | | |

(S&A tabulate the stabilisation as positive numbers; I keep the sign of an energy, so "LFSE = −0.4" means 0.4$\Delta_O$ *below* the barycentre. Both conventions appear; quote the magnitude and say "stabilisation".) Reproduced in `ch10_numbers.py §B`.

> [!derivation] Why all four spin-state crossovers are at $\Delta_O=P$ (🔵)
> From the table, the energy difference low − high spin is
> $$E_{LS}-E_{HS}=-(\Delta\text{LFSE})\,\Delta_O+(\Delta\text{pairs})\,P:\quad d^4:\ -1.0\Delta_O+1P;\ d^5:\ -2.0\Delta_O+2P;\ d^6:\ -2.0\Delta_O+2P;\ d^7:\ -1.0\Delta_O+1P.$$
> Each has the same **ratio** of $\Delta_O$-gain to $P$-cost (the number of electrons moved from $e_g$ to $t_{2g}$ equals the number of extra pairs formed), so each vanishes at **$\Delta_O=P$**. Because $P$ depends on the ion ($d^5$ largest) and $\Delta_O$ on ligand and metal, the switch point in the spectrochemical series is **not universal** (S&A p.477), but the criterion is.

> [!example] Examples to know (computed in `§F`)
> | complex | $\Delta_O$ (cm$^{-1}$) | $P$ free ion | $\Delta_O/P$ | state |
> |---|---|---|---|---|
> | $[\mathrm{Fe(OH_2)_6}]^{3+}$ | 14 000 | 29 900 | 0.47 | high spin |
> | $[\mathrm{Fe(CN)_6}]^{3-}$ | 35 000 | 29 900 | 1.17 | low spin |
> | $[\mathrm{Fe(OH_2)_6}]^{2+}$ | 10 400 | 14 600 | 0.71 | high spin |
> | $[\mathrm{Fe(CN)_6}]^{4-}$ | 32 200 | 14 600 | 2.21 | low spin |
> | $[\mathrm{CoF_6}]^{3-}$ | 13 100 | 19 200 | 0.68 | high spin |
> | $[\mathrm{Co(OH_2)_6}]^{3+}$ | 20 760 | 19 200 | 1.08 | low spin (borderline, correct) |
> | $[\mathrm{Co(NH_3)_6}]^{3+}$ | 22 870 | 19 200 | 1.19 | low spin |
> | $[\mathrm{Ru(ox)_3}]^{3-}$ vs $[\mathrm{Fe(ox)_3}]^{3-}$ | | | | low vs high spin (S&A p.477) |

> [!pitfall] The common slips
> - **Never** count $P$ for a high-spin complex (no extra pairs). For low-spin $d^6$ the pairs are *three*, but the free ion already has one, so the term is **2$P$**.
> - **$d^1$–$d^3$ and $d^8$–$d^{10}$ have no high/low-spin choice** in an octahedron (S&A Table 20.2; use no label).
> - $4d$ and $5d$ ions are low spin **even with weak-field ligands** ($[\mathrm{RuCl_6}]^{2-}$ is $t_{2g}^4$; S&A p.477).
> - The criterion uses the **free-ion $P$** only as a guide; Huheey warns the complexed $P$ is 15–30 % smaller, which can flip a borderline case.

---

## 5. Magnetism and the spin-only formula

$$\mu_{\rm so}=2\sqrt{S(S+1)}\,\mu_B=\sqrt{N(N+2)}\,\mu_B,\qquad \mu_B=e\hbar/2m_e=9.274\times10^{-24}\ \mathrm{J\,T^{-1}}.$$

| $N$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $\mu_{so}/\mu_B$ | 0 | 1.73 | 2.83 | 3.87 | 4.90 | 5.92 |

(S&A Table 20.3: $\mathrm{Ti^{3+}}$ 1.73, $\mathrm{V^{3+}}$ 2.83, $\mathrm{Cr^{3+}}$ 3.87, $\mathrm{Mn^{3+}}$ HS 4.90, $\mathrm{Fe^{3+}}$ HS 5.92: reproduced.) A measured moment identifies $N$, hence the spin state: a high-spin $d^6$ gives 4.90, a low-spin $d^6$ is diamagnetic.

> [!example] S&A Examples 20.2 and self-test (worked)
> - Octahedral Co(II), $\mu=4.0\,\mu_B$: $d^7$ options are HS ($N=3$, 3.87) or LS ($N=1$, 1.73): **high spin** $t_{2g}^5e_g^2$.
> - $[\mathrm{Mn(NCS)_6}]^{4-}$, $\mu=6.06\,\mu_B$: Mn(II) is $d^5$, closest to HS $N=5$ (5.92): **$t_{2g}^3e_g^2$**; the 0.14 excess is a small orbital contribution.

> [!pitfall] Orbital contribution
> Orbital angular momentum is **quenched** in most complexes, but survives when the applied field can rotate an electron into a **degenerate orbital of the right symmetry** (S&A Fig. 20.6): **low-spin $d^5$** ($\mathrm{K_3[Fe(CN)_6]}$: $\mu=2.3\,\mu_B$, between $N=1$ and $N=2$) and **high-spin $d^6$, $d^7$** deviate strongly; spin-only values are then lower bounds on reality. A change of spin state with temperature is **spin crossover** (S&A §20.9, not required).

![[sa_fig20_6_orbital_angular_momentum.png]]
*Figure CH10.8 (book crop). S&A Fig. 20.6: circulation of an electron between $d_{x^2-y^2}$ and $d_{xy}$ about the field direction: the origin of the orbital contribution.*

---

## 6. Tetrahedral complexes

Four ligands on alternate corners of a cube. There is no inversion centre, so the labels lose $g$: $t_2$ ($d_{xy},d_{yz},d_{zx}$) and $e$ ($d_{z^2},d_{x^2-y^2}$).

![[fig_ch10_geometry.png]]
*Figure CH10.9. Why the order inverts. In a cube the $t_2$ lobes point at the edge midpoints, **closer** to the corner ligands ($35.3^\circ$) than the $e$ lobes (face centres, $54.7^\circ$). In an octahedron it is the other way round ($e_g$ at $0^\circ$, $t_{2g}$ at $45^\circ$). Angles computed in `§L`.*

| Result | Value | Reason |
|---|---|---|
| order | $e$ **below** $t_2$ | $t_2$ lobes closer to the ligands |
| size | $\Delta_T\approx\tfrac49\Delta_O$ (S&A: $\tfrac49$; Huheey: $\tfrac49$) | 4 vs 6 ligands, and none points directly at an orbital (derivation in §2.1) |
| energies | $e=-\tfrac35\Delta_T=-2.67\,Dq$; $t_2=+\tfrac25\Delta_T=+1.78\,Dq$ | barycentre rule |
| spin | essentially **always high spin** | $P>\Delta_T$ almost always (first low-spin 3d tetrahedral complex: tetrakis(1-norbornyl)cobalt(IV), Huheey fn. 20) |

![[sa_fig20_13_lfse_oct_tet.png]]
*Figure CH10.10 (book crop). S&A Fig. 20.13: LFSE/$\Delta_O$ against $n$ for high-spin octahedral (circles) and tetrahedral (squares) complexes, $\Delta_T=\frac49\Delta_O$. My recomputed version is in Figure CH10.13.*

| $d^n$ | $e^{a}t_2^{b}$ | $N$ | LFSE/$\Delta_T$ | LFSE/$\Delta_O$ |
|---|---|---|---|---|
| $d^1$ | $e^1$ | 1 | −0.6 | −0.27 |
| $d^2$ | $e^2$ | 2 | −1.2 | −0.53 |
| $d^3$ | $e^2t_2^1$ | 3 | −0.8 | −0.36 |
| $d^4$ | $e^2t_2^2$ | 4 | −0.4 | −0.18 |
| $d^5$ | $e^2t_2^3$ | 5 | 0 | 0 |
| $d^6$ | $e^3t_2^3$ | 4 | −0.6 | −0.27 |
| $d^7$ | $e^4t_2^3$ | 3 | −1.2 | −0.53 |
| $d^8$ | $e^4t_2^4$ | 2 | −0.8 | −0.36 |
| $d^9$ | $e^4t_2^5$ | 1 | −0.4 | −0.18 |
| $d^{10}$ | $e^4t_2^6$ | 0 | 0 | 0 |

(S&A Table 20.4; observed $\Delta_T$: $\mathrm{VCl_4}$ 9010, $[\mathrm{CoCl_4}]^{2-}$ 3300, $[\mathrm{CoBr_4}]^{2-}$ 2900, $[\mathrm{CoI_4}]^{2-}$ 2700, $[\mathrm{Co(NCS)_4}]^{2-}$ 4700 cm$^{-1}$.) Self-consistency check (🔵): $[\mathrm{CoCl_6}]^{4-}$ would have $\Delta_O=f\,g=0.78\times9.3=7250$, so $\Delta_T=\frac49\times7250=3220\approx3300$ observed.

---

## 7. Square-planar and tetragonally distorted complexes

Remove the two ligands on $z$ from an octahedron (Figure CH10.3B; Huheey Fig. 11.12). Orbitals with a $z$ component ($d_{z^2},d_{xz},d_{yz}$) lose repulsion and fall; $d_{x^2-y^2}$ (pointing at the four remaining ligands) rises most. The labels in $D_{4h}$: $d_{x^2-y^2}=b_{1g}$, $d_{xy}=b_{2g}$, $d_{z^2}=a_{1g}$, $(d_{xz},d_{yz})=e_g$.

![[huheey_fig11_12_tetragonal_to_square_planar.png]]
*Figure CH10.11 (book crop). Huheey Fig. 11.12: (a) octahedron, (b) tetragonally elongated, (c) square-planar limit; $\Delta$ is the gap $b_{2g}$–$b_{1g}$. The $a_{1g}$ ($d_{z^2}$) level may fall below $e_g$ in the square-planar limit.*

> [!key] Square-planar energies (Huheey Table 11.5; computed, 🔵)
> In $Dq$ units (same M–L distance): $d_{x^2-y^2}$ **+12.28**, $d_{xy}$ **+2.28**, $d_{z^2}$ **−4.28**, $d_{xz},d_{yz}$ **−5.14** (sum 0). A non-cubic field needs the $l=2$ term as well (the book's extra parameters $Ds,Dt$); with the **single** ratio fixed by $d_{z^2}=-4.28$, my point-charge calculation reproduces **the other three numbers and the linear-complex row (+10.28, −6.28, −6.28, +1.14, +1.14)**. The total spread $d_{x^2-y^2}\to d_{xz,yz}$ is $1.0\Delta_O$ with the $l=4$ term alone, $1.74\Delta_O$ with Huheey's weights, and S&A quote $\Delta_{SP}\approx1.3\Delta_O$ as a rule of thumb `[verify]`: it is **model dependent**.

> [!key] Who is square planar? ($d^8$ with strong field)
> Eight electrons fill $d_{xz},d_{yz},d_{z^2},d_{xy}$ and leave $d_{x^2-y^2}$ **empty**: low-spin, diamagnetic. The stronger the field the higher the empty orbital rises, so the stabilisation grows. S&A p.481:
> - **$4d^8$ and $5d^8$** (large $\Delta$, small $P$, steric freedom): $\mathrm{Rh(I)}$, $\mathrm{Ir(I)}$, $\mathrm{Pd(II)}$, $\mathrm{Pt(II)}$, $\mathrm{Au(III)}$: $[\mathrm{PdCl_4}]^{2-}$, $[\mathrm{PtCl_4}]^{2-}$, $[\mathrm{Pt(NH_3)_4}]^{2+}$, $[\mathrm{AuCl_4}]^-$.
> - **$3d^8$**: tetrahedral $[\mathrm{NiX_4}]^{2-}$ ($\mathrm X$ = halide: small $\Delta$, steric repulsion wins) but square planar $[\mathrm{Ni(CN)_4}]^{2-}$ (strong field).

> [!pitfall] Square planar is not "tetrahedral + 90°"
> Tetrahedral $d^8$ is paramagnetic ($e^4t_2^4$, $N=2$); square planar $d^8$ is diamagnetic. A magnetic measurement therefore distinguishes $[\mathrm{NiCl_4}]^{2-}$ (above the spin-only 2.83 $\mu_B$ because of orbital contribution) from $[\mathrm{Ni(CN)_4}]^{2-}$ (0).

Other geometries (Huheey Table 11.5, orbital energies in $Dq$, $d_{z^2},d_{x^2-y^2},d_{xy},d_{xz,yz}$): linear $+10.28,-6.28,-6.28,+1.14$; tetrahedral $-2.67,-2.67,+1.78,+1.78$; octahedral $+6,+6,-4,-4$; cubic $-5.34,-5.34,+3.56$ (the book's trigonal-bipyramidal, square-pyramidal and others follow the same recipe; I reproduced only the first four numerically).

---

## 8. The Jahn–Teller effect

> [!key] Statement (S&A p.482)
> If the ground electronic configuration of a **non-linear** complex is **orbitally degenerate and asymmetrically filled**, the complex distorts to remove the degeneracy and lower its energy. It tells you that the symmetric geometry is **unstable**, not **which** distortion occurs.

For an octahedron elongated along $z$ (and compressed on $x,y$): $d_{z^2}$ falls by $\delta_1/2$, $d_{x^2-y^2}$ rises by $\delta_1/2$; $t_{2g}$ splits into $(d_{xz},d_{yz})$ down by $\delta_2/3$ and $d_{xy}$ up by $2\delta_2/3$ (barycentres kept).

![[sa_fig20_12_jahn_teller_levels.png]]
![[fig_ch10_jt.png]]
*Figure CH10.12. Left: S&A Fig. 20.12 (book crop). Right: **A** the energy curve $E(Q)=\frac12kQ^2\pm\alpha Q$ for a doubly degenerate state: the occupied branch has two minima at $\pm Q_0=\pm\alpha/k$ with $E_{JT}=-\alpha^2/2k$, so the symmetric point is a maximum on that branch; **B** the $d^9$ level scheme (net gain $\delta_1/2$); **C** which octahedral configurations are active.*

> [!example] $d^9$, $\mathrm{Cu^{2+}}$
> $t_{2g}^6e_g^3\to$ two electrons in the lowered $d_{z^2}$, one in the raised $d_{x^2-y^2}$: net **$-\delta_1/2$** (the filled $t_{2g}^6$ gives no net change). Hence $[\mathrm{Cu(OH_2)_6}]^{2+}$ has four short and two long bonds. Axial **elongation** is more common than compression (it weakens two bonds, not four). Static below 20 K, **dynamic** above (EPR; S&A p.482).

> [!key] Strong versus weak (S&A p.482)
> - **Strong** (unequal $e_g$ occupation): high-spin $d^4$ ($\mathrm{Mn^{3+}}$, $\mathrm{Cr^{2+}}$), low-spin $d^7$ ($\mathrm{Ni^{3+}}$), **$d^9$**. The $e_g$ orbitals point at the ligands, so splitting is large.
> - **Weak** (unequal $t_{2g}$ occupation): $d^1,d^2$, low-spin $d^4,d^5$, high-spin $d^6,d^7$. The $t_{2g}$ lobes do not point at the ligands: the distortion is too small to measure.
> - Tetrahedral: $d^1,d^3,d^4,d^6,d^8,d^9$ (weak, no $d$ orbital points at the ligands).

> [!pitfall] JT and the Irving–Williams anomaly
> $\mathrm{Cu^{2+}}$ complexes are **more** stable than $\mathrm{Ni^{2+}}$ although $\mathrm{Cu^{2+}}$ has an extra antibonding $e_g$ electron: the Jahn–Teller elongation lets the four equatorial bonds be short and strong (§9.4).

---

## 9. What CFT explains: thermodynamics and structure

### 9.1 Hydration and lattice enthalpies: the double hump

Across the first transition series the hydration enthalpy of $\mathrm{M^{2+}}$ increases (smaller ions) but not smoothly: it has **two maxima** (near V and Ni–Cu) and a minimum at $\mathrm{Mn^{2+}}$ ($d^5$, LFSE 0). Subtracting the **high-spin LFSE** restores a smooth curve.

![[fig_ch10_thermo.png]]
*Figure CH10.13. A: hydration enthalpies (read off S&A Fig. 20.7) and the same after subtracting the LFSE computed from the hexaaqua $\Delta_O$ (Table 20.1 for $\mathrm{Mn,Fe,Ni}$; Huheey Table 11.6 for $\mathrm{Co}$; $\mathrm{V,Cr,Cu}$ recalled `[verify]`). B: S&A Example 20.3. C: ionic radii (Shannon radii, recalled `[verify]`), Huheey Fig. 11.15.*

![[sa_fig20_7_hydration_enthalpy.png]]
*Figure CH10.14 (book crop). S&A Fig. 20.7: open circles observed, filled circles after subtracting the LFSE. My recomputed filled circles (2636, 2699, 2743, 2793, 2816, 2864, 2899 kJ/mol for V…Cu) agree with the plotted ones.*

> [!example] Numbers behind it (computed, `§G`)
> LFSE in kJ mol$^{-1}$ = LFSE$/\Delta_O\times\Delta_O\times0.011963$: $\mathrm{V^{2+}}$ ($d^3$, 12 400 cm$^{-1}$) 178; $\mathrm{Cr^{2+}}$ 100; $\mathrm{Mn^{2+}}$ **0**; $\mathrm{Fe^{2+}}$ 50; $\mathrm{Co^{2+}}$ 88; $\mathrm{Ni^{2+}}$ (8 500) **122**; $\mathrm{Cu^{2+}}$ 90. The corrected curve is monotonic (residual from a smooth quadratic: rms **5.6 kJ/mol**, against **50** for the raw data). So the LFSE is **about 3–6 %** of the hydration enthalpy; S&A (p.474) puts the whole differential-repulsion effect at "little more than about 10 per cent" of the metal–ligand interaction energy.

> [!example] S&A Example 20.3: oxides MO (rock salt), computed
> Lattice enthalpies: CaO 3460, TiO 3878, VO 3913, MnO 3810 kJ mol$^{-1}$. A linear step $(3810-3460)/5=70$ per electron predicts TiO 3600 and VO 3670; the excess is **278** (TiO, LFSE $0.8\Delta_O$) and **243** (VO, $1.2\Delta_O$). Caution (🔵): the implied $\Delta_O$ are 29 000 and 17 000 cm$^{-1}$: not equal, so the baseline is only a rough guide; the *sign and size order* of the effect is the point. **Self-test 20.3** (fluorides MnF$_2$ 2780 … ZnF$_2$ 2985): the excesses over a Mn–Zn line are +105 (Fe), +114 (Co), +157 (Ni): all positive and largest for $\mathrm{Ni^{2+}}$ ($d^8$, 1.2$\Delta_O$), as predicted; they are not in the ratio 1 : 2 : 3, again because the baseline is approximate.

![[huheey_fig11_14_lattice_energies.png]]
*Figure CH10.15 (book crop). Huheey Fig. 11.14: lattice energies of the divalent first-row halides: the same double hump, with $\mathrm{Ca^{2+}}$, $\mathrm{Mn^{2+}}$, $\mathrm{Zn^{2+}}$ ($d^0$, $d^5$, $d^{10}$: LFSE 0) on a smooth curve and the maximum deviations at $\mathrm{V^{2+}}$ and $\mathrm{Ni^{2+}}$ (LFSE $1.2\Delta_O$).*

### 9.2 Ionic radii

![[huheey_fig11_15_ionic_radii.png]]
*Figure CH10.16 (book crop). Huheey Fig. 11.15: radii of $\mathrm{M^{2+}}$ (above) and $\mathrm{M^{3+}}$ (below) against the number of $d$ electrons; filled circles are low spin.*

Electrons entering $t_{2g}$ (between the ligands) barely shield: the radius **falls** ($d^0\to d^3$). The next electron in a high-spin ion goes into **$e_g$**, directed at the ligands, repels them and the radius **rises** ($d^4,d^5$); then falls again as $t_{2g}$ refills ($d^6\to d^8$), and rises ($d^9,d^{10}$). **Low-spin** ions keep $e_g$ empty until $t_{2g}^6$, so they decrease monotonically to $d^6$ (Huheey p.409).

### 9.3 Stability of oxidation states: Co(III)

$\mathrm{Co^{3+}(aq)}$ oxidises water ($E^\circ=+1.83$ V, $-1.83$ in Huheey's oxidation convention), but with strong-field ligands Co(III) is **hard to avoid**. Huheey eqs. 11.6–11.12, written as $E^\circ(\mathrm{Co^{III}/Co^{II}})$ (sign reversed): aqua +1.83, ox +0.57, phen +0.42, edta +0.37, en +0.18, $\mathrm{NH_3}$ +0.11 V, $\mathrm{CN^-}$ −0.83 V. The order follows the **spectrochemical series**. The step $\mathrm{Co^{II}}$ (HS $t_{2g}^5e_g^2$, LFSE $0.8\Delta_O$) → $\mathrm{Co^{III}}$ (LS $t_{2g}^6$, $2.4\Delta_O$) gains about $1.6\Delta_O$ (before pairing), growing with $\Delta_O$. Computed (🔵): en versus aqua shifts the couple by 1.65 V, i.e. $K_{ox}/K_{red}$ changes by $10^{27.9}$. Huheey stresses that CFSE is *one* factor; **chelate entropy** reorders en and the others relative to the series ([[CH09 Redox]] §10, [[Standard Reduction Potential]]).

### 9.4 The Irving–Williams series

For $\mathrm{M^{2+}}$ the stability constants of complexes with a given ligand follow
$$\mathrm{Ba^{2+}<Sr^{2+}<Ca^{2+}<Mg^{2+}<Mn^{2+}<Fe^{2+}<Co^{2+}<Ni^{2+}<Cu^{2+}>Zn^{2+}}$$
(S&A p.483), "relatively insensitive to the ligand". Up to $\mathrm{Mn^{2+}}$ it tracks the **ionic radius** (electrostatics); beyond it the extra rise for $d^6$–$d^9$ is the **LFSE**; the fall to $\mathrm{Zn^{2+}}$ ($d^{10}$, LFSE 0) completes the argument. $\mathrm{Cu^{2+}}>\mathrm{Ni^{2+}}$ is the exception explained by the **Jahn–Teller** stabilisation.

![[sa_fig20_14_irving_williams.png]]
*Figure CH10.17 (book crop). S&A Fig. 20.14: $\log K_f$ for oxalate (red) and glycinate (blue) complexes along the series.*

### 9.5 Octahedral versus tetrahedral: OSPE and spinels

The **octahedral site preference energy** is the LFSE of the octahedral (high-spin) arrangement minus that of the tetrahedral one (same ligand, $\Delta_T=\frac49\Delta_O$). It is zero for $d^0$, high-spin $d^5$ and $d^{10}$ and largest ($0.844\,\Delta_O$) for **$d^3$ and $d^8$** (Cr$^{3+}$, Ni$^{2+}$): they "strongly prefer an octahedral geometry" (S&A p.482). $d^4,d^9$ prefer it moderately (and the Jahn–Teller effect adds to it); $d^1,d^2,d^6,d^7$ are only mildly disfavoured in tetrahedral coordination: $\mathrm{V(II)}$ and $\mathrm{Co(II)}$ form tetrahedral halides $\mathrm{MX_4^{2-}}$. For strong-field ligands the **low-spin** octahedral LFSE is larger still, so the preference grows.

![[fig_ch10_lfse.png]]
*Figure CH10.18. A: LFSE for octahedral high spin, octahedral low spin (before the pairing cost) and tetrahedral. B: the OSPE in units of $\Delta_O$. C: OSPE in kJ mol$^{-1}$ with the aqua $\Delta_O$ (computed, matches Huheey Table 11.9 and the numbers quoted in the text: Ni$^{2+}$ 86, Mn$^{3+}$ 106, Co$^{2+}$ 29.3, Cr$^{3+}$ 176, Fe$^{2+}$ ≈ 15–17).*

> [!key] Spinels $\mathrm{AB_2O_4}$ (S&A p.483; Huheey pp.411–413)
> The oxide ions form a cubic close-packed lattice; per formula unit there are 8 tetrahedral and 4 octahedral holes, of which A and B fill one-eighth and one-half. **Normal:** $\mathrm A^{2+}$ tetrahedral, $\mathrm B^{3+}$ octahedral, $\mathrm{(A)_t[B_2]_oO_4}$. **Inverse:** $\mathrm A^{2+}$ and half the $\mathrm B^{3+}$ swap, $\mathrm{(B)_t[AB]_oO_4}$. Huheey's parameter $\lambda$ = fraction of B in tetrahedral holes (0 normal, 0.5 inverse). The site chosen is the one that gives **the larger total LFSE**, so compare the OSPE of the two cations (oxide is a weak field, $\Delta_O$ as for water):
> | spinel | $\mathrm A^{2+}$ OSPE | $\mathrm B^{3+}$ OSPE | result |
> |---|---|---|---|
> | $\mathrm{MgAl_2O_4}$ | 0 | 0 | normal |
> | $\mathrm{Mn_3O_4}$ | $\mathrm{Mn^{2+}}$ 0 | $\mathrm{Mn^{3+}}$ **106** kJ | normal |
> | $\mathrm{Fe_3O_4}$ | $\mathrm{Fe^{2+}}$ ≈15 | $\mathrm{Fe^{3+}}$ 0 | **inverse** $\mathrm{(Fe^{3+})_t[Fe^{2+}Fe^{3+}]_oO_4}$ |
> | $\mathrm{NiFe_2O_4}$ | $\mathrm{Ni^{2+}}$ **86** | $\mathrm{Fe^{3+}}$ 0 | **inverse** |
> | $\mathrm{Co_3O_4}$ | $\mathrm{Co^{2+}}$ 29 | $\mathrm{Co^{3+}}$ **large** (low-spin $d^6$) | normal $\mathrm{(Co^{2+})_t[Co^{3+}_2]_oO_4}$ |
> The CFSE is only 5–10 % of the lattice energy (Huheey p.412) but decides the structure when the other terms are similar; for ions with very different radii or covalency, CFT alone fails (Huheey p.413).

---

## 10. The limits of the model

CFT explains **patterns** and *trends in magnitude of the energies*, but:
- it cannot explain the **spectrochemical series** (§3.3) or why $\mathrm{CN^-}$ and $\mathrm{CO}$ dominate ($\pi$ back-donation, [[CO Back-Donation]]);
- it predicts **no covalency**, yet the **nephelauxetic effect** shows electron–electron repulsion is **lower** in complexes than in the free ion, because the $d$ electrons are delocalised over ligand orbitals ("cloud expanding", Huheey p.413). Ligand series by decreasing repulsion (increasing nephelauxetic effect), $\mathrm{F^-}$ < $\mathrm{H_2O}$ < urea < $\mathrm{NH_3}$ < en ≈ ox < $\mathrm{Cl^-}$ < $\mathrm{CN^-}$ < $\mathrm{Br^-}$ < $\mathrm{N_3^-}$ < $\mathrm{I^-}$ (Table 11.10; `[verify]` the OCR). It is the *indirect evidence for covalency*;
- hence **ligand-field theory** (S&A §20.2): the MO theory of the $d$-metal complex, built from SALCs ([[Ligand Group Orbitals]]), in which $\Delta_O$ is the $t_{2g}$–$e_g^*$ gap and $\pi$-donor ligands lower, $\pi$-acceptors raise it. **Excluded from Quiz 3.**

> [!connection] How CH10 connects
> **Builds on:** [[CH02 Molecular Orbital Theory Diatomics]] (orbital pictures), [[CH09 Redox]] (the Co(III)/Co(II) couple), [[CH06 Hard and Soft Acids and Bases]] ($\mathrm{SCN^-}$, ambidentate donors), [[Symmetry Labels a b e t]].
> **Concepts:** [[Crystal Field Theory]] · [[Crystal Field Splitting Parameter]] · [[Spectrochemical Series]] · [[Ligand Field Stabilization Energy]] · [[High-Spin and Low-Spin Complexes]] · [[Pairing Energy]] · [[Spin-Only Magnetic Moment]] · [[Tetrahedral Crystal Field]] · [[Square-Planar Complexes]] · [[Jahn-Teller Effect]] · [[Octahedral Site Preference Energy]] · [[Spinel Structure]] · [[Irving-Williams Series]] · [[Nephelauxetic Effect]] · [[d Orbitals in Complexes]]
> **Other subjects:** [[Group Theory - Course Map]] (the $2+3$ split is the reduction of the $l=2$ representation in $O_h$), [[Quantum Mechanics - Course Map]] (first-order perturbation theory of a degenerate level; the Jahn–Teller curve is a degenerate-perturbation problem), [[Thermodynamics and Statistical Mechanics - Course Map]] (the high-spin/low-spin balance is a thermal population: spin crossover as a two-level system, [[SM03 The Canonical Ensemble]]), [[Climate - Course Map]] (the colours of minerals, e.g. blue $\mathrm{Cu^{2+}}$ and green $\mathrm{Fe^{2+}}$ weathering products).

---

## Summary
> [!summary] Cheat-sheet
> - **Octahedral:** $t_{2g}$ ($-0.4\Delta_O=-4Dq$) below $e_g$ ($+0.6\Delta_O=+6Dq$); barycentre fixed; $\Delta_O=10Dq$.
> - **Tetrahedral:** $e$ ($-0.6\Delta_T$) below $t_2$ ($+0.4\Delta_T$); $\Delta_T=\frac49\Delta_O$; always high spin.
> - **Square planar:** $d_{x^2-y^2}\gg d_{xy}>d_{z^2}>d_{xz,yz}$; low-spin $d^8$ ($4d$, $5d$, or $\mathrm{CN^-}$).
> - **Series:** $\mathrm{I^-<Br^-<Cl^-<F^-<OH^-<H_2O<NH_3<en<bpy<NO_2^-<CN^-<CO}$; $\Delta_O$ up with oxidation state and down the group.
> - **LFSE:** $(-0.4n_t+0.6n_e)\Delta_O+(\text{extra pairs})P$; **low spin iff $\Delta_O>P$** (all of $d^4$–$d^7$).
> - **Moment:** $\sqrt{N(N+2)}\,\mu_B$: 1.73, 2.83, 3.87, 4.90, 5.92.
> - **Jahn–Teller:** strong for HS $d^4$, LS $d^7$, $d^9$ ($e_g$); weak for $t_{2g}$ degeneracies.
> - **Thermo:** double humps (hydration, lattice), radii double dip, Irving–Williams (Cu anomaly = JT), Co(III) stable with strong field, OSPE $d^3,d^8$ highest, spinels normal/inverse by OSPE.
> - **Limits:** series, back-bonding and nephelauxetic effect need covalency: ligand-field theory.

## Practice
1. **LFSE.** Give the electron configuration, $N$ and LFSE (in $\Delta_O$, $P$) of $\mathrm{[Cr(OH_2)_6]^{2+}}$ (weak) and $[\mathrm{Cr(CN)_6}]^{4-}$ (strong), and which of the two is Jahn–Teller active.
2. **Spin state.** $[\mathrm{Fe(OH_2)_6}]^{2+}$: $\Delta_O=10\,400$ cm$^{-1}$, $P=14\,600$. High or low spin? Give $\mu_{so}$ and LFSE in cm$^{-1}$ and kJ mol$^{-1}$.
3. **Low-spin energy.** LFSE of $[\mathrm{Fe(CN)_6}]^{4-}$ ($\Delta_O=32\,200$, $P=14\,600$) in kJ mol$^{-1}$.
4. **Colour.** $[\mathrm{Ti(OH_2)_6}]^{3+}$ absorbs at 20 300 cm$^{-1}$. Give $\lambda$ (nm), the energy in kJ mol$^{-1}$ and eV, and the likely colour. Repeat for $32\,500$ cm$^{-1}$.
5. **Jørgensen.** Estimate $\Delta_O$ for $[\mathrm{Cr(en)_3}]^{3+}$ and $[\mathrm{Co(NH_3)_6}]^{3+}$ with $f(\mathrm{en})=1.28$, $f(\mathrm{NH_3})=1.25$, $g(\mathrm{Cr^{III}})=17.4$, $g(\mathrm{Co^{III}})=18.2$ kK.
6. **Tetrahedral.** $[\mathrm{CoCl_4}]^{2-}$ has $\Delta_T=3300$ cm$^{-1}$. Give its configuration, $N$, $\mu_{so}$, LFSE in kJ mol$^{-1}$ and the predicted $\Delta_O$ of $[\mathrm{CoCl_6}]^{4-}$.
7. **Geometry.** Predict (and justify) the geometry and magnetism of $[\mathrm{NiCl_4}]^{2-}$, $[\mathrm{Ni(CN)_4}]^{2-}$, $[\mathrm{PtCl_4}]^{2-}$, $[\mathrm{Ni(OH_2)_6}]^{2+}$.
8. **Magnetic moment.** Octahedral complexes of $\mathrm{Co^{3+}}$: $\mu=0$ for $[\mathrm{Co(NH_3)_6}]^{3+}$, 4.9 $\mu_B$ for $[\mathrm{CoF_6}]^{3-}$. Assign configurations and explain with $\Delta_O$ versus $P$.
9. **Derivation.** Show that for $d^4$, $d^5$, $d^6$ and $d^7$ the low-spin/high-spin crossover occurs at $\Delta_O=P$.
10. **Barycentre.** Derive $\frac35\Delta_O$ and $\frac25\Delta_O$, and then $-\frac35\Delta_T$ and $+\frac25\Delta_T$ for the tetrahedron.
11. **Jahn–Teller.** Which of $[\mathrm{Mn(OH_2)_6}]^{3+}$, $[\mathrm{Fe(OH_2)_6}]^{3+}$, $[\mathrm{Cu(OH_2)_6}]^{2+}$, $[\mathrm{Ni(OH_2)_6}]^{2+}$, $[\mathrm{Fe(CN)_6}]^{3-}$, $[\mathrm{Co(OH_2)_6}]^{2+}$ are Jahn–Teller active, and strongly or weakly?
12. **Hydration enthalpy.** The observed $-\Delta_{hyd}H$ of $\mathrm{Fe^{2+}}$ is 2843 kJ mol$^{-1}$; with $\Delta_O=10\,400$ cm$^{-1}$ remove the LFSE. Repeat for $\mathrm{Ni^{2+}}$ (2986; $\Delta_O=8500$).
13. **Spinels.** Predict normal or inverse: $\mathrm{NiAl_2O_4}$, $\mathrm{CoFe_2O_4}$, $\mathrm{Mn_3O_4}$, $\mathrm{ZnFe_2O_4}$; give the reason using OSPE.
14. **Co(III).** Why is $[\mathrm{Co(OH_2)_6}]^{3+}$ a strong oxidant but $[\mathrm{Co(en)_3}]^{3+}$ is stable? Estimate the factor in $K_{ox}/K_{red}$ from $E^\circ=+1.83$ and $+0.18$ V.
15. **Irving–Williams.** Why does $K_f$ for $\mathrm{Cu^{2+}}$ exceed that of $\mathrm{Ni^{2+}}$ with the same ligand, and why does it fall at $\mathrm{Zn^{2+}}$?

> [!example]- Solutions
> 1. $\mathrm{Cr^{2+}}$ is $d^4$. Weak: $t_{2g}^3e_g^1$, $N=4$, LFSE $=-0.6\Delta_O$, **Jahn–Teller active (strong)** ($e_g^1$). Strong: $t_{2g}^4$, $N=2$, LFSE $=-1.6\Delta_O+P$, only weakly active ($t_{2g}$ degeneracy).
> 2. $\Delta_O/P=0.71<1$: **high spin**, $t_{2g}^4e_g^2$, $N=4$, $\mu_{so}=\sqrt{4\cdot6}=4.90\,\mu_B$; LFSE $=0.4\times10\,400=4160$ cm$^{-1}=49.8$ kJ mol$^{-1}$.
> 3. $d^6$ low spin: $2.4\Delta_O-2P=2.4\times32\,200-2\times14\,600=77\,280-29\,200=48\,100$ cm$^{-1}=\mathbf{575}$ kJ mol$^{-1}$ (with the free-ion $P$; less if $P$ is reduced in the complex).
> 4. $\lambda=10^7/20\,300=493$ nm; $E=20\,300\times0.011963=243$ kJ mol$^{-1}=2.52$ eV; absorbed blue–green, transmitted **purple/violet**. For $32\,500$: $\lambda=308$ nm (UV, **colourless** in the visible), $E=389$ kJ mol$^{-1}$ (4.03 eV).
> 5. $[\mathrm{Cr(en)_3}]^{3+}$: $1.28\times17.4=22.3$ kK (obs. 22 300); $[\mathrm{Co(NH_3)_6}]^{3+}$: $1.25\times18.2=22.75$ kK (obs. 22 870).
> 6. $\mathrm{Co^{2+}}$ $d^7$, tetrahedral $e^4t_2^3$, $N=3$, $\mu_{so}=3.87\,\mu_B$ (experimental values 4.4–4.8 because of orbital contribution); LFSE $=1.2\Delta_T=3960$ cm$^{-1}=47.4$ kJ mol$^{-1}$; $\Delta_O=\frac94\times3300\approx7400$ cm$^{-1}$ (compare $f\,g=0.78\times9.3=7250$ cm$^{-1}$).
> 7. $[\mathrm{NiCl_4}]^{2-}$: $3d^8$, weak field, small $\Delta$, steric: **tetrahedral**, paramagnetic ($e^4t_2^4$, $N=2$). $[\mathrm{Ni(CN)_4}]^{2-}$: strong field: **square planar**, diamagnetic. $[\mathrm{PtCl_4}]^{2-}$: $5d^8$, large $\Delta$, small $P$: square planar, diamagnetic. $[\mathrm{Ni(OH_2)_6}]^{2+}$: octahedral, $t_{2g}^6e_g^2$, $N=2$, 2.83 $\mu_B$ (OSPE 86 kJ mol$^{-1}$ favours the octahedron).
> 8. $\mathrm{Co^{3+}}$ is $d^6$. $[\mathrm{Co(NH_3)_6}]^{3+}$ ($\Delta_O=22\,900>P\approx19\,150$): low spin $t_{2g}^6$, $N=0$. $[\mathrm{CoF_6}]^{3-}$ ($\Delta_O=13\,100<P$): high spin $t_{2g}^4e_g^2$, $N=4$, $\mu=4.90\,\mu_B$.
> 9. From the table: $E_{LS}-E_{HS}=-(\Delta\mathrm{LFSE})\Delta_O+(\Delta\text{pairs})P$: $d^4$: $-1.0\Delta_O+P$; $d^5$: $-2.0\Delta_O+2P$; $d^6$: $-2.0\Delta_O+2P$; $d^7$: $-1.0\Delta_O+P$. All vanish at $\Delta_O=P$.
> 10. With $e_g=x$, $t_{2g}=-y$: $2x-3y=0$, $x+y=\Delta_O\Rightarrow x=\frac35\Delta_O$, $y=\frac25\Delta_O$. Tetrahedral: $e$ (2 orbitals) at $-x'$, $t_2$ (3 orbitals) at $+y'$: $-2x'+3y'=0$, $x'+y'=\Delta_T\Rightarrow x'=\frac35\Delta_T$, $y'=\frac25\Delta_T$.
> 11. $\mathrm{Mn^{3+}}$ HS $d^4$ ($t_{2g}^3e_g^1$): **strong**. $\mathrm{Fe^{3+}}$ HS $d^5$: none. $\mathrm{Cu^{2+}}$ $d^9$: **strong**. $\mathrm{Ni^{2+}}$ $d^8$: none. $[\mathrm{Fe(CN)_6}]^{3-}$ LS $d^5$ ($t_{2g}^5$): weak. $\mathrm{Co^{2+}}$ HS $d^7$ ($t_{2g}^5e_g^2$): weak.
> 12. $\mathrm{Fe^{2+}}$: LFSE $=0.4\times10\,400\times0.011963=49.8$; corrected $2843-50=2793$ kJ mol$^{-1}$. $\mathrm{Ni^{2+}}$: $1.2\times8500\times0.011963=122$; corrected $2986-122=2864$.
> 13. $\mathrm{NiAl_2O_4}$: $\mathrm{Ni^{2+}}$ OSPE 86 vs $\mathrm{Al^{3+}}$ 0: **inverse** (largely). $\mathrm{CoFe_2O_4}$: $\mathrm{Co^{2+}}$ 29 vs $\mathrm{Fe^{3+}}$ 0: **inverse**. $\mathrm{Mn_3O_4}$: $\mathrm{Mn^{3+}}$ 106 vs $\mathrm{Mn^{2+}}$ 0: **normal**. $\mathrm{ZnFe_2O_4}$: both 0 ($d^{10}$, HS $d^5$): CFT predicts no preference; observed **normal** (other factors: covalent preference of $\mathrm{Zn^{2+}}$ for tetrahedral sites).
> 14. Aqua: LFSE gain on $\mathrm{Co^{II}}$(HS)$\to\mathrm{Co^{III}}$(LS) is small ($\Delta_O$ 20 700 cm$^{-1}$ with $E^\circ=+1.83$ V: oxidises water). With en $\Delta_O$ rises, so Co(III) gains $\approx1.6\Delta_O$ more: the couple falls to +0.18 V. Factor $10^{1.65/0.05916}=10^{27.9}$ in $K_{ox}/K_{red}$.
> 15. Up to $\mathrm{Mn^{2+}}$ the trend follows radius; beyond it the LFSE of $d^6$–$d^8$ adds to the binding. $\mathrm{Cu^{2+}}$ has $e_g^3$ (an antibonding electron) but the **Jahn–Teller elongation** strengthens four equatorial bonds, hence $\mathrm{Cu^{2+}}>\mathrm{Ni^{2+}}$. $\mathrm{Zn^{2+}}$ ($d^{10}$) has zero LFSE and a slightly larger radius.

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | octahedral splitting, $\Delta_O$, barycentre, $d^1$ spectrum | S&A §20.1a pp.473–475, Figs 20.1–20.3 ([[Shriver and Atkins Inorganic Chemistry 5th Ed.pdf#page=500\|PDF p.500–502]]); Huheey pp.394–399, Figs 11.3–11.8 ([[7_Inorganic_Chemistry_by_Huheey_E_Keiter_and_R_Keiter.pdf#page=411\|PDF p.411–416]]) | taught (reading range) |
> | spectrochemical series, factors affecting $\Delta$, $f\,g$ | S&A p.475, Table 20.1; Huheey pp.404–408, Tables 11.6–11.7 | taught |
> | LFSE, pairing, high/low spin | S&A §20.1b pp.475–478, Table 20.2, Example 20.1; Huheey pp.399–402, Tables 11.3–11.4 | taught |
> | magnetic moments | S&A §20.1c pp.478–479, Table 20.3, Example 20.2, Fig 20.6 | taught |
> | tetrahedral | S&A §20.1e pp.480–481, Tables 20.4–20.5; Huheey pp.401–403 | taught |
> | square planar, other symmetries | S&A §20.1f p.481, Fig 20.10; Huheey pp.403–405, Fig 11.12, Table 11.5 | taught |
> | Jahn–Teller | S&A §20.1g pp.481–482, Figs 20.11–20.12 | taught |
> | thermochemical correlations, radii, redox, spinels, OSPE | S&A §20.1d,h,i pp.479–483, Figs 20.7, 20.13–20.14, Example 20.3; Huheey pp.408–413, Figs 11.14–11.15, Tables 11.8–11.9 | taught |
> | nephelauxetic effect | Huheey p.413, Table 11.10 (OCR, partly garbled) | taught (end of range) |
> | point-charge derivation, $f\,g$ test, $\Delta_O=P$ derivation, hydration recomputation, OSPE numbers | `scripts/ch10_numbers.py`, `scripts/fig_ch10.py` | extra/beyond |
> | the lectures of 2, 3, 4, 9 Nov | **not in the folder** | gap |
>
> **Notes.** (1) Huheey is a **scan**; its text was read by OCR (Tesseract) and every number used was cross-checked against a sum rule or against S&A. Table 11.5's square-planar $d_{xy}$ entry was lost in OCR and is fixed by the zero trace and by the computation. (2) Book crops are in `Assets/crops/ch/` (15 files; page crops, not redrawn). (3) Values marked `[verify]` were recalled or OCR-doubtful: $g(\mathrm{Co^{2+}})$, $f(\mathrm{Cl^-})$, hexaaqua $\Delta_O$ of $\mathrm{V^{2+}}$, $\mathrm{Cr^{2+}}$, $\mathrm{Cu^{2+}}$, Shannon radii in Fig. CH10.13C, and the book slips (Huheey 338 vs 389 kJ/mol; VCl$_4$ 7900 vs 9010; $\Delta_{SP}/\Delta_O$ 1.3).

**References.** Shriver, D. F. and Atkins, P. W. *Inorganic Chemistry* (5th ed.), §20.1 · Huheey, J. E., Keiter, E. A. and Keiter, R. L. *Inorganic Chemistry* (4th ed.), Ch. 11 pp.394–413 · Jørgensen, C. K. *Modern Aspects of Ligand Field Theory* (1971) · Bethe, H. (1929); Van Vleck, J. H. (1935) *J. Chem. Phys.* 3, 803 · Jahn, H. A. and Teller, E. (1937) *Proc. R. Soc. A* 161, 220 · Irving, H. and Williams, R. J. P. (1953) *J. Chem. Soc.* 3192.

## Across subjects
- [[GT10 Symmetry Representations and Characters]] (Group Theory): the five $d$ orbitals span $E_g+T_{2g}$ in $O_h$ and $E+T_2$ in $T_d$: the splitting is a purely representation-theoretic statement.
- [[Quantum Mechanics - Course Map|Quantum Mechanics]] perturbation ideas: the crystal field is a perturbation of the $d$ shell, first order in the point-charge potential; the Jahn–Teller curve is degenerate perturbation theory.
