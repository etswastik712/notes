---
title: Loschmidt and Zermelo Paradoxes
aliases: ["reversibility paradox", "recurrence paradox", "Umkehreinwand", "Wiederkehreinwand"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Loschmidt and Zermelo Paradoxes

> [!info] Source
> Huang §4.4–4.5 (pp. 85–92); Kardar §3.5; [[SM04 Kinetic Theory and the Boltzmann Equation]] §7; [[SM02 Phase Space Liouville and the Microcanonical Ensemble]] §2.1.

> [!intuition] In one picture
> If the laws are reversible and the system is bounded, how can $H$ decrease for ever? Answer: it does so for *typical* states, and the exceptions are exponentially rare.

> [!key] Key facts
> **Loschmidt (1876):** reversing all velocities reverses the motion, so $H$ would increase. **Zermelo (1896):** by Poincaré recurrence the system returns near its initial state. **Resolution (Boltzmann):** the reversed and recurrent states are atypical (measure $\sim e^{-\Delta S/k_B}$), the recurrence time $\sim e^{N\cdot\text{const}}\tau$; molecular chaos for incoming pairs is the asymmetric, statistical input.

> [!example] Kac ring (recomputed)
> Exactly reversible and periodic (return at $t=N$ for $k$ even): $N=400$, $k=80$: $m_{400}=1$ exactly; yet $\langle m_t\rangle=(1-2\mu)^t$ and the imbalance has decayed to noise within 21 steps for $\mu=0.1$. Recurrence time over relaxation time $=N/20.6\approx485$ at $N=10^4$ ([[Kac Ring]]).

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Irreversibility]] · [[H-Theorem]] · [[Liouville's Theorem]] · [[Ergodic Hypothesis]] · [[Large Deviation Principle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
