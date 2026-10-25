---
title: Competition
aliases: ["intraspecific competition", "interspecific competition"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Competition

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the definition, intra- versus interspecific competition, and the features of interspecific competition ([[04-Competition_25-Aug_2026.pdf#page=3|slide 3]])

> [!intuition] In one picture
> Two users of the same limited thing: whatever one takes, the other cannot have.

> [!key] Definition
> **Competition** is any use or defence of a resource by one individual that reduces its availability to others. **Intraspecific** (same species): density-dependent growth, competition for mates. **Interspecific** (different species): a *non-trophic* interaction (neither eats the other) that lowers the growth rate or equilibrium size of at least one population. If the species do not affect each other there is no competition (slide).

## How competition enters a growth equation
Intraspecific competition is already in the logistic: growth of species 1 is $\dot N_1=r_1N_1(1-N_1/K_1)$, and each conspecific subtracts $1/K_1$ from the per-capita factor. Interspecific competition adds a second term, $-\alpha_{12}N_2/K_1$: individuals of species 2 count as $\alpha_{12}$ conspecifics ([[Lotka-Volterra Competition Model]]).

> [!example] How much does a competitor cost?
> $K_1=100$, $N_1=50$. Without species 2 the per-capita growth factor is $(100-50)/100=0.50$. With $N_2=40$ and $\alpha_{12}=0.5$ it is $(100-50-20)/100=0.30$: the competitor removes 40 % of the species' growth, as if the other species were 20 extra individuals of its own. Slide 6's criterion is exactly this: the growth rate (or equilibrium) of at least one species is reduced.

**Kinds.** *Exploitation* (using up the resource: the $R^*$ picture, [[Tilman R-Star Rule]]) and *interference* (blocking access: territories, aggression, allelopathy). Intraspecific: density-dependent growth and competition for mates (slide 5's video of antelope males). Molles §13.1 adds intraspecific competition in crowded plant stands (self-thinning).

> [!pitfall] Two things that are not competition
> Eating is a *trophic* interaction (predation, [[EE05 Predation]]). Two species that suppress each other through a shared predator ("apparent competition") do not compete for a resource, though the signs of the effects look the same. Competition needs a *limiting, shared* resource: if the species do not affect each other there is none (slide 6).

The consequences for communities are the subject of [[Competitive Exclusion Principle]] and [[Niche Partitioning]].

Used in: [[EE04 Competition and Invasions]]. Related: [[Competitive Exclusion Principle]] · [[Lotka-Volterra Competition Model]] · [[Density Dependence]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
