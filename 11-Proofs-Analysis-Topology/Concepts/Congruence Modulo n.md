---
title: Congruence Modulo n
aliases: ["modular arithmetic", "congruence classes", "Z/n"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Congruence Modulo n

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-5.pdf#page=1|Assignment 5]].

> [!intuition] In one picture
> Clock arithmetic: integers with the same remainder are identified.

> [!key] Definition
> $a\equiv b\pmod n\iff n\mid a-b$; $n$ classes $[0],\dots,[n-1]$; $a\equiv b,c\equiv d\Rightarrow a+c\equiv b+d$ and $ac\equiv bd$, so $[a]+[b]=[a+b]$, $[a][b]=[ab]$ are well defined.

$3^{16}\equiv(-1)^{16}=1\pmod4$; $7^{100}\equiv9\pmod{13}$; last digit of $3^{2026}$ is 9; squares are $\equiv0,1\pmod4$. In $\mathbb Z/{\equiv_5}$: $[5]+[-1]=[4]$, $[2][5]=[0]$.

Used in: [[PA03 Relations Equivalence and Order]]. Related: [[Equivalence Relation]] · [[Principle of Mathematical Induction]] · [[Construction of Integers and Rationals]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
