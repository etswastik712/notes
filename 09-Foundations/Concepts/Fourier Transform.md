---
title: Fourier Transform
aliases: ["Fourier transform", "FT", "spectrum"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Fourier Transform

> [!intuition] In one picture
> Rewrites a function of $x$ as a continuum of plane waves $e^{ikx}$; the amplitude per wavenumber is $\tilde f(k)$.

> [!key] Key facts
> Vault convention: $\tilde f(k)=\frac1{\sqrt{2\pi}}\int fe^{-ikx}\mathrm dx$, unitary (Plancherel). Rules: shift $\to e^{-ika}$, $f'\to ik\tilde f$, $f*g\to\sqrt{2\pi}\tilde f\tilde g$. Gaussian $\leftrightarrow$ Gaussian.

## In this vault
QM: position $\leftrightarrow$ momentum ([[Fourier Transform and Wave Packets]], [[Parseval-Plancherel Theorem]]). Waves: dispersion. Diffusion: $e^{-Dk^2t}$.

> [!pitfall] Watch out
> The $2\pi$ and sign conventions differ between books: always check with a Plancherel test.

Used in: [[Fourier and Laplace Transforms]]. Related: [[Fourier Series]] · [[Convolution Theorem]] · [[Uncertainty Principle (Fourier)]] · [[Dirac Delta Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
