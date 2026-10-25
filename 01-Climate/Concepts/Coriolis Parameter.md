---
title: Coriolis Parameter
aliases: [f, f-plane, beta-plane]
subject: climate
type: concept
scope: [taught, extra-book, extra-beyond]
by: [suhas-post, book]
status: draft
tags: [subject/climate, type/concept, taught, extra/book, extra/beyond, src/suhas-post, src/book, status/draft]
---
# Coriolis Parameter

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Scope of this note
> | Scope | What |
> |---|---|
> | 🟢 **Taught** | $f=2\Omega\sin\varphi$ and the horizontal Coriolis terms $+fv$, $-fu$ (22 Oct p9–12) |
> | 🟡 **Extra · book** | Rossby number $\mathrm{Ro}=U/fL$ and scale analysis (M&P §7.1, excerpt for CL13) |
> | 🔵 **Extra · beyond** | $\beta=2\Omega\cos\varphi/a$, $f$-plane and $\beta$-plane, inertial period |

> [!key] Definition
> The **Coriolis parameter** $f=2\Omega\sin\varphi$ is twice the local vertical component of the Earth's rotation. The horizontal momentum equations carry $+fv$ and $-fu$ ([[Coriolis Force]]).

> [!intuition] A turntable tilted with latitude
> At the pole the Earth is a turntable lying flat and spins horizontal motion fully ($f=2\Omega$). At the equator it stands on edge: horizontal motion is not turned ($f=0$). In between only the share $\sin\varphi$ of the spin lies along local "up". The sign changes across the equator, which is why deflection is to the right in the NH and to the left in the SH.

| latitude | $f$ (10⁻⁴ s⁻¹) | inertial period $2\pi/f$ |
|---|---|---|
| 10° | 0.25 | 69 h |
| 30° | 0.73 | 23.9 h (= sidereal day, $f=\Omega$) |
| 45° | 1.03 | 16.9 h |
| 60° | 1.26 | 13.8 h |
| 90° | 1.46 | 12.0 h |

🟡 **Rossby number** $\mathrm{Ro}=U/(fL)$: Coriolis vs the flow's own acceleration; $\approx0.1$ for synoptic weather (10 m s⁻¹, 1000 km), so rotation dominates ([[CL13 Horizontal Motion - Geostrophic Balance and Friction]]).
🔵 $\beta=\mathrm df/\mathrm dy=2\Omega\cos\varphi/a=1.6\times10^{-11}$ m⁻¹ s⁻¹ at 45°: the origin of Rossby waves ([[Waves - Course Map]]).

Derived in [[CL12 Rotating Frames and the Coriolis Force]] §5. See [[Rotating Reference Frames]], [[Foucault Pendulum]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
