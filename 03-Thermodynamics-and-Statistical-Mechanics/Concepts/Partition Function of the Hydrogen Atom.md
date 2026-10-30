---
title: Partition Function of the Hydrogen Atom
aliases: ["hydrogen partition function divergence", "Planck-Larkin cutoff"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Partition Function of the Hydrogen Atom

> [!info] Source
> Standard textbook remark; computed in [[SM03 The Canonical Ensemble]] §6.

> [!intuition] In one picture
> An isolated atom has infinitely many Rydberg levels crowded below the ionisation limit, each with weight close to $2n^2$: the sum cannot converge.

> [!key] Key facts
> $Z=\sum_n2n^2e^{-\beta(E_n-E_1)}\to\infty$ as $n_{\max}^3$; terms $\to2n^2e^{-13.6\,\mathrm{eV}/k_BT}$. Physical cutoff from the neighbours: orbital radius $n^2a_0<r/2$, so $n_{\max}\approx\sqrt{r/2a_0}$ ($45$ at $10^{20}$ m$^{-3}$).

> [!example] Numbers (recomputed)
> $T=10^4$ K: $Z(45)=2.009$ (ground state $99.55$ %, $n=2$: $2.9\times10^{-5}$); $Z(10^3)=95$, $Z(10^4)=9\times10^4$. $T=5800$ K: $Z=2.000$ up to $n=45$ but $1006$ at $n_{\max}=10^5$; ratio $n=2/n=1$ $=5.4\times10^{-9}$. The proper treatment includes ionisation: Saha equation (grand canonical, SM04 planned).

Used in: [[SM03 The Canonical Ensemble]]. Related: [[Partition Function]] · [[Canonical Ensemble]] · [[Thermal Wavelength]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
