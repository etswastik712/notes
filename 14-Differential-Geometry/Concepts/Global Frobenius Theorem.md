---
title: Global Frobenius Theorem
aliases: ["Theorem 19.21", "maximal connected integral manifolds", "Lemma 19.22"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Global Frobenius Theorem

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG29 via the [[mt3184-differential-geometry-and-lie-groups/2026-11-06-november-2-6|Nov 2–6 note (DG29–30)]] (statement).
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=520|Thm 19.21 and Lemma 19.22, p. 502]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=523|p. 505]].

> [!intuition] In one picture
> Glue all the local slices together: following the plane field as far as possible from each point produces a maximal leaf, and the leaves tile the manifold.

> [!key] Definition
> *If $D$ is involutive, the collection of all maximal connected integral manifolds of $D$ is a foliation of $M$.* Proof: the union of all connected integral manifolds through $p$ is again one (Lemma 19.22: topology by openness of overlaps, second countability by counting accessible slices), maximal; maximal ones meet only if equal; flat charts meet them in whole slices.

The leaves are immersed, not embedded in general (irrational torus). Leaves of a *left-invariant* $D$ on a Lie group are permuted by left translations (Prop 19.23): this gives Thm 19.26.

Used in: [[DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups]]. Related: [[Foliation]] · [[Frobenius Theorem]] · [[Invariant Distribution]] · [[Weakly Embedded Submanifold]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
