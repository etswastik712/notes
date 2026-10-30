---
title: Bump Function
aliases: ["cutoff function", "cut-off function", "flat function", "smooth step"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Bump Function

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** HW2 Q1, Test 1 Q1 (locality of tangent vectors), HW4 Q2 (extension of a vector).
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=59|Lee Lemmas 2.20–2.22 (pp. 41–42)]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=62|Prop. 2.25 (p. 44)]]; Tu §13.

> [!intuition] In one picture
> A smooth function that is $1$ on a chosen set and $0$ outside a slightly larger one: a smooth switch.

> [!key] Definition
> $f(t)=e^{-1/t}$ ($t>0$), $0$ otherwise, is smooth and flat at $0$; $h(t)=f(t)/(f(t)+f(1-t))$ is a smooth step ($0$ for $t\le0$, $1$ for $t\ge1$); $b(x)=h(2-|x|)$ is $1$ on $\overline B_1$ and supported in $\overline B_2$. On a manifold: for closed $A\subseteq U$ open there is smooth $\psi$ with $\psi=1$ on $A$, $\operatorname{supp}\psi\subseteq U$.

Numbers: $f(t)/t^{20}=3.7\times10^{-4}$ at $t=0.01$; $h(0.25)=0.0650$, $h(0.75)=0.9350$. Proves locality of derivations and lets one extend vectors to vector fields.

Used in: [[DM02 Smooth Maps and Partitions of Unity]]. Related: [[Partition of Unity]] · [[Smooth Extension Lemma]] · [[Smooth Urysohn Lemma]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
