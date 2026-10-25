---
title: Parity Operator
aliases: ["parity", "reflection operator"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Parity Operator

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_states_operators_notes.pdf#page=3|SO §3]], [[tutorial1.pdf#page=1|Tutorial I Q4]].

> [!intuition] In one picture
> Mirror the line; the states of a mirror-symmetric potential come out even or odd.

> [!key] Definition
> $\hat P\psi(x)=\psi(-x)$, eigenvalues $\pm1$ (even/odd). If $V(-x)=V(x)$ then $[\hat P,\hat H]=0$ and non-degenerate eigenfunctions are even or odd.

## Examples
$\hat P\cos kx=\cos kx$, $\hat P\sin kx=-\sin kx$; $e^{ikx}$ is not a parity eigenstate. Box about its centre: parity $(-1)^{n+1}$. Oscillator: $(-1)^n$.

> [!extra-beyond]- 🔵 Extra (beyond): a selection rule
> For same-parity states $\langle\psi_m|(x-\text{centre})|\psi_n\rangle=0$ (odd integrand): a superposition $\psi_1+\psi_3$ in a box has $\langle x\rangle=a/2$ for ever.

> [!pitfall] Degenerate levels
> $e^{\pm ikx}$ share an energy; the parity eigenstates $\cos,\sin$ are the right basis there.

Used in: [[QM03 States Operators and Measurement]], [[QM04 The Particle in a Box]]. Related: [[Degeneracy]] · [[Particle in a Box]] · [[Harmonic Oscillator]] · [[Node of a Wavefunction]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
