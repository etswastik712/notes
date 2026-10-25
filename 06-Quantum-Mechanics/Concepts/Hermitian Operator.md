---
title: Hermitian Operator
aliases: ["self-adjoint operator", "Hermitian"]
subject: qm
type: concept
scope: [taught, extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/book, extra/beyond, src/lecture-notes, status/draft]
---
# Hermitian Operator

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** allowed energies are real; $V$ real so that $\hat H$ is Hermitian ([[PH2113_Lecture9_FreeParticle_Ring_GeneralProperties.pdf#page=8|L9 §12]], [[PH2113_wavefunctions_potentials_schrodinger_Tutorial.pdf#page=1|Tutorial §2]]); no definition in the lecture notes. · 🟡 **extra · book:** definition and proofs (Griffiths Ch. 3). · 🔵 **extra · beyond:** the two short proofs below.

> [!intuition] In one picture
> The operators of measurable quantities: their answers are real numbers and their different answers are mutually exclusive.

> [!key] Definition
> $\hat A$ is Hermitian if $\int f^*(\hat Ag)\,\mathrm dx=\int(\hat Af)^*g\,\mathrm dx$ for all admissible $f,g$. Then eigenvalues are **real** and eigenstates of different eigenvalues are **orthogonal**.

## Why the two properties
> [!extra-beyond]- 🔵 Extra (beyond): proofs
> If $\hat A\phi=a\phi$: $\langle\phi|\hat A\phi\rangle=a\langle\phi|\phi\rangle$ and, by Hermiticity, also $=\langle\hat A\phi|\phi\rangle=a^*\langle\phi|\phi\rangle$; so $a=a^*$. If $\hat A\phi_a=a\phi_a$, $\hat A\phi_b=b\phi_b$: $b\langle\phi_a|\phi_b\rangle=\langle\phi_a|\hat A\phi_b\rangle=\langle\hat A\phi_a|\phi_b\rangle=a\langle\phi_a|\phi_b\rangle$, so $(a-b)\langle\phi_a|\phi_b\rangle=0$.

$\hat x$ and $\hat p=-i\hbar\,\mathrm d/\mathrm dx$ are Hermitian (integrate by parts, boundary terms vanish for normalisable states); $\hat H$ is Hermitian for real $V$. Complex $V$ breaks it and probability is not conserved ([[Probability Current]]).

> [!pitfall] Not every operator is an observable
> The ladder operators $\hat a_\pm$ are not Hermitian ($\hat a_\pm^\dagger=\hat a_\mp$): they change the state rather than measure it ([[Ladder Operators]]).

Used in: [[QM03 States Operators and Measurement]]. Related: [[Operator]] · [[Eigenstate and Eigenvalue]] · [[Orthonormality of Eigenfunctions]] · [[Measurement Postulate]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
