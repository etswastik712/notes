---
id: introduction-to-probability/2026-09-02-proof-of-expectation-of-binomial-rv
aliases: [Alternate proof of E of binomial]
tags: [probability, mt2113, proof]
trust_tier: agent_written
---

# Alternate proof of the expectation of a Binomial random variable

## Covered
Claim: if $P(X=i)=\binom ni p^i(1-p)^{n-i}$, then $\sum_{i=0}^n i\,P(X=i)=np$ (Classroom: proof of expectation of binomial RV.pdf).

Proof (differentiating the binomial theorem):
1. Binomial theorem: $(x+y)^n=\sum_{r=0}^n\binom nr x^ry^{n-r}$.
2. Differentiate in $x$: $n(x+y)^{n-1}=\sum_{r=0}^n\binom nr\,r\,x^{r-1}y^{n-r}$.
3. Multiply by $x$: $nx(x+y)^{n-1}=\sum_{r=0}^n r\binom nr x^ry^{n-r}$.
4. Put $x=p$, $y=1-p$, so $x+y=1$: $np=\sum_{r=0}^n r\binom nr p^r(1-p)^{n-r}=E[X]$.

Compare with the route via linearity of expectation (sum of $n$ Bernoulli($p$) indicators, each with mean $p$) in [[introduction-to-probability/2026-09-02-class-notes-2nd-september-2026]].

## From the post
(Alternate Proof of Expectation value of Binomial Distribution)

## Files
- [proof of expectation of binomial RV.pdf](https://drive.google.com/file/d/1VkXP82o0ME8fwwzyB2Ctnl8i6YmPepyb/view?usp=drive_web)

## Related
- [[08-Probability/PR03 Discrete Random Variables and Distributions]]: where the binomial expectation is derived in the vault.
- [[introduction-to-probability/2026-09-02-class-notes-2nd-september-2026]]: the linearity-of-expectation derivation of the same result.
