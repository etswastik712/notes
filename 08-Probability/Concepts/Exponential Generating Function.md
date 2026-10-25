---
title: Exponential Generating Function
aliases: ["EGF", "egf of the moments", "generating function (exponential)"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Exponential Generating Function

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Week3_notes.pdf#page=2|Week 3, p.2]] (the bracketed remark on combinatorics). · 🔵 **extra · beyond:** examples.

> [!intuition] In one picture
> Pack a sequence $a_0,a_1,a_2,\dots$ into one power series, with $n!$ in the denominators so that derivatives give back the numbers.

> [!key] Definition
> $\mathrm{EGF}(\{a_n\})(x)=\displaystyle\sum_{n\ge0}a_n\frac{x^n}{n!}$, so $a_n=\dfrac{\mathrm d^n}{\mathrm dx^n}\mathrm{EGF}\Big|_{x=0}$. The **MGF is the EGF of the moments**: $M_X(t)=\sum E[X^n]\,t^n/n!$.

## Examples
$a_n=1$: $\sum x^n/n!=e^x$. $a_n=n!$: $\sum x^n=\frac1{1-x}$ (this is the **exponential MGF** $\lambda/(\lambda-t)$ with $x=t/\lambda$, whose moments are $n!/\lambda^n$). $a_n=p$ ($n\ge1$), $a_0=1$: $1+p(e^x-1)=q+pe^x$ (the Bernoulli MGF). $a_{2k}=\frac{(2k)!}{k!2^k}$, odd $0$: $e^{x^2/2}$ (the $N(0,1)$ MGF).

> [!pitfall] Ordinary versus exponential
> The ordinary generating function $\sum a_nx^n$ (used for probabilities in the pgf) differs from the EGF by the $n!$; moments need the EGF.

Used in: [[PR06 Moments Generating Functions and Limit Theorems]] §2. Related: [[Moment Generating Function]] · [[Moments of a Random Variable]] · [[Counting Principles]] · [[Hermite Generating Function and Recurrences]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
