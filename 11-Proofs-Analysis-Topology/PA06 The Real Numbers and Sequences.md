---
title: PA06 The Real Numbers and Sequences
aliases: [PA06, real numbers, completeness, least upper bound, Dedekind cuts, Archimedean property, sequences, limits, Cauchy sequences, Bolzano-Weierstrass]
subject: analysis
type: chapter
chapter: 6
part: V
scope: [taught, extra-book, extra-beyond]
by: [lecture-notes, ai-notes]
status: draft
prereq: [PA05 Induction and the Number Systems]
tags: [subject/analysis, type/chapter, taught, extra/book, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# PA06 · The Real Numbers and Sequences

◀ [[PA05 Induction and the Number Systems]] · [[PA07 Metric and Topological Spaces]] ▶

<span class="scope-taught">taught (a little)</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Scope of this chapter
> The lecture notes in the folder (Lectures 17–20, Assignments 1–8) use the real numbers only **in passing**: decimal expansions and the geometric series in Lecture 19, "$\mathbb R$ is complete", intervals and the uncountability of $\mathbb R$. **No lecture or assignment treats sequences, limits or completeness theorems.** This chapter is therefore 🟡: it follows the AI-written `proofs-prems-topo.pdf` (Part IV ch. 15 and Part V ch. 16, proofs checked) and standard texts. Ask the instructor whether analysis of sequences is part of this course.

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Used in class** ([[Countable-Uncountable-sets.pdf#page=4|Lecture 19]]): decimal expansions as convergent series (the partial sums $1-10^{-n}\to1$), $0.4999\dots=0.5000\dots$, geometric series, "$\mathbb R$ is complete", intervals $(a,b)$.
>
> 🟡 **Extra · book** (AI notes ch. 15–16; Rudin, *Principles of Mathematical Analysis*, Ch. 1–3; Kumaresan et al.)
> - §1 $\mathbb Q$ is not complete; §2 the least-upper-bound property and Dedekind cuts; §3 Archimedean property, density, square roots
> - §4 sequences and limits, limit laws; §5 monotone convergence, nested intervals, Bolzano–Weierstrass, the Cauchy criterion
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - the Newton iteration for $\sqrt2$ compared with a slower rational iteration; $H_n$ versus $\sum1/k^2$ as a Cauchy test; $\sqrt{2+\sqrt{2+\cdots}}=2$ (`scripts/pa_numbers.py`)

> [!key] After this chapter you can
> - state **completeness** (every non-empty bounded-above set has a least upper bound) and show it **fails in $\mathbb Q$**,
> - derive the **Archimedean property**, **density of $\mathbb Q$** and existence of square roots from completeness,
> - prove a limit with the **$\varepsilon$–$N$** definition and negate it,
> - know and use the chain **monotone convergence ⇒ nested intervals ⇒ Bolzano–Weierstrass ⇒ Cauchy criterion**.

> [!intuition] The one-sentence story
> The rationals have holes ($\sqrt2$ is missing); completeness says the real line has none, so a sequence that *looks like* it is converging (Cauchy) really does converge, and every theorem of calculus rests on that.

## 1. Why $\mathbb Q$ is not enough
<span class="scope-extra-book">extra · book</span> *AI notes ch. 15.1*

> [!derivation] $\{q\in\mathbb Q:q>0,\ q^2<2\}$ has no least upper bound in $\mathbb Q$
> Let $S$ be this set; $1\in S$ and $2$ is an upper bound. Suppose $u\in\mathbb Q$ were a least upper bound ($u\ge1$). Since $u^2\ne2$ (the irrationality of $\sqrt2$, PA01) put $u'=\dfrac{2u+2}{u+2}=u-\dfrac{u^2-2}{u+2}$. Then $u'\in\mathbb Q$ and
> $$u'^2-2=\frac{2(u^2-2)}{(u+2)^2}\qquad(\text{check: }u=\tfrac32,\ u'=\tfrac{10}7,\ u'^2-2=\tfrac2{49}=\tfrac{2\cdot\frac14}{(7/2)^2}).$$
> If $u^2<2$: $u'>u$ and $u'^2<2$, so $u'\in S$ exceeds $u$, contradicting that $u$ is an upper bound. If $u^2>2$: $0<u'<u$ and $u'^2>2$; for $s\in S$, $s^2<2<u'^2$ so $s<u'$; thus $u'$ is a smaller upper bound, contradicting leastness. Hence no rational is the least upper bound: **the set has a "hole" at $\sqrt2$.**

The rationals $1,\tfrac32,\tfrac{17}{12},\tfrac{577}{408},\tfrac{665857}{470832},\dots$ ($x\mapsto\frac12(x+\frac2x)$) get arbitrarily close to each other (they are **Cauchy**) but have no limit in $\mathbb Q$ (Figure PA6.1 A): their errors $|x_n-\sqrt2|$ are $4.1\times10^{-1},\,8.6\times10^{-2},\,2.5\times10^{-3},\,2.1\times10^{-6},\,1.6\times10^{-12}$, the error roughly **squaring** each step. The slower rational map $u\mapsto\frac{2u+2}{u+2}$ ($1,\frac43,\frac75,\frac{24}{17},\frac{41}{29},\dots$) gains only a constant factor ($\approx0.17$) per step.

## 2. Completeness and the construction of $\mathbb R$
<span class="scope-extra-book">extra · book</span> *AI notes ch. 15.2*

> [!key] Completeness (least-upper-bound property)
> An ordered field $F$ is **complete** if every non-empty subset $S\subseteq F$ that is bounded above has a **least upper bound** $\sup S$ in $F$ (the lub of PA03). $\mathbb R$ is *the* complete ordered field: any two complete ordered fields are isomorphic by a unique order- and field-isomorphism. Similarly every non-empty set bounded below has an infimum.

> [!key] Dedekind cuts (the construction)
> A **cut** is a set $\alpha\subseteq\mathbb Q$ with (i) $\varnothing\ne\alpha\ne\mathbb Q$; (ii) $p\in\alpha,\ q<p\Rightarrow q\in\alpha$; (iii) $\alpha$ has no greatest element. Let $\mathbb R$ be the set of cuts ordered by $\alpha<\beta\iff\alpha\subsetneq\beta$. The rational $q$ is the cut $q^*=\{p:p<q\}$; $\sqrt2$ is the cut $\{p\in\mathbb Q:p\le0\ \text{or}\ p^2<2\}$, which is not of the form $q^*$: it fills the hole of §1.
> **Completeness of cuts:** if $S$ is a non-empty set of cuts bounded above by a cut $\gamma$, then $\sigma=\bigcup S$ is a cut (it contains each member, is $\subseteq\gamma\ne\mathbb Q$, is closed downward and has no greatest element) and is the least upper bound: any upper bound contains every member of $S$, hence contains $\sigma$. Addition is $\alpha+\beta=\{r+s\}$, zero is $0^*$; multiplication and the field axioms are routine but long (Rudin, Appendix to Ch. 1).

## 3. First consequences of completeness
<span class="scope-extra-book">extra · book</span> *AI notes ch. 15.3*

> [!key] Archimedean property
> $\mathbb N$ is **not bounded above** in $\mathbb R$; equivalently for $x,y>0$ there is $n$ with $nx>y$.
> *Proof.* If $\mathbb N$ were bounded above, $s=\sup\mathbb N$ exists; $s-1$ is not an upper bound, so some $n>s-1$, and $n+1>s$ with $n+1\in\mathbb N$: contradiction.

> [!key] Density of $\mathbb Q$
> For $x>0$ there is $n$ with $\frac1n<x$; and between any two reals $x<y$ there is a rational. *Proof.* Choose $n$ with $n(y-x)>1$, let $m$ be the least integer with $m>nx$ (well-ordering); then $m-1\le nx<m\le nx+1<ny$, so $x<\frac mn<y$. Likewise there is an irrational between any two reals (add $\sqrt2/N$ to a rational).

> [!derivation] Square roots exist
> For $a>0$ let $S=\{t>0:t^2<a\}$. $S\ne\varnothing$ ($t=\frac a{1+a}<1$ and $t^2<t<a$) and is bounded above by $1+a$. Put $s=\sup S$. If $s^2<a$, then for $h=\min\{1,\frac{a-s^2}{2(2s+1)}\}$ we get $(s+h)^2\le s^2+h(2s+1)<a$, so $s+h\in S$, contradicting that $s$ is an upper bound. If $s^2>a$, take $h=\frac{s^2-a}{2s}$; then $t=s-h>0$ and $t^2>s^2-2sh=a$, so $t$ is a smaller upper bound. Hence $s^2=a$; uniqueness: $x^2=y^2$ with $x,y>0$ gives $(x-y)(x+y)=0$. This is the missing step in PA04 Assignment 6 Q5 (surjectivity of $x\mapsto x^2$ on $\mathbb R_{\ge0}$).

> [!key] Absolute value and the triangle inequality
> $|x|=x$ ($x\ge0$), $-x$ ($x<0$). (a) $|x|=0\iff x=0$; (b) $|xy|=|x||y|$; (c) $|x|<r\iff-r<x<r$; (d) $|x+y|\le|x|+|y|$; (e) $\big||x|-|y|\big|\le|x-y|$. (d): from $-|x|\le x\le|x|$ and the same for $y$, $-(|x|+|y|)\le x+y\le|x|+|y|$.

> [!example] Decimals revisited (as used in Lecture 19)
> $0.999\dots=\sup\{0.9,0.99,0.999,\dots\}=1$: the partial sums $1-10^{-n}$ increase and for any $\varepsilon>0$ some $n$ has $10^{-n}<\varepsilon$ (Archimedean), so $1$ is the least upper bound. Hence $0.4999\dots=0.5$ and a real has at most two decimal expansions (one if normalised).

## 4. Sequences and limits
<span class="scope-extra-book">extra · book</span> *AI notes ch. 16.1*

A **sequence** in $X$ is a function $\mathbb N\to X$, $n\mapsto x_n$ (a definition by recursion is a sequence, PA05). A **subsequence** is $(x_{n_k})$ with $n_1<n_2<\cdots$.

> [!key] The $\varepsilon$–$N$ definition
> $x_n\to L$ iff $\ \forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\ge N:\ |x_n-L|<\varepsilon$.
> **Negation (PA01):** $x_n\not\to L$ iff $\exists\varepsilon>0\ \forall N\ \exists n\ge N:\ |x_n-L|\ge\varepsilon$. A sequence **diverges** if it converges to no $L$. It is **bounded** if $\exists M\,\forall n\,|x_n|\le M$ and **Cauchy** if $\forall\varepsilon>0\,\exists N\,\forall m,n\ge N:\ |x_m-x_n|<\varepsilon$.

> [!example] A limit from the definition
> $x_n=\frac{3n+1}{n+2}\to3$: $\big|\frac{3n+1}{n+2}-3\big|=\frac5{n+2}<\varepsilon\iff n>\frac5\varepsilon-2$. Take $N>\frac5\varepsilon$. E.g. $\varepsilon=10^{-3}$ needs $n>4998$ (indeed $x_{10^6}=2.999995$). And $(-1)^n$ diverges: for any candidate $L$ take $\varepsilon=\tfrac12$; the terms $\pm1$ cannot both be within $\tfrac12$ of $L$.

> [!key] Limit laws
> If $x_n\to a$ and $y_n\to b$: (a) limits are **unique**; (b) $(x_n)$ is **bounded**; (c) $x_n+y_n\to a+b$, $x_ny_n\to ab$; (d) $x_n\le y_n\ \forall n\Rightarrow a\le b$; (e) **squeeze**: $x_n\le z_n\le y_n$ and $a=b$ give $z_n\to a$.
> *Proofs.* (a) $|a-a'|\le|a-x_n|+|x_n-a'|<\varepsilon$ for large $n$, for every $\varepsilon$. (b) With $\varepsilon=1$, $|x_n|<|a|+1$ for $n\ge N$; take $M=\max(|x_1|,\dots,|x_N|,|a|+1)$. (c) For the product $|x_ny_n-ab|\le|x_n||y_n-b|+|b||x_n-a|\le M|y_n-b|+|b||x_n-a|$.

## 5. The completeness theorems
<span class="scope-extra-book">extra · book</span> *AI notes ch. 16.2*

> [!key] The chain of theorems (each follows from the previous one)
> 1. **Monotone convergence:** a bounded increasing sequence converges to its supremum (a bounded decreasing one to its infimum). *Proof:* $s=\sup\{x_n\}$ exists; for $\varepsilon>0$ some $x_N>s-\varepsilon$ and for $n\ge N$, $s-\varepsilon<x_N\le x_n\le s$.
> 2. **Nested intervals:** $[a_1,b_1]\supseteq[a_2,b_2]\supseteq\cdots$ (with $a_n\le b_n$) have $\bigcap[a_n,b_n]\ne\varnothing$. *Proof:* $a_n\le b_m$ for all $m,n$; $\sup a_n$ lies in every interval.
> 3. **Monotone subsequence lemma:** every real sequence has a monotone subsequence. *Proof:* call $m$ a *peak* if $x_m\ge x_n\ \forall n>m$. Infinitely many peaks give a decreasing subsequence; finitely many leave a point beyond which every index has a later, larger term: an increasing subsequence.
> 4. **Bolzano–Weierstrass:** every bounded real sequence has a convergent subsequence (monotone subsequence + monotone convergence).
> 5. **Cauchy criterion:** a real sequence converges iff it is Cauchy. *Proof of ⇐:* a Cauchy sequence is bounded; by B–W some $x_{n_k}\to L$; given $\varepsilon$, choose $N$ with $|x_m-x_n|<\varepsilon/2$ for $m,n\ge N$ and $k$ with $n_k\ge N$, $|x_{n_k}-L|<\varepsilon/2$, then $|x_n-L|<\varepsilon$.

![[fig_pa06_reals.png]]
*Figure PA6.1. A: errors of two rational sequences converging to $\sqrt2$ (the Newton iteration squares its error; the other gains a constant factor); both are Cauchy in $\mathbb Q$ but have no limit there. B: bisection gives nested intervals $[a_n,b_n]$ of width $2^{-n}$ shrinking to $\sqrt2$. C: $H_n=\sum1/k$ grows like $\ln n+\gamma$ ($H_{2000}=8.18$) while $\sum1/k^2\to\pi^2/6$.*

> [!example] Applications
> - **Monotone convergence:** $a_1=1$, $a_{n+1}=\sqrt{2+a_n}$ is increasing and bounded by 2; the limit $L$ solves $L=\sqrt{2+L}$, so $L=2$. Numerically $a_2,\dots,a_6=1.732,\,1.932,\,1.983,\,1.996,\,1.999$. Also $(1+\frac1n)^n$ increases and is bounded by 3: $2,2.25,2.488,2.594,2.705,2.718\to e$.
> - **Cauchy test:** $H_{2n}-H_n\ge\tfrac12$ for every $n$ (checked), so $(H_n)$ is **not Cauchy** and diverges; $\sum1/k^2$ has tail $<\frac1{100}$ after 100 terms, so it is Cauchy and converges.
> - **Bolzano–Weierstrass:** $x_n=(-1)^n(1+\frac1n)$ is bounded; its subsequences along even and odd $n$ converge to $+1$ and $-1$. $\sin n$ has subsequences converging to every point of $[-1,1]$ (the values over $n\le2\times10^5$ already fill $[-1,1]$ to five places).
> - **Nested intervals and uncountability:** if $x_1,x_2,\dots$ is any list of reals, choose $I_n\subset I_{n-1}$ (thirds of the previous interval) avoiding $x_n$; the real in $\bigcap I_n$ is not in the list. A second proof that $\mathbb R$ is uncountable ([[PA04 Functions and Cardinality]]).

> [!pitfall] The intervals must be **closed**
> $\bigcap_{n}[0,\tfrac1n]=\{0\}$ but $\bigcap_n(0,\tfrac1n)=\varnothing$ (nested open intervals can shrink to nothing). Completeness (via sup) delivers a point only in the closed case; this is the seed of **compactness** ([[PA07 Metric and Topological Spaces]]).

> [!note] The equivalences
> Each of least-upper-bound, monotone convergence (with Archimedean), nested intervals (with Archimedean) and Cauchy completeness (with Archimedean) characterises $\mathbb R$ among Archimedean ordered fields. $\mathbb Q$ satisfies none of them ($1,1.4,1.41,\dots$ is Cauchy without a limit). Without the Archimedean property some are strictly weaker.

## Map of this chapter
> [!connection] How PA06 connects
> **Builds on:** [[PA05 Induction and the Number Systems]] (the Archimedean property rests on induction; sequences are recursion), [[PA03 Relations Equivalence and Order]] (sup/inf = lub/glb) and [[PA04 Functions and Cardinality]] (decimal expansions, uncountability).
> **Leads to:** [[PA07 Metric and Topological Spaces]] (limits and Cauchy sequences in metric spaces; $[a,b]$ compact; the intermediate value theorem).
> **Concepts:** [[Least Upper Bound Property]] · [[Dedekind Cut]] · [[Archimedean Property]] · [[Sequence and Limit]] · [[Cauchy Sequence]] · [[Monotone Convergence Theorem]] · [[Bolzano-Weierstrass Theorem]] · [[Nested Interval Property]]
> **Other subjects:** [[Proofs, Analysis and Topology - Course Map]], [[Probability - Course Map]] ([[Continuity of Probability]]: $P(\bigcup E_n)=\lim P(E_n)$ is a monotone limit; the law of large numbers and the CLT are statements about limits of sequences, [[PR06 Moments Generating Functions and Limit Theorems]]; a cdf is right-continuous), [[Fixed Points and Linear Stability]] (iterates $x_{n+1}=g(x_n)$ converging to a fixed point are exactly the sequences of §1 and §5; Newton's method), [[Relaxation Time]].

## Summary
> [!summary] Cheat-sheet
> - **Completeness:** non-empty, bounded above ⇒ has a sup. $\mathbb Q$ fails ($\{q:q^2<2\}$; $u'=\frac{2u+2}{u+2}$ with $u'^2-2=\frac{2(u^2-2)}{(u+2)^2}$). $\mathbb R$ = Dedekind cuts.
> - Archimedean ($\mathbb N$ unbounded), density of $\mathbb Q$ and of irrationals, $\sqrt a$ exists, triangle inequality, $0.999\dots=1$.
> - $x_n\to L$: $\forall\varepsilon\,\exists N\,\forall n\ge N\ |x_n-L|<\varepsilon$; negation $\exists\varepsilon\,\forall N\,\exists n\ge N\ |x_n-L|\ge\varepsilon$. Limits unique, convergent ⇒ bounded, sums/products, squeeze.
> - MCT ⇒ nested intervals ⇒ monotone subsequence ⇒ **Bolzano–Weierstrass** ⇒ **Cauchy ⇒ convergent**. Closed intervals only.
> - **Numbers:** Newton rationals for $\sqrt2$: $\frac32,\frac{17}{12},\frac{577}{408}$ (errors $8.6\times10^{-2},2.5\times10^{-3},2.1\times10^{-6}$); $H_{2n}-H_n\ge\frac12$; $\sqrt{2+\sqrt{2+\cdots}}=2$.

## Practice
1. **From the definition.** Prove $\frac{3n+1}{n+2}\to3$ and find $N$ for $\varepsilon=10^{-4}$.
2. **Divergence.** Prove from the definition that $x_n=(-1)^n$ has no limit.
3. **Absolute value.** If $x_n\to a$ prove $|x_n|\to|a|$. Is the converse true?
4. **Sup and inf.** Find $\sup$, $\inf$, $\max$, $\min$ of (a) $\{1-\frac1n:n\in\mathbb N\}$; (b) $\{x\in\mathbb R:x^2<2\}$; (c) $\{(-1)^n(1+\frac1n)\}$; (d) $\{x\in\mathbb Q:x^2<2\}$ in $\mathbb R$ and in $\mathbb Q$.
5. **Archimedean.** Prove $\inf\{\frac1n:n\in\mathbb N\}=0$ and that $\bigcap_n(0,\frac1n)=\varnothing$.
6. **Monotone.** Show $a_1=1$, $a_{n+1}=\sqrt{2+a_n}$ is increasing and bounded by 2, and find its limit.
7. **Cauchy.** Show $(-1)^n$ is not Cauchy and that $x_n=\sum_{k=1}^n2^{-k}$ is.
8. **B–W.** Find the limits of the convergent subsequences of $x_n=\sin(n\pi/2)+\frac1n$.
9. **Why closed.** Give nested non-empty open intervals with empty intersection, and nested non-empty closed **unbounded** sets with empty intersection.
10. **Squeeze.** Prove $\frac{\sin n}n\to0$ and $\sqrt[n]{n}\to1$ (hint for the second: $n^{1/n}=1+d_n$, binomial theorem).

> [!example]- Solutions
> 1. $|x_n-3|=\frac5{n+2}<\varepsilon$ iff $n>\frac5\varepsilon-2$; for $\varepsilon=10^{-4}$ take $N=50{,}000$ ($>49{,}998$).
> 2. Suppose $x_n\to L$ and take $\varepsilon=\frac12$: for large $n$, $|(-1)^n-L|<\frac12$ for both parities, so $|1-(-1)|\le|1-L|+|L+1|<1$, but $2<1$ is false.
> 3. $\big||x_n|-|a|\big|\le|x_n-a|\to0$ (triangle inequality (e)). The converse is false: $x_n=(-1)^n$ has $|x_n|\to1$ but diverges.
> 4. (a) $\sup=1$ (not attained), $\min=\inf=0$ (at $n=1$), no max. (b) $\sup=\sqrt2$, $\inf=-\sqrt2$, no max or min (open). (c) values $-2,1.5,-1.33,\dots$: $\min=-2$ ($n=1$), $\sup=1.5$ ($n=2$) = $\max$; inf $=-2$. (d) In $\mathbb R$: $\sup=\sqrt2$, $\inf=-\sqrt2$; in $\mathbb Q$: **no** sup or inf exists (no rational is the least upper bound, §1).
> 5. $0$ is a lower bound; if $\varepsilon>0$ were a larger lower bound, Archimedean gives $n$ with $\frac1n<\varepsilon$. For the intersection: a positive $x$ eventually has $\frac1n<x$.
> 6. Increasing: $a_1=1<a_2=\sqrt3$; if $a_k<a_{k+1}$ then $\sqrt{2+a_k}<\sqrt{2+a_{k+1}}$. Bounded: $a_1<2$, and $a_k<2\Rightarrow a_{k+1}<\sqrt4=2$. Limit $L$: $L^2=2+L$, $(L-2)(L+1)=0$, $L=2$ (the other root is negative). Numerically $a_8=1.99993$, $a_9=1.99998$.
> 7. $|x_{n+1}-x_n|=2$: not Cauchy. For $m>n$: $|x_m-x_n|=\sum_{k=n+1}^m2^{-k}<2^{-n}<\varepsilon$ once $n>\log_2\frac1\varepsilon$: Cauchy; limit 1.
> 8. $\sin(n\pi/2)$ cycles $1,0,-1,0$ and $\frac1n\to0$: subsequences converge to $1,0,-1$.
> 9. $I_n=(0,\frac1n)$ (shrinks to nothing). Closed unbounded: $F_n=[n,\infty)$: nested, non-empty, $\bigcap F_n=\varnothing$ (Archimedean). Compactness requires closed **and bounded**.
> 10. $|\frac{\sin n}n|\le\frac1n\to0$ (squeeze). For $n^{1/n}=1+d_n$ with $d_n\ge0$ ($n\ge1$): $n=(1+d_n)^n\ge\binom n2d_n^2$ so $d_n^2\le\frac2{n-1}\to0$; thus $d_n\to0$.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | decimal expansions as series, $0.4999\dots=0.5$, "$\mathbb R$ is complete" | [[Countable-Uncountable-sets.pdf#page=4\|Lecture 19]] | taught (used) |
> | completeness, cuts, Archimedean, density, square roots, absolute value, sequences, completeness theorems | AI notes `proofs-prems-topo.pdf` ch. 15–16 (proofs read and rechecked) | extra/book |
> | Rudin, Ch. 1–3; Kumaresan et al. | textbooks | extra/book |
> | numerical iterations, $H_n$, $\sqrt{2+\cdots}$ | `scripts/pa_numbers.py`, `fig_pa06_reals.py` | extra/beyond |
>
> **Notes.** The AI notes' proof that $\bigcap I_n\ne\varnothing$ for the uncountability of $\mathbb R$ is the one reproduced above (split into thirds). Proofs of §§3–5 were read and rechecked; the long verification of the field axioms for cuts is not reproduced (it is routine; see Rudin).

**References.** Rudin, W. *Principles of Mathematical Analysis*, Ch. 1–3 · Kumaresan et al., *A Foundation Course in Mathematics* · Dedekind, R. (1872) *Stetigkeit und irrationale Zahlen* · Abbott, S. *Understanding Analysis*.
