---
title: Canonical Commutation Relation
aliases: ["[x,p]=iħ", "position-momentum commutator"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Canonical Commutation Relation

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_states_operators_notes.pdf#page=5|SO §5]], [[PH2113_matrices_expectation_uncertainty.pdf#page=3|MX §9]].

> [!intuition] In one picture
> Differentiating after multiplying by $x$ also differentiates the $x$: that is the whole origin of the uncertainty principle.

> [!key] Definition
> $[\hat x,\hat p]=i\hbar$. Derivation: $\hat x\hat p\psi=-i\hbar x\psi'$, $\hat p\hat x\psi=-i\hbar\psi-i\hbar x\psi'$, difference $i\hbar\psi$ for every $\psi$.

## Uses
- $\Delta x\,\Delta p\ge\tfrac12|i\hbar|=\hbar/2$ ([[Generalised Uncertainty Principle]]).
- $[\hat a_-,\hat a_+]=1$ for the oscillator follows from it ([[Ladder Operators]]).
- No $\hat x,\hat p$ can be finite matrices: $\mathrm{tr}[\hat x,\hat p]=0\ne\mathrm{tr}(i\hbar I)$.

> [!pitfall] A number, not zero
> Classical $xp-px=0$ for numbers; the quantum value is the constant $i\hbar$, the same for every state.

Used in: [[QM03 States Operators and Measurement]], [[QM05 The Harmonic Oscillator]]. Related: [[Commutator]] · [[Heisenberg Uncertainty Principle]] · [[Ladder Operators]] · [[Generalised Uncertainty Principle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
