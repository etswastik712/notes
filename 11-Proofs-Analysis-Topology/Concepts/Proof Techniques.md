---
title: Proof Techniques
aliases: ["direct proof", "proof by contradiction", "contrapositive proof", "proof by cases"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Proof Techniques

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=21|AI notes ch. 3]]; Sundstrom Ch. 3.

> [!intuition] In one picture
> Pick the technique from the logical form of what you must show.

> [!key] Definition
> Direct ($P\Rightarrow Q$: assume $P$, derive $Q$); contrapositive ($\neg Q\Rightarrow\neg P$); contradiction (assume the negation, derive $R\wedge\neg R$); cases; existence by witness or non-constructively; counterexample for a $\forall$; induction for $\mathbb N$.

> [!example] Three classics
> Sum of odds is even (direct); $n^2$ even $\Rightarrow n$ even (contrapositive); $\sqrt2\notin\mathbb Q$ (contradiction: lowest terms $p/q$ with $p^2=2q^2$ forces both even). Errors: affirming the consequent, proving the converse, one example "proving" a $\forall$.

Used in: [[PA01 Logic and Methods of Proof]]. Related: [[Counterexample]] · [[Principle of Mathematical Induction]] · [[Tautology]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
