---
title: Russell's Paradox
aliases: ["Russell paradox", "unrestricted comprehension"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Russell's Paradox

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=26|AI notes ch. 4.1]].

> [!intuition] In one picture
> The set of all sets that do not contain themselves would contain itself exactly when it does not.

> [!key] Definition
> $R=\{x:x\notin x\}$ gives $R\in R\iff R\notin R$: there is no such set. Separation fixes it: for any set $A$, $\{x\in A:x\notin x\}$ is a set and is **not** a member of $A$.

The proof of [[Cantor's Theorem]] uses the same self-reference ($B=\{a:a\notin f(a)\}$), and shows there is no universal set.

Used in: [[PA02 Sets Families and the ZFC Foundations]]. Related: [[ZFC Axioms]] · [[Cantor's Theorem]] · [[Power Set]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
