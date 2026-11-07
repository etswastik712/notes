---
title: Holonomy of a Plane Field
aliases: ["horizontal lift of a loop", "height gap", "non-holonomic constraint"]
subject: diff-geometry
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/diff-geometry, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Holonomy of a Plane Field

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** my explanation of the obstruction to integrability (DM16 §3); the interactive tool `dm_contact_holonomy`.

> [!intuition] In one picture
> Walk once round a loop in the $(x,y)$-plane while staying tangent to the planes: if the planes had integral surfaces you would come back to the same height; if not, you do not.

> [!key] Definition
> For $D=\ker(dz-A)$, $A=A_1dx+A_2dy$, the horizontal lift of a closed loop ends at $\Delta z=\oint A=\iint dA$ (Stokes). Integrable $\iff dA=0$. For $dA=k\,dx\wedge dy$: $\Delta z=k\cdot$(signed area), quadratic in the loop size.

Checked by ODE: $A=x\,dy$, square of side $0.5$: $\Delta z=0.250000$; circle of radius $0.5$: $0.785398=\pi/4$; $A=d(xy)$: $\Delta z=0$ for every loop. Mechanics (recalled): a non-integrable distribution on a configuration space is a **non-holonomic constraint** (a ball rolling without slipping): the gap is the net rotation after a loop.

Used in: [[DM16 Distributions, Involutivity and the Frobenius Theorem]]. Related: [[Involutive Distribution]] · [[Lie Bracket of Vector Fields]] · [[Frobenius Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
