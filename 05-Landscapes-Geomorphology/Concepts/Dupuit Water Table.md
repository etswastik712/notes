---
title: Dupuit Water Table
aliases: [Dupuit approximation, water-table mound, Boussinesq equation, groundwater discharge]
subject: landscapes
type: concept
scope: [extra-book]
by: [book, own-notes]
status: draft
tags: [subject/landscapes, type/concept, extra/book, src/book, src/own-notes, status/draft]
---
# Dupuit Water Table

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** A&A = Anderson and Anderson, *Geomorphology* (PDF page = printed page + 18). Ch. 11, printed pp.358–361 ([[LS25 Water in the Landscape]] §5).

> [!intuition] In one picture
> Groundwater piles up between two rivers into a smooth mound, steeper where more recharge has to be carried away.

> [!key] Definition and key results
> $S_y\partial_tH=\partial_x(KH\partial_xH)+I$. Steady Dupuit solution: $H^2=H_0^2+(H_L^2-H_0^2)x/L+(I/K)x(L-x)$ (an ellipse); crest $\sqrt{H_0^2+IL^2/4K}$; discharge to each stream $IL/2$. Linearised: diffusion with $D_H=K\bar H/S_y$, relaxation time $L^2/\pi^2D_H$ (1.6 yr for $L=500$ m, $K=10^{-5}$ m/s, $\bar H=10$ m, $S_y=0.2$).

> [!pitfall] Pitfall
> Dupuit assumes nearly horizontal flow (interfluve much longer than the water table is high); it fails near the stream bank.

Used in: [[LS25 Water in the Landscape]]. Related: [[Darcy's Law and Hydraulic Conductivity]] · [[Overland Flow and Runoff Mechanisms]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[THX1 Diffusion Random Walks and the Heat Equation]] and [[Diffusion Equation]] (Thermodynamics): the linearised water table is the heat equation
- [[LS12 Hillslope Transport and the Diffusion Equation]] (Landscapes): the steady mound is the same parabola/ellipse family as a steady hillslope
