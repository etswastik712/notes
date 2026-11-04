---
title: Clausius-Clapeyron Relation
subject: thermo
type: concept
scope: [extra-book, extra-beyond]
by: [book]
status: draft
tags: [subject/thermo, type/concept, extra/book, extra/beyond, src/book, status/draft]
---
# Clausius-Clapeyron Relation

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!key] Statement
> The saturation vapour pressure over liquid water rises almost exponentially with temperature:
> $$\frac{\mathrm d\ln e_s}{\mathrm dT}=\frac{L}{R_vT^2}\ \ (\approx6.5\ \%\ \mathrm K^{-1}\text{ at }288\ \mathrm K,\ 7.3\ \%\text{ at }273\ \mathrm K),$$
> with $L=2.5\times10^6$ J kg⁻¹ the latent heat of vaporisation and $R_v=461.5$ J kg⁻¹ K⁻¹. In the atmospheric range this is "~7 % per kelvin" (W&H §3.7.3, Eq. 3.92).

> [!extra-beyond]- 🔵 Extra (beyond): derivation
> At a phase boundary the two phases have equal Gibbs energy, which gives the **Clapeyron equation** $\mathrm dp/\mathrm dT=L/(T\,\Delta v)$ with $\Delta v=v_{\rm vap}-v_{\rm liq}$. For water vapour far below the critical point, $v_{\rm liq}\ll v_{\rm vap}\approx R_vT/e_s$ (ideal gas), so $\mathrm d e_s/\mathrm dT=Le_s/(R_vT^2)$. Integrating with $L$ constant: $e_s(T)=e_0\exp\!\big[\tfrac{L}{R_v}\big(\tfrac1{T_0}-\tfrac1T\big)\big]$.

**Numbers** (Bolton's fit): $e_s(0\,^\circ\mathrm C)=611$ Pa, $e_s(20\,^\circ\mathrm C)=2.34$ kPa, $e_s(30\,^\circ\mathrm C)=4.24$ kPa: nearly a doubling every 10 K.

> [!intuition] The air's holding capacity
> Warm air has a much bigger "vapour budget" than cold air, and the budget grows exponentially, not linearly. Cool a parcel and it quickly hits its limit; the excess condenses and releases latent heat. A 1 K warmer atmosphere holds ~7 % more water vapour, which is why a warming climate gets both a stronger greenhouse feedback (water vapour is a greenhouse gas) and heavier downpours.

Used in: the saturated adiabatic lapse rate and the moist tropical troposphere ([[CL09 Radiative-Convective Equilibrium]], [[Dry Adiabatic Lapse Rate]] vs $\Gamma_s$), the water-vapour feedback with $f\approx0.5$ ([[Climate Feedback Factor]], [[CL04 Feedback and Multiple Steady States]]), runaway greenhouse on Venus ([[Evolution of Earth and Life - Course Map]]). Thermodynamic setting: first-order phase transitions in [[Thermodynamics and Statistical Mechanics - Course Map]]; the sharply nonlinear $e_s(T)$ is also a source of tipping behaviour ([[Bistability and Tipping Points]]).

## Continued in the vault (added 2026-11-04)
- Molar form, boiling point at another pressure (Tutorial 1 Q3), the link to the van 't Hoff equation and Trouton's rule: [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] §5 ([[Trouton's Rule]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Continued in Part II (added 2026-10-30)
- Equal chemical potential in coexisting phases and the grand-ensemble view of coexistence (bimodal $P(N)$, Maxwell construction): [[SM05 The Grand Canonical Ensemble and Chemical Equilibrium]] §8.

## Across subjects
- [[Water-Vapour Feedback]] (Climate): the Clausius-Clapeyron equation $\mathrm d\ln P_s/\mathrm dT=L/R_vT^2$ (about $6.3\%$ per K near 288 K) is the thermodynamic reason that warmer air holds more water vapour, the origin of the water-vapour feedback.
