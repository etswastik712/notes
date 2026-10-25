---
title: Internal Phosphorus Loading
aliases: ["internal loading", "sediment phosphorus release"]
subject: eco-evo
type: concept
scope: [taught, extra-beyond]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/beyond, src/slides, status/draft]
---
# Internal Phosphorus Loading

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** 'a series of anoxic reactions releasing phosphorus' on the slide ([[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=7|slide 7]])  ·  🔵 **extra · beyond:** iron-redox mechanism and the positive feedback

> [!intuition] In one picture
> A lake can keep itself green: when the bottom water runs out of oxygen, phosphorus locked in the mud is let out again, feeding the next bloom.

> [!key] Definition
> Release of phosphorus from the sediment into the water. Under anoxia, iron(III) compounds that bind phosphate are reduced to soluble iron(II) and release it (Mortimer). Positive feedback: more P, more algae, more sinking organic matter, more oxygen demand, more P release. It keeps a lake eutrophic after the external load has been cut.

## A mass-balance sketch and a delay
Let $P$ be the lake concentration, $q=Q/V$ the flushing rate, $s$ the sedimentation rate and $I$ the internal release (per volume):
$$\frac{dP}{dt}=\frac{L_{ext}}{V}+I-(q+s)P\ \Rightarrow\ P^*=\frac{L_{ext}/V+I}{q+s},\qquad\tau=\frac1{q+s}.$$
After the external load is cut, $P$ relaxes at rate $q+s$ only if $I$ is small.

> [!example] Why recovery lags
> $q=1\ \text{yr}^{-1}$, $s=0.5\ \text{yr}^{-1}$ ($\tau=0.67$ yr). If $L_{ext}/V$ is stopped but release from the sediment stays at $I=15$ µg L⁻¹ yr⁻¹, the lake holds $P^*=15/1.5=10$ µg L⁻¹ (still the oligotrophic–mesotrophic boundary) until the sediment store is depleted, which can take years to decades: Lampert and Sommer's "phosphorus deposited in the sediments during the peak period of pollution may continue to be released for several years", and release may even rise as the water concentration falls (a larger diffusion gradient).
> **The feedback.** If $I$ increases with algal production ($I=\gamma P$, via anoxia), then $P^*=(L/V)/(q+s-\gamma)$: when $\gamma\to q+s$ the denominator vanishes and the lake pumps itself; a saturating $I(P)$ gives the S-shaped balance of [[Alternative Stable States]] (Box 1 of Scheffer et al. models the recycling term $r f(x)$).

**Mechanism.** In oxygenated sediment iron(III) hydroxides bind phosphate; under anoxia Fe(III) is reduced to the soluble Fe(II) and phosphate is released (Mortimer's mechanism, background; the reading says only "anoxic sediments"). Aluminium treatment binds phosphorus permanently, which is why it is a restoration method ([[Lake Restoration Methods]]).

> [!pitfall] External versus internal
> A lake can be restored in the *loading* sense and still be eutrophic because of its mud. Whether stratification occurs matters ([[Thermal Stratification of Lakes]]); shallow lakes release phosphorus even without stratification through resuspension. Chemistry background: [[Inorganic Chemistry - Course Map]].

Used in: [[EE06 Eutrophication and Alternative Stable States]]. Related: [[Cultural Eutrophication]] · [[Thermal Stratification of Lakes]] · [[Lake Restoration Methods]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
