---
title: Euler Totient Function
aliases: ["Euler phi", "totient", "phi(n)"]
subject: group-theory
type: concept
by: [book, own-notes]
status: draft
tags: [subject/group-theory, type/concept, src/book, status/draft]
---
# Euler Totient Function

> [!info] Source
> Kurzweil–Stellmacher; written up in [[GT03 Cyclic and Abelian Groups and Direct Products]].

> [!intuition] In one picture
> $\varphi(n)$ counts the integers $1\le k\le n$ coprime to $n$: the number of generators of $C_n$ and the order of $(\mathbb Z/n)^\times=\operatorname{Aut}(C_n)$.

> [!key] Key facts
> $\sum_{d\mid n}\varphi(d)=n$; $\varphi(p^k)=p^{k-1}(p-1)$; multiplicative on coprime arguments; Euler: $a^{\varphi(n)}\equiv1\pmod n$ (Lagrange in $(\mathbb Z/n)^\times$).

## In this vault
RSA-type arguments; counting generators of a clock.

Used in: [[GT03 Cyclic and Abelian Groups and Direct Products]]. Related: [[Cyclic Group]] · [[Primitive Root]] · [[Automorphism Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
