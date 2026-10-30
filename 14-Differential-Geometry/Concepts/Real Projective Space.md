---
title: Real Projective Space
aliases: ["RP^n", "projective space", "projective plane"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/book, status/draft]
---
# Real Projective Space

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=24|Lee Example 1.5, p. 6]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=39|Example 1.33, p. 21]]; Tu §7.

> [!intuition] In one picture
> The space of lines through the origin in $\mathbb R^{n+1}$: directions without orientation; equivalently the sphere with antipodal points identified.

> [!key] Definition
> $\mathbb{RP}^n=(\mathbb R^{n+1}\setminus0)/\mathbb R^\times=S^n/(x\sim-x)$, a compact connected $n$-manifold with $n+1$ charts $U_i=\{x^i\ne0\}$, $\varphi_i[x]=(x^j/x^i)_{j\ne i}$.

Hausdorff, second-countable and compact as a quotient of $S^n$ by a 2-to-1 open covering map ([[PA11 Subspaces, Products and Quotients]]). Transition on $\mathbb{RP}^2$: $(a,b)\mapsto(1/a,b/a)$, $\det=-1/a^3$. $\pi_1=\mathbb Z/2$ ($n\ge2$), $\mathbb{RP}^3\cong SO(3)$ ([[PA15 Covering Spaces and the Fundamental Group]]).

Used in: [[DM01 Smooth Manifolds]], [[PA11 Subspaces, Products and Quotients]]. Related: [[Smooth Manifold]] · [[Quotient Topology]] · [[Stereographic Projection]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
