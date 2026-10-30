---
title: Navier-Stokes Equations
aliases: ["Navier-Stokes", "viscous fluid equations", "compressible Navier-Stokes"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Navier-Stokes Equations

> [!info] Source
> Kardar §3.9; Huang §5.7–5.8 (pp. 111–117); [[SM04 Kinetic Theory and the Boltzmann Equation]] §11.

> [!intuition] In one picture
> Newton's second law for a fluid parcel: acceleration $=$ pressure force $+$ viscous force $+$ body force.

> [!key] Key facts
> $\rho\,D_t\mathbf u=-\nabla P+\eta\nabla^2\mathbf u+\tfrac13\eta\nabla(\nabla\cdot\mathbf u)+\rho\mathbf F$ and $\tfrac32nk_B\,D_tT=-P\nabla\cdot\mathbf u+\nabla\cdot(\kappa\nabla T)+\Phi$; derived from the Boltzmann equation with $P_{\alpha\beta}=P\delta_{\alpha\beta}-\eta(\partial_\alpha u_\beta+\partial_\beta u_\alpha-\tfrac23\delta_{\alpha\beta}\nabla\cdot\mathbf u)$, $\mathbf h=-\kappa\nabla T$. Applies for $\mathrm{Kn}\lesssim0.01$.

> [!example] Use in the vault
> Rivers ([[LS21 River Hydraulics and Hydraulic Geometry]]), Ekman friction and the Hadley cell ([[CL13 Horizontal Motion - Geostrophic Balance and Friction]], [[CL11 Mean Meridional Circulation and Angular Momentum]]) all use this equation with a turbulent (eddy) viscosity. Air past a 1 m body at 10 m s$^{-1}$: $\mathrm{Re}=6.4\times10^5$, $\mathrm{Ma}=0.029$.

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Euler Equations]] · [[Viscosity of a Gas]] · [[Hydrodynamic Modes]] · [[Knudsen Number]] · [[Prandtl Number]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
