---
id: intro-to-proofs/2026-10-22-assignment-8
aliases: [Assignment 8, Assignment-8]
tags: [intro-to-proofs, coursework, assignment, induction, cardinality, countable-sets, uncountable-sets]
trust_tier: agent_written
---
# Assignment-8

## Covered
Coursework sheet on countability, uncountability, Cantor's theorem, interval bijections, and mathematical induction (Classroom file: Assignment-8.pdf).

**Core definitions and conventions:**
- $\mathbb{N} = \{1, 2, 3, \dots\}$ and $N_k = \{1, 2, \dots, k\}$.
- $A \sim B$ denotes existence of a bijection $A \to B$ ($\sim$ is an equivalence relation).
- Known facts: subsets of countable sets are countable; $\mathbb{N} \times \mathbb{N}$, $\mathbb{Z}$, and $\mathbb{Q}$ are countably infinite.
- **Definition 1 (Uncountable set):** A set $A$ is uncountable if it is infinite and not countable (there is no bijection $\mathbb{N} \to A$).
- **Remark:** If $A \subseteq B$ and $A$ is uncountable, then $B$ is uncountable (Lecture 18). This is the quickest way to prove uncountability: exhibit an uncountable subset.
- **Definition 2 (Inductive set, PMI):** A subset $S \subseteq \mathbb{N}$ is inductive if $k \in S \implies k+1 \in S$ for every $k \in \mathbb{N}$. The Principle of Mathematical Induction (PMI) states: if $S \subseteq \mathbb{N}$ is inductive and $1 \in S$, then $S = \mathbb{N}$.
- **Extended PMI:** If $P(m)$ is true and $P(k) \implies P(k+1)$ for every integer $k \ge m$, then $P(n)$ is true for every integer $n \ge m$.
- **Four mandatory parts of an induction proof:**
  1. State explicitly what the proposition $P(n)$ is.
  2. Prove the base case ($P(1)$ or $P(m)$).
  3. Inductive hypothesis: assume $P(k)$ for an arbitrary integer $k \ge m$, and prove $P(k+1)$.
  4. State the explicit conclusion by PMI.

**Problems and what each one practises:**
- **Problem 1 (Unions, and the irrational numbers):**
  - (a) Let $A$ be countably infinite and $B$ countable. Show that $A \cup B$ is countably infinite.
    *Practises:* Writing $A \cup B = A \cup (B \setminus A)$ as a disjoint union, using that $B \setminus A \subseteq B$ is countable (finite or countably infinite), and constructing an explicit interleaving or sequential bijection with $\mathbb{N}$.
  - (b) Show that the set $\mathbb{R} \setminus \mathbb{Q}$ of irrational numbers is uncountable.
    *Practises:* Proof by contradiction: if $\mathbb{R} \setminus \mathbb{Q}$ were countable, then $\mathbb{R} = \mathbb{Q} \cup (\mathbb{R} \setminus \mathbb{Q})$ would be the union of two countable sets, hence countable by part (a), contradicting the uncountability of $\mathbb{R}$.
- **Problem 2 (A countable union of countable sets is countable):**
  - Let $A_1, A_2, A_3, \dots$ be countably infinite sets that are pairwise disjoint, with bijections $f_i: \mathbb{N} \to A_i$ for each $i \in \mathbb{N}$.
  - (a) Define $F: \mathbb{N} \times \mathbb{N} \to \bigcup_{i \in \mathbb{N}} A_i$ by $F((i, n)) = f_i(n)$. Show that $F$ is a bijection.
    *Practises:* Proving injectivity using disjointness of the families ($A_i \cap A_j = \emptyset$ for $i \ne j$) and injectivity of each $f_i$; proving surjectivity using $\bigcup A_i$ definition and surjectivity of each $f_i$. Concluding $\bigcup_{i \in \mathbb{N}} A_i$ is countably infinite using $\mathbb{N} \sim \mathbb{N} \times \mathbb{N}$.
- **Problem 3 (Sequences of 0s and 1s):**
  - Let $\{0, 1\}^\mathbb{N}$ be the set of all infinite binary sequences $(x_1, x_2, x_3, \dots)$ with each $x_n \in \{0, 1\}$.
  - (a) Show that $\{0, 1\}^\mathbb{N}$ is infinite.
    *Practises:* Embedding $\mathbb{N}$ into $\{0, 1\}^\mathbb{N}$ via distinct indicator sequences (e.g. sequences with a 1 only at position $n$).
  - (b) Let $f: \mathbb{N} \to \{0, 1\}^\mathbb{N}$ be any function, with $f(n) = (a_{n1}, a_{n2}, a_{n3}, \dots)$. Define $b = (b_1, b_2, \dots)$ by $b_n = 1 - a_{nn}$. Show that $b \notin \operatorname{Im}(f)$, and conclude that $\{0, 1\}^\mathbb{N}$ is uncountable.
    *Practises:* Applying Cantor's diagonal perturbation directly to binary sequence spaces.
- **Problem 4 (Cantor's theorem: a set is always smaller than its power set):**
  - Let $A$ be any set and $f: A \to \mathcal{P}(A)$ any function. Define $B = \{a \in A : a \notin f(a)\} \subseteq A$.
  - (a) Suppose $B = f(a_0)$ for some $a_0 \in A$. Analyze $a_0 \in B \iff a_0 \notin f(a_0) = B$, deriving a contradiction in both cases.
  - (b) Conclude that no function $A \to \mathcal{P}(A)$ is surjective, so $|A| \ne |\mathcal{P}(A)|$. Observe $a \mapsto \{a\}$ is an injection, establishing $|A| < |\mathcal{P}(A)|$.
    *Practises:* The Russell-style diagonalisation proof of Cantor's theorem for arbitrary sets.
- **Problem 5 (Bijections between intervals):**
  - (a) Show that $[0, 1) \sim (0, 1)$ by defining $g: [0, 1) \to (0, 1)$ with $g(0) = 1/2$, $g(1/n) = 1/(n+1)$ for $n \ge 2$, and $g(x) = x$ for all other $x$.
    *Practises:* The "Hilbert hotel" shift technique on a countable sequence of points $\{0, 1/2, 1/3, \dots\}$ while fixing the uncountable remainder.
  - (b) Deduce that $[0, 1] \sim (0, 1) \sim \mathbb{R}$.
    *Practises:* Extending the point-shifting technique to absorb two boundary points $\{0, 1\}$, and composing with the bijection $(0, 1) \sim \mathbb{R}$ from Lecture 20.
- **Problem 6 (Induction proofs for all $n \in \mathbb{N}$):**
  - (a) $\sum_{i=1}^n (2i-1) = n^2$.
  - (b) $\sum_{i=1}^n i \cdot i! = (n+1)! - 1$.
  - (c) 6 divides $n^3 + 5n$ for every $n \in \mathbb{N}$ (algebraic inductive step $(k+1)^3 + 5(k+1) = k^3 + 5k + 3k(k+1)$, where $k(k+1)$ is even, so $3k(k+1)$ is divisible by 6).
  - (d) $2^n > n^2$ for every integer $n \ge 5$ (extended PMI with base $m=5$: $2^5 = 32 > 25$; inductive step uses $2k^2 > (k+1)^2 \iff k^2 - 2k - 1 > 0$, true for $k \ge 5$).
  - *Practises:* Execution of all 4 components of standard and shifted PMI.
- **Problem 7 (What induction does and does not prove):**
  - (a) "Theorem" $n = n+1$ for all $n \in \mathbb{N}$: show the inductive step $P(k) \implies P(k+1)$ is valid ($k = k+1 \implies k+1 = (k+1)+1$), but condition $P(1)$ fails ($1 \ne 2$), illustrating that an inductive step without a valid base case proves nothing.
  - (b) For $x \in \mathbb{Q}$, let $P(x)$ be $x \ge 1$. $P(1)$ is true and $P(x) \implies P(x+1)$ for all $x \in \mathbb{Q}$. Explain why this fails to prove every rational is $\ge 1$: $\mathbb{Q}$ lacks the inductive / well-ordered successor property of $\mathbb{N}$ (the set $\{x \in \mathbb{Q} : x \ge 1\}$ does not generate all of $\mathbb{Q}$ via $+1$ shifts from 1).
  - *Practises:* Rigorous conceptual understanding of the foundational axioms of $\mathbb{N}$ versus dense ordered fields.

## From the post
(no text)

## Files
- [Assignment-8.pdf](https://drive.google.com/file/d/1YiTcK2EvgOSJThtPskmQyCgc1juz9D2s/view?usp=drive_web)
- Classroom post: [Assignment-8](https://classroom.google.com/c/ODcxNTUyOTc2ODA3/a/ODc0MjI5OTUzMDM5/details)

## Related
- [[intro-to-proofs/2026-10-20-countable-and-uncountable-sets-lectures-17-to-20]]: lecture notes covering countability, Cantor diagonalisation, and $(0, 1) \sim \mathbb{R}$
- [[11-proofs-analysis-topology/concepts/principle-of-mathematical-induction]]: theoretical foundations of PMI and inductive sets
- [[11-proofs-analysis-topology/pa05-induction-and-the-number-systems]]: lecture chapter on induction techniques and number systems
- [[11-proofs-analysis-topology/concepts/uncountable-set]]: Cantor's theorem and diagonal proofs

<!-- kurooto:materialac9d6a1f -->
## Concepts in Assignment-8
[[zettel/uncountable-set]], [[zettel/inductive-set]], [[zettel/cantor-s-theorem]]
<!-- /kurooto:materialac9d6a1f -->
