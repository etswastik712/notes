---
title: Normal Ordering
aliases: ["normal-ordered", "a a dagger ordering"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Normal Ordering

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond.**

> [!intuition] In one picture
> Always write annihilation operators to the right, so that they hit the vacuum and give zero.

> [!key] Definition
> A product is **normal-ordered** if every $\hat a^\dagger$ stands to the left of every $\hat a$. Reordering uses $\hat a\hat a^\dagger=\hat a^\dagger\hat a+1$.

## Why it helps
$\langle0|{:}\,\hat O\,{:}|0\rangle=0$ for any normal-ordered operator with at least one $\hat a$ or $\hat a^\dagger$, and for a **coherent state** $\langle\alpha|\hat a^{\dagger k}\hat a^l|\alpha\rangle=\alpha^{*k}\alpha^l$ immediately. Example: $\langle(\hat a+\hat a^\dagger)^2\rangle_\alpha=\langle\hat a^2+\hat a^{\dagger2}+2\hat a^\dagger\hat a+1\rangle=\alpha^2+\alpha^{*2}+2|\alpha|^2+1$, and the "$+1$" from reordering is the zero-point fluctuation.

> [!pitfall] The "+1" is not optional
> $\hat H=\hbar\omega(\hat a^\dagger\hat a+\tfrac12)$: the $\tfrac12$ is the reordering constant of $\tfrac12(\hat a\hat a^\dagger+\hat a^\dagger\hat a)$.

Used in: [[QM06 The Oscillator Toolbox]] §7. Related: [[Ladder Operators]] · [[Coherent State]] · [[Commutator]] · [[Oscillator Expectation Values]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
