---
title: Ricker Model
aliases: ["Ricker map", "Ricker equation"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Ricker Model

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the model, the roles of $r$ and $K$, and the four panels $r=1.3,\ 2.3,\ 2.5,\ 3.3$ ([[04_PopDyn_Chaos_18Aug_2026.pdf#page=24|slide 24]], [[04_PopDyn_Chaos_18Aug_2026.pdf#page=25|slide 25]])

> [!intuition] In one picture
> Each generation the population is multiplied by a growth factor $e^{r(1-n/K)}$ that is large when $n$ is small and falls below 1 when $n$ exceeds $K$. A strong overshoot can then crash it far below $K$.

> [!key] Definition
> $$n_{t+1}=n_t\exp\!\Big[r\Big(1-\frac{n_t}{K}\Big)\Big].$$ Fixed points $0$ and $K$; at $K$ the slope of the map is $1-r$, so $K$ is stable for $0<r<2$. $r$ sets the qualitative behaviour (stable point, 2-cycle, 4-cycle, …, chaos); $K$ only rescales. The map stays positive.

> [!verify] Check
> The slide labels its $r=2.5$ panel a '4-point limit cycle'. Numerically the Ricker map has period 2 at $r=2.5$ (the second doubling is at $r=2.5265$, the 4-cycle exists for $2.5265<r<2.6564$; `scripts/ee03_numbers.py`). The slide's own bifurcation diagram puts the second split above 2.5. Likely a plotting value slip; check with the instructor.

## Origin, stability, and cycles in numbers
Ricker (1954) introduced $n_{t+1}=n_t\exp[r(1-n_t/K)]$ for fish stock and recruitment; it follows from *log-linear* density dependence, $\ln(n_{t+1}/n_t)=r(1-n_t/K)$, and is positive for all $n>0$ (unlike the discrete logistic). The slope at $K$ is $1-r$: monotone return for $0<r<1$, damped oscillation for $1<r<2$, then instability.

> [!example] Attractors at $K=100$ (computed)
> $r=1.3$: $n_1=56.6,\ n_2=99.5,\ 100.1,\ 100.0$ (damped, multiplier $-0.3$). $r=2.3$: 2-cycle $159.22\leftrightarrow40.78$. $r=2.6$: 4-cycle $152.3,\ 39.1,\ 190.5,\ 18.1$. $r=3.3$: chaos, values from 0.75 to 280. Thresholds: $r=2,\ 2.5265,\ 2.6564,\ 2.6846$, chaos from $r_\infty=2.6924$ (May's Table 4). Lyapunov exponent: $-1.20$ at $r=1.3$, $+0.39$ at $r=3$.

> [!pitfall] The slide's $r=2.5$ panel
> At $r=2.5$ the map has period 2; the 4-cycle needs $r>2.5265$. The slide's "4-point" caption for $r=2.5$ should be read as $r\approx2.6$.

The Ricker model is the $\beta\to\infty$ limit of the [[Hassell Model]]. With a stochastic or integer-valued population, even $r$ below $r_\infty$ can produce extinction when a trough dips to a few animals ($r=3.3$ reaches 0.75): see [[Lattice Effect]].

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Period Doubling and Route to Chaos]] · [[Cobweb Diagram]] · [[Logistic Growth]] · [[Carrying Capacity]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
