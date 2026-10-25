---
title: Power Set
aliases: ["subsets", "empty set", "|P(A)|=2^n"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Power Set

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-prems_merged.pdf#page=3|Assignment 3, Q1–Q3]].

> [!intuition] In one picture
> All the subsets of a set; each element is in or out.

> [!key] Definition
> $\mathcal P(A)=\{S:S\subseteq A\}$; $|A|=n\Rightarrow|\mathcal P(A)|=2^n$ (subsets $\leftrightarrow$ 0–1 strings). $\varnothing\subseteq A$ for every $A$ (vacuous truth).

$\mathcal P(\varnothing)=\{\varnothing\}$ has $2^0=1$ element; $\mathcal P(\mathcal P(\{a,b\}))$ has $2^4=16$. An $n$-set has $\binom n2$ two-element subsets, $2^{n-1}$ even-sized subsets ($n\ge1$). Cantor: $|A|<|\mathcal P(A)|$ for every set, including infinite ones.

Used in: [[PA02 Sets Families and the ZFC Foundations]]. Related: [[Cantor's Theorem]] · [[Set Operations and De Morgan's Laws]] · [[Cartesian Product]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
