---
title: Isotropic Oscillator and Degeneracy
aliases: ["2D oscillator", "3D harmonic oscillator", "degenerate oscillator levels"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Isotropic Oscillator and Degeneracy

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond.**

> [!intuition] In one picture
> Three independent springs: the energy only depends on the total number of quanta, so many rung-triples share a level.

> [!key] Definition
> $\hat H=\hat H_x+\hat H_y+\hat H_z$, $\ E=(N+\tfrac32)\hbar\omega$, $N=n_x+n_y+n_z$; degeneracy $g_N=\binom{N+2}{2}=\tfrac{(N+1)(N+2)}2$ in 3-D, $N+1$ in 2-D; parity $(-1)^N$.

## Count (brute-force enumeration agrees)
| $N$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| 2-D | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 3-D | 1 | 3 | 6 | 10 | 15 | 21 | 28 |

It is a **stars-and-bars** count of non-negative solutions of $n_x+n_y+n_z=N$ ([[Counting Principles]]). At $N=3$: $(3,0,0)\times3$, $(2,1,0)\times6$, $(1,1,1)\times1$. The degeneracy comes from the rotation symmetry and a larger hidden symmetry.

> [!pitfall] The 1-D oscillator has no degeneracy
> Degeneracy needs more than one degree of freedom ([[Ground State Uniqueness]]).

Used in: [[QM06 The Oscillator Toolbox]] §9. Related: [[Degeneracy]] · [[Harmonic Oscillator]] · [[Parity Operator]] · [[Counting Principles]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
