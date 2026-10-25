---
title: Uncertainty of an Observable
aliases: ["standard deviation of an observable", "spread"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Uncertainty of an Observable

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_states_operators_notes.pdf#page=8|SO §8]], [[PH2113_matrices_expectation_uncertainty.pdf#page=3|MX §7]].

> [!intuition] In one picture
> How widely the results scatter around the average.

> [!key] Definition
> $(\Delta A)^2=\langle(A-\langle A\rangle)^2\rangle=\langle A^2\rangle-\langle A\rangle^2$. In an eigenstate $\Delta A=0$: definite value $\Leftrightarrow$ zero uncertainty.

## Examples (recomputed)
- Two equally likely eigenvalues $a_1,a_2$: $\Delta A=|a_2-a_1|/2$.
- Ring $a\psi_n+b\psi_{-n}$: $\Delta p=2|a||b||p_n|$ (maximal for equal weights).
- Box state: $\Delta x=a\sqrt{1/12-1/2n^2\pi^2}$, $\Delta p=n\pi\hbar/a$.
- $|{+z}\rangle$: $\Delta X=\Delta Y=1$.

> [!pitfall] Not an instrument error
> $\Delta A$ is the intrinsic spread of the outcome distribution of identically prepared systems.

Used in: [[QM03 States Operators and Measurement]], [[QM04 The Particle in a Box]]. Related: [[Expectation Value]] · [[Heisenberg Uncertainty Principle]] · [[Eigenstate and Eigenvalue]] · [[Generalised Uncertainty Principle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
