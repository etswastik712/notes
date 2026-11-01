---
title: F-Related Vector Fields
aliases: ["F-related", "pushforward of a vector field", "F_*X", "related vector fields"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# F-Related Vector Fields

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG10 (Prop 8.19) via [[mt3184-differential-geometry-and-lie-groups/2026-08-27-august-24-28|Aug 24–28 note]]; HW4 Q3.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=200|Lee Prop. 8.16, p. 182]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=201|Lee Prop. 8.19, p. 183]].

> [!intuition] In one picture
> Two fields that the map $F$ carries into each other: following $X$ in $M$ and then applying $F$ equals following $Y$ in $N$.

> [!key] Definition
> $X\in\mathfrak X(M)$ and $Y\in\mathfrak X(N)$ are $F$-related if $dF_p(X_p)=Y_{F(p)}$ for all $p$, iff $X(f\circ F)=(Yf)\circ F$ for all $f$ (Prop 8.16). If $F$ is a **diffeomorphism**, $F_*X=dF\circ X\circ F^{-1}$ is the unique related field (Prop 8.19). Brackets of related pairs are related ([[Naturality of the Lie Bracket]]).

HW4 Q3: $F(x,y)=(xy,y/x)$ on the open quadrant sends $x\partial_x+y\partial_y$ to $2u\partial_u$. $\partial_t$ on $\mathbb R$ is related to $-y\partial_x+x\partial_y$ under $t\mapsto(\cos t,\sin t)$. In general no related field exists for a non-injective or non-surjective $F$; for a Lie group homomorphism, left-invariant fields are related ([[DM11 The Lie Algebra of a Lie Group]]).

Used in: [[DM10 Vector Fields and Lie Brackets]]. Related: [[Vector Field]] · [[Differential of a Smooth Map]] · [[Diffeomorphism]] · [[Naturality of the Lie Bracket]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
