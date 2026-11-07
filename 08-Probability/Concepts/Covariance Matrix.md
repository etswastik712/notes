---
title: Covariance Matrix
aliases: ["variance-covariance matrix", "quadratic form of variance", "Var of a linear combination"]
subject: probability
type: concept
scope: [taught, extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/book, src/lecture-notes, status/draft]
---
# Covariance Matrix

<span class="scope-taught">taught</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** Homework 4 Q3 ($\mathrm{Var}(\sum c_iX_i)=c^{\mathsf T}Ac$ with $A_{ij}=\mathrm{Cov}(X_i,X_j)$). 🔵 positive semi-definiteness (mine).

> [!intuition] In one picture
> Put every variance on the diagonal and every pairwise co-movement off the diagonal; the variance of any weighted sum is then one matrix product.

> [!key] Key facts
> $A_{ij}=\mathrm{Cov}(X_i,X_j)$ is **symmetric** and **positive semi-definite**: $c^{\mathsf T}Ac=\mathrm{Var}(\sum c_iX_i)\ge0$ for all $c$. Diagonal $=$ variances. Under a linear map $Y=BX$ the matrix becomes $BAB^{\mathsf T}$. A diagonal $A$ means the variables are uncorrelated (independent, for jointly normal variables).

Example: $\mathrm{Var}X=4$, $\mathrm{Var}Y=9$, $\mathrm{Var}Z=1$, $\mathrm{Cov}(X,Y)=3$, $\mathrm{Cov}(X,Z)=-1$, $\mathrm{Cov}(Y,Z)=0$: $\mathrm{Var}(2X-3Y+Z)=58$.

Used in: [[PR07 Sums of Independent Variables Covariance and Correlation]]. Related: [[Covariance and Correlation]] · [[Cauchy-Schwarz Inequality]] · [[08-Probability/Concepts/Variance|Variance]] · [[Linearity of Expectation]] · [[Independence of Random Variables]].


## Continued in the vault (added 2026-11-07)
- A singular example: [[Multinomial Covariance Matrix]] ($n(\mathrm{diag}\,p-pp^{\mathsf T})$, rank $k-1$).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
