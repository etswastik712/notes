---
title: Logistic Growth
aliases: ["Verhulst-Pearl model", "logistic equation", "S-shaped growth"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Logistic Growth

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the continuous logistic (Verhulst-Pearl) model, with the empirical checks on the USA census (Pearl and Reed 1920) and the rotifer *Brachionus plicatilis* (Yoshinaga et al. 2001) ([[04_PopDyn_Chaos_18Aug_2026.pdf#page=18|slide 18]])

> [!intuition] In one picture
> Growth starts exponential, then slows as the population fills its environment and levels off at $K$: an S-curve.

> [!key] Definition
> $$\frac{dN}{dt}=rN\Big(1-\frac NK\Big),\qquad N(t)=\frac{K}{1+\frac{K-N_0}{N_0}e^{-rt}}.$$ The inflection point is at $N=K/2$ (fastest growth). Fixed points: $N^*=0$ (unstable, slope $r$) and $N^*=K$ (stable, slope $-r$), see [[Fixed Points and Linear Stability]].

## Solution and properties
Separating variables with $\frac1{N(1-N/K)}=\frac1N+\frac{1/K}{1-N/K}$ gives $\ln\frac N{K-N}=rt+C$ and
$$N(t)=\frac K{1+\frac{K-N_0}{N_0}e^{-rt}}.$$
The growth curve is symmetric about $N=K/2$ (inflection, $\dot N_{\max}=rK/4$), the fixed points are $0$ (slope $r$, unstable) and $K$ (slope $-r$, stable) and the return time to $K$ is $1/r$ ([[Relaxation Time]]).

> [!example] $K=100$, $r=0.6$, $N_0=2$
> $K/2$ is reached at $t=\ln49/0.6=6.49$; $N(10)=100/(1+49e^{-6})=89.2$; peak growth $rK/4=15$ at $N=50$. **Harvest:** with a constant take $H$, $\dot N=rN(1-N/K)-H$ has equilibria while $H\le rK/4=15$; at $H=15$ they merge at $K/2$ and above that the population collapses. That $rK/4$ is the *maximum sustainable yield*, reached at half the carrying capacity, and a fold ([[Bistability and Tipping Points]]).

**Evidence (slide 22).** US census (Pearl and Reed 1920; later data lie above the fitted curve) and the rotifer *Brachionus plicatilis* (a plateau of about 1,500 with fluctuations).

> [!pitfall] Not a law
> $r$ and $K$ are fitted constants, $K$ moves with resources ([[Carrying Capacity]]) and the straight-line $r'(N)$ is an assumption. In discrete time the logistic family cycles and goes chaotic ([[Ricker Model]]); in continuous time it never oscillates unless a delay is added. The related four forms (slide 20): $\dot N=rN(1-N/K)$; $N_{t+1}=N_t[1+r(1-N_t/K)]$ (the logistic map with $a=1+r$); $N_{t+1}=rN_t(1-N_t/K)$; the Ricker form.

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Density Dependence]] · [[Carrying Capacity]] · [[Ricker Model]] · [[Fixed Points and Linear Stability]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Logistic Distribution]] (Probability): the solution $N(t)=K/(1+e^{-r(t-t_0)})$ of logistic growth is $K$ times the cdf of a logistic distribution with location $t_0$ and scale $1/r$, so growth quantiles are logistic quantiles.
