---
title: Uniform Distribution
aliases: ["continuous uniform", "U(a,b)"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Uniform Distribution

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[week1_mt2113.pdf#page=3|week 1 p.3]], [[week1_mt2113.pdf#page=8|p.8]].

> [!intuition] In one picture
> A point dropped at random on an interval: probability proportional to length.

> [!key] Definition
> $f(x)=\frac1{b-a}$ on $[a,b]$, $F(x)=\frac{x-a}{b-a}$; $E[X]=\frac{a+b}2$, $\mathrm{Var}[X]=\frac{(b-a)^2}{12}$; MGF $\frac{e^{tb}-e^{ta}}{t(b-a)}$.

## Variance
$E[X^2]=\frac{a^2+ab+b^2}3$, minus $\frac{(a+b)^2}4$ gives $\frac{(b-a)^2}{12}$. $U(0,1)$: $\frac1{12}=0.0833$; $U(2,8)$: $E=5$, $\mathrm{Var}=3$.

## Used for
Random circle ($R\sim U(0,1)$, $A=\pi R^2$ has cdf $\sqrt{a/\pi}$); the broken stick ($E[X]=\frac12+p-p^2$, maximal $\frac34$ at $p=\frac12$); inverse-cdf sampling: if $U\sim U(0,1)$ then $-\ln U\sim$ Exp$(1)$.

Used in: [[PR05 Continuous Random Variables]]. Related: [[Discrete Uniform Distribution]] · [[Cdf Method for Transformations]] · [[Probability Density Function]].

## Added with the Week 2 and Week 3 lectures
Week 3: median $\frac{a+b}2$, **every** point is a mode, $E[X^m]=\frac{b^{m+1}-a^{m+1}}{(m+1)(b-a)}$, MGF $\frac{e^{tb}-e^{ta}}{t(b-a)}$ ($t\ne0$). Not memoryless. $F(X)\sim U(0,1)$ for any continuous $X$ ([[Probability Integral Transform]], [[Median and Mode]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
