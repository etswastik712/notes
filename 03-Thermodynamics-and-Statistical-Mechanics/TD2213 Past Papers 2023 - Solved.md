---
title: TD2213 Past Papers 2023 - Solved
aliases: [TD2213 2023, thermodynamics midsem 2023, thermodynamics endsem 2023, thermodynamics quizzes 2023]
subject: thermo
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/thermo, type/practice, taught, extra/beyond, src/exam-paper, status/draft, quiz/thermo]
---
# TD2213 Past Papers 2023 (January Semester): Quizzes, Mid-sem and End-sem, Solved

[[Thermodynamics and Statistical Mechanics - Course Map|Course Map]] · [[Thermodynamics Quiz Prep]] · other years: [[TD2213 End-Semester 2021 - Solved|2021]] · [[TD2213 Past Papers 2022 - Solved|2022]] · [[TD2213 Past Papers 2024 - Solved|2024]] · [[TD2213 Past Papers 2025 - Solved|2025]] · [[TD2213 End-Semester 2026 January Semester - Solved|2026]]

<span class="scope-taught">taught · past papers (Chaudhury, Musthafa)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> All are scans from the Drive **Question Paper Archive → Sem-3 → Thermodynamics (sem 4)**, downloaded 2026-11-22:
> - **Quiz 1**: 06 Feb 2023, [[Thermodynamics_Quiz1_Jan23.pdf]].
> - **Quiz 2**: Spring 2023, [[Thermodynamics_Quiz2_Jan23.pdf]].
> - **Mid-sem**: 18 Feb 2023, 40 marks, [[Thermodynamics_Midsem_Jan23_Srabanti-Musthafa.pdf]].
> - **End-sem**: 25 Apr 2023, 40 marks, [[Thermodynamics_Endsem_Jan23_Srabanti-Musthafa.pdf]].
>
> No keys exist; the solutions are mine. Numbers: `scripts/td_qp_archive_numbers.py`.

## Quiz 1 (06 Feb 2023)
> [!example]- Answers ([[TH02 Work Heat and the First Law]], [[TH03 The Ideal Gas and Adiabatic Processes]])
> 1. **$C_{p,m}-C_{V,m}$.** Start from $C_P-C_V=\big[(\partial U/\partial V)_T+P\big](\partial V/\partial T)_P$. For an ideal gas, $(\partial U/\partial V)_T=0$ and $(\partial V/\partial T)_P=R/P$, so the difference is **R**: the extra heat at constant P pays for the expansion work. For solids, α is tiny, so $C_P\approx C_V$ (the exact relation is $TV\alpha^2/\kappa_T$).
> 2. **$\Delta U=q_V$ is not a contradiction.** It holds only on a constant-volume path with no other work. U remains a state function; q happens to equal ΔU on that one path.
> 3. **van der Waals, PV against P.** Expanding at low P, $Z\approx1+(b-a/RT)P/RT$.
>    - For **H₂ and He**, a is very small, so $b>a/RT$ and Z rises with P: repulsion dominates (they are above their Boyle temperatures).
>    - For most other gases at room temperature, Z first dips: attraction dominates.
> 4. **P is a state function.** With $P=\frac{RT}{V-b}-\frac a{V^2}$:
>    $$\frac{\partial}{\partial V}\Big(\frac{\partial P}{\partial T}\Big)_V=-\frac R{(V-b)^2}=\frac{\partial}{\partial T}\Big(\frac{\partial P}{\partial V}\Big)_T.$$
>    The mixed partial derivatives are equal, so $dP$ is exact.
> 5. **Kinetic energy of two gases.** $KE=\tfrac32PV$.
>    - A: $1.5\times1.3\times5.750$ L atm $=$ **1136 J**.
>    - B: $1.5\times1\times7.475$ L atm $=$ **1136 J**, the same.
>
>    Same n and T give the same KE, whatever the molar mass.

## Quiz 2 (Spring 2023)
> [!example]- Answers ([[SM06 Entropy Information and the Arrow of Time]], [[SM03 The Canonical Ensemble]])
> 1. **Dipoles.** S = 1.386k without the field and 1.228k with it, so the system becomes **more ordered** ([[TD2213 End-Semester 2021 - Solved|2021]] Q1).
> 2. **A particle drops from level 2 to level 1.**
>    - System: $\Delta S=k\ln\frac{n_2}{n_1+1}\approx k\ln\frac{n_2}{n_1}$.
>    - Reservoir: $\Delta S=\frac{\varepsilon_2-\varepsilon_1}T$.
>
>    Details in 2021 Q4.
> 3. **Two dice.** One is standard; the other has three faces with 0 spots and three with 6. Then Y = (1…6) + (0 or 6), so **P(Y = k) = 1/12 for k = 1, …, 12**: a flat distribution.
> 4. **Free expansion in an isolated chamber.** (a) Ideal gas: **T unchanged**. (b) Real gas: **T usually drops**, because work is done against the intermolecular attractions.

## Mid-semester (18 Feb 2023)
> [!example]- Q1–Q5 ([[TH03 The Ideal Gas and Adiabatic Processes]], [[TH07 Enthalpy Thermochemistry and Calorimetry]])
> 1. Ar and He at 27 °C:
>    - (a) Same RMS speed: **false**, since $v_{rms}=\sqrt{3RT/M}$ and Ar is slower by $\sqrt{10}$.
>    - (b) Same average kinetic energy: **true**, $\tfrac32kT$ for both.
> 2. **Why one heat capacity for solids.** Solids barely expand ($C_P-C_V=TV\alpha^2/\kappa_T$ is tiny), so $C_P\approx C_V$.
> 3. **Can we tell whether ΔU came from heat or work? No.** U is a state function; the split into q and w depends on the path and is not recorded in the state.
> 4. **Fast processes are nearly adiabatic.** Heat transfer needs time (conduction is slow), while work is done as fast as the boundary moves.
> 5. **Heat of vaporisation ≠ ΔU.** At constant P the heat is ΔH. Part of it is the expansion work $P\Delta V\approx RT$ per mole, so $\Delta U=\Delta H-P\Delta V$.

> [!example]- Q6–Q12 ([[TH04 The Second Law Carnot Engines and Entropy]], [[TH05 Potentials Maxwell Relations Stability and the Third Law]])
> 6. **Joule–Thomson expansion of N₂, 6.0 → 2.0 MPa at 573 K**, with $\mu_{JT}=0.140-2.533\times10^{-2}P$ (K/MPa):
>    $$\Delta T=\int_{6}^{2}\mu\,dP=-0.56+0.405=\mathbf{-0.155\ K},$$
>    so $T_f\approx$ **572.85 K**.
> 7. **Crystallisation despite ΔS_sys < 0.** The latent heat released raises the entropy of the surroundings by $|\Delta H|/T$, which exceeds $|\Delta S_{sys}|$ below the melting point. Equivalently, $\Delta G=\Delta H-T\Delta S<0$.
> 8. **Engine with a 300 K source and a "−200 K" sink.** $\eta=1-T_c/T_h=1+200/300=1.67>1$, which is impossible. A negative absolute temperature exists only for systems with bounded spectra (spins), and such a system is *hotter* than any positive temperature, so it cannot act as the cold sink. The question is a trap; the Carnot formula does not apply. [!verify] The intended answer.
> 9. **Adiabatic against isothermal, same initial and final pressures.** The isotherm ends at a larger V; the adiabat is steeper and lower. The isothermal work is larger in magnitude: same logic as [[TD2213 Past Papers 2022 - Solved|2022]] Q12(ii).
> 10. **$C_V$ for $V=RT/P+aT^2$, with $C_P=A+BT+DP$.**
>     - $(\partial V/\partial T)_P=R/P+2aT$ and $(\partial V/\partial P)_T=-RT/P^2$.
>     - Hence $C_P-C_V=-T\dfrac{(\partial V/\partial T)_P^2}{(\partial V/\partial P)_T}=\dfrac{(R+2aTP)^2}{R}$.
>     - So $C_V=A+BT+DP-\dfrac{(R+2aTP)^2}{R}$.
> 11. **$C_P=20.17+0.3665T$, 25 → 200 °C, 1 mol.**
>     - $\Delta H=\int C_PdT=$ **28.26 kJ**.
>     - $\Delta U=\Delta H-R\Delta T=$ **26.81 kJ** (ideal gas, so U and H depend on T only).
>
>     (a) Constant P: $q=\Delta H=$ 28.26 kJ, $w=-R\Delta T=$ −1.45 kJ. (b) Constant V: $q=\Delta U=$ 26.81 kJ, w = 0. ΔU and ΔH are the same in both cases.
> 12. **Mountains: wet windward, dry leeward (Foehn).** Air forced up the windward side expands adiabatically and cools. Once saturated, its water condenses and rains out, while latent heat release makes it cool only at the moist rate. Descending the leeward side, the now-dry air is compressed adiabatically and warms at the dry rate (~9.8 K/km). It arrives warmer and drier than at the same height on the windward side: a rain shadow and arid land in region B. ([[CL09 Radiative-Convective Equilibrium]])

## End-semester (25 Apr 2023)
> [!example]- Q1–Q6
> 1. **2 mol, isothermal, 100 → 300 L at 300 K (irreversible).**
>    - $\Delta S_{sys}=nR\ln3=$ **18.3 J/K**. S is a state function, so the irreversibility does not matter.
>    - $\Delta G=-nRT\ln3=$ **−5.48 kJ**.
> 2. **Disulfide pairings** of n cysteines: **(n−1)!!** ([[TD2213 End-Semester 2021 - Solved|2021]] Q7).
> 3. **$\mu_{JT}$ with Jacobians.**
>    $$\mu_{JT}=\Big(\frac{\partial T}{\partial P}\Big)_H=-\frac{(\partial H/\partial P)_T}{C_P}=-\frac{V-T(\partial V/\partial T)_P}{C_P}=\frac V{C_P}(T\alpha-1).$$
> 4. **A leap year with 52 Sundays.** A leap year is 52 weeks plus 2 extra days. Of the 7 possible pairs of extra days, 2 contain a Sunday. So P(53 Sundays) = 2/7 and **P(only 52 Sundays) = 5/7**.
> 5. **Joule coefficient** for the van der Waals gas:
>    $$\Big(\frac{\partial T}{\partial V}\Big)_U=-\frac1{C_V}\Big[T\Big(\frac{\partial P}{\partial T}\Big)_V-P\Big]=-\frac{a}{C_VV^2}<0.$$
> 6. **Spontaneity at low or high T.** (i) PCl₃ + Cl₂ → PCl₅: ΔH < 0 and ΔS < 0 (2 mol of gas → 1), so it is **spontaneous at low T**. (ii) H₂O(g) + ½O₂ → H₂O₂(g): ΔH > 0 and ΔS < 0, so it is **never spontaneous**. ([[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]])

> [!example]- Q7–Q11 ([[TH09 Microstates Macrostates and Multiplicity]], [[TH10 Open Systems Mixing and Reacting Gases]])
> 7. **Two lattices, green and red particles.**
>    - (a) $W_A=\binom Nn\binom Mm$.
>    - (b) With the colours distinguishable and all sites open: $W_B=\binom{N+M}{n+m}$.
>    - (c) With N = M, n = m, Stirling at leading order gives $\ln\binom{2N}{2n}=2\ln\binom Nn$, so $W_A/W_B\approx1$. Only the subleading (√N) terms differ: e.g. N = 1000, n = 300 gives $\ln(W_B/W_A)=3.2$.
>    - (d) **B has the greater entropy**, but $\Delta S=k\ln(W_B/W_A)$ is **not extensive**. It is O(ln N), negligible per particle. Mixing two identical compositions produces no thermodynamic entropy, a version of the Gibbs paradox.
> 8. **Dimer on a lattice of V sites.**
>    - Dimer: V − 1 adjacent placements at energy −ε, so $F_{dimer}=-\varepsilon-kT\ln(V-1)$.
>    - Dissociated: about $V^2/2$ placements at energy 0, so $F_{diss}\approx-kT\ln(V^2/2)$.
>    - The equal-free-energy temperature $T_0=\varepsilon/[k\ln(V/2)]$ is asked in [[TD2213 Past Papers 2025 - Solved|2025]] ES Q5.
> 9. **Rolling for a 2**: **k = 7** (2021 Q3).
> 10. **The two engines on T–S diagrams**: $\eta_A=1-T_2/T_1$ (Carnot) is larger than $\eta_B=(T_1-T_2)/(T_1+T_2)$ (2021 Q2).
> 11. **Dipoles**: as in Quiz 2 Q1.

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | questions | the four scans above (Drive QP archive, 2026-11-22) | taught (past papers) |
> | numbers | `scripts/td_qp_archive_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] The intended reading of MS Q8 (the negative-temperature sink).
