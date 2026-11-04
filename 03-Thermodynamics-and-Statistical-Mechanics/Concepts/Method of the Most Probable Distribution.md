---
title: Method of the Most Probable Distribution
aliases: ["Boltzmann's method", "most probable occupation numbers", "method of Lagrange multipliers for distributions"]
subject: thermo
type: concept
scope: [extra-book]
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, extra/book, src/book, src/own-notes, status/draft]
---
# Method of the Most Probable Distribution

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Koks §5.1 and §7.9 (p. 432: particle statistics from counting configurations); Reif Ch. 6 preliminaries; Pathria Ch. 3 ("the method of the most probable distribution").
> 🟢 **taught (pointer only):** [[TH09 Microstates Macrostates and Multiplicity]] §6.

> [!intuition] In one picture
> Count the microstates of each possible set of occupation numbers, maximise the count subject to fixed $N$ and $E$, and read off the Boltzmann, Fermi–Dirac or Bose–Einstein law.

> [!key] Key facts
> Distinguishable: $W=N!\prod g_i^{N_i}/N_i!\Rightarrow N_i=g_ie^{-\alpha-\beta\varepsilon_i}$. Fermions: $W=\prod\binom{g_i}{n_i}\Rightarrow n_i/g_i=1/(e^{\alpha+\beta\varepsilon_i}+1)$. Bosons: $W=\prod\binom{n_i+g_i-1}{n_i}\Rightarrow n_i/g_i=1/(e^{\alpha+\beta\varepsilon_i}-1)$. $\beta=1/k_BT$ from $\delta S=\delta E/T$.

> [!example] Exact enumeration (recomputed)
> 5 levels, mean energy 1: the average over all microstates deviates from the Boltzmann fractions by $0.0145,\ 0.0047,\ 0.0023,\ 0.0012$ for $N=10,\ 30,\ 60,\ 120$ ($\propto1/N$). FD/BE with $g=8,16,32$: $0.0063,\ 0.0031,\ 0.0015$ and $0.0302,\ 0.0150,\ 0.0075$.

Used in: [[TH09 Microstates Macrostates and Multiplicity]]; [[SM03 The Canonical Ensemble]]; [[SM08 Quantum Ensembles and Identical Particles]].. Related: [[Boltzmann Distribution]] · [[Fermi-Dirac Distribution]] · [[Bose-Einstein Distribution]] · [[Stirling's Approximation]] · [[Maxwell-Boltzmann Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
