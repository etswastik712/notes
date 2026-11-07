---
title: Exponential Order Statistics
aliases: ["Renyi representation", "gaps of exponential order statistics", "minimum of exponentials", "HW5 Problem 2"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Exponential Order Statistics

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[hw5.pdf#page=1|HW5]] Problem 2 ($n=2$).
> 🔵 **extra · beyond:** the general-$n$ spacings (my argument by repeated memorylessness, simulation-checked).

> [!intuition] In one picture
> $n$ independent alarm clocks: the first rings at rate $n\lambda$; after that the survivors are "as good as new" (memoryless), so the next ring comes at rate $(n-1)\lambda$, and so on.

> [!key] Definition
> For iid $\mathrm{Expo}(\lambda)$: $Y_{(k)}-Y_{(k-1)}\sim\mathrm{Expo}((n-k+1)\lambda)$, independent; $E[Y_{(k)}]=\frac1\lambda\sum_{j=1}^k\frac{1}{n-j+1}$, $E[\max]=H_n/\lambda$. For $n=2$: $Y_1\sim\mathrm{Expo}(2\lambda)$, $Y_2-Y_1\sim\mathrm{Expo}(\lambda)$ independent of $Y_1$; $\mathrm{Var}\,Y_2=\frac5{4\lambda^2}$, $\mathrm{Corr}(Y_1,Y_2)=\frac1{\sqrt5}$.

Two parallel components, $\lambda=0.1$/h: first failure at $5$ h, system failure at $15$ h on average, $P(\text{gap}>10\,\text{h})=e^{-1}=0.368$. $n=5$: mean gaps $0.2,0.25,0.333,0.5,1$ and $E\max=2.2833$.

Used in: [[PR08 Order Statistics and the Multinomial Distribution]]. Related: [[Order Statistics]] · [[Memoryless Property]] · [[Exponential Distribution]] · [[Independence of Random Variables]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
