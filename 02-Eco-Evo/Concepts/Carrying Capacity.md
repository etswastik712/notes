---
title: Carrying Capacity
aliases: ["K"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Carrying Capacity

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** $K$ as the population size at which $n_{t+1}=n_t$ in the Ricker model, and the statement that it does not change the qualitative dynamics ([[04_PopDyn_Chaos_18Aug_2026.pdf#page=24|slide 24]])

> [!intuition] In one picture
> The size at which the environment can just support a population: births exactly balance deaths.

> [!key] Definition
> **Carrying capacity** $K$ is the population size at which the realised growth rate is zero. It is a property of the environment *and* of the model, not a universal constant. In the [[Ricker Model]] it fixes the equilibrium but, unlike $r$, not the qualitative behaviour.

## Meaning, and where $K$ comes from
$K$ is the density at which realised growth is zero; it is *not* a constant of nature. It is set by the resource supply and by how much each individual needs. In the consumer-resource model of [[EE04 Competition and Invasions]] the equilibrium is $N^*=y\,(R_{in}-R^*)$: yield $y$ times (supply minus the break-even level $R^*$), so $K$ rises with supply and falls as $R^*$ rises. For the chemostat toy of that chapter, $N^*_B=10-0.5=9.5$.

> [!example] Same $K$, different dynamics
> The Ricker model with $K=100$ and $K=1000$ and the same $r=2.6$ both give a 4-cycle; only the scale of the numbers differs (152, 39, 190, 18 for $K=100$). $r$ sets whether the equilibrium is stable; $K$ only rescales. In the Lotka-Volterra competition model $K_i$ is the single-species equilibrium of species $i$, and the outcome depends on $K_i$ *and* the competition coefficients: the larger $K$ does not guarantee victory (Park's *Tribolium*, [[Niche Partitioning]]).

**Measured values.** Wildebeest are regulated near 1.2 million ([[Serengeti Wildebeest Migration]]). A lake's $K$ for algae is a function of phosphorus loading ([[Nutrient Limitation]]).

> [!pitfall] "The" carrying capacity of a species
> There is none without saying *where and when*: $K$ varies with weather, habitat and human action, and populations may sit below it (predation, harvest) or overshoot it. The idea of "the carrying capacity of the Earth for people" is a different, normative question.

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Logistic Growth]] · [[Ricker Model]] · [[Density Dependence]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
