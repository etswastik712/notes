---
id: intro-to-proofs/2026-10-30-assignment-9
aliases: [Assignment-9]
tags: [intro-to-proofs, coursework]
trust_tier: agent_written
---
# Assignment-9

## Covered
Coursework sheet on strong induction and the Well-Ordering Principle (Classroom file: Assignment-9.pdf).

**Definitions and conventions**
- Strong induction: for each $n\in\mathbb N$ let $P(n)$ be a statement. If (i) $P(1)$ is true, and (ii) for every $k\in\mathbb N$, the truth of all of $P(1),P(2),\dots,P(k)$ implies the truth of $P(k+1)$, then $P(n)$ is true for every $n\in\mathbb N$.
- Least element: for $S\subseteq\mathbb N$, $m\in S$ is a least element if $m\le s$ for every $s\in S$. It is unique if it exists, and we write $m=\min S$.
- Well-Ordering Principle (WOP): every nonempty subset of $\mathbb N$ has a least element.
- PMI, strong induction and WOP are three equivalent statements about $\mathbb N$ (proved in class).
- Standard use of WOP: suppose the set $S$ of counterexamples is nonempty, let $m=\min S$, and produce a counterexample smaller than $m$.
- WOP also holds for $\mathbb N\cup\{0\}$ and for $\{n\in\mathbb Z: n\ge m\}$ for any fixed $m\in\mathbb Z$.
- Writing rule for induction (ordinary or strong): say what $P(n)$ is, prove the base case(s), state exactly what is assumed in the inductive step, prove $P(k+1)$, and conclude.
- Writing rule for WOP: say which set you take the least element of, and why that set is nonempty.

**Problems and what each one practises**
- Q1(a): a recursive sequence with $a_2=3$ and $a_n=a_{n-1}+a_{n-2}$ for $n\ge 3$; prove a bound on $a_n$ for every $n\in\mathbb N$ and explain why two base cases are needed. *Practises:* strong induction where the step uses two earlier terms. (The PDF text is garbled here: $a_1$ and the bound, probably "$<7/4$", are not legible; check the original PDF.)
- Q1(b): $b_1=2$, $b_2=4$, $b_n=4b_{n-1}-4b_{n-2}$ for $n\ge3$; compute $b_3,b_4,b_5$, guess a closed formula, prove it by strong induction. *Practises:* pattern guessing and strong induction on a two-term recurrence.
- Q1(c): every integer $n\ge8$ is $3x+5y$ with $x,y\ge0$ integers; say how many base cases are needed and why; show the statement is false for $n=7$. *Practises:* strong induction with a shifted starting point and several base cases (a step that reaches back by 3).
- Q2(a): prove directly that WOP implies strong induction, using $S=\{n\in\mathbb N: P(n)\text{ is false}\}$, assuming $S\ne\emptyset$ and considering $\min S$. *Practises:* the equivalence of the three principles.
- Q3(a): by WOP, every integer $n\ge2$ has a prime divisor. *Practises:* WOP on a set of integers $\ge2$ with no prime divisor.
- Q3(b): every nonempty subset of $\mathbb Z$ bounded below has a least element. *Practises:* reducing to WOP by shifting into $\mathbb N$ or $\mathbb N\cup\{0\}$.
- Q3(c): there is no rational number whose square is 3. *Practises:* WOP applied to denominators (minimal counterexample).
- Q4(a): $P(n)$: "$n^2+n$ is even". Prove it by WOP: take the least $m$ where it fails, show $P(m-1)$ also fails (treat $m=1$ separately). *Practises:* minimal-counterexample argument.
- Q4(b): prove the same statement by ordinary induction, then compare: where does the inductive step of (b) appear inside the argument of (a)? *Practises:* seeing induction and WOP as the same argument.

## From the post
(no text)

## Files
- [Assignment-9.pdf](https://drive.google.com/file/d/1pfURFWC4V6-nDx6G7Q-kn_nynzxQrpfd/view?usp=drive_web): read; Q1(a) text is partly garbled.

## Related
- [[intro-to-proofs/2026-10-22-assignment-8]]: previous sheet; PMI and the four parts of an induction proof
- [[intro-to-proofs/2026-10-19-solutions-assignment-7]]: Q4 there uses induction and a WOP minimum extraction
- [[11-Proofs-Analysis-Topology/PA09 Strong Induction and Recursion]]: their chapter on strong induction
- [[11-Proofs-Analysis-Topology/PA10 Well-Ordering and Well-Ordered Pairs]]: their chapter on WOP
