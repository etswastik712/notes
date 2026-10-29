---
title: Coastline Instability
aliases: [Ashton-Murray instability, cape and spit formation, shoreline diffusion]
subject: landscapes
type: concept
scope: [extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/landscapes, type/concept, extra/beyond, src/book, src/own-notes, status/draft]
---
# Coastline Instability

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book** (the idea, A&A = Anderson and Anderson, *Geomorphology* (PDF page = printed page + 18). Ch. 16, printed pp.513-514) and 🔵 **extra · beyond** (the linear analysis, [[LS27 Coasts Beaches Deltas and Rocky Shores]] §3.1).

> [!intuition] In one picture
> Low-angle waves smooth a coast; high-angle waves make every bump grow into a cape or a spit.

> [!key] Definition and key results
> $\partial_ty=\kappa\,\partial_x^2y$, $\kappa=2Q_0\cos2\alpha_0/D$: positive below $45^\circ$, negative above. $Q_0=10^6$ m³/yr, $D=10$ m, $15^\circ$: 1.7e5 m²/yr, a 10 km bump decays in 15 yr; $60^\circ$: $-10^5$, a 10 km bump grows with e-fold time 25 yr. Checked against the full nonlinear flux (0.7104, 1.2182 in 20 yr). Ill-posed at short wavelengths; shadowing sets the minimum scale. Carolina capes $\sim150$ km apart.

> [!pitfall] Pitfall
> Negative diffusion blows up on the grid scale in a naive finite-difference model; real capes are limited by wave shadowing.

Used in: [[LS27 Coasts Beaches Deltas and Rocky Shores]]. Related: [[Longshore Drift]] · [[Littoral Cell Budget]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Diffusion Equation]] and [[THX1 Diffusion Random Walks and the Heat Equation]] (Thermodynamics): the same equation with the sign of $D$ reversed
- [[Bistability and Tipping Points]] and [[Fixed Points and Linear Stability]] (Foundations): linear stability of a uniform state, growth rate $|\kappa|k^2$
