---
title: Geometric Distribution
aliases: ["geometric", "waiting time for the first success"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Geometric Distribution

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=22|class notes 27 Aug]], [[ilovepdf_merged-1.pdf#page=25|2 Sep]].

> [!intuition] In one picture
> How long you wait for the first success when trials are independent.

> [!key] Definition
> $P[X=n]=(1-p)^{n-1}p$, $n\ge1$ (trials up to and including the first success). $E[X]=\frac1p$, $\mathrm{Var}[X]=\frac{1-p}{p^2}$, MGF $\frac{pe^t}{1-(1-p)e^t}$.

## Mean by first step
$E[X]=p\cdot1+q(1+E[X])\Rightarrow E[X]=1/p$. Series: $\sum nq^{n-1}p=p/(1-q)^2$.

## Tail and memorylessness
$P[X>n]=q^n$, $P[X>m+n\mid X>m]=q^n$: [[Memoryless Property]]. $P[X\ge n]$ summed over $n$ also gives $\frac1p$.

> [!example] Numbers
> $p=0.25$: mean 4, variance 12; $p=0.2$: mean 5, variance 20, $P[X>5]=0.8^5=0.328$.

Used in: [[PR03 Discrete Random Variables and Distributions]], [[PR04 Joint Distributions Expectation and Variance]]. Related: [[Negative Binomial Distribution]] · [[Memoryless Property]] · [[Exponential Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
