---
title: Superposition Principle
aliases: ["linearity", "superposition of states"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Superposition Principle

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_Lecture9_FreeParticle_Ring_GeneralProperties.pdf#page=6|L9 §8]], [[PH2113_states_operators_notes.pdf#page=2|SO §2.1]].

> [!intuition] In one picture
> If two states are allowed, so is any mixture of them in amplitude: states form a vector space.

> [!key] Definition
> If $\Psi_1,\Psi_2$ solve the TDSE, so does $c_1\Psi_1+c_2\Psi_2$ ($c_i$ complex). Equal-energy states combine into a stationary state; different energies give a state with no definite energy.

## Examples
$\tfrac1{\sqrt2}(\psi_n+\psi_{-n})=\sqrt{2/L}\cos k_nx$ (momentum $\pm p_n$, each with probability $\tfrac12$); $\tfrac1{\sqrt2}(\psi_0+\psi_1)$ (no definite energy). Normalisation: $\sum|c_n|^2=1$ for orthonormal $\psi_n$.

> [!pitfall] A superposition is not an ignorance mixture
> $\tfrac1{\sqrt2}(\psi_n+\psi_{-n})$ does not mean "the particle has $+p$ or $-p$ and we do not know which": the **relative phase** matters ($\psi_n+e^{i\varphi}\psi_{-n}$ shifts the density), which no classical mixture can do.

Used in: [[QM02 The Schrodinger Equation and Stationary States]], [[QM03 States Operators and Measurement]], [[QM04 The Particle in a Box]]. Related: [[Global and Relative Phase]] · [[Time Evolution of a Superposition]] · [[Measurement Postulate]] · [[Wavefunction]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
