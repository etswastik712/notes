---
title: TD2213 Past Papers 2025 - Solved
aliases: [TD2213 2025, thermodynamics midsem 2025, thermodynamics endsem 2025, thermodynamics quizzes 2025]
subject: thermo
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/thermo, type/practice, taught, extra/beyond, src/exam-paper, status/draft, quiz/thermo]
---
# TD2213 Past Papers 2025 (January Semester): Quizzes, Mid-sem and End-sem, Solved

[[Thermodynamics and Statistical Mechanics - Course Map|Course Map]] · [[Thermodynamics Quiz Prep]] · other years: [[TD2213 End-Semester 2021 - Solved|2021]] · [[TD2213 Past Papers 2022 - Solved|2022]] · [[TD2213 Past Papers 2023 - Solved|2023]] · [[TD2213 Past Papers 2024 - Solved|2024]] · [[TD2213 End-Semester 2026 January Semester - Solved|2026]]

<span class="scope-taught">taught · past papers (Srabanti Chaudhury, Sunil Bhagwat)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> From the Drive **Question Paper Archive → Sem-3 → Thermodynamics (sem 4)**, downloaded 2026-11-22.
> - **The whole year in one file:** [[Thermodynamics_QuizzesMidsemEndsem_2025_Srabanti.pdf]] (7 pp.) has Quiz 1, the mid-sem (27 Feb), Quiz 2 (2 Apr) and the end-sem (25 Apr). [[Thermodynamics-All Papers 2025-Srabanti.pdf]] is a second scan of the same papers.
> - **Separate copies:** the end-sem as [[Thermodynamics Endsem.pdf]], the mid-sem as [[Thermodynamics Pg 1 .jpg]] and [[Thermodynamics pg2.jpg]], and Quiz 2 as [[Thermodynamics Quiz 2.pdf]].
> - [[Thermo AnsKey(Last3).pdf]] holds a student's handwritten solutions to mid-sem Q6–Q8. They are checked below.
>
> Numbers: `scripts/td_qp_archive_numbers.py`.

## Quiz 1 (Spring 2025, 20 marks)
> [!example]- Answers ([[TH04 The Second Law Carnot Engines and Entropy]], [[TH05 Potentials Maxwell Relations Stability and the Third Law]], [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]])
> 1. **Adiabatic mixing always produces entropy.** Take equal heat capacities C (per body). The final temperature is $T_f=\frac{T_1+T_2}2$, and $\Delta S=C\ln\frac{T_f^2}{T_1T_2}\ge0$ because the arithmetic mean is at least the geometric mean. Equality holds only if $T_1=T_2$. (For unequal C the same holds by the concavity of ln.)
> 2. **Joule–Thomson coefficient for $(P+a/V^2)V=RT$.**
>    - Differentiate at constant P: $(\partial V/\partial T)_P=\frac R{P-a/V^2}$.
>    - So $\mu_{JT}=\frac1{C_P}\Big[T\Big(\frac{\partial V}{\partial T}\Big)_P-V\Big]=\dfrac{2aV}{C_P(PV^2-a)}$, after substituting $RT=PV+a/V$.
>    - μ > 0 (cooling) whenever $PV^2>a$.
> 3. **$C_P=20.17+0.4001T$, 0 → 100 °C, 1 mol.**
>    - $\Delta H=$ **14.95 kJ** and $\Delta U=\Delta H-R\Delta T=$ **14.11 kJ**.
>    - (a) Constant P: q = ΔH, w = −0.83 kJ. (b) Constant V: q = ΔU, w = 0.
>
>    Same method as [[TD2213 Past Papers 2023 - Solved|2023]] MS Q11.
> 4. **Clausius–Clapeyron**, with $T_b=338.15$ K and $\Delta H_{vap}=12$ kJ/mol: $\ln P=-\frac{\Delta H}R\Big(\frac1{373.15}-\frac1{338.15}\Big)$, so **P(100 °C) ≈ 1.49 atm**. (That ΔH is unusually small for a liquid boiling at 65 °C; the number follows the data given.)
> 5. **P–V phase diagram.** Draw isotherms above, at and below $T_c$:
>    - below $T_c$: flat tie-lines across the liquid–vapour dome;
>    - at $T_c$: the critical isotherm, with an inflection point at the top of the dome;
>    - above $T_c$: hyperbola-like curves.
>
>    ([[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]])

## Mid-semester (27 Feb 2025, 40 marks)
> [!example]- Q1–Q5
> 1. **1 g ice at 0 °C melted and heated to 50 °C** (L = 334 J/g and c = 4.18 J/g K assumed; not given): $\Delta S=\frac{334}{273.15}+4.18\ln\frac{323.15}{273.15}=$ **1.93 J/K**.
> 2. **Heat exchanger.** 45 kg/min of water goes from 60 to 115 °C. The hot gas enters at 225 °C (read as °C) at 90 kg/min.
>    - The energy balance gives a gas outlet temperature of **115 °C**.
>    - $\Delta S=45(4.18)\ln\frac{388.15}{333.15}+90(1.045)\ln\frac{388.15}{498.15}=$ **+5.28 kJ K⁻¹ per minute**.
> 3. **A Carnot engine drives a refrigerator.** The engine takes 750 kJ/min at 1273 K and rejects heat at 300 K: $W=750(1-300.15/1273.15)=573$ kJ/min. A Carnot refrigerator between 263 K and 300 K has COP = 263.15/37 = 7.11.
>    - (i) Maximum heat removed from the cold space: **4077 kJ/min**.
>    - (ii) Total heat to the ambient air: 177 + 4077 + 573 = **4827 kJ/min**.
> 4. **Cells do not violate the second law.** A cell is an **open system**. Its internal order is paid for by exporting more entropy than it creates inside: heat released and disordered waste products, with metabolism fed by low-entropy food and sunlight. $\Delta S_{sys}+\Delta S_{surr}>0$. ([[SM06 Entropy Information and the Arrow of Time]])
> 5. **The cycle shown is the Diesel cycle**: adiabatic compression 1→2, isobaric heat input 2→3, adiabatic expansion 3→4, isochoric rejection 4→1.
>    - $Q_H=C_P(T_3-T_2)$ and $Q_L=C_V(T_4-T_1)$.
>    - $\eta=1-\dfrac{T_4-T_1}{\gamma(T_3-T_2)}$.
>    - On a T–S diagram the isobar and isochore are exponential curves; the isochore is steeper.

> [!example]- Q6–Q8 (and the student's handwritten solutions)
> 6. **Real-gas derivatives.** $(\partial H/\partial P)_T=V-T(\partial V/\partial T)_P$ and $(\partial U/\partial V)_T=T(\partial P/\partial T)_V-P$. Both vanish for an ideal gas.
>    For the Redlich–Kwong equation, $P=\frac{RT}{V-b}-\frac{a}{\sqrt T\,V(V+b)}$, which gives $(\partial U/\partial V)_T=\dfrac{3a}{2\sqrt T\,V(V+b)}$. Its value for N₂ needs a state (V, T) that the sheet does not give. With the formulas on the sheet ($P_c=33.5$ bar, $T_c=126.2$ K): a = 15.8 L² bar K^½ mol⁻², b = 0.0271 L/mol. [!verify] The question's exact target expression is not legible on the scan.
> 7. **Normal boiling point from the acentric factor** ($T_c=250$ K, $P_c=4.0$ MPa, ω = 0.248).
>    - From the definition of ω: $P^{sat}(0.7T_c=175\text{ K})=P_c10^{-(1+\omega)}=$ 0.226 MPa.
>    - Clausius–Clapeyron through this point **and the critical point** gives $\Delta H/R=\ln(P_c/P_{175})/(1/175-1/250)=1676$ K.
>    - Then **T_b ≈ 161.5 K**.
>
>    The student's solution finds the same 0.226 MPa but leaves $T_b$ in terms of an unknown ΔH_vap. The critical point supplies the second point.
> 8. **Residual Gibbs energy and Maxwell's equal-area rule.** At coexistence $G^{liq}=G^{vap}$. Subtracting the two residual expressions gives $\int_{V^{liq}}^{V^{vap}}P\,dV=P^{sat}(V^{vap}-V^{liq})$: the two shaded areas on the P–V loop are equal. ✓ The student's derivation is correct.

## Quiz 2 (2 Apr 2025, 20 marks)
> [!example]- Answers ([[SM03 The Canonical Ensemble]], [[SM07 Equipartition the Virial Theorem and Magnetic Systems]])
> 1. **50 g ice → water at 20 °C**: ΔS_ice = 76.3 J/K and ΔS_univ = 4.7 J/K, as in [[TD2213 Past Papers 2024 - Solved|2024]] ES Q6. **Phase change only**: ΔS_ice = 61.5 J/K and ΔS_univ = 61.5 − 16 800/293.15 = **+4.2 J/K**.
> 2. **Two-state spin.** Aligned: energy 0, moment +μ₀. Anti-aligned: energy 2μ₀B, moment −μ₀.
>    - $Z=1+e^{-2\mu_0B/kT}$.
>    - $p_\parallel=1/Z$ and $p_{anti}=e^{-2\mu_0B/kT}/Z$.
>    - $\langle\mu\rangle=\mu_0\tanh(\mu_0B/kT)$.
> 3. **Perfect de-mixing becomes improbable.** 2V white and 2V black particles fill 4V sites, giving $\binom{4V}{2V}\approx2^{4V}/\sqrt{2\pi V}$ arrangements. Only one of them (or two, counting the mirror image) has all white on one side. $P\approx\sqrt{2\pi V}\,2^{-4V}\to0$ exponentially as V grows. ([[TH09 Microstates Macrostates and Multiplicity]])
> 4. **Dipoles**: as in [[TD2213 End-Semester 2021 - Solved|2021]] Q1.
> 5. **Cysteines**: (n−1)!!, as in 2021 Q7.

## End-semester (25 Apr 2025, 40 marks)
> [!example]- Q1–Q4
> 1. **Entropy along 1 → 0 (isochore) → 2 (isobar).**
>    - $\Delta S=C_V\ln\frac{T_0}{T_1}+C_P\ln\frac{T_2}{T_0}$, with $T_0/T_1=P_2/P_1$ along the isochore.
>    - So $\Delta S=C_P\ln\frac{T_2}{T_1}-(C_P-C_V)\ln\frac{P_2}{P_1}=C_P\ln\frac{T_2}{T_1}-R\ln\frac{P_2}{P_1}$.
>    - On an adiabat, $T_2/T_1=(P_2/P_1)^{R/C_P}$, so $\Delta S=0$ for **any** $C_V$, using only $C_P=C_V+R$.
> 2. **10 kg of water at 90 °C mixed with 2.5 kg at 20 °C.** $T_f=$ **76 °C**, and $\Delta S=$ **+0.184 kJ/K**.
> 3. **Three-bead polymer binding a ligand.** Energy levels: both ligand bonds made (B, the bent form), **0**; one bond broken, **ε** (two ways); no bonds, **2ε**. The 2ε level includes the open linear chain and the unbound bent chain.
>    - Taking degeneracies 1, 2, 2: $Z=1+2e^{-\beta\varepsilon}+2e^{-2\beta\varepsilon}$.
>    - At T → 0, only B is occupied. At T → ∞, each of the 5 states has probability 1/5.
>    - ΔS(∞ − 0) = **k ln 5**.
>    - ⟨E⟩ is 0 at T = 0 and **6ε/5** at T → ∞.
>
>    [!verify] The degeneracies are read from the figure.
> 4. **1 mol ideal gas at 27 °C, reversible isothermal, 10 → 1 bar.**
>    - **q = 5.75 kJ** and **w = −5.75 kJ** (by the system);
>    - **ΔU = ΔH = 0**;
>    - **ΔS = R ln 10 = 19.1 J/K**;
>    - **ΔG = ΔA = −5.75 kJ**.

> [!example]- Q5–Q8
> 5. **Dimer against monomers.** From [[TD2213 Past Papers 2023 - Solved|2023]] ES Q8, set $F_{dimer}=F_{diss}$: $-\varepsilon-kT\ln V\approx-kT\ln(V^2/2)$, which gives **$T_0=\dfrac{\varepsilon}{k\ln(V/2)}$**.
> 6. **Jacobian identity.**
>    $$\Big(\frac{\partial G}{\partial S}\Big)_V=\frac{(\partial G/\partial T)_V}{(\partial S/\partial T)_V}=\frac{T}{C_V}\Big[-S+V\frac{\alpha}{\kappa_T}\Big]=-\frac{ST}{C_V}+\frac{VT\alpha}{\kappa_TC_V}.$$
>    The second step uses $(\partial G/\partial T)_V=-S+V(\partial P/\partial T)_V$ and $(\partial P/\partial T)_V=\alpha/\kappa_T$. [!verify] The sheet's signs appear reversed relative to this result.
> 7. **Residual entropy for a pressure-explicit EOS.** $S-S^{ig}(T,P)=\int_\infty^V\Big[\Big(\frac{\partial P}{\partial T}\Big)_V-\frac RV\Big]dV+R\ln Z$. Everything inside is measurable (P, V, T). For van der Waals, $S-S^{ig}=R\ln\frac{P(V-b)}{RT}$. ([[TH10 Open Systems Mixing and Reacting Gases]])
> 8. **Water vapour at 200 °C and 4 L/mol.**
>    | equation of state | P |
>    |---|---|
>    | ideal gas | **9.71 atm** (9.83 bar) |
>    | van der Waals | **9.44 atm** |
>    | Redlich–Kwong ($a=142.7$ L² bar K^½ mol⁻², $b=0.0211$ L/mol) | **9.48 bar** |

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | all four papers | [[Thermodynamics_QuizzesMidsemEndsem_2025_Srabanti.pdf]] (and the duplicate copies), page images | taught (past papers) |
> | student solutions (MS Q6–Q8) | [[Thermo AnsKey(Last3).pdf]] (handwritten; checked) | student work |
> | numbers | `scripts/td_qp_archive_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] The ice constants assumed in MS Q1. The 225 °C reading in MS Q2. The MS Q6 target. The ES Q3 degeneracies. The ES Q6 sign.
