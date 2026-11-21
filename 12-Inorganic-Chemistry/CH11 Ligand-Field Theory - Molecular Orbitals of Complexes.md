---
title: CH11 Ligand-Field Theory - Molecular Orbitals of Complexes
aliases: [CH11, ligand field theory, LFT, MO theory of complexes, MOT of complexes, sigma bonding in complexes, pi bonding in complexes, pi donor, pi acceptor, back bonding, synergic bonding, SALCs octahedral, Shriver Atkins 20.2, Huheey 11 MO]
subject: chemistry
type: chapter
chapter: 11
part: III
scope: [taught, extra-beyond]
by: [book]
status: draft
prereq: ["[[CH10 Crystal Field Theory]]", "[[CH03 Molecular Orbital Theory Polyatomics]]"]
tags: [subject/chemistry, type/chapter, taught, extra/beyond, src/book, src/own-notes, status/draft]
---
# CH11 · Ligand-Field Theory: Molecular Orbitals of Complexes

◀ [[CH10 Crystal Field Theory]] · [[Inorganic Chemistry - Course Map|Course Map]]

<span class="scope-taught">taught · in syllabus (lecture notes = book pages)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map (Classroom, NB, 18 Nov 2026)
> The instructor's post: "**Lecture Notes for MOT/LFT**: Please refer to the text books **Shriver Atkins BOOK 5th Edition Page 483 to 487** and **Huheey, Keiter and Keiter BOOK 4th Edition Page 413 to 424**." No slides were posted: those pages *are* the lecture notes. (Quiz 3, 17 Nov, was crystal-field theory only, "not molecular orbital theory, MOT and Pi-Bonding": [[CH10 Crystal Field Theory]].)
> 🟢 **Taught (the assigned pages, read in full)**
> - §1 why go beyond CFT: nephelauxetic effect, EPR hyperfine evidence of covalency, CFT cannot explain the spectrochemical series (S&A p.483; Huheey pp.413–414)
> - §2 σ bonding in octahedral complexes: metal orbital symmetries, ligand group orbitals (SALCs) $a_{1g}+e_g+t_{1u}$, the MO diagram, $\Delta_O$ between $t_{2g}$ and $e_g^*$ (S&A pp.484–485, Figs 20.15–20.16; Huheey pp.414–417, Figs 11.17–11.20)
> - §3 filling the MOs: $[\mathrm{Co(NH_3)_6}]^{3+}$, $[\mathrm{CoF_6}]^{3-}$; the photoelectron spectrum of $[\mathrm{Mo(CO)_6}]$ (S&A p.485, Example 20.4; Huheey p.417)
> - §4 other geometries: tetrahedral and square planar σ MO diagrams (Huheey pp.417–419, Figs 11.21–11.22)
> - §5 π bonding: four kinds of metal–ligand π interaction, π symmetry in $O_h$, **π donors lower $\Delta_O$, π acceptors raise it**, synergic bonding, the spectrochemical series explained (S&A pp.486–487, Figs 20.19–20.21; Huheey pp.419–424, Figs 11.23–11.28, Table 11.11)
>
> 🔵 **Extra · beyond (mine):** the character-table reductions of $\Gamma_\sigma$ and $\Gamma_\pi$, SALC normalisation, a two-level model of the π shift (`scripts/ch11_numbers.py`), the figure (`scripts/fig_ch11.py`).

> [!key] After this chapter you can
> - give three pieces of evidence that metal–ligand bonds are covalent,
> - list the $O_h$ symmetries of the metal $s$, $p$, $d$ orbitals ($a_{1g}$, $t_{1u}$, $e_g+t_{2g}$) and of the six σ ligand group orbitals ($a_{1g}+e_g+t_{1u}$), and say why $t_{2g}$ is **nonbonding** in a σ-only complex,
> - draw the σ MO diagram of an octahedral complex, place the 12 ligand electrons and the $n$ metal electrons, and identify $\Delta_O$ as the gap between $t_{2g}$ and $e_g^*$,
> - explain with π bonding why **halides and OH⁻ are weak-field** and **CO, CN⁻, PR₃ strong-field**, and what **synergic** (σ donation + π back-donation) bonding is,
> - sketch σ MO diagrams for tetrahedral and square-planar complexes and explain the stability of 16-electron square-planar $d^8$ complexes.

> [!intuition] One sentence
> Ligand-field theory is crystal-field theory with the ligands allowed to share electrons: the same two sets of d-based orbitals appear ($t_{2g}$ and $e_g^*$), but now $e_g^*$ is *antibonding*, so better σ donors push it up, and the $t_{2g}$ set can be pushed up (by filled ligand π orbitals) or pulled down (by empty ones) — which is the spectrochemical series that CFT could only list.

![[fig_ch11_ligand_field.png]]
*Figure CH11.1. A: σ-only MO diagram of an octahedral ML₆ (after S&A Fig. 20.16 and Huheey Fig. 11.20; schematic energies). The frontier orbitals — nonbonding $t_{2g}$ and antibonding $e_g^*$ — reproduce CFT's two sets. B: π bonding acts on $t_{2g}$ only: a π donor (filled ligand orbitals below the metal d) raises it and shrinks $\Delta_O$; a π acceptor (empty ligand π* above d) lowers it and enlarges $\Delta_O$. `scripts/fig_ch11.py`.*

## 1. Why go beyond crystal-field theory?
<span class="scope-taught">taught</span> *S&A p.483 §20.2 opening; Huheey pp.413–414*

CFT treats ligands as point charges or dipoles and ignores the **overlap** of ligand and metal orbitals (S&A). Evidence that the bonds are partly covalent (Huheey):
1. **Nephelauxetic ("cloud-expanding") effect**: electron–electron repulsion in complexes is smaller than in the free ion, as if the d electrons were spread over a larger, delocalised region (nephelauxetic series of metals and ligands, Huheey Table 11.10; [[CH10 Crystal Field Theory]] §10).
2. **EPR hyperfine structure**: unpaired metal electrons interact with **magnetic nuclei on the ligands**, so they are partly delocalised onto them.
3. CFT **cannot account for the spectrochemical series** (S&A): e.g. why OH⁻ is a weaker-field ligand than H₂O, or why neutral CO is so strong.

**Ligand-field theory** is "an application of molecular orbital theory that concentrates on the d orbitals of the central metal atom" (S&A): build symmetry-adapted linear combinations (**SALCs**, Huheey's **ligand group orbitals, LGOs**) of ligand orbitals, combine them with metal orbitals of the same symmetry, and estimate the energies from overlap and electronegativity, checked against UV/visible and photoelectron spectra ([[CH03 Molecular Orbital Theory Polyatomics]] used the same method for molecules).

## 2. σ bonding in an octahedral complex
<span class="scope-taught">taught</span> *S&A pp.484–485; Huheey pp.414–417*

Take six ligands each with one σ orbital pointing at the metal (NH₃, F⁻). The metal valence orbitals ($3d$, $4s$, $4p$ for the first row) fall into four $O_h$ symmetry sets:

| metal orbital | $O_h$ label | degeneracy | σ overlap with ligands? |
|---|---|---|---|
| $s$ | $a_{1g}$ | 1 | yes (spherical) |
| $p_x,p_y,p_z$ | $t_{1u}$ | 3 | yes (along the axes) |
| $d_{x^2-y^2},d_{z^2}$ | $e_g$ | 2 | yes (lobes **on** the axes) |
| $d_{xy},d_{yz},d_{zx}$ | $t_{2g}$ | 3 | **no** (lobes **between** the axes) |

**The ligand SALCs.** Treat the six σ bonds as vectors; under the $O_h$ operations they give the reducible representation $\Gamma_\sigma=(6,0,0,2,2,0,0,0,4,2)$, which reduces to
$$\Gamma_\sigma=a_{1g}+e_g+t_{1u}\qquad(\text{Huheey Fig. 11.18; reduction checked in } \texttt{ch11\_numbers.py}).$$
Unnormalised (S&A, with $\sigma_1\dots\sigma_6$ on $+x,-x,+y,-y,+z,-z$ in Huheey's labelling): $a_{1g}\propto\sigma_1+\dots+\sigma_6$ (normalised $1/\sqrt6$); $t_{1u}\propto\sigma_1-\sigma_2$ (and the $y$, $z$ analogues, $1/\sqrt2$); $e_g\propto\sigma_1+\sigma_2-\sigma_3-\sigma_4$ ($d_{x^2-y^2}$, factor ½) and $2\sigma_5+2\sigma_6-\sigma_1-\sigma_2-\sigma_3-\sigma_4$ ($d_{z^2}$, $1/\sqrt{12}$). **There is no SALC of $t_{2g}$ symmetry**, so the $t_{2g}$ orbitals stay **nonbonding** and wholly on the metal (Huheey Fig. 11.17b: no single sign choice gives net overlap with $d_{xy}$).

**The MO diagram** (Fig. CH11.1A): six bonding MOs ($a_{1g}$, $t_{1u}$, $e_g$), six antibonding ($a_{1g}^*$, $t_{1u}^*$, $e_g^*$), three nonbonding $t_{2g}$. The ligand orbitals lie well below the metal d (NH₃, F⁻ are electronegative), so the **bonding MOs are mostly ligand** ($c_L^2>c_M^2$): the 12 ligand electrons stay mostly on the ligands, "just as the crystal-field theory presumes", but are **partly delocalised** onto the metal. The $4s$ and $4p$ overlap the ligands better than the diffuse $3d$, so $a_{1g}$ and $t_{1u}$ are split furthest; $e_g$ and $e_g^*$ less; $t_{2g}$ not at all (Huheey p.417).

> [!key] What LFT says $\Delta_O$ is
> The **frontier orbitals** are the nonbonding, purely metal $t_{2g}$ and the **antibonding, mainly metal $e_g^*$**: the same two sets as CFT. $\Delta_O$ is their separation. Because $e_g^*$ is antibonding, **a better σ donor (stronger overlap) pushes $e_g^*$ higher and makes $\Delta_O$ larger** (S&A p.485) — so CH₃⁻ and H⁻ are high in the spectrochemical series without any π effect.

## 3. Filling the orbitals
<span class="scope-taught">taught</span> *S&A p.485 and Example 20.4; Huheey p.417*

A $d^n$ complex has $12+n$ electrons: the 12 from the ligands fill $a_{1g}^2t_{1u}^6e_g^4$; the $n$ metal electrons go into $t_{2g}$ and $e_g^*$ exactly as in CFT, high or low spin according to $\Delta_O$ versus the pairing energy $P$ ([[CH10 Crystal Field Theory]] §4).
- **$[\mathrm{Co(NH_3)_6}]^{3+}$** ($d^6$): 18 electrons, $a_{1g}^2t_{1u}^6e_g^4t_{2g}^6$, written simply $t_{2g}^6$: **diamagnetic** (pairing in $t_{2g}$ beats promotion to $e_g^*$).
- **$[\mathrm{CoF_6}]^{3-}$** ($d^6$): small gap, $t_{2g}^4e_g^{*2}$: high spin, 4 unpaired.
- **$[\mathrm{Mo(CO)_6}]$** (S&A Example 20.4): 6 electrons from Mo, 12 from CO: ground configuration $a_{1g}^2t_{1u}^6e_g^4t_{2g}^6$. Its **He(II) photoelectron spectrum** shows the ionisation energies of these MOs directly: the lowest-energy band is the $t_{2g}$ (metal), the higher bands the Mo–CO σ MOs and then the CO-based orbitals (S&A Fig. 20.17: ionisation energies roughly 8–20 eV) — experimental evidence for the MO ordering.

## 4. Other geometries (σ only)
<span class="scope-taught">taught</span> *Huheey pp.417–419, Figs 11.21–11.22*

- **Tetrahedral** ($T_d$): metal $s$ = $a_1$, $p$ = $t_2$, $d$ split into $e$ ($d_{z^2},d_{x^2-y^2}$) and $t_2$ ($d_{xy},d_{yz},d_{zx}$). The four LGOs are $a_1+t_2$. The $t_2$ LGOs interact with **both** metal $t_2$ sets ($p$ and $d$): three $t_2$ MO sets — bonding, slightly antibonding, clearly antibonding. **The metal $e$ orbitals are now nonbonding**; $\Delta_T$ is the gap $e\to t_2^*$. Example **$[\mathrm{CoCl_4}]^{2-}$**: 8 ligand + 7 metal = 15 electrons; 12 fill through $e$, the last 3 unpaired in the slightly antibonding $t_2^*$.
- **Square planar** ($D_{4h}$): $d$ → $a_{1g}$ ($d_{z^2}$), $e_g$ ($d_{xz},d_{yz}$), $b_{2g}$ ($d_{xy}$), $b_{1g}$ ($d_{x^2-y^2}$); $p$ → $a_{2u}$ ($p_z$) + $e_u$ ($p_x,p_y$). Four ligand LGOs: $a_{1g}+b_{1g}+e_u$; the $a_{1g}$ LGO overlaps both metal $a_{1g}$ orbitals ($s$, $d_{z^2}$), giving three MOs of that symmetry; $a_{2u}$, $e_g$, $b_{2g}$ stay nonbonding. **$d^8$ square planar**: 8 + 8 = **16 electrons fill the eight lowest MOs**: all bonding MOs full, all antibonding empty — the MO reason for the stability of square-planar $d^8$ complexes (Ni(II), Pd(II), Pt(II)); more electrons would enter antibonding levels, fewer would weaken bonding.

> [!info] What CFT and LFT share, and what they don't (Huheey p.419)
> The central part of each MO diagram reproduces the CFT splitting pattern of the same symmetry. The **common ground is only the symmetry**: LFT describes the bond itself (antibonding levels have no place in CFT) and gives far better quantitative predictions.

## 5. π bonding
<span class="scope-taught">taught</span> *S&A pp.486–487; Huheey pp.419–424*

**Which orbitals.** A π interaction has a nodal plane containing the bond axis; up to two per ligand, twelve in all for $O_h$ (never all realised). The twelve π vectors give $\Gamma_\pi=t_{1g}+t_{2g}+t_{1u}+t_{2u}$ (Huheey Fig. 11.24; checked). The metal has only $t_{2g}$ ($d_{xy},d_{yz},d_{zx}$) and $t_{1u}$ ($p$); the $t_{1u}$ are already busy in strong σ bonds, and $t_{1g}$, $t_{2u}$ have no metal partner. **So π bonding in an octahedral complex involves the $t_{2g}$ set only** — which is exactly the set that defines the bottom of $\Delta_O$.

**Four kinds of metal–ligand π interaction** (Huheey Table 11.11, Fig. 11.23):

| type | direction | examples |
|---|---|---|
| $p_\pi\to d_\pi$ | filled ligand **p** → empty metal d | RO⁻, RS⁻, O²⁻, F⁻, Cl⁻, Br⁻, I⁻, R₂N⁻ |
| $d_\pi\to d_\pi$ | filled metal d → empty ligand d | R₃P, R₃As, R₂S |
| $d_\pi\to\pi^*$ | filled metal d → empty ligand **π*** | CO, RNC, pyridine, CN⁻, N₂, NO₂⁻, ethylene |
| $d_\pi\to\sigma^*$ | filled metal d → empty ligand **σ*** | H₂, R₃P, alkanes |

(Some ligands fit two classes: I⁻ has filled p and low empty d; R₃P can accept into empty d or P–R σ*.)

### 5.1 π donors lower $\Delta_O$
A **π-donor** ligand has **filled** orbitals of π symmetry (Cl⁻, Br⁻, OH⁻, O²⁻, even H₂O; a π base). They lie below the metal d. Combining with the metal $t_{2g}$: the bonding combinations (mostly ligand) take the ligand π electrons, and the **metal's own $t_{2g}$ electrons now sit in the antibonding $t_{2g}^*$**, raised toward $e_g^*$: **$\Delta_O$ decreases** (S&A Fig. 20.20; Huheey Fig. 11.26 for $[\mathrm{CoF_6}]^{3-}$). This is why **F⁻ and the other halides are at the weak-field end** — weaker even than most σ-only ligands — and why **OH⁻ is weaker-field than H₂O** (a better π donor), "so puzzling in terms of a purely electrostatic model" (Huheey p.422). The net bond-energy gain is slight: the filled bonding $t_{2g}$ go down about as much as the nearly filled $t_{2g}^*$ go up.

### 5.2 π acceptors raise $\Delta_O$
A **π-acceptor** ligand has **empty** π-symmetry orbitals (a π acid), usually its LUMO: the π* of CO and N₂ (largest on C for CO), or the empty d / σ* of PR₃. These lie **above** the metal d. The bonding $t_{2g}$ combinations are then mostly metal and **lower** than the d orbitals: **$\Delta_O$ increases** (S&A Fig. 20.21; Huheey Fig. 11.27). Unlike π donation, this **adds bond energy**: the $t_{2g}$ fall at no cost because the ligand orbitals they mix with are empty.

> [!key] Synergic bonding (Huheey p.423)
> Electron density pushed onto a low-oxidation-state metal by σ donation is carried back to the ligand by π back-donation; "the more electron density that the π system can transfer from the metal to the ligand, the more the metal is able to accept via the σ system", and vice versa. Each system augments the other — up to a point. Back-donation is unfavourable for metals in **high** oxidation states (already positive). The increase in $\Delta_O$ can be large enough to move the $t_{2g}\to e_g^*$ band into the UV: **metal carbonyls are often colourless**.

### 5.3 The spectrochemical series, explained
S&A p.487: the order is partly that of σ-donor strength (CH₃⁻ and H⁻ are very high, being very strong σ donors with no suitable π orbitals), but **where π bonding is possible it dominates**:
$$\text{π donor}\ <\ \text{weak π donor}\ <\ \text{no π effects}\ <\ \text{π acceptor}$$
e.g. I⁻ < Br⁻ < Cl⁻ < F⁻ < OH⁻ < H₂O < NH₃ < … < CN⁻ < CO (the series of [[CH10 Crystal Field Theory]] §3.1). Amines, CH₃⁻ and H⁻ are pure σ. The heavier halides have empty d orbitals that could accept π density, but **empirically all halides are weak-field**, so the p-donor interaction dominates (Huheey p.424). And a caution (S&A): "weak-field / strong-field" says nothing about the overall *strength* of the M–L bond.

> [!example] 🔵 A two-level picture (extra · beyond)
> Mix a metal $t_{2g}$ level at $E_d=-10$ eV with a ligand π level 4 eV below it (donor) or above it (acceptor), coupling 1 eV: the $t_{2g}$-based level moves **up by 0.24 eV** (donor) or **down by 0.24 eV** (acceptor); with $e_g^*$ untouched by π, $\Delta_O$ changes by $\mp0.24$ eV (second-order perturbation, $\beta^2/\Delta E$; `scripts/ch11_numbers.py`). The sign is set only by **which side** of the d level the ligand orbital lies.

## Map of this chapter
> [!connection] How CH11 connects
> **Builds on:** [[CH10 Crystal Field Theory]] (the splitting patterns, $\Delta_O$, LFSE, spin states), [[CH02 Molecular Orbital Theory Diatomics]] and [[CH03 Molecular Orbital Theory Polyatomics]] (LCAO, SALCs, bonding/antibonding), [[CH04 Acid-Base Concepts]] (π acids and π bases), [[CH06 Hard and Soft Acids and Bases]] (soft π-acceptor ligands and low-oxidation-state metals).
> **Other subjects:** [[Group Theory - Course Map]] (characters, reducible representations, projection operators) · [[QM12 The Hydrogen Atom]] (the shapes of the d orbitals, $l=2$) · [[QM10 The Finite Barrier and Tutorial V|QM]] two-level mixing.

## Summary
> [!summary] Cheat-sheet
> - Evidence of covalency: nephelauxetic effect, EPR ligand hyperfine, the spectrochemical series.
> - $O_h$: $s=a_{1g}$, $p=t_{1u}$, $d=e_g+t_{2g}$; σ LGOs $=a_{1g}+e_g+t_{1u}$ → **$t_{2g}$ nonbonding**; 6 bonding (mostly ligand), 6 antibonding; frontier $t_{2g}$ / $e_g^*$; $\Delta_O$ = their gap.
> - $d^n$: $12+n$ electrons; $[\mathrm{Co(NH_3)_6}]^{3+}$ $t_{2g}^6$ diamagnetic; $[\mathrm{CoF_6}]^{3-}$ $t_{2g}^4e_g^{*2}$; Mo(CO)₆ by PES.
> - $T_d$: metal $e$ nonbonding, $t_2$ mixes $p$ and $d$; $[\mathrm{CoCl_4}]^{2-}$ 15 e⁻, 3 unpaired. $D_{4h}$ $d^8$: 16 e⁻ fill all bonding MOs.
> - π: only $t_{2g}$ ($\Gamma_\pi=t_{1g}+t_{2g}+t_{1u}+t_{2u}$). **π donors (filled, below d: halides, OH⁻) raise $t_{2g}$, lower $\Delta_O$; π acceptors (empty, above d: CO, CN⁻, PR₃) lower $t_{2g}$, raise $\Delta_O$**; synergic σ/π; carbonyls colourless.
> - Series: π donor < weak π donor < σ only < π acceptor.

## Practice
1. Why can't CFT explain that OH⁻ is weaker-field than H₂O? How does LFT explain it?
2. Show that no combination of six σ ligand orbitals has $t_{2g}$ symmetry, using $d_{xy}$ and the four ligands in the $xy$ plane.
3. Write the full MO configuration of $[\mathrm{Fe(CN)_6}]^{4-}$ (Fe(II), $d^6$) and of $[\mathrm{FeF_6}]^{3-}$ (Fe(III), $d^5$), and predict their magnetism.
4. Draw the π interaction between a metal $d_{xz}$ orbital and (a) a filled Cl⁻ $p_x$ on the $z$ axis, (b) the empty π* of CO on the $z$ axis.
5. Explain why $[\mathrm{Ni(CN)_4}]^{2-}$ is square planar and diamagnetic using the 16-electron count.
6. Mo(CO)₆ is colourless though Mo(0) is $d^6$. Why?
7. Arrange Cl⁻, NH₃, CO, H₂O, CN⁻, OH⁻ in order of $\Delta_O$ and classify each as π donor, σ only or π acceptor.
8. Why is π back-bonding unimportant in $[\mathrm{CoF_6}]^{3-}$ and important in Ni(CO)₄?
9. In $T_d$, why are the metal $e$ orbitals nonbonding while in $O_h$ it is $t_{2g}$ that is nonbonding?
10. Reduce $\Gamma_\sigma=(6,0,0,2,2,0,0,0,4,2)$ in $O_h$ (order 48) and confirm $a_{1g}+e_g+t_{1u}$.

> [!example]- Solutions
> 1. CFT would make the more negative OH⁻ the *stronger* field. LFT: OH⁻ is a better **π donor** (two filled π lone pairs, higher in energy than water's), raising $t_{2g}$ and shrinking $\Delta_O$.
> 2. $d_{xy}$ has lobes between the axes with signs $+,-,+,-$ around the plane; the four σ orbitals on $\pm x$, $\pm y$ each sit on a nodal plane of $d_{xy}$ (the $xz$ or $yz$ plane), so every overlap integral is zero whatever the signs (Huheey Fig. 11.17b).
> 3. $[\mathrm{Fe(CN)_6}]^{4-}$: 18 electrons, $a_{1g}^2t_{1u}^6e_g^4t_{2g}^6$; CN⁻ is a strong-field π acceptor: low spin, **diamagnetic**. $[\mathrm{FeF_6}]^{3-}$: 17 electrons, $a_{1g}^2t_{1u}^6e_g^4t_{2g}^3e_g^{*2}$; F⁻ is a weak-field π donor: high spin, **5 unpaired**.
> 4. (a) $d_{xz}$ and $p_x$ overlap side-on above and below the $z$ axis: bonding combination mostly Cl, antibonding mostly metal. (b) Same overlap with the CO π* (largest on C): bonding combination mostly metal, lowered.
> 5. Ni(II) $d^8$ + 4 × 2 ligand electrons = 16 fill the eight lowest MOs (all bonding + nonbonding); the antibonding $b_{1g}^*$ ($d_{x^2-y^2}$) stays empty; CN⁻ makes that gap large: diamagnetic.
> 6. CO is a strong π acceptor: $\Delta_O$ is so large that $t_{2g}\to e_g^*$ absorbs in the UV.
> 7. Cl⁻ < OH⁻ < H₂O < NH₃ < CN⁻ < CO: π donor, π donor, weak π donor, σ only, π acceptor, π acceptor.
> 8. F⁻ has no low empty π orbitals and Co(III) is a high oxidation state (back-donation unfavourable). Ni(0) is electron-rich and CO's π* is low: synergic σ donation + π back-donation.
> 9. In $T_d$ the ligands lie between the axes, so the axial $e$ orbitals ($d_{z^2}$, $d_{x^2-y^2}$) point between ligands, while $t_2$ have the right symmetry to mix with the ligand $t_2$ LGOs.
> 10. $n(A_{1g})=\frac1{48}(6+6\cdot2+3\cdot2+3\cdot4+6\cdot2)=\frac{48}{48}=1$ (the classes $E$, $6C_4$, $3C_2$, $3\sigma_h$, $6\sigma_d$); likewise $n(E_g)=1$, $n(T_{1u})=1$, all others 0 (`ch11_numbers.py`).

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | CFT's defect, LFT strategy, σ SALCs, Fig. 20.15–20.16, frontier orbitals, filling, Example 20.4 (Mo(CO)₆ PES) | S&A 5th ed. §20.2a pp.483–486 ([[Shriver and Atkins Inorganic Chemistry 5th Ed.pdf#page=510\|PDF pp.510–513]]; text layer, read) | taught (lecture notes = these pages) |
> | π donors and π acceptors, spectrochemical series interpretation | S&A §20.2b pp.486–487 ([[Shriver and Atkins Inorganic Chemistry 5th Ed.pdf#page=513\|PDF pp.513–514]]) | taught |
> | nephelauxetic, EPR, LGOs, $\Gamma_\sigma$, σ MO diagrams ($O_h$, $T_d$, $D_{4h}$), $[\mathrm{Co(NH_3)_6}]^{3+}$, $[\mathrm{CoCl_4}]^{2-}$, $d^8$ 16 e⁻, π types (Table 11.11), $\Gamma_\pi$, $[\mathrm{CoF_6}]^{3-}$, PR₃, synergic bonding, M(CO)₆, halides | Huheey, Keiter & Keiter 4th ed. pp.413–424 ([[7_Inorganic_Chemistry_by_Huheey_E_Keiter_and_R_Keiter.pdf#page=430\|PDF pp.430–441]]; a scan, read by OCR) | taught |
> | reductions, normalisation, electron counts, two-level shifts; figure | `scripts/ch11_numbers.py`, `scripts/fig_ch11.py` | extra/beyond |
>
> **Notes.** (1) The post gives Huheey "4th Edition Page 413 to 424"; the vault's Huheey copy is the 4th edition and pp.413–424 are §§ on MO theory of complexes (PDF = printed + 17, as in CH10). (2) Huheey is OCR'd: subscripts of symmetry labels were garbled and are restored from the context and the character table; Table 11.11's rows are as OCR'd. (3) The shared drive has the instructor's pre-midsem *Molecular Orbital Theory Part 1/2* PDFs (molecules, not complexes): [[chemistry/inorganic-chemistry/shared-drive-sources|shared-drive sources]].
