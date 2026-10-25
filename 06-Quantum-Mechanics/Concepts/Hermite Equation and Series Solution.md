---
title: Hermite Equation and Series Solution
aliases: ["Hermite equation", "Sommerfeld polynomial method", "analytic method", "power-series solution of the oscillator"]
subject: qm
type: concept
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# Hermite Equation and Series Solution

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Griffiths §2.3.2 ([[Griffiths - Introduction to quantum mechanics.pdf#page=52|PDF p.52]], recursion formula pp.54–55). · 🔵 **extra · beyond:** the shooting check and the worked truncations.

> [!intuition] In one picture
> The Schrödinger equation has a solution for every energy, but all except a discrete set blow up at infinity; a power series makes this visible.

> [!key] Definition
> With $\xi=\sqrt{m\omega/\hbar}\,x$, $K=2E/\hbar\omega$: $\psi''=(\xi^2-K)\psi$. Put $\psi=h\,e^{-\xi^2/2}$: $\ h''-2\xi h'+(K-1)h=0$, solved by $h=\sum a_j\xi^j$ with $\ a_{j+2}=\dfrac{2j+1-K}{(j+1)(j+2)}a_j$.

## Why it truncates only at $K=2n+1$
For large $j$, $a_{j+2}/a_j\to2/j$, the ratio of the coefficients of $e^{\xi^2}$; so a non-terminating $h$ grows like $e^{\xi^2}$ and $\psi\sim e^{+\xi^2/2}$ is not normalisable. The series ends iff $2n+1-K=0$, i.e. $E_n=(n+\tfrac12)\hbar\omega$, and the opposite-parity series must be set to zero. Then $h''-2\xi h'+2nh=0$, the **Hermite equation**, and $h\propto H_n$.

## Numbers
$K=5$: $h=1-2\xi^2=-\tfrac12H_2$. $K=9$: $h=1-4\xi^2+\tfrac43\xi^4=\tfrac1{12}H_4$. For the forbidden $K=2$, $a_{j+2}/a_j=0.0844,0.0459,0.0239$ at $j=20,40,80$ against $2/(j+2)=0.0909,0.0476,0.0244$ (→ the $e^{\xi^2}$ ratio).

## Shooting
Integrate $\psi''=(\xi^2-K)\psi$ from $\xi=0$ with $(1,0)$ (even) or $(0,1)$ (odd): $\psi(6)$ changes sign at $K=1,5,9$ and $K=3,7$, i.e. $E/\hbar\omega=\tfrac12,\tfrac52,\tfrac92$ and $\tfrac32,\tfrac72$ (Figure QM6.2 B).

> [!pitfall] Two series, one free constant each
> The even and odd parts decouple, so a non-terminating series cannot be rescued by the other parity; both $a_0$ and $a_1$ are free until quantisation fixes one of them to zero.

Used in: [[QM06 The Oscillator Toolbox]] §4.1. Related: [[Hermite Polynomials]] · [[Hermite Generating Function and Recurrences]] · [[Boundary Conditions and Quantisation]] · [[Energy Quantisation]] · [[Harmonic Oscillator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
