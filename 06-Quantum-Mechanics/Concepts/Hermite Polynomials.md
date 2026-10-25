---
title: Hermite Polynomials
aliases: ["Hermite functions", "oscillator wavefunctions"]
subject: qm
type: concept
scope: [taught, extra-book]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/book, src/lecture-notes, status/draft]
---
# Hermite Polynomials

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the first two excited states are built explicitly in [[Tutorial2.pdf#page=1|Tutorial II Q2]]. · 🟡 **extra · book:** general $H_n$ and the recursion (Griffiths §2.3).

> [!intuition] In one picture
> Each rung adds one more oscillation: polynomial of degree $n$ times the same Gaussian.

> [!key] Definition
> $\psi_n=\Big(\dfrac{m\omega}{\pi\hbar}\Big)^{1/4}\dfrac{1}{\sqrt{2^nn!}}H_n(\xi)e^{-\xi^2/2}$, $\xi=\sqrt{m\omega/\hbar}\,x$; $H_0=1$, $H_1=2\xi$, $H_2=4\xi^2-2$, $H_3=8\xi^3-12\xi$; $H_{n+1}=2\xi H_n-2nH_{n-1}$.

## Pattern
$\psi_1=(m\omega/\pi\hbar)^{1/4}\sqrt2\xi e^{-\xi^2/2}$, $\psi_2=(m\omega/\pi\hbar)^{1/4}(2\xi^2-1)/\sqrt2\,e^{-\xi^2/2}$ (nodes at $\pm1/\sqrt2$). Parity $(-1)^n$; $n$ nodes; all orthonormal.

> [!pitfall] Different conventions
> $H_n$ here is the "physicist's" Hermite polynomial (leading coefficient $2^n$); some books use probabilists' $He_n$.

Used in: [[QM05 The Harmonic Oscillator]]. Related: [[Harmonic Oscillator]] · [[Ladder Operators]] · [[Node of a Wavefunction]] · [[Parity Operator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
