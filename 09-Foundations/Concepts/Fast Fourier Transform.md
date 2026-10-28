---
title: Fast Fourier Transform
aliases: ["FFT", "Cooley-Tukey"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Fast Fourier Transform

> [!intuition] In one picture
> Divide and conquer evaluation of the DFT in $N\log_2N$ operations instead of $N^2$.

> [!key] Key facts
> Split into even and odd samples: $X_m=E_m+\omega^mO_m$. Speed-up $N/\log_2N$: 102 for $N=2^{10}$, 52 429 for $N=2^{20}$.

## In this vault
Makes spectral methods, fast convolution and DEM filtering practical.

> [!pitfall] Watch out
> Fastest for $N$ with small prime factors (powers of 2).

Used in: [[Fourier and Laplace Transforms]]. Related: [[Discrete Fourier Transform]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
