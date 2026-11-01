---
title: Péclet Number
aliases: [Peclet number, advection-diffusion ratio]
subject: foundations
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Péclet Number

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **Extra · beyond** ([[THX1 Diffusion Random Walks and the Heat Equation]] §6).

> [!intuition] In one picture
> The ratio of how far a medium carries stuff to how far diffusion spreads it.

> [!key] Definition and key results
> $Pe=vL/D$. $\ll1$: diffusion dominates; $\gg1$: advection dominates, thin diffusive boundary layers. Geotherm with $\varepsilon=1$ mm/yr over 10 km: 0.32; hillslope lowering 20 m/Myr over 100 m: 0.4; river salt: $\gg1$.

> [!pitfall] Pitfall
> The length $L$ is the scale you care about; the same system has different $Pe$ at different scales.

Used in: [[THX1 Diffusion Random Walks and the Heat Equation]], [[LSX1 Clocks in Rocks]]. Related: [[Diffusion Equation]] · [[Dimensional Analysis]] · [[Thermochronology]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Thermochronology]] (Landscapes): rapid exhumation advects heat upward ($Pe\gtrsim1$)
- [[LS24 Sediment Transport Mechanics]] (Landscapes): turbulent suspension is a diffusion-settling balance
- [[Delta Front]] (Landscapes): the delta front $z=z_0e^{-u_0x/K}$ is diffusion in a frame moving at $u_0$; its length $K/u_0$ is where the Péclet number is 1.
- [[Viscosity of a Gas]] (Thermodynamics): the kinematic viscosity $\nu=\eta/\rho$ computed from kinetic theory is the diffusivity of momentum, so the Reynolds number $UL/\nu$ is a Péclet number for momentum transport and the Prandtl number $\nu/D_T$ compares the two diffusivities.
