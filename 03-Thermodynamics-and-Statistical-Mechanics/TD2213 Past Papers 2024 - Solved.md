---
title: TD2213 Past Papers 2024 - Solved
aliases: [TD2213 2024, thermodynamics midsem 2024, thermodynamics endsem 2024, thermodynamics quiz 2024]
subject: thermo
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/thermo, type/practice, taught, extra/beyond, src/exam-paper, status/draft, quiz/thermo]
---
# TD2213 Past Papers 2024 (January Semester): Quiz, Mid-sem and End-sem, Solved

[[Thermodynamics and Statistical Mechanics - Course Map|Course Map]] · [[Thermodynamics Quiz Prep]] · other years: [[TD2213 End-Semester 2021 - Solved|2021]] · [[TD2213 Past Papers 2022 - Solved|2022]] · [[TD2213 Past Papers 2023 - Solved|2023]] · [[TD2213 Past Papers 2025 - Solved|2025]] · [[TD2213 End-Semester 2026 January Semester - Solved|2026]]

<span class="scope-taught">taught · past papers (Chaudhury, Musthafa)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> From the Drive **Question Paper Archive → Sem-3 → Thermodynamics (sem 4)**, downloaded 2026-11-22.
> - **Quiz**: 06 Feb 2024, [[thermodynamics_quiz 1_2024_compressed.pdf]].
> - **Mid-sem**: 19 Feb 2024, 40 marks, [[thermodynamics_midsem_2024_compressed.pdf]].
> - **End-sem**: 23 Apr 2024, 40 marks, [[Thermodynamics Endsem 2024.pdf]]. Read from the OCR text and the page images; the scan has a student's annotations.
>
> No keys; solutions mine. Numbers: `scripts/td_qp_archive_numbers.py`.

## Quiz (06 Feb 2024)
> [!example]- Answers ([[TH02 Work Heat and the First Law]], [[TH03 The Ideal Gas and Adiabatic Processes]])
> 1. **Adiabatic free expansion of an ideal gas.** There is no external pressure, so w = 0. The process is adiabatic, so q = 0. Hence ΔU = 0, T is unchanged, and ΔH = Δ(U + PV) = nRΔT = 0.
> 2. **Reversible adiabatic process.** $dU=-PdV$ gives $C_VdT=-\frac{RT}VdV$, so $TV^{\gamma-1}$ = const. Substituting $V\propto T/P$ gives $TP^{(1-\gamma)/\gamma}$ = const.
> 3. **dV is exact.** With $V=nRT/P$, $\frac{\partial}{\partial P}\big(\frac{nR}P\big)=-\frac{nR}{P^2}=\frac{\partial}{\partial T}\big(-\frac{nRT}{P^2}\big)$, so the mixed partials agree.
> 4. **Two gases A and B.** KE = 1136 J for both: same n and T give the same KE, whatever the molar mass ([[TD2213 Past Papers 2023 - Solved|2023]] Quiz 1 Q5).
> 5. **van der Waals at high T, fixed P.** The attraction term a/V² becomes negligible next to the kinetic pressure, leaving $P(V-b)=RT$. Repulsion dominates, so Z > 1 (above the Boyle temperature).

## Mid-semester (19 Feb 2024)
> [!example]- Q1–Q4
> 1. **$C_P-C_V$ of water** on either side of 4 °C. $C_P-C_V=TV\alpha^2/\kappa_T$. Because α appears **squared**, the difference is **positive in both ranges**: α < 0 between 0 and 4 °C, α > 0 between 4 and 7 °C. It is exactly **zero at 4 °C** (α = 0). ([[TH05 Potentials Maxwell Relations Stability and the Third Law]])
> 2. **Large a (H₂O) against small a (He).** A large a means strong attractions: larger μ_JT and a higher inversion temperature ($T_{inv}\approx2a/Rb$). So **H₂O cools** on Joule–Thomson expansion. He is above its inversion temperature at room temperature (μ < 0), so it **warms**.
> 3. **Why $C_{p,m}$ depends on T for ethane but not argon.** Ethane has rotational, torsional and vibrational modes that become excited progressively as T rises. Argon is monatomic, with translation only, so $C_P=\tfrac52R$ is constant. ([[SM07 Equipartition the Virial Theorem and Magnetic Systems]])
> 4. **Heat is not a state function.** $q=\Delta U-w$. ΔU is fixed by the end states, but w depends on the path (e.g. reversible against free expansion between the same states), so q does too.

> [!example]- Q5–Q11 ([[TH03 The Ideal Gas and Adiabatic Processes]], [[TH04 The Second Law Carnot Engines and Entropy]])
> 5. **1 mol monatomic gas, reversible adiabatic, 10 → 20 dm³ from 27 °C.**
>    - $T_2=300.15\times(1/2)^{2/3}=189.1$ K.
>    - **q = 0**; **ΔU = w = −1.39 kJ**; **ΔH = −2.31 kJ**.
> 6. **Ar at 1.42 L/mol and 300 K.** van der Waals: $P=\frac{RT}{V-b}-\frac a{V^2}=$ **17.30 bar**. The ideal-gas value is 17.56 bar. P < P_ideal (Z = 0.985), so **attractions dominate**.
> 7. **Isothermal expansion work, real against ideal.** With b neglected: $W_{real}=RT\ln\frac{V_2}{V_1}-a\Big(\frac1{V_1}-\frac1{V_2}\Big)<W_{ideal}$. Part of the energy goes into pulling the molecules apart against their attraction, so less work reaches the surroundings.
> 8. **Derive $dU=dq-PdV$.** Energy conservation gives $dU=dq+dw$. For quasi-static expansion against an external pressure equal to P, $dw=-P\,dV$.
> 9. **Molar entropy change, ideal gas.** $dS=\frac{C_P}TdT-\frac RPdP$, so $\Delta S=C_P\ln\frac{T_2}{T_1}-R\ln\frac{P_2}{P_1}=0.59+19.14=$ **19.74 J/(mol·K)**.
> 10. **1 kg water at 70 °C mixed with 3 kg at 30 °C.** $T_f=40$ °C, and $\Delta S=4185\big[\ln\frac{313.15}{343.15}+3\ln\frac{313.15}{303.15}\big]=$ **+24.6 J/K**.
> 11. **Enthalpy and Gibbs energy.** H = U + PV and G = H − TS. Enthalpy is the heat exchanged at constant P (with only PV work). From $dH=TdS+VdP$, the Maxwell relation is $\Big(\frac{\partial T}{\partial P}\Big)_S=\Big(\frac{\partial V}{\partial S}\Big)_P$. ([[TH07 Enthalpy Thermochemistry and Calorimetry]])

## End-semester (23 Apr 2024)
> [!example]- Q1–Q5
> 1. **Show $\Big(\frac{\partial H}{\partial V}\Big)_T=-V^2\Big(\frac{\partial P}{\partial T}\Big)_V\Big(\frac{\partial(T/V)}{\partial V}\Big)_P$.**
>    - Expand the right side: $-V^2(\partial P/\partial T)_V\big[-T/V^2+\tfrac1V(\partial T/\partial V)_P\big]=T(\partial P/\partial T)_V-V(\partial P/\partial T)_V(\partial T/\partial V)_P$.
>    - By the cyclic relation, $(\partial P/\partial T)_V(\partial T/\partial V)_P=-(\partial P/\partial V)_T$.
>    - So the right side is $T(\partial P/\partial T)_V+V(\partial P/\partial V)_T$, which is $(\partial H/\partial V)_T$ (from $dH=TdS+VdP$ and a Maxwell relation). ✓
>
>    [!verify] Read through the student's annotations.
> 2. **Birthday problem, 25 people**: **0.569**.
> 3. **Dipoles**: 1.386k → 1.228k, more ordered ([[TD2213 End-Semester 2021 - Solved|2021]] Q1).
> 4. **Brayton cycle**: two isentropes and two isobars. On a T–S diagram the isobars are exponential curves rising with S. The efficiency is $\eta=1-\frac{T_1}{T_2}=1-\Big(\frac{P_{low}}{P_{high}}\Big)^{(\gamma-1)/\gamma}$, with heat absorbed on the high-P isobar and rejected on the low-P one. ([[TH04 The Second Law Carnot Engines and Entropy]])
> 5. **Body brought to a reservoir's temperature**: $\Delta S_{univ}=C_P[\ln x-1+1/x]>0$ ([[TD2213 Past Papers 2022 - Solved|2022]] Q5).

> [!example]- Q6–Q11
> 6. **50 g ice at 0 °C, warmed to 20 °C by a reservoir at 20 °C.**
>    - Ice: $\Delta S=\frac{50\times336}{273.15}+50\times4.19\ln\frac{293.15}{273.15}=61.5+14.8=$ **76.3 J/K**.
>    - Reservoir: it gives up 20.99 kJ, so $\Delta S=-71.6$ J/K.
>    - **Universe: +4.7 J/K.**
> 7. **A fair die rolled three times.** (a) A 5 exactly twice: $3(\tfrac16)^2\tfrac56=$ **0.069**. (b) At least two 5s: **2/27 = 0.074**. ([[SM01 Probability Large Numbers and Information]])
> 8. **Four-monomer polymer.** The figure shows **1 compact conformation**, with one sticking contact at energy −ε, and **4 open conformations** at energy 0.
>    - (a) $F_c=-\varepsilon$ and $F_o=-kT\ln4$.
>    - (b) For open → compact: **ΔF = −ε + kT ln 4**, **ΔU = −ε**, **ΔS = −k ln 4**. Collapse is favoured when $T<\varepsilon/(k\ln4)$.
>
>    [!verify] The count of open conformations is read from a small figure; it is the standard example in Dill & Bromberg, *Molecular Driving Forces*. ([[SM03 The Canonical Ensemble]])
> 9. **$G=RT\ln\frac{aP}{(RT)^{5/2}}$.**
>    - $S=-\partial G/\partial T=-R\ln\frac{aP}{(RT)^{5/2}}+\tfrac52R$.
>    - $H=G+TS=\tfrac52RT$, so **$C_P=\tfrac52R$**: a monatomic ideal gas.
> 10. **U(V) for a van der Waals gas**: $(\partial U/\partial V)_T=a/V^2\ne0$, so $U=U_{ideal}(T)-a/V$ ([[TD2213 Past Papers 2022 - Solved|2022]] Q10).
> 11. **2 mol, 100 → 300 L at 300 K, with R = 1.98 cal/(mol K).** **ΔS = 4.35 cal/K** and **ΔG = −1.31 kcal**, the same as [[TD2213 Past Papers 2023 - Solved|2023]] ES Q1 in calories.

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | questions | the three files above (Drive QP archive, 2026-11-22) | taught (past papers) |
> | numbers | `scripts/td_qp_archive_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] The ES Q1 reading and the ES Q8 degeneracies.
