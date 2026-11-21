---
title: Eco-Evo Exam Prep
aliases: [Eco-evo formula sheet, BI2113 exam prep, Eco-evo revision]
subject: eco-evo
type: moc
scope: [taught, extra-book, extra-beyond]
by: [slides]
status: draft
tags: [subject/eco-evo, type/moc, taught, extra/book, extra/beyond, src/slides, src/book, src/own-notes, status/draft]
---
# Eco-Evo Exam Prep

◀ [[Ecology and Evolution - Course Map|Course Map]] · chapters [[EE01 Introduction to Biology and Ecological Thinking|EE01]] · [[EE02 Structured Population Models|EE02]] · [[EE03 Population Dynamics and Chaos|EE03]] · [[EE04 Competition and Invasions|EE04]] · [[EE05 Predation|EE05]] · [[EE06 Eutrophication and Alternative Stable States|EE06]] · [[EE07 Conservation Biology|EE07]] · [[Eco-Evo Problem Bank|Problem Bank]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] What this page covers and how the scope marks work
> One revision page for the whole course (BI2113), built **from the chapters, not from memory**: every relation below is stated, with its conditions, in the chapter named next to it, and every number was recomputed (`scripts/ee0N_numbers.py`).
> - 🟢 **taught**: on the slides or in the *mandatory* reading. This is the syllabus.
> - 🟡 **extra · book**: from the *paper* or *detailed-reading* tier; the instructor gives these no exam weight.
> - 🔵 **extra · beyond**: my derivations and numerical illustrations, labelled so you can leave them out.
>
> **Rule for the whole course** (slide 18 of lecture 1): slides + mandatory reading = examinable; detailed reading and papers are not. The papers are still worth a skim because the instructor highlights numbers from them.

> [!key] How to use this page
> 1. Learn the **formula sheet** (§1) until you can reproduce a row from its name.
> 2. Read the **traps** (§2) once; each one is a place where a slide, a model or a habit says something slightly different from the truth.
> 3. Do the **derivations** (§3) on paper.
> 4. Cover the answers of the **self-test** (§4) and the **essay prompts** (§5).
> 5. Do calculations in the [[Eco-Evo Problem Bank]] (every answer computed by `scripts/ee_problem_bank.py`).

## 1. Formula sheet
**EE01: thinking tools** (no equations; the numbers are the exam facts)
| Topic | Statement | Numbers | Scope |
|---|---|---|---|
| Why biology is hard to formalise | diverse and interconnected, stochastic, historical, emergent; so statistical, conditional "laws" ([[Emergence and Reductionism]], [[Nomothetic versus Idiographic Science]]) | | 🟢 |
| How vs why | proximate (mechanism) vs ultimate (adaptive benefit) ([[Proximate and Ultimate Causation]]) | | 🟢 |
| Wildebeest | ([[Serengeti Wildebeest Migration]]) | ≈1,500 km yr⁻¹; muscle efficiency 62.6 % (cow 41.8 %, mouse 34 %); 250,000 calves in 3 weeks (80 %); herd ≈ 1.2 million | 🟢 |
| Migration rule | follow forage: intake × nitrogen; rain rises SE → NW (400 → 1,200 mm) | tracking radius > 80–100 km (Holdo) | 🟢 |

**EE02: structured populations** ([[EE02 Structured Population Models]])
| Topic | Relation | Numbers | Scope |
|---|---|---|---|
| Bookkeeping | $N_{t+1}=N_t+B-D+I-E$ ([[Population Ecology]]) | | 🟢 |
| Life table | $l_x=n_x/n_0$, $m_x$, $R_0=\sum_x l_xm_x$ ([[Cohort Life Table]], [[Net Reproductive Rate]]) | *Phlox*: $R_0=2.4177$ | 🟢 |
| Survivorship | constant per-capita risk $q$: $\ln n_x=\ln n_0+x\ln(1-q)$, a straight line on a log axis ([[Survivorship Curve]]) | types I, II, III | 🟢 |
| Generation time, $r$ | $T=\sum xl_xm_x/R_0$, $r\approx\ln R_0/T$ | *Phlox* $T\approx331$ d | 🔵 |
| Euler-Lotka | $1=\sum_xF_xl_x\lambda^{-x}$; $\lambda>1\iff R_0>1$ | slide-16 case: $\lambda^4=\lambda^2+0.1\lambda+0.01$ | 🔵 |
| Leslie matrix | $\mathbf n_{t+1}=\mathbf L\mathbf n_t$; row 1 fecundities, sub-diagonal survivals ([[Leslie Matrix]]) | $\lambda=1.05082$, SAD $(0.635,0.302,0.057,0.005)$ | 🟢 |
| Long-run behaviour | $\mathbf n_t\to c\lambda^t\mathbf w$ ([[Dominant Eigenvalue and Perron-Frobenius Theorem]], [[Stable Age Distribution]]); needs non-negative, irreducible, **primitive** | | 🟢 / 🟡 |
| Stage matrix | $P$ stay, $G$ grow, $F$ fecundity; $P+G=\sigma$ ([[Lefkovitch Stage-Structured Matrix]]) | loggerhead $\lambda=0.9516$ ($-5$ %/yr) | 🟢 |
| Sensitivity, elasticity | $s_{ij}=v_iw_j/(\mathbf v\cdot\mathbf w)$; $e_{ij}=(a_{ij}/\lambda)s_{ij}$, $\sum e_{ij}=1$ ([[Sensitivity and Elasticity of Growth Rate]]) | protect **large juveniles**; eggs alone cannot give $\lambda>1$ | 🟢 / 🟡 |
| TEDs | by-catch 5.7 kg per kg shrimp ([[Loggerhead Turtle and Turtle Excluder Devices]]) | seasonal-offshore use ≈ 70 yr for 10×, full use about half | 🟢 |
| Doubling time | $t_d=\ln2/r$ ([[Age Pyramid]]) | Rwanda $r=0.027$: 25.7 yr; Sweden 0; Hungary $-0.003$ | 🟢 |

**EE03: dynamics and chaos** ([[EE03 Population Dynamics and Chaos]])
| Topic | Relation | Numbers | Scope |
|---|---|---|---|
| Exponential | $N_{t+1}=\lambda N_t$; $N=N_0e^{rt}$; $\lambda=e^r$ ([[Exponential Growth]]) | $t_d=\ln2/r$ | 🟢 |
| Logistic | $\dot N=rN(1-N/K)$; $N=K/[1+\frac{K-N_0}{N_0}e^{-rt}]$ ([[Logistic Growth]], [[Carrying Capacity]]) | inflection $K/2$; max rate $rK/4$; relaxation time $1/r$ | 🟢 |
| Ricker | $n_{t+1}=n_te^{r(1-n_t/K)}$, $g'(K)=1-r$ ([[Ricker Model]]) | stable $0<r<2$; 2-cycle from 2; 4-cycle 2.5265; 8-cycle 2.6564; chaos from 2.6924; **slide's $r=2.5$ is a 2-cycle** | 🟢 / 🔵 |
| Route to chaos | period doubling, Feigenbaum ratio $\to4.669$ ([[Period Doubling and Route to Chaos]], [[Fractals]]) | | 🔵 |
| Chaos | bounded, aperiodic, sensitive: Lyapunov $\Lambda>0$ ([[Deterministic Chaos]]) | Ricker $r=3$: $\Lambda\approx0.39$; horizon $\approx\ln(\text{range}/\delta_0)/\Lambda$ | 🟢 / 🔵 |
| Hassell | $N_{t+1}=\lambda N_t(1+aN_t)^{-\beta}$; $f'(N^*)=1-\beta(1-\lambda^{-1/\beta})$ ([[Hassell Model]]) | 22 of 24 insect populations monotone | 🟢 / 🔵 |
| Resolutions | integer counts ([[Lattice Effect]]); richer models ([[Time-Series Reconstruction]]) | Turchin & Taylor: simple models are biased to stability | 🟢 / 🟡 |

**EE04: competition and invasions** ([[EE04 Competition and Invasions]])
| Topic | Relation | Numbers | Scope |
|---|---|---|---|
| L-V competition | $\dot N_1=r_1N_1(K_1-N_1-\alpha_{12}N_2)/K_1$, and 1↔2 ([[Lotka-Volterra Competition Model]]) | $\alpha_{ij}$ = effect of $j$ **on** $i$ | 🟢 |
| Isoclines | $N_1=K_1-\alpha_{12}N_2$; $N_2=K_2-\alpha_{21}N_1$ ([[Phase Plane and Isoclines]]) | intercepts $K_1,\ K_1/\alpha_{12}$; $K_2,\ K_2/\alpha_{21}$ | 🟢 |
| Outcomes | 1 wins, 2 wins, stable coexistence, unstable (priority) | **3 of 4 are exclusion** | 🟢 |
| Coexistence | $\alpha_{12}<K_1/K_2$ **and** $\alpha_{21}<K_2/K_1$ (so $\alpha_{12}\alpha_{21}<1$, which alone is not enough) | | 🔵 |
| $R^*$ | $R^*=mk/(\mu-m)$ (Monod); lowest $R^*$ wins ([[Tilman R-Star Rule]]) | fast grower at high food can lose | 🟢 / 🔵 |
| Exclusion | $n$ species need $\ge n$ limiting factors ([[Competitive Exclusion Principle]]) | Gause: *P. aurelia* beats *P. caudatum* | 🟢 |
| Niche | hypervolume; fundamental vs realised ([[Ecological Niche]], [[Niche Partitioning]], [[Character Displacement]]) | Park's *Tribolium*: higher $K$ alone does not win | 🟢 |
| Overlap (toy) | $\alpha=\exp(-d^2/4\sigma^2)$ | 0.78 at $d=\sigma$; 0.37 at $2\sigma$ | 🔵 |
| Invasions | ([[Invasive Species]], [[Population Biology of Invasions]]) | Kerala: 28 alien fish + 4 weeds, 7 established | 🟢 / 🟡 |

**EE05: predation** ([[EE05 Predation]])
| Topic | Relation | Numbers | Scope |
|---|---|---|---|
| L-V predator-prey | $\dot H=rH-pHP$, $\dot P=apHP-mP$ ([[Lotka-Volterra Predator-Prey Model]]) | $H^*=m/(ap)$, $P^*=r/p$ | 🟢 |
| Cycles | neutral closed orbits; conserved $V=apH-m\ln H+pP-r\ln P$; small-cycle period $2\pi/\sqrt{rm}$ | predator lags prey | 🟢 / 🔵 |
| Logistic prey | $P^*=(r/p)(1-H^*/K)$, needs $K>m/(ap)$; stable spiral | | 🟢 |
| Volterra's principle | killing both at rate $\delta$: $r\to r-\delta$, $m\to m+\delta$ raises $H^*$, lowers $P^*$ | | 🔵 |
| Hare-lynx | ([[Predator-Prey Cycles]]) Krebs et al. 1995 | predators out ×2, food ×3, both ×11 | 🟢 |
| Experiments | ([[Gause Predator-Prey Experiments]], [[Huffaker Mite Experiment]]) | no refuge: both extinct; refuge: predator extinct; immigration: cycles; Huffaker 120 oranges | 🟢 |
| Metapopulation | Levins: $\dot p=cp(1-p)-ep$, $p^*=1-e/c$ ([[Metapopulation]]) | | 🔵 |
| Functional response | Holling II: $aN/(1+ahN)$, max $1/h$ ([[Functional and Numerical Responses]]) | | 🟡 |
| Defences | ([[Aposematism]], [[Crypsis]], [[Mimicry]], [[Anti-Predator Behaviour and Chemical Defence]], [[Predator Satiation]]) | toxins need warning colours | 🟢 |

**EE06: lakes** ([[EE06 Eutrophication and Alternative Stable States]])
| Topic | Relation | Numbers | Scope |
|---|---|---|---|
| Trophic state | classes by $P_{tot}$ at spring circulation ([[Trophic State of Lakes]]) | < 5, 5–10, 10–30, 30–100, > 100 µg L⁻¹ | 🟢 |
| Retention | $P_L=1.55\,[P_{in}/(1+\sqrt{\tau_w})]^{0.82}$ | halving $P_{in}$ multiplies $P_L$ by $0.5^{0.82}=0.566$ | 🟢 / 🔵 |
| Eutrophication | P → bloom → shade → anoxia → [[Internal Phosphorus Loading]] ([[Cultural Eutrophication]], [[Nutrient Limitation]]) | sewage N:P ≈ 4:1; global P ≈ 1.5 Tg yr⁻¹ | 🟢 |
| Lake Washington | diversion 1968; *Daphnia* back 1976 ([[Lake Washington Recovery]]) | transparency 1 → 3–4 → 10 m | 🟢 |
| Alternative states | ([[Alternative Stable States]], [[Shallow Lake Regime Shift]], [[Causal Loop Diagram]]) | loop $(-)(+)(-)(+)=+$ | 🟢 |
| Box 1 | $\dot x=a-bx+r\frac{x^p}{x^p+h^p}$; bistable iff $\max rf'>b$ | $b=1,r=1.4,h=1,p=8$: window $a\in(0.050,0.626)$; restoring needs a **92 %** cut | 🟡 / 🔵 |
| Restoration | ([[Biomanipulation]], [[Lake Restoration Methods]]) | each method has a stated drawback | 🟢 |

**EE07: conservation** ([[EE07 Conservation Biology]])
| Topic | Relation | Numbers | Scope |
|---|---|---|---|
| Extinction | ([[Extinction Rates]], [[Conservation Ethics]]) | 100–1,000× background; Muir / Pinchot / Leopold | 🟢 |
| Rarity | range × habitat × population: 8 cells, 7 rarities ([[Rabinowitz Rarity Classification]]) | pigeon: wide, narrow, large; tiger: wide, broad, small | 🟢 |
| Pigeon | ([[Passenger Pigeon Extinction]]) | last died 1914; hunting ended ≈ 1878 | 🟢 / 🟡 |
| Extinction risk | $P_{ext}=(d/b)^{N_0}$ even if $b>d$ ([[Demographic Genetic and Environmental Stochasticity]]) | $b/d=1.2$: 26 founders for < 1 % | 🔵 |
| Persistence | mean time $\sim e^{K\ln(b/d)}$ | ×4–5 per +10 at small $K$ | 🔵 |
| Allee | negative per-capita growth below $A$ ([[Allee Effect]]) | $r=0.5,A=20,K=100$: max harvest 26.3 | 🔵 |
| MVP | size for acceptable extinction risk over a stated time ([[Minimum Viable Population]]) | | 🟢 |
| Drift | $H_t=H_0(1-1/2N_e)^t$; $N_e=4N_mN_f/(N_m+N_f)$ ([[Genetic Drift and Inbreeding Depression]]) | half-life $\approx1.39N_e$ | 🔵 |
| Counting | $\hat N=C/\hat p$; Lincoln-Petersen $Mn/m$; Chapman $(M+1)(n+1)/(m+1)-1$ ([[Mark-Recapture Estimation]], [[Tiger Population Surveys]]) | camera trap, buffer ½ MMDM | 🟡 / 🔵 |
| Tigers | ([[Project Tiger]]) | 1,827 (1972) → 2,967 (2018; 2,603–3,346); 70 % of wild tigers | 🟢 |
| Reserves | Diamond's principles, SLOSS ([[Reserve Design and Management]]) | | 🟢 |

## 2. The 28 traps
**EE01-EE02**
1. **Proximate vs ultimate** are different questions about the *same* trait; "calves stand in 6 minutes" is proximate, "this lowers predation" is ultimate. ([[Proximate and Ultimate Causation]])
2. A **log axis** shows per-capita rates: a straight survivorship line is *constant proportional* mortality (type II), not constant numbers dying. ([[Survivorship Curve]])
3. $R_0$ is per **generation**; $\lambda$ per **time step**. They agree only on which side of 1 they lie. ([[Net Reproductive Rate]])
4. Perron-Frobenius needs the matrix **primitive**, not only irreducible: a purely periodic life cycle does not converge to a fixed shape. ([[Dominant Eigenvalue and Perron-Frobenius Theorem]])
5. **Sensitivity** is an absolute slope, **elasticity** a proportional one (sums to 1). The *largest sensitivity* can sit on a transition that cannot be changed, so use elasticities to rank, then ask what is feasible. (Caswell's published figure uses another convention and sums to 1.6.) ([[Sensitivity and Elasticity of Growth Rate]])
6. **Protecting eggs cannot rescue the loggerhead** even if every egg survived; large juveniles have the highest elasticity. ([[Loggerhead Turtle and Turtle Excluder Devices]])
7. Slide statements about TED timing ("occasionally ≈ 70 yr") refer to the paper's *seasonal-offshore* use. `[!verify]` in EE02.

**EE03**
8. $K$ is where $g(N)=N$; **only $r$ decides** stable, cyclic or chaotic in the Ricker model; $K$ just rescales. ([[Ricker Model]])
9. **Slide 25: $r=2.5$ shows a 2-cycle**, not a 4-cycle (the second doubling is at $r=2.5265$). `[!verify]` in EE03.
10. **Chaos is deterministic**, not noise: bounded, aperiodic, sensitive to initial conditions; the forecast horizon grows only logarithmically with precision. ([[Deterministic Chaos]])
11. Integer populations **cannot be strictly chaotic** (finite state space ⇒ eventually periodic), yet cycles can be extremely long. ([[Lattice Effect]])
12. "Natural populations are simple" (Hassell: 22 of 24 monotone) and "complex dynamics are common" (Turchin and Taylor) are reconciled by **model flexibility**, not by different data. ([[Hassell Model]], [[Time-Series Reconstruction]])

**EE04**
13. **Index order**: $\alpha_{12}$ is the effect of species 2 **on** 1.
14. $\alpha_{12}\alpha_{21}<1$ is **necessary, not sufficient**, for coexistence; check $\alpha_{12}<K_1/K_2$ and $\alpha_{21}<K_2/K_1$ separately (example in the [[Eco-Evo Problem Bank]], C1).
15. **3 of the 4 outcomes are exclusion** is a statement about the model, not a claim that exclusion is common. ([[Lotka-Volterra Competition Model]])
16. The **fastest grower at high food can lose**: $R^*$ ranks species at low resource. ([[Tilman R-Star Rule]])
17. **A bigger carrying capacity does not guarantee victory** (Park: *T. castaneum* is larger alone in cool-moist conditions but loses 71 % of contests). ([[Niche Partitioning]])
18. **Competition is non-trophic.** "Reduces the other's growth" is not sufficient; nothing is eaten. ([[Competition]])
19. EE04 slide 8's legend is inverted, so use the text, not the colours, to say which diatom wins. `[!verify]` in EE04.

**EE05**
20. The basic L-V cycle is **neutral and structurally unstable**: any added term (density dependence, refuges) turns closed orbits into spirals. ([[Lotka-Volterra Predator-Prey Model]])
21. **Volterra's principle**: killing predator and prey alike *raises* prey and *lowers* predators.
22. **Gause (b), with a refuge, ends with the predator extinct** (the slide just says "extinction"); without a refuge both die. ([[Gause Predator-Prey Experiments]])
23. **Toxins alone do not save the individual eaten**; the benefit is predator learning, hence warning colours. ([[Aposematism]])
24. A **Batesian mimic is protected only while rarer than its model**. ([[Mimicry]])

**EE06-EE07**
25. A **single criterion** (depth, $P$, Secchi) can misclassify a lake; modern classes use $P_{tot}$ at spring circulation. ([[Trophic State of Lakes]])
26. **Hysteresis**: restoring clear water takes a much larger cut in loading than the rise that caused the collapse (92 % in the Box 1 example). Cutting $P$ is necessary but not sufficient. ([[Alternative Stable States]])
27. $P_{ext}=(d/b)^{N_0}$ is **positive even when births exceed deaths**; and **Allee** thresholds mean a harvest that is sustainable at 100 can collapse the stock at 50. ([[Allee Effect]])
28. **Pugmark censuses failed**; the modern estimate is a model-based $\hat N=C/\hat p$ with a confidence interval (2,967; 2,603–3,346 for 2018). ([[Tiger Population Surveys]])

## 3. Derivations to practise
| Derive | Revise |
|---|---|
| $R_0$, $T$ and $r\approx\ln R_0/T$ from a life table | [[EE02 Structured Population Models]] §2; [[Net Reproductive Rate]] |
| the characteristic equation of a 3-class Leslie matrix; $\lambda>1\iff R_0>1$ | EE02 §4; [[Leslie Matrix]] |
| logistic solution and the inflection at $K/2$ | EE03 §4; [[Logistic Growth]] |
| the Ricker fixed point and $g'(K)=1-r$; the stability range $0<r<2$ | EE03 §5; [[Cobweb Diagram]] |
| isoclines and the four competition outcomes from the intercepts | EE04 §4; [[Phase Plane and Isoclines]] |
| $R^*=mk/(\mu-m)$ from a chemostat | EE04 §3; [[Tilman R-Star Rule]] |
| L-V predator-prey equilibrium, linearisation and the conserved $V$ | EE05 §3–4; [[Fixed Points and Linear Stability]] |
| Levins' equilibrium $p^*=1-e/c$ and the habitat-loss threshold | EE05 §5; [[Metapopulation]] |
| fold points of $\dot x=a-bx+rf(x)$ and the hysteresis loop | EE06 §6; [[Bistability and Tipping Points]] |
| $P_{ext}=(d/b)^{N_0}$ by first-step analysis | EE07 §4; [[Demographic Genetic and Environmental Stochasticity]] |

## 4. Self-test (cover the answers)
1. **Why does a log axis make type II survivorship a straight line?** Constant per-capita mortality $q$ gives $n_x=n_0(1-q)^x$, so $\ln n_x$ is linear in $x$.
2. **State what $\lambda>1\iff R_0>1$ means.** Replacement over a generation and growth per step are the same condition; the numbers differ.
3. **What does the stable age distribution depend on?** Only the matrix, not the starting vector; it is the dominant right eigenvector.
4. **Which loggerhead stage is most worth protecting, and why not the eggs?** Large juveniles: highest elasticity and long stage duration; egg protection alone cannot lift $\lambda$ above 1.
5. **Inflection and maximum growth of the logistic?** At $N=K/2$, rate $rK/4$.
6. **For what $r$ is the Ricker model stable?** $0<r<2$; 2-cycle from 2, 4-cycle from 2.5265, chaos from 2.6924.
7. **Does $K$ change the type of dynamics?** No: only $r$ does.
8. **Why can integer populations not be truly chaotic?** A finite set of states must repeat, so the orbit is eventually periodic; the period can be huge.
9. **What are the four L-V competition outcomes?** Species 1 wins; species 2 wins; stable coexistence; unstable equilibrium (the winner depends on the start).
10. **Who wins on one limiting resource?** The species with the lowest $R^*$.
11. **Fundamental vs realised niche?** The conditions where the species could persist without enemies, versus where it actually does (Connell's barnacles).
12. **Why did Park's *T. castaneum* lose in cool-moist conditions despite a larger equilibrium?** Winning depends on physical conditions and on interaction strength, not on $K$ alone.
13. **Three L-V predator-prey equilibrium facts.** $H^*=m/(ap)$, $P^*=r/p$, neutral cycles with the predator lagging.
14. **What stabilises predator-prey cycles in Gause and Huffaker?** Gause: immigration; Huffaker: a patchy environment with limited dispersal (metapopulation dynamics).
15. **Why does a poison not save the eaten animal?** The animal is already dead; the benefit is predator learning, so poison pairs with a warning signal.
16. **Order of trophic classes by $P_{tot}$.** ultra-oligotrophic < 5 < oligotrophic < 10 < mesotrophic < 30 < eutrophic < 100 < hypereutrophic.
17. **Why is eutrophication self-accelerating?** Bloom shading and decay create hypolimnetic anoxia, which releases sediment P (internal loading).
18. **What did Lake Washington show?** Diverting sewage (1968) restored clarity once *Daphnia* returned (1976): transparency 1 → 3–4 → 10 m.
19. **What is hysteresis in a shallow lake?** The loading at which the lake flips to turbid is higher than the loading at which it flips back.
20. **What does biomanipulation do?** Cuts planktivorous fish so *Daphnia* graze algae and the water clears; a push across the unstable threshold.
21. **Three ethics?** Muir (preserve), Pinchot (resource conservation), Leopold (land ethic).
22. **Why is the passenger pigeon a warning?** The MVP was passed while the species was still common (nomadic mast specialist; habitat loss + social facilitation + hunting).
23. **Why can a growing population go extinct?** With $b>d$, $P_{ext}=(d/b)^{N_0}>0$.
24. **Name the three stochasticities.** Demographic, genetic, environmental.
25. **How is a tiger population counted today?** Camera traps (stripes), capture-recapture models with confidence intervals; not pugmarks.
26. **What does SLOSS ask?** Is a single large reserve better than several small ones with the same total area?
27. **How many tigers in 2018?** 2,967 (CI 2,603–3,346); about 70 % of wild tigers.
28. **What is Volterra's principle?** Indiscriminate killing of predator and prey raises the average prey and lowers the average predator.

## 5. Essay prompts, with the outline an answer needs
1. **Why is biology hard to formalise?** History and contingency; stochasticity; emergence defeating reductionism; so conditional, statistical relations instead of universal laws. Mention the BI2113 response: simple models, concepts, narrative. ([[EE01 Introduction to Biology and Ecological Thinking]])
2. **Why is the wildebeest the dominant herbivore?** Biology (digestion, synchronous calving, muscle efficiency) *plus* environment (opposed rain and fertility gradients, so tracking over ≥ 80–100 km) *plus* the recipe: refuge, ephemeral good resource, connectivity.
3. **Which stage should conservation target, and by how much?** Use elasticity: large juveniles; show with numbers that eggs alone cannot give $\lambda>1$; then say whether TEDs are needed all the time or only at certain seasons.
4. **Reconcile Hassell et al. with Turchin and Taylor.** Same kind of data; the first used a rigid single-lag form biased toward stability; the second a flexible model that finds the whole spectrum.
5. **Competition versus predation.** Competition is non-trophic; both lower growth; the criterion is whether anything is eaten.
6. **Why do most L-V competition cases end in exclusion, and why do we still see coexisting species?** Self-limitation must exceed cross-limitation; niche partitioning, fluctuating conditions, plankton paradox.
7. **Gause and Huffaker as one story.** A closed uniform system collapses; immigration or spatial heterogeneity sustains oscillations.
8. **Why did phosphorus reduction fail in many shallow lakes?** Alternative stable states, hysteresis, buffering by vegetation, internal loading; biomanipulation as a threshold-crossing push.
9. **Compare restoration methods.** Mechanism **and** drawback for each (physical, chemical, biological).
10. **Compare the three ethics.** Spiritual preserve → utilitarian resource → systems land ethic; each gives a different practice.
11. **Why are small populations at risk even when healthy on average?** Three stochasticities, Allee effect, drift; link to MVP.
12. **What do the passenger pigeon and the tiger have in common?** Counts that looked fine until a threshold or a method failed.

## 6. Part IV: evolution (EE08–EE10), added 2026-11-21
<span class="scope-taught">taught</span> *the three evolution lectures and their mandatory readings; the wrap-up lecture says the syllabus is everything in BI2113* · chapters: [[EE08 Evolution - An Introduction]], [[EE09 Hardy-Weinberg Equilibrium]], [[EE10 Natural Selection]]

> [!key] Formula and fact sheet
> - **Frequencies**: $p=P+Q/2$ (always). **HW**: $p^2:2pq:q^2$, $p'=p$; one generation (two if the sexes differ); $2pq\le\tfrac12$; carriers : affected $=2p/q$.
> - **k alleles**: $(\sum p_i)^2$; heterozygosity $1-\sum p_i^2$. **Recessive**: $\hat q=\sqrt{\text{aa}}$, carriers $2pq$, untestable (0 df).
> - **χ²** $=\sum(o-e)^2/e$, df $=1$ for an HW test, critical 3.84.
> - **Blending**: $V_t=V_0/2^t$ (Jenkin). **Drift**: $H_t=H_0(1-1/2N)^t$ (EE07).
> - **Selection** (beyond): $\Delta p=pq[p(w_{11}-w_{12})+q(w_{12}-w_{22})]/\bar w$; overdominance $p^*=t/(s+t)$; $R=h^2S$.
> - **Finches**: 1977 drought 24 vs 130 mm, 84 % died, *Tribulus*, $h^2=0.65$; 1983 El Niño 1359 mm; 2004 + *G. magnirostris*.
> - **History**: Steno, Cuvier (extinction), Buffon (38 forms), Paley (watchmaker), Linnaeus (fixity), Lamarck (4 parts), Darwin (Malthus, Smith, Lyell), Jenkin, Mendel (1866/1900), Fisher–Haldane–Wright, Huxley 1942.
> - **EES**: GR methylation (Weaver 2004), vinclozolin (≥ 4 generations), toadflax *Lcyc*, *Elysia* (retracted).

> [!warning] Traps (Part IV)
> 29. "Lamarck = inheritance of acquired characters": a small, borrowed part of a four-part theory.
> 30. Using $\sqrt{\text{aa}}$ when all three genotypes are visible: use $p=P+Q/2$.
> 31. Sheep problem: carriers **among normal** sheep $=2pq/(1-q^2)$, not $2pq$.
> 32. Taster × taster: condition on the parents being tasters, $P(Tt\mid T\_)=2pq/(p^2+2pq)$.
> 33. A non-significant χ² does not prove HWE (or no selection).
> 34. HW is **neutrally** stable, not stable.
> 35. Selection acts on individuals/phenotypes; evolution is a population change in allele frequencies; **NS is not evolution**.
> 36. Selection is not forward-looking, not progressive; it uses existing variation (preadaptations, trade-offs: *Gambusia*).
> 37. The EES is an extension of the MS, not a refutation (slide 58; Pigliucci).

> [!question]- Self-test (Part IV), answers in the chapters
> 1. Derive HW with assumptions at each step (EE09 §3). 2. Pueblo 83/46/11: $p$, expected, χ² (0.757; 80.3/51.5/8.3; 1.59). 3. PKU 1/11000: $q$, carriers (0.0095, 1/53). 4. Why no CC in the acid-phosphatase sample (expected 0.27). 5. Darwin's chain with Malthus, Smith, Lyell (EE08 §4). 6. The four objections and answers (EE08 §5). 7. The three MS→EES concept shifts with cases (EE08 §7). 8. The four postulates on Daphne Major (EE10 §2). 9. Three Daphne lessons (EE10 §3). 10. Draw directional, stabilizing, disruptive (EE10 Fig. 10.1).

> [!example]- Essay prompts (Part IV)
> - "Nothing in biology makes sense except in the light of evolution" — the two analogies, proximate vs ultimate (EE08 §8).
> - "The Hardy–Weinberg law is boring; the deviations are interesting" — list the assumptions and what each departure does (drift EE07, selection EE10, non-random mating, migration, mutation).
> - "Natural selection is not evolution" — finches, heritability, the nature of selection (EE10 §5).

## Study plan (about 3 hours)
1. 30 min: syllabus maps and **Summary** boxes of EE01-EE07.
2. 40 min: §1 formula sheet, covering columns 2 and 3.
3. 30 min: §3 derivations on paper (choose five).
4. 40 min: [[Eco-Evo Problem Bank]], sections A-D, solutions closed.
5. 40 min: §4 self-test and §5 prompts out loud.

## Provenance
> [!provenance]- Source map
> Formulas, numbers and traps come from the seven chapters, each checked against its slides and mandatory reading; recomputed numbers are in `scripts/ee0N_numbers.py` and `scripts/ee_problem_bank.py`. The essay prompts follow the "likely exam question" boxes of an earlier set of AI-written LaTeX notes (`biology/eco-evo/_progress/main.tex`, `BI2113_Consolidated_Notes.pdf`); I re-derived every outline from the chapters, and those notes are **secondary** (they were not used as a source for any number). Two source issues remain flagged `[!verify]` in the chapters and should go to the instructor: the EE03 slide-25 panel and the EE04 slide-8 legend.
