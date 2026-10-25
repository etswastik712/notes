---
title: Covariance and Correlation
aliases: ["covariance", "correlation coefficient"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Covariance and Correlation

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** the 11–12 Sep sheet remarks that the variance of a sum of independent variables is 'not proved in class'; Blitzstein and Hwang Ch. 7.

> [!intuition] In one picture
> The tendency of two variables to move together.

> [!key] Definition
> $\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y]$; $\rho=\frac{\mathrm{Cov}}{\sigma_X\sigma_Y}\in[-1,1]$; $\mathrm{Var}[\sum X_i]=\sum\mathrm{Var}[X_i]+2\sum_{i<j}\mathrm{Cov}(X_i,X_j)$.

Independent $\Rightarrow\mathrm{Cov}=0$ (so variances add), but $\mathrm{Cov}=0\not\Rightarrow$ independent. Two dice: $\mathrm{Cov}(\text{sum},\text{max})=\frac{35}{12}=2.917$, $\rho=0.860$.

Used in: [[PR04 Joint Distributions Expectation and Variance]]. Related: [[Variance]] · [[Independence of Random Variables]] · [[Linearity of Expectation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
