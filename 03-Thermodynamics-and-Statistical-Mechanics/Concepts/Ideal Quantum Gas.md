---
title: Ideal Quantum Gas
aliases: ["ideal Fermi gas and ideal Bose gas", "free quantum gas", "non-interacting bosons and fermions"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Ideal Quantum Gas

> [!info] Source
> Kardar §7.3 (p. 187); Pathria Ch. 6 and §5.4; Huang §8.6 (p. 185); [[SM08 Quantum Ensembles and Identical Particles]] §5.2.

> [!intuition] In one picture
> A gas of non-interacting identical particles is a set of independent modes with occupation $\langle n\rangle=1/(z^{-1}e^{\beta\varepsilon}-\epsilon)$; all of its thermodynamics is one sum over modes.

> [!key] Key facts
> $\ln\mathcal Z=-\epsilon\sum_k\ln(1-\epsilon ze^{-\beta\varepsilon_k})$ ($\epsilon=+1$ bosons, $-1$ fermions); $PV=k_BT\ln\mathcal Z=\tfrac23E$ for $\varepsilon\propto p^2$ (any statistics); $n\lambda^3/g_s=f_{3/2}(z)$, $P/nk_BT=f_{5/2}(z)/f_{3/2}(z)=1-\epsilon z/2^{5/2}+\dots$ with $f_\nu(z)=\sum_{l\ge1}\epsilon^{l-1}z^l/l^\nu$.

> [!example] Exact numbers (recomputed)
> $z=0.3$: FD $n\lambda^3/g=0.2725$, $P/nkT=1.0479$; BE $0.3383$, $0.9398$. Bosons terminate at $n\lambda^3/g=\zeta(3/2)=2.612$ ($z\to1$; SM13).

Used in: [[SM08 Quantum Ensembles and Identical Particles]]. Related: [[Fermi-Dirac Distribution]] · [[Bose-Einstein Distribution]] · [[Grand Canonical Ensemble]] · [[Exchange Correlation of the Ideal Gas]] · [[Density of States]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
