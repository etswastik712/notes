---
title: Chi Transform
aliases: [chi coordinate, chi plot, integral coordinate]
subject: landscapes
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/landscapes, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Chi Transform

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **Extra · beyond** (Perron and Royden's integral approach; my derivation and numerical check in [[LS23 Bedrock Channels and River Incision]] §6.1).

> [!intuition] In one picture
> Re-measure a river not in metres but in travel time for a knickpoint; then every steady river is a straight line.

> [!key] Definition and key results
> $\chi(s)=\int_0^s(A_0/A)^m\,ds'$; for $n=1$, $\partial_tz=U-v\,\partial_\chi z$ with $v=KA_0^m$ constant; steady state $z=(U/v)\chi$; a step in $U$ gives two straight lines meeting at $\chi_k=vt$.

> [!pitfall] Pitfall
> Exact for $n=1$ only; for $n\neq1$ it is the steady-state coordinate but the transient is nonlinear.

Used in: [[LS23 Bedrock Channels and River Incision]]. Related: [[Knickpoint]] · [[Stream Power Law]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Impulse Response and Green's Function]] (Foundations): characteristics and the travel-time coordinate for a first-order wave equation
