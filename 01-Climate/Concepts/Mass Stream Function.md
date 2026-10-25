---
title: Mass Stream Function
aliases: [meridional overturning streamfunction, streamfunction]
subject: climate
type: concept
scope: [taught, extra-book, extra-beyond]
by: [suhas-post]
status: draft
tags: [subject/climate, type/concept, taught, extra/book, extra/beyond, src/suhas-post, status/draft]
---
# Mass Stream Function

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!key] Definition
> For a zonal-mean circulation, the **mass stream function** is
> $$\psi(\varphi,p)=\frac{2\pi a\cos\varphi}{g}\int_0^{p}[v]\,\mathrm dp' \qquad[\mathrm{kg\,s^{-1}}]$$
> where $[v]$ is the zonal-mean northward wind. It is the **net northward mass flux across a latitude circle above pressure level $p$**. Contours of $\psi$ are the streamlines of the meridional circulation: flow runs *along* them, faster where they are closer together.

- **Boundary values:** $\psi=0$ at the top ($p=0$) and at the ground (no net mass transport across a latitude circle in steady state).
- **Sign:** $\psi>0$ means northward flux above and southward below: a **clockwise** circle in a latitude–height plot (north to the right): the Northern-Hemisphere Hadley cell. $\psi<0$ is anticlockwise.
- **Winds from $\psi$** (pressure coordinates): $[v]=\dfrac{g}{2\pi a\cos\varphi}\dfrac{\partial\psi}{\partial p}$, $[\omega]=-\dfrac{g}{2\pi a^2\cos\varphi}\dfrac{\partial\psi}{\partial\varphi}$ (these satisfy mass continuity automatically).
- Marshall & Plumb use $\chi$ in height coordinates with $v=-(\rho a\cos\varphi)^{-1}\partial\chi/\partial z$, $w=(\rho a^2\cos\varphi)^{-1}\partial\chi/\partial\varphi$, units $10^9$ kg s⁻¹ (Sverdrups).

Used in [[CL11 Mean Meridional Circulation and Angular Momentum]]; see [[Hadley Cell]], [[Ferrel Cell and Polar Cell]]. The idea is the two-dimensional stream function of fluid mechanics (compare incompressible flow: constant $\psi$ along streamlines).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
