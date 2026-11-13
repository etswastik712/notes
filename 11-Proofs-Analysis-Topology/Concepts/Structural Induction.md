---
title: Structural Induction
aliases: ["induction on construction", "recursive structures"]
subject: analysis
type: concept
scope: [extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, extra/beyond, src/own-notes, status/draft, quiz/proofs, quiz/pa-strong]
---
# Structural Induction

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Sundstrom §4.3. 🔵 the tree counts are mine ([[PA09 Strong Induction and Recursion]] §5).

> [!intuition] In one picture
> Prove a property of everything built by a recursive recipe by proving it for the ingredients and showing each construction rule keeps it.

> [!key] Statement
> Objects are defined by basic cases and construction rules. If the basic objects have the property and every rule preserves it, all objects have it (strong induction on size). Full binary trees: leaves $=$ internal nodes $+1$; height $h\Rightarrow$ at most $2^h$ leaves; $m$ internal nodes $\Rightarrow$ $C_m$ shapes ([[Catalan Numbers]]).

Used in: [[PA09 Strong Induction and Recursion]]. Related: [[Strong Induction]] · [[Recursion Theorem]] · [[Statement and Truth Table]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
