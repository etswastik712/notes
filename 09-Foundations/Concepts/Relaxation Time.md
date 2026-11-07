---
title: Relaxation Time
subject: foundations
type: concept
scope: [taught, extra-beyond]
by: [argha]
status: draft
tags: [subject/foundations, type/concept, taught, extra/beyond, src/argha, status/draft]
---
# Relaxation Time

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** stability and response (Argha L4) · 🔵 **extra:** $\tau=C\Lambda$, ocean time-scales

> [!intuition] In one picture
> A bucket with a hole: a big bucket (large heat capacity) with a small hole (small restoring term) takes a long time to settle. $\tau$ = size of bucket ÷ size of hole.

> [!key] Definition
> For $\dot\theta=-\theta/\tau$, the **relaxation time** $\tau$ is the e-folding time: $\theta(t)=\theta_0e^{-t/\tau}$; half-life $\tau\ln2$. For a linearised system, $\tau=1/|f'(x^*)|$ ([[Fixed Points and Linear Stability]]).

**Climate.** With heat capacity per area $C$ and the Planck term, $\tau=C/(4\sigma T^3)=C\,\Lambda_P$ ([[Planck Sensitivity]]); with feedbacks $\tau=C\Lambda$ (Wallace & Hobbs §10.3.1), so **positive feedbacks lengthen the response**.

| layer | $C$ (J m⁻² K⁻¹) | $\tau$ |
|---|---|---|
| dry soil slab (20 cm) | $7.5\times10^5$ | 2.3 days |
| whole atmosphere | $1\times10^7$ | 1 month |
| ocean mixed layer, 50 m | $2\times10^8$ | 1.7 yr |
| ocean, 4 km | $1.6\times10^{10}$ | $\sim140$ yr |

Hence the observed climate lags its equilibrium response ([[CL04 Feedback and Multiple Steady States]]), and near a tipping point $\tau\to\infty$ ([[Bistability and Tipping Points]]). Ecology: return time to equilibrium after a disturbance, $1/r$ for logistic growth.

> [!connection] See also
> The relaxation time as the inverse of a pole of the transfer function $1/(1+\tau s)$, and the low-pass filter: [[Fourier and Laplace Transforms]] §1, §7.5–7.6.

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Greenhouse Gas Lifetime and Potency]] (Climate): a pulse decays as exp(-t/tau): the same first-order relaxation as the planetary temperature.
