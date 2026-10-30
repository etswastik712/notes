---
title: Sum of Independent Random Variables
aliases: ["convolution of densities", "distribution of X+Y", "sums of independent variables"]
subject: probability
type: concept
scope: [taught, extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/book, src/lecture-notes, status/draft]
---
# Sum of Independent Random Variables

<span class="scope-taught">taught</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the formula $f_{X+Y}(z)=\int f_X(x)f_Y(z-x)\mathrm dx$ is quoted on [[hw4.pdf#page=1|Homework 4]]; the MGF route is PR06. 🟡 the derivation from the cdf (Ross §6.3).

> [!intuition] In one picture
> To reach $z$ the first variable must be $x$ and the second exactly $z-x$: add up all the ways, each weighted by its likelihood.

> [!key] Key facts
> Independent $X,Y$: $f_{X+Y}=f_X*f_Y$ (continuous), $p_{X+Y}(s)=\sum_kp_X(k)p_Y(s-k)$ (discrete), $M_{X+Y}=M_XM_Y$. Means and variances add. Closed families: normal, Poisson, Gamma with a common rate, Cauchy (scales add).

Expo(1)+Expo(1) = Gamma(2,1), density $ze^{-z}$; $U(0,1)+U(0,1)$ = triangle on $[0,2]$; two dice give $c_s/36$ with $c_s=1,\dots,6,\dots,1$.

> [!pitfall] Watch out
> The density of a sum is not $f_X+f_Y$; it needs independence; the limits of integration are the region where both densities are positive.

Used in: [[PR07 Sums of Independent Variables Covariance and Correlation]], [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Convolution]] · [[Convolution Theorem]] · [[Moment Generating Function]] · [[Normal Distribution]] · [[Central Limit Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
