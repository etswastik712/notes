---
title: Thermal Wind
aliases: [thermal wind equation, thermal wind balance]
subject: climate
type: concept
scope: [taught, extra-book, extra-beyond]
by: [suhas-post]
status: draft
tags: [subject/climate, type/concept, taught, extra/book, extra/beyond, src/suhas-post, status/draft]
---
# Thermal Wind

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the idea that jet strength is tied to the latitudinal temperature gradient (21 Oct p12; M&P §5.4 closing paragraph) · 🟡 **extra book:** the equation (Webster & Fasullo p.8, eq. [11]) · 🔵 **extra:** derivation, numbers, weak-temperature-gradient tropics

> [!intuition] In one picture
> Warm columns are puffed up, cold columns squashed, so every pressure surface tilts poleward and the tilt **grows with height** like a staircase of ever-steeper ramps. A steeper ramp is a stronger pressure-gradient force, hence a stronger geostrophic wind: the wind must increase upward wherever the temperature changes horizontally.

> [!key] Definition
> The **thermal wind** is the *vertical shear of the geostrophic wind* produced by a horizontal temperature gradient, a direct consequence of geostrophic and hydrostatic balance:
> $$\frac{\partial u_g}{\partial z}=-\frac{g}{fT}\frac{\partial T}{\partial y},\qquad \frac{\partial v_g}{\partial z}=\frac{g}{fT}\frac{\partial T}{\partial x}\qquad\Big(\text{or }\ \frac{\partial\mathbf V_g}{\partial\ln p}=\frac{R}{f}\,\hat{\mathbf k}\times\nabla_pT\Big).$$

- **Derivation** (pressure coordinates): $u_g=-(g/f)\,\partial Z/\partial y|_p$ and the hypsometric equation $\partial Z/\partial\ln p=-RT/g$ give $\partial u_g/\partial\ln p=(R/f)\,\partial T/\partial y$; full steps in [[CL14 Observed Winds - Jets, Trades and the ITCZ]].
- **Sign:** NH ($f>0$) with colder pole ($\partial T/\partial y<0$) gives westerly shear; SH gives the same: jets are westerly in both hemispheres.
- **Numbers:** at 35° with $\Delta T=13$ K over 2000 km the shear is 3 m s⁻¹ per km, i.e. 30 m s⁻¹ over 10 km, the observed mean subtropical jet. Jet speed $\propto\Delta T$ and $\propto1/\sin\varphi$.
- **Tropics:** $f\to0$ and the horizontal temperature gradient is tiny (weak-temperature-gradient regime), so no thermal-wind jets: the surface easterlies persist aloft.
- **Not a force:** it is a *kinematic* consequence of two balances, valid when the flow is close to geostrophic (small Rossby number, [[Coriolis Parameter]]).

See [[Jet Streams]], [[Subtropical Jet]], [[Zonal-Mean Zonal Wind]], [[Meridional Temperature Structure]], [[Coriolis Force]]. Chapters: [[CL14 Observed Winds - Jets, Trades and the ITCZ]], [[CL13 Horizontal Motion - Geostrophic Balance and Friction]], [[CL06 Hydrostatic Balance and Vertical Structure]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
