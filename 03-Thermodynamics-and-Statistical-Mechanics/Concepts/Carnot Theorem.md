---
title: Carnot Theorem
aliases: ["Carnot's theorem"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Carnot Theorem

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[1a131e225246d9749a298f49675c5fe5_MIT8_333F13_Lec2.pdf#page=3|MIT L2 eq. I.20]].

> [!intuition] In one picture
> Run the rival engine to drive the Carnot engine backwards: if the rival were better, heat would flow cold-to-hot by itself.

> [!key] Definition
> No engine between two reservoirs is more efficient than a Carnot engine between them; all reversible engines between the same reservoirs have the same efficiency $\eta(T_H,T_C)$.

## Proof sketch
Use the other engine to run the Carnot engine as a refrigerator; the net transfer $Q_H-Q_H'=Q_C-Q_C'$ from hot to cold cannot be negative (Clausius), so $Q_H\ge Q_H'$ and $W/Q_H\le W/Q_H'$.

> [!pitfall] Efficiency, not work
> The theorem compares efficiencies at the same $T$'s; irreversible engines still obey the first law.

Used in: [[TH04 The Second Law Carnot Engines and Entropy]]. Related: [[Kelvin and Clausius Statements]] · [[Carnot Engine]] · [[Thermodynamic Temperature]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
