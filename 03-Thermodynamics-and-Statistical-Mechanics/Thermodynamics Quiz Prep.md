---
title: Thermodynamics Quiz Prep
aliases: [TD2213 quiz prep, thermo quiz, Tutorial 1 and 2 quiz, TH quiz prep]
subject: thermo
type: moc
scope: [taught]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/thermo, type/moc, taught, src/lecture-notes, src/own-notes, status/draft, quiz/thermo, quiz/th-tut1, quiz/th-tut2, quiz/th-background]
---
# Thermodynamics Quiz Prep (TD2213 Tutorials 1 and 2)

◀ [[Thermodynamics and Statistical Mechanics - Course Map|Course Map]] · chapters [[TH07 Enthalpy Thermochemistry and Calorimetry|TH07]] · [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries|TH08]] · background [[TH02 Work Heat and the First Law|TH02]] · [[TH04 The Second Law Carnot Engines and Entropy|TH04]] · [[TH05 Potentials Maxwell Relations Stability and the Third Law|TH05]]

<span class="scope-taught">taught · in syllabus (the two tutorial sheets)</span>

> [!warning] What this page covers (written 2026-11-12 for the quiz on 2026-11-13)
> **Scope: TD2213 Tutorial 1 (Q1–Q4) and Tutorial 2 (Q1–Q6)** and the topics they rest on. The sheets: [[TD2213_Tutorial1.pdf]], [[Thermodynamics_Tutorial_2_Questions.pdf]]; the instructor's answers: [[TD2213_Tutorial1_Questions_Answers.pdf]], [[TDD213_Tutorial_2_Answers.pdf]] (all read in full). **Tutorial 3 and the post-midsem lectures (open systems, mixing, reacting gases: [[TH10 Open Systems Mixing and Reacting Gases]]) are *not* in this scope** unless your quiz says so. Every number below was recomputed (`scripts/th_tutorial_numbers.py`, `scripts/quiz_numbers.py`).

> [!tip] How the tags work
> Every note and section related to these tutorials carries a tag. In Obsidian open the search pane and type **`tag:#quiz/th-tut1`** (Tutorial 1), **`tag:#quiz/th-tut2`** (Tutorial 2), **`tag:#quiz/th-background`** (the first/second-law prerequisites) or **`tag:#quiz/thermo`** (all). The tag is on the chapter's front matter, on each tutorial question's worked example, on the relevant section headings (TH07 §1, §2.2, §3, §4, §5; TH08 §1–§5) and on the concept notes listed in §7. #quiz/th-tut1 #quiz/th-tut2

## 1. Question map: where each tutorial question is solved

| Q | Topic | Formula | Answer (instructor) | Solved in |
|---|---|---|---|---|
| **T1 Q1** #quiz/th-tut1 | $\Delta H$ from $\Delta U$ at constant $P$ | $\Delta H=\Delta U+P(V_2-V_1)$, $1$ bar L $=100$ J | $\Delta U=2.5$ kJ, $2$ bar, $3\to8$ L: **$3.5$ kJ** | [[TH07 Enthalpy Thermochemistry and Calorimetry]] §1 |
| **T1 Q2** #quiz/th-tut1 | Gibbs–Helmholtz: $\Delta G^\circ/T$ at another $T$ | $\dfrac{\Delta G_2}{T_2}=\dfrac{\Delta G_1}{T_1}+\Delta H\Big(\dfrac1{T_2}-\dfrac1{T_1}\Big)$ | $-50$ kJ (25 °C), $-80$ kJ, 500 °C: **$-2.85$ J K⁻¹mol⁻¹** ($-2.82$ with 298 and 773 K); *the sheet says $-3.1$: a rounding slip* | [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] §4.1 |
| **T1 Q3** #quiz/th-tut1 | Clausius–Clapeyron: new boiling point | $\ln\dfrac{P_2}{P_1}=-\dfrac{\Delta H_{\rm vap}}R\Big(\dfrac1{T_2}-\dfrac1{T_1}\Big)$ | $80$ °C, $40$ kJ/mol, $P\times1.25$: **$359.0$ K $=85.9$ °C** ($+5.9$ K); *the sheet says $88.2$ °C: an arithmetic slip* | TH08 §5 |
| **T1 Q4** #quiz/th-tut1 | Entropy generation $>0$ for heat flow A→B | $\delta S_{\rm gen}=\delta Q\Big(\dfrac1{T_B}-\dfrac1{T_A}\Big)$; rate form $\dot S_{\rm gen}=\dfrac{h(T_A-T_B)^2}{T_AT_B}\ge0$ | proof; $1000$ J, 500 K→300 K: $1.333$ J K⁻¹ | TH08 §2 (both forms) |
| **T2 Q1** #quiz/th-tut2 | Kirchhoff's law (HCl) | $\Delta_rH(T_2)=\Delta_rH(T_1)+\Delta_rC_p(T_2-T_1)$ | $-120$ kJ, $\Delta C_p=+25$, $298\to350$ K: **$-118.7$ kJ/mol** | TH07 §4 |
| **T2 Q2** #quiz/th-tut2 | $K$ and $\Delta S^\circ$ give $\Delta H^\circ$ (ATPase) | $\Delta G^\circ=-RT\ln K$, $\Delta H^\circ=\Delta G^\circ+T\Delta S^\circ$ | $K=0.295$, $\Delta S^\circ=-45.0$: $\Delta G^\circ=+3.02$, **$\Delta H^\circ=-10.4$ kJ/mol** | TH08 §3.1–3.3 |
| **T2 Q3** #quiz/th-tut2 | Hess cycle: hydration of Mg²⁺ | $\Delta_{\rm sol}H=\Delta_{\rm latt}H+\Delta_{\rm hyd}H({\rm Mg^{2+}})+2\Delta_{\rm hyd}H({\rm Cl^-})$ | $-155=2526+x+2(-381)$: **$x=-1919$ kJ/mol** | TH07 §3.1 |
| **T2 Q4** #quiz/th-tut2 | Kirchhoff with data (water-gas) | $\Delta_rH^\circ=\sum\Delta_fH^\circ$(prod)$-\sum$(react); $\Delta_rC_p=\sum C_p-\sum C_p$ | **$+131.29$ kJ/mol (298 K), $+132.56$ (378 K)**; $\Delta_rC_p=+15.857$ | TH07 §4 |
| **T2 Q5** #quiz/th-tut2 | Bomb calorimetry (benzoic acid) | $q=C\Delta T$, $\Delta_cU=-q/n$, $\Delta_cH=\Delta_cU+\Delta n_gRT$ | $q=15.0$ kJ; **$\Delta_cU=-3664$**, $\Delta_cH=-3665$ kJ/mol ($\Delta n_g=-\tfrac12$) | TH07 §5.1 |
| **T2 Q6** #quiz/th-tut2 | Coffee-cup calorimetry (neutralisation) | $q=mc\Delta T$, $\Delta H=-q/n$ | $2.80$ kJ; **$-56.0$ kJ/mol** | TH07 §5.2 |

> [!verify] The two slips on the instructor's Tutorial 1 answer sheet (do not copy them)
> **Q2:** the sheet rounds $-0.1678+0.1647$ to $-0.0031$ kJ K⁻¹mol⁻¹ ("$-3.1$ J K⁻¹mol⁻¹"); the unrounded terms $-0.167785+0.164963$ give $-0.002822$ → **$-2.82$** (298/773 K) or **$-2.85$** (298.15/773.15 K). **Q3:** the same formula and inputs give $T_2=359.03$ K $=85.9$ °C, not $361.3$ K $=88.2$ °C (that would need $\Delta H_{\rm vap}\approx29$ kJ/mol). If a key or a classmate shows $-3.1$ or $88.2$, the method is right and the arithmetic is not. Both are flagged in TH08.

## 2. Formulas to know cold
> [!key] First law and enthalpy (TH02, TH07 §1–§2) #quiz/th-tut1 #quiz/th-tut2
> - $H=U+PV$; constant $P$: $\Delta H=q_P=\Delta U+P\Delta V$. Constant $V$: $\Delta U=q_V$. **1 bar L $=100$ J.**
> - $\Delta_rH=\Delta_rU+\Delta n_gRT$ ($\Delta n_g$ counts **gas moles only**: products minus reactants); standard state $1$ bar; $\Delta_fH^\circ=0$ for an element in its standard state.
> - **Hess:** $H$ is a state function; add steps; reverse a step → flip sign; scale a step → scale $\Delta H$. $\Delta_rH^\circ=\sum\nu\Delta_fH^\circ$.
> - **Kirchhoff** (constant $P$, no phase change, $\Delta C_p$ constant): $\Delta_rH(T_2)=\Delta_rH(T_1)+\Delta_rC_p(T_2-T_1)$, $\Delta_rC_p=\sum\nu C_{p,m}$.
> - **Calorimetry:** $q_{\rm released}=-C_{\rm cal}\Delta T$ (bomb, constant $V$, gives $\Delta U$); $q=mc\Delta T$ (cup, constant $P$, gives $\Delta H$); molar quantity $=-q/n$ (moles of the limiting reagent).

> [!key] Second law and Gibbs energy (TH04, TH08) #quiz/th-tut1 #quiz/th-tut2
> - $G=H-TS$; constant $T,P$: $\Delta G<0$ spontaneous, $\Delta S_{\rm universe}=-\Delta G/T$; $T^*=\Delta H/\Delta S$.
> - **Entropy generation:** $\delta S_{\rm gen}=\delta Q\,\dfrac{T_A-T_B}{T_AT_B}>0$ for $T_A>T_B$; finite bodies $S_{\rm gen}=C_A\ln\frac{T_f}{T_A}+C_B\ln\frac{T_f}{T_B}\ge0$ (Jensen).
> - $\Delta G=\Delta G^\circ+RT\ln Q$; **$\Delta G^\circ=-RT\ln K$** ($K$ dimensionless; pressures over $P^\circ=1$ bar).
> - **Gibbs–Helmholtz:** $\dfrac{\partial(G/T)}{\partial T}=-\dfrac H{T^2}$; integrated at constant $\Delta H$: $\dfrac{\Delta G_2}{T_2}-\dfrac{\Delta G_1}{T_1}=\Delta H\Big(\dfrac1{T_2}-\dfrac1{T_1}\Big)$.
> - **van 't Hoff:** $\dfrac{\mathrm d\ln K}{\mathrm dT}=\dfrac{\Delta H^\circ}{RT^2}$; $\ln\dfrac{K_2}{K_1}=-\dfrac{\Delta H^\circ}R\Big(\dfrac1{T_2}-\dfrac1{T_1}\Big)$ (endothermic: $K$ rises with $T$).
> - **Clausius–Clapeyron:** $\dfrac{\mathrm d\ln P}{\mathrm dT}=\dfrac{\Delta_{\rm vap}H}{RT^2}$ (same form as van 't Hoff); **Trouton:** $\Delta_{\rm vap}S=\Delta_{\rm vap}H/T_b\approx85$–$88$ J K⁻¹mol⁻¹.

## 3. Traps and conventions
1. **Units.** kJ versus J (Tutorial 1 Q2 works in kJ then converts to J K⁻¹mol⁻¹); bar L $\to$ J ($\times100$); $R=8.314$ J K⁻¹mol⁻¹.
2. **Temperatures.** Use kelvin in every $1/T$; $273$ versus $273.15$ changes the third significant figure ($-2.82$ vs $-2.85$ in T1 Q2).
3. **$\Delta H$ versus $\Delta U$.** $\Delta n_gRT$ counts only gases; benzoic acid: $\Delta n_g=7-\tfrac{15}2=-\tfrac12$ (liquid water does not count).
4. **Two chloride ions.** In the Mg²⁺ cycle the anion hydration is multiplied by $2$ (T2 Q3); and every step must be written in the direction you traverse it.
5. **Kirchhoff needs** constant $P$, no phase change and (for $\Delta C_p\Delta T$) a constant $\Delta C_p$.
6. **Heat released versus $\Delta H$.** $q$ released $=+$; $\Delta H=-q/n$ is negative for an exothermic reaction. Divide by the moles of the **limiting** reagent.
7. **$K$ is dimensionless**; $\Delta G^\circ$ is for the standard state, $\Delta G$ for the actual mixture.
8. **Gibbs–Helmholtz is for $G/T$, not $G$.** $\Delta G^\circ/T$ at 500 °C is *less* negative than at 25 °C for an exothermic reaction ($-100.6\to-2.85$ J K⁻¹mol⁻¹ in T1 Q2).
9. **Clausius–Clapeyron** is the integrated form with $\ln$; raising $P$ raises $T_b$.
10. **Entropy generation proof.** The direction $T_A>T_B$ comes from the second law (Clausius); the sign of $S_{\rm gen}$ then follows by algebra. In the rate form $h(T_A-T_B)^2/(T_AT_B)\ge0$ positivity is algebraic.
11. **Constant-$C_p$ and constant-$\Delta H$ assumptions** should be **stated** in an answer (they are the "assume" in each question).

## 4. Derivations to write from a blank page
- **Gibbs–Helmholtz:** $H=G+TS$, $S=-(\partial G/\partial T)_P\Rightarrow H=G-T(\partial G/\partial T)_P=-T^2\,\partial(G/T)/\partial T$; integrate with $\Delta H$ constant.
- **Clausius–Clapeyron:** on the coexistence curve $\mathrm dG^v=\mathrm dG^l\Rightarrow V^v\mathrm dP-S^v\mathrm dT=V^l\mathrm dP-S^l\mathrm dT\Rightarrow\dfrac{\mathrm dP}{\mathrm dT}=\dfrac{\Delta H}{T\Delta V}$; ideal vapour, $V^v\gg V^l$: $\dfrac{\mathrm d\ln P}{\mathrm dT}=\dfrac{\Delta H}{RT^2}$.
- **Kirchhoff:** $\Delta_rH=\sum\nu H_m$, $(\partial H/\partial T)_P=C_p\Rightarrow\mathrm d\Delta_rH/\mathrm dT=\Delta_rC_p$.
- **Entropy generation:** $\mathrm dS_A=-\delta Q/T_A$, $\mathrm dS_B=+\delta Q/T_B$, sum $=\delta Q(1/T_B-1/T_A)$; rate form with $\dot Q=h(T_A-T_B)$.
- **$\Delta G^\circ=-RT\ln K$:** $\sum\nu\mu=0$, $\mu_i=\mu_i^\circ+RT\ln a_i$.

## 5. Self-test (answers collapsed; numbers recomputed in `scripts/quiz_numbers.py`)
1. **(T1 Q1 style)** $\Delta U=-1.8$ kJ for a gas compressed at a constant $1.5$ bar from $10$ L to $4$ L. Find $\Delta H$.
2. **(T1 Q2 style)** $\Delta G^\circ(298.15\ \mathrm K)=-30$ kJ mol⁻¹ and $\Delta H^\circ=-60$ kJ mol⁻¹ (constant). Find $\Delta G^\circ/T$, $\Delta G^\circ$ and $K$ at $400$ K.
3. **(T1 Q3 style)** A liquid has $T_b=60$ °C at $1$ atm and $\Delta_{\rm vap}H=30$ kJ mol⁻¹. Find $T_b$ when the pressure falls by $20\%$.
4. **(T1 Q4 style)** $500$ J flows from a $400$ K reservoir to a $250$ K reservoir. Find $S_{\rm gen}$. Then a rate $h=5$ W K⁻¹ between bodies at $450$ K and $300$ K: find $\dot S_{\rm gen}$.
5. **(T2 Q1 style)** $\Delta_rH(298)=-92$ kJ mol⁻¹, $\Delta_rC_p=-20$ J K⁻¹mol⁻¹. Find $\Delta_rH(500\ \mathrm K)$.
6. **(T2 Q2 style)** $K=5.0$ at $298$ K and $\Delta_rS^\circ=-20$ J K⁻¹mol⁻¹. Find $\Delta G^\circ$ and $\Delta H^\circ$.
7. **(T2 Q3 style)** Lattice dissociation $+2000$, enthalpy of solution $-100$, anion hydration $-350$ each (two anions), all in kJ mol⁻¹. Find the cation's hydration enthalpy.
8. **(T2 Q4 style)** $\Delta_rH(298)=-40$ kJ mol⁻¹, $\Delta_rC_p=+3$ J K⁻¹mol⁻¹. Find $\Delta_rH$ at $500$ K.
9. **(T2 Q5 style)** $0.800$ g of a solid ($M=180$ g mol⁻¹, $\Delta n_g=+1$) in a bomb calorimeter, $C=8.50$ kJ K⁻¹, $\Delta T=2.10$ K, $T=298$ K. Find $q$, $\Delta_cU$, $\Delta_cH$.
10. **(T2 Q6 style)** $75$ mL of $1.0$ M HCl and $75$ mL of $1.0$ M NaOH, $\Delta T=6.0$ K, $\rho=1.00$ g mL⁻¹, $c=4.18$ J g⁻¹K⁻¹. Find $\Delta_{\rm neut}H$.
11. **(concept)** For an exothermic reaction, does $\Delta G^\circ/T$ at higher $T$ become more or less negative, and does $K$ rise or fall?
12. **(concept)** What do the Tutorial 1 Q2 and Tutorial 2 Q2 solutions have in common, and which equation links them?

> [!example]- Answers
> 1. $\Delta H=\Delta U+P\Delta V=-1.8+1.5\times(4-10)\times0.1=-1.8-0.9=\mathbf{-2.70}$ kJ.
> 2. $\Delta G^\circ/T=\dfrac{-30000}{298.15}+(-60000)\Big(\dfrac1{400}-\dfrac1{298.15}\Big)=-100.62+51.24=\mathbf{-49.38}$ J K⁻¹mol⁻¹; $\Delta G^\circ(400)=-49.38\times400=\mathbf{-19.75}$ kJ mol⁻¹; $K=e^{19750/(8.314\cdot400)}=\mathbf{380}$.
> 3. $\dfrac1{T_2}=\dfrac1{333.15}-\dfrac{8.314}{30000}\ln0.8$, $T_2=\mathbf{326.4}$ K $=\mathbf{53.3}$ °C (a fall of $6.7$ K).
> 4. $S_{\rm gen}=500\Big(\dfrac1{250}-\dfrac1{400}\Big)=\mathbf{0.750}$ J K⁻¹. Rate: $\dot S_{\rm gen}=\dfrac{5\cdot150^2}{450\cdot300}=\mathbf{0.833}$ W K⁻¹.
> 5. $-92+(-0.020)(202)=\mathbf{-96.04}$ kJ mol⁻¹.
> 6. $\Delta G^\circ=-RT\ln K=-8.314\cdot298\cdot\ln5=\mathbf{-3.99}$ kJ mol⁻¹; $\Delta H^\circ=\Delta G^\circ+T\Delta S^\circ=-3.99+298(-0.020)=\mathbf{-9.95}$ kJ mol⁻¹.
> 7. $\Delta_{\rm sol}H=\Delta_{\rm latt}H+x+2\Delta_{\rm hyd}H({\rm anion})$: $-100=2000+x-700\Rightarrow x=\mathbf{-1400}$ kJ mol⁻¹.
> 8. $-40+0.003\times202=\mathbf{-39.39}$ kJ mol⁻¹.
> 9. $q=8.50\times2.10=\mathbf{17.85}$ kJ; $n=0.800/180=4.44\times10^{-3}$ mol; $\Delta_cU=-17.85/4.44\times10^{-3}=\mathbf{-4016}$ kJ mol⁻¹; $\Delta_cH=\Delta_cU+\Delta n_gRT=-4016.3+2.48=\mathbf{-4013.8}$ kJ mol⁻¹.
> 10. $q=150\times4.18\times6.0=3762$ J; $n=0.075$ mol; $\Delta_{\rm neut}H=-3.762/0.075=\mathbf{-50.2}$ kJ mol⁻¹.
> 11. $\partial(G/T)/\partial T=-H/T^2>0$ for $H<0$: $\Delta G^\circ/T$ becomes **less negative** (item 2: $-100.6\to-49.4$) and $K$ **falls** (van 't Hoff: $\ln(K_2/K_1)=-6.16$, $K_2/K_1=0.0021$ for $298\to400$ K with $-60$ kJ).
> 12. Both use $\Delta G^\circ$ with $\Delta H^\circ$ and $\Delta S^\circ$ or $K$; the link is **$\Delta G^\circ=\Delta H^\circ-T\Delta S^\circ=-RT\ln K$**; T1 Q2 extends it to another $T$ with Gibbs–Helmholtz (van 't Hoff for $K$), T2 Q2 solves for $\Delta H^\circ$ at one $T$.

## 6. If the quiz goes slightly beyond the sheets
The relevant extras already in the vault: **van 't Hoff plots** and the effect of $\Delta C_p$ (TH08 §4.2); **Trouton's rule**, boiling on Everest (TH08 §5); **entropy production of a reaction** (TH08 §6); the **instructor's rate form of T1 Q4** (TH08 §2); **Hess with combustion data** (the propene example), Kirchhoff's assumptions and the **hot-copper-block calorimetry example** (TH07, Continued in the vault); the **water-gas shift and mixing examples** from the post-midsem lectures ([[TH10 Open Systems Mixing and Reacting Gases]]).

## 7. Tag index: every related note
- **Chapters:** [[TH07 Enthalpy Thermochemistry and Calorimetry]] (T1 Q1; T2 Q1, Q3–Q6), [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] (T1 Q2–Q4; T2 Q2), [[TH04 The Second Law Carnot Engines and Entropy]] (Practice 11 = T1 Q4), [[TH09 Microstates Macrostates and Multiplicity]] (Practice 10 = T1 Q4 microscopically), background [[TH02 Work Heat and the First Law]], [[TH05 Potentials Maxwell Relations Stability and the Third Law]], [[TH10 Open Systems Mixing and Reacting Gases]].
- **Concept notes (tagged):** [[Enthalpy]] · [[Reaction Enthalpy]] · [[Standard Enthalpy of Formation]] · [[Hess's Law]] · [[Kirchhoff's Law]] · [[Calorimetry]] · [[Lattice and Hydration Enthalpy]] · [[Heat Capacity]] · [[State Function]] · [[Gibbs Free Energy]] · [[Gibbs-Helmholtz Equation]] · [[Equilibrium Constant]] · [[Van 't Hoff Equation]] · [[Law of Mass Action]] · [[Clausius-Clapeyron Relation]] · [[Trouton's Rule]] · [[Entropy Production]] · [[Second Law of Thermodynamics]] · [[Kelvin and Clausius Statements]] · [[First Law of Thermodynamics]] · [[Internal Energy]] · [[Entropy]] · [[Chemical Potential]].

> [!provenance]- Source map
> | Content | Source |
> |---|---|
> | the ten questions | [[TD2213_Tutorial1.pdf]], [[Thermodynamics_Tutorial_2_Questions.pdf]] |
> | instructor's answers and the two slips | [[TD2213_Tutorial1_Questions_Answers.pdf]], [[TDD213_Tutorial_2_Answers.pdf]] (read in full 2026-11-12) |
> | solutions, derivations, traps | [[TH07 Enthalpy Thermochemistry and Calorimetry]], [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] |
> | self-test variants | mine; `scripts/quiz_numbers.py` |

## 8. Also solved, outside this quiz's scope (tagged `#quiz/th-tut3`)
- **Tutorial 3 (probability and microstates)**, full write-up in [[TH09 Microstates Macrostates and Multiplicity]] ("Tutorial 3 solved in full"): **Q1** dice, two distinguishable fair dice: (a) $P(\text{red even AND blue odd})=\frac14$, (b) $P(\text{red }2\text{ OR blue }5)=\frac{11}{36}$ (AND multiplies, OR subtracts the overlap), (c) $\frac{15}{36}=\frac5{12}$ (mutually exclusive events add). **Q2** $W_{\rm MPD}=\dfrac{N!}{[(N/2)!]^2}$ (two levels, $N_1=N/2$ by Stirling; second derivative $-4/N<0$), $\dfrac{N!}{[(N/M)!]^M}$ for $M$ levels (Lagrange multipliers: equal occupations; $N$ **divisible by $M$**); $\ln W_{\rm MPD}\simeq N\ln M=\ln W_{\rm total}$ but $W_{\rm MPD}/M^N\to0$. **Q3** three distinguishable particles, levels $0..4$, $E=5$: four distributions with $W=6,6,3,3$, **total $18$** (bosons $4$, fermions $2$).
- **The post-midsem lectures** (open-system balances, mixing, reacting gases, the water-gas shift, Haber trade-off): [[TH10 Open Systems Mixing and Reacting Gases]], and the Hess/Kirchhoff/calorimetry examples at the end of [[TH07 Enthalpy Thermochemistry and Calorimetry]].
