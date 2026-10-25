---
title: PR02 Conditional Probability Bayes Rule and Independence
aliases: [PR02, conditional probability, Bayes rule, independence of events, MT2113 classes 13-19 August]
subject: probability
type: chapter
chapter: 2
part: I
scope: [taught, extra-book, extra-beyond]
by: [lecture-notes]
status: draft
prereq: [PR01 Counting and the Axioms of Probability]
tags: [subject/probability, type/chapter, taught, extra/book, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# PR02 · Conditional Probability, Bayes' Rule and Independence

◀ [[PR01 Counting and the Axioms of Probability]] · [[PR03 Discrete Random Variables and Distributions]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**: [[ilovepdf_merged-1.pdf#page=12|class notes of 13 Aug]] (pp.12–14: conditional probability, the reduced sample space, urns, multiplication rule, the total-probability step), [[ilovepdf_merged-1.pdf#page=15|19 Aug]] (pp.15–16: Bayes' formula, multiplication rule for many events, independence), the sheets of [[Practice problems 14th August 2026.pdf|14 Aug]] (smokers, Monty Hall, a 95 %/95 % test, two coins) and [[Practice problems 21st August 2026.pdf|21 Aug]].
> - §1 definition, reduced sample space, multiplication rule
> - §2 law of total probability and Bayes' rule (disease test, plane search, multiple choice, insurance, inspector)
> - §3 urns without replacement and exchangeability
> - §4 independence of two events, of $r$ events, and pairwise vs mutual independence
> - §5 $P(\cdot\mid F)$ is itself a probability; "5 before 7" (21 Aug sheet)
> - §6 the Monty Hall problem (solved in class; problem 4 of the 14 Aug sheet)
>
> 🟡 **Extra · book**
> - §5 **gambler's ruin** (the 27 Aug notes call it "not formally a part of the syllabus"; it is on the 21 Aug practice sheet)
> - §6 conditional independence (Blitzstein and Hwang Ch. 2)
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §2 the odds form of Bayes' rule and the natural-frequency picture; how the posterior changes with prevalence; every number recomputed (`scripts/pr_numbers.py`)

> [!key] After this chapter you can
> - compute $P(E\mid F)$ by the definition or by shrinking the sample space, and chain conditional probabilities with the **multiplication rule**,
> - split a probability over a **partition** (total probability) and invert it with **Bayes' rule**,
> - tell **independence** from **mutual exclusivity**, and **pairwise** from **mutual** independence,
> - solve urn, test, search and gambler's-ruin problems by conditioning on the right first step.

> [!intuition] The one-sentence story
> New information shrinks the world of possibilities to $F$, and conditional probability is just "$E$'s share of $F$"; Bayes' rule is that same share read backwards, from effects to causes.

## 1. Conditional probability
<span class="scope-taught">taught</span> *13 Aug ([[ilovepdf_merged-1.pdf#page=12|p.12]])*

> [!key] Definition
> For events $E,F$ with $P[F]>0$,
> $$P[E\mid F]=\frac{P[E\cap F]}{P[F]}\qquad\Longleftrightarrow\qquad P[E\cap F]=P[E\mid F]\,P[F]\quad(\text{multiplication rule}).$$
> It measures how knowing that $F$ happened changes our belief in $E$.

When all outcomes are equally likely, work in the **reduced sample space** $F$ and count: $P[E\mid F]=|E\cap F|/|F|$.

> [!example] Cards (class, 13 Aug)
> The 52 cards are dealt equally to North, South, East and West. North and South together hold 8 spades. What is the probability East has 3 spades? Given the 8 spades, the other 26 cards (West and East) contain exactly 5 spades, and East's 13 cards are a random $13$-subset of those 26: $P=\dfrac{\binom53\binom{21}{10}}{\binom{26}{13}}=0.339$. (Conditioning removed North and South's cards from the sample space.)

> [!key] The multiplication rule for $n$ events ($P[E_i]>0$, 19 Aug)
> $$P\Big[\bigcap_{i=1}^nE_i\Big]=P[E_1]\,P[E_2\mid E_1]\,P[E_3\mid E_1\cap E_2]\cdots P\Big[E_n\ \Big|\ \bigcap_{i=1}^{n-1}E_i\Big].$$
> Proof: apply $P[A\cap B]=P[A\mid B]P[B]$ repeatedly with $B=E_1\cap\dots\cap E_{n-1}$.

> [!example] Four piles, one ace each (class, 19 Aug)
> Deal a shuffled deck into 4 piles of 13. What is the probability each pile has exactly one ace? **By conditioning**: let $E_1$ = "the ace of spades is in some pile" (certain); $E_2$ = "the ace of hearts is in a different pile" ($\tfrac{39}{51}$); $E_3$ = "the ace of diamonds is in a third pile" ($\tfrac{26}{50}$); $E_4$ = "the ace of clubs is in the last pile" ($\tfrac{13}{49}$). Hence $P=1\cdot\tfrac{39}{51}\cdot\tfrac{26}{50}\cdot\tfrac{13}{49}=0.1055$. **By counting**: $\dfrac{4!\,48!/(12!)^4}{52!/(13!)^4}$ gives the same $0.1055$ (a simulation of 20,000 deals gives $0.107$).

> [!pitfall] $P[E\mid F]$ is not $P[F\mid E]$
> $P[\text{positive test}\mid\text{ill}]=0.95$ says nothing by itself about $P[\text{ill}\mid\text{positive test}]$; the two differ by the prior (see §2). In the courtroom this confusion is called the **prosecutor's fallacy**.

## 2. Total probability and Bayes' rule
<span class="scope-taught">taught</span> *13 and 19 Aug ([[ilovepdf_merged-1.pdf#page=13|p.13]], [[ilovepdf_merged-1.pdf#page=15|p.15]])*

Split $E=(E\cap F)\cup(E\cap F^c)$, which are disjoint, so
$$P[E]=P[E\mid F]\,P[F]+P[E\mid F^c]\,(1-P[F]).$$
More generally, if $E_1,\dots,E_n$ are pairwise disjoint with $\bigcup E_i=\Omega$ (a **partition**) and $F$ is any event,

> [!key] Law of total probability and Bayes' rule
> $$P[F]=\sum_{j=1}^nP[F\mid E_j]\,P[E_j],\qquad\boxed{\ P[E_i\mid F]=\frac{P[F\mid E_i]\,P[E_i]}{\sum_{j=1}^nP[F\mid E_j]\,P[E_j]}\ }$$
> $P[E_i]$ = **prior** (before seeing $F$), $P[F\mid E_i]$ = **likelihood**, $P[E_i\mid F]$ = **posterior**.

![[fig_pr02_bayes.png]]
*Figure PR2.1. A: the posterior $P(D\mid +)$ against the prevalence, for a test with 95 % sensitivity and 1 % or 5 % false positives (the 0.5 % class example and the 1 % sheet example are marked). B: the same class example as natural frequencies for 10,000 people: 47.5 true positives against 99.5 false positives.*

> [!example] The disease test (class, 19 Aug)
> A test detects the disease (D) in 95 % of the ill and gives a false positive for 1 % of the healthy; 0.5 % of the population is ill. Then
> $$P[D\mid+]=\frac{0.95\times0.005}{0.95\times0.005+0.01\times0.995}=\frac{0.00475}{0.01470}=0.323 .$$
> Only about **one positive in three** is a real case, because the healthy are so numerous that even 1 % false positives (99.5 per 10,000) outnumber the 47.5 true ones. 🔵 With the same test the posterior rises to $0.68$ at 10 % prevalence and $0.95$ at 50 % (for the 95 %/5 % test of the next example).

> [!example] Plane search (class, 19 Aug)
> A plane is equally likely ($\tfrac13$ each) to be in region 1, 2 or 3. If the plane is in region $i$, a search of that region finds it with probability $1-\beta_i$. Search region 1 finds nothing. Then
> $$P[R_1\mid F]=\frac{\beta_1\cdot\frac13}{\beta_1\cdot\frac13+\frac13+\frac13}=\frac{\beta_1}{\beta_1+2},\qquad P[R_{2}\mid F]=P[R_3\mid F]=\frac1{\beta_1+2}.$$
> For $\beta_1=0.2$: $0.091$ for region 1 and $0.455$ for each of regions 2 and 3: the failed search moves belief **away** from region 1, but not to zero, since the search could have missed.

> [!example] Five more (sheets of 14 and 21 Aug)
> **A 95 %/95 % test (14 Aug, problem 5).** Prevalence 1 %, sensitivity and specificity 95 %: $P[D\mid+]=\dfrac{0.95\cdot0.01}{0.95\cdot0.01+0.05\cdot0.99}=0.161$ (the 1 % prevalence limits the posterior far more than the 95 % accuracy suggests).
> **Smokers (14 Aug, problem 3).** Smokers are 23 times more likely to develop lung cancer, $21.6\%$ of men smoke: $P[S\mid C]=\dfrac{23\cdot0.216}{23\cdot0.216+0.784}=0.864$.
> **Two coins (14 Aug, problem 6).** Fair or biased ($P[H]=\tfrac34$) coin chosen at random, three heads: $P[\text{fair}\mid HHH]=\dfrac{\frac12\cdot\frac18}{\frac12\cdot\frac18+\frac12\cdot\frac{27}{64}}=\dfrac8{35}=0.229$.
> **Multiple choice (21 Aug).** The student knows the answer with probability $p$, otherwise guesses with success $1/m$: $P[\text{knew}\mid\text{correct}]=\dfrac{p}{p+(1-p)/m}$; for $p=0.6$, $m=4$ this is $0.857$.
> **Insurance (21 Aug).** Accident-prone ($30\%$ of people, accident probability $0.4$) vs not ($0.2$): $P[\text{prone}\mid\text{accident}]=\dfrac{0.4\cdot0.3}{0.4\cdot0.3+0.2\cdot0.7}=\dfrac{6}{13}=0.462$.
> **Inspector (21 Aug).** Prior of guilt $0.6$; the trait is certain for the guilty and held by $20\%$ of the population: $\dfrac{0.6}{0.6+0.4\cdot0.2}=0.882$.

> [!extra-beyond]- 🔵 Extra (beyond): odds form
> Dividing Bayes' rule for $E$ by that for $E^c$ gives $\dfrac{P[E\mid F]}{P[E^c\mid F]}=\dfrac{P[F\mid E]}{P[F\mid E^c]}\cdot\dfrac{P[E]}{P[E^c]}$: posterior odds = **likelihood ratio** × prior odds. For the disease test the likelihood ratio is $0.95/0.01=95$ and the prior odds are $0.005/0.995$; $95\times0.005025=0.477$, odds $0.477:1$, i.e. probability $0.477/1.477=0.323$ (agrees).

## 3. Urns and exchangeability
<span class="scope-taught">taught</span> *13 Aug ([[ilovepdf_merged-1.pdf#page=13|pp.13–14]]); sheet 21 Aug, problems 1, 5*

An urn has $b$ black and $w$ white balls; draw sequentially **without replacement**.

> [!key] Order does not matter
> The probability of a particular colour sequence $C_1,\dots,C_k$ with $\ell$ black and $k-\ell$ white is
> $$\frac{b(b-1)\cdots(b-\ell+1)\;w(w-1)\cdots(w-k+\ell+1)}{(b+w)(b+w-1)\cdots(b+w-k+1)},$$
> **the same for every order** of the colours (the denominator counts the balls left at each draw and does not depend on the colours; the numerator multiplies the black and white balls left in the order they are used). This is called **exchangeability**.

For two draws, $P[B_1W_2]=\frac{b}{b+w}\frac{w}{b+w-1}=P[W_1B_2]$. For $b=5$, $w=3$: both equal $\tfrac{5}{8}\cdot\tfrac37=\tfrac{15}{56}=0.268$.

> [!example] Given $k$ blacks in $n$ draws, is the first black? (21 Aug, problem 1)
> By exchangeability every position is equally likely to hold the black balls, so $P[B_1\mid B_k]=k/n$. Check with Bayes: with $B$ = first ball black, $B_k$ = exactly $k$ blacks in the $n$ draws,
> $$P[B_k]=\frac{\binom bk\binom w{n-k}}{\binom{b+w}n},\quad P[B]=\frac b{b+w},\quad P[B_k\mid B]=\frac{\binom{b-1}{k-1}\binom w{n-k}}{\binom{b+w-1}{n-1}}\ \Rightarrow\ P[B\mid B_k]=\frac{k}{n}.$$
> For $b=5$, $w=3$, $n=4$, $k=2$ both routes give $\tfrac12$ (recomputed).

> [!example] A weighted urn (21 Aug, problem 5)
> 8 red and 4 white balls, 2 drawn without replacement. Equal chance: $\frac8{12}\cdot\frac7{11}=\frac{14}{33}=0.424$. If a red ball has weight $r$, a white ball weight $w$ and the next ball is chosen with probability proportional to its weight: $\dfrac{8r}{8r+4w}\cdot\dfrac{7r}{7r+4w}$; for $r=2$, $w=1$ this is $0.622$; for $r=1$, $w=3$ it is $0.147$.

## 4. Independence
<span class="scope-taught">taught</span> *19 Aug ([[ilovepdf_merged-1.pdf#page=16|p.16]]); sheet 21 Aug, problems 6–8*

> [!key] Definitions
> Events $E,F$ ($P[F]>0$) are **independent** if $P[E\mid F]=P[E]$, equivalently
> $$P[E\cap F]=P[E]\,P[F].$$
> Events $E_1,\dots,E_r$ are **(mutually) independent** if for **every** non-empty sub-collection $\{i_1,\dots,i_s\}$, $P\big[\bigcap_jE_{i_j}\big]=\prod_jP[E_{i_j}]$. An infinite family is independent if every finite sub-family is.

- If $E,F$ are independent so are $E,F^c$; $E^c,F$; and $E^c,F^c$ (sheet problem 8). Proof of the first: $P[E\cap F^c]=P[E]-P[E\cap F]=P[E](1-P[F])$.
- Independence is **not** mutual exclusivity. If $E\cap F=\varnothing$ and both have positive probability then $P[E\cap F]=0\ne P[E]P[F]$: disjoint events are strongly **dependent** (if one occurs the other cannot).
- An event is independent of itself only if $P[E]=P[E]^2$, i.e. $P[E]\in\{0,1\}$ (problem 7; this is the seed of Kolmogorov's zero-one law).
- Chain-rule proof of the product form (problem 6): with independence, $P[E_k\mid E_1\cap\dots\cap E_{k-1}]=P[E_k]$ for every $k$, so the multiplication rule collapses to $\prod P[E_i]$.

> [!example] Pairwise independent, not mutually independent (class, 19 Aug)
> Roll two fair dice. Let $A$ = "first die shows a given face" (say 6), $B$ = "second die shows the same face", $C$ = "the dice agree". Then $P[A]=P[B]=\tfrac16$, $P[C]=\tfrac16$ and
> $P[A\cap B]=\tfrac1{36}=P[A]P[B]$, $P[A\cap C]=\tfrac1{36}=P[A]P[C]$, $P[B\cap C]=\tfrac1{36}=P[B]P[C]$, so the events are **pairwise independent**. But $P[A\cap B\cap C]=\tfrac1{36}\neq\tfrac1{216}=P[A]P[B]P[C]$: $A\cap B$ already forces $C$, so they are **not mutually independent**. (With coins the same story: $A$ = H on toss 1, $B$ = H on toss 2, $C$ = tosses agree: $P[ABC]=\tfrac14$ against $\tfrac18$.)

> [!pitfall] Check every sub-collection
> Mutual independence needs $2^r-r-1$ product conditions, not just the pairs. Pairwise independence is the weaker property and is the one that suffices for the variance of a sum (PR04).

## 5. $P[\cdot\mid F]$ is a probability; two recursions
<span class="scope-taught">taught</span> · <span class="scope-extra-book">extra · book</span> (gambler's ruin) *19 Aug ([[ilovepdf_merged-1.pdf#page=16|p.16]]); sheet 21 Aug, problems 9–11*

For fixed $F$ with $P[F]>0$, the function $A\mapsto P[A\mid F]$ satisfies the three axioms; therefore every result of PR01 holds with $P[\cdot\mid F]$ in place of $P$ (for instance $P[A^c\mid F]=1-P[A\mid F]$, and inclusion-exclusion holds conditionally). This is the reason one can condition in stages.

> [!example] "5 before 7" (21 Aug, problem 11)
> Two fair dice are rolled repeatedly; the outcome is the sum. $P[5]=\tfrac4{36}$, $P[7]=\tfrac6{36}$. Let $E_n$ be "no 5 or 7 in the first $n-1$ trials and a 5 at trial $n$". By independence of trials, $P[E_n]=(1-\tfrac{10}{36})^{n-1}\tfrac4{36}$. The $E_n$ are disjoint and their union is "a 5 appears before a 7", so by the third axiom
> $$P=\sum_{n\ge1}\Big(\frac{26}{36}\Big)^{n-1}\frac{4}{36}=\frac{4/36}{10/36}=\frac25 .$$
> This says: ignore every trial that is neither, and condition on the first trial that is: $P[5\mid5\text{ or }7]=\tfrac4{4+6}$.

> [!example] Gambler's ruin (21 Aug, problem 9; 🟡 not formally in the syllabus)
> A gambler with $i$ units plays against a casino with $n-i$ units; each round he wins one unit with probability $p$, else loses one. Let $p_i$ = P(bankrupt before reaching $n$), with $p_0=1$, $p_n=0$. **Condition on the first round**: $p_i=p\,p_{i+1}+(1-p)\,p_{i-1}$, i.e. $p_{i+1}-p_i=\tfrac{1-p}{p}(p_i-p_{i-1})$. Telescoping, with $\rho=(1-p)/p$:
> $$p_i=\frac{\rho^i-\rho^n}{1-\rho^n}\quad(p\ne\tfrac12),\qquad p_i=1-\frac in\quad(p=\tfrac12).$$
> Numbers ($i=3$, $n=10$): $p=\tfrac12$: bankrupt $0.70$, success $0.30$; $p=0.6$: bankrupt $0.284$; $p=0.4$: bankrupt $0.958$ (all recomputed).

> [!extra-beyond]- 🔵 Extra (beyond): solving the recursion
> Put $d_i=p_i-p_{i-1}$. Then $d_{i+1}=\rho d_i$, so $d_i=\rho^{i-1}d_1$ and $p_i=1+d_1(1+\rho+\dots+\rho^{i-1})$. The condition $p_n=0$ fixes $d_1=-(1-\rho)/(1-\rho^n)$ for $\rho\ne1$; for $\rho=1$, $d_i=d_1=-1/n$, which gives $p_i=1-i/n$.

## 6. The Monty Hall problem and conditional independence
<span class="scope-taught">taught</span> (Monty Hall: solved in class, 14 Aug sheet problem 4; named again on 19 Aug) · <span class="scope-extra-book">extra · book</span> (conditional independence)

A prize is behind one of 3 doors. You pick door 1; the host, who **knows** where the prize is, always opens a different door with a goat and offers a switch. Let $C_i$ = "prize behind door $i$" and $H_3$ = "host opens door 3". Then $P[H_3\mid C_1]=\tfrac12$ (he may open 2 or 3), $P[H_3\mid C_2]=1$ (forced), $P[H_3\mid C_3]=0$. By Bayes,
$$P[C_2\mid H_3]=\frac{1\cdot\frac13}{\frac12\cdot\frac13+1\cdot\frac13+0}=\frac23,\qquad P[C_1\mid H_3]=\frac13 .$$
**Switching wins with probability $2/3$** (simulated: $0.666$ over 100,000 plays). The point is that the host's action is **not independent of the prize**; with 100 doors and 98 opened, switching wins with probability $0.99$.

> [!extra-book]- 🟡 Extra (book): conditional independence
> $E$ and $F$ are **conditionally independent given $G$** if $P[E\cap F\mid G]=P[E\mid G]P[F\mid G]$. This neither implies nor is implied by ordinary independence: two coin tosses are independent given the coin's bias, but not independent unconditionally if the bias is unknown (the first toss tells you about the coin). Marble problem (21 Aug, problem 10): one marble, blue or green with equal probability, a green one is added and one is drawn at random, found green: $P[\text{other is green}]=\tfrac23$, not $\tfrac12$, because the draw favours the bag with two greens.

## Map of this chapter
> [!connection] How PR02 connects
> **Builds on:** [[PR01 Counting and the Axioms of Probability]] (the axioms hold conditionally; naive probability gives the reduced sample space).
> **Leads to:** [[PR03 Discrete Random Variables and Distributions]] (independent trials give the binomial and geometric laws; "5 before 7" is a geometric sum) → [[PR04 Joint Distributions Expectation and Variance]] (independence of random variables).
> **Concepts:** [[Conditional Probability]] · [[Multiplication Rule]] · [[Law of Total Probability]] · [[Bayes' Theorem]] · [[Independence of Events]] · [[Exchangeability]] · [[Gambler's Ruin]] · [[Monty Hall Problem]] · [[Conditional Independence]]
> **Other subjects:** [[Probability - Course Map]], [[Akaike Information Criterion]] (model comparison uses likelihoods), [[Quantum Mechanics - Course Map]] (conditioning on a measurement outcome is the projection postulate, [[QM03 States Operators and Measurement]]), [[EE06 Eutrophication and Alternative Stable States]] (hysteresis, Markov-type recursion on first steps).

## Summary
> [!summary] Cheat-sheet
> - $P[E\mid F]=P[E\cap F]/P[F]$; $P[E\cap F]=P[E\mid F]P[F]$; chain $P[\cap E_i]=P[E_1]P[E_2\mid E_1]\cdots$.
> - Partition $E_1,\dots,E_n$: $P[F]=\sum P[F\mid E_j]P[E_j]$; **Bayes** $P[E_i\mid F]=\dfrac{P[F\mid E_i]P[E_i]}{\sum_jP[F\mid E_j]P[E_j]}$; odds form: posterior odds = likelihood ratio × prior odds.
> - Urn without replacement: every colour order equally likely (exchangeability); $P[B_1\mid k\text{ blacks in }n]=k/n$.
> - Independent: $P[E\cap F]=P[E]P[F]$, then also with complements; mutually independent needs **all** sub-collections; pairwise ≠ mutual; disjoint ≠ independent; $P[E]\in\{0,1\}$ if $E$ is independent of itself.
> - $P[\cdot\mid F]$ satisfies the axioms. **Gambler's ruin** $p_i=\frac{\rho^i-\rho^n}{1-\rho^n}$, $\rho=\frac{1-p}p$; $1-i/n$ if fair. **5 before 7:** $\frac4{4+6}$.
> - **Numbers:** disease test $0.323$; plane search $0.091/0.455/0.455$; four piles one ace each $0.1055$; Monty Hall switch $2/3$.

## Practice
1. **Dice.** Two fair dice are rolled. Given that the sum is 8, find the probability that at least one die shows 6, and the probability that the dice are different.
2. **Cards.** Two cards are dealt from a deck without replacement. Find the probability that both are aces; that the second is an ace; and that the first is an ace given that the second is.
3. **Bayes.** A factory has three machines producing 50 %, 30 % and 20 % of the output with defect rates $2\%$, $3\%$ and $5\%$. A random item is defective. Find the probability that it came from each machine.
4. **Test.** A screening test has sensitivity 90 % and false-positive rate 4 %. For a prevalence of 2 %, find $P[\text{ill}\mid+]$. What prevalence makes it equal to $\tfrac12$?
5. **Independence.** $P[A]=0.4$, $P[B]=0.5$, $P[A\cup B]=0.7$. Are $A,B$ independent? Find $P[A\cap B^c]$.
6. **Three events.** Roll one fair die. Let $A=\{1,2,3\}$, $B=\{3,4,5\}$, $C=\{3,6\}$. Check each pair for independence, then decide whether $A,B,C$ are mutually independent.
7. **Urn.** An urn has 6 red and 4 blue balls. Three balls are drawn without replacement. Find the probability that the colours are red, blue, red in that order, and that exactly two of the three are red.
8. **Gambler.** A fair game: the gambler starts with 4 units and stops at 0 or 10. Find the probability of reaching 10. Repeat for $p=0.45$.
9. **Race.** Two dice are rolled repeatedly. Find the probability that a sum of 6 occurs before a sum of 7.
10. **Reversing.** Show that if $P[A\mid B]>P[A]$ then $P[B\mid A]>P[B]$, and that $P[A\mid B]+P[A^c\mid B]=1$.

> [!example]- Solutions
> 1. Sum 8 has 5 outcomes: $(2,6),(3,5),(4,4),(5,3),(6,2)$. At least one 6: $2/5$. Different: $4/5$ (only $(4,4)$ matches).
> 2. Both aces: $\tfrac4{52}\cdot\tfrac3{51}=\tfrac1{221}$. Second an ace: $\tfrac4{52}$ (by symmetry/exchangeability). First an ace given the second is: $3/51=1/17$.
> 3. $P[\text{def}]=0.5(0.02)+0.3(0.03)+0.2(0.05)=0.01+0.009+0.01=0.029$. Posteriors: $0.010/0.029=0.345$, $0.009/0.029=0.310$, $0.010/0.029=0.345$.
> 4. $\dfrac{0.9\cdot0.02}{0.9\cdot0.02+0.04\cdot0.98}=\dfrac{0.018}{0.0572}=0.315$. Setting the posterior to $\tfrac12$: likelihood ratio $0.9/0.04=22.5$, so prior odds $=1/22.5$ and prevalence $=1/23.5=4.26\%$.
> 5. $P[A\cap B]=0.4+0.5-0.7=0.2=P[A]P[B]$: independent. $P[A\cap B^c]=P[A]-P[A\cap B]=0.2$.
> 6. $P[A]=P[B]=\tfrac12$, $P[C]=\tfrac13$. $P[A\cap B]=\tfrac16\ne\tfrac14$: **not** independent. $P[A\cap C]=\tfrac16=\tfrac12\cdot\tfrac13$ and $P[B\cap C]=\tfrac16$: independent. Triple: $P[A\cap B\cap C]=P[\{3\}]=\tfrac16\ne\tfrac1{12}$. So the triple is not mutually independent (and not even pairwise).
> 7. R,B,R: $\tfrac6{10}\cdot\tfrac49\cdot\tfrac58=\tfrac16$. Exactly two red: $\binom62\binom41/\binom{10}3=60/120=\tfrac12$ (three orders each of probability $\tfrac16$).
> 8. $p=\tfrac12$: $4/10=0.4$. For $p=0.45$: $\rho=0.55/0.45=1.2222$, $\rho^4=2.2315$, $\rho^{10}=7.4388$: $P[\text{bankrupt}]=\dfrac{\rho^4-\rho^{10}}{1-\rho^{10}}=\dfrac{2.2315-7.4388}{1-7.4388}=0.809$, so reaching 10 has probability $0.191$.
> 9. $P[6]=\tfrac5{36}$, $P[7]=\tfrac6{36}$: $\dfrac5{5+6}=\dfrac5{11}=0.4545$.
> 10. $P[A\mid B]>P[A]\Rightarrow P[A\cap B]>P[A]P[B]\Rightarrow P[B\mid A]=P[A\cap B]/P[A]>P[B]$. And $P[A\mid B]+P[A^c\mid B]=\dfrac{P[A\cap B]+P[A^c\cap B]}{P[B]}=\dfrac{P[B]}{P[B]}=1$.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | conditional probability, reduced sample space, North/South/East/West spades, urns, multiplication rule, total probability | [[ilovepdf_merged-1.pdf#page=12\|class notes 13 Aug, pp.12–14]] | taught |
> | Bayes' formula (partition form), four piles, plane search, disease test, independence, dice example, $P[\cdot\mid F]$ | [[ilovepdf_merged-1.pdf#page=15\|class notes 19 Aug, pp.15–16]] | taught |
> | multiple choice, insurance, inspector, weighted urn, independence facts, gambler's ruin, marble, "5 before 7" | [[Practice problems 21st August 2026.pdf\|sheet 21 Aug]] | taught |
> | smokers, Monty Hall, 95 %/95 % test, two coins | [[Practice problems 14th August 2026.pdf\|sheet 14 Aug]] (problems 3–6) | taught |
> | conditional independence | Blitzstein and Hwang Ch. 2 (not opened: scan) | extra/book |
> | odds form, prevalence sweep, recomputed numbers | `scripts/pr_numbers.py`, `fig_pr02_bayes.py` | extra/beyond |
>
> **Notes.** The 19 Aug text says each die "yields a head"; I take it to mean a fixed face. Solutions are mine. The sheet leaves the gambler's-ruin recursion to the tutorial; the closed form above is my solution of it.

> [!verify] Two different disease-test problems
> The class example (19 Aug) uses $0.95$ detection, $0.01$ false positive and $0.5\%$ prevalence, giving $0.323$. The 14 Aug sheet (problem 5) uses a 95 %/95 % test at 1 % prevalence, giving $0.161$. They are different problems; Figure PR2.1 marks both.

**References.** Blitzstein, J. K. and Hwang, J. *Introduction to Probability*, Ch. 2 · Ross, S. *A First Course in Probability* (8th ed.), Ch. 3 · Bayes, T. (1763) *An Essay towards solving a Problem in the Doctrine of Chances*.
