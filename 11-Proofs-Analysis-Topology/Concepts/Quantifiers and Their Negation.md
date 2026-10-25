---
title: Quantifiers and Their Negation
aliases: ["predicate", "forall exists", "order of quantifiers", "negating quantified statements"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Quantifiers and Their Negation

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-prems_merged.pdf#page=5|Assignment 2, Q3–Q8]].

> [!intuition] In one picture
> $\forall$ must hold for every case; $\exists$ needs just one witness; negation swaps them.

> [!key] Definition
> $\neg\forall x\,P(x)\sim\exists x\,\neg P(x)$; $\neg\exists x\,P(x)\sim\forall x\,\neg P(x)$. $\forall x\in A\,P\equiv\forall x(x\in A\Rightarrow P)$; $\exists x\in A\,P\equiv\exists x(x\in A\wedge P)$. $\forall x\exists y\ne\exists y\forall x$.

> [!example] Order matters
> Over $\mathbb R$, $\forall x\exists y\,(y>x)$ is true; $\exists y\forall x\,(y>x)$ is false. Negation of "for every $\varepsilon$ there is $\delta$ such that…" is "there is an $\varepsilon$ such that for every $\delta$ there is an $x$…" (the template for every $\varepsilon$–$\delta$ and $\varepsilon$–$N$ definition).

Used in: [[PA01 Logic and Methods of Proof]]. Related: [[Conditional Statement]] · [[Counterexample]] · [[Sequence and Limit]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
