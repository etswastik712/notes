---
title: Linearisation and Sensitivity
subject: foundations
type: concept
scope: [taught, extra-beyond]
by: [argha]
status: draft
tags: [subject/foundations, type/concept, taught, extra/beyond, src/argha, status/draft]
---
# Linearisation and Sensitivity

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** chain rule, log-derivative, $\Lambda$ (Argha L4) · 🔵 **extra:** geometric-series view of feedback

> [!intuition] In one picture
> Zoom in far enough on any smooth curve and it looks like a straight line: its slope tells you how much the output changes per unit input. Sensitivity analysis is just reading that slope.

> [!key] Tools
> - **Taylor/linearisation:** $f(x+\Delta x)\approx f(x)+f'(x)\Delta x$.
> - **Chain rule / total derivative:** for $T(F,y_1,\dots)$ with $y_i=y_i(T)$: $\dfrac{\mathrm dT}{\mathrm dF}=\dfrac{\partial T}{\partial F}+\sum_i\dfrac{\partial T}{\partial y_i}\dfrac{\mathrm dy_i}{\mathrm dT}\dfrac{\mathrm dT}{\mathrm dF}$.
> - **Logarithmic differentiation** for power laws $y=c\prod x_i^{p_i}$: $\dfrac{\Delta y}{y}\approx\sum_ip_i\dfrac{\Delta x_i}{x_i}$.

**Example.** $T_e=[S(1-\alpha)/4\sigma]^{1/4}$ gives $\Delta T/T=\tfrac14\Delta S/S-\tfrac14\Delta\alpha/(1-\alpha)$ ([[CL04 Feedback and Multiple Steady States]]).

**Feedback as a geometric series.** If a response $\Delta T_0$ triggers a secondary response $f\,\Delta T_0$, and that triggers $f^2\Delta T_0$, then $\Delta T=\Delta T_0\sum_nf^n=\Delta T_0/(1-f)$ for $|f|<1$; at $f\ge1$ the series diverges ([[Climate Feedback Factor]]).

Related: [[Planck Sensitivity]], [[Fixed Points and Linear Stability]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
