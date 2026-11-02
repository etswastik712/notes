---
title: Wigner-Kirkwood Expansion
aliases: ["semiclassical expansion", "hbar expansion of the partition function", "quantum corrections to the partition function"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Wigner-Kirkwood Expansion

> [!info] Source
> Wigner (1932), Kirkwood (1933), quoted; Pathria Ch. 5, Huang Ch. 8 treat the free-particle case; [[SM08 Quantum Ensembles and Identical Particles]] §3.2.

> [!intuition] In one picture
> Quantum mechanics lowers the partition function of a confined particle by the mean squared force: the first correction is of order $\hbar^2$.

> [!key] Key facts
> $Z=Z_{\rm cl}\big[1-\frac{\beta^3\hbar^2}{24m}\sum_i\langle(\nabla_iV)^2\rangle_{\rm cl}+O(\hbar^4)\big]$ (recalled). Oscillator: $-x^2/24$ with $x=\hbar\omega/k_BT$, reproducing $\frac{x/2}{\sinh(x/2)}=1-x^2/24+\dots$.

> [!example] Oscillator check (recomputed)
> Exact $z_q/z_c$ at $x=0.1,\ 0.5,\ 1,\ 2$: $0.99958,\ 0.98966,\ 0.95952,\ 0.85092$; series $0.99958,\ 0.98958,\ 0.95833,\ 0.83333$.

Used in: [[SM08 Quantum Ensembles and Identical Particles]]. Related: [[Partition Function]] · [[Density Matrix]] · [[Thermal Wavelength]] · [[SM03 The Canonical Ensemble|SM03]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
