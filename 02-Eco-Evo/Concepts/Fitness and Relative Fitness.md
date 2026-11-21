---
title: Fitness and Relative Fitness
aliases: ["fitness", "relative fitness", "w11 w12 w22", "selection coefficient", "dominance coefficient", "mean fitness"]
subject: eco-evo
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/eco-evo, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Fitness and Relative Fitness

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** one-locus selection model, EE10 §7

> [!intuition] In one picture
> A genotype's fitness is its expected contribution to the next generation; only ratios matter.

> [!key] Definition
> Relative fitnesses $w_{11}:w_{12}:w_{22}$, often $1:1-hs:1-s$ ($s$ selection coefficient, $h$ dominance). After HW zygotes: $p'=(p^2w_{11}+pqw_{12})/\bar w$, $\Delta p=pq[p(w_{11}-w_{12})+q(w_{12}-w_{22})]/\bar w$, $\bar w=p^2w_{11}+2pqw_{12}+q^2w_{22}$. With $s=0.1$, $p$ 0.01 → 0.99 takes 175 generations (additive), ~1000 (dominant or recessive favoured allele).

Tool: `ee_selection`.

Used in: [[EE10 Natural Selection]]. Related: [[Natural Selection]] · [[Hardy-Weinberg Equilibrium]] · [[Modes of Selection]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
