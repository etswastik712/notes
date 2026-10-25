---
title: Lattice Effect
aliases: ["integerisation", "integerization", "indivisibility of organisms"]
subject: eco-evo
type: concept
scope: [taught, extra-book]
by: [slides, henson, dey-joshi]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/book, src/slides, src/paper, status/draft]
---
# Lattice Effect

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** Henson et al. (2001) and the slide 'Why does integerisation kill chaos?' ([[04_PopDyn_Chaos_18Aug_2026.pdf#page=32|slide 32]])  ·  🟡 **extra · book:** Dey and Joshi, 'Chaos in ecological systems: fact or artifact?' (detailed reading)

> [!intuition] In one picture
> You cannot have 3.7 wolves. Force a chaotic map onto whole numbers and only finitely many states exist, so the trajectory must eventually repeat itself.

> [!key] Definition
> If a deterministic map is bounded above and restricted to integer values, its state set is finite, so any trajectory must revisit a state and is then periodic (pigeonhole principle). **Chaos is replaced by limit cycles (possibly of long period) or extinction.** The lattice effect explains the lack of deterministic chaos in real populations; it does *not* exclude long-period cycles (slide).

## The argument and the numbers
Let $g$ map the integers $\{0,\dots,M\}$ into themselves (population bounded above and rounded). A deterministic trajectory on a finite set must revisit a state; from then on it repeats: **eventually periodic**. A series that never repeats (chaos) needs infinitely many states. Rounding therefore converts chaos into a limit cycle (or to 0, extinction).

> [!example] Integerised Ricker (computed)
> $K=100$, $r=3.0$, start 30: the population never exceeds 245 (at most 246 states), and the series locks onto a **10-cycle after a 21-step transient**. Cycle lengths (300 random starts): $K=100$: 14 at $r=2.8$, 10 at $r=3.0$; $K=1000$: 36 and 25 to 36; $K=10{,}000$: 82 and 155. So **cycle length grows with $K$**: for large populations the cycle is longer than any data set and is indistinguishable from chaos. At $r=3.3$ the real-valued orbit dips to 0.75, which rounds to 1; had it fallen below 0.5 the integer population would be extinct.

> [!pitfall] A statement about models
> The slide: the lattice effect "can only explain why *deterministic chaos* cannot be observed in biological systems; it does not exclude limit cycles with long periodicities". Also real populations have demographic noise ([[Demographic Genetic and Environmental Stochasticity]]) which is not captured by a deterministic rounding rule: stochastic integer models are a different object. The point is an *encoding error* ([[Modelling Relation]]): $N$ is not a real number.

Source: Henson et al., *Science*, 19 Oct 2001 (slide 32); Dey and Joshi (detailed reading, not in the folder). Related: [[Deterministic Chaos]], [[Hassell Model]].

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Deterministic Chaos]] · [[Hassell Model]] · [[Modelling Relation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
