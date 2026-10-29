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

Used in: [[PR04 Joint Distributions Expectation and Variance]], [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[08-Probability/Concepts/Variance|Variance]] · [[Skewness and Kurtosis]] · [[Moment Generating Function]] · [[Factorial Moments]].

## Added with the Week 2 and Week 3 lectures
Lecture (Week 3): $E[X^0]=1$, $E[X^1]=\mu$, $E[X^2]=\sigma^2+\mu^2$; uniform $E[X^m]=\frac{b^{m+1}-a^{m+1}}{(m+1)(b-a)}$; exponential $n!/\lambda^n$; $N(0,1)$ even moments $\frac{(2k)!}{k!2^k}$; Bernoulli $E[X^n]=p$. Moments from the MGF's Taylor series: [[Exponential Generating Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
