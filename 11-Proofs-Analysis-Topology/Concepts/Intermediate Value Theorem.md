---
title: Intermediate Value Theorem
aliases: ["IVT", "Bolzano's theorem"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Intermediate Value Theorem

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=79|AI notes ch. 18.5]].

> [!intuition] In one picture
> A continuous function cannot jump over a value.

> [!key] Definition
> If $f:[a,b]\to\mathbb R$ is continuous and $f(a)<c<f(b)$ (or reverse), then $f(x)=c$ for some $x$. Proof: $f([a,b])$ is connected, hence an interval containing $f(a),f(b)$.

Bisection: $\cos x=x$ has root $0.73908513$ (40 halvings for $10^{-12}$); $x^3+x-1$: bracket $[0.6797,0.6836]$ after 8 steps (root $0.68233$). A continuous $f:[0,1]\to[0,1]$ has a fixed point ($g=f-\mathrm{id}$ has $g(0)\ge0\ge g(1)$).

Used in: [[PA07 Metric and Topological Spaces]]. Related: [[Connected Space]] · [[Fixed Points and Linear Stability]] · [[Bistability and Tipping Points]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
