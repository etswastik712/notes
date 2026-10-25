---
title: Hydrogen Atom Stability
aliases: ["size of the hydrogen atom", "Bohr radius estimate"]
subject: qm
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/beyond, src/lecture-notes, status/draft]
---
# Hydrogen Atom Stability

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_Wavefunction_to_Uncertainty (1).pdf#page=3|WU §10]], [[PH2113_Lecture6-7.pdf#page=3|L7 §6]]. · 🔵 **extra · beyond:** the general $A/r^2-B/r$ result and the ions.

> [!intuition] In one picture
> Squeezing the electron closer costs kinetic energy faster ($1/r^2$) than the Coulomb attraction pays back ($1/r$): the atom stops collapsing at a definite size.

> [!key] Definition
> $E(r)\sim\dfrac{\hbar^2}{2m_er^2}-\dfrac{e^2}{4\pi\varepsilon_0r}$ is minimised at $r=a_0=\dfrac{4\pi\varepsilon_0\hbar^2}{m_ee^2}=0.529$ Å with $E=-13.6$ eV.

## Derivation and caution
$\mathrm dE/\mathrm dr=0\Rightarrow r_{\min}=a_0$, $E_{\min}=-\hbar^2/2m_ea_0^2=-2.18\times10^{-18}$ J $=-13.61$ eV (measured $13.606$ eV).

> [!pitfall] Trust the scaling, not the prefactor
> The estimate uses $\Delta p\sim\hbar/r$. With the strict $\Delta p\ge\hbar/2r$ the minimum is at $a_0/4$ with $-54.4$ eV. The exact agreement is a happy accident of the Coulomb problem; the scaling $a_0\propto\hbar^2/me^2$, $E\propto me^4/\hbar^2$ is robust.

> [!extra-beyond]- 🔵 Extra (beyond): ions
> $E=A/r^2-B/r\Rightarrow r=2A/B$, $E=-B^2/4A$. Nuclear charge $Ze$: $r=a_0/Z$, $E=-Z^2\times13.6$ eV; He$^+$ gives $-54.4$ eV, the exact value.

Used in: [[QM01 From Waves to Probabilities]]. Related: [[Heisenberg Uncertainty Principle]] · [[Compton Wavelength]] · [[Zero-Point Energy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
