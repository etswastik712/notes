---
title: Least Upper Bound Property
aliases: ["completeness of R", "supremum property", "sup and inf"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Least Upper Bound Property

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=66|AI notes ch. 15.1]].

> [!intuition] In one picture
> A set of reals that is bounded above has a tightest upper bound, with no gap.

> [!key] Definition
> An ordered field is **complete** if every non-empty subset bounded above has a least upper bound $\sup S$ in it. $\mathbb R$ is the complete ordered field (unique up to isomorphism); $\mathbb Q$ is not.

$S=\{q\in\mathbb Q:q>0,q^2<2\}$: if $u$ were its lub, $u'=\frac{2u+2}{u+2}$ with $u'^2-2=\frac{2(u^2-2)}{(u+2)^2}$ gives a member larger than $u$ (if $u^2<2$) or a smaller upper bound (if $u^2>2$). Hence no rational sup. In $\mathbb R$, $\sup S=\sqrt2$.

Used in: [[PA06 The Real Numbers and Sequences]]. Related: [[Extremal Elements and Bounds]] · [[Dedekind Cut]] · [[Archimedean Property]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
