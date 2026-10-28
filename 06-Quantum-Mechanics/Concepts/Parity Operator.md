---
title: Parity Operator
aliases: ["parity", "reflection operator"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Parity Operator

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_states_operators_notes.pdf#page=3|SO §3]], [[tutorial1.pdf#page=1|Tutorial I Q4]].

> [!intuition] In one picture
> Mirror the line; the states of a mirror-symmetric potential come out even or odd.

> [!key] Definition
> $\hat P\psi(x)=\psi(-x)$, eigenvalues $\pm1$ (even/odd). If $V(-x)=V(x)$ then $[\hat P,\hat H]=0$ and non-degenerate eigenfunctions are even or odd.

## Examples
$\hat P\cos kx=\cos kx$, $\hat P\sin kx=-\sin kx$; $e^{ikx}$ is not a parity eigenstate. Box about its centre: parity $(-1)^{n+1}$. Oscillator: $(-1)^n$.

> [!extra-beyond]- 🔵 Extra (beyond): a selection rule
> For same-parity states $\langle\psi_m|(x-\text{centre})|\psi_n\rangle=0$ (odd integrand): a superposition $\psi_1+\psi_3$ in a box has $\langle x\rangle=a/2$ for ever.

> [!pitfall] Degenerate levels
> $e^{\pm ikx}$ share an energy; the parity eigenstates $\cos,\sin$ are the right basis there.

Used in: [[QM03 States Operators and Measurement]], [[QM04 The Particle in a Box]]. Related: [[Degeneracy]] · [[Particle in a Box]] · [[Harmonic Oscillator]] · [[Node of a Wavefunction]].

## Added with QM06 (oscillator toolbox)
$\hat P\psi_n=(-1)^n\psi_n$ for the oscillator (since $H_n$ has parity $(-1)^n$); $\hat x$ is odd so $\langle x\rangle_n=0$ and the matrix element $\langle m|\hat x|n\rangle$ needs $m-n$ odd (the ladder gives the stronger $|m-n|=1$, [[Selection Rules]]). $\hat P$ equals the Fourier transform squared ($\tilde\psi_n\to(-i)^{2n}\psi_n$) and $\hat U(T/2)=-i\hat P$ ([[Time Evolution Operator]]). Unitary, with eigenvalues $\pm1$ ([[Unitary Operator]]).

> [!connection] Group theory used here
> Parity generates the cyclic group $C_2$ and the parity theorem is the decomposition into its two irreducible representations: [[GT03 Cyclic and Abelian Groups and Direct Products]], [[GT10 Symmetry Representations and Characters]]; see [[Where Groups Appear in the Vault]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
