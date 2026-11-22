---
title: MTH2133 Past Papers 2025 - Solved
aliases: [Introduction to Proofs midsem 2025, MTH2133 2025, proofs past paper]
subject: proofs
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/proofs, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# MTH2133 Introduction to Proofs: Mid-sem 2025, Solved

[[Proofs, Analysis and Topology - Course Map|Course Map]] · [[Proofs Quiz Prep]]

<span class="scope-taught">taught · last year's mid-sem (Steven Spallone)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The paper
> `Sem-3 Papers(Aug 2025)/Mid Sem/Introduction to Proofs.pdf` (1 p., scan), from the Drive **Question Paper Archive → Sem-3**, downloaded 2026-11-22 to `math/proofs-analysis-topology/lecture-notes-slides/past-papers/qp-archive/`. Mid-sem of **24 Sep 2025**, 7 questions × 10 points, best 60. **The archive has no other proofs paper**, so this year's note has a mid-sem only. This year's mid-sem and its solutions are already in the vault ([[Mid-Sem-Exam-MT2133-solutions-students.pdf]]). Solutions mine.

> [!question] Q.I · $f:(0,\infty)\to\mathbb R$ differentiable with $xf'(x)=f(x)$ for all $x>0$. Prove $\exists C$ with $f(x)=Cx$ for all $x>0$ (no moving differentials around).

> [!example]- Solution ([[PA13 The Derivative and the Inverse Function Theorem]])
> Let $g(x)=f(x)/x$ on $(0,\infty)$. It is differentiable, with $g'(x)=\dfrac{xf'(x)-f(x)}{x^2}=0$. By the **mean value theorem**, for any $0<a<b$, $g(b)-g(a)=g'(\xi)(b-a)=0$. So $g$ is constant, $g\equiv C$ (e.g. $C=f(1)$), and $f(x)=Cx$. ∎

> [!question] Q.II · $A,B,C\subseteq X$: is $A\cap B\cap C\subseteq(A\triangle B)\triangle C$? (a) Venn diagram; (b) reduce to propositional logic.

> [!example]- Solution ([[PA02 Sets Families and the ZFC Foundations]], [[PA01 Logic and Methods of Proof]])
> (a) $(A\triangle B)\triangle C$ consists of the points in an **odd number** of the three sets: the three "only" regions plus the triple overlap. The triple overlap (3, odd) is shaded, so the inclusion is **true**.
> (b) With $a,b,c$ for "$x\in A$" etc., the statement is $\forall x\,[(a\wedge b\wedge c)\to((a\oplus b)\oplus c)]$. This is a tautology: if $a=b=c=$ T then $a\oplus b=$ F and F $\oplus$ T $=$ T. ∎

> [!question] Q.III · Over the integers, which are true? (a) $\forall z\exists x\exists!y\,(xy=z)$; (b) $\exists!x\forall y\exists!z\,(xy=z)$; (c) $\exists!z\forall y\exists x\,(xy=z)$; (d) $\exists x\exists y\exists!z\,(xy=z)$; (e) $\forall x\exists!z\exists y\,(xy=z)$.

> [!example]- Solution ([[PA01 Logic and Methods of Proof]])
> - (a) **True**: take $x=1$; then $y=z$ is the unique solution (for $z=0$ too).
> - (b) **False**: for *every* $x$, $z=xy$ is unique, so $x$ is not unique.
> - (c) **True**: $y=0$ forces $z=0$, and $z=0$ works (take $x=0$). So exactly one such $z$.
> - (d) **True**: any $x,y$; $z=xy$ is unique.
> - (e) **False**: for $x=1$, every $z$ is of the form $1\cdot y$, so $z$ is not unique.
>
> **Answer: (a), (c), (d).** (Checked by brute force on a range of integers.)

> [!question] Q.IV · Prove no rational number has square 2/3.

> [!example]- Solution ([[PA05 Induction and the Number Systems]])
> Suppose $(p/q)^2=2/3$ with $p,q$ integers, $q>0$, $\gcd(p,q)=1$. Then $3p^2=2q^2$. So $2\mid3p^2$, and since 2 is prime and $2\nmid3$, $2\mid p$. Write $p=2m$: $12m^2=2q^2$ ⇒ $q^2=6m^2$ ⇒ $2\mid q^2$ ⇒ $2\mid q$, contradicting $\gcd(p,q)=1$. ∎ (Alternatively, use $3\mid2q^2$ ⇒ $3\mid q$, then $3\mid p$.)

> [!question] Q.V · (a) A positive *left* integer has a prime factor that is also a left integer. (b) There are infinitely many left primes.

> [!example]- Solution ([[PA09 Strong Induction and Recursion]])
> [!verify] "Left integer" is a definition from the 2025 lectures and is not in the vault. The two-part structure is the classic one for $n\equiv3\pmod4$ (or $n\equiv2\pmod3$). The proof below is for **$n\equiv3\pmod4$**; the mod-3 version is identical with $3p_1\cdots p_k-1$.
> (a) Let $n\equiv3\pmod4$, $n>0$. $n$ is odd, so all its prime factors are odd: each is $\equiv1$ or $3\pmod4$. If all were $\equiv1$, their product $n$ would be $\equiv1\pmod4$ (since $1\cdot1\equiv1$), a contradiction. So some prime factor is $\equiv3\pmod4$. (Formally: induction on the number of prime factors, or strong induction on $n$.)
> (b) Suppose $p_1,\dots,p_k$ are all the left primes. Let $N=4p_1\cdots p_k-1\equiv3\pmod4$. By (a) $N$ has a left prime factor $p_i$. But $p_i\mid4p_1\cdots p_k$, so $p_i\mid1$, a contradiction. ∎

> [!question] Q.VI · How many decimal digits does $3^{20}$ have? Prove it.

> [!example]- Solution
> **10 digits**; equivalently, $10^9\le3^{20}<10^{10}$. Upper bound: $3^{20}=9^{10}<10^{10}$. Lower bound: $3^{20}=81^5>80^5=2^{20}\cdot5^5=3\,276\,800\,000>10^9$. (Indeed $3^{20}=3\,486\,784\,401$.) ∎

> [!question] Q.VII · $x\in(0,1)$ with an eventually periodic decimal expansion. (a) Define it. (b) A formula for $x$ as a rational. (c) If $n>0$ is not divisible by 2 or 5, prove $\exists k>0$ with $n\mid10^k-1$ (use $1/n$).

> [!example]- Solution ([[PA06 The Real Numbers and Sequences]])
> (a) $x=0.a_1a_2a_3\ldots$ is **eventually periodic** if there are $N\ge0$ and $p\ge1$ with $a_{n+p}=a_n$ for all $n>N$.
> (b) With $A=\overline{a_1\cdots a_N}$ and $B=\overline{a_1\cdots a_{N+p}}$ (as integers): $x=\dfrac{B-A}{10^N(10^p-1)}$. (Example: $0.1\overline{6}=\frac{16-1}{10\cdot9}=\frac16$.)
> (c) $1/n$ is rational, so its decimal expansion is eventually periodic (long division has only $n$ possible remainders). By (b), $\dfrac1n=\dfrac{M}{10^N(10^p-1)}$ for some integer $M$, so $nM=10^N(10^p-1)$ and $n\mid10^N(10^p-1)$. Since $\gcd(n,10)=1$, $\gcd(n,10^N)=1$, and Euclid's lemma gives $n\mid10^p-1$. Take $k=p\ge1$. (If the expansion terminates, use period $p=1$ with repeating 0s; the formula still holds.) ∎ (This is the order of 10 mod $n$; cf. Euler's theorem $10^{\varphi(n)}\equiv1$.)

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | questions | `Sem-3 Papers(Aug 2025)/Mid Sem/Introduction to Proofs.pdf` (Drive QP archive, 2026-11-22; scan) | taught (past paper) |
> | Q.III, Q.VI checks | brute force in Python (this session) | extra/beyond |
>
> **Flags.** [!verify] The definition of "left integer" (Q.V).
