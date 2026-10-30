---
title: Wick's Theorem
aliases: ["Isserlis theorem", "Wick contraction"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Wick's Theorem

> [!info] Source
> Kardar §2.4 (p.45); [[SM01 Probability Large Numbers and Information]] §2.3.

> [!intuition] In one picture
> In a Gaussian every even moment is a sum over all ways of pairing the variables, each pair contributing its covariance.

> [!key] Key facts
> For zero-mean jointly Gaussian variables $\langle x_ax_bx_cx_d\rangle=C_{ab}C_{cd}+C_{ac}C_{bd}+C_{ad}C_{bc}$; for one variable $\langle x^{2k}\rangle=(2k-1)!!\,\sigma^{2k}$ ($=\tfrac{(2k)!}{2^kk!}\sigma^{2k}$, the number of pairings). Odd moments vanish.

> [!example] Moments
> $\langle x^4\rangle=3\sigma^4$ (3 pairings), $\langle x^6\rangle=15\sigma^6$ (15 pairings). The same numbers are $\langle x^{2k}\rangle$ in the oscillator ground state ([[Moment Generating Function]], [[Probabilists' Hermite Polynomials]]).

*Why:* the generating function $e^{\sigma^2t^2/2}$ has only the term $\kappa_2$, so every moment is built from $\kappa_2$ alone. In quantum field theory the same statement says all Feynman diagrams of a free field are products of propagators.

Used in: [[SM01 Probability Large Numbers and Information]]. Related: [[Cumulant]] · [[Gaussian Integral]] · [[Normal Distribution]] · [[Covariance Matrix]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
