---
title: Quantum Boltzmann Equation
aliases: ["Uehling-Uhlenbeck equation", "Boltzmann-Nordheim equation", "Pauli blocking in collisions"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Quantum Boltzmann Equation

> [!info] Source
> Uehling and Uhlenbeck (1933), recalled; [[SM08 Quantum Ensembles and Identical Particles]] §6; classical limit in [[SM04 Kinetic Theory and the Boltzmann Equation|SM04]].

> [!intuition] In one picture
> The Boltzmann collision integral with Pauli blocking (fermions) or Bose enhancement (bosons) of the final states.

> [!key] Key facts
> $C[f]=\int\mathrm d^3p_2\,\mathrm d\Omega\,\sigma_\Omega|\mathbf v_{12}|[f_1'f_2'(1+\epsilon f_1)(1+\epsilon f_2)-f_1f_2(1+\epsilon f_1')(1+\epsilon f_2')]$; H-function $\int[f\ln f-\epsilon(1+\epsilon f)\ln(1+\epsilon f)]$; stationary solutions $\ln\frac f{1+\epsilon f}=\alpha-\beta\varepsilon$, i.e. $f=1/(e^{\beta\varepsilon-\alpha}-\epsilon)$: **FD or BE**.

> [!pitfall] Classical limit
> For $f\ll1$ the factors $(1+\epsilon f)\to1$ and the equation reduces to SM04's; for degenerate fermions the available final states lie within $k_BT$ of the Fermi surface, which suppresses collisions at low $T$ ($\tau\propto T^{-2}$ in a Fermi liquid, recalled).

Used in: [[SM08 Quantum Ensembles and Identical Particles]]. Related: [[Boltzmann Equation]] · [[H-Theorem]] · [[Collision Invariants]] · [[Fermi-Dirac Distribution]] · [[Bose-Einstein Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
