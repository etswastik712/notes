---
id: intro-to-proofs/2026-11-10-peano-s-axioms
aliases: [Peano's axioms, Lecture 25]
tags: [intro-to-proofs, lecture]
trust_tier: agent_written
---
# Peano's axioms

## Covered
Source: Lecture 25 handout (Classroom file L-25.pdf). It follows Lecture 24, where $\mathbb N$ was taken as given and PMI accepted as a fact.

**Peano system.** A set $N$ with a distinguished element $1$ and a function $s:N\to N$ (successor) such that
- (P1) $1\notin \operatorname{Im}(s)$, i.e. $s(n)\ne 1$ for all $n$;
- (P2) $s$ is injective: $s(m)=s(n)\Rightarrow m=n$;
- (P3) (Induction) if $S\subseteq N$, $1\in S$ and $s(S)\subseteq S$, then $S=N$.

(P3) is PMI written with $s(k)$ in place of $k+1$, because $+$ is not yet defined. "1" is only a name for the distinguished element, as "e" names the identity of a group. From here only (P1)-(P3) are used.

**Example.** $\{1,2,3,\dots\}$ with $s(n)=n+1$.

**Non-examples (each axiom is needed).**
- $X=\{1\}$, $s(1)=1$: (P2), (P3) hold, (P1) fails.
- $X=\{1,2\}$, $s(1)=2$, $s(2)=2$: (P1), (P3) hold, (P2) fails.
- $X=\mathbb N\cup\mathbb N'$ ($\mathbb N'$ a disjoint copy), $s(n)=n+1$, $s(n')=(n+1)'$: (P1), (P2) hold; $S=\mathbb N$ has $1\in S$, $s(S)\subseteq S$, $S\ne X$, so (P3) fails.

**Lemma 1 (predecessor).** Every $n\ne1$ is $s(m)$ for exactly one $m$. Proof: $S=\{1\}\cup\operatorname{Im}(s)$ contains $1$ and is closed under $s$, so $S=N$ by (P3); uniqueness is (P2).

**Addition.** $n+1:=s(n)$ and $n+s(m):=s(n+m)$. Once $m+1$ is written for $s(m)$, the second rule reads $n+(m+1)=(n+m)+1$; this is a definition, not associativity. Example: $2+2=2+s(1)=s(2+1)=s(s(2))=s(3)=4$. That these rules define a single function $N\times N\to N$ is the Recursion Theorem, taken as given.

**Theorem 3.** $1+n=n+1$. Induction on $n$: $1+(k+1)=(1+k)+1=(k+1)+1$ (second rule, then hypothesis).

**Theorem 4 (associativity).** $(a+b)+c=a+(b+c)$. Fix $a,b$, induct on $c$. Base: second rule. Step: $(a+b)+(c+1)=((a+b)+c)+1=(a+(b+c))+1=a+((b+c)+1)=a+(b+(c+1))$.

**Order.** $a<b$ iff $b=a+x$ for some $x\in N$; $a\le b$ iff $a<b$ or $a=b$.

**Theorem 5.** $a<b\Rightarrow a+1\le b$ (nothing lies strictly between $a$ and $a+1$). Proof: $b=a+x$; if $x=1$ done; otherwise $x=y+1$ (Lemma 1) and $b=a+(y+1)=a+(1+y)=(a+1)+y$ by Theorems 3 and 4, so $a+1<b$.

Theorem 5 and Lemma 1 are exactly the two facts used in Lecture 24 to prove WOP from PMI, so PMI $\Leftrightarrow$ WOP rests only on (P1)-(P3) and the definitions of $+$ and $<$.

**Multiplication.** $n\cdot1:=n$, $n\cdot(m+1):=n\cdot m+n$.

**Further results (all by induction).** $s(n)\ne n$; commutativity $a+b=b+a$ (induction on $b$; base is Theorem 3); cancellation $a+c=b+c\Rightarrow a=b$ (uses P2); trichotomy (exactly one of $a<b$, $a=b$, $b<a$); $<$ transitive and $a<b\Rightarrow a+c<b+c$; multiplication associative, commutative, distributive over $+$, with identity $1$.

**Remarks.**
- Any two Peano systems are isomorphic (a bijection taking $1$ to $1$ and commuting with the successors), which justifies speaking of *the* natural numbers.
- $\mathbb Z$ (classes of pairs $(a,b)$, as $a-b$), then $\mathbb Q$ (classes of pairs $(a,b)$, $b\ne0$, as $a/b$), then $\mathbb R$ (Dedekind cuts); each step uses an equivalence relation.
- The axioms do not assert existence. ZFC gives a model $\mathbb N_0$: $0=\emptyset$, $s(x)=x\cup\{x\}$, with the Axiom of Infinity giving the set $\{0,s(0),s(s(0)),\dots\}$; then (P1)-(P3) are theorems.
- Starting from $1=\emptyset$ instead gives $\mathbb N$; $(\mathbb N_0,s)$ and $(\mathbb N,s)$ are different but isomorphic Peano systems.

**Exercises on the sheet.** (a) $a+c=b+c\Rightarrow a=b$. (b) $n\cdot1=1\cdot n$. (c) $a(b+c)=ab+ac$. (d) no $n$ satisfies $n<1$. (e) $a<b$ and $b<a$ cannot both hold (use cancellation and $s(n)\ne n$).

## From the post
(no text)

## Files
- [L-25.pdf](https://drive.google.com/file/d/1_jOCzJWoIJpxbgV1iibWHW19hLlip6XQ/view?usp=drive_web): read in full. Lecture 24 itself is not in the notes.

## Related
- [[intro-to-proofs/2026-10-30-assignment-9]]: PMI, strong induction and WOP are shown equivalent there; this handout derives the foundations
- [[intro-to-proofs/2026-10-22-assignment-8]]: PMI and inductive sets, which (P3) restates
- [[11-Proofs-Analysis-Topology/PA05 Induction and the Number Systems]]: their chapter on induction and the construction of number systems
- [[11-Proofs-Analysis-Topology/PA08 Mathematical Induction]]: their chapter on PMI
- [[11-Proofs-Analysis-Topology/PA10 Well-Ordering and Well-Ordered Pairs]]: their chapter on WOP
- [[zettel/well-ordering-principle]]: WOP, proved from PMI using Lemma 1 and Theorem 5 here

<!-- kurooto:material75d65193 -->
## Concepts in L-25
[[zettel/peano-system]], [[zettel/successor-function-predecessor-property]], [[zettel/recursive-definition-of-addition]], [[zettel/commutativity-with-one]], [[zettel/associativity-of-addition]], [[zettel/natural-number-order]], [[zettel/discrete-order-step-property]], [[zettel/recursive-definition-of-multiplication]]
<!-- /kurooto:material75d65193 -->
