---
title: Independence of Events
aliases: ["independent events", "mutual independence", "pairwise independence"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Independence of Events

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=16|class notes 19 Aug]], [[Practice problems 21st August 2026.pdf#page=2|sheet 21 Aug, problems 6–8]].

> [!intuition] In one picture
> Knowing that $F$ happened tells you nothing about $E$.

> [!key] Definition
> $E,F$ are independent iff $P[E\cap F]=P[E]P[F]$ (equivalently $P[E\mid F]=P[E]$). $E_1,\dots,E_r$ are **mutually independent** iff the product rule holds for **every** non-empty sub-collection.

## Facts
- If $E,F$ are independent so are $E,F^c$; $E^c,F$; $E^c,F^c$.
- Independent is not disjoint: disjoint events of positive probability are strongly dependent.
- An event independent of itself has $P[E]\in\{0,1\}$.
- Pairwise independence does **not** give mutual independence.

> [!example] Two dice (class)
> $A$ = first die shows 6, $B$ = second shows 6, $C$ = the dice agree. Every pair is independent ($\tfrac1{36}=\tfrac16\cdot\tfrac16$) but $P[A\cap B\cap C]=\tfrac1{36}\ne\tfrac1{216}$.

Used in: [[PR02 Conditional Probability Bayes Rule and Independence]]. Related: [[Conditional Probability]] · [[Independence of Random Variables]] · [[Conditional Independence]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
