---
title: Fibonacci Numbers
aliases: ["Fibonacci sequence", "golden ratio", "Zeckendorf"]
subject: analysis
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/analysis, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Fibonacci Numbers

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** the standard test case for two-step induction ([[PA08 Mathematical Induction]], [[PA09 Strong Induction and Recursion]]).

> [!intuition] In one picture
> Each term is the sum of the previous two: $1,1,2,3,5,8,13,21,\dots$; rabbits breeding, or the number of ways to climb $n$ steps taking $1$ or $2$.

> [!key] Facts
> $F_{n+2}=F_{n+1}+F_n$, $F_1=F_2=1$. $\varphi^{n-2}\le F_n<2^n$ ($\varphi=\frac{1+\sqrt5}2$, $\varphi^2=\varphi+1$). $F_1+\dots+F_n=F_{n+2}-1$; $\sum F_k^2=F_nF_{n+1}$; Cassini $F_{n+1}F_{n-1}-F_n^2=(-1)^n$; $F_n$ even iff $3\mid n$. **Zeckendorf:** every $n$ is a sum of non-consecutive $F_k$ ($100=89+8+3$). Ratio of consecutive terms $\to\varphi$.

Used in: [[PA08 Mathematical Induction]], [[PA09 Strong Induction and Recursion]]. Related: [[Strong Induction]] · [[Recursion Theorem]] · [[EE02 Structured Population Models]] (Fibonacci's rabbits).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Leslie Matrix]] (Eco-Evo): Fibonacci's rabbits are a two-age-class Leslie model: $N_{t+2}=N_{t+1}+N_t$ is the matrix $\begin{pmatrix}1&1\\1&0\end{pmatrix}$ whose dominant eigenvalue is the golden ratio $\varphi$, the asymptotic growth factor.
