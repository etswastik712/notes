---
title: Closure Interior and Boundary
aliases: ["closure", "interior", "boundary", "dense set"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Closure Interior and Boundary

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=77|AI notes ch. 18.3]].

> [!intuition] In one picture
> Interior: points with room inside $A$; closure: $A$ plus what it approaches; boundary: the difference.

> [!key] Definition
> $\mathrm{int}A$ = largest open subset; $\mathrm{cl}A$ = smallest closed superset; $\mathrm{bd}A=\mathrm{cl}A\setminus\mathrm{int}A$. $A$ open iff $A=\mathrm{int}A$; closed iff $A=\mathrm{cl}A$.

In $\mathbb R$: $\mathrm{int}[0,1]=(0,1)$, $\mathrm{cl}(0,1)=[0,1]$, $\mathrm{bd}[0,1]=\{0,1\}$, $\mathrm{int}\,\mathbb Q=\varnothing$, $\mathrm{cl}\,\mathbb Q=\mathbb R$ (so $\mathbb Q$ is dense). Cofinite topology: every non-empty open set is dense.

Used in: [[PA07 Metric and Topological Spaces]]. Related: [[Open and Closed Sets]] · [[Topological Space]] · [[Archimedean Property]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
