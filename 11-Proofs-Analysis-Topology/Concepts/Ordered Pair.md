---
title: Ordered Pair
aliases: ["Kuratowski pair", "Kuratowski definition"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Ordered Pair

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ordered pairs.pdf#page=1|instructor's note, pp.1–8]].

> [!intuition] In one picture
> A set that remembers which entry came first.

> [!key] Definition
> Property (OP): $(A,B)=(C,D)\iff A=C\wedge B=D$. **Kuratowski:** $(A,B):=\{\{A\},\{A,B\}\}$; $\bigcap(A,B)=\{A\}$, $\bigcup(A,B)=\{A,B\}$.

Fails: $\{A,B\}$, $\{\{A\},\{B\}\}$, $\{A,\{B\}\}$ ($\{Z,\{X\}\}=\{Y,\{Y\}\}$ for $X=\varnothing,Y=\{\varnothing\},Z=\{Y\}$). Works with Regularity: $\{A,\{A,B\}\}$. On all 16 sets of rank 3 the Kuratowski and $\{A,\{A,B\}\}$ encodings have 0 collisions; the failing ones have 120, 120 and 6. $(A,A)=\{\{A\}\}\ne\{A\}$ by Regularity.

Used in: [[PA02 Sets Families and the ZFC Foundations]]. Related: [[Cartesian Product]] · [[ZFC Axioms]] · [[Binary Relation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
