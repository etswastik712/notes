---
title: Three-Box Carbon Model
aliases: ["BEAM", "Bolin and Eriksson model", "Glotter 2014 model", "Three Boxes of Carbon"]
subject: climate
type: concept
scope: [taught, extra-beyond]
by: [joy]
status: draft
tags: [subject/climate, type/concept, taught, extra/beyond, src/joy, status/draft]
---
# Three-Box Carbon Model

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** Joy O7 §8, carbon-boxes handout Part 2
> 🔵 **extra · beyond:** re-implementation `scripts/cl_carbon_boxes.py`

> [!intuition] In one picture
> Air, upper ocean, deep ocean: three tanks connected in a row, with chemistry that makes the middle tank fill unevenly.

> [!key] Definition
> $\dot M_{AT}=E-k_a(M_{AT}-AB\,M_{UP})$, $\dot M_{UP}=k_a(\dots)-k_d(M_{UP}-M_{LO}/\delta)$, $\dot M_{LO}=k_d(\dots)$; 595 / 714 / 35 680 GtC; $1/k_a=5$ yr, deep turnover $\delta/k_d=1000$ yr ($\delta=50$). Settled level independent of the rates (334 ppm for our emissions); upper ocean catches up in ~4 months, the deep ocean in ~1000 yr. Fits Mauna Loa only with a 200-yr turnover (a fudge: the thermocline is fast, the abyss slow).

Tool: `cl_three_boxes`.

Used in: [[CL30 Tutorials III - Three Boxes of Carbon]], [[CL29 The Ocean's Ledger VI - Slow Swings and the Ocean's Memory for Carbon]]. Related: [[Revelle Factor]] · [[Stommel Two-Box Model]] · [[Ocean Carbon Sink and Airborne Fraction]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
