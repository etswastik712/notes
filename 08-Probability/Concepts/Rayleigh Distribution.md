---
title: Rayleigh Distribution
aliases: ["Rayleigh"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Rayleigh Distribution

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[week1_mt2113.pdf#page=4|week 1 p.4]], [[week1_mt2113.pdf#page=5|p.5]], homework [[week1_mt2113.pdf#page=1|Q1]].

> [!intuition] In one picture
> The length of a 2D Gaussian vector; arises when you take a distance in the plane.

> [!key] Definition
> $f(x)=xe^{-x^2/2}$, $F(x)=1-e^{-x^2/2}$ ($x\ge0$); $E[X]=\sqrt{\pi/2}=1.2533$, $E[X^2]=2$, $\mathrm{Var}=2-\frac\pi2=0.4292$; quartiles $0.7585,1.1774,1.6651$.

## Mean by parts
$E[X]=\int_0^\infty x\cdot xe^{-x^2/2}dx=\big[-xe^{-x^2/2}\big]+\int_0^\infty e^{-x^2/2}dx=\frac12\sqrt{2\pi}$.

$P[1<X<3]=e^{-1/2}-e^{-9/2}=0.5954$. Quantiles: $q_i=\sqrt{-2\ln(1-\frac i4)}$. If $R$ is Rayleigh then $R^2/2\sim$ Exp$(1)$ and $\int_0^\infty x^2e^{-x^2/2}dx=\frac12\sqrt{2\pi}$ also gives $E[Z^2]=1$.

Used in: [[PR05 Continuous Random Variables]]. Related: [[Normal Distribution]] · [[Exponential Distribution]] · [[Cumulative Distribution Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Maxwell-Boltzmann Distribution]] (Thermodynamics): the Maxwell speed density $ax^2e^{-bx^2}$ is the 3-D relative of the Rayleigh density $xe^{-x^2/2\sigma^2}$ of the 2-D speed of Gaussian components; both normalise by $\int x^ke^{-x^2}\mathrm dx$ (Quiz 1, Q3).
