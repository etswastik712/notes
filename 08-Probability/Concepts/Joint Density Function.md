---
title: Joint Density Function
aliases: ["joint pdf", "joint density", "two continuous random variables"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Joint Density Function

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** no lecture note in the folder; the instructor's Homework 4 uses it implicitly (the convolution formula). Ross §6.1–6.2; Blitzstein and Hwang Ch. 7.

> [!intuition] In one picture
> A pdf makes probability an area under a curve; a joint pdf makes it the volume above a region of the plane.

> [!key] Definition
> $f(x,y)\ge0$ with $\iint f=1$ and $P[(X,Y)\in B]=\iint_Bf$. Marginals $f_X(x)=\int f(x,y)\mathrm dy$. **Independent iff $f=f_Xf_Y$.** $E[g(X,Y)]=\iint gf$.

A support that is not a rectangle already rules out independence (uniform on a disc: $\mathrm{Cov}=0$ but dependent).

Used in: [[PR07 Sums of Independent Variables Covariance and Correlation]]. Related: [[Joint Distribution]] (the discrete twin) · [[Marginal Distribution]] · [[Independence of Random Variables]] · [[Continuous Random Variable]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
