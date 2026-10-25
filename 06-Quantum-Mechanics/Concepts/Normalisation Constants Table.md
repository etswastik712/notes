---
title: Normalisation Constants Table
aliases: ["normalisation constants", "list of normalisation constants"]
subject: qm
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Normalisation Constants Table

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** box, ring, Gaussian, $\psi_0$ constants. · 🔵 **extra · beyond:** $\psi_n$ in three ways and the continuum case.

> [!intuition] In one picture
> One place to look up "what constant makes this state normalised?".

> [!key] Definition
> $\int|\psi|^2\mathrm dx=1$ fixes $|N|$; the phase is free.

| State | $N$ | Because |
|---|---|---|
| box $\sin(n\pi x/a)$ | $\sqrt{2/a}$ | $\int_0^a\sin^2=a/2$ |
| ring $e^{ik_nx}$ | $1/\sqrt L$ | $\int_0^L1=L$ |
| $e^{-\lvert x\rvert/a}$ | $1/\sqrt a$ | $2\int_0^\infty e^{-2x/a}=a$ |
| $e^{-x^2/4\sigma^2}$ | $(2\pi\sigma^2)^{-1/4}$ | $\int e^{-ax^2}=\sqrt{\pi/a}$ |
| $\psi_0$ oscillator | $(m\omega/\pi\hbar)^{1/4}$ | same |
| $\psi_n$ oscillator | $(m\omega/\pi\hbar)^{1/4}(2^nn!)^{-1/2}$ | $\int H_n^2e^{-\xi^2}=\sqrt\pi2^nn!$ |
| $\sum c_n\psi_n$ | $\sum\lvert c_n\rvert^2=1$ | orthonormality |
| $\lvert\alpha\rangle+\lvert-\alpha\rangle$ | $[2(1+e^{-2\lvert\alpha\rvert^2})]^{-1/2}$ | $\langle\alpha\vert-\alpha\rangle=e^{-2\lvert\alpha\rvert^2}$ |
| plane wave $e^{ikx}/\sqrt{2\pi}$ | $\delta(k-k')$ | [[Delta-Function Normalisation]] |

## Checks
$\int\psi_n^2\mathrm dx=1$ numerically for $n\le10$; cat state with $\alpha=1$: $N=0.66363$; $\int H_2^2e^{-\xi^2}=8\sqrt\pi$.

> [!pitfall] Normalisable vs normalised
> Growing functions and plane waves on a line are not normalisable; Gaussians and the others become states only after multiplying by $N$.

Used in: [[QM01 From Waves to Probabilities]], [[QM04 The Particle in a Box]], [[QM06 The Oscillator Toolbox]] §1. Related: [[Normalisation of a Wavefunction]] · [[Gaussian Integral]] · [[Hermite Polynomials]] · [[Born Rule]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
