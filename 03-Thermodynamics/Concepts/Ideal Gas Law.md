---
title: Ideal Gas Law
aliases: [Equation of state, Gas law]
subject: thermo
type: concept
scope: [taught, extra-beyond]
by: [suhas-pre, argha]
status: draft
tags: [subject/thermo, type/concept, taught, extra/beyond, src/suhas-pre, src/argha, status/draft]
---
# Ideal Gas Law

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** $p=\rho RT$, $pV=nR^*T$, $p=n_0k_BT$, Boyle/Charles as special cases, Dalton, $R_d$, $R_v$, virtual temperature (Suhas pre-midsem; Argha L5 sl. 51 for $p=\rho k_BT/m$) · 🔵 **extra:** the kinetic derivation, molecular numbers, how ideal air is

> [!intuition] In one picture
> A handball court: $N$ balls bounce off the walls. Shrink the court and walls are hit more often (Boyle); make the balls faster and each hit is harder *and* more frequent (pressure $\propto T$). The gas law is the arithmetic of that bookkeeping. Squeeze a bicycle pump and the barrel warms: $p$, $V$ and $T$ are locked together.

> [!key] Three equivalent forms
> $$p=\rho RT\ \ (R=R^*/M),\qquad pV=nR^*T,\qquad p=n_0k_BT\ \ (k_B=R^*/N_A).$$
> $R^*=8.3145$ J mol⁻¹ K⁻¹, $k_B=1.381\times10^{-23}$ J K⁻¹, $N_A=6.022\times10^{23}$ mol⁻¹. For dry air $M_d=28.97$ g mol⁻¹, **$R_d=287.0$ J kg⁻¹ K⁻¹**; water vapour $M_w=18.016$, $R_v=461.5$, $\varepsilon=R_d/R_v=0.622$.

- **Special cases:** $T$ fixed ⇒ $pV$ const (Boyle); $p$ fixed ⇒ $V\propto T$ (Charles); $V$ fixed ⇒ $p\propto T$.
- **Mixtures:** Dalton, $p=\sum p_i$, $p_i=x_ip$; mean molar mass $\overline M=\sum x_iM_i$, $R_{\rm mix}=R^*/\overline M$.
- **Moist air:** keep $R_d$ and use the **virtual temperature** $T_v=T(1+0.608\,q)$, because vapour (M = 18) is lighter than dry air ([[Virtual Temperature]]).
- **Numbers:** sea-level density $101325/(287.05\times288.15)=1.225$ kg m⁻³; molecules per m³ $2.55\times10^{25}$ at 288 K, $8.6\times10^{24}$ at 10 km.
- **Kinetic origin** (🔵): $p=\tfrac13n_0m\langle v^2\rangle$ and $\tfrac12m\langle v_x^2\rangle=\tfrac12k_BT$ give $p=n_0k_BT$; rms speed of N₂ at 288 K is 507 m s⁻¹, mean free path ~65 nm.
- **Accuracy** (🔵): molecules occupy ~0.07 % of the volume, so deviations from ideality are ~0.1 % at sea level.

Chapters: [[CL05 Thermodynamic State of the Atmosphere]] (full treatment) and [[CL06 Hydrostatic Balance and Vertical Structure]] (with gravity: $p=p_0e^{-z/H}$, [[Scale Height]], [[Hypsometric Equation]]). Related: [[Atmospheric Composition]], [[Mixing Ratio and Humidity]], [[Thermodynamics - Course Map]] (kinetic theory, statistical mechanics).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
