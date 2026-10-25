---
title: Clausius Theorem
aliases: ["Clausius inequality"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Clausius Theorem

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[1a131e225246d9749a298f49675c5fe5_MIT8_333F13_Lec2.pdf#page=4|MIT L2 §I.F]].

> [!intuition] In one picture
> Add up heat divided by temperature round any loop: you can never get a positive total.

> [!key] Definition
> For any cyclic transformation $\oint\bar\mathrm dQ/T\le0$, equality iff reversible. Hence $\int\bar\mathrm dQ_{\rm rev}/T$ is path-independent and $S$ exists; for any change $\mathrm dS\ge\bar\mathrm dQ/T$.

## Check
Engine between $500$ and $300$ K taking $1000$ J and delivering $600$ J: $\sum Q/T=1000/500-400/300=+0.667>0$: violates it, hence impossible.

> [!pitfall] $T$ is the boundary temperature
> In an irreversible cycle $T$ in the integral is that of the reservoir or boundary where heat enters, not a single temperature of the system.

Used in: [[TH04 The Second Law Carnot Engines and Entropy]]. Related: [[Entropy]] · [[Second Law of Thermodynamics]] · [[Carnot Engine]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
