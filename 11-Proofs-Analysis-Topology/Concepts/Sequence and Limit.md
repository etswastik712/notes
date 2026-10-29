---
title: Sequence and Limit
aliases: ["convergence of sequences", "epsilon-N definition", "limit laws", "subsequence"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Sequence and Limit

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=70|AI notes ch. 16.1]].

> [!intuition] In one picture
> Eventually all terms are as close as you like to $L$.

> [!key] Definition
> $x_n\to L$ iff $\forall\varepsilon>0\,\exists N\,\forall n\ge N:|x_n-L|<\varepsilon$. Negation: $\exists\varepsilon\,\forall N\,\exists n\ge N:|x_n-L|\ge\varepsilon$. Limits are unique; convergent sequences are bounded; sums, products, squeeze.

$\frac{3n+1}{n+2}\to3$ ($|x_n-3|=\frac5{n+2}<\varepsilon\iff n>\frac5\varepsilon-2$). $(-1)^n$ diverges. In a metric space replace $|x_n-L|$ by $d(x_n,L)$; continuity is "preserves limits of sequences".

Used in: [[PA06 The Real Numbers and Sequences]]. Related: [[Quantifiers and Their Negation]] · [[Cauchy Sequence]] · [[Monotone Convergence Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Law of Large Numbers]] (Probability): the law of large numbers is a limit theorem for the sequence of sample means; unlike the real-analysis limit it holds in probability or almost surely, not pointwise.
