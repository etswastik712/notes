---
title: Entropy of Mixing of Ideal Gases
aliases: ["Delta S_mix", "Gibbs energy of mixing", "mixing of ideal gases", "-R sum n ln x", "isothermal expansion into the partial pressure"]
subject: thermo
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/thermo, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Entropy of Mixing of Ideal Gases

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Bhagwat.pdf#page=1|Bhagwat notes]], pp. 3–4: $\Delta S_i=-n_iR\ln x_i$, $\Delta H_{\rm mix}=0$, $\Delta G_{\rm mix}=RT\sum n_i\ln x_i$.
> 🔵 **extra · beyond:** numbers for air and $N$ components, the work to separate air (mine, checked).

> [!intuition] In one picture
> Each gas, after mixing, occupies the whole volume at its **partial pressure** $x_iP$: mixing is an isothermal expansion of each gas from $P$ to $x_iP$. Nothing exchanges energy; the entropy rises because each molecule has more room.

> [!key] Definition
> $\Delta S_{\rm mix}=-R\sum_in_i\ln x_i=-nR\sum x_i\ln x_i>0$; $\Delta H_{\rm mix}=0$ (ideal gas: $\mathrm dH=T\mathrm dS+V\mathrm dP=0$ at constant $T$); $\Delta G_{\rm mix}=RT\sum n_i\ln x_i<0$; $\mu_i=\mu_i^\circ+RT\ln(x_iP/P^\circ)$. Maximum $R\ln N$ at equal fractions.

Numbers at 298.15 K: equimolar binary $5.763$ J mol$^{-1}$K$^{-1}$, $\Delta G=-1.718$ kJ mol$^{-1}$; air-like $0.79/0.21$: $4.273$, $-1.274$ kJ mol$^{-1}$ (the minimum work to separate air). For *identical* gases $\Delta S=0$: the Gibbs paradox.

Used in: [[TH10 Open Systems Mixing and Reacting Gases]], [[TH05 Potentials Maxwell Relations Stability and the Third Law]]. Related: [[Gibbs Paradox]] · [[Chemical Potential]] · [[Gibbs Free Energy]] · [[Entropy Production]] · [[Maxwell Relations]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
