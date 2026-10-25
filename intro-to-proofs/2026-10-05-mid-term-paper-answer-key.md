---
id: intro-to-proofs/2026-10-05-mid-term-paper-answer-key
aliases: [Mid term paper answer key]
tags: [intro-to-proofs, exam, solutions]
trust_tier: agent_written
---
# Mid term paper answer key

## Covered
Mid Semester Examination MT2133 (Introduction to Proofs), 25 Sept 2026, 2 hours, 40 points; instructor's solutions (Classroom: Mid-Sem-Exam-MT2133-solutions-students.pdf).

**Q1. Definitions [6].**
- Tautology: a compound statement true for every assignment of truth values to its components (e.g. $P\lor\lnot P$).
- Partial order on $A$: a relation $\le$ with, for all $a,b,c\in A$: reflexive $a\le a$; antisymmetric ($a\le b$ and $b\le a\Rightarrow a=b$); transitive ($a\le b$, $b\le c\Rightarrow a\le c$).
- Equivalence relation on $A$: reflexive $a\sim a$; symmetric ($a\sim b\Rightarrow b\sim a$); transitive.

**Q2. Truth table of $P\land(P\Rightarrow Q)\Rightarrow Q$ [5].** Columns $P$, $Q$, $P\Rightarrow Q$, $P\land(P\Rightarrow Q)$, whole statement. The last column is T in all four rows, so it is a tautology (modus ponens).

**Q3. Negations [2+2].**
- Rules used: $\lnot(\forall x\,p(x))\sim\exists x\,\lnot p(x)$, $\lnot(\exists y\,q(y))\sim\forall y\,\lnot q(y)$, $\lnot(P\Rightarrow Q)\sim P\land\lnot Q$.
- (a) $\forall x\in\mathbb R,\exists y\in\mathbb R,\ y^2=x$ has negation $\exists x\in\mathbb R,\forall y\in\mathbb R,\ y^2\ne x$. The original is false (take $x=-1$, since $y^2\ge0$).
- (b) $\forall x\in\mathbb Z,(x\text{ odd}\Rightarrow x^2\text{ odd})$ has negation $\exists x\in\mathbb Z,(x\text{ odd}\land x^2\text{ even})$. The original is true: $x=2k+1\Rightarrow x^2=2(2k^2+2k)+1$.

**Q4. True or false [2+2+2].**
- (a) "$A\times B=B\times A\Rightarrow A=B$" is false: $A=\emptyset$, $B=\{1\}$ gives $A\times B=B\times A=\emptyset$. It holds when both sets are nonempty.
- (b) "Every nonempty subset of $(\mathbb N,\mid)$ has a minimum" is false: $S=\{2,3\}$ has minimal elements 2 and 3 but no minimum, since neither divides the other. Any $S$ with two distinct primes works.
- (c) $a\equiv b\pmod n\Rightarrow a^2\equiv b^2\pmod n$ is true: $a-b=nk\Rightarrow a^2-b^2=(a-b)(a+b)=n\,k(a+b)$.

**Q5. Prove $A-(B\cup C)=(A-B)\cap(A-C)$ [4].** Two inclusions. ($\subseteq$) $x\in A$ and $x\notin B\cup C$; by De Morgan $x\notin B$ and $x\notin C$, so $x\in A-B$ and $x\in A-C$. ($\supseteq$) $x\in A$, $x\notin B$, $x\notin C$, so $x\notin B\cup C$, so $x\in A-(B\cup C)$.

**Q6. $A_n=n\mathbb Z$, $n\in\mathbb N$ [2+3].**
- $\bigcup_n A_n=\mathbb Z$ because $A_1=\mathbb Z$.
- $\bigcap_n A_n=\{0\}$. ($\supseteq$) $0=n\cdot0$. ($\subseteq$) If $x\ne0$ is in every $A_n$, let $y=|x|>0$; $y$ is divisible by every positive integer. Take $n=2y$: $y=2y\,k$ gives $1=2k$, impossible by parity. Alternatives given: use $n=y+1$ (then $y=(y+1)k$ has no integer $k$), or note a nonzero integer has only finitely many divisors.

**Q7. Equivalence relations [5+1].**
- (a) $[a]=[b]\iff a\sim b$. ($\Leftarrow$) Let $a\sim b$ and $x\in[a]$: $x\sim a$ by symmetry, $x\sim b$ by transitivity, $b\sim x$ by symmetry, so $[a]\subseteq[b]$; swap roles for $[b]\subseteq[a]$. ($\Rightarrow$) $b\in[b]=[a]$ by reflexivity, so $a\sim b$.
- (b) $100=14\cdot7+2$, so $[100]=[2]=\{7k+2\mid k\in\mathbb Z\}=\{\dots,-12,-5,2,9,16,\dots\}$ in $\mathbb Z/7$.

**Q8. Least upper bound from greatest lower bounds [4].** Hypothesis: every nonempty subset of the poset $A$ has a glb, and $S\subseteq A$ has at least one upper bound. Let $U$ be the (nonempty) set of upper bounds of $S$ and $\alpha=\mathrm{glb}(U)$. Claim 1: $\alpha$ is an upper bound of $S$, since each $s\in S$ is a lower bound of $U$ and $\alpha$ is the greatest lower bound, so $s\le\alpha$. Claim 2: for any upper bound $\gamma$ of $S$ we have $\gamma\in U$, so $\alpha\le\gamma$. Hence $\alpha=\mathrm{lub}(S)$.

Proof patterns worth remembering: double inclusion for set identities; negation by quantifier flipping; counterexample with $\emptyset$ or divisibility order; contradiction via parity; class equality via symmetry plus transitivity; the set of all upper bounds as the auxiliary object.

## From the post
(no text)

## Files
- [Mid-Sem-Exam-MT2133-solutions-students.pdf](https://drive.google.com/file/d/12q-7cQupIQlrLzIdNUXvoe0HDqxLgBpp/view?usp=drive_web)
- Classroom post: [Mid term paper answer key](https://classroom.google.com/c/ODcxNTUyOTc2ODA3/m/ODg5MDUzNDcxNDY5/details)

## Related
- [[11-Proofs-Analysis-Topology/PA01 Logic and Methods of Proof]]: their notes on truth tables, negation and proof methods (Q2, Q3)
- [[11-Proofs-Analysis-Topology/PA02 Sets Families and the ZFC Foundations]]: set identities, indexed unions and intersections (Q4a, Q5, Q6)
- [[11-Proofs-Analysis-Topology/PA03 Relations Equivalence and Order]]: posets, bounds, equivalence classes (Q1, Q4b, Q7, Q8)
- [[intro-to-proofs/2026-09-03-assignment-4]]: practice problems on the same poset and equivalence-relation topics
- [[intro-to-proofs/2026-09-15-tautology]]: tautology vs. true statement (Q1a, Q2)
