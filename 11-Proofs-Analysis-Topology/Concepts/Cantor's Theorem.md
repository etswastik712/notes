---
title: Cantor's Theorem
aliases: ["|A| < |P(A)|", "power set is larger"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Cantor's Theorem

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-8.pdf#page=1|Assignment 8, Q4]].

> [!intuition] In one picture
> No set is as large as its set of subsets.

> [!key] Definition
> For every $f:A\to\mathcal P(A)$, $B=\{a\in A:a\notin f(a)\}$ is not in the image. So $|A|<|\mathcal P(A)|$ ($a\mapsto\{a\}$ injects).

If $B=f(a_0)$: $a_0\in B\Rightarrow a_0\notin f(a_0)=B$; $a_0\notin B\Rightarrow a_0\in B$. Contradiction either way. Verified on 2000 random $f$ on a 6-set. The tower $\aleph_0<|\mathcal P(\mathbb N)|<|\mathcal P(\mathcal P(\mathbb N))|<\cdots$ and $|\mathcal P(\mathbb N)|=\mathfrak c$.

Used in: [[PA04 Functions and Cardinality]]. Related: [[Power Set]] · [[Russell's Paradox]] · [[Continuum Hypothesis]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
