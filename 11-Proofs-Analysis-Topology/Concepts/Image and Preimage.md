---
title: Image and Preimage
aliases: ["pre-image", "inverse image", "f(S)", "f^{-1}(T)"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Image and Preimage

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-6.pdf#page=1|Assignment 6, Defs 1–2]].

> [!intuition] In one picture
> Where $S$ is sent / what is sent into $T$; the preimage exists for every function.

> [!key] Definition
> $f(S)=\{f(a):a\in S\}$; $f^{-1}(T)=\{a\in A:f(a)\in T\}$. $f^{-1}$ of a union/intersection is the union/intersection of preimages; $f(f^{-1}(T))\subseteq T$ with equality if $f$ is onto.

$f(x)=x^2$: $f^{-1}(4)=\{\pm2\}$, $f^{-1}(-1)=\varnothing$, $f([-2,1])=[0,4]$, $f^{-1}([1,4])=[-2,-1]\cup[1,2]$, $f(f^{-1}([-1,4]))=[0,4]\ne[-1,4]$. Preimages are the basis of continuity: $f$ is continuous iff preimages of open sets are open.

Used in: [[PA04 Functions and Cardinality]]. Related: [[Function]] · [[Continuous Function (Topological)]] · [[Injective Surjective and Bijective Functions]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
