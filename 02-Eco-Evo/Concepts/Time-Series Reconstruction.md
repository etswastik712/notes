---
title: Time-Series Reconstruction
aliases: ["Turchin and Taylor", "complex dynamics in ecological time series"]
subject: eco-evo
type: concept
scope: [taught, extra-book]
by: [slides, turchin]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/book, src/slides, src/paper, status/draft]
---
# Time-Series Reconstruction

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the slide: fitting many models of varying lags and complexity finds all behaviours; overly simple models bias toward stability ([[04_PopDyn_Chaos_18Aug_2026.pdf#page=34|slide 34]])  ·  🟡 **extra · book:** Turchin and Taylor (1992), *Ecology* 73: 289-305; Ch. 7 of Turchin's book

> [!intuition] In one picture
> Look at a 3-D object only through its shadow and you may think it is simple. Fitting a one-lag model to a time series can make rich dynamics look like simple damping.

> [!key] Definition
> Hassell et al. fitted a single-lag model of fixed form. Turchin and Taylor (1992) fitted many models differing in the number of time lags and in complexity, and found damping, cycles *and* chaos. Their conclusion: 'use of overly simple models for reconstructing endogenous dynamics from data may be biased in favor of finding stability.'

## The method and what it found
Turchin and Taylor (1992) model the yearly change $R_t=\ln(N_t/N_{t-1})$ as a flexible polynomial **response surface** in the lagged densities $N_{t-1},N_{t-2}$ (**response-surface methodology**, with a Box-Cox-like transform to handle skewed counts), then classify the fitted dynamics by its dominant eigenvalue and Lyapunov exponent (exponential or oscillatory damping, limit cycle, quasiperiodicity, chaos), and test the periodic cases against the **autocorrelation function**. Series of at least 18 years, 14 insect and 22 vertebrate populations. Insects: 1 unregulated, 3 exponentially stable, 6 damped oscillations, 1 limit cycle, 2 quasiperiodic, 1 chaos; vertebrates similar, no chaos. Hassell et al. (one lag, fixed form): 22 of 24 monotone.

> [!example] Why one lag misleads (my construction)
> Take $N_{t+1}=N_t\exp[r(1-(N_t+bN_{t-1})/(K(1+b)))]$ with $r=1.6$, $b=3$, $K=100$: a two-lag system that cycles permanently. Regress $\ln(N_{t+1}/N_t)$ on $N_t$ alone: $R^2=0.30$ (the points trace a loop, not a line), fitted $\hat r=0.76$, and a one-lag Ricker with $\hat r=0.76$ would predict **monotone damping** ($1-\hat r=+0.24$). The one-lag shadow of a hidden-dimension system looks stable (slide 35's cube).

> [!pitfall] More lags is not free
> Higher-dimensional fits use more parameters from short, noisy series, so model choice must penalise complexity ([[Akaike Information Criterion]]); Turchin and Taylor's own caution is that the method is new and chaos is hardest to detect. The conclusion on the slide is about *bias*: overly simple models favour stability ([[Hassell Model]]).

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Hassell Model]] · [[Akaike Information Criterion]] · [[Lattice Effect]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
