---
title: Completeness Relation
aliases: ["resolution of the identity", "completeness", "closure relation"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Completeness Relation

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (the content):** expansion $\Psi=\sum c_n\psi_n$ with $\sum|c_n|^2=1$ ([[PH2113_states_operators_notes.pdf#page=2|SO §2.1]]). · 🔵 **extra · beyond:** the operator statement and its uses.

> [!intuition] In one picture
> The rungs of the ladder together span the whole space: nothing is missing, so you may insert "a sum over all rungs" anywhere.

> [!key] Definition
> $\displaystyle\sum_n|n\rangle\langle n|=\hat 1$ (discrete), $\displaystyle\int|x\rangle\langle x|\,\mathrm dx=\hat 1$ (continuous). Hence $|\psi\rangle=\sum_nc_n|n\rangle$, $c_n=\langle n|\psi\rangle$, and $\sum|c_n|^2=\langle\psi|\psi\rangle$ (Parseval).

## Uses
- **Expansion and probabilities:** $c_n=\langle n|\psi\rangle$, $P(n)=|c_n|^2$.
- **Squares of operators:** $\langle m|\hat x^2|m\rangle=\sum_n\langle m|\hat x|n\rangle\langle n|\hat x|m\rangle=\sum_n|x_{mn}|^2$; for $m=3$: $3.5=3.5$ (checked).
- **Sum rules:** $\sum_n(E_n-E_m)|x_{nm}|^2=\hbar^2/2m$ ([[Sum Rules]]).
- **Two-level case:** $|{+z}\rangle\langle{+z}|+|{-z}\rangle\langle{-z}|=\hat 1$.

> [!pitfall] Completeness needs the whole set
> A truncated sum gives only an approximation, and finite matrices break $[\hat x,\hat p]=i\hbar$ ([[Number Basis]]). Completeness of the Hermite functions in $L^2(\mathbb R)$ is a theorem I did not prove.

Used in: [[QM06 The Oscillator Toolbox]] §2–§3. Related: [[Dirac Notation]] · [[Orthonormality of Eigenfunctions]] · [[Number Basis]] · [[Hilbert Space]] · [[Parseval-Plancherel Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
