---
title: Dirac Delta Function
aliases: ["delta function", "Dirac delta", "sifting property"]
subject: foundations
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Dirac Delta Function

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (used):** delta normalisation and the delta potential ([[Delta Function Potential]]). · 🔵 **extra · beyond:** the general properties.

> [!intuition] In one picture
> An infinitely narrow spike of unit area: it picks out the value of a function at one point.

> [!key] Definition
> $\displaystyle\int\delta(x-a)f(x)\,\mathrm dx=f(a)$; $\ \delta(cx)=\delta(x)/|c|$; $\ \displaystyle\int_{-\infty}^\infty e^{ikx}\mathrm dk=2\pi\delta(x)$; $\ \delta=\lim_{\varepsilon\to0}\dfrac{e^{-x^2/2\varepsilon^2}}{\varepsilon\sqrt{2\pi}}$.

## In this vault
Quantum: $\langle x|x'\rangle=\delta(x-x')$, $\langle p|p'\rangle=\delta(p-p')$ ([[Delta-Function Normalisation]]), the delta potential. Probability: the "density" of a point mass is a delta (a degenerate random variable) and a Gaussian of width $\to0$ is its approximation ([[Normal Distribution]]).

> [!pitfall] Not a function
> $\delta$ is a distribution: it only has meaning under an integral.

Used in: [[QM06 The Oscillator Toolbox]] §1. Related: [[Delta-Function Normalisation]] · [[Delta Function Potential]] · [[Fourier Transform and Wave Packets]] · [[Gaussian Integral]].

> [!connection] See also
> Transforms of $\delta$, the comb and Poisson summation: [[Fourier and Laplace Transforms]] §4.

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
