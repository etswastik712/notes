---
title: Cauchy Sequence
aliases: ["Cauchy criterion", "complete metric space"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Cauchy Sequence

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=71|AI notes ch. 16.2 and 17.3]].

> [!intuition] In one picture
> The terms get arbitrarily close to **each other**: a convergence test that does not mention the limit.

> [!key] Definition
> $\forall\varepsilon\,\exists N\,\forall m,n\ge N:|x_m-x_n|<\varepsilon$. In $\mathbb R$: Cauchy $\iff$ convergent. A metric space is **complete** if every Cauchy sequence converges: $\mathbb R$ yes; $\mathbb Q$, $(0,1)$ no.

Newton's rationals $1,\frac32,\frac{17}{12},\frac{577}{408},\dots$ are Cauchy in $\mathbb Q$ with no limit there. $H_{2n}-H_n\ge\frac12$: the harmonic partial sums are not Cauchy, while $\sum1/k^2$ is (tail $<\frac1{100}$ after 100 terms). $(-1)^n$ is not Cauchy.

Used in: [[PA06 The Real Numbers and Sequences]]. Related: [[Bolzano-Weierstrass Theorem]] · [[Metric Space]] · [[Sequence and Limit]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
