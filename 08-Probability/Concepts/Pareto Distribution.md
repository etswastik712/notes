---
title: Pareto Distribution
aliases: ["power-law distribution", "Pareto"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Pareto Distribution

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (as a homework problem):** Homework 3 Q2 ([[Week3_notes.pdf#page=6|Week 3, p.6]]): median and mode. · 🔵 **extra · beyond:** moments, the exponential link.

> [!intuition] In one picture
> A heavy power-law tail: huge values are rare but not exponentially rare.

> [!key] Definition
> $f(x)=\dfrac a{x^{a+1}}$ ($x\ge1$), $F(x)=1-x^{-a}$; median $2^{1/a}$; mode $1$; $E[X^k]=\dfrac a{a-k}$ iff $k<a$.

## Facts (checked)
Median: $1-x^{-a}=\tfrac12\Rightarrow2^{1/a}$ ($1.4142$ for $a=2$, $2$ for $a=1$); mode $1$ (the density is strictly decreasing, maximal at the boundary). Mean $\frac a{a-1}$ for $a>1$ ($2$ for $a=2$), **infinite for $a\le1$**; variance finite only for $a>2$. If $Y\sim\mathrm{Expo}(a)$ then $X=e^Y$ is Pareto$(a)$ because $P[X>x]=P[Y>\ln x]=x^{-a}$: a Pareto is the exponential of an exponential. Scale-free: $P[X>2x\mid X>x]=2^{-a}$ for every $x$ (compare the **memoryless** exponential, $P[Y>t+s\mid Y>s]$ independent of $s$).

> [!pitfall] No mean, no CLT
> For $a\le2$ the variance is infinite and the CLT fails for sums of Paretos ([[PR06 Moments Generating Functions and Limit Theorems]] §5).

Used in: [[PR06 Moments Generating Functions and Limit Theorems]] §3.3. Related: [[Median and Mode]] · [[Exponential Distribution]] · [[Memoryless Property]] · [[Cauchy Distribution]] · [[Moments of a Random Variable]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
