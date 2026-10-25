---
title: Dimensional Analysis
aliases: ["dimensional reasoning", "Buckingham pi"]
subject: foundations
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/foundations, type/concept, taught, extra/beyond, src/lecture-notes, status/draft]
---
# Dimensional Analysis

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** used in [[PH2113_Lecture8_Uncertainty_Wavefunctions_Schrodinger (1).pdf#page=2|L8 §2]] to find the Compton length. · 🔵 **extra · beyond:** the general method and other uses.

> [!intuition] In one picture
> Before solving anything, ask which combinations of the quantities you have can make a length, a time or an energy. Often there is only one.

> [!key] Definition
> If a quantity $Q$ is built from given quantities as a product of powers, equate the **dimensions** of each base unit (kg, m, s) on both sides; the resulting linear equations for the exponents often have a unique solution. It fixes the **scaling**, never the dimensionless number in front.

## Worked cases
> [!example] A length from $\hbar,c,m$
> $\ell=\hbar^ac^bm^d$: kg: $a+d=0$; m: $2a+b=1$; s: $-a-b=0$ $\Rightarrow$ $a=1$, $b=-1$, $d=-1$: $\ell=\hbar/mc$. A **time** (s: $-a-b=1$, m: $2a+b=0$) gives $\hbar/mc^2$.

> [!example] The same idea elsewhere
> The Rossby number $U/fL$ in [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] and the atomic length $\hbar^2/me^2$ ($=a_0$ up to $4\pi\varepsilon_0$) both come from asking which combination has the right dimensions.

> [!pitfall] Pure numbers are invisible
> Factors such as $2\pi$, $1/2$ or $\sqrt3$ are dimensionless and drop out; only physical reasoning (or a calculation) fixes them. If the answer has several dimensionless groups, the method alone cannot choose a unique form.

Used in: [[QM01 From Waves to Probabilities]]. Related: [[Compton Wavelength]] · [[Hydrogen Atom Stability]] · [[Linearisation and Sensitivity]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
