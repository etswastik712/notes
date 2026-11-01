---
title: Viscosity of a Gas
aliases: ["gas viscosity", "Maxwell viscosity law", "momentum diffusion"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Viscosity of a Gas

> [!info] Source
> Huang §5.6 (pp. 108–110); Reif §12.3 (pp. 476–479); Kardar §3.9; [[SM04 Kinetic Theory and the Boltzmann Equation]] §10.

> [!intuition] In one picture
> Fast molecules from a faster layer cross into a slower one carrying extra momentum: friction is momentum diffusing across the flow.

> [!key] Key facts
> $P_{xy}=-\eta\,\partial_yu_x$, $\eta=nk_BT\tau$ (single time) $\simeq\frac13nm\bar v\lambda$ (crude) $=\frac5{16}\sqrt{mk_BT/\pi}/d^2$ (exact first approx., hard spheres). **Independent of density** ($\tau\propto1/n$) for $\mathrm{Kn}\lesssim0.1$; $\propto\sqrt{m}$, $\propto\sqrt T$ (hard spheres). Kinematic $\nu=\eta/\rho$: shear modes decay at $\nu k^2$.

> [!example] Air (recomputed)
> $\eta\approx18.5$ µPa s; $\nu=1.57\times10^{-5}$ m$^2$s$^{-1}$; He $19.9$, Ne $31.8$, Ar $22.7$, N$_2$ $17.9$ µPa s (recalled). Maxwell verified the density independence by damping a pendulum.

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Navier-Stokes Equations]] · [[Thermal Conductivity of a Gas]] · [[Relaxation Time Approximation]] · [[Mean Free Path]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Péclet Number]] (Foundations): the kinematic viscosity $\nu=\eta/\rho$ computed from kinetic theory is the diffusivity of momentum, so the Reynolds number $UL/\nu$ is a Péclet number for momentum transport and the Prandtl number $\nu/D_T$ compares the two diffusivities.
