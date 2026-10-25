---
title: Coupon Collector Problem
aliases: ["coupon collector"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Coupon Collector Problem

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Practice problems 28th August and following weekend.pdf#page=1|sheet 28 Aug, problem 3]], [[Practice problems 4th September 2026.pdf#page=1|sheet 4 Sep, problem 1]].

> [!intuition] In one picture
> How many draws until you have seen every type? The last few types are the slow ones.

> [!key] Definition
> $N$ equally likely types, $T$ = draws to collect all: $E[T]=N\sum_{i=1}^N\frac1i=NH_N\approx N(\ln N+\gamma)$; expected distinct types after $n$ draws: $N[1-(1-\frac1N)^n]$.

## Mean by linearity
Once $i-1$ types are held, the wait for a new one is Geometric$(\frac{N-i+1}N)$ with mean $\frac N{N-i+1}$; sum over $i$.

## Pmf by inclusion-exclusion
$P[T>n]=\sum_{i=1}^N(-1)^{i+1}\binom Ni(1-\frac iN)^n$. $N=3$: $P[T=3]=\frac6{27}$ and $E[T]=5.5$.

> [!example] Numbers
> $N=6$: $14.70$ (simulation $14.68$); $N=10$: $29.29$; $N=50$: $224.96$. Ten types, 20 draws: $8.78$ distinct on average.

Used in: [[PR03 Discrete Random Variables and Distributions]], [[PR04 Joint Distributions Expectation and Variance]]. Related: [[Linearity of Expectation]] · [[Inclusion-Exclusion Principle]] · [[Geometric Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
