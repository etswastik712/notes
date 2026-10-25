---
id: intro-to-proofs/exam-prep
aliases: ["Exam prep: Intro to Proofs"]
tags: [exam-prep, intro-to-proofs]
trust_tier: agent_written
---

# Exam prep: Intro to Proofs

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
Not announced yet. The mid-sem was held on 2026-09-25 (answer key: [[intro-to-proofs/2026-10-05-mid-term-paper-answer-key]]). Quizzes are held during tutorials; Quizzes 3 and 4 have been graded (answer sheets can be collected during Batch 1 office hours, Tuesdays 4:00-5:00 PM in A459). Evaluation: internal 20%, mid-sem 40%, end-sem 40% (Classroom: announcement 2026-08-04). No future quiz or end-sem dates have been posted yet.

## Covered so far
- [[intro-to-proofs/2026-08-06-assignment-1]]: truth tables, De Morgan, tautology/contradiction/contingency, primes, Goldbach and twin prime conjectures
- [[intro-to-proofs/2026-08-13-assignment-2]]: conditionals (converse, contrapositive), quantifiers, negation, quantifier order
- [[intro-to-proofs/2026-09-03-assignment-4]]: posets (extremal elements, bounds, glb/lub), equivalence relations, partitions; 9 practice problems
- [[intro-to-proofs/2026-09-15-ordered-pairs]]: Kuratowski ordered pair and which other encodings work or fail
- [[intro-to-proofs/2026-09-15-tautology]]: tautology vs. merely true statement
- [[intro-to-proofs/2026-09-15-application-of-zorn-s-lemma]]: Zorn's lemma and the existence of a basis
- [[intro-to-proofs/2026-10-05-mid-term-paper-answer-key]]: mid-sem solutions: definitions, truth table, negations, set identities, indexed families, $[a]=[b]\iff a\sim b$, lub from glb
- [[intro-to-proofs/2026-10-08-assignment-5]]: not read (file not downloaded)
- [[intro-to-proofs/2026-10-08-assignment-6]]: not read (file not downloaded)
- [[intro-to-proofs/2026-10-15-assignment-7]]: countable sets, Cartesian products; questions 4 and 5 solved in [[intro-to-proofs/2026-10-19-solutions-assignment-7]]
- [[intro-to-proofs/2026-10-19-solutions-assignment-7]]: instructor solutions for Assignment 7 Q4 (subsets of countable sets) and Q5 (bijections on $A \times B$)
- [[intro-to-proofs/2026-10-20-countable-and-uncountable-sets-lectures-17-to-20]]: Lectures 17 to 20: countability of $\mathbb{Q}$, subset of countable is countable, Cantor's diagonal argument for uncountability of $(0, 1)$ and $\mathbb{R}$, continuum hypothesis
- [[intro-to-proofs/2026-10-22-assignment-8]]: Assignment 8: countability of unions, irrational numbers $\mathbb{R} \setminus \mathbb{Q}$, $\{0, 1\}^\mathbb{N}$, Cantor's theorem $|A| < |\mathcal{P}(A)|$, interval bijections $[0, 1) \sim (0, 1) \sim \mathbb{R}$, induction (PMI) identities and scope

## Must know
- Logical equivalence $\sim$ is not equality $=$; De Morgan: $\lnot(P\lor Q)\sim\lnot P\land\lnot Q$ and $\lnot(P\land Q)\sim\lnot P\lor\lnot Q$; $(P\Rightarrow Q)\sim(\lnot P\lor Q)$; $P\lor Q\sim\lnot(\lnot P\land\lnot Q)$ (Classroom: Assignment 1 Q3).
- Contrapositive $\lnot Q\Rightarrow\lnot P$ is equivalent to $P\Rightarrow Q$; the converse $Q\Rightarrow P$ is not. "$P$ only if $Q$", "$P$ is sufficient for $Q$" and "$Q$ is necessary for $P$" all express $P\Rightarrow Q$ (Classroom: Assignment 2 Q1).
- Order of quantifiers matters: $\forall x\,\exists y\,(y>x)$ is not the same as $\exists y\,\forall x\,(y>x)$ (Classroom: Assignment 2 Q6).
- Ordered pair property (OP): $(A,B)=(C,D)\iff A=C$ and $B=D$; a proposed encoding $F$ is valid iff $F(A,B)=F(C,D)\iff A=C,\ B=D$.
- Kuratowski encoding: $(A,B)=\{\{A\},\{A,B\}\}$; $\bigcap(A,B)=\{A\}$, $\bigcup(A,B)=\{A,B\}$. $\{A,B\}$, $\{\{A\},\{B\}\}$ and $\{A,\{B\}\}$ fail; $\{A,\{A,B\}\}$ works in ZFC but needs Regularity.
- $(A,A)=\{\{A\}\}\ne\{A\}$ by Regularity (else $A\in A$); this is a consequence, not the defining property.
- Tautology: a compound statement true under every truth assignment, a property of logical form. True statement $\not\Rightarrow$ tautology (e.g. $0\ne1$, $5<7$); $(P\land Q)\Rightarrow P$, $P\lor\lnot P$ and $P\land(P\Rightarrow Q)\Rightarrow Q$ are tautologies (Classroom: mid-sem Q1-Q2). A contradiction is false under every assignment, e.g. $P\land\lnot P$ (Classroom: Assignment 1 Q4).
- Partial order: reflexive ($a \le a$), antisymmetric ($a \le b \land b \le a \implies a=b$), transitive ($a \le b \land b \le c \implies a \le c$). Equivalence relation: reflexive, symmetric, transitive (mid-sem Q1).
- Negation rules: $\lnot(\forall x\,p)\sim\exists x\,\lnot p$; $\lnot(\exists y\,q)\sim\forall y\,\lnot q$; $\lnot(P\Rightarrow Q)\sim P\land\lnot Q$ (mid-sem Q3, Assignment 2).
- $A\times B=B\times A\Rightarrow A=B$ fails only when one set is empty and the other is not; a minimum need not exist when minimal elements do (e.g. $\{2,3\}$ under divisibility) (mid-sem Q4).
- Chain: subset of a poset with every two elements comparable. Maximal element $m$: $m\le x\Rightarrow x=m$.
- Zorn's Lemma: a nonempty poset in which every chain has an upper bound has a maximal element.
- Basis of a vector space: every vector space over a field has a basis (poset of linearly independent subsets ordered by inclusion; union of a chain is independent; maximal element spans).
- Equivalence classes: $[a]=[b]\iff a\sim b$; two equivalence classes are either identical or disjoint; equivalence relations on $A$ are in bijection with partitions of $A$ (mid-sem Q7, Assignment 4 Q8-Q9).
- Minimum is unique if it exists; every nonempty finite poset has at least one maximal and one minimal element.
- Lub from glb: if every nonempty subset of a poset has a glb and $S$ has an upper bound, then $\mathrm{lub}(S)=\mathrm{glb}(\text{upper bounds of }S)$ (mid-sem Q8).
- Congruence mod $n$: $a\equiv b\pmod n\Rightarrow a^2\equiv b^2\pmod n$; $\bigcup_{n\in\mathbb N}n\mathbb Z=\mathbb Z$, $\bigcap_{n\in\mathbb N}n\mathbb Z=\{0\}$.
- Finite set: $A = \emptyset$ or there exists a bijection $A \to \{1, 2, \dots, k\}$ for some $k \in \mathbb{N}$ (Classroom: Lecture 17).
- Equicardinality: $|A| = |B| \iff \exists$ bijection $A \to B$. Cardinality equivalence $\sim$ is reflexive, symmetric ($f^{-1}$), and transitive ($g \circ f$) (Classroom: Lecture 17-18).
- Countable set: a set is countable if it is finite or in bijection with $\mathbb{N}$ ($|A| = \aleph_0$) (Classroom: Lecture 17).
- Countability of $\mathbb{Q}$: $\mathbb{Q}_{>0}$ is countable via diagonal grid traversal of reduced fractions $m/n$; $\mathbb{Q}_{<0}$ is countable via $x \mapsto -x$; $\mathbb{Q} = \mathbb{Q}_{<0} \cup \{0\} \cup \mathbb{Q}_{>0}$ is countably infinite via $f(1)=0$, $f(2k)=a_k$, $f(1+2t)=-a_t$ (Classroom: Lecture 17).
- Subsets of countable sets: if $A \subseteq B$ and $B$ is finite, $A$ is finite; if $B$ is countably infinite, any non-empty subset $A \subseteq B$ is countable (well-ordering extraction of increasing indices $n_{k+1} = \min\{n > n_k : f(n) \in A\}$) (Classroom: Lecture 18, Assignment 7 Q4).
- Uncountable set criterion: if $A \subseteq B$ and $A$ is uncountable, then $B$ is uncountable (Classroom: Lecture 18, Assignment 8).
- Proper subset non-equivalence: a finite set is never in bijection with any of its proper subsets. Conversely, any infinite set is in bijection with a proper subset (e.g. $\mathbb{N} \sim \text{odd natural numbers}$ via $n \mapsto 2n-1$) (Classroom: Lecture 18).
- Uncountability of $(0, 1)$: every real in $(0, 1)$ has a unique normalized decimal representation (not ending in infinite 9s); no function $f: \mathbb{N} \to (0, 1)$ is surjective by Cantor's diagonal argument (perturber $b_k = 3$ if $a_{kk} \ne 3$, $b_k = 7$ if $a_{kk}=3$ satisfies $b \notin \operatorname{Im}(f)$) (Classroom: Lecture 19).
- Interval equicardinality: any open interval $(a, b) \sim (0, 1)$ via linear bijection $f(x) = a + (b-a)x$. $(0, 1) \sim \mathbb{R}$ via piecewise bijection $f(x) = 1 - \frac{1}{2x}$ on $(0, 1/2]$ and $\frac{1}{2(1-x)} - 1$ on $[1/2, 1)$ with inverse $g(y) = \frac{1}{2(1-y)}$ for $y \le 0$ and $1 - \frac{1}{2(1+y)}$ for $y \ge 0$. Hence $(a, b)$ and $\mathbb{R}$ are uncountable, with $|\mathbb{R}| = \mathfrak{c} = 2^{\aleph_0}$ (Classroom: Lecture 19-20).
- Boundary absorption (Hilbert hotel): $[0, 1) \sim (0, 1)$ via $g(0) = 1/2$, $g(1/n) = 1/(n+1)$ for $n \ge 2$, $g(x) = x$ otherwise; hence $[0, 1] \sim (0, 1) \sim \mathbb{R}$ (Classroom: Assignment 8 Q5).
- Countable union of countable sets: if $\{A_i\}_{i \in \mathbb{N}}$ are pairwise disjoint and countably infinite with bijections $f_i: \mathbb{N} \to A_i$, then $F((i, n)) = f_i(n)$ is a bijection $\mathbb{N} \times \mathbb{N} \to \bigcup_{i \in \mathbb{N}} A_i$, so $\bigcup_{i \in \mathbb{N}} A_i$ is countably infinite (Classroom: Assignment 8 Q2).
- Irrationals: $\mathbb{R} \setminus \mathbb{Q}$ is uncountable (if countable, $\mathbb{R} = \mathbb{Q} \cup (\mathbb{R} \setminus \mathbb{Q})$ would be countable) (Classroom: Assignment 8 Q1).
- Sequence space: $\{0, 1\}^\mathbb{N}$ is uncountable via diagonal sequence $b_n = 1 - a_{nn}$ (Classroom: Assignment 8 Q3).
- Cantor's Theorem: for every set $A$, $|A| < |\mathcal{P}(A)|$; no function $f: A \to \mathcal{P}(A)$ is surjective, because $B = \{a \in A : a \notin f(a)\} \notin \operatorname{Im}(f)$ (Classroom: Lecture 20, Assignment 8 Q4).
- Continuum Hypothesis (CH): there is no set $X$ with $\aleph_0 < |X| < \mathfrak{c}$; independent of ZFC (Gödel 1940, Cohen 1963) (Classroom: Lecture 20).
- Inductive sets and PMI: $S \subseteq \mathbb{N}$ is inductive if $k \in S \implies k+1 \in S$. If $1 \in S$ and $S$ is inductive, $S = \mathbb{N}$. Every induction proof requires: (1) predicate $P(n)$, (2) base case, (3) inductive hypothesis $P(k) \implies P(k+1)$, (4) conclusion by PMI (Classroom: Assignment 8).

## Typical questions
- Build truth tables (up to three variables), verify equivalences such as De Morgan, classify as tautology/contradiction/contingency: [[intro-to-proofs/2026-08-06-assignment-1]] Q1-Q5.
- Express a conditional in "only if", "sufficient", "necessary" forms; write converse and contrapositive; negate conditionals as $P\land\lnot Q$: [[intro-to-proofs/2026-08-13-assignment-2]] Q1-Q2.
- Symbolise quantified statements, negate them and compare truth values (including quantifier order and the $L(x,y)$ likes-book family): Assignment 2 Q3-Q8.
- Minimal/maximal, minimum/maximum, bounds, glb/lub of a subset of a poset (divisibility, power set, product order, subspaces): [[intro-to-proofs/2026-09-03-assignment-4]] Q1-Q4.
- Decide whether a relation is an equivalence relation and find its classes; build relations with prescribed properties: Assignment 4 Q5-Q7.
- Prove uniqueness of the minimum, existence of maximal elements in finite posets, classes equal or disjoint, equivalence relation $\leftrightarrow$ partition: Assignment 4 Q8-Q9.
- Test whether a set expression is a valid ordered pair: [[intro-to-proofs/2026-09-15-ordered-pairs]].
- Decide whether a statement is a tautology (truth table) vs. just true: [[intro-to-proofs/2026-09-15-tautology]]; build a truth table: mid-sem Q2.
- Negate quantified statements and decide which version is true: mid-sem Q3.
- Prove set identities by double inclusion; compute unions and intersections of indexed families: mid-sem Q5-Q6 in [[intro-to-proofs/2026-10-05-mid-term-paper-answer-key]].
- Prove $[a]=[b]\iff a\sim b$; list a congruence class: mid-sem Q7.
- Prove a lub exists from glb hypotheses: mid-sem Q8.
- Zorn's lemma argument for existence of a maximal object: [[intro-to-proofs/2026-09-15-application-of-zorn-s-lemma]].
- Prove non-empty subset of a countable set is countable (induction for finite sets, well-ordering minimum extraction for countably infinite): [[intro-to-proofs/2026-10-19-solutions-assignment-7]] Q4.
- Prove $A \times B$ is countably infinite given $A, B$ countably infinite: [[intro-to-proofs/2026-10-19-solutions-assignment-7]] Q5.
- Prove a set is countable by exhibiting an explicit bijection or diagonal traversal with $\mathbb{N}$: [[intro-to-proofs/2026-10-20-countable-and-uncountable-sets-lectures-17-to-20]] (e.g. $\mathbb{Q}$, $\mathbb{Z}$, $E$).
- Prove a countable union of countable sets is countable: [[intro-to-proofs/2026-10-22-assignment-8]] Q2.
- Prove a set is uncountable by showing an uncountable subset or by contradiction using union of countable sets: [[intro-to-proofs/2026-10-22-assignment-8]] Q1b ($\mathbb{R} \setminus \mathbb{Q}$).
- Execute Cantor's diagonal argument: on decimal expansions in $(0, 1)$ ([[intro-to-proofs/2026-10-20-countable-and-uncountable-sets-lectures-17-to-20]]) or on binary sequences $\{0, 1\}^\mathbb{N}$ ([[intro-to-proofs/2026-10-22-assignment-8]] Q3).
- Prove Cantor's theorem $|A| < |\mathcal{P}(A)|$ using the diagonal set $B = \{a \in A : a \notin f(a)\}$: [[intro-to-proofs/2026-10-22-assignment-8]] Q4.
- Construct bijections between intervals with differing boundary points ($[0, 1) \sim (0, 1) \sim [0, 1] \sim \mathbb{R}$): [[intro-to-proofs/2026-10-22-assignment-8]] Q5, [[intro-to-proofs/2026-10-20-countable-and-uncountable-sets-lectures-17-to-20]].
- Mathematical induction proofs: summations, factorials, divisibility ($6 \mid n^3 + 5n$), and inequalities ($2^n > n^2$ for $n \ge 5$): [[intro-to-proofs/2026-10-22-assignment-8]] Q6.
- Conceptual analysis of PMI: explaining why inductive step without base case is insufficient, and why PMI cannot prove statements on $\mathbb{Q}$: [[intro-to-proofs/2026-10-22-assignment-8]] Q7.

## Gaps
- Assignments 3, 5, and 6: files could not be downloaded, so their problem statements are not in the notes.
- Assignment 7: Questions 1 to 3 are not in the notes (only solutions for Questions 4 and 5 were posted).
- No due dates were given in Classroom for Assignments 1, 2, 4, 5, 6, 7 and 8, and no end-sem or future quiz dates have been announced.
- Assignments 1 and 2 are filed as problem lists only; no solutions were posted, so worked answers are not in the notes.
- The syllabus for the end-sem has not been announced; presumably it covers material after the mid-sem (functions, cardinality, induction) but this is not confirmed.
<!-- /kurooto:exam-prep -->
