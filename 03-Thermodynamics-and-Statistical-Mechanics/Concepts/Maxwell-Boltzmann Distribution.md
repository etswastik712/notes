---
title: Maxwell-Boltzmann Distribution
aliases: ["Maxwell distribution", "Maxwell speed distribution"]
subject: thermo
type: concept
scope: [extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, extra/book, extra/beyond, src/lecture-notes, status/draft]
---
# Maxwell-Boltzmann Distribution

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** `KTG_Chapter.pdf` §1.3. · 🔵 **extra · beyond:** atmospheric escape.

> [!intuition] In one picture
> Most molecules move near the typical speed; few are very slow or very fast, with a Gaussian-in-velocity tail.

> [!key] Definition
> $f(v)=4\pi\big(m/2\pi k_BT\big)^{3/2}v^2e^{-mv^2/2k_BT}$; $v_{mp}=\sqrt{2k_BT/m}$, $\langle v\rangle=\sqrt{8k_BT/\pi m}$, $v_{rms}=\sqrt{3k_BT/m}$. Fraction above $xv_{mp}$: $\operatorname{erfc}x+\frac2{\sqrt\pi}xe^{-x^2}$.

## Numbers
N$_2$, 300 K: $422$, $476$, $517$ m s$^{-1}$; $4.6\%$ above $2v_{mp}$, $0.044\%$ above $3v_{mp}$. He: $1116$, $1260$, $1367$. $v_{rms}/v_{esc}$: N$_2$ $0.046$, He $0.12$, H$_2$ $0.17$: why Earth loses H$_2$.

> [!pitfall] Speed, not velocity
> The $v^2$ factor comes from the volume of the velocity shell; the *velocity* distribution is a Gaussian peaked at $0$.

Used in: [[TH06 From Kinetic Theory to Statistical Mechanics]]. Related: [[Kinetic Theory of Gases]] · [[Equipartition of Energy]] · [[Mean Free Path]] · [[Partition Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Rayleigh Distribution]] (Probability): the Maxwell speed density $ax^2e^{-bx^2}$ is the 3-D relative of the Rayleigh density $xe^{-x^2/2\sigma^2}$ of the 2-D speed of Gaussian components; both normalise by $\int x^ke^{-x^2}\mathrm dx$ (Quiz 1, Q3).

## Continued in Part II (added 2026-10-30)
- Derived from the canonical ensemble for *any* interaction (momenta are independent Gaussians of variance $mk_BT$): [[SM03 The Canonical Ensemble]] §4.2; the companion Boltzmann factor $mgz$ gives the [[Barometric Formula]].
