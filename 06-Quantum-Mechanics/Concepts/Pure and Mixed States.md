---
title: Pure and Mixed States
aliases: [pure ensemble, mixed ensemble, coherent superposition versus mixture]
subject: qm
type: concept
scope: [extra-book]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, src/book, src/own-notes, status/draft]
---
# Pure and Mixed States

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** Sakurai §3.4.1–3.4.2 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=189|PDF p.189 ff.]]); the example is in [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §6.

> [!intuition] In one picture
> A pure state is *one* ket (maximal knowledge, still probabilistic outcomes); a mixture is a classical lottery over kets.

> [!key] Definition and key results
> Pure: $\rho=|\psi\rangle\langle\psi|$, $\rho^2=\rho$, $|\mathbf r|=1$. Mixed: $\rho^2\ne\rho$, $|\mathbf r|<1$. The off-diagonal elements (coherences) distinguish $\frac1{\sqrt2}(|{+z}\rangle+|{-z}\rangle)$ from the 50:50 mixture: the former gives $S_x=+$ with certainty, the latter $\langle\sigma_x\rangle=0$.

The oven beam is maximally mixed (every analyser sees 50:50, whatever its axis). A pure state $|{+z}\rangle$ also gives 50:50 along $x$, but for a different reason: superposition, not ignorance. Interference needs coherence.

> [!pitfall] Pitfall
> Mixed does not mean "unknown pure state": half of an entangled pair is mixed although the whole pair is pure.

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §6. Related: [[Density Matrix]] · [[Superposition Principle]] · [[Measurement Postulate]] · [[Entanglement]].

## Continued in Part II (added 2026-11-02)
- Purity of a thermal spin-½ and the Bloch vector $\tanh(\mu B/k_BT)$: [[SM08 Quantum Ensembles and Identical Particles]] §2.1 ([[Quantum Ensembles]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
