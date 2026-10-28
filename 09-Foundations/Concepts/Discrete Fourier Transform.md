---
title: Discrete Fourier Transform
aliases: ["DFT", "discrete Fourier transform"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Discrete Fourier Transform

> [!intuition] In one picture
> The Fourier transform of $N$ equally spaced samples, itself $N$ numbers.

> [!key] Key facts
> $X_m=\sum_nx_ne^{-2\pi imn/N}$; $FF^\dagger=N\mathbf 1$; cyclic convolution theorem. Resolution $1/\mathcal T$. It is the character table of $\mathbb Z_N$.

## In this vault
Group theory link: [[GT04 Symmetry Representations and Characters]], [[Character Table]]. Numerics: [[Fast Fourier Transform]].

> [!pitfall] Watch out
> Zero-padding interpolates, it does not improve resolution.

Used in: [[Fourier and Laplace Transforms]]. Related: [[Fast Fourier Transform]] · [[Spectral Leakage and Windows]] · [[Sampling Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
