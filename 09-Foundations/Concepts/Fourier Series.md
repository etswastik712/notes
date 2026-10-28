---
title: Fourier Series
aliases: ["Fourier series", "trigonometric series", "Fourier coefficients"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Fourier Series

> [!intuition] In one picture
> A periodic function written as a sum of sines and cosines (or $e^{inx}$); the coefficients are projections onto an orthonormal basis.

> [!key] Key facts
> $f=\sum c_ne^{inx}$, $c_n=\frac1{2\pi}\int_{-\pi}^{\pi}fe^{-inx}\mathrm dx$; Parseval $\frac1{2\pi}\int\lvert f\rvert^2=\sum\lvert c_n\rvert^2$. Square wave: $\frac4\pi\sum_{\text{odd}}\sin nx/n$. Coefficients decay like $1/n^{m+1}$ if the first $m$ derivatives are continuous.

## In this vault
Sums like $\sum1/n^2=\pi^2/6$ come from Parseval. Related to [[Fourier Transform]] (period $\to\infty$).

> [!pitfall] Watch out
> Convergence is in the mean square always, pointwise at jumps only to the midpoint ([[Gibbs Phenomenon]]).

Used in: [[Fourier and Laplace Transforms]]. Related: [[Fourier Transform]] · [[Gibbs Phenomenon]] · [[Convolution Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
