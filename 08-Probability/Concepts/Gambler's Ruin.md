---
title: Gambler's Ruin
aliases: ["random walk with absorbing barriers", "gambler ruin"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Gambler's Ruin

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** set on [[Practice problems 21st August 2026.pdf#page=3|the 21 Aug sheet, problem 9]], but the 27 Aug notes say it is "not formally a part of the syllabus".

> [!intuition] In one picture
> A gambler with $i$ units keeps playing fair or biased rounds until reaching $n$ or going broke.

> [!key] Definition
> With win probability $p$ per round and $\rho=\frac{1-p}p$, $P[\text{bankrupt from }i]=p_i=\dfrac{\rho^i-\rho^n}{1-\rho^n}$ ($p\ne\tfrac12$), $p_i=1-\frac in$ ($p=\tfrac12$).

## Derivation
Condition on the first round: $p_i=p\,p_{i+1}+(1-p)p_{i-1}$ with $p_0=1$, $p_n=0$. With $d_i=p_i-p_{i-1}$, $d_{i+1}=\rho d_i$, so $p_i=1+d_1(1+\rho+\dots+\rho^{i-1})$ and $p_n=0$ fixes $d_1$.

## Numbers ($i=3$, $n=10$)
$p=\tfrac12$: bankrupt $0.70$; $p=0.6$: $0.284$; $p=0.4$: $0.958$. For $i=4$, $n=10$ and $p=0.45$ the chance of reaching 10 is $0.191$.

Used in: [[PR02 Conditional Probability Bayes Rule and Independence]]. Related: [[Law of Total Probability]] · [[Conditional Probability]] · [[Standardisation of a Random Variable]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
