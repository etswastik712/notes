---
title: Expectation
aliases: ["expected value", "mean", "first moment"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Expectation

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=19|class notes 20 Aug]], [[ilovepdf_merged-1.pdf#page=28|10 Sep]].

> [!intuition] In one picture
> The probability-weighted average of the values: the balance point of the distribution.

> [!key] Definition
> Discrete: $E[X]=\sum_xx\,p(x)$; continuous: $E[X]=\int x\,f(x)\,\mathrm dx$ (absolutely convergent). $E[aX+b]=aE[X]+b$; $E[g(X)]=\sum g(x)p(x)$ or $\int g\,f$ ([[Law of the Unconscious Statistician]]).

## Examples
Fair die $\tfrac72$; Bernoulli$(p)$ $p$; Binomial $np$; Geometric $\frac1p$; Poisson $\lambda$; $U(a,b)$ $\frac{a+b}2$; Rayleigh $\sqrt{\pi/2}$. For the 120 students on three buses of 36, 40, 44, a random student's bus has mean size $\frac{36^2+40^2+44^2}{120}=40.27>40$ ([[Size-Biased Sampling]]).

> [!pitfall] $E[g(X)]\ne g(E[X])$
> For a die, $E[X^2]=\tfrac{91}6=15.17$ but $(E[X])^2=12.25$. Equality only for linear $g$.

> [!pitfall] It may not exist
> The Cauchy distribution has $E|X|=\infty$ ([[Cauchy Distribution]]).

Used in: [[PR03 Discrete Random Variables and Distributions]], [[PR04 Joint Distributions Expectation and Variance]], [[PR05 Continuous Random Variables]]. Related: [[Linearity of Expectation]] · [[08-Probability/Concepts/Variance|Variance]] · [[Moments of a Random Variable]] · [[Law of the Unconscious Statistician]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
