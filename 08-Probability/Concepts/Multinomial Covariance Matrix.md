---
title: Multinomial Covariance Matrix
aliases: ["n(diag p - p p^T)", "covariance of multinomial counts", "singular covariance matrix"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Multinomial Covariance Matrix

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[hw5.pdf#page=1|HW5]] Problem 3(b).
> 🔵 **extra · beyond:** rank and eigenvalues (mine).

> [!intuition] In one picture
> The counts must add to $n$, so a big count forces small ones: every off-diagonal entry is negative, and the all-ones direction has zero variance.

> [!key] Definition
> $\Sigma=n\big(\mathrm{diag}(p)-pp^{\mathsf T}\big)$, from the indicator covariances $\mathrm{Cov}(Y_{ij},Y_{kj})=-p_ip_k$ ($i\ne k$), $p_i(1-p_i)$ ($i=k$), and independence across trials. $\Sigma\mathbf 1=0$: rank $k-1$. $\mathrm{Corr}(X_i,X_k)=-\sqrt{p_ip_k/((1-p_i)(1-p_k))}$.

$n=10$, $p=(0.2,0.3,0.5)$: $\Sigma=\begin{pmatrix}1.6&-0.6&-1.0\\-0.6&2.1&-1.5\\-1.0&-1.5&2.5\end{pmatrix}$ (exact enumeration of 66 outcomes), eigenvalues $0,\,2.319,\,3.881$.

Used in: [[PR08 Order Statistics and the Multinomial Distribution]], [[PR07 Sums of Independent Variables Covariance and Correlation]]. Related: [[Multinomial Distribution]] · [[Covariance Matrix]] · [[Covariance and Correlation]] · [[Indicator Random Variable]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
