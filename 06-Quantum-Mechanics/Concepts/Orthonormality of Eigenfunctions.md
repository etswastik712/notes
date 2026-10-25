---
title: Orthonormality of Eigenfunctions
aliases: ["orthogonality", "orthonormal basis"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Orthonormality of Eigenfunctions

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Particle_in_a_box.pdf#page=8|box lecture p.8]], [[PH2113_states_operators_notes.pdf#page=2|SO §2.1]].

> [!intuition] In one picture
> Different energy states do not overlap: like perpendicular axes.

> [!key] Definition
> $\int\psi_m^*\psi_n\,\mathrm dx=\delta_{mn}$. Then $\Psi=\sum c_n\psi_n$ has $c_n=\int\psi_n^*\Psi\,\mathrm dx$ and $\sum|c_n|^2=1$.

## Proofs
Box: $\sin A\sin B=\tfrac12[\cos(A-B)-\cos(A+B)]$ integrates to zero over $[0,a]$ when $m\ne n$. Ring: $\int_0^Le^{i(k_n-k_m)x}\mathrm dx=0$. General: eigenfunctions of a Hermitian operator with different eigenvalues are orthogonal ([[Hermitian Operator]]).

> [!pitfall] Degenerate states
> Two states with the same energy need not be orthogonal automatically; choose an orthonormal pair ($\cos$, $\sin$ or $e^{\pm ikx}$).

Used in: [[QM03 States Operators and Measurement]], [[QM04 The Particle in a Box]]. Related: [[Normalisation of a Wavefunction]] · [[Hermitian Operator]] · [[Measurement Postulate]] · [[Particle in a Box]].

## Added with QM06 (oscillator toolbox)
**Why different energies are orthogonal** (Tutorial III Q3): for a Hermitian $\hat H$ and $E_n\ne E_m$, $(E_n-E_m)\int\psi_m^*\psi_n\,\mathrm dx=0$ (after showing $E$ real). **Oscillator:** $\langle m|n\rangle=0$ for $0\le m<n\le6$ (`sympy`) and by ladders via $\hat a\psi_0=0$. **Hermite weight:** the polynomials are orthogonal only with $e^{-\xi^2}$ ([[Orthogonal Polynomials]]). **Degenerate levels** need [[Gram-Schmidt Orthogonalisation]]. **Parseval:** $\sum|c_n|^2=\langle\psi|\psi\rangle$ ([[Completeness Relation]], [[Parseval-Plancherel Theorem]]). See [[QM05 The Harmonic Oscillator]] §10.

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
