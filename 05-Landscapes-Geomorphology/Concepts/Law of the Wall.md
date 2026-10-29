---
title: Law of the Wall
aliases: [log law, logarithmic velocity profile, von Karman law]
subject: landscapes
type: concept
scope: [extra-book]
by: [book, own-notes]
status: draft
tags: [subject/landscapes, type/concept, extra/book, src/book, src/own-notes, status/draft]
---
# Law of the Wall

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** A&A = Anderson and Anderson, *Geomorphology* (PDF page = printed page + 18). Ch. 12, printed pp.383–388 ([[LS21 River Hydraulics and Hydraulic Geometry]] §3).

> [!intuition] In one picture
> Near a wall the eddies cannot be bigger than their distance from it, so the effective viscosity grows linearly with height and the velocity grows as the logarithm.

> [!key] Definition and key results
> $U(z)=\dfrac{u_*}{\kappa}\ln\dfrac z{z_0}$, $\kappa\approx0.4$, $u_*=\sqrt{\tau_b/\rho}$; $z_0\approx D/30$ (Nikuradse). From $\tau_b=\rho\kappa u_*z\,dU/dz$. Depth mean $\langle U\rangle=\frac{u_*}\kappa[\ln(H/z_0)-1]$, found at $z=H/e$ (six-tenths rule).

> [!pitfall] Pitfall
> $z_0$ is a fitting length (where the extrapolated profile reaches zero), not a physical height; $U=0$ at $z=0$ is impossible for a log.

Used in: [[LS21 River Hydraulics and Hydraulic Geometry]], [[LS24 Sediment Transport Mechanics]] (entrainment, Rouse profile). Related: [[Shear Velocity]] · [[Manning Equation]] · [[Shields Criterion]] · [[Rouse Profile]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] (Climate): the same logarithmic surface-layer wind profile and eddy viscosity in the atmospheric boundary layer
- [[Dimensional Analysis]] (Foundations): $u_*$ is the only velocity scale built from $\tau_b$ and $\rho$
