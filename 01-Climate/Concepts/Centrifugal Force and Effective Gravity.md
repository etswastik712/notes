---
title: Centrifugal Force and Effective Gravity
aliases: [Effective gravity, Centrifugal acceleration]
subject: climate
type: concept
scope: [taught, extra-book, extra-beyond]
by: [suhas-post, book]
status: draft
tags: [subject/climate, type/concept, taught, extra/book, extra/beyond, src/suhas-post, src/book, status/draft]
---
# Centrifugal Force and Effective Gravity

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Scope of this note
> | Scope | What |
> |---|---|
> | 🟢 **Taught** | centrifugal acceleration $\Omega^2\mathbf R_\perp$, vertical and horizontal components, $\mathbf g_{\rm eff}=\mathbf g^*+\Omega^2\mathbf R_\perp$, the plastic Earth flows into an oblate spheroid (15 Oct p2–11) |
> | 🟡 **Extra · book** | gradient form and the modified potential $\phi=gz-\tfrac12\Omega^2R^2$; parabolic free surface (M&P §6.6) |
> | 🔵 **Extra · beyond** | Maclaurin flattening, WGS84 gravity at pole and equator |

> [!key] Definition
> The **centrifugal acceleration** $+\Omega^2\mathbf R_\perp$ points outward from the rotation axis with magnitude $\Omega^2a\cos\varphi$ and depends on **position only**. Added to true gravity it gives the **effective gravity** $\mathbf g_{\rm eff}=\mathbf g^*+\Omega^2\mathbf R_\perp$, which is what a plumb line or a spirit level measures as "down".

> [!intuition] Pizza dough
> Spin a ball of dough: it flows outward until its surface is perpendicular to the net force. The plastic Earth did the same and became an oblate spheroid; once it had, a resting object feels **no net horizontal force**, so the centrifugal force is used up and only the Coriolis force remains for moving things.

- At latitude $\varphi$: vertical part $\Omega^2a\cos^2\varphi$ (outward, opposes gravity), horizontal part $\Omega^2a\sin\varphi\cos\varphi$ (equatorward). Equator: $\Omega^2a=0.0339$ m s⁻² $=g/290$.
- On a *sphere* the horizontal part of $\mathbf g^*+\Omega^2\mathbf R_\perp$ points equatorward; on the *bulged* Earth the poleward along-surface component of gravity cancels it. (The slides use "poleward" for the latter: see the `[!verify]` in [[CL12 Rotating Frames and the Coriolis Force]] §4.1.)
- Tilt of $\mathbf g_{\rm eff}$ from the radial direction: $\le0.1^\circ$ (at 45°).
- Potential form: $\mathbf g_{\rm eff}=-\nabla\phi$, $\phi=gz-\tfrac12\Omega^2R_\perp^2$ (🟡 M&P Eq. 6-30); in solid-body rotation $z=h_0+\Omega^2r^2/2g$.

> [!extra-beyond]- 🔵 Extra (beyond): numbers
> Homogeneous fluid planet: flattening $\approx\tfrac54\Omega^2a/g=1/231$ (27.6 km), actual Earth $1/298$ (21.4 km). WGS84 gravity: 9.7803 (equator), 9.8322 m s⁻² (poles): centrifugal explains 65 % of the difference.

Derived and illustrated in [[CL12 Rotating Frames and the Coriolis Force]]. See [[Coriolis Force]], [[Rotating Reference Frames]], [[CL06 Hydrostatic Balance and Vertical Structure]] (hydrostatic balance and geopotential), [[Eotvos Effect]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
