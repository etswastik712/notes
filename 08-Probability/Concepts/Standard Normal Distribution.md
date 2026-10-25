---
title: Standard Normal Distribution
aliases: ["N(0,1)", "standard normal", "SND"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Standard Normal Distribution

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[week1_mt2113.pdf#page=8|week 1 p.8]], [[week1_mt2113.pdf#page=9|p.9]].

> [!intuition] In one picture
> The bell curve with mean 0 and variance 1; every other normal is a stretch and shift of it.

> [!key] Definition
> $\varphi(z)=\frac1{\sqrt{2\pi}}e^{-z^2/2}$; $\Phi(z)=\int_{-\infty}^z\varphi$. $E[Z]=0$, $\mathrm{Var}[Z]=E[Z^2]=1$, $E[Z^4]=3$.

## $\int\varphi=1$ via polar coordinates
$I=\int e^{-x^2/2}dx$, $I^2=\iint e^{-(x^2+y^2)/2}dx\,dy=\int_0^{2\pi}\int_0^\infty e^{-r^2/2}r\,dr\,d\theta=2\pi$, so $I=\sqrt{2\pi}$ ([[Gaussian Integral]]).

## Moments
$E[Z]=0$ (odd); $E[Z^2]=\frac2{\sqrt{2\pi}}\int_0^\infty z^2e^{-z^2/2}dz=1$; $E[Z^{2k}]=1,3,15,105,\dots$ Expected excess $E[(Z-c)^+]=\varphi(c)-c(1-\Phi(c))$: $0.3989$ at $c=0$, $0.0833$ at $c=1$.

Used in: [[PR05 Continuous Random Variables]]. Related: [[Normal Distribution]] · [[Gaussian Integral]] · [[Standardisation of a Random Variable]].

## Added with the Week 2 and Week 3 lectures
$|Z|$ is the folded (half-) normal: $f=2\varphi$ on $y\ge0$, mean $\sqrt{2/\pi}$, variance $1-\frac2\pi$, MGF $2e^{t^2/2}\Phi(t)$ ([[Folded Normal Distribution]]). Even moments $E[Z^{2k}]=\frac{(2k)!}{k!2^k}$ from the Taylor series of $e^{t^2/2}$.

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
