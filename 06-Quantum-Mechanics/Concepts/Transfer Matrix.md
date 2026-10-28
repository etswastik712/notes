---
title: Transfer Matrix
aliases: ["transfer-matrix method"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Transfer Matrix

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **Extra · beyond:** [[QM08 Quantum Tunnelling]] §3, §7 (used as the numerical check of every formula).

> [!intuition] In one picture
> Carry the pair (right-moving, left-moving) amplitudes across each interface with a $2\times2$ matrix; multiply the matrices for a stack.

> [!key] Definition and key results
> $\binom{A_{j+1}}{B_{j+1}}=M_j\binom{A_j}{B_j}$ from continuity of $\psi,\psi'$. $T$ follows from the total $M$ with $B_N=0$.

Handles any piecewise-constant potential (barriers, wells, superlattices); `scripts/qm08_numbers.py::tmat`.

Used in: [[QM08 Quantum Tunnelling]] §3, §7, §8. Related: [[Rectangular Barrier]] · [[Resonant Tunnelling]] · [[Kronig-Penney Model]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
