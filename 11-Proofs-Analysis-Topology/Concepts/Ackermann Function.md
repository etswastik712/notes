---
title: Ackermann Function
aliases: ["Ackermann-Peter function", "total recursive function that is not primitive recursive"]
subject: analysis
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/analysis, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Ackermann Function

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** [[PA10 Well-Ordering and Well-Ordered Pairs]] §5.

> [!intuition] In one picture
> A recursion whose arguments can grow wildly, yet which must stop because every call lowers the pair **lexicographically**.

> [!key] Definition
> $A(0,n)=n+1$, $A(m+1,0)=A(m,1)$, $A(m+1,n+1)=A(m,A(m+1,n))$. $A(1,n)=n+2$, $A(2,n)=2n+3$, $A(3,n)=2^{n+3}-3$; $A(3,3)=61$ (2432 calls). Termination is induction on $(\mathbb N\times\mathbb N,\text{lex})$; no single-number induction works.

Used in: [[PA10 Well-Ordering and Well-Ordered Pairs]]. Related: [[Lexicographic Order]] · [[Recursion Theorem]] · [[Well-Ordered Set]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
