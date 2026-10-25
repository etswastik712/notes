---
title: Normalisation of a Wavefunction
aliases: ["normalisation", "normalization", "normalising a state"]
subject: qm
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Normalisation of a Wavefunction

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_Wavefunction_to_Uncertainty (1).pdf#page=1|WU §2]], [[Particle_in_a_box.pdf#page=5|box lecture pp.5–6]], [[Harmonic_oscillator.pdf#page=7|oscillator lecture p.7]], the tutorial Q2 and Q3 constants. · 🔵 **extra · beyond:** the three ways for $\psi_n$, superpositions with overlap, continuum normalisation.

> [!intuition] In one picture
> Scale the amplitude so that the total probability is exactly 1.

> [!key] Definition
> Choose $N$ in $\psi=N\varphi$ so that $\displaystyle\int|\psi|^2\mathrm dx=\langle\psi|\psi\rangle=1$. It fixes $|N|$ only; the overall phase is free.

## Procedure
1. Check $\int|\varphi|^2\mathrm dx<\infty$ (normalisable; [[Admissible Wavefunction]]).
2. Compute $I=\int|\varphi|^2\mathrm dx$; set $N=I^{-1/2}$ (times any phase).
3. Re-check: the Schrödinger equation is linear, so $N\varphi$ is still a solution; the evolution keeps $\int|\Psi|^2$ fixed ([[Probability Current]]).

## Constants
All the standard constants (box $\sqrt{2/a}$, ring $1/\sqrt L$, $e^{-|x|/a}$: $1/\sqrt a$, Gaussian $(2\pi\sigma^2)^{-1/4}$, oscillator $\psi_0$ and $\psi_n$) are tabulated with their integrals in [[Normalisation Constants Table]].

## The oscillator $\psi_n$ three ways
(a) **ladder:** only $\psi_0$ needs an integral, then $\|\hat a^\dagger\psi_n\|^2=n+1$; (b) **Hermite integral:** $\int H_n^2e^{-\xi^2}=\sqrt\pi2^nn!$; (c) **recursion** $N_{n+1}=N_n/\sqrt{2(n+1)}$; all give $N_n=(m\omega/\pi\hbar)^{1/4}/\sqrt{2^nn!}$ ([[QM06 The Oscillator Toolbox]] §1).

## Superpositions
For orthonormal $\psi_n$: $\sum|c_n|^2=1$. For non-orthogonal parts the cross terms count: $\|\,|\alpha\rangle+|-\alpha\rangle\|^2=2+2e^{-2|\alpha|^2}$, so $N=0.66363$ for $\alpha=1$.

## Other spaces
Momentum space is automatically normalised by Parseval ([[Parseval-Plancherel Theorem]]); plane waves are delta-normalised ([[Delta-Function Normalisation]]); in probability the same step normalises a **pdf**: $\int f=1$ (the sheet problem $c(1-x^2)$ in [[PR05 Continuous Random Variables]]); the difference is that a wavefunction normalises $|\psi|^2$, not $\psi$.

> [!pitfall] A plane wave cannot be normalised on the line, and $|N|^2$ not $N$
> $\int|A|^2\mathrm dx$ diverges on the line; on a ring of length $L$ the same wave is normalised by $1/\sqrt L$. Normalisability depends on the domain. When solving, you get $|N|^2$ from the integral, so take a square root.

Used in: [[QM01 From Waves to Probabilities]], [[QM02 The Schrodinger Equation and Stationary States]], [[QM04 The Particle in a Box]], [[QM05 The Harmonic Oscillator]], [[QM06 The Oscillator Toolbox]] §1. Related: [[Born Rule]] · [[Admissible Wavefunction]] · [[Orthonormality of Eigenfunctions]] · [[Gaussian Integral]] · [[Normalisation Constants Table]] · [[Delta-Function Normalisation]] · [[Probability Density Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
