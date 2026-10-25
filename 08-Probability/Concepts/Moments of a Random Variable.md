---
title: Moments of a Random Variable
aliases: ["raw moments", "central moments"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Moments of a Random Variable

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=27|class notes 9 Sep]].

> [!intuition] In one picture
> $E[X^n]$ describes the shape: mean, spread, lopsidedness, tail weight.

> [!key] Definition
> $n$-th raw moment $E[X^n]$; $n$-th central moment $E[(X-E[X])^n]$ (binomial-expand to get it from raw moments).

$\mu_2=E[X^2]-\mu^2$, $\mu_3=E[X^3]-3\mu E[X^2]+2\mu^3$. If $E|X|^s<\infty$ then $E|X|^r<\infty$ for $r<s$. For $N(0,1)$ all odd moments vanish and $E[Z^{2k}]=\frac{(2k)!}{2^kk!}$; for Exp$(\lambda)$, $E[X^k]=k!/\lambda^k$; for the Poisson, $E[X^3]=\lambda^3+3\lambda^2+\lambda$.

Used in: [[PR04 Joint Distributions Expectation and Variance]], [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Variance]] · [[Skewness and Kurtosis]] · [[Moment Generating Function]] · [[Factorial Moments]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
