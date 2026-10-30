---
title: Phase Space
aliases: ["Gamma space", "state space of a gas"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Phase Space

> [!info] Source
> Kardar §3.1 (p.57); [[SM02 Phase Space Liouville and the Microcanonical Ensemble]] §1.

> [!intuition] In one picture
> A single point that records the position and momentum of every particle: one snapshot of the whole system.

> [!key] Key facts
> $\Gamma=\mathbb R^{6N}$ for $N$ particles in 3-D; microstate $\mu=(\mathbf p_1,\dots,\mathbf p_N,\mathbf q_1,\dots,\mathbf q_N)$ moving by Hamilton's equations; a macrostate is a region. Measure $\mathrm d\Gamma=\prod\mathrm d^3p\,\mathrm d^3q/(N!\,h^3)$ counts quantum states (one per $h^{3N}$) and treats identical particles as indistinguishable.

> [!example] One oscillator
> $\mathcal H=p^2/2m+\tfrac12m\omega^2q^2$: the energy curve is an ellipse of area $2\pi E/\omega$, so the number of states below $E$ is area$/h=E/\hbar\omega$: one state per $\hbar\omega$ ([[QM05 The Harmonic Oscillator]]).

Used in: [[SM02 Phase Space Liouville and the Microcanonical Ensemble]]. Related: [[Liouville's Theorem]] · [[Phase Space Picture of the Oscillator]] · [[Density of States]] · [[Microcanonical Ensemble]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
