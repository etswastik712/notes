---
title: Survivorship Curve
aliases: ["Type I II III survivorship"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Survivorship Curve

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the three idealised types and why the y-axis is logarithmic ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=11|slide 11]])

> [!intuition] In one picture
> On a linear axis, losing 60 % of 1000 looks worse than losing 60 % of 400 although the risk is identical. A log axis turns equal *proportions* into equal vertical steps, so constant risk becomes a straight line.

> [!key] Definition
> A **survivorship curve** plots $\log l_x$ against age. **Type I:** mortality low until late in life. **Type II:** constant per-capita mortality; $l_x=(1-q)^x$, a straight line on the log axis. **Type III:** very high early mortality, then low. Real curves are mixtures and approximations (slide).

## Why log, and how steep
Constant risk gives a straight line: if each interval kills a fraction $q$, then $n_x=n_0(1-q)^x$ and $\ln n_x=\ln n_0+x\ln(1-q)$. The slope of a log-survivorship curve is therefore the per-capita **hazard** $-\mu$ (continuous time: $n=n_0e^{-\mu x}$), and *a bend in the curve is a change in risk*. A linear axis shows how many die; a log axis shows how likely each individual is to die.

> [!example] How extreme can Type III be?
> Molles' mackerel: of $10^{6}$ eggs more than 999,990 die in 70 days. Survival $\le10^{-5}$ over 70 days means a mean daily mortality of at least $1-e^{-\ln(10^{5})/70}=1-e^{-0.1645}=15\,\%$ **per day**. The slide's hypothetical Type II (60 % lost per step) has $q=0.6$ and log-slope $\ln0.4=-0.92$ per step, steeper per step but constant.

**Examples (Molles).** Type I: Dall sheep, the annual plant *Phlox drummondii* after its early loss, the rotifer *Floscularia* (a life played out in 11 days). Type II: American robin, white-crowned sparrow, the common mud turtle after year 1. Type III: mackerel, the prawn *Leander* (about 2,000 survivors per $10^6$ eggs after one year), the desert shrub *Cleome* (39 per million seeds reach age 1, 0.0039 %).

> [!pitfall] Reading the types
> Type III is about *juvenile* survival, not about short lives. Real curves are mixtures: *Phlox* has a Type III-like first class and a Type I-like end; the three types are bounds that frame what is possible. The plot also hides *when reproduction happens*; pair it with $m_x$ ([[Cohort Life Table]]).

Survivorship is the $l_x$ factor in [[Net Reproductive Rate]] and sets the sub-diagonal of a [[Leslie Matrix]].

Used in: [[EE02 Structured Population Models]]. Related: [[Cohort Life Table]] · [[Net Reproductive Rate]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
