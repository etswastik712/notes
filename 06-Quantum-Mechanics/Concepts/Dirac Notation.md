---
title: Dirac Notation
aliases: ["bra-ket notation", "bras and kets", "ket", "bra"]
subject: qm
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Dirac Notation

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (two-level kets and the dictionary):** [[PH2113_matrices_expectation_uncertainty.pdf|MX]] (state $|\psi\rangle=(a,b)^{\mathsf T}$, "wave mechanics dictionary"). · 🔵 **extra · beyond:** outer products, projectors and the number-basis usage.

> [!intuition] In one picture
> A state is an arrow (ket) in a vector space, a bra is the matching row vector, and $\langle\phi|\psi\rangle$ is their dot product.

> [!key] Definition
> $|\psi\rangle\leftrightarrow\psi(x)$; $\langle\phi|\psi\rangle=\int\phi^*\psi\,\mathrm dx$; $\langle\psi|\hat A|\psi\rangle=\int\psi^*\hat A\psi\,\mathrm dx$; $\langle\phi|\psi\rangle^*=\langle\psi|\phi\rangle$; normalised: $\langle\psi|\psi\rangle=1$.

## Dictionary
| Wave mechanics | Dirac |
|---|---|
| $\psi(x)$ | $\lvert\psi\rangle$ |
| $\int\phi^*\psi\,\mathrm dx$ | $\langle\phi\vert\psi\rangle$ |
| $\hat A\phi_a=a\phi_a$ | $\hat A\lvert a\rangle=a\lvert a\rangle$ |
| $c_n=\int\phi_n^*\psi\,\mathrm dx$ | $c_n=\langle n\vert\psi\rangle$ |
| $\langle A\rangle=\int\psi^*\hat A\psi$ | $\langle\psi\vert\hat A\vert\psi\rangle$ |

## Outer products and projectors
$|\phi\rangle\langle\psi|$ is an operator ($|\chi\rangle\mapsto|\phi\rangle\langle\psi|\chi\rangle$). $\hat P_n=|n\rangle\langle n|$ projects on rung $n$, $\hat P_n^2=\hat P_n$, and $\sum_n\hat P_n=\hat 1$ ([[Completeness Relation]]). The measurement postulate says: probability $|\langle a|\psi\rangle|^2=\langle\psi|\hat P_a|\psi\rangle$, and the state afterwards is $\hat P_a|\psi\rangle/\|\hat P_a|\psi\rangle\|$.

## Matrix elements
$A_{mn}=\langle m|\hat A|n\rangle$; for the adjoint, $(A^\dagger)_{mn}=A_{nm}^*$ ([[Hermitian Conjugate]]).

> [!pitfall] A bra is not a function
> $\langle\phi|$ is the *conjugate* of $|\phi\rangle$; moving a state across the bar conjugates it, which is why $\langle\phi|\hat A\psi\rangle=\langle\hat A^\dagger\phi|\psi\rangle$ carries a dagger.

Used in: [[QM03 States Operators and Measurement]], [[QM06 The Oscillator Toolbox]] §2. Related: [[Number Basis]] · [[Completeness Relation]] · [[Hermitian Conjugate]] · [[Measurement Postulate]] · [[Eigenstate and Eigenvalue]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
