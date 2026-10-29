---
title: Adiabatic Process and Potential Temperature
subject: thermo
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/thermo, type/concept, extra/book, src/book, status/draft]
---
# Adiabatic Process and Potential Temperature

<span class="scope-extra-book">extra · book</span>

> [!key] Definitions
> An **adiabatic** process exchanges no heat with the surroundings, $\mathrm dq=0$. For an ideal gas this gives Poisson's relations
> $$pV^{\gamma}=\text{const},\qquad Tp^{-\kappa}=\text{const},\qquad\kappa=\frac{R}{c_p}=\frac{\gamma-1}{\gamma}=0.286 .$$
> The **potential temperature** is the temperature a parcel would have if brought adiabatically to $p_0=1000$ hPa:
> $$\theta=T\Big(\frac{p_0}{p}\Big)^{\kappa}.$$

**Derivation.** From the [[First Law of Thermodynamics]] with $\mathrm dq=0$: $c_p\,\mathrm dT=\alpha\,\mathrm dp=RT\,\mathrm dp/p$, so $\mathrm d\ln T=\kappa\,\mathrm d\ln p$, hence $T\propto p^\kappa$ along an adiabat and $\theta$ is constant.

**Entropy link.** Since $\mathrm ds=\mathrm dq/T$, a reversible adiabatic process is **isentropic**, and $s=c_p\ln\theta+\text{const}$. So $\theta$ is *entropy in temperature units*; "mixed layer with uniform $\theta$" means uniform entropy: a statement from the second law ([[Thermodynamics - Course Map]]).

**Examples.** $T=280$ K at 800 hPa ⇒ $\theta=298.4$ K. $T=255$ K at 500 hPa ⇒ $\theta=310.9$ K.

> [!intuition] A pressure-corrected temperature
> $\theta$ removes the cooling that comes merely from rising to lower pressure, as sea-level pressure removes the effect of station height. An adiabatically moving parcel keeps its $\theta$; two parcels with the same $\theta$ have the same "thermal identity". A layer whose $\theta$ rises with height is stable; a thoroughly mixed layer has one $\theta$.

Used for: [[Atmospheric Stability]] ($\partial\theta/\partial z>0$ stable, $N^2=g\,\partial\ln\theta/\partial z$), [[Convective Adjustment]], the tropical moist-neutral state (constant moist potential temperature) in [[CL09 Radiative-Convective Equilibrium]]. See [[Dry Adiabatic Lapse Rate]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Lapse Rate]] (Climate): the dry adiabatic lapse rate $\Gamma_d=g/c_p$ is the adiabatic condition $pV^\gamma=$ const applied to a rising, hydrostatically cooled parcel.
