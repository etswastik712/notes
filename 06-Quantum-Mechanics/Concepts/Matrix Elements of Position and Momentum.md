---
title: Matrix Elements of Position and Momentum
aliases: ["x matrix", "tridiagonal matrix of x", "matrix elements of x"]
subject: qm
type: concept
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# Matrix Elements of Position and Momentum

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Griffiths §2.3 gives $\hat x,\hat p$ in terms of $\hat a_\pm$ ([[Griffiths - Introduction to quantum mechanics.pdf#page=47|PDF p.47]]); the lecture uses it for $\langle x\rangle$ ([[Harmonic_oscillator.pdf#page=12|p.12]]). · 🔵 **extra · beyond:** the matrices, the $p$–$x$ relation and the checks.

> [!intuition] In one picture
> Position hops the oscillator one rung up or down; it never leaves it where it was.

> [!key] Definition
> $\langle m|\hat x|n\rangle=\sigma\big(\sqrt n\,\delta_{m,n-1}+\sqrt{n+1}\,\delta_{m,n+1}\big)$, $\ \langle m|\hat p|n\rangle=\dfrac{i\hbar}{2\sigma}\big(\sqrt{n+1}\,\delta_{m,n+1}-\sqrt n\,\delta_{m,n-1}\big)$, $\ \sigma=\sqrt{\hbar/2m\omega}$.

## First entries (units $\sigma$)
$x_{01}=1$, $x_{12}=\sqrt2$, $x_{23}=\sqrt3$, $x_{34}=2$ ($\times\sigma$; in units $\sqrt{\hbar/m\omega}$: $0.71,\ 1,\ 1.22,\ 1.41$, Fig. QM6.1 A). $\hat x^2$ has $\langle n|\hat x^2|n\rangle=(2n+1)\sigma^2$ and $\langle n+2|\hat x^2|n\rangle=\sigma^2\sqrt{(n+1)(n+2)}$.

## Relation between $\hat p$ and $\hat x$
From $\hat p=m\,\mathrm d\hat x/\mathrm dt=\frac{im}\hbar[\hat H,\hat x]$: $\ \langle m|\hat p|n\rangle=\dfrac{im(E_m-E_n)}\hbar\langle m|\hat x|n\rangle$, e.g. $p_{n+1,n}=im\omega\,x_{n+1,n}$ (checked).

## Check of the canonical commutator
$\langle0|[\hat x,\hat p]|0\rangle=x_{01}p_{10}-p_{01}x_{10}=\tfrac{i\hbar}2+\tfrac{i\hbar}2=i\hbar$ using only two matrix elements.

> [!pitfall] Real, imaginary and Hermitian
> $\hat x$ is real symmetric, $\hat p$ purely imaginary antisymmetric; both are Hermitian. A different phase convention for $|n\rangle$ changes the signs/phases of these entries but never the physics.

Used in: [[QM06 The Oscillator Toolbox]] §2–§3. Related: [[Number Basis]] · [[Selection Rules]] · [[Ladder Operators]] · [[Oscillator Expectation Values]] · [[Canonical Commutation Relation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
