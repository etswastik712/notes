---
title: Blending Inheritance
aliases: ["blending theory", "Jenkin's objection", "Fleeming Jenkin"]
subject: eco-evo
type: concept
scope: [taught, extra-beyond]
by: [slides, book, own-notes]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/beyond, src/slides, src/book, src/own-notes, status/draft]
---
# Blending Inheritance

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Evolution_06-Oct-2026.pdf#page=50|EE08 slide 50]] (objection 4)
> 🔵 **extra · beyond:** variance arithmetic and simulation, EE08 §5.1

> [!intuition] In one picture
> If offspring were the average of their parents, a population would turn uniform in a few generations and selection would have nothing to work on.

> [!key] Definition
> Under blending, offspring trait $=\tfrac12(z_m+z_f)$; with random mating $\operatorname{Var}=\tfrac14(V+V)=V/2$, so $V_t=V_0/2^t$ (Jenkin 1867: half the heritable variation lost each generation). Darwin 'had no answer'. Mendelian inheritance keeps variation (the Hardy–Weinberg law 'finally put to rest' the objection, Templeton p. 34).

Simulation (20 000 individuals): blending variance 1 → 0.50 → 0.25 → 0.125 …; Mendelian at 20 loci stays within 2 % of 1 over 8 generations (`scripts/ee08_10_numbers.py`). Tool: `ee_blending`.

Used in: [[EE08 Evolution - An Introduction]], [[EE09 Hardy-Weinberg Equilibrium]]. Related: [[Hardy-Weinberg Equilibrium]] · [[Modern Synthesis]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
