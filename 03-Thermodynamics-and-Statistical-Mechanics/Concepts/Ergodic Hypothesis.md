---
title: Ergodic Hypothesis
aliases: ["ergodicity", "time average equals ensemble average", "mixing"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Ergodic Hypothesis

> [!info] Source
> Kardar §4.1; Pathria §1.2; [[SM02 Phase Space Liouville and the Microcanonical Ensemble]] §3.

> [!intuition] In one picture
> If a trajectory visits the whole energy surface evenly, then the long-time average of an observable equals its average over the surface with equal weights.

> [!key] Key facts
> $\lim_{T\to\infty}\frac1T\int_0^T\mathcal O(\mu(t))\,\mathrm dt=\langle\mathcal O\rangle_{\rm micro}$. Not literally true for integrable systems (invariant tori) nor for weakly perturbed ones (KAM); what is used is mixing plus concentration of measure, and the **postulate of equal a priori probabilities** for an isolated system.

> [!pitfall] The postulate does not need ergodicity
> The shell density $\rho=1/\Omega$ is stationary (Liouville) and treats all microstates alike; the time to sample the surface is astronomically long ($\sim10^{6N}$ molecular times), so the time-average argument is a *heuristic*, not the justification.

Used in: [[SM02 Phase Space Liouville and the Microcanonical Ensemble]]. Related: [[Liouville's Theorem]] · [[Microcanonical Ensemble]] · [[Statistical Entropy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
