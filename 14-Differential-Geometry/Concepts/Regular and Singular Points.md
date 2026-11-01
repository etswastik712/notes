---
title: Regular and Singular Points
aliases: ["singular point", "regular point", "equilibrium point", "canonical form near a regular point", "flow box", "Theorem 9.22", "straightening a vector field"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Regular and Singular Points

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG24 via [[mt3184-differential-geometry-and-lie-groups/2026-10-16-october-12-16|Oct 12–16 note]]; HW7 Q4, Q6.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=237|Lee Prop. 9.21, p. 219]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=238|Lee Thm 9.22, p. 220]].

> [!intuition] In one picture
> Where the field vanishes nothing moves; where it does not, the flow lines are locally parallel straight lines.

> [!key] Definition
> $p$ singular if $V_p=0$: then $\theta^{(p)}\equiv p$ (equilibrium). $p$ regular: $\theta^{(p)}$ is an immersion (Prop 9.21). **Canonical form (Thm 9.22):** near a regular point there are coordinates with $V=\partial/\partial s^1$ (and $S=\{s^1=0\}$ for any transverse hypersurface $S$). A maximal curve is constant, injective or periodic.

HW7 Q6: with $V$ nowhere zero on a compact $M$, $\theta_t$ ($t>0$ small) is homotopic to the identity and fixed-point free, proved with a flow-box chart. Polar coordinates are the canonical form of $-y\partial_x+x\partial_y$. The first non-trivial local invariants appear for several fields ([[DM13 Lie Derivatives and Commuting Vector Fields]]).

Used in: [[DM12 Integral Curves, Flows and Flowouts]]. Related: [[Flowout Theorem]] · [[Integral Curve]] · [[Vector Field]] · [[Flow of a Vector Field]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
