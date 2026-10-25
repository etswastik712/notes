---
title: Two-Level System
aliases: ["two-state system", "qubit", "two-dimensional state space"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Two-Level System

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_matrices_expectation_uncertainty.pdf#page=1|MX §1–5]].

> [!intuition] In one picture
> The smallest quantum system: a state is just a pair of complex numbers.

> [!key] Definition
> A normalised vector $\binom ab$ ($|a|^2+|b|^2=1$); observables are Hermitian $2\times2$ matrices. Probability of an outcome is $|c|^2$ in the corresponding eigenbasis; $\langle A\rangle=\langle\psi|A|\psi\rangle$.

## Dictionary to wave mechanics
state $\leftrightarrow\psi(x)$; Hermitian matrix $\leftrightarrow\hat x,\hat p,\hat H$; $\sum_{n=1}^2c_n|a_n\rangle\leftrightarrow\sum_nc_n\phi_n$ (sum becomes integral for a continuous spectrum); $|c_n|^2$ the same.

> [!example] Numbers
> $|\psi\rangle=(\tfrac{\sqrt3}2,\tfrac12)$: $Z$: $0.75/0.25$; $X$: $0.933/0.067$; $Y$: $0.5/0.5$; $\langle Z\rangle=\tfrac12$, $\Delta Z=\tfrac{\sqrt3}2$.

> [!pitfall] Not a classical coin
> The state $|{+z}\rangle$ is an equal superposition of $|{+x}\rangle$ and $|{-x}\rangle$; measuring $X$ on it is 50:50, and phases between components set the results in other bases.

Used in: [[QM03 States Operators and Measurement]]. Related: [[Pauli Matrices]] · [[Measurement Postulate]] · [[Expectation Value]] · [[Generalised Uncertainty Principle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
