---
title: Proofs Quiz Prep
aliases: [MT2133 quiz prep, induction and WOP quiz, Assignment 8 and 9 quiz, PA quiz prep]
subject: analysis
type: moc
scope: [taught]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/analysis, type/moc, taught, src/lecture-notes, src/own-notes, status/draft, quiz/proofs, quiz/pa-induction, quiz/pa-strong, quiz/pa-wop]
---
# Proofs Quiz Prep (induction, strong induction and the Well-Ordering Principle)

◀ [[Proofs, Analysis and Topology - Course Map|Course Map]] · chapters [[PA08 Mathematical Induction|PA08]] · [[PA09 Strong Induction and Recursion|PA09]] · [[PA10 Well-Ordering and Well-Ordered Pairs|PA10]] · background [[PA05 Induction and the Number Systems|PA05]] · [[PA16 Peano's Axioms and the Natural Numbers|PA16]]

<span class="scope-taught">taught · in syllabus (Assignments 8 and 9, Lecture 25)</span>

> [!warning] What this page covers (written 2026-11-12 for the quiz on 2026-11-13)
> **Scope: the induction and WOP assignments: [[Assignment-8.pdf]] Problems 6–7 (the induction half of that sheet; its Problems 1–5 are cardinality: [[PA04 Functions and Cardinality]]) and [[Assignment-9.pdf]] Problems 1–4 (strong induction and the Well-Ordering Principle)**, with the background in Lecture 24–25 ([[L-25.pdf]]). Full solutions of every one of these problems were **added today** to [[PA08 Mathematical Induction]] (A8 Q6–Q7), [[PA09 Strong Induction and Recursion]] (A9 Q1, Q2a) and [[PA10 Well-Ordering and Well-Ordered Pairs]] (A9 Q3, Q4) and checked by machine (`scripts/quiz_numbers.py`). Assignment 9 Q1(a) is garbled in the text layer; I read the recurrence from the page image ($a_1=1$, $a_2=3$, bound $(7/4)^n$). The other tool's note of A8 Q6(c) omits a "$+6$" in the inductive-step identity (PA08, flagged).

> [!tip] How the tags work
> Open the search pane and type **`tag:#quiz/pa-induction`** (PMI and strong-induction proofs), **`tag:#quiz/pa-strong`**, **`tag:#quiz/pa-wop`** (WOP and minimal counterexample) or **`tag:#quiz/proofs`** (all). Tags are on the chapter front matter, on the section headings (PA08 §1–§4, PA09 §1–§4, PA10 §1–§3, PA05 §1–§4), on the "solved in full" sections and on the concept notes of §7. #quiz/pa-induction #quiz/pa-strong #quiz/pa-wop

## 1. Problem map: where each assignment problem is solved

| Problem | What it asks | Key idea | Solved in |
|---|---|---|---|
| **A8 Q6(a)** #quiz/pa-induction | $\sum_{i=1}^n(2i-1)=n^2$ | step: $n^2+(2n+1)=(n+1)^2$ | PA08 (Continued) |
| **A8 Q6(b)** #quiz/pa-induction | $\sum i\cdot i!=(n+1)!-1$ | step: $(k+1)!-1+(k+1)(k+1)!=(k+2)!-1$ | PA08 |
| **A8 Q6(c)** #quiz/pa-induction | $6\mid n^3+5n$ | $(k+1)^3+5(k+1)=(k^3+5k)+3k(k+1)+6$; $k(k+1)$ even | PA08 |
| **A8 Q6(d)** #quiz/pa-induction | $2^n>n^2$ for $n\ge5$ (extended PMI, base $5$) | $2\cdot2^k>2k^2\ge(k+1)^2\iff k^2-2k-1\ge0$; $P(2),P(3),P(4)$ false | PA08 |
| **A8 Q7(a)** #quiz/pa-induction | "$n=n+1$": valid step, false base | the step alone proves nothing | PA08, §4 |
| **A8 Q7(b)** #quiz/pa-induction | induction on $\mathbb Q$ ($x\ge1$) | PMI is about $\mathbb N$ (start + successor); $\{x\ge1\}\ne\mathbb Q$ | PA08, §4; PA16 |
| **A9 Q1(a)** #quiz/pa-strong | $a_1=1,a_2=3,a_n=a_{n-1}+a_{n-2}$: $a_n<(7/4)^n$; why two bases | $\tfrac{44}{16}<\tfrac{49}{16}$; step uses $a_{n-1},a_{n-2}$ | PA09 (Continued) |
| **A9 Q1(b)** #quiz/pa-strong | $b_n=4b_{n-1}-4b_{n-2}$, $b_1=2,b_2=4$: $b_3,b_4,b_5$; closed form | $8,16,32$; $b_n=2^n$ | PA09 |
| **A9 Q1(c)** #quiz/pa-strong | every $n\ge8$ is $3x+5y$; bases; false for $7$ | bases $8,9,10$; step $n-3$; $7$ fails | PA09 |
| **A9 Q2(a)** #quiz/pa-strong #quiz/pa-wop | WOP $\Rightarrow$ strong induction | $S=\{n:P(n)\text{ false}\}$, $m=\min S$, $P(1..m-1)$ true $\Rightarrow P(m)$ | PA09; PA10 §2 |
| **A9 Q3(a)** #quiz/pa-wop | every $n\ge2$ has a prime divisor | $m$ composite $=ab$, $a<m$ has a prime divisor | PA10 (Continued) |
| **A9 Q3(b)** #quiz/pa-wop | non-empty $S\subseteq\mathbb Z$ bounded below has a least element | shift into $\mathbb N$: $T=\{s-b+1\}$ | PA10 |
| **A9 Q3(c)** #quiz/pa-wop | no rational has square $3$ | least $q$ with $p^2=3q^2$; $3\mid p$, $q^2=3r^2$, $r<q$ | PA10 |
| **A9 Q4(a)** #quiz/pa-wop | $n^2+n$ even by WOP | $m=\min$ failure; $m^2+m$ odd $\Rightarrow(m-1)^2+(m-1)$ odd | PA10 |
| **A9 Q4(b)** #quiz/pa-induction #quiz/pa-wop | same by induction; compare | the step $P(k)\Rightarrow P(k+1)$ is the contrapositive inside (a) | PA10 |

## 2. The principles, precisely
> [!key] The four statements (all equivalent for $\mathbb N=\{1,2,\dots\}$) #quiz/pa-induction #quiz/pa-strong #quiz/pa-wop
> - **PMI (sets):** if $S\subseteq\mathbb N$, $1\in S$ and $k\in S\Rightarrow k+1\in S$ for every $k$, then $S=\mathbb N$. **(statements):** $P(1)$ and $\forall k\,(P(k)\Rightarrow P(k+1))$ $\Rightarrow$ $\forall n\,P(n)$. **Extended:** $P(m)$ and $P(k)\Rightarrow P(k+1)$ for all $k\ge m$ $\Rightarrow$ $P(n)$ for all $n\ge m$.
> - **Strong induction:** $P(1)$, and $\forall k\,(P(1)\wedge\dots\wedge P(k)\Rightarrow P(k+1))$ $\Rightarrow$ $\forall n\,P(n)$.
> - **WOP:** every non-empty subset of $\mathbb N$ has a least element (also true for $\mathbb N\cup\{0\}$ and $\{n\in\mathbb Z:n\ge m\}$).
> - **Equivalence cycle:** PMI $\Rightarrow$ WOP ($S$ non-empty with no least element; $T=\{n:\{1,\dots,n\}\cap S=\varnothing\}$ is inductive $\Rightarrow$ $S=\varnothing$) $\Rightarrow$ strong induction (A9 Q2a) $\Rightarrow$ PMI (strong's hypothesis is weaker to check). Details: [[PA10 Well-Ordering and Well-Ordered Pairs]] §2.
> - **Why $\mathbb N$ and not $\mathbb Q$:** the three principles are the induction/least-element axioms of $\mathbb N$ ([[PA16 Peano's Axioms and the Natural Numbers]], (P3)); $\mathbb Q$ and $\mathbb R$ have no least element for $(0,\infty)$.

> [!key] How to write the proof (the sheets' rules) #quiz/pa-induction #quiz/pa-wop
> **Induction / strong induction:** (1) say what $P(n)$ is; (2) prove the base case(s); (3) state exactly what is assumed (for $P(k)$, or for $P(1),\dots,P(k)$) and prove $P(k+1)$; (4) conclude "by PMI (strong induction), $P(n)$ for all $n\ge m$". **WOP:** (1) say which set $S$ you take the least element of and **why it is non-empty** (assume the claim fails, so the set of counterexamples is non-empty); (2) let $m=\min S$; (3) produce a counterexample smaller than $m$ (or show $m$ cannot be one); (4) contradiction.

## 3. Patterns: which tool for which problem
| Pattern | Tool | Example | Remember |
|---|---|---|---|
| sum identities, divisibility by a fixed number | PMI | A8 Q6(a)–(c) | add and subtract so that the hypothesis appears: $(k+1)^3+5(k+1)=(k^3+5k)+\dots$ |
| inequality true only from some $n$ | extended PMI, base $m$ | $2^n>n^2$, $n\ge5$ | the **base must be the first true $n$** and the step must work from there; check it holds for $k\ge m$ |
| recurrence using two earlier terms | strong induction, **two bases** | A9 Q1(a),(b) | number of bases = how far back the step reaches |
| "every amount $\ge N$ is $ax+by$" | strong induction, **several bases** | $3x+5y$, $n\ge8$ | bases are a run of $\min(a,b)$ consecutive values ($8,9,10$); $N=ab-a-b+1$ |
| existence of a prime divisor/factorisation | WOP or strong induction | A9 Q3(a) | composite $m=ab$, both factors smaller |
| irrationality | WOP on denominators (minimal counterexample) | A9 Q3(c) | produce a smaller denominator |
| parity/divisibility "is $P(m-1)$ also false?" | WOP ≡ induction step | A9 Q4 | the induction step is the contrapositive inside the WOP argument |
| least element of a set bounded below in $\mathbb Z$ | shift into $\mathbb N$ and use WOP | A9 Q3(b) | $T=\{s-b+1\}$ |

## 4. Traps (what goes wrong in induction proofs)
1. **Base case missing or wrong** (A8 Q7a: $n=n+1$); an inductive step without a base proves nothing.
2. **Base case too early or too few** for what the step needs (Fibonacci-type: two bases; $n-3$: three bases).
3. **Step fails at the smallest $k$** ("all horses have the same colour": the overlap argument breaks at $n=2$); "all integers equal": the pair $(a-1,b-1)$ leaves $\mathbb N$ at $k=1$.
4. **Starting too late / claiming too much:** $2^n>n^2$ is false at $n=2,3,4$ although the step holds for $k\ge3$; the base must be $5$.
5. **Induction on a set that is not $\mathbb N$** (A8 Q7b): $\mathbb Q$ is not generated from $1$ by $x\mapsto x+1$.
6. **Not stating what is assumed**: ordinary induction assumes $P(k)$, strong induction assumes $P(1),\dots,P(k)$; say which.
7. **WOP without showing non-emptiness** or with a set not contained in $\mathbb N$ (shift first, A9 Q3b).
8. **Circularity:** the step must prove $P(k+1)$ *using* the hypothesis, not assume $P(k+1)$.
9. **Never reaches $\infty$:** induction proves $P(n)$ for every finite $n$, not for "$n=\infty$" ([[PA08 Mathematical Induction]] §4).

## 5. Self-test (solutions collapsed; every claim below was checked by machine)
1. **(PMI)** Prove $\sum_{i=0}^n2^i=2^{n+1}-1$ for all $n\ge0$, and $7\mid8^n-1$ for all $n\ge1$.
2. **(shifted base)** Find the least $m$ with $n!>2^n$ for all $n\ge m$ and prove it.
3. **(strong induction, two bases)** $c_1=c_2=1$, $c_n=c_{n-1}+2c_{n-2}$. Compute $c_3,\dots,c_6$, guess a closed form and prove it.
4. **(several bases)** Show every integer $n\ge18$ can be written $n=4x+7y$ with $x,y\ge0$. How many base cases? Show $17$ is not representable.
5. **(WOP, divisibility)** Prove $3\mid n^3-n$ for all $n\in\mathbb N$ by taking a least counterexample.
6. **(WOP, no integer between)** Show there is no integer $n$ with $0<n<1$ using Problem 3(b).
7. **(WOP, factorisation)** Every integer $n\ge2$ is a product of primes.
8. **(WOP, irrationality)** $\sqrt2$ is irrational.
9. **(find the flaw)** "All horses have the same colour": where does the induction break?
10. **(find the flaw)** $P(x)$: "$x\ge1$" for $x\in\mathbb Q$; $P(1)$ and $P(x)\Rightarrow P(x+1)$. Why does this not prove $P(x)$ for all rationals?
11. **(concept)** Why is strong induction no stronger than PMI? Give the one-line reduction.
12. **(compare)** In Assignment 9 Q4, where does the inductive step of (b) appear inside the WOP argument of (a)?

> [!example]- Solutions
> 1. $P(n)$: $\sum_{i=0}^n2^i=2^{n+1}-1$. Base $n=0$: $1=2-1$. Step: $\sum_{i=0}^{k+1}2^i=(2^{k+1}-1)+2^{k+1}=2^{k+2}-1$. For $7\mid8^n-1$: base $7$; step $8^{k+1}-1=8(8^k-1)+7$, both terms divisible by $7$.
> 2. $m=\mathbf4$: $1!<2$, $2!=2<4$, $3!=6<8$ fail, $4!=24>16$. Step ($k\ge4$): $(k+1)!=(k+1)k!>(k+1)2^k\ge2\cdot2^k=2^{k+1}$.
> 3. $c_3,\dots,c_6=3,5,11,21$ ($c_7=43$); guess $c_n=\dfrac{2^n-(-1)^n}3$ (characteristic roots $2,-1$). Strong induction, bases $c_1=\frac{2+1}3=1$, $c_2=\frac{4-1}3=1$; step: $c_n=\dfrac{2^{n-1}-(-1)^{n-1}}3+2\cdot\dfrac{2^{n-2}-(-1)^{n-2}}3=\dfrac{2^{n-1}+2^{n-1}-(-1)^{n-1}-2(-1)^{n}}3=\dfrac{2^n+(-1)^n-2(-1)^n}3=\dfrac{2^n-(-1)^n}3$ (using $-(-1)^{n-1}=(-1)^n$). Two bases because the step uses two earlier terms.
> 4. $P(n)$: $n=4x+7y$. **Four bases** (the step reaches back by $4$): $18=4+14=4\cdot1+7\cdot2$, $19=12+7$, $20=4\cdot5$, $21=7\cdot3$. Step $n\ge22$: $n-4\ge18$ is representable; add a $4$. $17$: $17-7y\in\{17,10,3\}$, none divisible by $4$. (Frobenius number $4\cdot7-4-7=17$; checked: non-representable amounts up to $40$ are $1,2,3,5,6,9,10,13,17$.)
> 5. Let $m$ be the least counterexample, i.e. $3\nmid m^3-m$. $m\ne1$ ($0$ is divisible). $m^3-m=\big((m-1)^3-(m-1)\big)+3m(m-1)$, so if $3\nmid m^3-m$ then $3\nmid(m-1)^3-(m-1)$: $m-1\ge1$ is a smaller counterexample. Contradiction.
> 6. Suppose $S=\{n\in\mathbb Z:0<n<1\}\ne\varnothing$; it is bounded below by $0$, so by 3(b) it has a least element $m$. Then $0<m<1$ gives $0<m^2<m<1$, so $m^2\in S$ and $m^2<m$: contradiction. (Here $m^2<m$ because $0<m<1$ and $m>0$.)
> 7. Let $S=\{n\ge2:n\text{ is not a product of primes}\}$ and suppose $S\ne\varnothing$ with least element $m$. $m$ is not prime (a prime is a product of one prime), so $m=ab$ with $2\le a,b<m$; by minimality $a,b\notin S$, so each is a product of primes, hence so is $m$: contradiction.
> 8. Suppose $p^2=2q^2$ has a solution in positive integers; let $q$ be the least such. $p^2$ even $\Rightarrow p$ even, $p=2r$, $4r^2=2q^2\Rightarrow q^2=2r^2$ with $r<q$: a smaller solution, contradiction.
> 9. $P(n)$: "any $n$ horses have one colour". Base $n=1$ true. The step from $n=1$ to $n=2$ uses the **overlap** of two sets of $1$ horse, which is empty, so "the two horses share a horse of the common colour" fails: $P(1)\not\Rightarrow P(2)$; the step is valid only for $k\ge2$, but the base case $P(2)$ is false.
> 10. PMI says: a subset of $\mathbb N$ containing $1$ and closed under $k\mapsto k+1$ is all of $\mathbb N$. Starting from $1$ and adding $1$ reaches only $\{1,2,3,\dots\}$; $\{x\in\mathbb Q:x\ge1\}$ contains $1$, is closed under $+1$, and is not $\mathbb Q$ ($\mathbb Q$ is not generated by a start and a successor).
> 11. A PMI proof of $Q(n):=P(1)\wedge\dots\wedge P(n)$ gives strong induction: $Q(1)=P(1)$, and $Q(k)\Rightarrow P(k+1)$ (the strong hypothesis) $\Rightarrow Q(k+1)$. Equivalently, strong induction's hypothesis is stronger, so it is easier to use but the principle is no stronger.
> 12. (a) says: if $P(m)$ is the first failure then $P(m-1)$ has failed too (contrapositive: $P(m-1)\Rightarrow P(m)$). That implication is *exactly* the inductive step of (b) with $k=m-1$: $(k)^2+k$ even $\Rightarrow(k+1)^2+(k+1)$ even, because the difference is $2(k+1)$.

## 6. Practice with solutions already in the chapters
[[PA08 Mathematical Induction]] (Practice 1–12: cubes, $9\mid4^n+6n-1$, $\sum1/\sqrt k\ge\sqrt n$, Cassini, lattice paths, forward–backward AM–GM, the flaw), [[PA09 Strong Induction and Recursion]] (Practice 1–10: stamps, Zeckendorf, Josephus, weak versus strong), [[PA10 Well-Ordering and Well-Ordered Pairs]] (Practice: prime divisor, division algorithm, Bézout, infinite descent) and [[PA05 Induction and the Number Systems]] (the PMI/WOP/strong statements and Peano).

## 7. Tag index: every related note
- **Chapters:** [[PA08 Mathematical Induction]] · [[PA09 Strong Induction and Recursion]] · [[PA10 Well-Ordering and Well-Ordered Pairs]] · [[PA05 Induction and the Number Systems]] · [[PA16 Peano's Axioms and the Natural Numbers]].
- **Concept notes (tagged):** [[Principle of Mathematical Induction]] · [[Strong Induction]] · [[Well-Ordering Principle]] · [[Well-Ordered Set]] · [[Minimal Counterexample]] · [[Common Induction Errors]] · [[Strengthening the Induction Hypothesis]] · [[Forward-Backward Induction]] · [[Structural Induction]] · [[Recursion Theorem]] · [[Natural Numbers]] · [[Peano System]] · [[Order on the Natural Numbers]] · [[Arithmetic on the Natural Numbers from the Successor]] · [[Fibonacci Numbers]] · [[Division Algorithm and Bezout's Identity]] · [[Counterexample]]; zettel: [[zettel/principle-of-strong-induction]] · [[zettel/well-ordering-principle]] · [[zettel/method-of-minimal-counterexample]] · [[zettel/inductive-set]].

> [!provenance]- Source map
> | Content | Source |
> |---|---|
> | Assignment 8 Q6–Q7 | [[Assignment-8.pdf]] (statements via [[intro-to-proofs/2026-10-22-assignment-8]]); solutions in [[PA08 Mathematical Induction]] |
> | Assignment 9 Q1–Q4 | [[Assignment-9.pdf]] (read in full; Q1(a) from the page image); solutions in [[PA09 Strong Induction and Recursion]] and [[PA10 Well-Ordering and Well-Ordered Pairs]] |
> | Lecture 24–25 | [[L-25.pdf]] ([[PA16 Peano's Axioms and the Natural Numbers]]) |
> | self-test | mine; claims checked in `scripts/quiz_numbers.py` and the interactive checks of this session |

## 8. Also solved, outside this quiz's scope
- **Assignment 10 (groups)**, full proofs in [[GT01 Groups Subgroups and Cosets]] ("Assignment 10 solved in full", tagged `#quiz/pa-groups`): a group is closure + associativity + identity + inverses; $\mu_n$ (cyclic of order $n$), $S^1$ (infinite), $T=\{\begin{pmatrix}1&a\\0&1\end{pmatrix}\}\cong(\mathbb R,+)$ are abelian; the equilateral triangle has **exactly 6 symmetries** ($e$, two rotations, three reflections) forming $S_3$, **non-abelian** ($r\circ s=(1\,3)\ne(2\,3)=s\circ r$); the non-square rectangle has **4** (Klein four-group, abelian); the square has **8** ($D_4$, non-abelian).
- **Assignment 8 Problems 1–5 (cardinality)**, full proofs in [[PA04 Functions and Cardinality]] (tagged `#quiz/pa-cardinality`): union of a countably infinite and a countable set (finite case: shift; infinite case: interleave), $\mathbb R\setminus\mathbb Q$ uncountable, countable union of disjoint countable sets via $F(i,n)=f_i(n)$, $\{0,1\}^{\mathbb N}$ uncountable (diagonal $b_n=1-a_{nn}$), Cantor's theorem ($B=\{a:a\notin f(a)\}$), $[0,1)\sim(0,1)$ and $[0,1]\sim(0,1)\sim\mathbb R$ (shift a countable sequence by $1$ or $2$ places).
- **Mid-semester 2026 solutions:** Practice boxes at the end of [[PA01 Logic and Methods of Proof]], [[PA02 Sets Families and the ZFC Foundations]], [[PA03 Relations Equivalence and Order]]; **Peano axioms:** [[PA16 Peano's Axioms and the Natural Numbers]].
