---
title: Sampling Theorem
aliases: ["Nyquist-Shannon theorem", "Nyquist frequency", "sampling theorem"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Sampling Theorem

> [!intuition] In one picture
> A band-limited signal is fully determined by samples taken at more than twice its highest frequency.

> [!key] Key facts
> Sampling replicates the spectrum every $f_s$; no overlap iff $f_s>2B$. Reconstruction: $f(t)=\sum f(nT)\,\mathrm{sinc}(\pi(t-nT)/T)$. Nyquist frequency $f_s/2$.

## In this vault
DEM of spacing $\Delta$ cannot see wavelengths below $2\Delta$ ([[LS03 Digital Elevation Models and Terrain Analysis]]).

> [!pitfall] Watch out
> Anti-alias before sampling, not after.

Used in: [[Fourier and Laplace Transforms]]. Related: [[Aliasing]] · [[Dirac Comb and Poisson Summation]] · [[Discrete Fourier Transform]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
