---
title: Statistical Entropy
aliases: ["Boltzmann entropy", "S = k ln Omega"]
subject: thermo
type: concept
scope: [extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, extra/book, extra/beyond, src/lecture-notes, status/draft, quiz/th-tut3]
---
# Statistical Entropy

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** pointer in [[97dcd8dee3d3301cd7c27745b17b10b5_MIT8_333F13_Lec4.pdf#page=5|MIT L4 §I.J]]. · 🟡 **extra · book:** `Thermo_StatMech_Notes.pdf` §3–4.

> [!intuition] In one picture
> Entropy is the logarithm of the number of microscopic ways to realise the macroscopic state.

> [!key] Definition
> $S=k_B\ln\Omega(E,V,N)$ (or $k_B\ln g$ for $g$ degenerate states). Equal a priori probability of accessible microstates; $1/T=\partial S/\partial E$.

## Check
Free expansion $V\to2V$: $\Omega\to2^N\Omega$, $\Delta S=Nk_B\ln2=5.763$ J K$^{-1}$ (same as $R\ln2$). Probability that $N=100$ molecules all return to one half: $2^{-100}=7.9\times10^{-31}$.

> [!pitfall] Counting needs $N!$ and $h$
> Without dividing by $N!$ (indistinguishability) the entropy is not extensive; $h$ makes the phase-space count dimensionless.

Used in: [[TH06 From Kinetic Theory to Statistical Mechanics]]. Related: [[Entropy]] · [[Third Law of Thermodynamics]] · [[Sackur-Tetrode Equation]] · [[Canonical Ensemble]].

## Continued in the vault (added 2026-11-04)
- Elementary counting treatment and simulations: [[TH09 Microstates Macrostates and Multiplicity]] ([[Fundamental Postulate of Statistical Mechanics]], [[Statistical Temperature]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Continued in Part II (added 2026-10-30)
- Phase-space counting, the shell-width independence, the Gibbs paradox and Einstein solids: [[SM02 Phase Space Liouville and the Microcanonical Ensemble]]; Shannon's form $-\sum p\ln p$ and typical sequences: [[SM01 Probability Large Numbers and Information]] ([[Shannon Entropy]]).
- The Boltzmann entropy $S_B=-k_B\int f(\ln h^3f-1)$ of a non-equilibrium gas and its increase (H-theorem), equal to Sackur–Tetrode at equilibrium: [[SM04 Kinetic Theory and the Boltzmann Equation]] §6 ([[H-Theorem]]).
- Coarse-grained decomposition $S_{cg}=\langle S_B\rangle+H[p_M]$ and the five entropies: [[SM06 Entropy Information and the Arrow of Time]] §1 ([[Boltzmann Entropy]], [[Gibbs Entropy]]).
