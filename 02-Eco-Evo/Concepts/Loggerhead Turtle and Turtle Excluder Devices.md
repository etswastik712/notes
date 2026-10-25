---
title: Loggerhead Turtle and Turtle Excluder Devices
aliases: ["TED", "TEDs", "Caretta caretta", "turtle excluder device"]
subject: eco-evo
type: concept
scope: [taught, extra-book]
by: [slides, crowder]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/book, src/slides, src/paper, status/draft]
---
# Loggerhead Turtle and Turtle Excluder Devices

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the case study on the slides: stage matrix (Crouse et al. 1987), sensitivity result, trawling by-catch, ~70 years if TEDs used only occasionally, Indian legislation in 1996 ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=22|slide 22]], [[02_StageStructuredDynamics_11-Aug-2026.pdf#page=27|slide 27]])  ·  🟡 **extra · book:** Crowder et al. (1994), *Ecological Applications* 4: 437-445

> [!intuition] In one picture
> Where should scarce conservation money go: protecting eggs, which is easy and popular, or the stage that the arithmetic says matters? The matrix gives the answer, and it is not the eggs.

> [!key] Definition
> For the loggerhead (*Caretta caretta*) the stage-based projection has $\lambda<1$, and $\lambda$ is most sensitive to the survival of **large juveniles**. Improving egg survival can never make $\lambda>1$. Shrimp trawls kill large juveniles (5.7 kg of by-catch per kg of shrimp); **turtle excluder devices** let them escape. Simulations: occasional use needs about 70 years for a substantial effect, so permanent use was recommended.

## The case in numbers
Stages of the five-stage model (Table 1): eggs/hatchlings (1 yr, $\sigma=0.6747$), small juveniles (7 yr, 0.75), large juveniles (8 yr, 0.6758), subadults (6 yr, 0.7425), adults (> 32 yr, 0.8091, 76.5 eggs a year). The matrix gives $\lambda=0.9516$ ($-4.96\,\%$ a year; small-juvenile survival was lowered from 0.8144 to 0.75 to match the observed decline), a stable stage distribution $(0.239,\ 0.648,\ 0.103,\ 0.007,\ 0.003)$ (adults 0.3 %), and reproductive values $1,\ 1.4,\ 7.5,\ 115,\ 432$.

> [!example] What helps and what does not
> Cutting mortality by 10/50/90 % in one stage raises $r$ to: eggs $-0.048/-0.042/-0.037$; large juveniles $-0.036/+0.015/+0.060$ (baseline $-0.0496$). Perfect egg survival leaves $\lambda=0.965<1$; perfect large-juvenile survival gives 1.073. A 20 % cut in mortality of large juveniles, subadults and adults together reaches $\lambda=1$.
> **TEDs.** With Heron Island (unexploited) survivals 0.83/0.885/0.91 and a TED effect of $0.67$ of the gap ("seasonal offshore", 1990–92) the model gives $\lambda=1.035$ and $\times10$ in 67 years (paper: about 70); with $0.99$ (all waters, all year) $\lambda=1.073$ and 33 years. Strandings in South Carolina fell 37 % in TED years, consistent with the first estimate.

**Why slow, and why waves.** A turtle takes over 20 years to mature. The present stage structure reflects decades of heavy trawling, so after TEDs the number of nesting females first rises, flattens or dips about 10–15 years on, and rises again after 25–30 years (a 54-class Leslie simulation).

> [!pitfall] Hold the numbers loosely
> Quantitative forecasts rest on guessed survivals, a deterministic model and additive trawl mortality; the authors use the model to find *which parameters matter*. Slide 28's "occasionally" is the paper's "seasonal offshore" TED rule. Method background: [[Lefkovitch Stage-Structured Matrix]] and [[Sensitivity and Elasticity of Growth Rate]].

Used in: [[EE02 Structured Population Models]]. Related: [[Lefkovitch Stage-Structured Matrix]] · [[Sensitivity and Elasticity of Growth Rate]] · [[Project Tiger]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
