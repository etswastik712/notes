---
title: Commuting Vector Fields
aliases: ["commuting flows", "[V,W]=0", "Theorem 9.44"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/lecture-notes, src/book, status/draft]
---
# Commuting Vector Fields

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=251|Lee Thm 9.44, p. 233]].

> [!intuition] In one picture
> Two vector fields commute when it does not matter in which order you flow along them.

> [!key] Definition
> $[V,W]=0$ iff $VWf=WVf$ for all $f$ iff **the flows commute**: $\theta_t\psi_s=\psi_s\theta_t$ (Thm 9.44; for non-complete fields wherever both sides are defined). In general $\theta_t\psi_s-\psi_s\theta_t\approx-st[V,W]$; for $V=\partial_x$, $W=x\partial_y$ it is exactly $-st\,\partial_y$.

$E=x\partial_x+y\partial_y$ and $R=-y\partial_x+x\partial_y$ commute (dilations and rotations commute); $\partial_x$ and $x\partial_y$ do not. HW9 Q4: $[X,Y]=0\iff\exp tX\exp sY=\exp sY\exp tX$ ([[DM14 One-Parameter Subgroups and the Exponential Map]]). Simultaneous straightening: [[Commuting Frame]].

Used in: [[DM13 Lie Derivatives and Commuting Vector Fields]], [[DM14 One-Parameter Subgroups and the Exponential Map]]. Related: [[Lie Bracket of Vector Fields]] · [[Invariant Vector Field]] · [[Flow of a Vector Field]] · [[Commuting Frame]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
