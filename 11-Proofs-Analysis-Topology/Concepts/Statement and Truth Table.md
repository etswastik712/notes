---
title: Statement and Truth Table
aliases: ["proposition", "truth table", "connectives"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Statement and Truth Table

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-prems_merged.pdf#page=7|Assignment 1]].

> [!intuition] In one picture
> A statement is true or false; a truth table lists the truth value of a compound under every assignment.

> [!key] Definition
> A **statement** is a sentence that is true or false, not both. Connectives $\neg,\wedge,\vee,\Rightarrow,\Leftrightarrow$ have fixed tables; with $n$ variables a truth table has $2^n$ rows. $\vee$ is inclusive; $P\Rightarrow Q$ is false only for ($P$ true, $Q$ false).

$x>0$ is a predicate, not a statement, until $x$ is given a value or quantified. The $2^{2^n}$ truth functions of $n$ variables are $4,16,256,65536$; $\{\neg,\wedge\}$ generates all 16 two-variable ones.

> [!example] $(P\vee Q)\wedge(P\vee R)$
> True in rows 1–5 (every row with $P$ true, plus $Q$ and $R$ both true): the column of $P\vee(Q\wedge R)$.

Used in: [[PA01 Logic and Methods of Proof]]. Related: [[Logical Equivalence]] · [[11-Proofs-Analysis-Topology/Concepts/Tautology|Tautology]] · [[Conditional Statement]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
