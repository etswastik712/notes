---
title: Open and Closed Sets
aliases: ["open set", "closed set", "open ball"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Open and Closed Sets

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=73|AI notes ch. 17.1]].

> [!intuition] In one picture
> Open: every point has room around it. Closed: contains everything that can be approached.

> [!key] Definition
> $U$ open iff $\forall x\in U\,\exists r>0\,B(x,r)\subseteq U$; $F$ closed iff its complement is open iff it contains the limits of its sequences. **Arbitrary unions** of open sets are open; **finite intersections** are open.

In $\mathbb R$: $(a,b)$ open; $[a,b]$ closed; $[a,b)$ neither; $\mathbb Z$ closed; $\mathbb Q$ neither; $\mathbb R,\varnothing$ both. $\bigcap(-\frac1n,\frac1n)=\{0\}$ not open; $\bigcup[\frac1n,1-\frac1n]=(0,1)$ not closed. Closed ball $\{d\le r\}$ is closed.

Used in: [[PA07 Metric and Topological Spaces]]. Related: [[Topological Space]] · [[Closure Interior and Boundary]] · [[Indexed Family of Sets]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
