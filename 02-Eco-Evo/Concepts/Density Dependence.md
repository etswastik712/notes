---
title: Density Dependence
aliases: ["density-dependent growth", "realised growth rate", "realized growth rate"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Density Dependence

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the realised growth rate as a function of $N$, and the slide's warning that it is often not linear ([[04_PopDyn_Chaos_18Aug_2026.pdf#page=17|slide 17]])

> [!intuition] In one picture
> Crowds slow people down. When a population is crowded each individual has less food, space or safety, so the average birth rate falls and the death rate rises.

> [!key] Definition
> A rate is **density dependent** if it changes with population size $N$. The **realised per capita growth rate** is $r'(N)=\frac1N\frac{dN}{dt}$ with $r'(0)=r$ (the intrinsic rate); negative density dependence ($r'$ decreasing in $N$) regulates a population. The logistic model assumes $r'(N)=r(1-N/K)$, a straight line.

## Forms and consequences
A rate is density dependent if it varies with $N$. Writing the realised per-capita rate as $r'(N)$, the common forms are: **linear** ($r(1-N/K)$, logistic); **log-linear** ($\ln(N_{t+1}/N_t)=r(1-N/K)$, Ricker); **power** ($\lambda(1+aN)^{-\beta}$, Hassell); **theta-logistic** $r[1-(N/K)^\theta]$; and, at *low* density, **Allee** forms in which $r'$ rises with $N$ ([[Allee Effect]]).

> [!example] Compensation classes
> Look at the next-generation map $g(N)$ around $K$. If $g'(K)>0$ the response is **under-compensating** (monotone return); $g'(K)=0$ is exact compensation; $-1<g'(K)<0$ over-compensating but stable (damped oscillation); $g'(K)<-1$ unstable cycles and chaos. For the Ricker model $g'(K)=1-r$: 0.7 at $r=0.3$ (under), 0 at $r=1$ (exact), $-0.3$ at $r=1.3$ (damped), $-1.3$ at $r=2.3$ (2-cycle). The Hassell model has $g'(K)=1-\beta(1-\lambda^{-1/\beta})$: $\beta\le1$ is always under-compensating.

> [!pitfall] Regulation versus limitation
> A *limiting* factor sets the level of $N$; a *regulating* factor acts with strength rising with $N$ and so returns it to a level after a disturbance. Rain can limit a desert herbivore without regulating it. Also the sign matters: with a time lag ($\tau$ generations) the same negative feedback can overshoot ([[Logistic Growth]], delayed form).

Slide 23's hypothetical curve (fast fall of the realised rate from about 8 at low density to near zero by 600) shows that straight-line $r'(N)$ is a convenience. The choice of form is the [[Modelling Relation]]'s encoding step.

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Logistic Growth]] · [[Carrying Capacity]] · [[Allee Effect]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
