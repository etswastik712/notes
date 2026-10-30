---
title: Liouville's Theorem
aliases: ["Liouville theorem", "incompressible phase-space flow"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Liouville's Theorem

> [!info] Source
> Kardar §3.2 (p.59); [[SM02 Phase Space Liouville and the Microcanonical Ensemble]] §2.

> [!intuition] In one picture
> Hamiltonian flow moves a blob of initial conditions around phase space like an incompressible fluid: it can be stretched into a filament, but its volume is conserved.

> [!key] Key facts
> $\mathrm d\rho/\mathrm dt=0$ along trajectories, i.e. $\partial_t\rho=-\{\rho,\mathcal H\}$, because the flow field $(\dot q_i,\dot p_i)$ has zero divergence ($\partial^2\mathcal H/\partial q\partial p$ cancels). Stationary densities: $\rho=f(\mathcal H)$ and functions of other conserved quantities.

> [!example] A pendulum blob (recomputed)
> A disc of radius 0.35 in the $(q,p)$ plane stays at area $0.3848$ for $t=0\ldots32$ while it is sheared into a spiral (amplitude-dependent period). An oscillator (period independent of amplitude) only rotates it, never mixes it.

*Consequences:* the fine-grained Gibbs entropy $-k\int\rho\ln\rho$ is constant; the second law is a *coarse-grained* statement; Poincaré recurrence is not forbidden but takes $\sim10^{6N}$ molecular times (estimate). Quantum version: $\partial_t\hat\rho=-\tfrac i\hbar[\hat{\mathcal H},\hat\rho]$.

Used in: [[SM02 Phase Space Liouville and the Microcanonical Ensemble]]. Related: [[Phase Space]] · [[Ergodic Hypothesis]] · [[Microcanonical Ensemble]] · [[Phase Space Picture of the Oscillator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
