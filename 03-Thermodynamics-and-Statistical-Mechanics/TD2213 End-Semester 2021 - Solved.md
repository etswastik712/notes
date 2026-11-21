---
title: TD2213 End-Semester 2021 - Solved
aliases: [TD2213 2021 end sem, thermodynamics past paper 2021]
subject: thermo
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/thermo, type/practice, taught, extra/beyond, src/exam-paper, status/draft, quiz/thermo]
---
# TD2213 End-Semester 2021 — Solved

[[Thermodynamics and Statistical Mechanics - Course Map|Course Map]] · the 2026 paper: [[TD2213 End-Semester 2026 January Semester - Solved]] · [[Thermodynamics Quiz Prep]]

<span class="scope-taught">taught · past paper</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The paper
> [[end sem TD2213 2021.pdf]] (2 pp., found on your Google Drive on 2026-11-21, saved to `physics/thermodynamics-stat-mech/lecture-notes-slides/past-papers/`). No date, instructors or answer key on the sheet; read from the text layer and the page images (the figures of Q1–Q2 and the formula of Q6). Three sections; marks in brackets. Solutions mine.

## Section 1 (5 marks each)

> [!example]- Q1 · Dipoles with and without a field ([[SM06 Entropy Information and the Arrow of Time]], [[TH09 Microstates Macrostates and Multiplicity]])
> Directions $n,e,w,s$: without field $p=\tfrac14$ each; with field $p=\tfrac7{16},\tfrac14,\tfrac14,\tfrac1{16}$. Gibbs entropy per molecule $S=-k\sum p_i\ln p_i$.
> (a) $S=k\ln4=\mathbf{1.386\,k}$. (b) $S=-k\big[\tfrac7{16}\ln\tfrac7{16}+2\cdot\tfrac14\ln\tfrac14+\tfrac1{16}\ln\tfrac1{16}\big]=\mathbf{1.228\,k}$ (per mole: 11.53 and 10.21 J mol⁻¹ K⁻¹). (c) $S$ falls: the field makes the system **more ordered**.

> [!example]- Q2 · Two reversible engines on a T–S diagram ([[TH04 The Second Law Carnot Engines and Entropy]])
> In a $T$–$S$ diagram heat $=\int T\,dS$ (area under the path) and the work per cycle is the enclosed area.
> **A** (rectangle: isotherm at $T_1$ from $S_1$ to $S_2$, adiabat down, isotherm at $T_2$ back, adiabat up): $q_{in}=T_1\Delta S$, $q_{out}=T_2\Delta S$: $\eta_A=1-\dfrac{T_2}{T_1}$ — the Carnot engine.
> **B** (triangle: heat absorbed along the straight line from $(S_1,T_1)$ to $(S_2,T_2)$, rejected at $T_2$, then an adiabat): $q_{in}=\tfrac12(T_1+T_2)\Delta S$, $q_{out}=T_2\Delta S$, work $=\tfrac12(T_1-T_2)\Delta S$: $\eta_B=\dfrac{T_1-T_2}{T_1+T_2}$.
> $\eta_A>\eta_B$ (same numerator, smaller denominator): A takes in **all** its heat at the highest temperature, B at temperatures averaging $(T_1+T_2)/2$. Among engines between $T_1$ and $T_2$ the Carnot cycle is the most efficient.

> [!example]- Q3 · Rolling until a 2 appears ([[SM01 Probability Large Numbers and Information]], [[PR01 Counting and the Axioms of Probability]])
> $P(\text{at least one 2 in }k)=1-(5/6)^k\ge\tfrac23\iff(5/6)^k\le\tfrac13\iff k\ge\ln3/\ln1.2=6.03$. So **$k=7$** ($(5/6)^6=0.335$ just misses; $(5/6)^7=0.279$).

> [!example]- Q4 · A particle moves from level 2 to level 1 ([[TH09 Microstates Macrostates and Multiplicity]], [[SM03 The Canonical Ensemble]])
> System: $W=\dfrac{N!}{n_1!\,n_2!}$; after the move $W'=\dfrac{N!}{(n_1+1)!(n_2-1)!}$, so $\Delta S_{sys}=k\ln\dfrac{W'}{W}=k\ln\dfrac{n_2}{n_1+1}\approx k\ln\dfrac{n_2}{n_1}$ (with $n_1,n_2\gg1$). Reservoir: it receives the energy $\varepsilon_2-\varepsilon_1$ at $T$: $\Delta S_{res}=\dfrac{\varepsilon_2-\varepsilon_1}T$. At equilibrium the total is zero, which gives the Boltzmann ratio $\dfrac{n_2}{n_1}=e^{-(\varepsilon_2-\varepsilon_1)/kT}$.

> [!example]- Q5 · Two copper blocks ([[TH04 The Second Law Carnot Engines and Entropy]])
> Using each block's specific heat as given (1 kg at 150 °C with 0.393, 0.5 kg at 0 °C with 0.381 kJ kg⁻¹ K⁻¹): $0.393(423.15-T_f)=0.1905(T_f-273.15)$ ⇒ $T_f=\mathbf{374.2\ K\ (101.0\ °C)}$. $\Delta S_{univ}=0.393\ln\frac{374.18}{423.15}+0.1905\ln\frac{374.18}{273.15}=-48.3+60.0=\mathbf{+11.6\ J\,K^{-1}}$ (blocks isolated, so this is the universe's change; positive: irreversible).

> [!example]- Q6 · $C_P-C_V=TV\alpha^2/\kappa_T$ ([[TH05 Potentials Maxwell Relations Stability and the Third Law]])
> With $S(T,V)$: $dS=\frac{C_V}TdT+\big(\frac{\partial P}{\partial T}\big)_VdV$ (Maxwell relation from $F$). At constant $P$: $C_P=T\big(\frac{\partial S}{\partial T}\big)_P=C_V+T\big(\frac{\partial P}{\partial T}\big)_V\big(\frac{\partial V}{\partial T}\big)_P$. The cyclic relation gives $\big(\frac{\partial P}{\partial T}\big)_V=-\frac{(\partial V/\partial T)_P}{(\partial V/\partial P)_T}=\frac{\alpha}{\kappa_T}$ with $\alpha=\frac1V\big(\frac{\partial V}{\partial T}\big)_P$, $\kappa_T=-\frac1V\big(\frac{\partial V}{\partial P}\big)_T$; and $\big(\frac{\partial V}{\partial T}\big)_P=V\alpha$. Hence $C_P-C_V=\dfrac{TV\alpha^2}{\kappa_T}$ (≥ 0 since $\kappa_T>0$; ideal gas: $\alpha=1/T$, $\kappa_T=1/P$ ⇒ $nR$).

> [!example]- Q7 · Disulfide pairings ([[PR01 Counting and the Axioms of Probability]])
> Count perfect matchings of $n$ cysteines: pair the first with any of $n-1$, the next unpaired with any of $n-3$, …: $(n-1)(n-3)\cdots1=(n-1)!!=\dfrac{n!}{2^{n/2}(n/2)!}$. E.g. $n=4$: 3; $n=6$: 15; $n=8$: 105.

## Section 2 (2 marks each)
> [!example]- Solutions
> 1. $n_2/n_1=e^{-\Delta\varepsilon/kT}=0.20$ ⇒ $\Delta\varepsilon=kT\ln5=1.38\times10^{-23}\times350\times1.609=\mathbf{7.77\times10^{-21}\ J}$ (0.049 eV). ([[SM03 The Canonical Ensemble]])
> 2. **Cooler.** The escaping gas expands fast (little time for heat exchange) against the atmosphere: an approximately adiabatic expansion does work at the expense of internal energy; throttled through the puncture, air at room temperature also cools (positive Joule–Thomson coefficient). ([[TH03 The Ideal Gas and Adiabatic Processes]])
> 3. $P(\ge2\text{ fives in }3)=\binom32(\tfrac16)^2\tfrac56+(\tfrac16)^3=\tfrac{15+1}{216}=\mathbf{\tfrac2{27}}=0.074$.

## Section 3 (3 marks each)
> [!example]- Solutions
> 1. 40 buttons, 25 removed ⇒ 15 left; $P(\text{red})=\tfrac13$ ⇒ 5 reds left ⇒ **1 red removed** (6 − 5).
> 2. Free (Joule) expansion of an isolated gas: $Q=W=0$, so $U$ is constant. (a) **Ideal gas: $T$ unchanged** ($U=U(T)$). (b) **Real gas: usually cools**: $(\partial T/\partial V)_U=-\frac{1}{C_V}\big[T(\partial P/\partial T)_V-P\big]$, which for a van der Waals gas is $-a n^2/(C_VV^2)<0$ (work done against intermolecular attraction).
> 3. Into vacuum: $Q=0$, $W=0$, $\Delta U=0$, so $T$ is constant; compute $\Delta S$ along a reversible isotherm between the same states: $\Delta S=nR\ln(V_2/V_1)>0$. The surroundings are untouched ($\Delta S_{surr}=0$), so $\Delta S_{univ}>0$ with no heat flow: **irreversible** ([[TH04 The Second Law Carnot Engines and Entropy]]).

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | all questions | [[end sem TD2213 2021.pdf]] (Drive, 2026-11-21; text layer + page images) | taught (past paper) |
> | solutions and numbers | mine (checked in Python: Q1, Q3, Q5, §2 Q1, Q3) | extra/beyond |
>
> **Flags.** [!verify] Q5 gives two specific heats "at 150 and 0" °C; they are used as each block's constant $c$ — averaging them instead moves $T_f$ by < 0.1 K. Q2's paths are read from the hand-drawn figure.
