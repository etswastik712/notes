---
title: Fick's and Fourier's Laws
aliases: [Fick's law, Fourier's law of conduction, flux-gradient law]
subject: thermo
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/thermo, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Fick's and Fourier's Laws

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **Extra · beyond** ([[THX1 Diffusion Random Walks and the Heat Equation]] §2.2; Fourier's law appears in the climate and thermodynamics chapters as heat conduction).

> [!intuition] In one picture
> Stuff flows from where there is more to where there is less, in proportion to the steepness.

> [!key] Definition and key results
> $\mathbf J=-D\nabla c$ (Fick), $\mathbf q=-k\nabla T$ (Fourier), soil flux $q=-\kappa_h\nabla z$, alluvial $Q_s=-\alpha Q\,\partial_xz$. Combined with conservation: $\partial_tu=-\nabla\cdot\mathbf J$ gives the diffusion equation; $\kappa_T=k/\rho c_p\approx10^{-6}$ m²/s for rock.

> [!pitfall] Pitfall
> A flux proportional to the gradient is a *model*: it fails for steep slopes (soil), turbulent flow with a threshold, and non-local transport.

Used in: [[THX1 Diffusion Random Walks and the Heat Equation]]. Related: [[Diffusion Equation]] · [[Heat and Work]] · [[Kinetic Theory of Gases]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[LS12 Hillslope Transport and the Diffusion Equation]] (Landscapes): soil creep as a Fick law
- [[Darcy's Law and Hydraulic Conductivity]] (Landscapes): Darcy's law $q=-K\nabla h$ is a third instance of the flux-gradient law (after Fick and Fourier), with the conductivity built from a pore-scale Poiseuille flow.

## Continued in Part II (added 2026-10-30)
- Derived from the Boltzmann equation: $\mathbf h=-\kappa\nabla T$ with $\kappa=\tfrac{15}4\tfrac{k_B}m\eta$ (exact first approximation), diffusion $D\sim\bar v\lambda/3$; tests against five noble gases: [[SM04 Kinetic Theory and the Boltzmann Equation]] §10 ([[Thermal Conductivity of a Gas]]).
