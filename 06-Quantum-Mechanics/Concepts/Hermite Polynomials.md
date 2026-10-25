---
title: Hermite Polynomials
aliases: ["Hermite functions", "oscillator wavefunctions", "Hermite polynomial H_n", "physicists Hermite polynomials"]
subject: qm
type: concept
scope: [taught, extra-book, extra-beyond]
by: [lecture-notes, book, own-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/book, extra/beyond, src/lecture-notes, src/book, src/own-notes, status/draft]
---
# Hermite Polynomials

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the first excited states are built explicitly by the ladder ([[Tutorial2.pdf#page=1|Tutorial II Q2]], [[Harmonic_oscillator.pdf#page=11|lecture p.11]]). · 🟡 **extra · book:** general $H_n$, the series solution, the recursion and the Rodrigues formula (Griffiths §2.3.2, [[Griffiths - Introduction to quantum mechanics.pdf#page=52|PDF pp.52–59]]). · 🔵 **extra · beyond:** generating-function proofs, zeros, the link to probability.

> [!intuition] In one picture
> Each rung adds one more oscillation: a polynomial of degree $n$ times the same Gaussian.

> [!key] Definition
> $\psi_n(x)=\Big(\dfrac{m\omega}{\pi\hbar}\Big)^{1/4}\dfrac1{\sqrt{2^nn!}}\,H_n(\xi)\,e^{-\xi^2/2}$, $\ \xi=\sqrt{m\omega/\hbar}\,x$; $\ H_n(\xi)=(-1)^ne^{\xi^2}\dfrac{\mathrm d^n}{\mathrm d\xi^n}e^{-\xi^2}$; $\ e^{2\xi t-t^2}=\sum H_n\frac{t^n}{n!}$.

## Facts to keep (all checked symbolically)
| Property | Statement |
|---|---|
| first six | $1,\ 2\xi,\ 4\xi^2-2,\ 8\xi^3-12\xi,\ 16\xi^4-48\xi^2+12,\ 32\xi^5-160\xi^3+120\xi$ |
| recurrence | $H_{n+1}=2\xi H_n-2nH_{n-1}$ |
| derivative | $H_n'=2nH_{n-1}$; $\ H_{n+1}=2\xi H_n-H_n'$ |
| ODE | $H_n''-2\xi H_n'+2nH_n=0$ |
| parity | $H_n(-\xi)=(-1)^nH_n(\xi)$ |
| leading term | $2^n\xi^n$ |
| orthogonality | $\int H_mH_ne^{-\xi^2}\mathrm d\xi=\sqrt\pi\,2^nn!\,\delta_{mn}$ |
| values at 0 | $H_{2k}(0)=(-1)^k(2k)!/k!$, $H_{2k+1}(0)=0$ |

## Why they appear
Writing $\psi=he^{-\xi^2/2}$ turns the Schrödinger equation into the Hermite equation $h''-2\xi h'+(K-1)h=0$; a power series is normalisable only when it terminates, which forces $K=2n+1$, i.e. $E_n=(n+\tfrac12)\hbar\omega$ ([[Hermite Equation and Series Solution]]). The same polynomials come out of the **ladder**: $\hat a^\dagger(H_ne^{-\xi^2/2})=\tfrac1{\sqrt2}H_{n+1}e^{-\xi^2/2}$.

## Shape
$n$ real simple zeros (the nodes): $H_2$: $\pm0.7071$; $H_3$: $0,\pm1.2247$; $H_4$: $\pm0.5246,\pm1.6507$; $H_5$: $0,\pm0.9586,\pm2.0202$. Parity $(-1)^n$; the outermost node lies inside the turning point $\sqrt{2n+1}$ ([[Node of a Wavefunction]], [[Parity Operator]]).

## Cross-links
Fourier transform: $\tilde\psi_n=(-i)^n\psi_n$ in scaled variables ([[Fourier Invariance of Hermite Functions]]). Probability: $\mathrm{He}_n(x)=2^{-n/2}H_n(x/\sqrt2)$ is orthogonal under the normal density ([[Probabilists' Hermite Polynomials]], [[PR06 Moments Generating Functions and Limit Theorems]]). General theory: [[Orthogonal Polynomials]].

> [!pitfall] Three different "Hermite" objects
> The **polynomial** $H_n$ (weight $e^{-\xi^2}$), the **function** $\psi_n=N_nH_ne^{-\xi^2/2}$ (orthonormal on $\mathbb R$) and the probabilists' $\mathrm{He}_n$. Quote which one.

Used in: [[QM05 The Harmonic Oscillator]] §5, [[QM06 The Oscillator Toolbox]] §4. Related: [[Harmonic Oscillator]] · [[Ladder Operators]] · [[Hermite Generating Function and Recurrences]] · [[Hermite Equation and Series Solution]] · [[Normalisation Constants Table]] · [[Gaussian Integral]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
