---
title: Hypergeometric Distribution
aliases: ["hypergeometric", "sampling without replacement"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Hypergeometric Distribution

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=20|class notes 20 Aug]], [[Practice problems 28th August and following weekend.pdf#page=1|sheet 28 Aug, problem 4]].

> [!intuition] In one picture
> The binomial's cousin when you sample without putting back: dependent draws, same mean.

> [!key] Definition
> Urn with $w$ white, $b$ black; $n$ drawn without replacement; $X$ = whites: $P[X=k]=\dfrac{\binom wk\binom b{n-k}}{\binom{w+b}n}$, $E[X]=\dfrac{nw}{w+b}$.

## Mean
$X=\sum_{i=1}^n\mathbf 1\{\text{draw }i\text{ white}\}$, and by [[Exchangeability]] each draw is white with probability $\frac w{w+b}$, so $E[X]=\frac{nw}{w+b}$.

> [!example] With vs without replacement
> 100 slips, 21 of them $\ge80$, five drawn: with replacement $P[X=0]=0.79^5=0.3077$; without $\binom{79}5/\binom{100}5=0.2994$. The without-replacement law is narrower (less variance), as in Figure PR3.1.

Used in: [[PR03 Discrete Random Variables and Distributions]]. Related: [[Binomial Distribution]] · [[Exchangeability]] · [[Linearity of Expectation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
