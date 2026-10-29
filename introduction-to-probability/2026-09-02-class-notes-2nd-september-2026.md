---
id: introduction-to-probability/2026-09-02-class-notes-2nd-september-2026
aliases: [Class notes 2 Sep 2026]
tags: [probability, mt2113, class-notes]
trust_tier: agent_written
---

# Class notes 2nd September 2026

## Covered
The instructor moves the discussion of transformations of random variables to after joint distributions (Classroom: Class notes 2nd September 2026.pdf).

**Joint pmf.** All random variables considered together must be defined on the same sample space, even if they come from different random experiments. For real $X_1,X_2$ one considers $\{X_1\le x_1,X_2\le x_2\}=\{X_1\le x_1\}\cap\{X_2\le x_2\}$. For discrete $X_1$ (values $a_1,a_2,\dots$) and $X_2$ (values $b_1,b_2,\dots$), each at most countable, the joint pmf is
$$p(a_i,b_j)=P[X_1=a_i,X_2=b_j]=P\big(\{X_1=a_i\}\cap\{X_2=b_j\}\big)\quad\text{for all } i,j.$$

**Example: two distinguishable fair dice.** $X_1$ = sum (values $2,\dots,12$), $X_2$ = maximum (values $1,\dots,6$). Always $X_1>X_2$ (sum exceeds max), so only pairs $a_1>a_2$ matter. For instance $P[X_1=7,X_2=5]=P[\{(2,5),(5,2)\}]=\tfrac{2}{36}=\tfrac1{18}$, using 36 equally likely outcomes. Practice problem set by the instructor: $X_1$ = sum, $X_2$ = absolute difference of the two faces; analyse the joint distribution.

**Independence of random variables.** $X_1,X_2$ are independent if
$$P[X_1\le x_1,X_2\le x_2]=P[X_1\le x_1]\,P[X_2\le x_2]\quad\text{for all }x_1,x_2\in\mathbb R.$$
For discrete variables this is equivalent to $P[X_1=a_i,X_2=b_j]=P[X_1=a_i]P[X_2=b_j]$ for all $i,j$. It extends to any finite collection in the same way as for events. Exercise: check that the sum and the max of the dice example fail or hold as the definition requires (the notes say "check that $X_1$ and $X_2$ in the previous example are indeed independent", referring to the two-coin-toss indicators $X_i=1$ if toss $i$ is a head, $0$ otherwise).

**Sum of independent Bernoulli variables.** If $X_1,\dots,X_n$ are independent with $X_i=1$ w.p. $p$ and $0$ w.p. $1-p$, then $\sum_i X_i$ has the $\text{Binomial}(n,p)$ pmf (intuition given in class).

**Indicator random variable.** For an event $A$, $X=\mathbf 1_A$ equals $1$ when $A$ happens and $0$ otherwise. With $A_i$ = "trial $i$ succeeds" (trials independent, success probability $p$), $\sum_i\mathbf 1_{A_i}$ counts the successes in $n$ trials.

**Negative binomial.** $X$ = number of tosses until the first head is $\text{Geometric}(p)$ (to be derived in class). For a fixed positive integer $k$, let $Y$ be the number of tosses until the $k$-th head. Then $Y=X_1+\dots+X_k$, where $X_i$ is the number of tosses after the $(i-1)$-st head up to and including the $i$-th head. These are independent and each is $\text{Geometric}(p)$. $Y$ has the $\text{Negative Binomial}(k,p)$ distribution. (The notes spell it "Geometrci"; typo in the source.)

**Linearity of expectation.** For any two random variables $X_1,X_2$ on the same sample space (not necessarily independent, nor discrete),
$$E[X_1+X_2]=E[X_1]+E[X_2].$$
The statement must be known; the proof is optional. Discrete proof: with joint pmf $p(\cdot,\cdot)$,
$$E[X_1+X_2]=\sum_i\sum_j(a_i+b_j)p(a_i,b_j),\tag{1.2}$$
and by the third axiom $\sum_jp(a_i,b_j)=P[X_1=a_i]$ and $\sum_ip(a_i,b_j)=P[X_2=b_j]$. Splitting the sum and interchanging the order of summation gives $\sum_ia_iP[X_1=a_i]+\sum_jb_jP[X_2=b_j]=E[X_1]+E[X_2]$.

**Applications.** Linearity makes $E[\text{Binomial}(n,p)]$ immediate (sum of $n$ indicators), and it gives $E[\text{Negative Binomial}(k,p)]$ once $E[\text{Geometric}(p)]$ is known.

## From the post
Dear everyone, here are the class notes for today's class (after we address most of the remaining contents from previous day's class notes). Note that I have planned to move the discussion of transformations of random variables *after* we talk a bit about joint distributions of random variables.

Separate announcement the same day: Dear everyone, please let me know if you have any doubts about the definition of joint distribution (joint pmf, joint cdf) discussed in class today. This is a fairly new concept -- but it is closely related to what we have already seen. Ultimately, you wish to understand how two or more random variables (again, defined on the same sample space) behave together. So, you look at the intersection of two or more events, where each such event is concerned with one of the random variables under consideration.

We shall recall these definitions one more time tomorrow, and discuss linearity of expectation. I hope the examples we saw in class today help -- but if you wish, I can provide more examples. Some examples I shall try to add to the list of suggested problems as well.

## Files
- [Class notes 2nd September 2026.pdf](https://drive.google.com/file/d/1vJZRji9LoMELgoy2Es-kx1FtNdMHt2S9/view?usp=drive_web)

## Related
- [[08-Probability/PR04 Joint Distributions Expectation and Variance]]: the chapter on joint pmfs, independence and linearity.
- [[08-Probability/PR03 Discrete Random Variables and Distributions]]: binomial, geometric and negative binomial background.
- [[introduction-to-probability/2026-08-26-class-notes-27th-august-2026]]: previous class notes (transformations are deferred from there).
- [[introduction-to-probability/2026-09-02-proof-of-expectation-of-binomial-rv]]: alternative proof of the binomial mean posted the same day.

<!-- kurooto:material3aa20daa -->
## Concepts in Class notes 27th August 2026
[[zettel/linearity-of-expectation]], [[zettel/poisson-distribution-as-binomial-limit]], [[zettel/sum-of-independent-bernoulli-trials-representation-of-binomial]], [[zettel/difference-random-variable-of-symmetrical-binomial-counters]], [[zettel/truncated-geometric-random-variable-for-coin-tosses]]
<!-- /kurooto:material3aa20daa -->

<!-- kurooto:materialc2318d8b -->
## Concepts in Class notes 27th August 2026
[[zettel/sum-of-independent-bernoulli-trials-representation-of-binomial]], [[zettel/truncated-geometric-random-variable-for-coin-tosses]], [[zettel/poisson-distribution-as-binomial-limit]], [[zettel/difference-random-variable-of-symmetrical-binomial-counters]]
<!-- /kurooto:materialc2318d8b -->
