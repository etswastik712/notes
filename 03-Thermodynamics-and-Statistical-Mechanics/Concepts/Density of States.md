---
title: Density of States
aliases: ["g(E)", "Omega(E)", "number of states per energy"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Density of States

> [!info] Source
> Pathria §2.3; Kardar §4.2; [[SM02 Phase Space Liouville and the Microcanonical Ensemble]] §4, §6.

> [!intuition] In one picture
> How many microstates sit in each energy window; it grows steeply with $E$ for a gas and is what the Boltzmann factor competes with.

> [!key] Key facts
> $\Omega(E)=\mathrm d\Sigma/\mathrm dE$ with $\Sigma(E)$ the number of states below $E$. Ideal gas: $\Sigma\propto V^NE^{3N/2}$, $\Omega\propto E^{3N/2-1}$. One free particle in a box: $g(E)=\frac V{4\pi^2}\big(\frac{2m}{\hbar^2}\big)^{3/2}\sqrt E$ (no spin). 1-D oscillator: constant, $1/\hbar\omega$. $Z(\beta)=\int\Omega(E)e^{-\beta E}\mathrm dE$ is its Laplace transform.

> [!example] Counting (recomputed)
> One He atom in 1 litre with $E=\tfrac32k_BT$ at 300 K has $\Sigma=1.08\times10^{28}$ states, equal to $1.38\,V/\lambda^3$ ($=\tfrac{4\pi}3(\tfrac3{2\pi})^{3/2}V/\lambda^3$).

Used in: [[SM02 Phase Space Liouville and the Microcanonical Ensemble]], [[SM03 The Canonical Ensemble]]. Related: [[Microcanonical Ensemble]] · [[Partition Function]] · [[Laplace Transform]] · [[Thermal Wavelength]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
