---
title: Canonical Ensemble
aliases: ["Boltzmann distribution"]
subject: thermo
type: concept
scope: [extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, extra/book, extra/beyond, src/lecture-notes, status/draft]
---
# Canonical Ensemble

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** `Thermo_StatMech_Notes.pdf` §5. · 🔵 **extra · beyond:** relative fluctuations.

> [!intuition] In one picture
> A small system in contact with a big heat bath: its energy fluctuates, and states of low energy are exponentially favoured.

> [!key] Definition
> $p_i=e^{-\beta E_i}/Z$ (the bath's $\Omega_B(E_{\rm tot}-E_i)\propto e^{-E_i/k_BT}$). Fixed $T$ (not fixed $E$); equivalent to the microcanonical ensemble for large $N$.

## Fluctuations
$\Delta E/E=\sqrt{2/3N}$ for a monatomic gas: $2.6\times10^{-12}$ for $N=10^{23}$ (so ensembles are equivalent), $8\%$ for $N=100$.

> [!pitfall] The bath sets the temperature
> The canonical ensemble describes the *system*; $T$ is the bath's.

Used in: [[TH06 From Kinetic Theory to Statistical Mechanics]]. Related: [[Partition Function]] · [[Statistical Entropy]] · [[Equipartition of Energy]] · [[Maxwell-Boltzmann Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Continued in Part II (added 2026-10-30)
- Derivation from a reservoir, $Z$ as a generating function of all energy cumulants, equivalence of ensembles, $F[q]-F=k_BT\,D(q\|p)$, and the exact Gamma law of the ideal-gas energy: [[SM03 The Canonical Ensemble]]; see [[Boltzmann Distribution]] and [[Equivalence of Ensembles]].
