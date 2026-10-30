---
title: Smooth Manifold Chart Lemma
aliases: ["chart lemma", "Lemma 1.35", "manifold construction lemma"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Smooth Manifold Chart Lemma

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG8 (via [[mt3184-differential-geometry-and-lie-groups/2026-08-20-august-17-21|Aug 17–21 note]]); HW3 Q2; [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=39|Lee Lemma 1.35, p. 21]].

> [!intuition] In one picture
> Build a manifold from a bare *set* by specifying coordinates; if they overlap smoothly and separate points, the topology and smooth structure are forced.

> [!key] Definition
> Given a set $M$, subsets $U_\alpha$ and bijections $\varphi_\alpha:U_\alpha\to$ open $\subseteq\mathbb R^n$ with (ii) open overlaps, (iii) smooth transitions, (iv) countably many $U_\alpha$ covering $M$, (v) any two points lie in a common $U_\alpha$ or in disjoint $U_\alpha,U_\beta$: then $M$ has a unique smooth manifold structure with the $\varphi_\alpha$ as smooth charts.

Used for $TM$ ([[DM04 The Tangent Bundle and the Rank Theorem]]) and Grassmannians. Gluing two copies of $\mathbb R^n$ by $w\mapsto w/|w|^2$ gives $S^n$; by the identity it violates (v): the [[Line with Two Origins]].

Used in: [[DM01 Smooth Manifolds]], [[DM04 The Tangent Bundle and the Rank Theorem]]. Related: [[Smooth Manifold]] · [[Smooth Atlas]] · [[Hausdorff Space]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
