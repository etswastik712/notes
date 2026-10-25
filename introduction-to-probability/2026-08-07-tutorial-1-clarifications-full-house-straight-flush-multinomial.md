---
id: introduction-to-probability/2026-08-07-tutorial-1-clarifications-full-house-straight-flush-multinomial
aliases: [Tutorial 1 clarifications, full house and straight flush counts]
tags: [introduction-to-probability, mt2113, counting]
trust_tier: agent_written
---

# Tutorial 1 clarifications: full house, straight flush, overcounting, multinomial with $k>n$

## Covered
Four short clarifications posted after the 6-7 August classes and the first tutorial, all on the counting problems of [[introduction-to-probability/2026-08-06-practice-problems-7th-august-2026]] (problem 5) and the multinomial theorem (Classroom: announcements of 2026-08-06 and 2026-08-07).

**1. Multinomial theorem when the number of variables $k$ exceeds the exponent $n$.** Put $y=x_{n+1}+x_{n+2}+\dots+x_k$ and first expand $(x_1+\dots+x_n+y)^n$ by the multinomial theorem. Within each term, look at the power of $y$ and expand that power of $y$ in turn. This still gives a (sort of) combinatorial argument. The instructor notes it is probably not the only way (Classroom: announcement of 2026-08-06).

**2. Size of the full-house set (5-card hand, three of one denomination and two of another).**
- Count used in class: $\binom{13}{1}\binom43\binom{12}{1}\binom42=3744$.
- A student's version "$2!\binom{13}{2}\binom43\binom42$" gives the correct number for this example, but the correct way to write it is $\binom21\binom{13}{2}\binom43\binom42$. After choosing the 2 denominations, $\binom21$ is the choice of which of the two denominations is taken 3 times and which 2 times (Classroom: announcement of 2026-08-07, with an image attached, not read).
- Check: $2\cdot78\cdot4\cdot6=3744$.

**3. Overcounting in a full house.** A student asked why $\binom{52}{1}\binom32\binom{48}{1}\binom31$ is not allowed. It overcounts: if the triple is $\{7\clubsuit,7\diamondsuit,7\heartsuit\}$, choosing $7\clubsuit$ first is treated as different from choosing $7\diamondsuit$ or $7\heartsuit$ first, so the triple is counted $3$ times. For a pair such as $\{9\clubsuit,9\diamondsuit\}$ the pair is counted $2$ times. Dividing out these overcounts recovers the answer from class (Classroom: LHC 103 batch tutorial, announcement of 2026-08-07). The instructor left "think why?" for the double count of the pair: the two cards of the pair can be picked in $2!$ orders.

**4. Straight flush.** The Ace may be the lowest card (A-2-3-4-5) or the highest (10-J-Q-K-A), but the sequence cannot wrap around from King to 2. So J-Q-K-A-2, Q-K-A-2-3 and K-A-2-3-4 are not straights. The valid rank sequences are the 10 starting at A, 2, 3, ..., 10. With 4 suits, the number of straight flushes is $10\times4=40$ (Classroom: announcement of 2026-08-07).

## From the post
Item 1 (2026-08-06): "Dear everyone, one of you asked today, when I was explaining the combinatorial proof for the multinomial theorem, what happens if k (the number of variables) exceeds n (the exponent). You can do the following trick (though this is most likely not the only way): you can define a new variable y=(x_{n+1}+x_{n+2}+...+x_{k}), and do the expansion for (x_{1}+x_{2}+...+x_{n}+y)^{n} first. Then, you can consider, within each term, the power of y, and then expand that one. This still gives you a combinatorial (sort of) argument."

Item 2 (2026-08-07): "One of the students asked about Q.5, that can we write size of full house as "2! 13C2 4C3 4C2" ( I used 13C1 4C3 12C1 4C2). Yes, this is will give correct answer for this example. BUT THE CORRECT WAY TO WRITE WILL BE * 2C1 13C2 4C3 4C2*. This is because after choosing 2 denominations, 2C1 provides the choices we are making (ie. From 2 which denominations, which one will be 3 times and which one will be 2 times)."

Item 3 (2026-08-07): "Clarification regarding Question 5 (Straight Flush). During today's tutorial, one of the students asked why sequences such as J-Q-K-A-2, Q-K-A-2-3, etc., are not considered straight flushes. [...] Therefore, there are 10 possible rank sequences, and with 4 suits, the total number of straight flushes is: 10 times 4 = 40. I hope this clarifies the doubt."

Item 4 (2026-08-07): "In the LHC 103 batch tutorial, towards the end someone raised the question on P5 that why can't they count it as 52C1 \times 3C2 \times 48C1 \times 3C1. This results into an overcount. Observe that if the triple is {7C,7D,7H} (as per the notation I used in class) then your method treats picking 7C first as different from choosing 7D or 7H first. So a thrice overcount here. For the pair, say {9C,9D}, again a double overcount (think why?). Fixing this overcount should give you the answer discussed in class. Hope this helps!"

## Files
- [Aug 7, 2026 at 3:21 PM.jpg](https://drive.google.com/file/d/1xeBdKBHe3m7aSb0c-wMPcGGkktCovHUx/view?usp=drive_web): image attached to the full-house post, not read (no text extracted).

## Related
- [[introduction-to-probability/2026-08-06-practice-problems-7th-august-2026]]: problem 5 (full house, straight flush) that these posts clarify
- [[introduction-to-probability/2026-08-05-class-notes-5th-august-2026]]: combinations, multinomial coefficients and the multinomial theorem
- [[introduction-to-probability/2026-08-05-class-notes-6th-august-2026]]: naive definition $P[A]=|A|/|S|$ used for the hand probabilities
