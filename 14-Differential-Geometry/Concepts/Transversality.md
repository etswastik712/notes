---
title: Transversality
aliases: ["transverse", "transverse intersection", "transversal maps"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/book, status/draft]
---
# Transversality

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=162|Lee Thm 6.30, p. 144]]; Thms 6.35–6.36; Guillemin–Pollack Ch. 2.

> [!intuition] In one picture
> Two things meet 'cleanly' when their tangent spaces together span everything: no tangential grazing.

> [!key] Definition
> $f:N\to M$ is **transverse** to an embedded $S\subseteq M$ if $df_p(T_pN)+T_{f(p)}S=T_{f(p)}M$ for all $p\in f^{-1}(S)$. Then $f^{-1}(S)$ is an embedded submanifold of codimension $\operatorname{codim}S$. Case $S=\{q\}$: $q$ is a regular value.

$y=x^2-c$ is transverse to the $x$-axis iff $c\ne0$ (slope angles $\pm45^\circ$ at $c=0.25$; tangent at $c=0$). The circle is tangent to $y=1$ at $(0,1)$. Transversality is generic and stable.

Used in: [[DM07 Sard Whitney and Transversality]]. Related: [[Regular Level Set Theorem]] · [[Regular Value]] · [[Embedded Submanifold]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
