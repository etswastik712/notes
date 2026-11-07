---
title: Order Statistics
aliases: ["order statistic", "k-th smallest", "sorted sample", "minimum and maximum", "Y(k)"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Order Statistics

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[hw5.pdf#page=1|HW5]], Problems 1–2 (min and max of two; the sorted sample of $n$).
> 🔵 **extra · beyond:** the $k$-th order statistic for general $n$ (my derivation, simulation-checked).

> [!intuition] In one picture
> Sort $n$ independent draws: the sorted values are *dependent* (each is squeezed between its neighbours) even though the draws were independent.

> [!key] Definition
> $Y_{(1)}\le\dots\le Y_{(n)}$ the sorted iid sample (cdf $F$, density $f$). $Y_{(1)}=\min$, $Y_{(n)}=\max$; $f_{Y_{(k)}}=\frac{n!}{(k-1)!(n-k)!}F^{k-1}(1-F)^{n-k}f$; $F_{\max}=F^n$, $F_{\min}=1-(1-F)^n$. Uniform$(0,1)$: $Y_{(k)}\sim\mathrm{Beta}(k,n-k+1)$, mean $\frac{k}{n+1}$.

$n=5$ uniforms: means $\frac16,\frac26,\frac36,\frac46,\frac56$ (simulation $0.1666\ldots0.8334$). $n=3$ uniforms: median density $6y(1-y)$, $P(\text{median}>0.7)=0.216$.

Used in: [[PR08 Order Statistics and the Multinomial Distribution]]. Related: [[Joint Density of Order Statistics]] · [[Exponential Order Statistics]] · [[Cumulative Distribution Function]] · [[Uniform Distribution]] · [[Joint Density Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
