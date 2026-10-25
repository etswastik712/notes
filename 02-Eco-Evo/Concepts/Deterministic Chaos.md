---
title: Deterministic Chaos
aliases: ["chaos", "sensitive dependence on initial conditions", "SDIC"]
subject: eco-evo
type: concept
scope: [taught, extra-book]
by: [slides, may]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/book, src/slides, src/paper, status/draft]
---
# Deterministic Chaos

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** chaos as one outcome of simple density-dependent maps; the slides' 'does chaos exist in nature?' puzzle ([[04_PopDyn_Chaos_18Aug_2026.pdf#page=3|slide 3]])  ·  🟡 **extra · book:** May (1976); Crichton's *Jurassic Park* extracts on SDIC and fractals (fun, non-technical)

> [!intuition] In one picture
> A rule with no randomness can still be unpredictable in practice: any tiny error in the starting value doubles again and again until the forecast is worthless.

> [!key] Definition
> **Deterministic chaos** is bounded, aperiodic behaviour of a deterministic system with **sensitive dependence on initial conditions (SDIC)**: two nearby trajectories separate roughly as $e^{\Lambda t}$ with Lyapunov exponent $\Lambda>0$. The system has no noise; the unpredictability is the system's own.

## Lyapunov exponent and forecast horizon
Two orbits starting $\delta_0$ apart separate as $\delta_t\approx\delta_0e^{\Lambda t}$; $\Lambda=\lim\frac1T\sum\ln|g'(n_t)|$. Ricker, $K=100$: $\Lambda=-1.20,\ -0.90,\ -0.58$ at $r=1.3,\ 2.3,\ 2.6$ (stable point or cycles); $+0.39$ at $r=3.0$; $+0.42$ at $r=3.3$; $-0.07$ at $r=3.6$ (a window). A forecast loses its value when the error reaches the size of the attractor, after $t^*\approx\ln(\Delta/\delta_0)/\Lambda$.

> [!example] How long can you forecast?
> $r=3$, $\Delta=100$, $\delta_0=10^{-6}$: $t^*=\ln10^{8}/0.39=47$ generations. Reduce the measurement error by a factor of 1000 and you gain $\ln1000/0.39=18$ generations. For a $10^{-4}$ error the horizon is 35 generations, and doubling it to 70 needs an error near $1.4\times10^{-10}$. Horizons grow only *logarithmically* with precision; that is the practical meaning of sensitive dependence, and the reason weather ([[CL01 Earth as a System]]) cannot be forecast beyond about two weeks.

> [!pitfall] What chaos is not
> Not noise (the rule is exact and reproducible), not instability (orbits are bounded), not unpredictability in *distribution* (statistics of the attractor are stable). In real data, chaos is hard to separate from noise on short, noisy series; and the lattice effect shows that integer populations cannot be strictly chaotic ([[Lattice Effect]]). The Jurassic Park extract gives the shells-and-weather illustration (non-examinable).

The route there: [[Period Doubling and Route to Chaos]].

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Period Doubling and Route to Chaos]] · [[Lattice Effect]] · [[Fractals]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
