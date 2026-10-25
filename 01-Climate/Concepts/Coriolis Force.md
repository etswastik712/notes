---
title: Coriolis Force
aliases: [Coriolis acceleration, Coriolis effect]
subject: climate
type: concept
scope: [taught, extra-book, extra-beyond]
by: [suhas-post, book]
status: draft
tags: [subject/climate, type/concept, taught, extra/book, extra/beyond, src/suhas-post, src/book, status/draft]
---
# Coriolis Force

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Scope of this note
> | Scope | What |
> |---|---|
> | 🟢 **Taught** | definition $-2\boldsymbol\Omega\times\mathbf u$, right (NH) / left (SH), workless, derivation, three physical explanations, components, $f=2\Omega\sin\varphi$ ([[CL12 Rotating Frames and the Coriolis Force]]) |
> | 🟡 **Extra · book** | the rotating-table experiments (radial inflow, parabolic surface), M&P §6.6 |
> | 🔵 **Extra · beyond** | Eötvös effect, Foucault pendulum, inertial oscillation, Larmor analogy |

> [!key] Definition
> In a frame rotating with angular velocity $\boldsymbol\Omega$, a parcel moving with velocity $\mathbf u$ relative to the frame seems to be accelerated by $-2\boldsymbol\Omega\times\mathbf u$: **perpendicular** to $\mathbf u$, to its **right** in the Northern Hemisphere ($\Omega$ anticlockwise seen from above), **proportional to speed** and **workless**.

> [!intuition] Merry-go-round and magnetic force
> Throw a ball across a merry-go-round: seen from the ground it goes straight, seen from the carousel it curves, because the carousel turns under it. It is also the mechanical twin of the magnetic force $q\mathbf u\times\mathbf B$: it turns motion but never speeds it up.

**Components** (east, north, up; $\boldsymbol\Omega=(0,\Omega\cos\varphi,\Omega\sin\varphi)$):
$$-2\boldsymbol\Omega\times\mathbf u=\big(2\Omega\sin\varphi\,v-2\Omega\cos\varphi\,w,\ -2\Omega\sin\varphi\,u,\ 2\Omega\cos\varphi\,u\big).$$
For large-scale flow only $+fv$ and $-fu$ survive, with the [[Coriolis Parameter]] $f=2\Omega\sin\varphi\approx10^{-4}$ s⁻¹.

**Three equivalent explanations** (all derived in [[CL12 Rotating Frames and the Coriolis Force]]): (i) vector algebra of the frame transformation, $(\mathrm d\mathbf A/\mathrm dt)_I=(\mathrm d\mathbf A/\mathrm dt)_r+\boldsymbol\Omega\times\mathbf A$; (ii) the extra centrifugal force of a body moving east or west; (iii) angular-momentum conservation for north–south motion, $A=\Omega a^2\cos^2\varphi+ua\cos\varphi$ ([[Absolute Angular Momentum of Air]]).

**Numbers.** 40 m s⁻¹ jet at 45°: $4.1\times10^{-3}$ m s⁻² (≈ $4\times10^{-4}g$); 10 m s⁻¹ wind at 30°: $7.3\times10^{-4}$ m s⁻²; 100 m s⁻¹ shell over 100 km at 45°: 3.6 km deflection.

> [!pitfall] Common mistakes
> It does not accelerate a parcel, only turns it. A resting parcel feels none. "Right in the NH" is relative to the direction of motion. The factor is 2. It is not what makes bathtubs drain one way (Rossby number $\gg1$ there).

Used in: [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] (geostrophic balance), [[CL11 Mean Meridional Circulation and Angular Momentum]] (ring of air), [[CL14 Observed Winds - Jets, Trades and the ITCZ]] (trades and westerlies). See [[Centrifugal Force and Effective Gravity]], [[Rotating Reference Frames]], [[Eotvos Effect]], [[Foucault Pendulum]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
