---
title: Variance
aliases: ["standard deviation", "second central moment"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Variance

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=27|class notes 9 Sep]], [[ilovepdf_merged-1.pdf#page=29|10 Sep]].

> [!intuition] In one picture
> The average squared distance from the mean: how spread out the distribution is.

> [!key] Definition
> $\mathrm{Var}[X]=E[(X-\mu)^2]=E[X^2]-(E[X])^2$; $\sigma=\sqrt{\mathrm{Var}}$; $\mathrm{Var}[aX+b]=a^2\mathrm{Var}[X]$.

## Shortcut and scaling
$E[(X-\mu)^2]=E[X^2]-2\mu^2+\mu^2$. A shift leaves the spread unchanged; a scale $a$ multiplies it by $a^2$.

## Table
Bernoulli $pq$; Binomial $npq$; Poisson $\lambda$; Geometric $q/p^2$; NegBin $kq/p^2$; die $\frac{35}{12}$; $U(a,b)$ $\frac{(b-a)^2}{12}$; Rayleigh $2-\frac\pi2$; $N(\mu,\sigma^2)$ $\sigma^2$; Exp$(\lambda)$ $\frac1{\lambda^2}$.

> [!pitfall] Variance of a sum
> Independence is not needed for the mean of a sum but is for the variance (the instructor's sheet notes this is not proved in class).

Used in: [[PR04 Joint Distributions Expectation and Variance]], [[PR05 Continuous Random Variables]]. Related: [[Expectation]] · [[Moments of a Random Variable]] · [[Factorial Moments]] · [[Covariance and Correlation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
