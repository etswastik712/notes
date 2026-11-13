---
title: Jensen's Inequality
aliases: ["Jensen inequality", "E g(X) >= g(E X)", "convex function inequality", "tangent line below the graph", "AM-GM from Jensen"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft, quiz/probability, quiz/pr-hw6]
---
# Jensen's Inequality

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[hw6_edited.pdf#page=1|HW6]] Q3: the tangent line of $g$ with $g''>0$ lies below the graph (the sheet says this is used in the proof of Jensen).
> 🔵 **extra · beyond:** Jensen's inequality from the lemma, the quantitative form, AM–GM (mine).

> [!intuition] In one picture
> A convex curve sags below its chords and **sits above its tangents**; averaging the inequality 'curve $\ge$ tangent at the mean' over the random variable gives 'average of the curve $\ge$ curve at the average'.

> [!key] Definition
> **Lemma:** $g''>0\Rightarrow g(x)>g(a)+g'(a)(x-a)$ for $x\ne a$ ($h=g-\text{tangent}$ has $h'$ increasing through $0$ at $a$). **Jensen:** $g$ convex $\Rightarrow E[g(X)]\ge g(E[X])$ (take $a=E X$, expectation of $g(X)\ge g(\mu)+g'(\mu)(X-\mu)$); equality iff $X$ constant when $g''>0$. If $g''\ge m>0$: $E g(X)-g(EX)\ge\frac m2\operatorname{Var}X$.

$g=x^2$: $\operatorname{Var}X\ge0$. $g=e^{tx}$: $M_X(t)\ge e^{tEX}$. $g=-\ln$: AM–GM ($(1,4,16)$: GM $4\le$ AM $7$). $X\sim N(0,1)$: $E e^X=e^{1/2}=1.6487\ge1$. $e^x\ge ex$ with equality only at $x=1$, so $\ln x\le x/e$.

Used in: [[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]], [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Expectation]] · [[Variance]] · [[Moment Generating Function]] · [[Law of the Unconscious Statistician]] · [[Markov and Chebyshev Inequalities]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
