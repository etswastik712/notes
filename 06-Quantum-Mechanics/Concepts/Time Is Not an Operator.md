---
title: Time Is Not an Operator
aliases: ["no time operator", "Pauli theorem on time"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Time Is Not an Operator

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_states_operators_notes.pdf#page=11|SO §9.3]].

> [!intuition] In one picture
> $x$, $p$ and $E$ describe the system at an instant; $t$ labels the instants themselves.

> [!key] Definition
> There is no self-adjoint $\hat T$ with $[\hat T,\hat H]=i\hbar$ if the spectrum of $\hat H$ is bounded below (Pauli).

## Argument
If $[\hat H,\hat T]=-i\hbar$ then $[\hat H,e^{ia\hat T/\hbar}]=a\,e^{ia\hat T/\hbar}$, so $e^{ia\hat T/\hbar}|E\rangle$ has energy $E+a$ for **every** real $a$: the spectrum would be unbounded below. But the ring has $E_0=0$ and the box $E_1>0$.

> [!pitfall] This does not forbid time-energy tradeoffs
> Statements like $\Delta E\,\Delta t\gtrsim\hbar$ concern the timescale over which an observable changes, not an operator $\hat T$; they are not covered by the commutator bound.

Used in: [[QM03 States Operators and Measurement]]. Related: [[Canonical Commutation Relation]] · [[Zero-Point Energy]] · [[Heisenberg Uncertainty Principle]] · [[Operator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
