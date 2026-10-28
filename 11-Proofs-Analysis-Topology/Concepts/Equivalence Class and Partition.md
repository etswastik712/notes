---
title: Equivalence Class and Partition
aliases: ["partition", "Bell number"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Equivalence Class and Partition

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-prems_merged.pdf#page=1|Assignment 4, Q8(c), Q9]].

> [!intuition] In one picture
> Equivalence relations and partitions are the same data.

> [!key] Definition
> A **partition** of $A$ is a family of non-empty, pairwise disjoint sets whose union is $A$. $\sim\ \mapsto\ A/{\sim}$ and $P\mapsto(x\sim_Py\iff x,y\text{ in one block})$ are inverse. The number of partitions of an $n$-set is the Bell number $1,1,2,5,15,52,203$.

Proof: classes cover because $a\in[a]$; two classes meeting at $z$ coincide since $a\sim z\sim b$. The five partitions of $\{1,2,3\}$: $\{123\}$, three of type $\{ab\}\{c\}$, and $\{1\}\{2\}\{3\}$. A partition of the sample space is exactly the hypothesis of the law of total probability.

Used in: [[PA03 Relations Equivalence and Order]]. Related: [[Equivalence Relation]] · [[Congruence Modulo n]] · [[Law of Total Probability]].

> [!connection] Group theory used here
> Lagrange's theorem is the statement that cosets partition a group into equal pieces: [[GT01 Groups Subgroups and Cosets]]; see [[Where Groups Appear in the Vault]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
