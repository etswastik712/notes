---
title: Gaussian Integral
aliases: ["Gaussian integrals", "completing the square"]
subject: foundations
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/foundations, type/concept, taught, src/lecture-notes, status/draft]
---
# Gaussian Integral

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_wavefunctions_potentials_schrodinger_Tutorial.pdf#page=4|Tutorial P6]] and Tutorial II Q5 ([[Tutorial2.pdf#page=2|p.2]]).

> [!intuition] In one picture
> Square the integral and go to polar coordinates; the awkward $x$-integral becomes an easy $r$-integral.

> [!key] Definition
> $\displaystyle\int_{-\infty}^{\infty}e^{-ax^2}\mathrm dx=\sqrt{\pi/a}$ and $\displaystyle\int_{-\infty}^{\infty}e^{-ax^2+bx}\mathrm dx=\sqrt{\pi/a}\,e^{b^2/4a}$ ($\mathrm{Re}\,a>0$).

## Derivation and uses
$I^2=\iint e^{-a(x^2+y^2)}\mathrm dx\,\mathrm dy=\int_0^{2\pi}\mathrm d\theta\int_0^\infty re^{-ar^2}\mathrm dr=\pi/a$. Complete the square for the second form.

> [!example] Fourier transform and normalisation
> With $a=1/2\sigma^2$, $b=-ik$: $\frac1{\sqrt{2\pi}}\int e^{-x^2/2\sigma^2-ikx}\mathrm dx=\sigma e^{-\sigma^2k^2/2}$. Normalising $\psi=Ae^{-x^2/4\sigma^2}$ with $a=1/2\sigma^2$ gives $A=(2\pi\sigma^2)^{-1/4}$. Moments: $\langle x^2\rangle=\sigma^2$.

> [!pitfall] Convergence
> Needs $\mathrm{Re}\,a>0$; $b$ may be complex (that is how the Fourier transform works), but $a$ must not be zero or negative. In probability the same integral normalises the normal distribution ([[Probability - Course Map]]).

Used in: [[QM01 From Waves to Probabilities]], [[QM05 The Harmonic Oscillator]]. Related: [[Gaussian Wave Packet]] · [[Fourier Transform and Wave Packets]] · [[Heisenberg Uncertainty Principle]].

## Added with QM06 (oscillator toolbox)
Moments used by the oscillator: $\int x^2e^{-ax^2}\mathrm dx=\dfrac{\sqrt\pi}{2a^{3/2}}$ (by parts, or $-\partial_a\sqrt{\pi/a}$), and in general $\int x^{2k}e^{-ax^2}\mathrm dx=\dfrac{\Gamma(k+\frac12)}{a^{k+1/2}}$. With $a=m\omega/\hbar$ and the ground-state normalisation $\sqrt{a/\pi}$: $\langle x^2\rangle=1/2a=\hbar/2m\omega$ (Tutorial III Q2) and $\langle x^{2k}\rangle=(2k-1)!!\,(1/2a)^k$. Hermite weight: $\int H_mH_ne^{-\xi^2}=\sqrt\pi2^nn!\delta_{mn}$ ([[Hermite Generating Function and Recurrences]]). See [[Probabilists' Hermite Polynomials]].

> [!connection] See also
> The Gaussian's Fourier transform by completing the square: [[Fourier and Laplace Transforms]] §3.3.

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Continued in Part II (added 2026-10-30)
- The momentum integral behind $\lambda=h/\sqrt{2\pi mk_BT}$ and the saddle-point method: [[SM03 The Canonical Ensemble]] §4.1, [[Saddle Point Method]].
