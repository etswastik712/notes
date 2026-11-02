---
title: Identical Particles
aliases: ["indistinguishable particles", "symmetrisation postulate", "bosons and fermions", "exchange symmetry"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Identical Particles

> [!info] Source
> Kardar §7.1 (pp. 181–184); Pathria §5.4 (pp. 128–132); [[SM08 Quantum Ensembles and Identical Particles]] §4.

> [!intuition] In one picture
> Particles of one species are not labelled: exchanging two leaves the physics unchanged, so the wave function is either symmetric (bosons) or antisymmetric (fermions).

> [!key] Key facts
> $\hat P\psi=\psi$ (bosons), $(-1)^P\psi$ (fermions) for all $P\in S_N$; states are labelled by occupation numbers $\{n_k\}$ ($n_k\in\{0,1\}$ for fermions); normalisation $\sqrt{N!\prod n_k!}$ (bosons), $\sqrt{N!}$ (fermions). Counting in $g$ states: bosons $\binom{N+g-1}N$, fermions $\binom gN$, classical $g^N/N!$ valid for $g\gg N^2$.

> [!example] Counting (recomputed)
> $N=3$, $g=10$: 1000 distinguishable, 220 bosonic, 120 fermionic states against $g^N/N!=166.7$. Two particles in a box, levels 1 and 2: $\langle(x_1-x_2)^2\rangle/L^2=0.038$ (symmetric), $0.103$ (distinguishable), $0.168$ (antisymmetric).

Used in: [[SM08 Quantum Ensembles and Identical Particles]]. Related: [[Spin-Statistics Theorem]] · [[Slater Determinant]] · [[Pauli Exclusion Principle]] · [[Symmetric Group]] · [[Gibbs Paradox]] · [[Number Basis]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Exchangeability]] (Probability): exchangeable random variables have a joint law invariant under every permutation, the probabilistic analogue of a symmetric many-boson wave function; de Finetti's theorem (mixtures of i.i.d. laws) has the quantum de Finetti theorem as counterpart.
