---
title: Age Pyramid
aliases: ["population pyramid", "age structure diagram"]
subject: eco-evo
type: concept
scope: [taught, extra-book]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/book, src/slides, status/draft]
---
# Age Pyramid

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the rule on the slide: greater $\lambda$, broader base; narrow base, declining population ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=29|slide 29]])  ·  🟡 **extra · book:** UN *World Population Prospects 2024* and the India growth report in the course folder (not on the reading slide)

> [!intuition] In one picture
> Stack the age classes sideways: a wide bottom means many children relative to adults, so tomorrow's parents outnumber today's.

> [!key] Definition
> An **age pyramid** shows the number (or share) of people in each age class, males and females back to back. A broad base signals a large $\lambda$ (growing population), a narrow base a falling one, near-vertical sides a roughly stable one.

## Reading and computing a pyramid
Each bar is the share of the population in an age class. If a population has been growing at a steady $r$, the age distribution is the stable one ([[Stable Age Distribution]]): shares fall with age like $l_xe^{-rx}$. A broad base means $r>0$, near-vertical sides $r\approx0$, a narrow base $r<0$ (slide 29).

> [!example] Three countries (Molles Fig. 11.24; UN 2020)
> Sweden $b=d=0.010$, $r=0$; Hungary $b=0.010$, $d=0.013$, $r=-0.003$ (halving time $\ln2/0.003=231$ years); Rwanda $b=0.037$, $d=0.010$, $r=+0.027$ (doubling time 25.7 years; $\lambda=e^{r}=1.027$). My model pyramids ($R_0=2.0,\ 1.0,\ 0.6$): $\lambda=1.12,\ 1.00,\ 0.92$ per five years, and 36 %, 20 %, 12 % of the population under 15.

**History in the shape.** Molles' white oaks (1–50-year trees dominate: replacing themselves), Rio Grande cottonwoods (40–50-year trees, no seedlings for a decade after dams ended floods), and the large cactus finch (gaps after the 1977 and 1984–85 droughts) show that an age distribution is a record of past reproduction and survival, not only of the present rate.

> [!extra-beyond]- 🔵 Extra (beyond): replacement and momentum
> Replacement fertility: $R_0=\text{TFR}\times\tfrac{100}{205}\times s=1$ gives TFR $=2.05/s\approx2.1$. **Momentum:** a toy country with $\lambda=1.275$ per 20 years whose fertility is cut to $R_0=1$ immediately still ends 17 % larger, because the large young cohorts have yet to reproduce (WPP 2024: 79 % of growth to 2054 is momentum; world peak about 10.3 billion in the mid-2080s).

Pitfall: pyramids show *shares*; a country with a narrow base may still be growing for a generation (momentum). Links: [[Net Reproductive Rate]], [[Leslie Matrix]].

Used in: [[EE02 Structured Population Models]]. Related: [[Stable Age Distribution]] · [[Population Ecology]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
