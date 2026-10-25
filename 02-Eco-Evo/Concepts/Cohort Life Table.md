---
title: Cohort Life Table
aliases: ["life table", "l_x m_x table"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Cohort Life Table

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the *Phlox drummondii* table (Leverich and Levin 1979): 996 individuals followed through 9 age classes ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=10|slide 10]])

> [!intuition] In one picture
> Follow one batch of newborns until the last one dies and write down, at each age, how many are left and how many offspring they make. Everything demographic is in that table.

> [!key] Definition
> A **cohort life table** records, for each age class $x$: the number alive $n_x$, the survivorship $l_x=n_x/n_0$, and the mean number of offspring per survivor $m_x$ (fecundity). The product $l_xm_x$ is the expected offspring at age $x$ per newborn.

## Building the table
From the counts $n_x$ everything else follows: deaths in the interval $d_x=n_x-n_{x+1}$, interval mortality $q_x=d_x/n_x$, survivorship $l_x=n_x/n_0$ and the expected offspring $l_xm_x$.

> [!example] First rows of the *Phlox* table
> $n=996,\ 158,\ 154,\ 151,\dots$. The first class loses $d=996-158=838$ individuals, $q=0.841$: 84 % die before day 299. The next intervals lose $4,\ 3,\ 4$ plants, $q=0.025,\ 0.019,\ 0.026$. Mortality is then very small for weeks and rises again to $q=0.70$ and $q=1$ in the last two intervals. Reproduction ($m_x$ peaks at 8.66 seeds per plant) is concentrated where $l_x$ is already small, so the largest term of $\sum l_xm_x$ ($0.6436$) comes from only 7.4 % of the original cohort.

**Cohort versus static.** A cohort table follows individuals born together (accurate; hard for long-lived animals). A **static** table records the age at death of individuals from different cohorts (Murie's Dall sheep: 608 skulls aged by horn rings) or uses the age distribution of a population. Both assume something: that survival has not changed between cohorts, and for the age-distribution method that the population is neither growing nor shrinking and is closed. If the population is growing, young animals are over-represented and mortality of the young is *underestimated*.

> [!pitfall] Class widths and the first class
> The slide's first class is 299 days long and the others 7: $l_x$ is a value at the *start* of each class, so a plot between data points (as in [[Survivorship Curve]]) is an interpolation. Fecundity $m_x$ is per surviving individual *in the interval*, so $l_xm_x$ needs matching age conventions.

The table feeds [[Net Reproductive Rate]] (its column sum) and the matrices of [[Leslie Matrix]] ($P_x=l_{x+1}/l_x$, $F_x$ from $m_x$).

Used in: [[EE02 Structured Population Models]]. Related: [[Survivorship Curve]] · [[Net Reproductive Rate]] · [[Population Ecology]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
