---
title: Hermite Generating Function and Recurrences
aliases: ["Rodrigues formula", "Hermite recurrence", "generating function of Hermite polynomials", "orthogonality of Hermite polynomials"]
subject: qm
type: concept
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# Hermite Generating Function and Recurrences

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** the recursion and Rodrigues formula appear in Griffiths §2.3.2 ([[Griffiths - Introduction to quantum mechanics.pdf#page=56|PDF pp.56–59]]). · 🔵 **extra · beyond:** the generating-function derivations and the check.

> [!intuition] In one picture
> One exponential, $e^{2\xi t-t^2}$, stores every Hermite polynomial as a Taylor coefficient, and every identity is a one-line derivative of it.

> [!key] Definition
> $e^{2\xi t-t^2}=\displaystyle\sum_{n=0}^\infty H_n(\xi)\frac{t^n}{n!}$. Equivalently $H_n=(-1)^ne^{\xi^2}\dfrac{\mathrm d^n}{\mathrm d\xi^n}e^{-\xi^2}$ (**Rodrigues**).

## What follows (all checked symbolically)
- $\partial_\xi$: $H_n'=2nH_{n-1}$. $\ \partial_t$: $H_{n+1}=2\xi H_n-2nH_{n-1}$. Together $H_{n+1}=2\xi H_n-H_n'$ and $H_n''-2\xi H_n'+2nH_n=0$.
- Parity $H_n(-\xi)=(-1)^nH_n$; leading term $2^n\xi^n$; $H_{2k}(0)=(-1)^k(2k)!/k!$.
- $\displaystyle\int H_mH_ne^{-\xi^2}\mathrm d\xi=\sqrt\pi\,2^nn!\,\delta_{mn}$ (multiply two generating functions, integrate: $\sqrt\pi e^{2st}$).

| $n$ | $H_n(\xi)$ |
|---|---|
| 0 | $1$ |
| 1 | $2\xi$ |
| 2 | $4\xi^2-2$ |
| 3 | $8\xi^3-12\xi$ |
| 4 | $16\xi^4-48\xi^2+12$ |
| 5 | $32\xi^5-160\xi^3+120\xi$ |
| 6 | $64\xi^6-480\xi^4+720\xi^2-120$ |

## Link to the ladder
$\hat a_+(H_ne^{-\xi^2/2})=\tfrac1{\sqrt2}H_{n+1}e^{-\xi^2/2}$ and $\hat a_-(H_ne^{-\xi^2/2})=\sqrt2\,nH_{n-1}e^{-\xi^2/2}$: the ladder relations *are* these recurrences.

> [!pitfall] Convention
> This is the physicists' $H_n$ (weight $e^{-\xi^2}$, leading coefficient $2^n$); the probabilists' $\mathrm{He}_n$ (weight $e^{-x^2/2}$) differ by a rescaling ([[Probabilists' Hermite Polynomials]]).

Used in: [[QM06 The Oscillator Toolbox]] §4.2–§4.3. Related: [[Hermite Polynomials]] · [[Hermite Equation and Series Solution]] · [[Orthogonal Polynomials]] · [[Ladder Operators]] · [[Gaussian Integral]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Moment Generating Function]] (Probability): the generating function $e^{xt-t^2/2}=\sum He_n(x)t^n/n!$ is the exponential kernel $e^{tx}$ divided by the moment generating function of the standard normal, $E[e^{tZ}]=e^{t^2/2}$.
