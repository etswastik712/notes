---
title: Demographic Genetic and Environmental Stochasticity
aliases: ["demographic stochasticity", "environmental stochasticity", "genetic stochasticity", "stochastic extinction"]
subject: eco-evo
type: concept
scope: [taught, extra-beyond]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/beyond, src/slides, status/draft]
---
# Demographic Genetic and Environmental Stochasticity

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the three kinds of stochasticity and why small populations are more vulnerable ([[07_Conservation Biology.pdf#page=15|slide 15]])  ·  🔵 **extra · beyond:** scaling arguments for each kind of noise

> [!intuition] In one picture
> Chance matters more when numbers are small: a few unlucky births or deaths can wipe out a handful of animals, but not a million.

> [!key] Definition
> Small populations face extinction risk from three kinds of randomness: **demographic** (random variation in births, deaths, sex ratio), **genetic** (genetic drift leading to inbreeding depression and loss of heterozygosity), and **environmental** (random year-to-year variation and catastrophes). Demographic noise in the per capita rate scales like $1/\sqrt N$ and so matters at small $N$; environmental noise acts on all individuals alike and does not fade with $N$.

## Scaling and persistence times
**Demographic** noise: individual births and deaths are random events; the variance in total change is proportional to $N$, so *relative* noise is $\propto1/\sqrt N$ (32 % at $N=10$, 10 % at 100, 3 % at 1,000). **Environmental** noise: all individuals share good and bad years, so the variance of the *per-capita* rate does not shrink with $N$. **Catastrophes** are rare large environmental events. **Genetic** stochasticity is drift and inbreeding ([[Genetic Drift and Inbreeding Depression]]).

> [!example] Extinction risk from demographic noise
> Linear birth-death, $b=1.1$, $d=1.0$: $P_{ext}=(d/b)^{N_0}$: 0.91 (1 founder), 0.39 (10), 0.0085 (50). With births capped at $K$ and $b/d=1.2$, the mean time to extinction is 17, 72, 294, 1,299 and 6,193 time units for $K=10,20,30,40,50$: **exponential in $K$**. If the time to extinction is roughly exponentially distributed, the probability of extinction within $t=100$ is $1-e^{-100/T}$: 0.75 for $K=20$ ($T=72$) but 0.074 for $K=40$ ($T=1{,}299$).
> **Environmental noise** (🔵) changes the scaling: the mean persistence time then grows only as a *power* of $K$ (when growth is positive), so a large population remains vulnerable to a run of bad years that no population size averages away (Lande 1993). Catastrophes put a ceiling on persistence however large the population.

> [!pitfall] Which stochasticity matters depends on size
> Small populations: demographic and genetic effects dominate and interact (an **extinction vortex**: fewer animals, more inbreeding, lower fitness, fewer animals). Large populations: environmental noise and catastrophes dominate. Estimating all three for a real species is the job of population viability analysis ([[Minimum Viable Population]]). Slide 15 lists the three; the Allee effect ([[Allee Effect]]) is a deterministic threshold on top.

Used in: [[EE07 Conservation Biology]]. Related: [[Minimum Viable Population]] · [[Genetic Drift and Inbreeding Depression]] · [[Allee Effect]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
