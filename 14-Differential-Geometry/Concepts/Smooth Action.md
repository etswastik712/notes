---
title: Smooth Action
aliases: ["smooth group action", "Lie group action", "left action", "transitive action", "free action"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Smooth Action

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slides DG14–DG15 via [[mt3184-differential-geometry-and-lie-groups/2026-09-10-september-7-12|Sep 7–12 note]].

> [!intuition] In one picture
> A Lie group acting as a family of diffeomorphisms of a manifold, varying smoothly with the group element.

> [!key] Definition
> A smooth map $\theta:G\times M\to M$, $(g,p)\mapsto g\cdot p$, with $g_1\cdot(g_2\cdot p)=(g_1g_2)\cdot p$ and $e\cdot p=p$. Each $\theta_g$ is a diffeomorphism (inverse $\theta_{g^{-1}}$). **Transitive:** one orbit. **Free:** all stabilisers trivial.

Examples: left translation, conjugation, $GL(n,\mathbb R)$ on $\mathbb R^n$ (transitive on $\mathbb R^n\setminus\{0\}$), $SO(3)$ on $S^2$, congruence $A\cdot X=AXA^T$ on $M(n,\mathbb R)$, the irrational flow of $\mathbb R$ on $T^2$ (free, dense orbits). The finite-group version is [[Group Action]].

Used in: [[DM09 Group Actions and Semidirect Products]], [[DM12 Integral Curves, Flows and Flowouts]]. Related: [[Orbit Map and Stabiliser]] · [[Equivariant Map]] · [[Homogeneous Space]] · [[Lie Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
