---
title: Dirac Comb and Poisson Summation
aliases: ["Dirac comb", "Shah function", "Poisson summation formula"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Dirac Comb and Poisson Summation

> [!intuition] In one picture
> A train of delta spikes whose Fourier transform is again a train of spikes (spacing $T\leftrightarrow2\pi/T$).

> [!key] Key facts
> $\sum\delta(x-nT)=\frac1T\sum e^{2\pi imx/T}$; Poisson: $\sum_nf(nT)=\frac1T\sum_m\hat f(m/T)$. Check: $\sum e^{-\pi tn^2}=t^{-1/2}\sum e^{-\pi n^2/t}$ ($t=0.7$: $1.2221051$ both sides).

## In this vault
Engine of the [[Sampling Theorem]]; Bloch's theorem and diffraction gratings (reciprocal lattice) in [[QM08 Quantum Tunnelling]].

> [!pitfall] Watch out
> Only meaningful as a distribution ([[Dirac Delta Function]]).

Used in: [[Fourier and Laplace Transforms]]. Related: [[Sampling Theorem]] · [[Dirac Delta Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
