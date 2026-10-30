---
title: Thermal Conductivity of a Gas
aliases: ["gas heat conduction", "Eucken relation", "Fourier law for gases"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Thermal Conductivity of a Gas

> [!info] Source
> Huang §5.5 (pp. 104–108); Reif §12.4; Kardar §3.9 (eq. 3.119); [[SM04 Kinetic Theory and the Boltzmann Equation]] §10.

> [!intuition] In one picture
> Hot molecules from the hot side cross to the cold side with more kinetic energy than the cold molecules crossing back: heat is energy diffusing along a temperature gradient.

> [!key] Key facts
> $\mathbf h=-\kappa\nabla T$; single time: $\kappa=\frac52\frac{nk_B^2T\tau_K}m=\frac52\frac{k_B}m\eta$; exact first approx., monatomic: $\kappa=\frac{15}4\frac{k_B}m\eta$ (Eucken factor $\kappa/\eta c_v=\tfrac52$); diatomic: modified Eucken $\eta(c_v+\frac94R/M)$. Independent of density for $\mathrm{Kn}\lesssim0.1$; below it $\kappa\propto P$ (vacuum flask).

> [!example] Numbers (recomputed)
> From $\eta$ alone: He $0.155$ (meas. $0.156$), Ar $0.01772$ (0.01772), Xe $0.00551$ (0.00569) W m$^{-1}$K$^{-1}$. Thermal diffusivity of air $D_T=2.2\times10^{-5}$ m$^2$s$^{-1}$.

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Fick's and Fourier's Laws]] · [[Prandtl Number]] · [[Viscosity of a Gas]] · [[Heat Capacity]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
