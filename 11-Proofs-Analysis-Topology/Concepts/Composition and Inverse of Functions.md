---
title: Composition and Inverse of Functions
aliases: ["composite", "inverse function", "g after f"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Composition and Inverse of Functions

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-7.pdf#page=1|Assignment 7 (used throughout)]].

> [!intuition] In one picture
> Do $f$ then $g$; undo by running backwards.

> [!key] Definition
> $(g\circ f)(a)=g(f(a))$. A composite of bijections is a bijection; $f$ is a bijection iff $\exists g$ with $g\circ f=\mathrm{id}_A$ and $f\circ g=\mathrm{id}_B$. $g\circ f$ injective $\Rightarrow f$ injective; $g\circ f$ surjective $\Rightarrow g$ surjective.

Used to show $\sim$ is transitive. Lecture 20: $g\circ f=\mathrm{id}_{(0,1)}$ and $f\circ g=\mathrm{id}_{\mathbb R}$ for the bijection $(0,1)\leftrightarrow\mathbb R$ (checked on 96 and 81 rational points). Counterexample for the converse: $f:\{1\}\to\{1,2\}$ and a constant $g$.

Used in: [[PA04 Functions and Cardinality]]. Related: [[Injective Surjective and Bijective Functions]] · [[Cardinality]] · [[Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
