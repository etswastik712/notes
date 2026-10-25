---
title: Minimum Viable Population
aliases: ["MVP"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Minimum Viable Population

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the definition on the slide ([[07_Conservation Biology.pdf#page=15|slide 15]])

> [!intuition] In one picture
> How many animals are enough? Enough that, accounting for bad luck, the population has an acceptable chance of lasting for a stated time.

> [!key] Definition
> **Minimum viable population (MVP):** the minimum population size that will ensure, at some acceptable level of risk, that the population will persist for a specified time. The conventional wording (Shaffer 1981) is a 99 % chance of persistence for 1,000 years.

## From extinction times to a number
MVP is relative to a *risk level* and a *time horizon*. Shaffer's (1981) convention: 99 % chance of persistence for 1,000 years; other studies use 95 % over 100 years. A population-viability analysis combines the three stochasticities, the Allee threshold and the effect of age or stage structure ([[Sensitivity and Elasticity of Growth Rate]]), then reads the smallest $N$ that meets the target.

> [!example] MVP for a toy population
> The birth-death model with $b/d=1.2$ has mean extinction times $T=17,\ 72,\ 294,\ 1{,}299,\ 6{,}193$ for $K=10,\ 20,\ 30,\ 40,\ 50$. Taking one time unit as one year, the persistence probability over $t$ years is about $e^{-t/T}$: for a **1,000-year** horizon this is $e^{-1000/1299}=0.46$ at $K=40$ and $e^{-1000/6193}=0.85$ at $K=50$; reaching 99 % ($t/T\le0.01$) needs $T\ge100{,}000$, i.e. $K\approx65$ to 70 in this model. The MVP is far above the "average survival" size and depends strongly on assumed rates.
> **Rules of thumb (🔵).** The 50/500 rule (effective size 50 to avoid short-term inbreeding, about 500 for long-term evolutionary potential; Franklin 1980) refers to *effective* size ([[Genetic Drift and Inbreeding Depression]]), usually well below the census count.

**Bucher.** The passenger pigeon's MVP was unusually high because its food finding depended on flock size: a species that benefits from being many reaches its threshold while still numerous ([[Passenger Pigeon Extinction]]).

> [!pitfall] A number is a model output
> MVP changes with the model, the data and the acceptable risk; it is not a property of the species alone, and conservation must also protect the habitat that makes the number reachable ([[Reserve Design and Management]]). Definition (slide 15): "the minimum population size that will ensure, at some acceptable level of risk, that the population will persist for a specified time".

Used in: [[EE07 Conservation Biology]]. Related: [[Demographic Genetic and Environmental Stochasticity]] · [[Allee Effect]] · [[Project Tiger]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
