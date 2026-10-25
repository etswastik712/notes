---
title: Expectation Value
aliases: ["mean value", "average value", "expectation"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Expectation Value

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_states_operators_notes.pdf#page=7|SO §7]], [[PH2113_matrices_expectation_uncertainty.pdf#page=2|MX §4, §6]].

> [!intuition] In one picture
> The average of many measurements on identically prepared systems; it need not be a result that any single measurement can give.

> [!key] Definition
> $\langle A\rangle=\sum_a|c_a|^2a=\displaystyle\int\Psi^*\hat A\Psi\,\mathrm dx=\langle\Psi|\hat A|\Psi\rangle$. E.g. $\langle x\rangle=\int x|\Psi|^2\mathrm dx$, $\langle p\rangle=\int\Psi^*(-i\hbar\partial_x)\Psi\,\mathrm dx$.

## Examples
- A state giving $0$ or $10$ eV with probability $\tfrac12$: $\langle E\rangle=5$ eV, but 5 eV is never found.
- Box: $\langle x\rangle=a/2$ for every $n$ (for $n=2$ the density at $a/2$ is zero).
- Ring $a\psi_n+b\psi_{-n}$: $\langle p\rangle=(|a|^2-|b|^2)p_n$.
- Two-level $(\tfrac{\sqrt3}2,\tfrac12)$: $\langle Z\rangle=\tfrac12$.

> [!pitfall] Average is not typical
> $\langle p\rangle=0$ for a cosine does not mean the momentum is 0: each measurement gives $\pm p_n$. Quote $\Delta A$ with it ([[Uncertainty of an Observable]]).

Used in: [[QM03 States Operators and Measurement]], [[QM04 The Particle in a Box]], [[QM05 The Harmonic Oscillator]]. Related: [[Uncertainty of an Observable]] · [[Measurement Postulate]] · [[Eigenstate and Eigenvalue]] · [[Time Evolution of a Superposition]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
