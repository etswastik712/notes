---
title: Foliation by Fibres of a Submersion
aliases: ["level-set foliation", "HW10 Q5", "Lee Problem 19-8", "fibres of a submersion"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Foliation by Fibres of a Submersion

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** HW10 Q5 via [[mt3184-differential-geometry-and-lie-groups/2026-11-06-hw10|HW10]].
> 🟡 **extra · book:** Lee Problem 19-8 ([[John M. Lee - Introduction to Smooth Manifolds.pdf#page=531|p. 513]]).

> [!intuition] In one picture
> The rank theorem says a submersion is a coordinate projection locally, so its fibres are the slices of a flat chart.

> [!key] Definition
> If $F:M\to N$ is a smooth submersion, the **connected components of the nonempty fibres** $F^{-1}(q)$ form a foliation of $M$ of dimension $\dim M-\dim N$. Proof: rank-theorem charts $(x^1..x^n)\mapsto(x^1..x^m)$ with a cube domain: a fibre meets the chart in a single connected slice.

$F=x^2+y^2-z^2$ on $\mathbb R^3\setminus0$: one component for $c>0$, two for $c=0$ (cone nappes) and for $c<0$; $\ker dF=\mathrm{span}\{R,B_1,B_2\}$ with $[R,B_1]=B_2$, $[R,B_2]=-B_1$, $[B_1,B_2]=-R$: the leaves are $SO(2,1)^0$-orbits.

Used in: [[DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups]]. Related: [[Foliation]] · [[Rank Theorem]] · [[Regular Level Set Theorem]] · [[Characteristic Property of Surjective Submersions]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
