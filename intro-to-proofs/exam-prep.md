---
id: intro-to-proofs/exam-prep
aliases: ["Exam prep: Intro to Proofs"]
tags: [exam-prep, intro-to-proofs]
trust_tier: agent_written
---

# Exam prep: Intro to Proofs

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
Not announced yet. The mid-sem was held on 2026-09-25 (answer key: [[intro-to-proofs/2026-10-05-mid-term-paper-answer-key]]); no later quiz or exam date has been posted. (A Quiz 3 for Batch 3 was graded on 2026-09-17.) Mid-sem portion, for reference: everything in class till 18 Sept except the proof that every vector space has a basis.

## Covered so far
- [[intro-to-proofs/2026-09-03-assignment-4]]: posets (extremal elements, bounds, glb/lub), equivalence relations, partitions; 9 problems
- [[intro-to-proofs/2026-09-15-ordered-pairs]]: Kuratowski ordered pair and which other encodings work or fail
- [[intro-to-proofs/2026-09-15-tautology]]: tautology vs. merely true statement
- [[intro-to-proofs/2026-09-15-application-of-zorn-s-lemma]]: Zorn's lemma and the existence of a basis
- [[intro-to-proofs/2026-10-05-mid-term-paper-answer-key]]: mid-sem solutions: definitions, truth table, negations, set identities, indexed families, $[a]=[b]\iff a\sim b$, lub from glb
- [[intro-to-proofs/2026-10-08-assignment-5]]: not read (file not downloaded)
- [[intro-to-proofs/2026-10-08-assignment-6]]: not read (file not downloaded)
- [[intro-to-proofs/2026-10-15-assignment-7]]: not read (file not downloaded)

## Must know
- Ordered pair property (OP): $(A,B)=(C,D)\iff A=C$ and $B=D$; a proposed encoding $F$ is valid iff $F(A,B)=F(C,D)\iff A=C,\ B=D$.
- Kuratowski: $(A,B)=\{\{A\},\{A,B\}\}$; $\bigcap(A,B)=\{A\}$, $\bigcup(A,B)=\{A,B\}$. $\{A,B\}$, $\{\{A\},\{B\}\}$ and $\{A,\{B\}\}$ fail; $\{A,\{A,B\}\}$ works in ZFC but needs Regularity.
- $(A,A)=\{\{A\}\}\ne\{A\}$ by Regularity (else $A\in A$); this is a consequence, not the defining property.
- Tautology: a compound statement true under every truth assignment, a property of logical form. True statement $\not\Rightarrow$ tautology (e.g. $0\ne1$, $5<7$); $(P\land Q)\Rightarrow P$, $P\lor\lnot P$ and $P\land(P\Rightarrow Q)\Rightarrow Q$ are tautologies (Classroom: mid-sem Q1-Q2).
- Partial order: reflexive, antisymmetric, transitive. Equivalence relation: reflexive, symmetric, transitive (mid-sem Q1).
- Negation rules: $\lnot(\forall x\,p)\sim\exists x\,\lnot p$; $\lnot(\exists y\,q)\sim\forall y\,\lnot q$; $\lnot(P\Rightarrow Q)\sim P\land\lnot Q$ (mid-sem Q3).
- $A\times B=B\times A\Rightarrow A=B$ fails only when one set is empty and the other is not; a minimum need not exist when minimal elements do (e.g. $\{2,3\}$ under divisibility) (mid-sem Q4).
- Chain: subset of a poset with every two elements comparable. Maximal: $m\le x\Rightarrow x=m$.
- Zorn's Lemma: a nonempty poset in which every chain has an upper bound has a maximal element.
- Every vector space over a field has a basis (proof: poset of linearly independent sets under inclusion; union of a chain is independent; a maximal element spans, else add a vector outside the span). Excluded from the mid-sem portion.
- $[a]=[b]\iff a\sim b$; two equivalence classes are equal or disjoint; equivalence relations correspond to partitions (mid-sem Q7, Assignment 4 Q8-Q9).
- Minimum is unique if it exists; every nonempty finite poset has a maximal and a minimal element.
- If every nonempty subset of a poset has a glb and $S$ has an upper bound, then $\mathrm{lub}(S)=\mathrm{glb}(\text{upper bounds of }S)$ (mid-sem Q8).
- $a\equiv b\pmod n\Rightarrow a^2\equiv b^2\pmod n$; $\bigcup_{n\in\mathbb N}n\mathbb Z=\mathbb Z$, $\bigcap_{n\in\mathbb N}n\mathbb Z=\{0\}$.

## Typical questions
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

## Gaps
- Assignments 3, 5, 6 and 7: files could not be downloaded, so their problems are not in the notes. Assignment 5 to 7 are presumably post-mid-sem topics; the topics are unknown.
- No due dates are posted for Assignments 3 to 7.
- No class material after the mid-sem has been filed, and no exam or quiz date is known.
<!-- /kurooto:exam-prep -->
