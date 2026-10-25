---
title: Metric Space
aliases: ["metric", "distance function", "triangle inequality"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Metric Space

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=73|AI notes ch. 17.1]].

> [!intuition] In one picture
> A set with a notion of distance.

> [!key] Definition
> $d(x,y)\ge0$ ($=0$ iff $x=y$), $d(x,y)=d(y,x)$, $d(x,z)\le d(x,y)+d(y,z)$. Examples: Euclid, $\ell^1$, $\ell^\infty$, discrete, sup metric. $\|x-y\|^2$ is **not** a metric ($d(0,2)=4>2$).

Open ball $B(x,r)=\{y:d(x,y)<r\}$; in $\mathbb R^2$ the unit balls of $\ell^1,\ell^2,\ell^\infty$ are a diamond (area 2), a disc ($\pi$) and a square (4). 5000 random triples: no violation for the four metrics, 1256 violations for the squared distance.

Used in: [[PA07 Metric and Topological Spaces]]. Related: [[Open and Closed Sets]] · [[Cauchy Sequence]] · [[Topological Space]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
