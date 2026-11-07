---
id: introduction-to-probability/2026-08-05-why-study-probability
aliases: [Why study probability]
tags: [introduction-to-probability, motivation]
trust_tier: agent_written
---

# Why study probability

## Covered
Motivational notes on applications of probability and statistics (Classroom: Why study probability.pdf). Context material, not technical results.

**Applications by area**
- **Physics.** Born (1926): $|\psi|^2$ is the probability density for finding a whole, point-like electron at a location, not a smeared-out charge density (Schrödinger's first reading). A particle with energy $E$ meeting a barrier of height $V>E$ is classically reflected with certainty; in quantum mechanics $\psi(x)\propto e^{-\alpha x}$ inside a flat barrier ($\alpha>0$), so it can emerge on the other side (tunnelling), which is used in modern transistors.
- **Chemistry.** Reactions occur when colliding molecules have kinetic energy above the activation energy. Molecular speeds follow the Maxwell-Boltzmann distribution; the fraction able to react at temperature $T$ is the integral of its density from the threshold speed to infinity, so raising the temperature raises the rate.
- **Biology.** Alleles segregate at random in meiosis. With allele frequencies $p$ (for $A$) and $q$ (for $a$) and random mating, the genotype frequencies are $p^2$ for $AA$, $q^2$ for $aa$ and $2pq$ for $Aa$ (Hardy-Weinberg equilibrium). Significant deviation, measured by a $\chi^2$ goodness-of-fit test, signals natural selection or non-random mating.
- **Earth and climate sciences.** Earthquake occurrence (location, time, magnitude) is modelled with stochastic processes such as non-homogeneous Poisson processes. Modern climate models add stochastic noise to the physical fluid equations (stochastic parametrisation), replacing purely deterministic formulae.

**Probability makes statistics possible**
- Probability starts from a model and moves toward data; statistics builds a model from observed data.
- Measurements give noisy samples around a true value; probability (via confidence intervals) says where the true value may lie with a given confidence.
- Prediction (climate, stock markets, bank and insurance risk) uses time series: today's value depends on yesterday's plus random noise.
- Clinical trials need randomisation, treatment and control groups and double-blinding, so that statistics can say whether a benefit is coincidence.
- Product testing under extreme heat or stress uses survival analysis, accelerated life testing and extreme value theory.
- An LLM computes a large conditional probability from its training data rather than looking an answer up; a short example is promised in class.

**Reading:** the statistics book containing the Salk polio vaccine trial is by David Freedman, Robert Pisani and Roger Purves (the title is missing from the post text).

## From the post
Dear everyone, here are some notes I prepared regarding the various applications of probability (and statistics). Also, the book on statistics (containing a description of the Jonas Salk polio vaccine trial) is called  by David Freedman, Robert Pisani, and Roger Purves.

## Files
- [Why study probability.pdf](https://drive.google.com/file/d/1fzMx9gKkhsmYRs1CjJ6E3mfH54cXToQB/view?usp=drive_web)

## Related
- [[08-Probability/Probability - Course Map]]: your map of the probability course
- [[08-Probability/Concepts/Poisson Distribution]]: Poisson processes are used in the earthquake model
- [[08-Probability/Concepts/Normal Distribution]]: the Gaussian family behind the confidence-interval remark

<!-- kurooto:materialab5cdead -->
## Concepts in Why study probability
[[zettel/quantum-tunneling]], [[zettel/maxwell-boltzmann-distribution-in-reaction-kinetics]], [[zettel/stochastic-parametrization]], [[zettel/language-model-conditional-probability-generation]]
<!-- /kurooto:materialab5cdead -->
