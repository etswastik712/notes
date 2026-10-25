---
title: Hassell Model
aliases: ["Hassell map"]
subject: eco-evo
type: concept
scope: [taught, extra-book]
by: [slides, hassell]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/book, src/slides, src/paper, status/draft]
---
# Hassell Model

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the model and the result: 22 of 24 insect populations showed monotonic damping (Hassell, Lawton and May 1976) ([[04_PopDyn_Chaos_18Aug_2026.pdf#page=28|slide 28]])

> [!intuition] In one picture
> A flexible curve for density dependence with two knobs, so it can be fitted to real data to see whether real populations cycle or settle.

> [!key] Definition
> $$N_{t+1}=\lambda N_t\,(1+aN_t)^{-\beta}.$$ $\lambda$ is the growth parameter; $a,\beta$ set the density-dependent feedback ($\beta=1$ is the Beverton-Holt form). Equilibrium $N^*=(\lambda^{1/\beta}-1)/a$; slope there $f'(N^*)=1-\beta(1-\lambda^{-1/\beta})$.

## Properties and limits
$N_{t+1}=\lambda N_t(1+aN_t)^{-\beta}$. Fixed point $1+aN^*=\lambda^{1/\beta}$, $N^*=(\lambda^{1/\beta}-1)/a$; slope $f'(N^*)=1-\beta\,(1-\lambda^{-1/\beta})$. Special cases: $\beta=1$ is **Beverton-Holt** (never oscillates); letting $\beta\to\infty$ with $a\beta=c$ fixed gives $(1+cN/\beta)^{-\beta}\to e^{-cN}$, the **Ricker** model. So $\beta$ is a knob for *how abruptly* density dependence bites ("scramble" for large $\beta$, "contest" for small).

> [!example] Stability map (computed)
> Monotone damping needs $\beta(1-\lambda^{-1/\beta})\le1$; instability needs $\ge2$. $\lambda=10,\ \beta=3$: $f'=1-3(1-10^{-1/3})=-0.61$: oscillatory damping. Instability sets in at $\lambda=27$ for $\beta=3$, at $\lambda=11.4$ for $\beta=6$ and at 9.3 for $\beta=10$; for $\beta\le2$ never. For $\beta=6$ the monotone-to-oscillatory boundary is at $\lambda=2.99$.
> **Data.** Hassell, Lawton and May (1976) placed 24 insect populations on this plane: 22 showed monotonic damping, one damped oscillation, one a limit cycle, none chaos (slide 29).

> [!pitfall] Reading the puzzle correctly
> Most populations sit in the monotone region of the plane *under a one-lag model*. That does not show the real dynamics are simple: Turchin and Taylor refitted with delayed density dependence and found the whole spectrum ([[Time-Series Reconstruction]]); and integer numbers rule out strict chaos anyway ([[Lattice Effect]]).

Model choice among forms like this one is a job for [[Akaike Information Criterion]]; the form is an [[Modelling Relation]] encoding step.

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Ricker Model]] · [[Lattice Effect]] · [[Time-Series Reconstruction]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
