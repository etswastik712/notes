---
title: Laplacian in Polar and Spherical Coordinates
aliases: ["polar Laplacian", "spherical Laplacian", "nabla squared in polar coordinates"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Laplacian in Polar and Spherical Coordinates

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[tutorial7.pdf|Tutorial VII]] Q1; [[Angular_momentum.pdf#page=3|Angular_momentum.pdf pp.3–4]]; [[Hydrogen_atom.pdf#page=2|hydrogen notes eq. 11]]

> [!intuition] In one picture
> The same operator written in coordinates that respect the symmetry: the radial part acquires 1/r (2D) or 2/r (3D) first-derivative terms, the angular part becomes angular momentum.

> [!key] Definition
> 2D: $\nabla^2=\partial_r^2+\frac1r\partial_r+\frac1{r^2}\partial_\phi^2$ (chain rule with $\partial_x r=\cos\phi$, $\partial_x\phi=-\sin\phi/r$, …). 3D: $\nabla^2=\frac1{r^2}\partial_r(r^2\partial_r)+\frac{1}{r^2\sin\theta}\partial_\theta(\sin\theta\,\partial_\theta)+\frac{1}{r^2\sin^2\theta}\partial_\varphi^2=\frac1{r^2}\partial_r(r^2\partial_r)-\frac{\hat L^2}{\hbar^2r^2}$.

Used in: [[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]], [[QM12 The Hydrogen Atom]]. Related: [[Angular Momentum Algebra]] · [[Radial Probability Density]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
