---
title: Metapopulation
aliases: ["metapopulation dynamics", "Levins model"]
subject: eco-evo
type: concept
scope: [taught, extra-beyond]
by: [slides, levins]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/beyond, src/slides, src/paper, status/draft]
---
# Metapopulation

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the word and its role in Huffaker's result: extinction-recolonisation promotes prey survivorship ([[05_01_Sep_2026_Predation.pdf#page=13|slide 13]])  ·  🔵 **extra · beyond:** Levins' model $\dot p=cp(1-p)-ep$

> [!intuition] In one picture
> A 'population of populations': each patch can go extinct, but dispersal from other patches refills it.

> [!key] Definition
> A **metapopulation** is a set of local populations linked by dispersal. In Levins' model the fraction of occupied patches $p$ obeys $\dot p=cp(1-p)-ep$ (colonisation rate $c$, local extinction rate $e$) with equilibrium $p^*=1-e/c$, positive only if $c>e$.

## Levins' model and the extinction threshold
Let $p$ be the fraction of habitat patches occupied, $c$ the colonisation rate and $e$ the local extinction rate: $\dot p=cp(1-p)-ep$. This is a logistic equation with $r=c-e$ and "carrying capacity" $p^*=1-e/c$, positive only if $c>e$ (the metapopulation persists while each occupied patch produces on average more than one newly occupied patch).

> [!example] Habitat loss
> $c=0.3$, $e=0.1$: $p^*=0.67$. Destroy a fraction $D$ of the patches: $\dot p=cp(1-D-p)-ep$ gives $p^*=1-D-e/c=0.67-D$. The metapopulation dies out when $D>1-e/c=0.67$: occupancy falls to zero while one-third of the patches are still intact. The curve lags: even at $D=0.5$ the equilibrium is $p^*=0.17$, a fraction of what the remaining habitat could hold ("extinction debt" if the patches are already declining).

**Where it applies.** Huffaker's oranges (prey metapopulation), butterflies in meadows (Molles Concept 10.2), reserves linked by corridors ([[Reserve Design and Management]]), and the movement of seeds among habitat patches. The model assumes identical patches, no spatial structure of distances and instant recolonisation, all relaxed in spatially explicit versions.

> [!pitfall] Patch occupancy is not population size
> $p$ counts occupied patches, not individuals; a metapopulation can persist with each local population small and short-lived. Similar logic gives the *rescue effect* and the benefit of connectivity in [[EE07 Conservation Biology]]; compare the threshold form of [[Allee Effect]] and [[Minimum Viable Population]].

Used in: [[EE05 Predation]]. Related: [[Huffaker Mite Experiment]] · [[Logistic Growth]] · [[Reserve Design and Management]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
