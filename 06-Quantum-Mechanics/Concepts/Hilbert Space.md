---
title: Hilbert Space
aliases: ["state space", "L2", "square-integrable functions", "l2"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Hilbert Space

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond** (the analysis side is in [[PA06 The Real Numbers and Sequences]] and [[PA07 Metric and Topological Spaces]]).

> [!intuition] In one picture
> The arena of quantum mechanics: a vector space with a dot product, in which Cauchy sequences always converge.

> [!key] Definition
> A complex vector space with inner product $\langle\phi|\psi\rangle$ that is **complete** in the induced norm $\|\psi\|=\sqrt{\langle\psi|\psi\rangle}$. Wave mechanics: $L^2(\mathbb R)$, the functions with $\int|\psi|^2<\infty$. Number basis: $\ell^2$, sequences $(c_n)$ with $\sum|c_n|^2<\infty$. Two-level system: $\mathbb C^2$.

## Why completeness matters
Limits of sequences of states (e.g. a packet being squeezed, or partial sums $\sum_{n\le N}c_n|n\rangle$) must stay in the space for expansions to make sense. The inner product defines a norm and a **metric** $d(\phi,\psi)=\|\phi-\psi\|$, so Hilbert spaces are complete metric spaces (the subject of PA06–PA07).

> [!pitfall] Plane waves and $\delta$ are not in the space
> They are not square-integrable; they live in a larger "rigged" space and are handled by delta normalisation ([[Delta-Function Normalisation]]).

Used in: [[QM06 The Oscillator Toolbox]] §2. Related: [[Completeness Relation]] · [[Dirac Notation]] · [[Admissible Wavefunction]] · [[Parseval-Plancherel Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Cauchy Sequence]] (Analysis): a Hilbert space is a complete inner-product space: completeness means every Cauchy sequence in the norm converges, which is what licenses eigenfunction expansions.
- [[Metric Space]] (Analysis): the norm $\|\psi\|=\sqrt{\langle\psi|\psi\rangle}$ gives the metric $d(\psi,\phi)=\|\psi-\phi\|$, so a Hilbert space is a complete metric space with extra (inner-product) structure.
