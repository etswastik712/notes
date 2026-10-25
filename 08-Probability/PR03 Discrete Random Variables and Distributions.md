---
title: PR03 Discrete Random Variables and Distributions
aliases: [PR03, discrete random variables, pmf, cdf, expectation, binomial, Poisson, geometric, hypergeometric, MT2113 classes 20 Aug-2 Sep]
subject: probability
type: chapter
chapter: 3
part: II
scope: [taught, extra-book, extra-beyond]
by: [lecture-notes]
status: draft
prereq: [PR01 Counting and the Axioms of Probability, PR02 Conditional Probability Bayes Rule and Independence]
tags: [subject/probability, type/chapter, taught, extra/book, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# PR03 · Discrete Random Variables and Distributions

◀ [[PR02 Conditional Probability Bayes Rule and Independence]] · [[PR04 Joint Distributions Expectation and Variance]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**: [[ilovepdf_merged-1.pdf#page=17|class notes of 20 Aug]] (pp.17–19), [[ilovepdf_merged-1.pdf#page=20|27 Aug]] (pp.20–22), the first part of [[ilovepdf_merged-1.pdf#page=23|2 Sep]] (pp.23–26: the geometric and negative-binomial constructions) and the sheets of [[Practice problems 28th August and following weekend.pdf|28 Aug]] and [[Practice problems 4th September 2026.pdf|4 Sep]].
> - §1 random variables, indicator variables, pmf, cdf and its properties
> - §2 expectation, the formula $E[g(X)]=\sum g(x)p(x)$, linearity $E[aX+b]=aE[X]+b$
> - §3 Bernoulli, binomial, discrete uniform, hypergeometric
> - §4 geometric, negative binomial
> - §5 Poisson as a limit of Binomial$(n,c/n)$
>
> 🟡 **Extra · book**
> - §3–§5 the hypergeometric mean by indicators, the name "negative binomial" (series of $(1-q)^{-m}$), the Poisson as a model for rare events; first-step analysis for the geometric mean (Blitzstein and Hwang)
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §5 an error bound for the Poisson limit (total variation $\approx c^2/(2n)$), checked numerically; the distribution-family diagram; the coupon-collector law via inclusion-exclusion; all numbers recomputed (`scripts/pr_numbers.py`)

> [!key] After this chapter you can
> - define a **random variable**, its **pmf** and **cdf**, and recover one from the other, including from a step-function cdf,
> - compute $E[X]$ and $E[g(X)]$ without finding the pmf of $g(X)$, and use $E[aX+b]=aE[X]+b$,
> - **recognise** which named distribution a story gives (Bernoulli, binomial, hypergeometric, uniform, geometric, negative binomial, Poisson), write its pmf and its mean,
> - derive the **Poisson** pmf as the limit of Binomial$(n,c/n)$.

> [!intuition] The one-sentence story
> A random variable is a number attached to the outcome; its pmf is the table of probabilities of that number, and each named distribution is the answer to one counting question (how many successes? how many trials until a success? how many white balls without replacement?).

![[PR03 The Discrete Distribution Family.svg]]
*Figure PR3.0. The discrete family and how its members are related (SVG; an editable Excalidraw copy is in `Assets/excalidraw/`).*

## 1. Random variables, pmf and cdf
<span class="scope-taught">taught</span> *20 Aug ([[ilovepdf_merged-1.pdf#page=17|pp.17–19]])*

A **random variable** (rv) is a real-valued function of the outcome of a random experiment: when $n$ dice are rolled we may care only about the sum, not the whole outcome. A **discrete** rv takes at most countably many values $x_1,x_2,\dots$. Its **probability mass function**
$$p(x)=P[X=x]\quad(x\in\mathbb R),\qquad p(x_i)>0,\quad\sum_ip(x_i)=1 .$$
The **cumulative distribution function** (cdf), defined for **every** random variable, is
$$F(a)=P[X\le a]=\sum_{x\le a}p(x).$$
For a discrete rv it is a **step function** with a jump of height $p(x_i)$ at $x_i$.

> [!key] Properties of every cdf
> 1. **Increasing:** $x_1\le x_2\Rightarrow F(x_1)\le F(x_2)$ (the event $\{X\le x_1\}\subset\{X\le x_2\}$).
> 2. **Right-continuous:** $F(a)=\lim_{x\downarrow a}F(x)$. (Proof, not examinable: the events $\{X\le x_n\}$ decrease to $\{X\le a\}$ when $x_n\downarrow a$, and probability is continuous along decreasing sequences, PR01 §5.)
> 3. $\lim_{x\to\infty}F(x)=1$, $\lim_{x\to-\infty}F(x)=0$.
> Also $P[X=a]=F(a)-F(a^-)$, the jump at $a$; $P[a<X\le b]=F(b)-F(a)$.

> [!example] pmf from a step cdf (28 Aug sheet, problem 7)
> $F(x)=0\ (x<0)$, $\tfrac12\ (0\le x<1)$, $\tfrac35\ (1\le x<2)$, $\tfrac45\ (2\le x<3)$, $\tfrac9{10}\ (3\le x<3.5)$, $1\ (x\ge3.5)$. The jumps give $p(0)=\tfrac12$, $p(1)=\tfrac1{10}$, $p(2)=\tfrac15$, $p(3)=\tfrac1{10}$, $p(3.5)=\tfrac1{10}$ (sum $=1$), and
> $E[X]=0\cdot\tfrac12+1\cdot\tfrac1{10}+2\cdot\tfrac15+3\cdot\tfrac1{10}+3.5\cdot\tfrac1{10}=1.15$.

> [!example] Two dice, sum (20 Aug)
> Let $X_1,X_2$ be the two faces and $S=X_1+X_2$. $X_1$ and $X_2$ have the **same distribution** (uniform on $\{1,\dots,6\}$) but are **not equal** as random variables (they are different functions on the 36-point space). The pmf of $S$ is $p(s)=\tfrac{6-|s-7|}{36}$ for $s=2,\dots,12$ (Figure PR4.1 B in the next chapter), $E[S]=7$.

> [!definition] Indicator random variable (2 Sep)
> For an event $A$, $\mathbf 1_A=1$ if $A$ occurs and $0$ otherwise. It is Bernoulli$(P[A])$, and $E[\mathbf 1_A]=P[A]$. Counting successes is adding indicators: $X=\sum_i\mathbf 1_{A_i}$.

## 2. Expectation
<span class="scope-taught">taught</span> *20 and 27 Aug ([[ilovepdf_merged-1.pdf#page=19|p.19]], [[ilovepdf_merged-1.pdf#page=21|pp.21–22]])*

> [!key] Expectation of a discrete rv
> $$E[X]=\sum_{x:\,p(x)>0}x\,p(x)=\sum_ix_ip(x_i),$$
> the probability-weighted average of the values (assuming the sum converges absolutely). If the pmf is read as a frequency distribution, this is the usual mean.

> [!example] The buses (27 Aug)
> 120 students go on three buses holding 36, 40 and 44. One **student** is picked at random and $X$ is the size of their bus: $E[X]=\tfrac{36}{120}36+\tfrac{40}{120}40+\tfrac{44}{120}44=\tfrac{36^2+40^2+44^2}{120}=40.27$, which exceeds the plain average of the three bus sizes ($40$): a random student is more likely to be on a big bus (**size-biased sampling**).

> [!key] Expectation of a function (LOTUS for discrete $X$, 27 Aug)
> If $Y=g(X)$ then $\displaystyle E[g(X)]=\sum_ig(x_i)\,p(x_i)$; no pmf of $Y$ is needed. In particular (**linearity**) $E[aX+b]=aE[X]+b$.
>
> *Proof outline.* Let $Y$ take values $y_1,y_2,\dots$ and put $S_j=\{x_i:g(x_i)=y_j\}$; the $S_j$ partition the values of $X$ and $\{Y=y_j\}=\{X\in S_j\}$, so $P[Y=y_j]=\sum_{x_i\in S_j}p(x_i)$. Then $\sum_ig(x_i)p(x_i)=\sum_j\sum_{x_i\in S_j}y_jp(x_i)=\sum_jy_jP[Y=y_j]=E[Y]$. (The class notes say the proof is not examined, but the formula is.)

> [!pitfall] $E[g(X)]\ne g(E[X])$ in general
> For $X$ uniform on $\{1,\dots,6\}$: $E[X^2]=\tfrac{91}6=15.17$ while $(E[X])^2=12.25$. The two coincide only for linear $g$.

## 3. Bernoulli, binomial, uniform, hypergeometric
<span class="scope-taught">taught</span> *20 and 27 Aug ([[ilovepdf_merged-1.pdf#page=19|pp.19–22]])*

> [!key] The binomial
> Toss a coin $n$ times, independently, with $P[\text{head}]=p$; $X$ = number of heads. Then
> $$p(k)=\binom nkp^k(1-p)^{n-k},\ k=0,\dots,n;\qquad E[X]=np .$$
> For $n=1$ this is **Bernoulli**$(p)$. With indicators $X=\sum_{i=1}^nX_i$ where the $X_i$ are independent Bernoulli$(p)$.

*Why the pmf is this:* a particular sequence with $k$ heads has probability $p^k(1-p)^{n-k}$ (independence), and there are $\binom nk$ such sequences (PR01).

> [!derivation] Two proofs that $E[X]=np$
> **(a) By the binomial theorem** (class notes, last page). Differentiate $(x+y)^n=\sum_r\binom nrx^ry^{n-r}$ in $x$ and multiply by $x$: $nx(x+y)^{n-1}=\sum_rr\binom nrx^ry^{n-r}$. Set $x=p$, $y=1-p$ so that $x+y=1$: $np=\sum_rr\binom nrp^r(1-p)^{n-r}=E[X]$.
> **(b) By linearity** (2 Sep, no independence needed for the mean): $E[X]=\sum_iE[X_i]=n\,p$, since $E[X_i]=1\cdot p+0\cdot(1-p)=p$.

> [!example] Two coins with different biases (28 Aug sheet, problem 6)
> Heads probabilities $0.6$ and $0.7$, independent; $X$ = total heads. $P[X=0]=0.4\cdot0.3=0.12$, $P[X=1]=0.6\cdot0.3+0.4\cdot0.7=0.46$, $P[X=2]=0.42$, and $E[X]=0.6+0.7=1.3$. It is **not** binomial (the probabilities differ), yet linearity still gives the mean.

> [!key] Discrete uniform
> On a finite set $\Omega$: $P[X=x]=1/|\Omega|$. For $\{1,\dots,n\}$, $E[X]=\tfrac{n+1}2$. Example: the **maximum** of 5 slips drawn from 100 has $E[X]=5\cdot101/6=84.17$ (🔵).

> [!key] The hypergeometric
> An urn has $w$ white and $b$ black balls; draw $n$ without replacement; $X$ = number of white balls:
> $$p(k)=\frac{\binom wk\binom b{n-k}}{\binom{w+b}n},\qquad E[X]=\frac{nw}{w+b} .$$
> **Sampling with replacement** gives Binomial$(n,\tfrac w{w+b})$; without replacement, the draws are no longer independent but are **exchangeable** (PR02 §3), so each draw is white with the same probability $\tfrac w{w+b}$ and linearity gives the same mean.

> [!example] With vs without replacement (28 Aug sheet, problem 1)
> 100 slips numbered 1–100, five drawn. $X$ = number of slips $\ge80$ (21 of the 100). With replacement $X\sim$ Bin$(5,0.21)$: $P[X=0]=0.79^5=0.3077$. Without replacement: $P[Y=0]=\binom{79}{5}/\binom{100}5=0.2994$; the hypergeometric pmf is a little tighter around its mean. Probability that **100** appears at least once: $1-0.99^5=0.04901$ (with replacement) against exactly $\tfrac5{100}=0.05$ (without).

![[fig_pr03_distributions.png]]
*Figure PR3.1. A: the hypergeometric (25 balls, 10 white, 5 drawn) and the binomial with the same mean, $5\cdot\tfrac25=2$; the hypergeometric is the narrower. B: Geometric$(0.25)$ and negative binomial$(3,0.4)$ by number of trials. C: the total-variation distance between Binomial$(n,3.2/n)$ and Poisson$(3.2)$ falls like $1/n$.*

## 4. Waiting times: geometric and negative binomial
<span class="scope-taught">taught</span> *27 Aug and 2 Sep ([[ilovepdf_merged-1.pdf#page=22|pp.22]], [[ilovepdf_merged-1.pdf#page=25|pp.25–26]], [[ilovepdf_merged-1.pdf#page=31|p.31]])*

> [!key] Geometric$(p)$
> Independent trials with success probability $p$; $X$ = **number of trials up to and including the first success**:
> $$P[X=n]=(1-p)^{n-1}p,\ n=1,2,\dots;\qquad E[X]=\frac1p .$$
> Check of normalisation: $\sum_{n\ge1}q^{n-1}p=p/(1-q)=1$ (with $q=1-p$).

> [!verify] Trials here, failures in the Week 2–3 lectures
> The post-midterm handwritten notes ([[Week2_notes.pdf#page=2|Week 2]], [[Week3_notes.pdf#page=5|Week 3]]) define $\mathrm{Geom}(p)$ by $P[X=k]=q^kp$, $k=0,1,2,\dots$ (**failures** before the first success; mean $q/p$, variance $q/p^2$, MGF $\frac p{1-qe^t}$; Homework 3 Q5 asks for exactly $q/p$ and $q/p^2$). The class notes of 2 Sep, followed above, count **trials** (mean $1/p$). The two are related by $X_{\rm trials}=1+X_{\rm fail}$. Check the support in each problem. See [[PR06 Moments Generating Functions and Limit Theorems]] §3.2.

> [!derivation] $E[X]=1/p$, two ways
> *Series:* $E[X]=\sum_{n\ge1}n\,q^{n-1}p=p\,\dfrac{d}{dq}\sum_{n\ge0}q^n=p\,\dfrac1{(1-q)^2}=\dfrac1p$.
> *First step* 🟡 (conditioning, PR02): with probability $p$ the first trial succeeds ($X=1$); otherwise one trial is spent and the process restarts: $E[X]=p\cdot1+q(1+E[X])\Rightarrow E[X]=1/p$.

> [!example] Truncated geometric (27 Aug)
> A coin ($P[H]=p$) is flipped until a head occurs or $n$ flips are made; $X$ = number of flips. $P[X=k]=q^{k-1}p$ for $k<n$ and $P[X=n]=q^{n-1}$. For $p=0.3$, $n=5$: $0.3,\ 0.21,\ 0.147,\ 0.1029,\ 0.2401$ (sum $=1$), $E[X]=\tfrac{1-q^n}p=2.773$.

> [!key] Negative binomial$(k,p)$ (class convention)
> $Y$ = number of trials needed to obtain the **$k$-th success**. Write $Y=X_1+\dots+X_k$ with $X_i$ independent Geometric$(p)$ (the wait for the $i$-th success after the $(i-1)$-th). Then
> $$P[Y=n]=\binom{n-1}{k-1}p^k(1-p)^{n-k},\ n=k,k+1,\dots;\qquad E[Y]=\frac kp .$$
> *Why this pmf:* the $k$-th success is at trial $n$ exactly when trial $n$ is a success and the previous $n-1$ trials contain $k-1$ successes.

> [!example] Numbers
> $k=3$, $p=0.4$: $P[Y=3]=0.064$, $P[Y=4]=0.1152$, $P[Y=5]=0.1382$; $E[Y]=7.5$. For Geometric$(0.25)$, $E[X]=4$.

> [!note] Where the name comes from (class notes, last pages)
> Let $f=n-k$ be the number of **failures**. Then $P=\binom{f+k-1}{f}p^k q^f$, and $\binom{f+k-1}f=(-1)^f\binom{-k}f$ is the coefficient of $q^f$ in $(1-q)^{-k}$ (generalised binomial theorem), so $\sum_fP=p^k(1-q)^{-k}=1$. The pmf is "binomial with a negative exponent". The same distribution is often defined by the number of failures $f$ rather than trials $n$; the class notes use trials.

## 5. The Poisson distribution
<span class="scope-taught">taught</span> *27 Aug ([[ilovepdf_merged-1.pdf#page=21|p.21]], [[ilovepdf_merged-1.pdf#page=22|p.22]]); 28 Aug sheet, problem 8*

> [!key] Poisson$(\lambda)$
> $$P[X=n]=e^{-\lambda}\frac{\lambda^n}{n!},\ n=0,1,2,\dots;\qquad E[X]=\lambda .$$
> The normalising constant: if $p(i)=c\lambda^i/i!$ then $1=c\sum\lambda^i/i!=ce^{\lambda}$, so $c=e^{-\lambda}$ (class problem, 27 Aug). For $\lambda=2$: $P[X=0]=e^{-2}=0.1353$ and $P[X>2]=1-e^{-2}(1+2+2)=0.3233$.

> [!derivation] Poisson as the limit of Binomial$(n,c/n)$ (27 Aug; derived in class)
> Fix $k$ and let $n\to\infty$:
> $$\binom nk\Big(\frac cn\Big)^k\Big(1-\frac cn\Big)^{n-k}=\frac{c^k}{k!}\cdot\underbrace{\frac{n(n-1)\cdots(n-k+1)}{n^k}}_{\to1}\cdot\underbrace{\Big(1-\frac cn\Big)^{n}}_{\to e^{-c}}\cdot\underbrace{\Big(1-\frac cn\Big)^{-k}}_{\to1}\ \longrightarrow\ e^{-c}\frac{c^k}{k!}.$$
> So $\text{Poisson}(c)$ is the law of the number of **rare events** (many chances $n$, each of tiny probability $c/n$).
> *Mean:* $E[X]=\sum_{n\ge1}n\,e^{-\lambda}\dfrac{\lambda^n}{n!}=\lambda e^{-\lambda}\sum_{n\ge1}\dfrac{\lambda^{n-1}}{(n-1)!}=\lambda$.

> [!example] How good is the approximation? (🔵)
> $P[X\le2]$ for Poisson$(3.2)$ is $0.3799$; for Binomial$(100,0.032)$ it is $0.3758$ and for Binomial$(1000,0.0032)$ it is $0.3795$. The total-variation distance between Binomial$(n,3.2/n)$ and Poisson$(3.2)$ is $0.0080$ at $n=100$, $0.00079$ at $n=1000$ and $0.00008$ at $n=10{,}000$: it shrinks like $1/n$ (Figure PR3.1 C), consistent with the known bound $\mathrm{TV}\le c^2/n$ for these laws.

> [!pitfall] Poisson mean equals variance
> This is the signature of a Poisson count. Real count data with variance larger than the mean (**over-dispersion**) are not Poisson; see the negative binomial as a mixture ([[Negative Binomial Distribution]]). The variance is derived in [[PR04 Joint Distributions Expectation and Variance]].

> [!example] A coupon-collector pmf by inclusion-exclusion (🔵, 28 Aug sheet, problem 3)
> $N$ coupon types, one drawn at random each time; $T$ = number of draws to collect all types. Let $A_i$ = "type $i$ not seen in the first $n$ draws". Then $\{T>n\}=\bigcup_iA_i$ and, by inclusion-exclusion (PR01), $P[T>n]=\sum_{i=1}^N(-1)^{i+1}\binom Ni\big(1-\tfrac iN\big)^n$, $P[T=n]=P[T>n-1]-P[T>n]$. For $N=3$: $P[T>3]=0.7778$, $P[T=3]=\tfrac6{27}=0.2222$, and summing the tail, $E[T]=\sum_{n\ge0}P[T>n]=5.5=3H_3$ (also $14.7=6H_6$ for $N=6$; derived by linearity in PR04).

## Map of this chapter
> [!connection] How PR03 connects
> **Builds on:** [[PR01 Counting and the Axioms of Probability]] (counting gives binomial and hypergeometric pmfs) and [[PR02 Conditional Probability Bayes Rule and Independence]] (independent trials; first-step conditioning).
> **Leads to:** [[PR04 Joint Distributions Expectation and Variance]] (several random variables, linearity, variance) → [[PR05 Continuous Random Variables]] (replace the pmf by a density).
> **Concepts:** [[Random Variable]] · [[Probability Mass Function]] · [[Cumulative Distribution Function]] · [[Expectation]] · [[Law of the Unconscious Statistician]] · [[Indicator Random Variable]] · [[Bernoulli Distribution]] · [[Binomial Distribution]] · [[Hypergeometric Distribution]] · [[Discrete Uniform Distribution]] · [[Geometric Distribution]] · [[Negative Binomial Distribution]] · [[Poisson Distribution]] · [[Poisson Limit Theorem]] · [[Coupon Collector Problem]]
> **Other subjects:** [[Probability - Course Map]], [[Ecology and Evolution - Course Map]] (counts of individuals, demographic stochasticity; [[EE07 Conservation Biology]]), [[TH06 From Kinetic Theory to Statistical Mechanics]] (Poisson and binomial counts of molecules in a volume), [[QM04 The Particle in a Box]] (discrete outcome probabilities).

## Summary
> [!summary] Cheat-sheet
> | name | counts | pmf | mean |
> |---|---|---|---|
> | Bernoulli$(p)$ | one trial | $p^x(1-p)^{1-x}$ | $p$ |
> | Binomial$(n,p)$ | successes in $n$ trials | $\binom nkp^kq^{n-k}$ | $np$ |
> | Hypergeometric | whites in $n$ draws w/o replacement | $\binom wk\binom b{n-k}/\binom{w+b}n$ | $\frac{nw}{w+b}$ |
> | Uniform$\{1..n\}$ | equally likely | $1/n$ | $\frac{n+1}2$ |
> | Geometric$(p)$ | trials to 1st success | $q^{n-1}p$ | $1/p$ |
> | Neg. binomial$(k,p)$ | trials to $k$-th success | $\binom{n-1}{k-1}p^kq^{n-k}$ | $k/p$ |
> | Poisson$(\lambda)$ | rare events | $e^{-\lambda}\lambda^n/n!$ | $\lambda$ |
>
> - **cdf:** increasing, right-continuous, limits 0 and 1; jump = pmf. $E[g(X)]=\sum g(x)p(x)$; $E[aX+b]=aE[X]+b$; $E[\mathbf 1_A]=P[A]$.
> - **Poisson limit:** Binomial$(n,c/n)\to$ Poisson$(c)$. **Numbers:** step-cdf mean $1.15$; buses $40.27$; $\lambda=2$: $P[X>2]=0.3233$; NegBin$(3,0.4)$ mean $7.5$.

## Practice
1. **Binomial.** A fair die is rolled 8 times; $X$ = number of sixes. Find $P[X=2]$, $P[X\ge1]$ and $E[X]$.
2. **From a cdf.** $F(x)=0\ (x<1)$, $0.2\ (1\le x<2)$, $0.5\ (2\le x<4)$, $1\ (x\ge4)$. Find the pmf, $P[X\ge2]$ and $E[X]$.
3. **LOTUS.** $X$ has pmf $p(-1)=0.3$, $p(0)=0.2$, $p(2)=0.5$. Find $E[X]$, $E[X^2]$ and $E[3X-2]$.
4. **Hypergeometric.** A committee of 4 is chosen at random from 6 men and 4 women. Find the pmf of the number of women and its mean.
5. **Geometric.** A basketball player sinks a free throw with probability $0.7$ (independent). Find the probability that the first success is on the 3rd throw, and the expected number of throws.
6. **Negative binomial.** Using $p=0.7$ as in problem 5, find the probability that the 4th success occurs on the 6th throw and the expected number of throws needed for 4 successes.
7. **Poisson.** Flaws in a roll of cloth occur at an average rate of $\lambda=2$ per roll, Poisson. Find the probability of no flaw, of exactly two, and of more than three.
8. **Poisson limit.** A call centre receives 600 calls a day; each call independently comes from a given client with probability $0.005$. Compare the exact binomial probability with its Poisson approximation for the event that the client makes no call.
9. **A random walk.** A particle takes 6 independent $\pm1$ steps, $+1$ with probability $0.6$. Write the position as $Y=2X-6$ with $X\sim$ Bin$(6,0.6)$ and find $P[Y=2]$ and $E[Y]$.
10. **Proof.** Show that $E[X]=\sum_{n\ge1}P[X\ge n]$ for a rv taking values in $\{0,1,2,\dots\}$, and use it to recover $E[X]=1/p$ for the geometric.

> [!example]- Solutions
> 1. $P[X=2]=\binom82(\tfrac16)^2(\tfrac56)^6=28\cdot\tfrac{15625}{1\,679\,616}=0.2605$; $P[X\ge1]=1-(5/6)^8=0.7674$; $E[X]=8/6=1.333$.
> 2. Jumps: $p(1)=0.2$, $p(2)=0.3$, $p(4)=0.5$. $P[X\ge2]=0.8$. $E[X]=0.2+0.6+2.0=2.8$.
> 3. $E[X]=-0.3+0+1.0=0.7$; $E[X^2]=0.3+0+2.0=2.3$; $E[3X-2]=3(0.7)-2=0.1$.
> 4. Women $W\in\{0,\dots,4\}$: $p(k)=\binom4k\binom6{4-k}/\binom{10}4$ with $\binom{10}4=210$: $p=15,\ 80,\ 90,\ 24,\ 1$ over $210$, i.e. $0.0714,\ 0.381,\ 0.4286,\ 0.1143,\ 0.0048$; $E[W]=4\cdot4/10=1.6$.
> 5. $P[X=3]=0.3^2\cdot0.7=0.063$; $E[X]=1/0.7=1.4286$.
> 6. $P[Y=6]=\binom53(0.7)^4(0.3)^2=10\cdot0.2401\cdot0.09=0.2161$; $E[Y]=4/0.7=5.714$.
> 7. $P[0]=e^{-2}=0.1353$; $P[2]=2e^{-2}=0.2707$; $P[>3]=1-e^{-2}(1+2+2+\tfrac43)=1-0.8571=0.1429$.
> 8. $np=3$. Binomial$(600,0.005)$: $P[0]=0.995^{600}=0.0494$; Poisson$(3)$: $e^{-3}=0.0498$.
> 9. $Y=2$ means $X=4$: $P=\binom64(0.6)^4(0.4)^2=15\cdot0.1296\cdot0.16=0.3110$; $E[Y]=2E[X]-6=2(3.6)-6=1.2$.
> 10. $\sum_{n\ge1}P[X\ge n]=\sum_{n\ge1}\sum_{k\ge n}p(k)=\sum_{k\ge1}p(k)\sum_{n=1}^{k}1=\sum_kkp(k)=E[X]$ (swap the order of summation; all terms are non-negative). For the geometric, $P[X\ge n]=q^{n-1}$, so $E[X]=\sum_{n\ge1}q^{n-1}=\tfrac1{1-q}=\tfrac1p$.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | random variable, pmf, cdf and its properties, expectation, binomial, uniform, hypergeometric | [[ilovepdf_merged-1.pdf#page=17\|class notes 20 Aug, pp.17–19]] | taught |
> | Poisson limit, buses, LOTUS (discrete), linearity $E[aX+b]$, random walk, truncated geometric | [[ilovepdf_merged-1.pdf#page=20\|class notes 27 Aug, pp.20–22]] | taught |
> | indicators, geometric, negative binomial, linearity of expectation | [[ilovepdf_merged-1.pdf#page=23\|class notes 2 Sep, pp.23–26]] | taught |
> | name "negative binomial"; mean of the binomial from the binomial theorem | [[ilovepdf_merged-1.pdf#page=31\|class notes p.31–32]] | taught |
> | slips, winnings, coupons, hypergeometric mean, two coins, step cdf, Poisson mean | [[Practice problems 28th August and following weekend.pdf\|sheet 28 Aug]] | taught |
> | first-step analysis; Poisson total-variation check; coupon collector pmf | Blitzstein and Hwang Ch. 4 (not opened); `scripts/pr_numbers.py` | extra/book, beyond |
>
> **Notes.** The class convention is that the negative binomial counts **trials**; many books (and `scipy.stats.nbinom`) count failures, so the pmf and mean differ by a shift of $k$. Transformations of random variables were moved by the instructor to after joint distributions ([[PR04 Joint Distributions Expectation and Variance]]).

> [!verify] Negative binomial convention
> Class notes: trials to the $k$-th success, $P[Y=n]=\binom{n-1}{k-1}p^kq^{n-k}$, mean $k/p$. Most software: failures before the $k$-th success, mean $k(1-p)/p$. Check which one an exam question means.

**References.** Blitzstein, J. K. and Hwang, J. *Introduction to Probability*, Ch. 3–4 · Ross, S. *A First Course in Probability* (8th ed.), Ch. 4 · Le Cam, L. (1960) *An approximation theorem for the Poisson binomial distribution* (the $1/n$ bound).
