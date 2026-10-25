---
title: Gumbel Distribution
aliases: ["extreme value type I", "Gumbel", "distribution of the maximum"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Gumbel Distribution

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (as a homework problem):** Homework 2 Q2 ([[Week2_notes.pdf#page=5|Week 2, p.5]]): the cdf and the limit of $M_n-\ln n$. · 🔵 **extra · beyond:** mean, variance, return periods, the extreme-value theorem.

> [!intuition] In one picture
> The law of the largest of many exponential-tailed values, once you subtract $\ln n$: the shape of floods, record rainfalls and record highs.

> [!key] Definition
> $Y=-\ln X$, $X\sim\mathrm{Expo}(1)$: $F(y)=e^{-e^{-y}}$, $f(y)=e^{-y}e^{-e^{-y}}$. If $X_i$ are i.i.d. Expo$(1)$ and $M_n=\max X_i$: $P[M_n-\ln n\le y]=\big(1-\tfrac{e^{-y}}n\big)^n\to e^{-e^{-y}}$.

## Facts
Mode $0$, median $-\ln\ln2=0.3665$, mean $\gamma=0.5772$ (Euler), variance $\pi^2/6=1.6449$, skewness $1.1395$. Numbers at $y=0.5$: $0.393,0.485,0.524,0.540,0.5447$ for $n=1,2,5,20,200$, limit $0.5452$ (simulation of $10^6$: mean $0.5783$, variance $1.655$).

## Return levels (🔵)
The $T$-period level $y_T$ with $P[Y>y_T]=1/T$ is $y_T=-\ln\big(-\ln(1-1/T)\big)$: $4.600$ for $T=100$ (standard units). The block maximum of $n$ independent exponential-tailed values is $\approx\ln n+Y$: for 365 daily values the annual maximum sits near $\ln365=5.90$ plus a Gumbel fluctuation. The **Fisher–Tippett–Gnedenko** theorem (stated) says this is the limit for the maximum of any law with an exponential-type tail, including the normal; heavier (Pareto) tails give a different limit.
**Simulation:** $-\ln(-\ln U)$ with $U\sim U(0,1)$ is Gumbel ([[Probability Integral Transform]]).

> [!pitfall] Maximum, not sum
> The CLT governs sums; the Gumbel law governs maxima, and the normalisation is $-\ln n$ (a shift), not $\sqrt n$ (a scale).

Used in: [[PR05 Continuous Random Variables]] §4 (HW2 Q2). Related: [[Exponential Distribution]] · [[Probability Integral Transform]] · [[Cumulative Distribution Function]] · [[Median and Mode]] · [[Central Limit Theorem]] · [[Pareto Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
