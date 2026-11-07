---
title: Integrating Factor
aliases: ["integrating factor of a 1-form", "Lee Problem 19-3", "heat form integrating factor", "entropy as integrating factor"]
subject: diff-geometry
type: concept
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# Integrating Factor

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=530|Lee Problem 19-3, p. 512]] (statement only).

> [!intuition] In one picture
> A 1-form that is not closed may become exact after multiplying by a function; in two variables that always works, in three or more it needs $\omega\wedge d\omega=0$.

> [!key] Definition
> $\mu>0$ is an **integrating factor** for $\omega$ if $\mu\omega$ is exact. For nowhere-vanishing $\omega$ it exists near each point iff $d\omega\wedge\omega=0$ (Frobenius); if $\dim M=2$ it always exists (Lee Problem 19-3).

Thermodynamics (🔵): on the $(U,V)$ plane, $\delta Q=dU+P\,dV$ with $P=2U/3V$ has $d\delta Q\ne0$ but $\delta Q/U=d(\tfrac32\ln U+\ln V)$: the integrating factor is $1/T$, the potential is $S/R$. One mole, $V$ doubling at fixed $T$: $\Delta S=R\ln2=5.763$ J/K. Carathéodory's principle (recalled, not read) is the statement that such a factor exists for all reversible heat forms.

Used in: [[DM16 Distributions, Involutivity and the Frobenius Theorem]]. Related: [[Defining Forms and Pfaffian Systems]] · [[Entropy]] · [[Involutive Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
