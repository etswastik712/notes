---
title: Gibbs Phenomenon
aliases: ["Gibbs phenomenon", "Gibbs overshoot", "ringing"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Gibbs Phenomenon

> [!intuition] In one picture
> Partial Fourier sums overshoot a jump by a fixed 8.95 % of the jump, however many terms are used.

> [!key] Key facts
> Overshoot $=\frac2\pi\mathrm{Si}(\pi)-1=0.179$ for a jump of 2 (8.95 %). Located at $x=\pi/2N$; the region shrinks, the height does not.

## In this vault
Ringing near sharp edges in filtered images and DEMs. Cure: smooth windows (Fejér, Hann) at the price of a blurred edge.

> [!pitfall] Watch out
> $L^2$ convergence does not imply uniform convergence.

Used in: [[Fourier and Laplace Transforms]]. Related: [[Fourier Series]] · [[Spectral Leakage and Windows]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
