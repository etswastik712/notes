---
title: Rotating Reference Frames
aliases: [Non-inertial frames, Transport theorem]
subject: foundations
type: concept
scope: [taught, extra-beyond]
by: [suhas-post, own-notes]
status: draft
tags: [subject/foundations, type/concept, taught, extra/beyond, src/suhas-post, src/own-notes, status/draft]
---
# Rotating Reference Frames

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Scope of this note
> | Scope | What |
> |---|---|
> | 🟢 **Taught** | the rule for any vector, $\mathbf u_I=\mathbf u_r+\boldsymbol\Omega\times\mathbf R$, acceleration with Coriolis and centrifugal terms ([[CL12 Rotating Frames and the Coriolis Force]]) |
> | 🔵 **Extra · beyond** | the Euler force, general (non-constant $\Omega$) statement, other applications, the Larmor analogy |

> [!key] The rule
> For any vector $\mathbf A$ and a frame rotating at $\boldsymbol\Omega$: $\left(\dfrac{\mathrm d\mathbf A}{\mathrm dt}\right)_I=\left(\dfrac{\mathrm d\mathbf A}{\mathrm dt}\right)_r+\boldsymbol\Omega\times\mathbf A$.

> [!intuition] Arrows glued to a carousel
> An arrow fixed to the carousel is frozen for the rider but turns for the outsider: its tip moves by $(\boldsymbol\Omega\,\mathrm dt)\times\mathbf A$. Add any change the rider also sees, and you have the rule.

Applying it twice gives $\mathbf a_I=\mathbf a_r+2\boldsymbol\Omega\times\mathbf u_r+\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r)+\dot{\boldsymbol\Omega}\times\mathbf r$, so in the rotating frame Newton's law acquires:

| apparent acceleration | expression | depends on | note |
|---|---|---|---|
| **Coriolis** | $-2\boldsymbol\Omega\times\mathbf u$ | velocity | workless; turns motion |
| **Centrifugal** | $-\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r)=+\Omega^2\mathbf r_\perp$ | position | conservative |
| **Euler** | $-\dot{\boldsymbol\Omega}\times\mathbf r$ | position, rotation change | $\approx0$ for the Earth ($\sim10^{-12}$ m s⁻²) |

- Derived and applied to the Earth in [[CL12 Rotating Frames and the Coriolis Force]]; terms: [[Coriolis Force]], [[Centrifugal Force and Effective Gravity]], [[Coriolis Parameter]].
- 🔵 Other uses: [[Foucault Pendulum]] (plane of swing rotates at $\Omega\sin\varphi$), [[Eotvos Effect]], cyclone rotation, gyroscopes, centrifuges, ocean inertial oscillations.
- 🔵 Formal parallel: a charge in a magnetic field feels $q\mathbf u\times\mathbf B$, of the Coriolis form with $q\mathbf B\leftrightarrow2m\boldsymbol\Omega$: **Larmor's theorem** ([[Quantum Mechanics - Course Map]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
