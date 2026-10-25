---
title: Gram-Schmidt Orthogonalisation
aliases: ["Gram Schmidt", "orthonormalising a degenerate eigenspace"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Gram-Schmidt Orthogonalisation

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond.**

> [!intuition] In one picture
> Take vectors one at a time and subtract the part already covered by the earlier ones.

> [!key] Definition
> $\displaystyle e_k\ \propto\ v_k-\sum_{j<k}\langle e_j|v_k\rangle\,e_j$, then normalise. Applied to an eigenspace of a Hermitian operator it gives an orthonormal basis of the *same* eigenspace.

## Where it is needed
Eigenfunctions of different eigenvalues are automatically orthogonal ([[Orthonormality of Eigenfunctions]], Tutorial III Q3), but within a **degenerate** level orthogonality is a choice. Example: on the ring $e^{\pm ik_nx}$ are already orthogonal; $\cos k_nx$ and $\sin k_nx$ are another orthogonal pair in the same eigenspace. In the 3-D oscillator a level of degeneracy $g_N$ needs $g_N$ orthonormal states.

> [!pitfall] Order dependence
> Different orderings of the $v_k$ give different (equally valid) orthonormal bases.

Used in: [[QM05 The Harmonic Oscillator]] §10, [[QM06 The Oscillator Toolbox]]. Related: [[Degeneracy]] · [[Orthogonal Polynomials]] · [[Hilbert Space]] · [[Isotropic Oscillator and Degeneracy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
