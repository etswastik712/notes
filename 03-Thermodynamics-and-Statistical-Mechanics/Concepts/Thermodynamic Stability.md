---
title: Thermodynamic Stability
aliases: ["stability conditions", "stability of equilibrium"]
subject: thermo
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, extra/beyond, src/lecture-notes, status/draft]
---
# Thermodynamic Stability

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[97dcd8dee3d3301cd7c27745b17b10b5_MIT8_333F13_Lec4.pdf#page=1|MIT L4 §I.I]]. · 🔵 **extra · beyond:** the van der Waals numbers.

> [!intuition] In one picture
> A stable system pushes back against any fluctuation: more entropy would require leaving equilibrium.

> [!key] Definition
> $\delta T\,\delta S+\delta J\!\cdot\!\delta x+\delta\mu\,\delta N\ge0$. Hence $C_x\ge0$, $\kappa_T\ge0$, the matrix $(\partial J_i/\partial x_j)_T$ positive definite; critical point: $\partial_VP=\partial_V^2P=0$, $\partial_V^3P<0$.

## Example
Van der Waals CO$_2$: unstable region ($\partial P/\partial V>0$) $95$–$185$ cm$^3$ mol$^{-1}$ at 280 K, $113$–$147$ at 300 K, closing at $T_c=304$ K. Unstable states separate into liquid and vapour.

> [!pitfall] Positive diagonal is necessary, not sufficient
> The response matrix must be **positive definite** (all eigenvalues positive).

Used in: [[TH05 Potentials Maxwell Relations Stability and the Third Law]]. Related: [[Response Functions]] · [[Equation of State]] · [[Third Law of Thermodynamics]] · [[Thermodynamic Equilibrium]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
