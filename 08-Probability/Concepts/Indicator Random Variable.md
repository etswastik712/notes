---
title: Indicator Random Variable
aliases: ["indicator", "indicator function"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Indicator Random Variable

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=24|class notes 2 Sep]].

> [!intuition] In one picture
> A 0–1 counter that fires when an event happens; adding indicators counts events.

> [!key] Definition
> $\mathbf 1_A=1$ if $A$ occurs, else 0. It is Bernoulli$(P[A])$ and $E[\mathbf 1_A]=P[A]$.

## Counting by indicators
$X=\sum_i\mathbf 1_{A_i}\Rightarrow E[X]=\sum_iP[A_i]$, even if the $A_i$ are dependent. Binomial: $np$. Hypergeometric: $n\frac w{w+b}$. Fixed points of a permutation: $n\cdot\frac1n=1$. Distinct coupon types after $n$ draws: $N[1-(1-\frac1N)^n]$.

Also $\mathbf 1_A^2=\mathbf 1_A$, so $\mathrm{Var}[\mathbf 1_A]=P[A](1-P[A])$.

Used in: [[PR03 Discrete Random Variables and Distributions]], [[PR04 Joint Distributions Expectation and Variance]]. Related: [[Linearity of Expectation]] · [[Bernoulli Distribution]] · [[Binomial Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
