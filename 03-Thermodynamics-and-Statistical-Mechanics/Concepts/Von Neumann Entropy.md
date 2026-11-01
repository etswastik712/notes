---
title: Von Neumann Entropy
aliases: ["quantum entropy", "S = -k Tr rho ln rho"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Von Neumann Entropy

> [!info] Source
> von Neumann (1927); Blundell §15.4; [[SM06 Entropy Information and the Arrow of Time]] §5.

> [!intuition] In one picture
> The Shannon entropy of the eigenvalues of the density matrix: zero for a pure state, $\ln d$ for the maximally mixed state.

> [!key] Key facts
> $S_{\rm vN}=-k_B\mathrm{Tr}\,\hat\rho\ln\hat\rho$; invariant under $\hat\rho\to U\hat\rho U^\dagger$; maximised at fixed $\langle\hat H\rangle$ by $e^{-\beta\hat H}/Z$.

> [!example] Two-level
> Maximally mixed qubit: $\ln2=1$ bit; for the thermal state with $\varepsilon/kT=1$: $S/k=0.582$ (SM03).

Used in: [[SM06 Entropy Information and the Arrow of Time]]. Related: [[Entanglement Entropy]] · [[Gibbs Entropy]] · [[Shannon Entropy]] · [[Canonical Ensemble]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
