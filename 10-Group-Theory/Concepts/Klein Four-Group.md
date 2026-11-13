---
title: Klein Four-Group
aliases: ["V_4", "Z_2 x Z_2", "symmetries of a rectangle", "Vierergruppe"]
subject: group-theory
type: concept
by: [lecture-notes, own-notes]
status: draft
tags: [subject/group-theory, type/concept, src/lecture-notes, src/own-notes, status/draft, quiz/pa-groups]
---
# Klein Four-Group

> [!info] Source
> [[Assignment-10.pdf]] Problem 4(c) (symmetries of a non-square rectangle); written up in [[GT01 Groups Subgroups and Cosets]].

> [!intuition] In one picture
> The symmetries of a rectangle that is not a square: do nothing, flip left–right, flip up–down, turn by a half-turn. Doing any move twice undoes it, and the product of two flips is the third move.

> [!key] Key facts
> - $V_4=\{e,a,b,ab\}$ with $a^2=b^2=(ab)^2=e$, i.e. $\mathbb Z_2\times\mathbb Z_2$; **abelian of order 4 with no element of order 4**, so **not cyclic** (contrast $\mu_4\cong\mathbb Z_4$).
> - As permutations of the rectangle's vertices $1,2,3,4$ (cyclic order): $e$, $(1\,3)(2\,4)$, $(1\,2)(3\,4)$, $(1\,4)(2\,3)$ (verified by machine).
> - Normal subgroup of $S_4$ and of $A_4$ (the double transpositions); the square has a larger group, $D_4$, of order 8 and non-abelian.

Used in: [[GT01 Groups Subgroups and Cosets]]. Related: [[Dihedral Group]] · [[Direct Product of Groups]] · [[Symmetric Group]] · [[Cyclic Group]] · [[Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
