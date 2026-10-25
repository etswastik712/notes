---
title: Ground State Uniqueness
aliases: ["non-degenerate ground state", "nodeless ground state"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Ground State Uniqueness

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Tutorial2.pdf#page=2|Tutorial II Q4]].

> [!intuition] In one picture
> Two different nodeless ground states could be combined to cancel somewhere, and a combination with a node cannot be a ground state.

> [!key] Definition
> If the ground state of $\hat H=-\frac{\hbar^2}{2m}\partial_x^2+V$ has no nodes, it is non-degenerate: for $\psi_1,\psi_2>0$, $\phi=\psi_1-c\psi_2$ with $c=\psi_1(x_0)/\psi_2(x_0)$ has a node at $x_0$ and is still a ground state: contradiction.

## Notes
The nodeless property is a standard theorem (oscillation theorem, not proved here). The argument says nothing about excited states, which have nodes and may be degenerate (the ring's $\pm n$).

> [!pitfall] Needs linearity
> $\phi$ is an eigenfunction of the same energy only because $\hat H$ is linear.

Used in: [[QM05 The Harmonic Oscillator]]. Related: [[Node of a Wavefunction]] · [[Degeneracy]] · [[Harmonic Oscillator]] · [[Zero-Point Energy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
