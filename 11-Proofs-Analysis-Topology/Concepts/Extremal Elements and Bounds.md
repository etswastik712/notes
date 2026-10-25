---
title: Extremal Elements and Bounds
aliases: ["minimal and maximal", "minimum and maximum", "glb and lub", "supremum and infimum"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Extremal Elements and Bounds

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-prems_merged.pdf#page=1|Assignment 4, Q1–Q4, Q8]].

> [!intuition] In one picture
> Minimal = nothing below it in $S$; minimum = below everything in $S$; bounds may lie outside $S$.

> [!key] Definition
> For $S\subseteq P$: minimal ($\nexists s<m$), **minimum** ($m\le s$ for all $s$; unique), lower bound (any $p\le s$ for all $s$), glb (largest lower bound), and dually maximal/maximum/upper bound/lub. A minimum is minimal, not conversely; in a total order they agree.

$S=\{2,3,4,6\}$ in divisors of 24: minimal 2, 3; maximal 4, 6; lower bound 1; upper bounds 12, 24; glb 1, lub 12. In $\mathcal P(\{1,2,3,4\})$, $S=\{\{1\},\{2\},\{1,2\},\{1,3\},\{2,3\}\}$: glb $\varnothing$, lub $\{1,2,3\}$. $\mathbb Z^2$, $\{(0,1),(1,0),(1,2),(2,1)\}$: glb $(0,0)$, lub $(2,2)$.

Used in: [[PA03 Relations Equivalence and Order]]. Related: [[Partially Ordered Set]] · [[Least Upper Bound Property]] · [[Zorn's Lemma]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
