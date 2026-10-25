---
title: Allee Effect
aliases: ["Allee effect", "depensation", "positive density dependence", "social facilitation"]
subject: eco-evo
type: concept
scope: [taught, extra-beyond]
by: [slides, own-notes]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/beyond, src/slides, src/own, status/draft]
---
# Allee Effect

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the slide's 'social facilitation in food finding' as a possible cause of the pigeon's collapse ([[07_Conservation Biology.pdf#page=12|slide 12]])  ·  🔵 **extra · beyond:** the strong Allee effect and its model

> [!intuition] In one picture
> Some species do worse when rare: it is harder to find mates, defend against predators or find food.

> [!key] Definition
> An **Allee effect** is positive density dependence at low density: per capita growth *increases* with $N$ for small $N$. A strong Allee effect has a threshold $A$ below which the population declines to extinction, e.g. $\dot N=rN\,(N/A-1)(1-N/K)$, which is bistable (0 and $K$ stable, $A$ unstable).

## The model, thresholds and a harvest fold
Per-capita growth with a strong Allee effect: $g(N)=r(N/A-1)(1-N/K)$, negative for $N<A$, positive for $A<N<K$, with equilibria $0$ (stable), $A$ (unstable) and $K$ (stable). A **weak** Allee effect has $g$ rising with $N$ at low density but positive throughout (slower, no threshold). Mechanisms: difficulty finding mates, cooperative defence or feeding, **social facilitation in food finding** (passenger pigeon), predator saturation, and conspecific-dependent habitat modification.

> [!example] Numbers ($r=0.5$, $A=20$, $K=100$)
> At $N=5$ the per-capita rate is $-0.356$ (the logistic with the same $r,K$ would give $+0.475$). Growth peaks at $f_{\max}=26.3$ at $N=70.6$ (logistic: $rK/4=12.5$). From $N=15$ the population dies out; from $N=30$ it grows to 100. With a constant harvest $H=20$ the equilibria move to **52.1 (unstable)** and **85.9 (stable)**: a bad year that takes the population below 52 means extinction although $A$ itself is 20; at $H\ge26.3$ the two merge (fold) and nothing remains. Harvest quotas set from the *average* yield ignore this ([[Bistability and Tipping Points]]).

> [!pitfall] Component versus demographic Allee effects
> A component Allee effect (e.g. mate finding) lowers one fitness component; it gives a *demographic* Allee effect (negative per-capita growth at low $N$) only if it outweighs the density-dependent gains. Not all small populations are Allee-limited; stochastic loss ($P_{ext}=(d/b)^{N_0}$) acts without it ([[Demographic Genetic and Environmental Stochasticity]]).

Related: [[Density Dependence]], [[Minimum Viable Population]], [[Passenger Pigeon Extinction]]; the shallow-lake fold has the same mathematics ([[Alternative Stable States]]).

Used in: [[EE07 Conservation Biology]]. Related: [[Density Dependence]] · [[Bistability and Tipping Points]] · [[Passenger Pigeon Extinction]] · [[Minimum Viable Population]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
