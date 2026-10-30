---
title: Tangent Vector
aliases: ["derivation at a point", "tangent vector at p", "derivation"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Tangent Vector

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[mt3184-differential-geometry-and-lie-groups/2026-08-14-hw2|HW2]] Q1, [[mt3184-differential-geometry-and-lie-groups/2026-09-03-test-i|Test 1]] Q1 (locality via bump functions); week 2 (slides unreadable).
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=71|Lee Lemma 3.1, Prop. 3.2, pp. 53–54]]; Tu §2.

> [!intuition] In one picture
> A rule for differentiating functions at a point: 'rate of change of $f$ in a direction'. Linearity and the product rule are all it must obey.

> [!key] Definition
> A **derivation at $p$** is a linear $v:C^\infty(M)\to\mathbb R$ with $v(fg)=f(p)v(g)+g(p)v(f)$. Constants are killed; $v$ is **local** ($f=g$ near $p\Rightarrow vf=vg$, by a bump function).

On $\mathbb R^n$: $v=\sum v(x^i)\,\partial/\partial x^i|_a$ (Hadamard's lemma). Equivalent definitions: velocity of curves, or $n$-tuples with a transformation law ([[Velocity of a Curve]], [[Transformation Law for Tangent Vectors]]).

Used in: [[DM03 Tangent Vectors and the Differential]]. Related: [[Tangent Space]] · [[Coordinate Basis]] · [[Bump Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
