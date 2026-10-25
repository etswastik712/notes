---
title: Archimedean Property
aliases: ["Archimedean", "density of the rationals"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Archimedean Property

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=68|AI notes ch. 15.3]].

> [!intuition] In one picture
> No real number is larger than every natural number.

> [!key] Definition
> $\mathbb N$ is not bounded above in $\mathbb R$: for $x,y>0$ some $n$ has $nx>y$. Consequences: $\inf\{\frac1n\}=0$; between any two reals there is a rational (and an irrational).

Proof: if $s=\sup\mathbb N$, some $n>s-1$ and $n+1>s$. Density: choose $n(y-x)>1$ and the least integer $m>nx$; then $x<\frac mn<y$. $\bigcap_n(0,\frac1n)=\varnothing$ and $\bigcap_n(-\frac1n,\frac1n)=\{0\}$ rest on it; so does $0.999\dots=1$.

Used in: [[PA06 The Real Numbers and Sequences]]. Related: [[Least Upper Bound Property]] · [[Principle of Mathematical Induction]] · [[Sequence and Limit]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
