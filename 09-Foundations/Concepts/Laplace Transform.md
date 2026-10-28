---
title: Laplace Transform
aliases: ["Laplace transform", "unilateral Laplace transform"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Laplace Transform

> [!intuition] In one picture
> Fourier with a convergence factor and a starting time: $F(s)=\int_0^\infty f(t)e^{-st}\mathrm dt$, ideal for initial-value problems.

> [!key] Key facts
> $f'\to sF-f(0)$, $f*g\to FG$, $e^{-at}f\to F(s+a)$, delay $\to e^{-as}$. Table: $1\to1/s$, $e^{-at}\to1/(s+a)$, $\sin\omega t\to\omega/(s^2+\omega^2)$. Inverse by partial fractions or the Bromwich integral.

## In this vault
Maxwell model, relaxation, oscillators ([[LS01 Landscapes as Physical Systems]], [[LS02 Mechanics and Mathematics Toolkit]]); the MGF is the Laplace transform at $-t$ ([[Moment Generating Function]]).

> [!pitfall] Watch out
> Region of convergence matters; initial conditions appear automatically.

Used in: [[Fourier and Laplace Transforms]]. Related: [[Transfer Function]] · [[Poles and Stability]] · [[Final and Initial Value Theorems]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
