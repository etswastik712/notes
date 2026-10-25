---
title: Cumulative Distribution Function
aliases: ["cdf", "distribution function"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Cumulative Distribution Function

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=18|class notes 20 Aug]], [[ilovepdf_merged-1.pdf#page=28|10 Sep]].

> [!intuition] In one picture
> $F(x)$ is the running total of probability up to $x$: it starts at 0, only increases and ends at 1.

> [!key] Definition
> $F(x)=P[X\le x]$, defined for **every** random variable. Properties: (1) increasing; (2) right-continuous; (3) $F(-\infty)=0$, $F(\infty)=1$. Also $P[a<X\le b]=F(b)-F(a)$ and $P[X=a]=F(a)-F(a^-)$.

## Why right-continuous
If $x_n\downarrow a$ then $\{X\le x_n\}$ decreases to $\{X\le a\}$ and probability is continuous along decreasing sequences ([[Continuity of Probability]]; the proof is not examined). The left limit is $P[X<x]$, so a jump is a point mass.

## Two shapes
Discrete: a step function. Continuous: a continuous function with $F'=f$. To find a distribution, find $F$ first (the event $\{g(X)\le y\}$ is easier to handle), then differentiate if continuous ([[Cdf Method for Transformations]]).

Used in: [[PR03 Discrete Random Variables and Distributions]], [[PR05 Continuous Random Variables]]. Related: [[Probability Mass Function]] · [[Probability Density Function]] · [[Continuity of Probability]] · [[Cdf Method for Transformations]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
