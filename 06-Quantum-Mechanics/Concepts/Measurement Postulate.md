---
title: Measurement Postulate
aliases: ["measurement in quantum mechanics", "collapse"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Measurement Postulate

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_states_operators_notes.pdf#page=7|SO §6]], [[PH2113_states_operators_notes.pdf#page=13|SO §13]].

> [!intuition] In one picture
> Measure $A$ and the result is always one of its eigenvalues, drawn with probabilities set by the amplitudes.

> [!key] Definition
> Expand $\Psi=\sum_ac_a\phi_a$ in eigenstates of $\hat A$. Measuring $A$ gives eigenvalue $a$ with probability $|c_a|^2$ ($c_a=\langle\phi_a|\Psi\rangle$); afterwards the state is $\phi_a$.

## Examples
$\Psi=\tfrac{\sqrt3}2\psi_n+\tfrac12\psi_{-n}$: $+p_n$ with probability $\tfrac34$, $-p_n$ with $\tfrac14$. $|\psi\rangle=\tfrac{\sqrt3}2|{+z}\rangle+\tfrac12|{-z}\rangle$ measured with $Z$: $\tfrac34$, $\tfrac14$; with $X$: $0.933$, $0.067$; with $Y$: $\tfrac12,\tfrac12$ (same state, different basis).

> [!pitfall] Probabilities of energy do not change in time
> For a time-independent $\hat H$, $|c_n|^2$ is constant under evolution; only relative phases change ([[Time Evolution of a Superposition]]).

Used in: [[QM03 States Operators and Measurement]]. Related: [[Born Rule]] · [[Eigenstate and Eigenvalue]] · [[Expectation Value]] · [[Superposition Principle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
