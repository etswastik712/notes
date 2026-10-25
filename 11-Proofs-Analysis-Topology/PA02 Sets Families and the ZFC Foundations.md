---
title: PA02 Sets Families and the ZFC Foundations
aliases: [PA02, sets, power set, De Morgan, indexed families, Cartesian product, ordered pairs, Kuratowski, ZFC, Russell's paradox, Assignment 3]
subject: analysis
type: chapter
chapter: 2
part: II
scope: [taught, extra-book, extra-beyond]
by: [lecture-notes, ai-notes]
status: draft
prereq: [PA01 Logic and Methods of Proof]
tags: [subject/analysis, type/chapter, taught, extra/book, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# PA02 · Sets, Families and the ZFC Foundations

◀ [[PA01 Logic and Methods of Proof]] · [[PA03 Relations Equivalence and Order]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**: [[Assignment-prems_merged.pdf#page=3|Assignment 3]] (PDF p.3–4: sets, subsets, power set, Venn diagrams, De Morgan, products, indexed unions, intersections and products) and the instructor's note [[ordered pairs.pdf|Ordered Pairs in ZFC: Why the Kuratowski Definition Works]] (8 pp.).
> - §1 sets, subsets, the empty set, power sets and $|\mathcal P(A)|=2^n$
> - §2 the algebra of sets, De Morgan's laws, the logic–set dictionary
> - §3 Cartesian products, indexed families: $\bigcup,\bigcap,\prod$ of sequences of sets
> - §4 ordered pairs: what they must do, what fails, why Kuratowski works
>
> 🟡 **Extra · book** (AI notes `proofs-prems-topo.pdf` Part II)
> - §5 Russell's paradox and the ZFC axioms; how the basic constructions come from the axioms
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §4 a **brute-force test** of five candidate pair definitions on all sets of rank 3 (`scripts/pa_numbers.py`)

> [!key] After this chapter you can
> - prove a set identity by the **direct (element-chasing) method** and recognise vacuous truths such as $\varnothing\subseteq A$,
> - count subsets ($|\mathcal P(A)|=2^n$) and describe $\bigcup_nA_n$, $\bigcap_nA_n$, $\prod_nA_n$ for a given sequence of sets,
> - explain why $\{A,B\}$ cannot be an ordered pair and prove that the **Kuratowski pair** $\{\{A\},\{A,B\}\}$ satisfies $(A,B)=(C,D)\iff A=C\wedge B=D$,
> - say why axioms are needed (Russell) and name the ZFC axioms.

> [!intuition] The one-sentence story
> A set is determined by its members and by nothing else; every other mathematical object (pairs, relations, functions, numbers) is a set built from the empty set, and the ordered pair is the first nontrivial piece of that construction.

## 1. Sets, subsets and the power set
<span class="scope-taught">taught</span> *Assignment 3, questions 1–3*

A set is determined by its elements. $A\subseteq B$ means $\forall x\,(x\in A\Rightarrow x\in B)$; the assignments write $\subset$ for this (so $A\subset A$ is allowed) and $\varphi$ for the empty set; I write $\subseteq$ and $\varnothing$ and use $A\subsetneq B$ for a proper subset.

> [!example] $\varnothing\subseteq A$ (Assignment 3 Q1)
> For every $x$, the statement $x\in\varnothing\Rightarrow x\in A$ is true because its hypothesis is false (**vacuous truth**). So the empty set is a subset of every set.

> [!example] Subsets of $\mathbb R[X]$ (Q2)
> Let $\mathbb R[X]=\{a_nX^n+\dots+a_1X+a_0:a_i\in\mathbb R\}$. Take $S_1=\{X,\,X+1\}$ and $S_2=\{X+1,\,X^2\}$: $S_1\cap S_2=\{X+1\}$ and $S_1\cup S_2=\{X,X+1,X^2\}$. An infinite example: $S_1$ = polynomials with zero constant term, $S_2$ = polynomials containing only even powers of $X$; then $S_1\cap S_2$ = even polynomials with no constant term and $S_1\cup S_2$ is the set of polynomials that either vanish at 0 or are even.

> [!key] Power set
> $\mathcal P(A)=\{S:S\subseteq A\}$. If $|A|=n$ then $|\mathcal P(A)|=2^n$ (Assignment 3 Q3).

> [!derivation] Why $2^n$
> A subset $S\subseteq A=\{a_1,\dots,a_n\}$ is determined by deciding, for each $a_i$, whether $a_i\in S$: $n$ independent yes/no choices, so $2\cdot2\cdots2=2^n$ subsets (formally: $S\mapsto(\mathbf 1_S(a_1),\dots,\mathbf 1_S(a_n))$ is a bijection to $\{0,1\}^n$). Check: $n=0$: $\mathcal P(\varnothing)=\{\varnothing\}$ has $1=2^0$ element; verified by listing all subsets for $n\le8$.

## 2. The algebra of sets
<span class="scope-taught">taught</span> *Assignment 3, questions 4–6*

$A\cup B$, $A\cap B$, $A\setminus B$ (written $A-B$ in the assignments), $A^c=X\setminus A$ for a fixed ambient set $X$. 

> [!key] The logic–set dictionary
> | logic | sets | | logic | sets |
> |---|---|---|---|---|
> | $\wedge$ | $\cap$ | | $P\Rightarrow Q$ | $\{P\}\subseteq\{Q\}$ |
> | $\vee$ | $\cup$ | | $P\Leftrightarrow Q$ | $\{P\}=\{Q\}$ |
> | $\neg$ | complement | | tautology | the whole set $X$ |
> | De Morgan | De Morgan | | contradiction | $\varnothing$ |
>
> Every identity of PA01 becomes a set identity; every set identity is proved by **chasing an element** through the corresponding logical equivalence.

> [!derivation] De Morgan, direct method (Q5)
> $x\in(A\cap B)^c\iff\neg(x\in A\wedge x\in B)\iff x\notin A\vee x\notin B\iff x\in A^c\cup B^c$. The step in the middle is De Morgan's law for statements. Likewise $x\in(A\cup B)^c\iff x\notin A\wedge x\notin B\iff x\in A^c\cap B^c$.

> [!example] Products (Q6)
> (a) If $T\subseteq A$ then $T\times B\subseteq A\times B$: a point $(t,b)$ with $t\in T\subseteq A$, $b\in B$ lies in $A\times B$.
> (b) $A\times(B\cup C)=(A\times B)\cup(A\times C)$: $(a,x)\in A\times(B\cup C)\iff a\in A\wedge(x\in B\vee x\in C)\iff(a\in A\wedge x\in B)\vee(a\in A\wedge x\in C)$ (distributivity).

> [!example] Venn diagrams (Q4)
> $A\cap B^c$ is the part of $A$ outside $B$ (the same as $A\setminus B$); $(A\cap B)^c$ is everything except the lens $A\cap B$, i.e. $A^c\cup B^c$ (all regions but the overlap). Drawing two overlapping discs in a box and shading shows the three regions at once.

## 3. Indexed families and products
<span class="scope-taught">taught</span> *Assignment 3, questions 7–12*

For sets $A_n$, $n\in\mathbb N$ (an **indexed family**): $\bigcup_nA_n=\{x:\exists n\ x\in A_n\}$, $\bigcap_nA_n=\{x:\forall n\ x\in A_n\}$, and $\prod_nA_n=\{(a_1,a_2,\dots):a_n\in A_n\ \forall n\}$, the set of all **sequences** whose $n$-th term lies in $A_n$.

| Q | $A_n$ | $\bigcup_nA_n$ | $\bigcap_nA_n$ | notes |
|---|---|---|---|---|
| 7 | $(-\tfrac1n,\tfrac1n)$ | $(-1,1)$ | $\{0\}$ | decreasing; $\prod$ = sequences with $\lvert a_n\rvert<\tfrac1n$ |
| 8 | $\{1,\dots,n\}$ | $\mathbb N$ | $\{1\}$ | $\prod$: $a_n\in\{1,\dots,n\}$; $(1,2,3,\dots)$ and $(1,1,1,\dots)$ belong, $(2,2,2,\dots)$ does not ($a_1$ must be 1) |
| 9 | $[-n,\,1-\tfrac1n)$ | $(-\infty,1)$ | $[-1,0)$ | $A_n\subseteq A_{n+1}$, so $\bigcap=A_1$ |
| 10 | $H_n=\{(x,y):y\ge-n\}\subset\mathbb R^2$ | $\mathbb R^2$ | $H_1=\{y\ge-1\}$ | increasing: $\bigcap=H_1$ |

> [!derivation] Q7 and Q9 in detail
> *Q7.* $x\in\bigcup A_n$ iff $|x|<1/n$ for some $n$; the largest interval is $A_1=(-1,1)$ (they are nested), so $\bigcup=(-1,1)$. $x\in\bigcap A_n$ iff $|x|<1/n$ for all $n$; by the Archimedean property only $x=0$ qualifies.
> *Q9.* $A_n=[-n,1-\tfrac1n)$ increases with $n$. Given $x<1$, pick $n\ge-x$ and $n>1/(1-x)$; then $x\in A_n$. And $1\notin A_n$ for any $n$. So $\bigcup=(-\infty,1)$ while $\bigcap=A_1=[-1,0)$.

> [!example] Q11: a basis of an infinite product
> $\mathbb R$ is a vector space over $\mathbb R$; for finite products $\prod_{n=1}^r\mathbb R=\mathbb R^r$ the vectors $e_1,\dots,e_r$ form a basis. For $\prod_{n=1}^\infty\mathbb R$ the set $\{e_1,e_2,\dots\}$ is **not** a basis: linear combinations are finite, so $(1,1,1,\dots)$ is not in the span. (A basis exists anyway by Zorn's lemma, [[PA03 Relations Equivalence and Order]], but it cannot be written down.)

> [!example] Q12: an empty set in the family
> If $A_k=\varnothing$ for some $k$, then $\bigcap_nA_n=\varnothing$ (nothing lies in $A_k$) and $\prod_nA_n=\varnothing$ (no sequence can have $a_k\in\varnothing$), while $\bigcup_nA_n=\bigcup_{n\ne k}A_n$.

> [!pitfall] $\prod A_n$ is not a union
> An element of $\prod A_n$ is an **entire sequence**, one entry from each $A_n$; an element of $\bigcup A_n$ is a single point.

## 4. Ordered pairs
<span class="scope-taught">taught</span> *the instructor's note [[ordered pairs.pdf|Ordered Pairs in ZFC]]*

An ordered pair must satisfy one property:

> [!key] The property (OP)
> $(A,B)=(C,D)\iff A=C\wedge B=D$. It must remember which entry is first. (It is **not** required that $(A,B)\ne(B,A)$ for all $A,B$ — they are equal if $A=B$ — nor that $(A,A)\ne\{A\}$; the latter happens to hold for Kuratowski pairs but is a consequence, not the defining property.)

**Test for any proposal $F(A,B)$:** does $F(A,B)=F(C,D)$ imply $A=C$ and $B=D$? A single failure disqualifies it.

> [!example] Failed candidates
> - $\{A,B\}$: $\{1,2\}=\{2,1\}$, so the order is lost.
> - $\{\{A\},\{B\}\}=\{\{B\},\{A\}\}$: symmetric again.
> - $\{A,\{B\}\}$: with $X=\varnothing$, $Y=\{\varnothing\}$, $Z=\{\{\varnothing\}\}$: $F(Z,X)=\{Z,\{X\}\}=\{Z,Y\}$ and $F(Y,Y)=\{Y,\{Y\}\}=\{Y,Z\}$, so $F(Z,X)=F(Y,Y)$ although $(Z,X)\ne(Y,Y)$.

> [!key] The Kuratowski pair
> $(A,B):=\{\{A\},\{A,B\}\}$. $A$ occurs in both inner sets; $B$ only in $\{A,B\}$. The roles are asymmetric.

> [!derivation] Proof of (OP) for Kuratowski (the instructor's proof)
> Write $\bigcap\mathcal F=\{x:x\in E\ \forall E\in\mathcal F\}$, $\bigcup\mathcal F=\{x:\exists E\in\mathcal F\ x\in E\}$. For $\mathcal F=\{\{A\},\{A,B\}\}$: $\bigcap\mathcal F=\{A\}\cap\{A,B\}=\{A\}$ and $\bigcup\mathcal F=\{A,B\}$ (also when $A=B$). Equal families have equal $\bigcap$ and $\bigcup$.
> Assume $\{\{A\},\{A,B\}\}=\{\{C\},\{C,D\}\}$. Intersections: $\{A\}=\{C\}$, so $A=C$. Unions: $\{A,B\}=\{C,D\}=\{A,D\}$. Now $B\in\{A,D\}$ gives $B=A$ or $B=D$. If $B=D$ done. If $B=A$ then $\{A,D\}=\{A,B\}=\{A\}$, forcing $D=A=B$. So $B=D$. The converse is substitution. $\square$
> Two bonuses: $\bigcap(A,B)=\{A\}$ recovers the first coordinate; $\bigcup(A,B)=\{A,B\}$ recovers the unordered pair.

> [!key] Another valid pair, and what it costs
> $\{A,\{A,B\}\}$ also works **in ZFC**, but the proof needs the **Axiom of Regularity**: from $\{A,\{A,B\}\}=\{C,\{C,D\}\}$ suppose $A\ne C$; then $A=\{C,D\}$ and $C=\{A,B\}$, so $A\in C\in A$, a membership cycle that Regularity forbids. Hence $A=C$, then $\{A,B\}=\{A,D\}$ (as $A\ne\{A,B\}$, else $A\in A$), so $B=D$.

> [!example] 🔵 A brute-force test (all sets of rank $\le3$)
> There are 16 sets in $V_3$ (built from $\varnothing$ by three rounds of "all subsets"). Over all $16\times16$ pairs $(A,B)$ count the **collisions** $F(A,B)=F(C,D)$ with $(A,B)\ne(C,D)$ for each candidate:
> | candidate | collisions |
> |---|---|
> | Kuratowski $\{\{A\},\{A,B\}\}$ | 0 |
> | $\{A,\{A,B\}\}$ | 0 |
> | $\{A,B\}$ | 120 (every $A\ne B$ with its swap) |
> | $\{\{A\},\{B\}\}$ | 120 |
> | $\{A,\{B\}\}$ | 6 (the $X,Y,Z$ example among them) |
> Zero collisions on $V_3$ is not a proof, but the failures are exactly the ones the note exhibits.

> [!pitfall] What the Kuratowski definition is not
> It is a **choice of representation**: any $F$ with property (OP) would do. After proving (OP) nobody looks inside the braces again.

## 5. Why axioms: Russell and ZFC
<span class="scope-extra-book">extra · book</span> *AI notes `proofs-prems-topo.pdf` ch. 4–5*

> [!key] Russell's paradox
> If every property defined a set, $R=\{x:x\notin x\}$ would be a set; then $R\in R\iff R\notin R$. So **unrestricted comprehension is inconsistent**. ZFC restricts it: a set can be carved out of an existing set by a property (**Separation**) but there is no universal set.

> [!key] The ZFC axioms (one line each)
> | # | axiom | content |
> |---|---|---|
> | 1 | Extensionality | sets with the same members are equal |
> | 2 | Separation (schema) | $\{x\in A:\varphi(x)\}$ is a set |
> | 3 | Pairing | $\{a,b\}$ is a set |
> | 4 | Union | $\bigcup\mathcal F$ is a set |
> | 5 | Power set | $\mathcal P(X)$ is a set |
> | 6 | Infinity | there is a set containing $\varnothing$ and closed under $x\mapsto x\cup\{x\}$ |
> | 7 | Replacement (schema) | the image of a set under a definable function is a set |
> | 8 | Regularity | every non-empty set has an $\in$-minimal member (so $A\notin A$) |
> | 9 | Choice | every family of non-empty pairwise disjoint sets has a choice set |
>
> From these: $\varnothing$ (Separation: $\{x\in A:x\ne x\}$), $A\cap B$, $A\setminus B$ (Separation), $\{A,B\}$, $\{A\}$ (Pairing), $A\cup B$ (Pairing + Union), $\mathcal P(A)$, the ordered pair of §4, $A\times B$ (a subset of $\mathcal P(\mathcal P(A\cup B))$), relations and functions as subsets of $A\times B$ ([[PA03 Relations Equivalence and Order]], [[PA04 Functions and Cardinality]]) and the natural numbers ([[PA05 Induction and the Number Systems]]).

> [!example] Regularity at work
> $A\in A$ is impossible: $\{A\}$ would have no $\in$-minimal member. This is exactly what the ordered-pair note uses to show $(A,A)=\{\{A\}\}\ne\{A\}$ (else $\{A\}=A$ and $A\in A$).

## Map of this chapter
> [!connection] How PA02 connects
> **Builds on:** [[PA01 Logic and Methods of Proof]] (every proof here is a chase through a logical equivalence).
> **Leads to:** [[PA03 Relations Equivalence and Order]] (relations are subsets of products), [[PA04 Functions and Cardinality]] (a function is a set of ordered pairs; $|\mathcal P(A)|>|A|$), [[PA07 Metric and Topological Spaces]] (a topology is a family of subsets closed under arbitrary $\bigcup$ and finite $\bigcap$).
> **Concepts:** [[Set Operations and De Morgan's Laws]] · [[Power Set]] · [[Indexed Family of Sets]] · [[Cartesian Product]] · [[Ordered Pair]] · [[ZFC Axioms]] · [[Russell's Paradox]] · [[Axiom of Choice]]
> **Other subjects:** [[Probability - Course Map]] ([[PR01 Counting and the Axioms of Probability]]: events are subsets of a sample space and De Morgan is used verbatim; $|\mathcal P(S)|=2^{|S|}$ counts the events of a finite sample space), [[Quantum Mechanics - Course Map]] (state spaces as sets with structure).

## Summary
> [!summary] Cheat-sheet
> - $\varnothing\subseteq A$ (vacuous); $|\mathcal P(A)|=2^{|A|}$ (subsets ↔ bit strings); prove identities by **element chasing**.
> - De Morgan: $(A\cap B)^c=A^c\cup B^c$, $(A\cup B)^c=A^c\cap B^c$; $A\times(B\cup C)=(A\times B)\cup(A\times C)$.
> - Families: $\bigcup_n(-\tfrac1n,\tfrac1n)=(-1,1)$, $\bigcap=\{0\}$; $[-n,1-\tfrac1n)$: $\bigcup=(-\infty,1)$, $\bigcap=[-1,0)$; $H_n=\{y\ge-n\}$: $\bigcup=\mathbb R^2$, $\bigcap=H_1$; an empty $A_k$ kills $\bigcap$ and $\prod$.
> - Ordered pair test: $F(A,B)=F(C,D)\Rightarrow A=C,B=D$. $\{A,B\}$, $\{\{A\},\{B\}\}$, $\{A,\{B\}\}$ fail; Kuratowski works (needs only pairing); $\{A,\{A,B\}\}$ works with Regularity.
> - Russell: $\{x:x\notin x\}$ is not a set; ZFC = Extensionality, Separation, Pairing, Union, Power set, Infinity, Replacement, Regularity, Choice.

## Practice
1. **Chase.** Prove $A\setminus(B\cup C)=(A\setminus B)\cap(A\setminus C)$.
2. **Symmetric difference.** For $A\triangle B=(A\setminus B)\cup(B\setminus A)$, show $A\triangle B=(A\cup B)\setminus(A\cap B)$ and list $A\triangle B$ for $A=\{1,2,3\}$, $B=\{2,3,4,5\}$.
3. **Counting subsets.** How many subsets of $\{1,\dots,6\}$ have an even number of elements? How many contain 1 but not 2?
4. **Power set.** Write $\mathcal P(\{a,b,c\})$. How many elements has $\mathcal P(\mathcal P(\{a,b\}))$?
5. **Families.** For $A_n=[0,1+\tfrac1n]$, $n\ge1$, find $\bigcup A_n$ and $\bigcap A_n$. Repeat for $B_n=(0,\tfrac1n)$.
6. **Products.** Show $(A\cap B)\times C=(A\times C)\cap(B\times C)$. Is $(A\cup B)\times(C\cup D)=(A\times C)\cup(B\times D)$? Give a counterexample if not.
7. **Uniqueness of $\varnothing$.** Prove that there is only one empty set (use extensionality).
8. **Pairs.** Show that $\{A,\{A,B\}\}$ with $A=\varnothing$, $B=\varnothing$ equals $\{\varnothing,\{\varnothing\}\}$, and compare it with the Kuratowski pair $(\varnothing,\varnothing)$.
9. **Kuratowski.** Using $\bigcap$ and $\bigcup$, compute the first and second coordinate of $\{\{1\},\{1,2\}\}$ and of $\{\{3\}\}$.
10. **Russell.** Explain why $\{x\in A:x\notin x\}$ **is** a set for any set $A$ and prove that it is not an element of $A$ (hint: assume it is).

> [!example]- Solutions
> 1. $x\in A\setminus(B\cup C)\iff x\in A\wedge\neg(x\in B\vee x\in C)\iff x\in A\wedge x\notin B\wedge x\notin C\iff x\in(A\setminus B)\cap(A\setminus C)$.
> 2. $x\in A\triangle B\iff$ exactly one of $x\in A$, $x\in B$ $\iff x\in A\cup B\wedge x\notin A\cap B$. For the example, $\{1,4,5\}$.
> 3. Even-sized subsets: half of $2^6=64$, i.e. $32$ ($\sum_{k\text{ even}}\binom6k=1+15+15+1$). Containing 1 but not 2: choose freely among the other 4 elements, $2^4=16$.
> 4. $\{\varnothing,\{a\},\{b\},\{c\},\{a,b\},\{a,c\},\{b,c\},\{a,b,c\}\}$. $|\mathcal P(\{a,b\})|=4$, so $|\mathcal P(\mathcal P(\{a,b\}))|=2^4=16$.
> 5. $A_n$ decreases to $[0,1]$: $\bigcup=A_1=[0,2]$, $\bigcap=[0,1]$. $B_n=(0,\tfrac1n)$ decreases: $\bigcup=B_1=(0,1)$, $\bigcap=\varnothing$ (a positive $x$ eventually exceeds $1/n$).
> 6. $(x,z)\in(A\cap B)\times C\iff x\in A\wedge x\in B\wedge z\in C\iff(x,z)\in A\times C\wedge(x,z)\in B\times C$. The second is **false** in general: with $A=\{1\}$, $B=\{2\}$, $C=\{3\}$, $D=\{4\}$ the left side contains $(1,4)$, the right side does not.
> 7. If $\varnothing_1,\varnothing_2$ are both empty, $x\in\varnothing_1\iff x\in\varnothing_2$ holds (both sides false for every $x$); by extensionality they are equal.
> 8. $\{\varnothing,\{\varnothing\}\}$ is the set $2=\{0,1\}$; $(\varnothing,\varnothing)=\{\{\varnothing\},\{\varnothing,\varnothing\}\}=\{\{\varnothing\}\}=\{1\}$, a singleton. They are different sets, showing that different encodings of the pair $(\varnothing,\varnothing)$ give different objects.
> 9. $\bigcap\{\{1\},\{1,2\}\}=\{1\}$ (first coordinate 1); $\bigcup=\{1,2\}$, second coordinate 2 (the element other than 1). For $\{\{3\}\}$: both are $\{3\}$, so the pair is $(3,3)$.
> 10. It is a subset of $A$ defined by a property: Separation. Suppose $R=\{x\in A:x\notin x\}\in A$. If $R\in R$ then by definition $R\notin R$; if $R\notin R$ then, since $R\in A$, $R\in R$. Contradiction. So $R\notin A$: no set contains all sets of this kind, hence no universal set.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | sets, subsets, $\mathcal P(A)$, De Morgan, products, indexed families and the twelve questions | [[Assignment-prems_merged.pdf#page=3\|Assignment 3]] | taught |
> | ordered pairs, Kuratowski, failed candidates, $\{A,\{A,B\}\}$, Regularity | [[ordered pairs.pdf]] (instructor's note) | taught |
> | Russell's paradox, the nine axioms, constructions from the axioms | AI notes `proofs-prems-topo.pdf` Part II | extra/book |
> | brute-force pair test, counting checks | `scripts/pa_numbers.py` | extra/beyond |
>
> **Notes.** The assignments use $\varphi$ for $\varnothing$, $\subset$ for $\subseteq$, $A-B$ for $A\setminus B$. Q7 of Assignment 3 asks for $\prod A_n$ as well; I describe it (sequences with $|a_n|<1/n$). The AI notes' solutions to Assignment 3 were compared; the answers above agree.

**References.** Sundstrom, T. *Mathematical Reasoning*, Ch. 5 · Kumaresan et al., *A Foundation Course in Mathematics* · Munkres, J. *Topology*, §1 · Kuratowski, K. (1921) *Sur la notion de l'ordre dans la théorie des ensembles*.
