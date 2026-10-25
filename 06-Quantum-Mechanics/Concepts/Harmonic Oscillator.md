---
title: Harmonic Oscillator
aliases: ["quantum harmonic oscillator", "oscillator"]
subject: qm
type: concept
scope: [taught, extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/book, extra/beyond, src/lecture-notes, status/draft]
---
# Harmonic Oscillator

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Tutorial2.pdf#page=1|Tutorial II]]. · 🟡 **extra · book:** Hermite functions (Griffiths §2.3). · 🔵 **extra · beyond:** molecular numbers.

> [!intuition] In one picture
> A parabola potential is the generic shape near any minimum, and its levels are an equally spaced ladder.

> [!key] Definition
> $V=\tfrac12m\omega^2x^2$: $E_n=(n+\tfrac12)\hbar\omega$, $\psi_0=(m\omega/\pi\hbar)^{1/4}e^{-m\omega x^2/2\hbar}$, $\psi_n=(\hat a_+)^n\psi_0/\sqrt{n!}$; parity $(-1)^n$, $n$ nodes.

## Numbers
$\Delta x\Delta p=(n+\tfrac12)\hbar$; $\langle V\rangle=\langle T\rangle=E/2$; forbidden-region probability $15.7\%$ ($n=0$). **CO:** $\hbar\omega=0.266$ eV ($2144$ cm$^{-1}$, $4.66$ µm). **CO$_2$ bend:** $0.083$ eV ($667$ cm$^{-1}$, $15.0$ µm; [[CL07 Optical Properties of the Atmosphere]]).

> [!pitfall] Superposition moves, eigenstates do not
> $\langle x\rangle=0$ in every $\psi_n$, but $(\psi_0+\psi_1)/\sqrt2$ has $\langle x\rangle=\sqrt{\hbar/2m\omega}\cos\omega t$.

Used in: [[QM05 The Harmonic Oscillator]]. Related: [[Ladder Operators]] · [[Number Operator]] · [[Hermite Polynomials]] · [[Zero-Point Energy]].

## Added with QM06 (oscillator toolbox)
Everything beyond the course material is in [[QM06 The Oscillator Toolbox]]: [[Number Basis]], [[Matrix Elements of Position and Momentum]], [[Selection Rules]], [[Oscillator Expectation Values]] ($\langle x^4\rangle=(6n^2+6n+3)\sigma^4$), [[Hermite Equation and Series Solution]], [[Hermite Generating Function and Recurrences]], [[Fourier Invariance of Hermite Functions]], [[Ehrenfest Theorem]], [[Virial Theorem]], [[Heisenberg Picture]], [[Coherent State]], [[Thermal Harmonic Oscillator]], [[Einstein Heat Capacity]], [[Isotropic Oscillator and Degeneracy]], [[Anharmonic Oscillator]], [[Classical Probability Density of the Oscillator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
