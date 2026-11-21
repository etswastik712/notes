---
title: TD2213 End-Semester 2026 January Semester - Solved
aliases: [TD2213 past paper, thermodynamics end-sem 2026, TD2213 endsem April 2026, thermo past paper solved]
subject: thermo
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/thermo, type/practice, taught, extra/beyond, src/exam-paper, status/draft, quiz/thermo]
---
# TD2213 End-Semester Examination, 2026 January Semester — Solved

[[Thermodynamics and Statistical Mechanics - Course Map|Course Map]] · revision: [[Thermodynamics Quiz Prep]] · [[Statistical Mechanics Quiz Prep]]

<span class="scope-taught">taught · past paper of this course</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The paper
> *Thermodynamics*, TD2213, end-semester examination of the **2026 January semester** (date of exam **29 April 2026**; 2 hours; 40 marks), instructors **Prof. Arun Venkatnathan** and **Prof. Sunil S. Bhagwat** — the previous run of this course. Source: three phone photos of the paper ([[WhatsApp Image 2026-11-14 at 1.20.19 PM.jpeg|p.1]], [[WhatsApp Image 2026-11-14 at 1.20.19 PM(1).jpeg|p.2]], [[WhatsApp Image 2026-11-14 at 1.20.20 PM.jpeg|p.3, data]]), moved from `~/Downloads` into `physics/thermodynamics-stat-mech/lecture-notes-slides/` on 2026-11-21; read from the images. **No answer key**: every solution below is mine; all numbers are reproduced by `scripts/td2213_endsem2026_numbers.py` with the paper's own data and constants. Section A: Q1, Q2, and **Q3 or Q4**; Section B (Q5–Q11) compulsory.

## The data sheet (paper p.3)
- **Data 1**: $C_p^0=A+BT+CT^2+DT^3$ in cal mol⁻¹ K⁻¹. **Data 2**: acentric factor $\omega=-1.0-\log_{10}\big(P^{\text{sat}}/P_c\big)\big|_{T=0.7T_c}$. **Data 3**: Redlich–Kwong $P=\dfrac{RT}{V-b}-\dfrac{a}{\sqrt T\,V(V+b)}$ with $a=0.42748\,R^2T_c^{2.5}/P_c$, $b=0.08664\,RT_c/P_c$. **Data 4**: $k_B=1.38\times10^{-23}$ J K⁻¹, $h=6.626\times10^{-34}$ J s, 1 cal = 4.1858 J, 1 atm = 1.01325 × 10⁵ Pa = 1.01325 bar, and a handwritten "1 Hz = 3 × 10¹⁰ cm⁻¹" ([!verify] this should read **1 cm⁻¹ ↔ 3 × 10¹⁰ Hz**).
- **Table 1** (used below): methane $M=16.04$, $T_c=191.1$ K, $P_c=45.8$ atm, $\omega=0.011$, $A=4.75$, $B\times10^2=1.2$, $C\times10^5=0.303$, $D\times10^9=-2.63$, $T_b=-161.5$ °C; propane 44.09, 370 K, 42 atm, $\omega=0.153$, $A=-0.966$, $B\times10^2=7.279$, $C\times10^5=-3.755$, $D\times10^9=7.58$, $T_b=-41.97$ °C; water vapour 18.02, 647.4 K, 218.3 atm, $\omega=0.344$; also N₂, O₂, NH₃, CO₂.

## Section A

> [!question] Q1 (5) · Heat flow between two bodies
> Body A at $T_A$ is in contact with body B at $T_B$; heat flows only from A to B at the rate $\dot Q_B\propto(T_A-T_B)$, strictly between A and B. Estimate the rate of entropy change of A and of B.

> [!example]- Solution ([[TH04 The Second Law Carnot Engines and Entropy]])
> Write $\dot Q_B=k(T_A-T_B)$, $k>0$. Each body receives its heat reversibly at its own temperature (internal equilibrium): $\dot S_A=-\dot Q_B/T_A=-k(T_A-T_B)/T_A$, $\dot S_B=+\dot Q_B/T_B=k(T_A-T_B)/T_B$. Total (the isolated pair): $\dot S_{\text{gen}}=k(T_A-T_B)\big(\tfrac1{T_B}-\tfrac1{T_A}\big)=\dfrac{k(T_A-T_B)^2}{T_AT_B}\ge0$, zero only when $T_A=T_B$: heat flowing down a temperature difference generates entropy, as the second law requires.

> [!question] Q2 (5) · LPG cylinder
> An LPG cylinder containing only propane is designed to operate at 25 °C. Calculate the pressure it must withstand if the temperature reaches 45 °C. (Hint: $T_b$ is the boiling point at atmospheric pressure.)

> [!example]- Solution ([[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]])
> The cylinder holds liquid and vapour, so the pressure is the **vapour pressure** at 45 °C. Two points on the vapour-pressure curve from the data: (i) the normal boiling point $T_b=231.18$ K at 1 atm; (ii) from the acentric factor, at $T=0.7T_c=259.0$ K, $P^{\text{sat}}=P_c\,10^{-(1+\omega)}=42\times10^{-1.153}=2.95$ atm. The integrated Clausius–Clapeyron form $\ln P=A-B/T$ through both: $B=\ln(2.95)/(1/231.18-1/259.0)=2330$ K. Then
> $$P^{\text{sat}}(318.15\ \text{K})=\mathbf{15.7\ atm\ (15.9\ bar)},\qquad P^{\text{sat}}(298.15\ \text{K})=9.6\ \text{atm}.$$
> The cylinder must withstand **≈ 16 bar** (about 1.6 times its 25 °C pressure). Check with the Lee–Kesler correlation (not on the paper): 15.2 atm at 45 °C, 9.4 atm at 25 °C — within 4 %.

> [!question] Q3 (5) · Heat capacities of methane, ideal and Redlich–Kwong
> (a) $C_p$ of methane as an ideal gas at 25 °C and 0 bar. (b) $C_v$ likewise. (c) Derive the variation of $C_v$ with molar volume and hence $(\partial C_v/\partial V)_T$ from the RK equation. (d) $C_v$ at 100 bar and 25 °C by RK, and the difference from $C_v$ at 0 bar, taking $V=0.2111$ L mol⁻¹; answer in J mol⁻¹ K⁻¹.

> [!example]- Solution ([[TH03 The Ideal Gas and Adiabatic Processes]], [[TH05 Potentials Maxwell Relations Stability and the Third Law]])
> (a) $C_p^0=4.75+0.012(298.15)+0.303\times10^{-5}(298.15)^2-2.63\times10^{-9}(298.15)^3=8.527$ cal mol⁻¹ K⁻¹ $=\mathbf{35.69}$ J mol⁻¹ K⁻¹.
> (b) Ideal gas: $C_v^0=C_p^0-R=\mathbf{27.38}$ J mol⁻¹ K⁻¹.
> (c) From $dU=T\,dS-P\,dV$ and the Maxwell relation $(\partial S/\partial V)_T=(\partial P/\partial T)_V$: $(\partial U/\partial V)_T=T(\partial P/\partial T)_V-P$. Differentiate with respect to $T$ at fixed $V$: $\big(\partial C_v/\partial V\big)_T=T\big(\partial^2P/\partial T^2\big)_V$. For RK, $(\partial P/\partial T)_V=\frac{R}{V-b}+\frac{a}{2T^{3/2}V(V+b)}$ and $(\partial^2P/\partial T^2)_V=-\frac{3a}{4T^{5/2}V(V+b)}$, so
> $$\Big(\frac{\partial C_v}{\partial V}\Big)_T=-\frac{3a}{4T^{3/2}V(V+b)}.$$
> (d) Integrate from $V=\infty$ (0 bar, ideal) to $V$: $C_v(V)-C_v^0=-\frac{3a}{4T^{3/2}}\int_\infty^V\frac{dV'}{V'(V'+b)}=\frac{3a}{4bT^{3/2}}\ln\Big(1+\frac bV\Big)$. Methane: $a=31.73$ L² atm K^½ mol⁻², $b=0.02967$ L mol⁻¹ ($R=0.08206$ L atm mol⁻¹ K⁻¹). With $V=0.2111$: $\Delta C_v=0.02049$ L atm mol⁻¹ K⁻¹ $=\mathbf{2.08}$ J mol⁻¹ K⁻¹ (numerical integration agrees), so $C_v(100\ \text{bar})=\mathbf{29.46}$ J mol⁻¹ K⁻¹. Consistency: RK at $V=0.2111$, 25 °C gives 98.7 atm = **100.0 bar**, as the paper states.

> [!question] Q4 (5, alternative to Q3) · Steam expansion
> Steam at 30 bar and 550 °C expands adiabatically and reversibly to 7 bar. Estimate the final temperature from the ideal-gas equation of state with $C_p=40$ J mol⁻¹ K⁻¹ independent of temperature. Write the steps to calculate the entropy for a real gas for this process.

> [!example]- Solution ([[TH03 The Ideal Gas and Adiabatic Processes]], [[TH10 Open Systems Mixing and Reacting Gases]])
> Reversible + adiabatic = isentropic: $C_p\ln(T_2/T_1)-R\ln(P_2/P_1)=0$, so $T_2=T_1(P_2/P_1)^{R/C_p}=823.15\times(7/30)^{0.2079}=\mathbf{608\ K\ (335\ °C)}$.
> **Real gas** (state function, so build a path): (1) at $(T_1,P_1)$ compute the **residual entropy** $S^R_1=S-S^{ig}$ from an EOS (e.g. RK with water's $T_c$, $P_c$: solve for $V$, then $S^R/R=\ln\frac{Z(V-b)}V-\frac{a}{2bRT^{3/2}}\ln\frac{V+b}V$); (2) take the ideal gas from $(T_1,P_1)$ to $(T_2,P_2)$: $\Delta S^{ig}=\int C_p^{ig}dT/T-R\ln(P_2/P_1)$; (3) add $S^R_2$ at $(T_2,P_2)$; (4) set $S^R_2+\Delta S^{ig}-S^R_1=0$ and solve for $T_2$ iteratively. (Doing it with RK: $S^R_1=-0.40$ J mol⁻¹ K⁻¹, $T_2=605$ K = 332 °C, 3 K below the ideal estimate; steam tables would be the standard real-gas route.)

## Section B

> [!question] Q5 (2) · Hess's law
> $\Delta_rU$ for S + O₂ → SO₂ (per mole), given $2\mathrm{SO_2+O_2\to2SO_3}$, $\Delta_rU=-200$ kJ mol⁻¹ and $2\mathrm S+3\mathrm O_2\to2\mathrm{SO_3}$, $\Delta_rU=-793$ kJ mol⁻¹.

> [!example]- Solution ([[TH07 Enthalpy Thermochemistry and Calorimetry]])
> Subtract the first from the second: $2\mathrm S+2\mathrm O_2\to2\mathrm{SO_2}$, $\Delta U=-793-(-200)=-593$ kJ; per mole of SO₂: $\mathbf{-296.5}$ **kJ mol⁻¹**. (Energy is a state function, so the equations add like algebra.)

> [!question] Q6 (3) · Chlorine isotopes
> 76 % ³⁵Cl, 24 % ³⁷Cl. Probability of forming ³⁵Cl₂, ³⁷Cl₂, ³⁵Cl³⁷Cl?

> [!example]- Solution ([[SM01 Probability Large Numbers and Information]])
> Independent random pairing: $0.76^2=\mathbf{0.5776}$, $0.24^2=\mathbf{0.0576}$, mixed $2\times0.76\times0.24=\mathbf{0.3648}$ (two orders); they sum to 1. (The same $p^2:2pq:q^2$ as Hardy–Weinberg: [[EE09 Hardy-Weinberg Equilibrium]].)

> [!question] Q7 (3) · Kirchhoff
> $2\mathrm H(g)\to\mathrm H_2$, $\Delta C_p=6.0+2.0\times10^{-3}T$ J K⁻¹, $\Delta H^\circ_{298}=-20.0$ kJ mol⁻¹. At what temperature is $\Delta H^\circ=0$?

> [!example]- Solution ([[TH07 Enthalpy Thermochemistry and Calorimetry]])
> $\Delta H(T)=\Delta H_{298}+\int_{298}^T\Delta C_p\,dT=-20000+6.0(T-298)+1.0\times10^{-3}(T^2-298^2)$. Setting it to zero: $10^{-3}T^2+6T-21877=0$ → $T=\mathbf{2557\ K}$. *(The data are clearly illustrative: the real H–H bond enthalpy is ≈ 436 kJ mol⁻¹, so this is an exercise in Kirchhoff's law, not chemistry.)*

> [!question] Q8 (3) · Vibrational partition function of F₂
> $q_{\text{vib}}=1/(1-e^{-\Theta_{\text{vib}}/T})$; fundamental frequency $2.676\times10^{13}$ Hz. $\Theta_{\text{vib}}$ and $q_{\text{vib}}$ at 25 °C.

> [!example]- Solution ([[SM03 The Canonical Ensemble]])
> $\Theta_{\text{vib}}=h\nu/k_B=6.626\times10^{-34}\times2.676\times10^{13}/1.38\times10^{-23}=\mathbf{1285\ K}$ (wavenumber 892 cm⁻¹). $q_{\text{vib}}=1/(1-e^{-1285/298.15})=1/(1-0.0135)=\mathbf{1.0136}$: almost all molecules in the ground vibrational level (zero of energy at the ground state).

> [!question] Q9 (4) · Derive $U=\langle E\rangle=k_BT^2(\partial\ln Q/\partial T)$
> with $\langle E\rangle=\sum_ip_i\epsilon_i$, $p_i=e^{-\beta\epsilon_i}/Q$, $\beta=1/k_BT$.

> [!example]- Solution ([[SM03 The Canonical Ensemble]])
> $Q=\sum_ie^{-\beta\epsilon_i}$, so $\dfrac{\partial Q}{\partial\beta}=-\sum_i\epsilon_ie^{-\beta\epsilon_i}$ and $\langle E\rangle=\dfrac1Q\sum_i\epsilon_ie^{-\beta\epsilon_i}=-\dfrac1Q\dfrac{\partial Q}{\partial\beta}=-\dfrac{\partial\ln Q}{\partial\beta}$. With $\beta=1/k_BT$, $\dfrac{\partial}{\partial\beta}=\dfrac{dT}{d\beta}\dfrac{\partial}{\partial T}=-k_BT^2\dfrac{\partial}{\partial T}$, hence $U=\langle E\rangle=k_BT^2\Big(\dfrac{\partial\ln Q}{\partial T}\Big)$ (at fixed volume, i.e. fixed $\epsilon_i$).

> [!question] Q10 (5) · Translational partition function of D₂
> Internal energy and entropy from the translational partition function of a D₂ molecule confined to a 100 cm³ vessel at 25 °C.

> [!example]- Solution ([[SM03 The Canonical Ensemble]], [[SM08 Quantum Ensembles and Identical Particles]])
> $m=4.028$ u $=6.69\times10^{-27}$ kg; thermal wavelength $\Lambda=h/\sqrt{2\pi mk_BT}=0.504$ Å; $q_{\text{trans}}=V/\Lambda^3=10^{-4}/(5.04\times10^{-11})^3=\mathbf{7.8\times10^{26}}$. **Energy**: $U=k_BT^2\,\partial\ln q/\partial T=\tfrac32k_BT=6.17\times10^{-21}$ J per molecule, $\tfrac32RT=\mathbf{3.72}$ **kJ mol⁻¹**. **Entropy** ([!verify] the paper does not say how many molecules): for **one mole** in 100 cm³ (indistinguishable, Sackur–Tetrode) $S=R[\ln(q/N_A)+\tfrac52]=\mathbf{80.4}$ J mol⁻¹ K⁻¹; for a single molecule, $S=k_B(\ln q+\tfrac32)=8.75\times10^{-22}$ J K⁻¹. State which reading you use.

> [!question] Q11 (2+1+2) · Four distinguishable particles
> Four distinguishable particles in six levels with energies 0, 1, 2, 3, 4, 5; total energy 5 units. Find all distributions, the number of microstates of each, the most probable distribution, and show that the energy distribution follows Maxwell–Boltzmann.

> [!example]- Solution ([[TH09 Microstates Macrostates and Multiplicity]], [[SM03 The Canonical Ensemble]])
> Occupations $(n_0,\dots,n_5)$ with $\sum n_i=4$, $\sum in_i=5$; $W=4!/\prod n_i!$:
>
> | distribution (energies of the 4 particles) | $n_0\,n_1\,n_2\,n_3\,n_4\,n_5$ | $W$ |
> |---|---|---|
> | 0,0,1,4 | 2 1 0 0 1 0 | 12 |
> | 0,0,2,3 | 2 0 1 1 0 0 | 12 |
> | 0,1,1,3 | 1 2 0 1 0 0 | 12 |
> | 0,1,2,2 | 1 1 2 0 0 0 | 12 |
> | 0,0,0,5 | 3 0 0 0 0 1 | 4 |
> | 1,1,1,2 | 0 3 1 0 0 0 | 4 |
>
> **6 distributions, 56 microstates** (check: the number of ways to give 5 quanta to 4 distinguishable particles is $\binom{8}{3}=56$). **Most probable**: four distributions **tie** at $W=12$ ([!verify] the question expects one; with so few particles there is no unique maximum — say so). **Boltzmann**: averaging the occupation of each level over all 56 equally likely microstates gives $\bar n=1.50,\,1.07,\,0.71,\,0.43,\,0.21,\,0.07$ for $\epsilon=0..5$: falling roughly geometrically (ratios 0.71, 0.67, 0.60, 0.50), i.e. $\bar n_i\propto e^{-\beta\epsilon_i}$ with $\beta\epsilon\approx0.4$ for the lower levels; the deviation at high levels is the finite-size (energy-cap) effect, which vanishes as $N\to\infty$, when the most probable distribution becomes sharply the Boltzmann one.

## Topic map: where each question is taught
| question | topic | vault |
|---|---|---|
| Q1 | entropy generation in heat flow | [[TH04 The Second Law Carnot Engines and Entropy]] |
| Q2 | vapour pressure, Clausius–Clapeyron, acentric factor | [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] |
| Q3 | ideal-gas $C_p(T)$, Maxwell relation for $(\partial C_v/\partial V)_T$, RK EOS | [[TH03 The Ideal Gas and Adiabatic Processes]], [[TH05 Potentials Maxwell Relations Stability and the Third Law]] |
| Q4 | isentropic ideal gas, residual properties | [[TH03 The Ideal Gas and Adiabatic Processes]], [[TH10 Open Systems Mixing and Reacting Gases]] |
| Q5, Q7 | Hess, Kirchhoff | [[TH07 Enthalpy Thermochemistry and Calorimetry]] |
| Q6 | independent probabilities | [[SM01 Probability Large Numbers and Information]] |
| Q8–Q10 | partition functions, $U=k_BT^2\partial_T\ln Q$, Sackur–Tetrode | [[SM03 The Canonical Ensemble]], [[SM08 Quantum Ensembles and Identical Particles]] |
| Q11 | microstates, multiplicity, Boltzmann distribution | [[TH09 Microstates Macrostates and Multiplicity]] |

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | all questions and the data sheet | photos of the TD2213 end-semester paper, 2026 January semester (29 April 2026), read from the images (`physics/thermodynamics-stat-mech/lecture-notes-slides/WhatsApp Image 2026-11-14 at …`) | taught (past paper) |
> | every solution and number; Lee–Kesler check; RK residual entropy | `scripts/td2213_endsem2026_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] (1) "1 Hz = 3 × 10¹⁰ cm⁻¹" (handwritten on the data sheet) is inverted. (2) Q10 does not state the amount of gas: both readings given. (3) Q11 has a four-way tie for the most probable distribution. (4) Q7's numbers are not physical for H₂ (illustrative Kirchhoff exercise). (5) Q2 assumes the Clausius–Clapeyron line through two points; the paper's data allow no better.
