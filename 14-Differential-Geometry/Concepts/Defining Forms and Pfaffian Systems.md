---
title: Defining Forms and Pfaffian Systems
aliases: ["local defining forms", "1-form criterion for involutivity", "differential ideal criterion", "Pfaffian system"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/lecture-notes, src/book, status/draft]
---
# Defining Forms and Pfaffian Systems

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=511|Lemma 19.5, p. 493]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=512|Thm 19.7, p. 494]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=513|Prop 19.8, p. 495]]; Prop 19.11 (p. 496) mentioned only.

> [!intuition] In one picture
> Describe the planes by the 1-forms that kill them: $D=\ker\omega$. The planes fit together exactly when $d\omega$ also kills them.

> [!key] Definition
> $D=\ker\omega^1\cap\dots\cap\ker\omega^{n-k}$ (**local defining forms**, Lemma 19.5). $D$ involutive $\iff$ $d\eta$ annihilates $D$ whenever $\eta$ does (Thm 19.7, from $d\eta(X,Y)=X\eta(Y)-Y\eta(X)-\eta([X,Y])$) $\iff d\omega^i=\sum_j\omega^j\wedge\alpha^i_j$. For one form: $\omega\wedge d\omega=0$.

$\omega=dz-y\,dx$: $d\omega=dx\wedge dy$, $\omega\wedge d\omega=dz\wedge dx\wedge dy\ne0$: not integrable. $\omega=d(z-xy)$: closed, integrable. Contact form $dz-x\,dy$: $\omega\wedge d\omega\ne0$.

Used in: [[DM16 Distributions, Involutivity and the Frobenius Theorem]]. Related: [[Involutive Distribution]] · [[Integrating Factor]] · [[Distribution]] · [[Frobenius Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
