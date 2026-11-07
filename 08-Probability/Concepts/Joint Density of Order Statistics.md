---
title: Joint Density of Order Statistics
aliases: ["joint density of the sorted sample", "n! f(y1)...f(yn)", "min and max joint density", "two preimages"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, src/own-notes, status/draft]
---
# Joint Density of Order Statistics

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[hw5.pdf#page=1|HW5]] Problem 1 and the instructor's solution [[HW-5, Q.1.jpg]].

> [!intuition] In one picture
> Sorting forgets the labels: $n!$ different orderings of the labels give the same sorted vector, so the density on the ordered region is $n!$ times the product density.

> [!key] Definition
> For iid $X_i$ with density $f$: $f_{Y_1,\dots,Y_n}(y_1,\dots,y_n)=n!\,f(y_1)\cdots f(y_n)$ on $y_1<\dots<y_n$ ($0$ elsewhere). For $n=2$: $f_{Y_1,Y_2}=2f(y_1)f(y_2)$, proved by the two preimages $(y_1,y_2),(y_2,y_1)$ or by $F_{Y_1,Y_2}=2F(y_1)F(y_2)-F(y_1)^2$ and $\partial^2/\partial y_1\partial y_2$.

Check: Expo(1), $y_1=0.5,y_2=1.2$: cdf formula $0.39510$ vs simulation $0.39502$; $\iint_{y_1<y_2}2f f=1$.

Used in: [[PR08 Order Statistics and the Multinomial Distribution]]. Related: [[Order Statistics]] · [[Cdf Method for Transformations]] · [[Joint Density Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
