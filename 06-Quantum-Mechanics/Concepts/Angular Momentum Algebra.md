---
title: Angular Momentum Algebra
aliases: [angular momentum commutation relations, ladder operators for angular momentum, J plus J minus]
subject: qm
type: concept
scope: [extra-book]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, src/book, src/own-notes, status/draft]
---
# Angular Momentum Algebra

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** Sakurai §3.5 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=200|PDF p.200 ff.]]); Griffiths §4.3 ([[Griffiths - Introduction to quantum mechanics.pdf#page=160|p.145 ff.]]). The ladder method is taught for the oscillator ([[Ladder Operators]]).

> [!intuition] In one picture
> The same trick as the oscillator ladder: a commutator and the demand that the ladder ends at both ends produce the whole spectrum.

> [!key] Definition and key results
> $[J_i,J_j]=i\hbar\epsilon_{ijk}J_k$, $J_\pm=J_x\pm iJ_y$, $[J_z,J_\pm]=\pm\hbar J_\pm$, $[J_+,J_-]=2\hbar J_z$, $\mathbf J^2=J_-J_++J_z^2+\hbar J_z$. Result: $j=0,\frac12,1,\frac32,\dots$, $m=-j,\dots,j$, $J_\pm|j,m\rangle=\hbar\sqrt{j(j+1)-m(m\pm1)}\,|j,m\pm1\rangle$.

Positivity of $\|J_\pm|\lambda,m\rangle\|^2=\hbar^2[\lambda-m(m\pm1)]$ bounds $m$, so $J_+|j\rangle=0$ at the top ($\lambda=j(j+1)$) and $J_-|{-j}\rangle=0$ at the bottom; stepping from $-j$ to $j$ needs $2j\in\mathbb N$. For $j=\frac12$ this gives the Pauli matrices; the SG apparatus reads out $2j+1$.

> [!pitfall] Pitfall
> Only the commutators are used: nothing says $j$ is orbital or spin. Integer $j$ from $-i\hbar\mathbf r\times\nabla$ (single-valued), half-integer $j$ from spin only.

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §9.1. Related: [[Spin]] · [[Spin-One Systems]] · [[Schwinger Oscillator Model]] · [[Commutator]] · [[Ladder Operators]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
