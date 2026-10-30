---
id: introduction-to-probability/2026-08-19-class-notes-19th-august-2026
aliases: [Class notes 19 August 2026]
tags: [introduction-to-probability, lecture, bayes, multiplication-rule, independence]
trust_tier: agent_written
---

# Class notes 19 August 2026

## Covered
Bayes' rule, the multiplication rule for several events, and independence of events (Classroom: Class notes 19th August 2026).

**Multiplication rule.** For events $E,F$ of the same sample space with $P[F]>0$,
$$P[E\mid F]=\frac{P[E\cap F]}{P[F]}\iff P[E\cap F]=P[E\mid F]\,P[F].$$
For events $E_1,\dots,E_n$ with $P[E_i]>0$ for each $i$,
$$P\Big[\bigcap_{i=1}^nE_i\Big]=P[E_n\mid E_1,\dots,E_{n-1}]\,P[E_{n-1}\mid E_1,\dots,E_{n-2}]\cdots P[E_2\mid E_1]\,P[E_1],$$
obtained by peeling off $E_1$, then $E_2$, and so on.

**Example (class).** A deck of 52 cards is divided into 4 piles of 13. What is the probability that each pile has exactly one ace? Solved two ways, one of them with the multiplication rule.

**Bayes' formula for several events.** Let $E_1,\dots,E_n,F$ be events of the same sample space $\Omega$ with $\bigcup_iE_i=\Omega$ and $E_i\cap E_j=\emptyset$ for $i\ne j$. Then
$$P[F]=\sum_{i=1}^nP[F\cap E_i]=\sum_{i=1}^nP[F\mid E_i]P[E_i],$$
$$P[E_i\mid F]=\frac{P[F\cap E_i]}{P[F]}=\frac{P[F\mid E_i]P[E_i]}{\sum_{j=1}^nP[F\mid E_j]P[E_j]}.$$

**Examples (class).**
- A plane is missing and equally likely to be in any of 3 regions. If $1-\beta_i$ is the probability of finding it on searching region $i$ when it is there, find $P[\text{in region }i\mid\text{search of region 1 unsuccessful}]$ for $i=1,2,3$.
- A test detects a disease with probability 95% when present and gives a false positive for 1% of healthy people; 0.5% of the population has the disease. Find $P[\text{disease}\mid\text{positive}]$.

**Independence of two events.** For $P[F]>0$, $E$ and $F$ are independent if $P[E\mid F]=P[E]$ (knowing $F$ occurred does not affect the chances of $E$). Equivalent: $P[E\cap F]=P[E]P[F]$. If $E$ and $F$ are independent, so are $E$ and $F^c$.

**Independence of several events.** $E_1,\dots,E_r$ are independent if for every non-empty subset $\{i_1,\dots,i_s\}\subset\{1,\dots,r\}$
$$P\Big[\bigcap_{j=1}^sE_{i_j}\Big]=\prod_{j=1}^sP[E_{i_j}].$$
An infinite collection is independent if every finite sub-collection is.

**Example (class).** Two independent fair dice (the notes say "head", but the events are about die outcomes): $A$ = first die gives a given outcome, $B$ = second die gives a given outcome, $C$ = both dice give the same outcome. Are $A,B,C$ independent? The notes point to this example as showing something important (pairwise independence need not give independence of all three; the check is left to the student).

**Conditional probability is a probability.** Mentioned on 13 August but omitted from those notes: for any event $F$ with $P[F]>0$, $f(A)=P[A\mid F]$ satisfies the three axioms of probability.

## From the post
Dear everyone, here are the class notes for today's class.

## Files
- [Class notes 19th August 2026.pdf](https://drive.google.com/file/d/11TC4DPQ0oGRhuDqcxDWTBocQts7Jo6jU/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-08-11-class-notes-13th-august-2026]]: conditional probability, multiplication rule and total probability introduced there
- [[introduction-to-probability/2026-08-13-practice-problems-14th-august-2026]]: Bayes problems this class formalises
- [[introduction-to-probability/2026-08-19-practice-problems-21st-august-2026]]: problems 2-10 practise this material
- [[introduction-to-probability/2026-08-19-class-notes-20th-august-2026]]: next class, random variables
- [[08-Probability/Probability - Course Map]]: their own probability chapters

<!-- kurooto:materialbbf3fd0f -->
## Concepts in Class notes 19th August 2026
[[zettel/multiplication-rule-for-conditional-probability]], [[zettel/bayes-rule-for-a-finite-partition]], [[zettel/partition-of-the-sample-space]], [[zettel/conditional-probability-measure]], [[zettel/independence-of-events]], [[zettel/mutual-independence-of-a-finite-collection-of-events]]
<!-- /kurooto:materialbbf3fd0f -->
