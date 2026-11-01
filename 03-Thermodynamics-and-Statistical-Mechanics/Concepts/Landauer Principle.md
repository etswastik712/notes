---
title: Landauer Principle
aliases: ["Landauer bound", "cost of erasure", "k T ln 2 per bit"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Landauer Principle

> [!info] Source
> Landauer (1961); Blundell §15.2 (p. 160); [[SM06 Entropy Information and the Arrow of Time]] §3.2.

> [!intuition] In one picture
> Forgetting is what costs: resetting a bit to a standard state throws away one bit of entropy, which must go into the surroundings as heat.

> [!key] Key facts
> Erasing a bit with unknown content dissipates $Q\ge k_BT\ln2$ ($2.87\times10^{-21}$ J, $17.9$ meV at 300 K); for a memory of Shannon entropy $H$: $Q\ge k_BT\,\Delta H$; erasing a known state is free; reversible computation (no erasure) has no bound.

> [!example] Numbers (recomputed)
> 1 GB: $\ge2.3\times10^{-11}$ J; $10^9$ erased bits per second: $2.9\times10^{-12}$ W; real logic is $3.5\times10^3$–$3.5\times10^5$ times above the bound (orders of magnitude, recalled).

Used in: [[SM06 Entropy Information and the Arrow of Time]]. Related: [[Maxwell's Demon]] · [[Szilard Engine]] · [[Shannon Entropy]] · [[Exergy and Availability]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
