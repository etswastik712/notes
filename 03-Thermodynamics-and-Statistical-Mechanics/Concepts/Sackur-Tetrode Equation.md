---
title: Sackur-Tetrode Equation
aliases: ["Sackur–Tetrode"]
subject: thermo
type: concept
scope: [extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, extra/book, extra/beyond, src/lecture-notes, status/draft]
---
# Sackur-Tetrode Equation

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** `Thermo_StatMech_Notes.pdf` §4.3. · 🔵 **extra · beyond:** the comparison with measured entropies.

> [!intuition] In one picture
> The entropy of a monatomic gas from first principles: the one place where thermodynamics and quantum mechanics meet in a number.

> [!key] Definition
> $S=Nk_B\Big[\ln\Big(\dfrac VN\Big(\dfrac{2\pi mk_BT}{h^2}\Big)^{3/2}\Big)+\dfrac52\Big]$.

## Check against calorimetry
At 298.15 K, 1 bar: He $126.15$, Ne $146.33$, Ar $154.85$, Kr $164.09$, Xe $169.69$ J mol$^{-1}$K$^{-1}$ (measured $126.15$, $146.33$, $154.85$, $164.08$, $169.68$, recalled from tables). Doubling $T$ at fixed $P$: $\tfrac52R\ln2=14.4$ J mol$^{-1}$K$^{-1}$.

> [!pitfall] Valid only in the classical, dilute regime
> It fails at low $T$ (negative entropy) where $n\lambda^3\gtrsim1$ and quantum statistics takes over.

Used in: [[TH06 From Kinetic Theory to Statistical Mechanics]]. Related: [[Statistical Entropy]] · [[Third Law of Thermodynamics]] · [[Entropy]] · [[Partition Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
