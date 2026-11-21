---
id: intro-to-proofs/2026-11-18-team-quiz-assignments-6-9-with-solutions
aliases: [Team quiz Assignments 6-9 with solutions]
tags: [intro-to-proofs, quiz, solutions]
trust_tier: agent_written
---
# Team quiz, Assignments 6-9 (questions and solutions)

## Covered
Six-question team quiz held in the second tutorial (Batch 1, discussed by Ekta), posted with solutions. Throughout, $\mathbb N=\{1,2,3,\dots\}$. Format: six rounds of 9 minutes (3 discussion, 4 board work, 2 checking); 4 points per complete correct solution, +1 for a first-time presenter's attempt; max 30 points per team.

**1. Functions.** $f:\mathbb R\to\mathbb R$, $f(x)=x^2-4$.
- (a) Image: $x^2\ge0$ gives outputs in $[-4,\infty)$; conversely for $y\ge-4$, $x=\sqrt{y+4}$ gives $f(x)=y$. So $\operatorname{Im}f=[-4,\infty)$. Pre-image: $x^2-4=5\iff x^2=9$, so $f^{-1}(\{5\})=\{-3,3\}$.
- (b) Not injective: $f(1)=f(-1)=-3$. Not surjective onto $\mathbb R$: $-5$ has no pre-image.
- (c) $D=[0,\infty)$ works (also accepted: $D=(-\infty,0]$ with the negative square root). Injective: $f(x)=f(z)\Rightarrow(x-z)(x+z)=0$; if $x+z=0$, non-negativity gives $x=z=0$, otherwise $x=z$. Surjective: for $y\ge-4$, $\sqrt{y+4}\in D$ maps to $y$.

**2. Pairs of natural numbers.** $S=\{(m,n)\in\mathbb N\times\mathbb N: m<n\}$. Bijection $F:\mathbb N\times\mathbb N\to S$, $F(a,b)=(a,a+b)$.
- Well defined: $b\ge1\Rightarrow a<a+b$, so $F(a,b)\in S$.
- Injective: equal first coordinates give $a=c$; then $a+b=c+d$ gives $b=d$.
- Surjective: for $(m,n)\in S$, $n-m>0$ and $F(m,n-m)=(m,n)$.
- Hence $S$ is countably infinite: compose with a bijection $\mathbb N\to\mathbb N\times\mathbb N$.

**3. A sequence missing from a list.** $A$ = infinite 0-1 sequences with first entry $0$.
- $A$ is infinite: the sequences with exactly one $1$, at position $2,3,4,\dots$, are distinct elements of $A$.
- Diagonal: given a list $a^{(1)},a^{(2)},\dots$ in $A$, set $b_1=0$ and $b_{n+1}=1-a^{(n)}_{n+1}$. Then $b\in A$ and $b$ differs from $a^{(n)}$ at position $n+1$, so $b$ is not in the list. No list exhausts $A$; being infinite, $A$ is uncountable.
- Check: diagonalising on the first entry would leave $A$; the formula above keeps it fixed.

**4. Induction.** Claim: $1\cdot2+2\cdot3+\dots+n(n+1)=\dfrac{n(n+1)(n+2)}3$ for all $n\in\mathbb N$.
- Base $n=1$: both sides equal $2$.
- Step: assume $P(k)$; then $\sum_{j=1}^{k+1}j(j+1)=\frac{k(k+1)(k+2)}3+(k+1)(k+2)=\frac{(k+1)(k+2)(k+3)}3$, which is $P(k+1)$.

**5. Strong induction (Assignment 9 pattern).** Every integer $n\ge12$ is $4x+5y$ with $x,y\ge0$ integers.
- Initial cases: $12=4\cdot3+5\cdot0$, $13=4\cdot2+5\cdot1$, $14=4\cdot1+5\cdot2$, $15=4\cdot0+5\cdot3$.
- Step for $n\ge16$: assume $P(j)$ for all $12\le j<n$; since $12\le n-4<n$, $n-4=4x+5y$, so $n=4(x+1)+5y$.
- Why four base cases: the step goes back by 4, so the four consecutive cases start each remainder class mod 4.
- $11$ is not representable: $y\in\{0,1,2\}$ would need $4x\in\{11,6,1\}$, none divisible by 4.

**6. Least denominator (WOP).** No rational has square $2$. Use: if $p^2$ is even then $p$ is even.
- Suppose one does. Then $D=\{q\in\mathbb N:\exists p\in\mathbb Z,\ p^2=2q^2\}$ is nonempty; let $q=\min D$ with matching $p$.
- $p^2=2q^2$ is even so $p=2u$; then $q^2=2u^2$, so $q=2v$ with $v\in\mathbb N$ and $u^2=2v^2$.
- So $v\in D$ with $v=q/2<q$, contradicting minimality.
- Check: the contradiction must use a smaller positive denominator; "lowest terms" alone does not explicitly use WOP.

## From the post
Dear Batch 1,

Please find the questions and their solutions attached, which were discussed by Ekta in the last second tutorial.

You can collect all of your quiz papers from my office A-459 tomorrow (19 - 11 - 2026) from 4:00 PM - 5:00 PM, or today (18-11-2026) between 6:00 PM - 6:30 PM.

Best,
Aakanksha

## Files
- [Team_Quiz_Assignments_6-9_with_Solutions.pdf](https://drive.google.com/file/d/1kVz18_ijGc7RYXXjICzCGw279rxepAEk/view?usp=drive_web): read in full.

## Related
- [[intro-to-proofs/2026-10-22-assignment-8]]: countability, diagonal argument and induction identities (Q2, Q3, Q4 here)
- [[intro-to-proofs/2026-10-30-assignment-9]]: strong induction and WOP (Q5, Q6 here)
- [[intro-to-proofs/2026-10-19-solutions-assignment-7]]: bijections on products and countability
- [[intro-to-proofs/2026-10-20-countable-and-uncountable-sets-lectures-17-to-20]]: Cantor's diagonal argument
- [[zettel/well-ordering-principle]]: Q6 uses it
- [[zettel/principle-of-strong-induction]]: Q5 uses it
- [[zettel/method-of-minimal-counterexample]]: Q6 pattern

<!-- kurooto:materiale4527841 -->
## Concepts in Team_Quiz_Assignments_6-9_with_Solutions
(none new)
<!-- /kurooto:materiale4527841 -->
