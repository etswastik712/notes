---
title: TH10 Open Systems Mixing and Reacting Gases
aliases: [TH10, open system, big equation, energy balance, entropy balance, steady flow, throttling, entropy of mixing, Gibbs energy of mixing, extent of reaction, reacting systems, pressure dependence of equilibrium, Le Chatelier pressure, post midsem thermo, Bhagwat notes]
subject: thermo
type: chapter
chapter: 10
part: IV
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
prereq: ["[[TH02 Work Heat and the First Law]]", "[[TH04 The Second Law Carnot Engines and Entropy]]", "[[TH05 Potentials Maxwell Relations Stability and the Third Law]]", "[[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]]"]
tags: [subject/thermo, type/chapter, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft, quiz/thermo, quiz/th-background]
---
# TH10 · Open Systems, Mixing and Reacting Gases

◀ [[TH09 Microstates Macrostates and Multiplicity]] · [[Thermodynamics and Statistical Mechanics - Course Map|Course Map]] · [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] ▶

<span class="scope-taught">taught · in syllabus (class notes of a classmate)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Scope of this chapter
> **Added 2026-11-12.** New sources, all student notes of the post-midsem lectures (the instructor's own slides are **not** in the folder, so the "taught" tag is inferred from the notes' content and the course context): **[[Bhagwat.pdf]]** (5 pp., a clean typed-on-tablet version), **[[post midsem thermo.pdf]]** (28 pp., phone photographs of the handwritten notebook that Bhagwat's pages were made from; many pages are rotated, read at low resolution) and **[[Kardar - bhagwat.pdf]]** (4 pp., generalised work, extensivity, Maxwell relations). I compared them with TH01–TH09: **Maxwell relations, $\mathrm dG=V\mathrm dP-S\mathrm dT$, Gibbs–Duhem, the ideal-gas chemical potential, $\Delta G^\circ=-RT\ln K$, Gibbs–Helmholtz, van 't Hoff and Clausius–Clapeyron are already in TH05 and TH08** (not repeated; one new remark on $(\partial\mu/\partial P)_T=V/N$ was added to TH05). **Not in the vault, and the content of this chapter:** (i) the **open-system energy and entropy balances** (the notes' "big equation"), (ii) the **thermodynamics of mixing ideal gases** ($\Delta S_i=-n_iR\ln x_i$, $\Delta G_{\rm mix}=RT\sum n_i\ln x_i$, $\Delta H_{\rm mix}=0$), (iii) **reacting ideal-gas mixtures**: the extent of reaction, mole fractions as functions of $\varepsilon$, $K=\prod(x_iP/P^\circ)^{\nu_i}$ and the **pressure and inert-gas dependence of the equilibrium composition**. New chapter under the new-material rule. The worked examples (heater, throttle, tank filling, equilibrium compositions) are mine; the numbers were checked in `scripts/th10_numbers.py`.

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught: Bhagwat / post-midsem notes)**
> - §1 what defines a system (boundaries), measurable versus conceptual variables, the state postulate; §2 the **open-system energy balance** and its closed, no-work special cases; §3 the **entropy balance** $\dot S^{\rm t}_{\rm gen}$ and the Gibbs-energy criterion; §4 **mixing** of ideal gases; §5 **reacting systems**: extent, $K$, pressure dependence; §6 the liquid–vapour direction argument
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §2 multi-stream and steady-flow forms; the three worked examples (heater, **throttle**, **tank filling**) with their entropy generation; §4 numbers for air, ternary and $N$-component mixing, the work to separate air; §5 the closed form for SO$_2$/SO$_3$, the pressure table, inert gas at constant $P$ versus constant $V$, $\Delta\nu=0$ and $\Delta\nu=+1$ examples, why the minimum of $G$ is interior; Practice 1–11; tool `th_reacting_equilibrium`

> [!key] After this chapter you can
> - write the **energy and entropy balances for an open system** and reduce them to the first law, to the steady-flow enthalpy balance, to throttling ($H_{\rm in}=H_{\rm out}$) and to the filling of a tank,
> - compute the **entropy generated** in a heater, a valve and a filling process and say what it costs in lost work,
> - derive $\Delta S_{\rm mix}$, $\Delta G_{\rm mix}$ and $\Delta H_{\rm mix}=0$ for ideal gases and explain them as an isothermal expansion of each gas into its partial pressure,
> - describe a reacting mixture by the **extent of reaction** $\varepsilon$, find the equilibrium composition from $K$, and predict the effect of pressure, inert gas and $\Delta\nu$ on it.

> [!intuition] The one-sentence story
> Treat the system as a box with a **boundary** that heat, work and matter can cross, and write down, for the whole box, what comes in minus what goes out equals what accumulates; the only thing that is *not* conserved is entropy, which can only be **generated** inside. Mixing and reacting are then the simplest "processes inside": ideal gases mix without any energy change, purely because the number of accessible arrangements grows ($\Delta S_{\rm mix}>0$, $\Delta G_{\rm mix}<0$), and a reaction proceeds until the slope $\partial G/\partial\varepsilon=\sum\nu_i\mu_i$ of the **Gibbs energy of the mixture** is zero; the mixing terms make that minimum interior, so no reaction ever goes quite to completion.

![[fig_th10_mixing_reacting.png]]
*A: entropy and Gibbs energy of mixing of two ideal gases against the mole fraction; the maximum is $R\ln2$ at $x=\tfrac12$ and $\Delta G_{\rm mix}=-T\Delta S_{\rm mix}$ at 298.15 K (§4). B: $[G(\varepsilon)-G(0)]/RT$ for $\mathrm{SO_2}+\tfrac12\mathrm{O_2}\rightleftharpoons\mathrm{SO_3}$ with $K=10$ (illustrative) at 0.1, 1 and 10 bar; the minima are at $\varepsilon=0.571,\ 0.764,\ 0.882$ (§5). C: equilibrium extent against pressure for $\Sigma\nu=-\tfrac12,\ 0,\ +1$ (§5). Numbers: `scripts/th10_numbers.py`; `scripts/fig_th10.py`.*

## 1. Systems, boundaries and variables
<span class="scope-taught">taught</span> *Source: [[Bhagwat.pdf#page=1|Bhagwat p. 1]]; [[post midsem thermo.pdf#page=6|post-midsem notebook p. 6]] (state postulate)*

- **The boundary defines the system.** *No heat exchange* $\Rightarrow$ **adiabatic**; *no matter exchange* $\Rightarrow$ **closed**; *neither heat, work nor matter* $\Rightarrow$ **isolated**. A system that exchanges matter is **open**.
- **Notation of the notes.** A superscript **t** means *total* (an extensive quantity, = number of moles times the molar value, e.g. $U^{\rm t}=nU$) and a **dot** means a rate $\mathrm d/\mathrm dt$; $\dot n$ is the *net* molar flow rate into the system.
- **Measurable versus conceptual.** $P,V,T,n$ can be read off an instrument; $S,H,G,U$ (and $A$) are **conceptual**: they can only be inferred through the relations of TH05 (Maxwell relations convert "conceptual" derivatives into measurable ones).
- **Closed systems and what stays constant** (notebook p. 15, dated 14/10/26). *Single component, closed:* $n$ constant. *Several components, non-reacting:* each $n_i$ constant. *Reacting:* neither the $n_i$ nor the total $n_t$ stays constant, and the reaction **need not go to completion** (§5).
- **State postulate.** For a single-phase pure substance, fixing **two intensive properties** fixes all the others (the notebook's statement; it is the Gibbs phase rule for one component and one phase, $F=C-\Phi+2=2$).

## 2. The big equation: the energy balance of an open system
<span class="scope-taught">taught</span> *Source: [[Bhagwat.pdf#page=1|Bhagwat p. 1]]; [[post midsem thermo.pdf#page=1|post-midsem notebook pp. 1–2]]* · <span class="scope-extra-beyond">extra · beyond</span> *multi-stream and steady-flow forms, examples*

$$\boxed{\ \frac{\mathrm dU^{\rm t}}{\mathrm dt}=\dot Q-P\frac{\mathrm dV^{\rm t}}{\mathrm dt}+\dot n\,(U+PV)+\dot W\ }$$

Term by term (the notes' annotation):
- $\dot Q$: **heat** entering through the boundary;
- $-P\,\mathrm dV^{\rm t}/\mathrm dt$: **expansion work** done *by* the system against its surroundings;
- $\dot nU$: the **energy carried in by the matter** ($\dot n$ moles per second, $U$ per mole);
- $\dot n\,PV$: the **flow work** done *on* the system in pushing $\dot n$ moles per second, of molar volume $V$ (the incoming material's), into it at pressure $P$;
- $\dot W$: **all the other work** (shaft, electrical, any non-$PV$ work).

Because $U+PV=H$, the matter term is $\dot n\,H$: "as if the material did not take up volume and just carried the energy $H$." (For a flow leaving the system $\dot n<0$, and $H$ is that of the outgoing stream.) The equation is the **conservation of energy** (mass plus energy for nuclear processes is not considered; the notes' remark).

**Special cases.**
- **Closed, no other work** ($\dot n=0$, $\dot W=0$): $\dfrac{\mathrm dU^{\rm t}}{\mathrm dt}=\dot Q-P\dfrac{\mathrm dV^{\rm t}}{\mathrm dt}$; per mole $\dfrac{\mathrm dU}{\mathrm dt}=\dot q-P\dfrac{\mathrm dv}{\mathrm dt}$, with the shorthand $\mathrm dU=\mathrm dQ-P\,\mathrm dV$: **the first law**.
- 🔵 **Several streams:** replace $\dot n H$ by $\sum_{\rm in}\dot n_kH_k-\sum_{\rm out}\dot n_kH_k$.
- 🔵 **Steady flow** ($\mathrm dU^{\rm t}/\mathrm dt=\mathrm dV^{\rm t}/\mathrm dt=0$): $\ \sum_{\rm in}\dot nH-\sum_{\rm out}\dot nH+\dot Q+\dot W=0$: an **enthalpy balance** (the open-system face of $H$ in [[TH07 Enthalpy Thermochemistry and Calorimetry]]).

## 3. The entropy balance and entropy generation
<span class="scope-taught">taught</span> *Source: [[Bhagwat.pdf#page=1|Bhagwat pp. 1–2]]; [[post midsem thermo.pdf#page=3|post-midsem notebook pp. 3–5]]*

$$\boxed{\ \frac{\mathrm dS^{\rm t}}{\mathrm dt}=\frac{\dot Q}{T}+\dot n\,S+\dot S^{\rm t}_{\rm gen}\ }$$
Entropy enters with the heat (at the boundary temperature $T$) and with the matter ($S$ per mole) and is **generated inside** by irreversible processes: $\dot S^{\rm t}_{\rm gen}\ge0$, $=0$ for a reversible process (the second law). A reversible heat transfer ($\Delta T\to0$) generates none; my reading of the notebook's remark (partly illegible): *entropy is also generated in any spontaneous process whenever a finite temperature difference $\Delta T$ exists.* "More $T$ difference, more entropy gained or lost for the same $\dot Q$": the entropy generated by heat flow is $\dot Q\,(1/T_B-1/T_A)$ ([[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] §2).

**Closed system, no shaft work.** Combine with §2: $\dot Q=T\,\mathrm dS^{\rm t}/\mathrm dt-T\dot S^{\rm t}_{\rm gen}$ (equal to $T\,\mathrm dS^{\rm t}/\mathrm dt$ for a reversible process), hence
$$T\dot S^{\rm t}_{\rm gen}=-\frac{\mathrm dU^{\rm t}}{\mathrm dt}+T\frac{\mathrm dS^{\rm t}}{\mathrm dt}-P\frac{\mathrm dV^{\rm t}}{\mathrm dt}\ \ (\ge0).$$
The notebook's reading: if this is **positive** the process is **spontaneous** (it goes in the direction written); if **negative** it goes in the opposite direction; if **zero** the system is at equilibrium and the process is reversible. With the free energies $A=U-TS$ (Helmholtz) and $G=H-TS$ (Gibbs): at **constant $T,V$**, $\mathrm dA=-T\,\mathrm dS_{\rm gen}\le0$; at **constant $T,P$**, $\mathrm dG=\mathrm dU+P\,\mathrm dV-T\,\mathrm dS=\boxed{-T\,\mathrm dS_{\rm gen}}\le0$, i.e. **$G$ decreases in every spontaneous change and is minimal at equilibrium** ([[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] §1; TH05).

### 3.1 Three flow examples 🔵 (numbers: `scripts/th10_numbers.py`)
> [!example] A heater (steady flow)
> $\dot n=1$ mol s$^{-1}$ of an ideal diatomic gas ($C_p=\tfrac72R=29.10$ J mol$^{-1}$K$^{-1}$) is heated at constant pressure from 300 K to 600 K. §2, steady, $\dot W=0$: $\dot Q=\dot n\,C_p\Delta T=\mathbf{8730}$ W. §3, steady: $0=\dot Q/T_w+\dot n(S_{\rm in}-S_{\rm out})+\dot S_{\rm gen}$, so $\dot S_{\rm gen}=\dot nC_p\ln2-\dot Q/T_w=20.17-\dot Q/T_w$ W K$^{-1}$ with the gas's entropy rise $20.17$ W K$^{-1}$: heater wall at $600$ K: $5.62$; at $800$ K: $9.26$; at $1500$ K: $14.35$ W K$^{-1}$. The hotter the heating surface, the more entropy is generated for the same heat; $\dot S_{\rm gen}\to0$ only if each element of heat is supplied at the temperature the gas has at that point.

> [!example] A throttle (valve, steady, adiabatic, no work)
> $\dot Q=\dot W=0$ and steady flow give $H_{\rm in}=H_{\rm out}$, which for an ideal gas means $T_{\rm out}=T_{\rm in}$. Then $\dot S_{\rm gen}=\dot n\,(S_{\rm out}-S_{\rm in})=\dot n R\ln(P_{\rm in}/P_{\rm out})$: for $10\to1$ bar and $\dot n=1$ mol s$^{-1}$, $\dot S_{\rm gen}=\mathbf{19.15}$ W K$^{-1}$, and with surroundings at 300 K the **lost power** is $T_0\dot S_{\rm gen}=5743$ W, exactly the power $\dot nRT\ln10$ a reversible isothermal expander would have delivered: the throttle wastes all of it.

> [!example] Filling a tank (unsteady)
> An evacuated, rigid ($\mathrm dV^{\rm t}=0$), adiabatic tank is connected to a line at $T_{\rm line}$. §2 with $\dot Q=\dot W=0$: $\mathrm dU^{\rm t}/\mathrm dt=\dot nH_{\rm line}$; integrating, $U^{\rm t}_{\rm final}=N\,H_{\rm line}$, i.e. $C_vT_f=C_pT_{\rm line}$ and
> $$T_f=\gamma\,T_{\rm line}.$$
> Diatomic gas ($\gamma=7/5$) from a 300 K line ends at **420 K**; a monatomic gas ($\gamma=5/3$) at **500 K** ("the flow work $PV$ of the gas pushed in is turned into internal energy"). If filling stops when the tank pressure equals the line's, the entropy generated per mole admitted is $C_p\ln\gamma=9.79$ J mol$^{-1}$K$^{-1}$ (diatomic). *Check:* $C_vT_f=8730.2=C_pT_{\rm line}$ J mol$^{-1}$.

## 4. Mixing of ideal gases
<span class="scope-taught">taught</span> *Source: [[Bhagwat.pdf#page=3|Bhagwat pp. 3–4]]* · <span class="scope-extra-beyond">extra · beyond</span> *numbers, $N$ components, the work to separate air*

For an **ideal gas** the enthalpy does not change on mixing, but $S$, $G$ and $A$ do. Take gas A ($n_A$, $P$, $T$) and gas B ($n_B$, $P$, $T$) and let them mix at the same $P$ and $T$; the mixture has $n=n_A+n_B$ and mole fractions $x_i=n_i/n$.

**Entropy.** Regard each gas as undergoing an **isothermal expansion from $P$ to its partial pressure $x_iP$**. With the Maxwell relation $(\partial S/\partial P)_T=-(\partial V/\partial T)_P=-nR/P$:
$$\Delta S_i=\int_P^{x_iP}\Big(\frac{\partial S}{\partial P}\Big)_T\mathrm dP=-n_iR\ln\frac{x_iP}{P}=-n_iR\ln x_i,\qquad\boxed{\Delta S_{\rm mix}=-R\sum_in_i\ln x_i=-nR\sum_ix_i\ln x_i>0.}$$
**Enthalpy.** $\mathrm dH=T\mathrm dS+V\mathrm dP=-\dfrac{nRT}{P}\mathrm dP+\dfrac{nRT}P\mathrm dP=0$ at constant $T$: $\Delta H_{\rm mix}=0$ (the notes' check).
**Gibbs energy.** $\Delta G_{\rm mix}=\Delta H-T\Delta S=\boxed{RT\sum_in_i\ln x_i<0}$: **mixing is spontaneous and entirely entropic**. Per mole of mixture, $G_{\rm mix}=\sum_ix_i\,\mu_i$ with
$$\mu_i=G_i^\circ+RT\ln x_i\quad(\text{at }P=P^\circ),\qquad\mu_i=\mu_i^\circ(T)+RT\ln\frac{x_iP}{P^\circ}\ \ (\text{general }P),$$
which is the ideal-gas chemical potential of TH05 with $P_i=x_iP$.

> [!example] Numbers (298.15 K; `th10_numbers.py`)
> | mixture | $\Delta S_{\rm mix}$ (J mol$^{-1}$K$^{-1}$) | $\Delta G_{\rm mix}$ (kJ mol$^{-1}$) |
> |---|---|---|
> | equimolar binary | $R\ln2=5.763$ | $-1.718$ |
> | air-like, $0.79\,\mathrm N_2+0.21\,\mathrm O_2$ | $4.273$ ($0.514R$) | $-1.274$ |
> | $1:3$ | $4.676$ | $-1.394$ |
> | equimolar ternary | $R\ln3=9.134$ | $-2.723$ |
>
> The entropy is **maximal for equal fractions** and equals $R\ln N$ for $N$ components. The same $1.274$ kJ per mole of air is the **minimum work to separate air into pure N$_2$ and O$_2$** at 298.15 K (reversible isothermal separation; [[SM06 Entropy Information and the Arrow of Time]], availability). For $2$ mol A and $3$ mol B: $\Delta S=-R(2\ln0.4+3\ln0.6)=27.98$ J K$^{-1}$ ($5.596$ per mole), $\Delta G_{\rm mix}(300\ \mathrm K)=-8.39$ kJ.

> [!derivation] The notebook's route: $\Delta G_{\rm mix}$ from $\mathrm dG=V\mathrm dP$ (pp. 12–14)
> A mixture of $80\%$ N$_2$ and $20\%$ O$_2$, initially at $1$ atm and $300$ K: the *partial pressure* of a component is the pressure it would need to occupy the final volume $V_T$ alone, $P_i=x_iP$ (the page: $n_{\rm N_2}=P_{\rm N_2}V_{\rm N_2}/RT$ and $P\,V_T=\sum P_iV_i$ with $V_T=\sum V_i$ "volume being added" when the final pressure is $P_f=1$ atm). From $G=f(T,P)$, $\mathrm dG=V\mathrm dP-S\mathrm dT$, **at constant $T$** $\mathrm dG=V\mathrm dP$, and for an ideal gas $V=RT/P$:
> $$\Delta G_A=\int_P^{P_A}\frac{RT}P\,\mathrm dP=RT\ln\frac{P_A}P=RT\ln x_A,\qquad\Delta G^{\rm t}_{\rm mix}=n_ART\ln x_A+n_BRT\ln x_B,\qquad\Delta G_{\rm mix}=RT\sum_ix_i\ln x_i,$$
> and "$G^{\rm IG}_{\rm mixture}=\sum x_i\big(G_i+RT\ln x_i\big)$: the bracket is the **partial molar Gibbs energy, a.k.a. the chemical potential $\mu_i$**". The same result as the entropy route above ($\Delta H=0$, so $\Delta S_{\rm mix}=-\Delta G_{\rm mix}/T$). *Numbers (`th_notebook_numbers.py`):* $\Delta G_{\rm mix}=RT(0.8\ln0.8+0.2\ln0.2)=-1248$ J mol$^{-1}$ at 300 K, i.e. $\Delta S_{\rm mix}=4.161$ J mol$^{-1}$K$^{-1}=0.5004R$; per mole of N$_2$ $RT\ln0.8=-557$ J, per mole of O$_2$ $RT\ln0.2=-4015$ J (the scarcer component gains the most free energy per mole).

> [!pitfall] The formula is for *different* gases
> $\Delta S_{\rm mix}=-R\sum n_i\ln x_i$ holds when the species can be told apart; "mixing" two samples of the **same** gas gives $\Delta S=0$. That discontinuity is the **Gibbs paradox** ([[Gibbs Paradox]]; [[SM06 Entropy Information and the Arrow of Time]] §2).

## 5. Reacting systems and the pressure dependence of equilibrium
<span class="scope-taught">taught</span> *Source: [[Bhagwat.pdf#page=4|Bhagwat pp. 4–5]] (the notebook's reacting-systems pages 15–18 are the second source)* · <span class="scope-extra-beyond">extra · beyond</span> *the closed forms, the tables, inert gas, $\Delta\nu=0,+1$*

In a **closed** system a chemical reaction need not go to completion ("limiting reagent", or, even with exact stoichiometric amounts, equilibrium sets in). Describe it by the **extent of reaction** $\varepsilon$ (mol): for $\sum_i\nu_iA_i=0$ ($\nu_i<0$ reactants, $>0$ products)
$$n_i=n_i^0+\nu_i\varepsilon,\qquad\mathrm dn_i=\nu_i\,\mathrm d\varepsilon,\qquad x_i=\frac{n_i^0+\nu_i\varepsilon}{\sum_jn_j^0+\varepsilon\sum_j\nu_j}.$$
The notes' example: $\mathrm{SO_2}+\tfrac12\mathrm{O_2}\rightleftharpoons\mathrm{SO_3}$, $\nu=(-1,-\tfrac12,+1)$, start with $C$ mol SO$_2$ and $C/2$ mol O$_2$: moles $C-\varepsilon,\ \tfrac C2-\tfrac\varepsilon2,\ \varepsilon$ (the table "initial / consumed / formed").

**Driving force.** At constant $T,P$: $\mathrm dG^{\rm t}=\sum\mu_i\mathrm dn_i=\Big(\sum_i\nu_i\mu_i\Big)\mathrm d\varepsilon$, so
$$\Big(\frac{\partial G^{\rm t}}{\partial\varepsilon}\Big)_{T,P}=\sum_i\nu_i\mu_i=\Delta_rG=RT\ln\frac QK\qquad\text{(the driving force of the reaction)},$$
negative: the reaction goes forward; **zero: equilibrium**; the extent at equilibrium is where $G^{\rm t}(\varepsilon)$ is **minimal**.

**The equilibrium constant and pressure.** With $\mu_i=G_i^\circ+RT\ln(x_iP/P^\circ)$ and $\Delta G^\circ=\sum\nu_iG_i^\circ$, $\sum\nu_i\mu_i=0$ gives $\Delta G^\circ=-RT\ln K$ with
$$\boxed{K=\prod_i\Big(\frac{x_iP}{P^\circ}\Big)^{\nu_i}=\Big[\prod_ix_i^{\nu_i}\Big]\Big(\frac P{P^\circ}\Big)^{\sum_i\nu_i}}$$
($\Delta G^\circ$ and $K$ depend on $T$ only: [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] §3). Hence **at fixed $K$ the composition $\prod x_i^{\nu_i}=K(P/P^\circ)^{-\Sigma\nu}$ depends on $P$ unless $\Sigma\nu=0$**: the notes' statements, "if $\sum\nu_i=0$ the $P/P^\circ$ factors cancel so pressure won't shift equilibrium"; "$\sum\nu_i=-\tfrac12$: $K$ depends on $P^{-1/2}$, so higher $P$ pushes the reaction forward (to fewer moles)." In words (**Le Chatelier**): raising the pressure favours the side with fewer moles of gas.

> [!example] $\mathrm{SO_2}+\tfrac12\mathrm{O_2}\rightleftharpoons\mathrm{SO_3}$ with $K=10$ (illustrative value, not a measured $K$) 🔵
> Start with $1$ mol SO$_2$ and $\tfrac12$ mol O$_2$: moles $(1-\varepsilon,\ \tfrac{1-\varepsilon}2,\ \varepsilon)$, total $N=\tfrac{3-\varepsilon}2$, so $x=\big(\tfrac{2(1-\varepsilon)}{3-\varepsilon},\ \tfrac{1-\varepsilon}{3-\varepsilon},\ \tfrac{2\varepsilon}{3-\varepsilon}\big)$ and
> $$K=\frac{x_{\rm SO_3}}{x_{\rm SO_2}\sqrt{x_{\rm O_2}}}\Big(\frac P{P^\circ}\Big)^{-1/2}=\frac{\varepsilon\sqrt{3-\varepsilon}}{(1-\varepsilon)^{3/2}}\Big(\frac P{P^\circ}\Big)^{-1/2}.$$
> | $P$ (bar) | 0.1 | 1 | 2 | 5 | 10 | 50 | 200 |
> |---|---|---|---|---|---|---|---|
> | $\varepsilon_{\rm eq}$ | 0.5707 | **0.7645** | 0.8074 | 0.8537 | 0.8819 | 0.9290 | 0.9547 |
> | $x_{\rm SO_3}$ | 0.470 | 0.684 | 0.737 | 0.796 | 0.833 | 0.897 | 0.934 |
>
> At 1 bar: $x=(0.2107,\ 0.1054,\ 0.6839)$ for SO$_2$, O$_2$, SO$_3$. **Inert gas at constant total pressure** (1 bar) acts like a **dilution**, i.e. like lowering $P$ ($\Sigma\nu<0$ pushes back): with $0,\ 1.5,\ 3,\ 10$ mol of inert, $\varepsilon_{\rm eq}=0.7645,\ 0.7031,\ 0.6667,\ 0.5783$. At **constant volume and temperature** adding an inert gas changes no partial pressure, hence not $Q$: **no shift**. 
>
> **$\Sigma\nu=0$:** $\mathrm H_2+\mathrm I_2\rightleftharpoons2\mathrm{HI}$ (start $1,1,0$): $K=\dfrac{4\varepsilon^2}{(1-\varepsilon)^2}$, so $\varepsilon_{\rm eq}=\dfrac{\sqrt K}{2+\sqrt K}$ at every pressure ($K=50$: $0.7795$). **$\Sigma\nu=+1$:** $\mathrm N_2\mathrm O_4\rightleftharpoons2\mathrm{NO_2}$ (start $1,0$): $K=\dfrac{4\varepsilon^2}{1-\varepsilon^2}\dfrac P{P^\circ}$, $\varepsilon_{\rm eq}=\sqrt{K/(K+4P/P^\circ)}$; $K=0.15$ (illustrative): $\varepsilon_{\rm eq}=0.522,\ 0.190,\ 0.061$ at $0.1,\ 1,\ 10$ bar: the dissociation *falls* as $P$ rises.

> [!key] Why a gas reaction never goes to completion (nor fails to start) 🔵
> $\partial G^{\rm t}/\partial\varepsilon=RT\ln(Q/K)$. As $\varepsilon\to0$ a **product** has $x\to0$, so $Q\to0$ and the slope $\to-\infty$ (the first bit of reaction always lowers $G$); as the limiting **reactant** runs out, $x\to0$ in a denominator, $Q\to\infty$ and the slope $\to+\infty$. For SO$_2$/SO$_3$ at $K=10$, $P=1$ bar: $\ln(Q/K)=-15.57$ at $\varepsilon=10^{-6}$ and $+18.77$ at $1-10^{-6}$. The cause is the **entropy of mixing** terms $n_i\ln x_i$ in $G$: the minimum is always interior (Fig. B; the grid minimum $\varepsilon=0.7640$ and the root of $Q=K$, $0.76448$, coincide).

> [!example] The notebook's $\Sigma\nu=0$ example: the water-gas shift $\mathrm{CO}+\mathrm{H_2O}\rightleftharpoons\mathrm{CO_2}+\mathrm{H_2}$ at 1100 K (pp. 17–18)
> The page writes $K$ with $x_i$ and $P/P^\circ$ and notes that for $\Sigma\nu=0$ **the $P/P^\circ$ factors cancel, so pressure has no effect**. At $1100$ K it takes $\Delta G^\circ=0$ (so $K=1$) and starts with $1$ mol CO and $1$ mol steam: $n=(1-\varepsilon,\,1-\varepsilon,\,\varepsilon,\,\varepsilon)$, $\sum n=2$, $K=\dfrac{(\varepsilon/2)^2}{((1-\varepsilon)/2)^2}=1\Rightarrow\boxed{\varepsilon=\tfrac12}$. A side calculation on the page with $1$ mol CO and $2$ mol steam gives $\varepsilon^2=(1-\varepsilon)(2-\varepsilon)=2-3\varepsilon+\varepsilon^2$, so $\boxed{\varepsilon=\tfrac23}$ (both exact; more steam pushes the reaction forward). The general statement of the page: $-\dfrac{\Delta G^\circ_T}{RT}=\ln\Big(\dfrac{\text{products}}{\text{reactants}}\Big)\Big(\dfrac P{P^\circ}\Big)^{\Sigma\nu}$, so $\dfrac{\rm prod}{\rm react}=e^{-\Delta G^\circ/RT}\Big(\dfrac P{P^\circ}\Big)^{-\Sigma\nu}$ [the notebook writes the exponent as $+\Sigma\nu$ in the last line; I have corrected the sign to agree with the first line]: **for $P>P^\circ$ and $\Sigma\nu<0$ products increase with $P$; for $\Sigma\nu>0$ products decrease**. (The $\Delta G^\circ=0$ at 1100 K is the page's given, not a looked-up value.)

> [!key] Rate versus yield: the Haber remark (p. 15)
> "Nitrogen and hydrogen react at **low $T$: higher yield but very slow**; at **high $T$: very fast but the yield falls** (equilibrium reached)". The two halves are the thermodynamic statement ($\mathrm{N_2}+3\mathrm{H_2}\rightleftharpoons2\mathrm{NH_3}$ is exothermic, so $K$ falls as $T$ rises: van 't Hoff, [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] §4, $K(298\ \mathrm K)=5.8\times10^5\to K(773\ \mathrm K)=6.9\times10^{-5}$) and the kinetic one (the rate rises with $T$); and with $\Sigma\nu=-2$ high pressure raises the yield (§5 above), the reason such a reaction is run hot, at high $P$ and on a catalyst.

**Temperature.** Pressure changes the *composition*, never $K$; temperature changes $K$ itself, through the van 't Hoff equation $\mathrm d\ln K/\mathrm dT=\Delta H^\circ/RT^2$ (TH08 §4): endothermic reactions shift forward on heating, exothermic ones back. The Gibbs–Helmholtz equation $\partial(G/T)/\partial T=-H/T^2$ that gives it is derived in the notes exactly as in TH08 §4.1.

*The interactive tool for this section (reaction, $K$, $P$, inert gas; $G(\varepsilon)$ and $\varepsilon_{\rm eq}$ against $P$) is embedded before the chapter summary.*

## 6. Liquid–vapour equilibrium as a minimum of $G$
<span class="scope-taught">taught</span> *Source: [[Bhagwat.pdf#page=2|Bhagwat p. 2]]*

A closed vessel holds liquid and vapour at fixed $T,P$: $G^{\rm t}=n^vG^v+n^lG^l$ with $n^v+n^l$ constant, so $\mathrm dn^l=-\mathrm dn^v$. At fixed $T,P$ the molar $G^v,G^l$ are **intensive** and do not change, hence
$$\mathrm dG^{\rm t}=(G^v-G^l)\,\mathrm dn^v.$$
If $G^v<G^l$ then $\mathrm dG^{\rm t}<0$ requires $\mathrm dn^v>0$: **the liquid vaporises**; if $G^v>G^l$ the vapour condenses; **at equilibrium $G^v=G^l$** and $\mathrm dG^{\rm t}=0$. Along the coexistence curve both change together, $\mathrm dG^v=\mathrm dG^l$: $V^v\mathrm dP-S^v\mathrm dT=V^l\mathrm dP-S^l\mathrm dT$, so $\dfrac{\mathrm dP}{\mathrm dT}=\dfrac{\Delta S}{\Delta V}=\dfrac{\Delta H_{\rm vap}}{T\Delta V}$ and, for an ideal vapour with $V^v\gg V^l$ ($\Delta V\simeq RT/P$), $\dfrac{\mathrm d\ln P}{\mathrm dT}=\dfrac{\Delta H_{\rm vap}}{RT^2}$: **Clausius–Clapeyron**, the same form as van 't Hoff (notes: "similar to Clausius–Clapeyron"), derived and applied in TH08 §5. *Number from the notebook's setting* (pp. 7–8: "from a given $P_i,T_i,T_f$ you find $P_f$ for equilibrium"; then "for $0.7$ atm $=P_2$, $P_1=1$ atm"): the boiling point at $0.7$ atm, $\frac1{T_2}=\frac1{T_1}-\frac R{\Delta H_{\rm vap}}\ln0.7$ with $T_1=373.15$ K and $\Delta H_{\rm vap}=40.66$ kJ mol$^{-1}$ (recalled): $T_2=363.26$ K $=\mathbf{90.1}$ °C, about $9.9$ K lower than at 1 atm (compare the altitude example in TH08 §5). The notebook derives $\mathrm dP/\mathrm dT=\Delta H^{\rm vap}/(T\Delta V^{\rm vap})$ (the Clapeyron relation) from $\mathrm dG^v=\mathrm dG^l$ exactly as above, then notes $\Delta V^{\rm vap}\approx V^v$ is much larger than $V^l$ and $V^v=RT/P$. *Number* 🔵: water at 373.15 K and 90 kPa (below the 101.325 kPa vapour pressure): the vapour's chemical potential is lower than at saturation by $RT\ln(90/101.325)=-367.7$ J mol$^{-1}$, the liquid's by only $V\Delta P=-0.20$ J mol$^{-1}$, so $G^v-G^l=-367.5$ J mol$^{-1}<0$ and the liquid **vaporises**.

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Reacting ideal gases: the minimum of G(ε), and how pressure and inert gas shift it
> Pick a gas reaction (A ⇌ B, N₂O₄ ⇌ 2NO₂, 2A ⇌ B, SO₂ + ½O₂ ⇌ SO₃, N₂ + 3H₂ ⇌ 2NH₃), the equilibrium constant K, the total pressure P and the amount of inert gas.
>
> ![[th_reacting_equilibrium.png|720]]
>
> **Try:** Choose SO₂ + ½O₂ ⇌ SO₃ with K = 10 and P = 1 bar: ε_eq = 0.7645. Raise P to 10 bar: 0.8819 (Σν = −½, so K = [x-product](P/P°)^(−½)). Add 3 mol of inert gas at 1 bar: ε_eq falls to 0.6667. Switch to A ⇌ B (Σν = 0): the right-hand curve is flat, ε_eq = K/(1+K) whatever P and the inert gas. Switch to N₂O₄ ⇌ 2NO₂ (Σν = +1): ε_eq falls as P rises.
>
> [▶ Open the tool in your browser](../Assets/interactive/th_reacting_equilibrium.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/th_reacting_equilibrium.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How TH10 connects
> **Builds on:** [[TH02 Work Heat and the First Law]] (first law, $H=U+PV$), [[TH04 The Second Law Carnot Engines and Entropy]] (entropy, Clausius inequality), [[TH05 Potentials Maxwell Relations Stability and the Third Law]] ($G$, $\mu$, the ideal-gas chemical potential, Maxwell relation used in §4), [[TH07 Enthalpy Thermochemistry and Calorimetry]] (the steady-flow enthalpy balance), [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] ($K$, entropy generation, van 't Hoff, Clausius–Clapeyron).
> **Leads to:** [[TH09 Microstates Macrostates and Multiplicity]] (the microscopic reason for $\Delta S_{\rm mix}$: more arrangements), [[SM05 The Grand Canonical Ensemble and Chemical Equilibrium]] ($K$ from partition functions, the Saha equation), [[SM06 Entropy Information and the Arrow of Time]] (mixing entropy as available work, the Gibbs paradox), chemical engineering (steady-flow balances: turbines, compressors, heat exchangers, reactors).
> **Concepts:** [[Open System Energy Balance]] · [[Entropy of Mixing of Ideal Gases]] · [[Extent of Reaction]] · [[Pressure Dependence of Chemical Equilibrium]] · [[Entropy Production]] · [[Chemical Potential]] · [[Equilibrium Constant]] · [[Gibbs Free Energy]] · [[Law of Mass Action]] · [[Gibbs Paradox]]
> **Other subjects:** [[Climate - Course Map|Climate]] (a flow balance of heat and moisture through an air parcel is the open-system equation; the Clausius–Clapeyron derivation of §6 is the one used in [[CL05 Thermodynamic State of the Atmosphere]]), [[Inorganic Chemistry - Course Map|Inorganic Chemistry]] (equilibrium constants and reaction quotients, $\Delta G=-nFE$), [[Ecology and Evolution - Course Map|Ecology and Evolution]] (mass balances of nutrients through a lake, the same "in minus out equals accumulation").

## Summary
> [!summary] Cheat-sheet
> - **Open system (energy):** $\dfrac{\mathrm dU^{\rm t}}{\mathrm dt}=\dot Q-P\dfrac{\mathrm dV^{\rm t}}{\mathrm dt}+\dot n(U+PV)+\dot W$, $U+PV=H$; closed, no work: $\mathrm dU=\mathrm dQ-P\mathrm dV$; steady flow: $\sum\dot nH_{\rm in}-\sum\dot nH_{\rm out}+\dot Q+\dot W=0$.
> - **Entropy:** $\dfrac{\mathrm dS^{\rm t}}{\mathrm dt}=\dfrac{\dot Q}T+\dot nS+\dot S_{\rm gen}$, $\dot S_{\rm gen}\ge0$; closed: $T\dot S_{\rm gen}=-\dot U^{\rm t}+T\dot S^{\rm t}-P\dot V^{\rm t}$; constant $T,P$: $\mathrm dG=-T\mathrm dS_{\rm gen}\le0$.
> - **Examples:** heater 300→600 K, 1 mol s$^{-1}$: $\dot Q=8730$ W, $\dot S_{\rm gen}=9.26$ W K$^{-1}$ (wall at 800 K); throttle $10\to1$ bar: $\dot S_{\rm gen}=\dot nR\ln10=19.15$ W K$^{-1}$, $T_{\rm out}=T_{\rm in}$; tank filling: $T_f=\gamma T_{\rm line}$ (420 K for 300 K, $\gamma=\tfrac75$).
> - **Mixing:** $\Delta S_{\rm mix}=-R\sum n_i\ln x_i$, $\Delta H_{\rm mix}=0$, $\Delta G_{\rm mix}=RT\sum n_i\ln x_i$; $\mu_i=\mu_i^\circ+RT\ln(x_iP/P^\circ)$; max $R\ln N$; air: $4.27$ J mol$^{-1}$K$^{-1}$, $-1.27$ kJ mol$^{-1}$ at 298 K.
> - **Reacting gases:** $n_i=n_i^0+\nu_i\varepsilon$; $\partial G/\partial\varepsilon=\sum\nu_i\mu_i=RT\ln(Q/K)$; $K=\prod(x_iP/P^\circ)^{\nu_i}=\prod x_i^{\nu_i}(P/P^\circ)^{\Sigma\nu}$; $\Sigma\nu<0$: higher $P$ → products; $\Sigma\nu>0$: reactants; $\Sigma\nu=0$: no effect; inert at constant $P$ = lower $P$; at constant $V$: no effect; the minimum of $G(\varepsilon)$ is interior.
> - **Liquid–vapour:** $\mathrm dG^{\rm t}=(G^v-G^l)\mathrm dn^v$; equilibrium $G^v=G^l$; coexistence gives Clausius–Clapeyron.

## Practice
1. **Heater.** $2$ mol s$^{-1}$ of a diatomic ideal gas is heated at constant pressure from $25$ °C to $200$ °C. Find $\dot Q$ and $\dot S_{\rm gen}$ if the heater surface is at $500$ K and at $800$ K.
2. **Throttle.** $5$ mol s$^{-1}$ of an ideal gas at $350$ K is throttled from $8$ to $2$ bar. Find $T_{\rm out}$, $\dot S_{\rm gen}$ and the lost power for $T_0=300$ K.
3. **Tank filling.** An evacuated rigid adiabatic tank is filled from a line of helium at $400$ K. Find $T_f$ and the entropy generated per mole admitted ($p_{\rm final}=p_{\rm line}$). Repeat for N$_2$.
4. **Mixing.** $2$ mol of A and $3$ mol of B (ideal) mix at $300$ K and $1$ bar. Find $\Delta S_{\rm mix}$, $\Delta G_{\rm mix}$, $\Delta H_{\rm mix}$.
5. **Maximum.** Show that $\Delta S_{\rm mix}$ per mole is maximal for equal mole fractions and equals $R\ln N$ for $N$ components.
6. **Equilibrium composition.** For $\mathrm{SO_2}+\tfrac12\mathrm{O_2}\rightleftharpoons\mathrm{SO_3}$ with $K=10$ at $5$ bar (start $1$ mol SO$_2$, $\tfrac12$ mol O$_2$) find $\varepsilon_{\rm eq}$ and the mole fractions. Why is the answer larger than at $1$ bar?
7. **Inert gas.** For the same reaction at $1$ bar, what happens when $3$ mol of an inert gas are added (a) at constant total pressure, (b) at constant volume and temperature?
8. **$\Sigma\nu=0$.** Show that for $\mathrm H_2+\mathrm I_2\rightleftharpoons2\mathrm{HI}$ the extent is independent of $P$ and find it for $K=50$.
9. **$\Sigma\nu=+1$.** For $\mathrm N_2\mathrm O_4\rightleftharpoons2\mathrm{NO_2}$ ($K=0.15$, start with $1$ mol N$_2$O$_4$) derive $\varepsilon_{\rm eq}(P)$ and evaluate it at $0.1$, $1$, $10$ bar.
10. **Direction.** Water at $373.15$ K is held at $90$ kPa in a closed vessel with liquid and vapour present. Which way does it go and by how much is the chemical potential of the vapour below that of the liquid?
11. **Interior minimum.** Show that $\partial G/\partial\varepsilon\to-\infty$ as $\varepsilon\to0$ and $+\infty$ at the end of the reaction for an ideal-gas reaction, and say what this implies.

> [!example]- Solutions
> 1. $\dot Q=2\times29.10\times175=\mathbf{10\,185}$ W. Gas entropy rise $2\times29.10\ln\frac{473.15}{298.15}=26.88$ W K$^{-1}$. Surface at 500 K: $\dot S_{\rm gen}=26.88-10185/500=\mathbf{6.51}$ W K$^{-1}$; at 800 K: $26.88-12.73=\mathbf{14.15}$ W K$^{-1}$.
> 2. $H_{\rm in}=H_{\rm out}\Rightarrow T_{\rm out}=350$ K. $\dot S_{\rm gen}=5R\ln4=\mathbf{57.63}$ W K$^{-1}$; lost power $300\times57.63=\mathbf{17.29}$ kW.
> 3. $T_f=\gamma T_{\rm line}$: He ($\gamma=\frac53$): $\mathbf{666.7}$ K, $S_{\rm gen}/n=C_p\ln\gamma=\frac52R\ln\frac53=\mathbf{10.62}$ J mol$^{-1}$K$^{-1}$; N$_2$ ($\gamma=\frac75$): $\mathbf{560}$ K, $\frac72R\ln1.4=9.79$ J mol$^{-1}$K$^{-1}$.
> 4. $\Delta S=-R(2\ln0.4+3\ln0.6)=\mathbf{27.98}$ J K$^{-1}$; $\Delta G_{\rm mix}=-T\Delta S=\mathbf{-8.39}$ kJ; $\Delta H_{\rm mix}=0$.
> 5. $-\sum x_i\ln x_i$ is maximal under $\sum x_i=1$ at $x_i=1/N$ (Lagrange multiplier or Jensen: $\sum x_i\ln\frac1{x_i}\le\ln\sum x_i\frac1{x_i}=\ln N$), giving $R\ln N$: $5.763,\ 9.134,\ 13.382$ J mol$^{-1}$K$^{-1}$ for $N=2,3,5$.
> 6. Solve $\dfrac{\varepsilon\sqrt{3-\varepsilon}}{(1-\varepsilon)^{3/2}}=10\sqrt5$: $\varepsilon_{\rm eq}=\mathbf{0.8537}$, $x=(0.1363,\ 0.0681,\ 0.7956)$ for SO$_2$, O$_2$, SO$_3$. Larger than at 1 bar ($0.7645$) because $\Sigma\nu=-\tfrac12<0$: the product side has fewer moles, and higher pressure favours it.
> 7. (a) Dilution: partial pressures fall, equivalent to lower $P$; $\varepsilon_{\rm eq}=0.6667$ (from $0.7645$): a shift back toward reactants. (b) $n_i$, $V$, $T$ unchanged $\Rightarrow$ partial pressures unchanged $\Rightarrow$ $Q$ unchanged: **no shift**.
> 8. $K=\dfrac{(2\varepsilon)^2}{(1-\varepsilon)^2}$ (the pressure factors cancel since $\Sigma\nu=0$) so $\dfrac{2\varepsilon}{1-\varepsilon}=\sqrt K$, $\varepsilon=\dfrac{\sqrt K}{2+\sqrt K}=\dfrac{7.0711}{9.0711}=\mathbf{0.7795}$.
> 9. $n=(1-\varepsilon,2\varepsilon)$, $N=1+\varepsilon$, $K=\dfrac{x_{\rm NO_2}^2}{x_{\rm N_2O_4}}\dfrac P{P^\circ}=\dfrac{4\varepsilon^2}{(1+\varepsilon)(1-\varepsilon)}\dfrac P{P^\circ}$, so $\varepsilon^2(K+4P/P^\circ)=K$, $\varepsilon=\sqrt{K/(K+4P/P^\circ)}$: $\mathbf{0.522},\ \mathbf{0.190},\ \mathbf{0.061}$ at $0.1,\ 1,\ 10$ bar.
> 10. $G^v-G^l\simeq RT\ln(P/P_{\rm sat})-V_l(P-P_{\rm sat})=-367.7+0.2=\mathbf{-367.5}$ J mol$^{-1}$: $G^v<G^l$, so $\mathrm dn^v>0$: **the liquid vaporises** until $P$ rises to $P_{\rm sat}$ (or all of it is vapour).
> 11. $\partial G/\partial\varepsilon=RT\ln(Q/K)$. At $\varepsilon\to0$ a product has $x\to0$ and $\nu>0$, so $Q\to0$, $\ln Q\to-\infty$; at the end a reactant has $x\to0$ and $\nu<0$ so $Q\to\infty$. $G$ falls initially and rises at the end: the minimum is interior, i.e. **$0<\varepsilon_{\rm eq}<$ its maximum for any finite $K$**. For SO$_2$/SO$_3$ at $K=10$: $-15.57$ at $10^{-6}$ and $+18.77$ at $1-10^{-6}$ (in units of $RT$).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | boundaries, measurable versus conceptual variables, the big equation and its special cases, the entropy balance and $\dot S_{\rm gen}$, the Gibbs-energy form, liquid–vapour direction, Clausius–Clapeyron, mixing ($\Delta S_i=-n_iR\ln x_i$, $\Delta H=0$), reacting systems (extent, $\sum\nu_i\mu_i$, $K$ and its pressure dependence), Gibbs–Helmholtz and van 't Hoff | [[Bhagwat.pdf]] (5 pp., all read page by page this session); the photographed originals [[post midsem thermo.pdf]] (28 pp.; **all 28 pages read** in a second pass, rotated and often upside-down: pp. 1–6 the big equation, entropy balance, Helmholtz/Gibbs and the liquid–vapour argument; pp. 7–8 Clausius–Clapeyron; pp. 9–11 the four main equations and the Maxwell relations (TH05); pp. 12–14 mixing of gases; pp. 15–18 reacting systems; p. 19 Gibbs–Helmholtz; p. 20 endo/exothermic diagram; pp. 21–24 Hess, Kirchhoff, calorimetry and the start of microstates ([[TH07 Enthalpy Thermochemistry and Calorimetry]]); pp. 25–28 microstate counting and the Tutorial 3 solutions ([[TH09 Microstates Macrostates and Multiplicity]])) | taught (class notes, inferred) |
> | state postulate | [[post midsem thermo.pdf#page=6\|post-midsem notebook p. 6]] (read at low resolution) | taught (class notes, inferred) |
> | multi-stream and steady-flow forms, heater, throttle, tank-filling examples, numbers for mixing, closed forms and tables for the reactions, inert gas at constant $P$ and $V$, interior minimum, Practice | derived here; `scripts/th10_numbers.py`, `scripts/fig_th10.py`, tool `th_reacting_equilibrium` | extra/beyond |
>
> **Flags.** (1) The "taught" label is inferred: all three PDFs are a classmate's notes. (2) The notebook photographs are rotated and small; the typed Bhagwat pages were the primary reading and the photographs the cross-check; the notebook's extra examples (water-gas shift, mixing of 80/20 N$_2$/O$_2$, Haber remark, 0.7 atm boiling point) were read from pp. 8, 12–18. (3) $K=10$, $0.15$ and $50$ are **illustrative**, not measured equilibrium constants (the notes give none). (4) $C_p=\tfrac72R$ and $\gamma=\tfrac75,\tfrac53$ are the ideal-gas values; no data table was consulted. (5) The notes' steady-state forms for several streams are my generalisation of their single-stream equation.

**References.** No book was consulted for this chapter; every formula comes from the class notes above or is derived here and checked numerically. Background: [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] cites Schroeder §5.1–5.3 and §5.6 for the same equilibrium material.

## Across subjects
- [[CL05 Thermodynamic State of the Atmosphere]] (Climate): the open-system energy and entropy balances (with the moisture term) describe an air parcel; the Clausius–Clapeyron relation of §6 sets saturation.
- [[Inorganic Chemistry - Course Map|Inorganic Chemistry]]: the reaction quotient $Q$, the equilibrium constant and the extent of reaction are the same objects; $\Delta G=-nFE$ for cells.
- [[SM05 The Grand Canonical Ensemble and Chemical Equilibrium]]: the same $K$ from counting states.
