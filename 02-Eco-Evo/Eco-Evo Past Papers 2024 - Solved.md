---
title: Eco-Evo Past Papers 2024 - Solved
aliases: [BI2113 2024, eco evo midsem 2024, eco evo endsem 2024, eco evo assignment 2024]
subject: eco-evo
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/eco-evo, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# Eco-Evo Past Papers 2024 (BI2113): Mid-sem, End-sem and Assignment 1, Solved

[[Ecology and Evolution - Course Map|Course Map]] · [[Eco-Evo Exam Prep]] · other years: [[Eco-Evo Past Papers 2021 - Solved|2021]] · [[Eco-Evo Past Papers 2022 - Solved|2022]] · [[Eco-Evo Past Papers 2023 - Solved|2023]] · [[Eco-Evo Past Papers 2025 - Solved|2025]]

<span class="scope-taught">taught · past papers (Sutirth Dey)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> From the Drive **Question Paper Archive → Sem-3**, downloaded 2026-11-22 to `biology/eco-evo/lecture-notes-slides/past-papers/qp-archive/`:
> - **Mid-sem**, 19 Sep 2024, 40 marks, 11 questions: [[Ecology and Evolution.pdf]] (`Sem - 3 Papers (Aug 2024)/Mid Sem/`, text layer). The same paper as the scan [[EcoEvo-Midsem 2024-Sutirth.pdf]] (`BI2113/`).
> - **End-sem**, 21 Nov 2024, 40 marks, 15 questions: [[Biology - End Sem_2024.pdf]] (OCR text). The same paper as the scan [[EcoEvo-Endsem 2024-Sutirth.pdf]]. The header still reads "Mid-Semester".
> - **Assignment 1** (graded, 20 marks, due 7 Oct 2024): [[Assignment 1.pdf]] (`Sem - 3 Papers (Aug 2024)/Quiz/Graded Assignment of Ecology and Evolution /`).
>
> Matrices and figures were read from the page images. No keys: solutions mine. Numbers (including the simulations for Assignment Q2 and Q4): `scripts/ee_qp_archive_numbers.py`.

## Mid-semester (19 Sep 2024)

> [!question] Q1 (3 × 3) · Distinguish: (a) Type I and Type III survivorship curves (diagram); (b) the population pyramid of a rapidly growing and of a declining population (diagram); (c) sediment dredging and hypolimnetic oxygenation (definition, pros and cons).

> [!example]- Solution ([[Survivorship Curve]], [[Age Pyramid]], [[Lake Restoration Methods]])
> (a) Plot $\log l_x$ against age.
> - **Type I**: flat (high survival) through most of life, then a steep drop at old age. Few offspring, much parental care: humans, large mammals.
> - **Type III**: a steep drop early (huge juvenile mortality), then flat for the few survivors. Many small offspring, no care: oysters, most fish, many plants.
>
> (b) **Rapid growth**: a broad base narrowing steadily upward (a triangle), with each cohort larger than the one before. **Decline**: a **narrow base**, wider in the middle or upper ages (urn- or constrictive shape), because recent cohorts are smaller than older ones.
> (c) **Dredging**: removing the P-rich surface sediment to cut **internal loading**. It removes the stock permanently and works in shallow lakes. But it is expensive, needs disposal sites for the (possibly contaminated) mud, and disturbs the benthos temporarily. **Hypolimnetic oxygenation**: pumping O₂ or air into the deep layer of a stratified lake so the sediment surface stays oxic and P stays bound to Fe(III). It also helps fish and zooplankton. But it is expensive, must run for over 10 years with uncertain permanence, works only in deep stratified lakes, and does not remove the P.

> [!question] Q2 (2) · A stage-structured Leslie-type matrix (fecundities $F_1$–$F_4$ in row 1, $P_1$–$P_3$ on the sub-diagonal); the entry in **row 2, column 3** is marked. What does it mean if it were 0.4 instead of 0?

> [!example]- Solution ([[Lefkovitch Stage-Structured Matrix]])
> Entry $(2,3)$ sends individuals **from stage 3 to stage 2**. A value of 0.4 means **40 % of stage-3 individuals go back to stage 2** at the next step: regression to an earlier stage (as when a plant shrinks to a smaller size class after damage or drought). This is possible only in a *stage* model, never in an age model.

> [!question] Q3 (2) · Five bird species eat fifteen fish species in an island lake; the fish are regulated top-down. The manager exterminates two bird species, yet fish diversity soon drops to five species. Why (birds reproduce much more slowly than fish)?

> [!example]- Solution ([[Predation]], [[Competitive Exclusion Principle]])
> The birds were acting as **keystone predators**. Predation kept the competitively dominant fish below their carrying capacities, so many species could coexist. With less predation, the strongest competitors increased and **excluded the weaker species** by competition. The remaining birds cannot increase fast enough to compensate. The same logic as Paine's *Pisaster* removal: predation can *raise* diversity.

> [!question] Q4 (2) · $\lambda=0.98$ at equilibrium: steps to fall to 50 %?

> [!example]- Solution
> $0.98^n=0.5$ ⇒ $n=\ln0.5/\ln0.98=34.3$ ⇒ **34 steps**.

> [!question] Q5 (2) · Juveniles survive 0.4 a year, and 30 % of the survivors mature; adults survive 0.8 and produce 5 offspring a year; juveniles do not reproduce. The transition matrix?

> [!example]- Solution ([[Lefkovitch Stage-Structured Matrix]])
> Juvenile → juvenile: $0.4\times0.7=0.28$; juvenile → adult: $0.4\times0.3=0.12$.
> $$\begin{pmatrix}J\\A\end{pmatrix}_{t+1}=\begin{pmatrix}0.28&5\\0.12&0.8\end{pmatrix}\begin{pmatrix}J\\A\end{pmatrix}_t\qquad(\lambda=1.36)$$

> [!question] Q6 (2 + 1) · The most likely benefit of synchronised reproduction for migratory wildebeest? Would it work for a stationary population?

> [!example]- Solution ([[Predator Satiation]], [[EE01 Introduction to Biology and Ecological Thinking]])
> **Predator swamping (satiation):** ~80 % of calves are born within about three weeks (≈ 500 an hour at the peak). Predators can kill only a limited number per day, so the *fraction* of calves taken falls, and the calves soon outrun them. Precocial calves stand within minutes.
> **Stationary population: much less effective.** Swamping works when the predators' numbers are set by the lean part of the year and cannot follow the prey's pulse. Resident predators live alongside a stationary herd all year, so their numbers are adjusted to that herd. A resident herd is also small (tens of thousands), so its calf pulse cannot exceed the predators' capacity by much.

> [!question] Q7 (3) · Two hypotheses (besides hunting and the genetic-diversity work) for the extinction of the passenger pigeon, and how likely each is.

> [!example]- Solution ([[EE07 Conservation Biology]] §3, [[Passenger Pigeon Extinction]])
> From the slide's six candidate causes:
> - **Habitat alteration with social facilitation in food finding**: forest clearance reduced the mast (beechnuts, acorns). The birds depended on flock-mates to find unpredictable mast patches, so a smaller population found food less well, which fed back into further decline (an Allee effect; Bucher 1992). **The most plausible**, but the slide says "we do not know".
> - **Climate change or catastrophic events**: **no records**, so unlikely or unsupported.
> - **Disease and parasites**: **no records**.
> - **Competition with domesticated species**: "does not look like the case".

> [!question] Q8 (3) · From one *Azolla*, 10 000 plants cover the pond in 30 days (continuous, density-independent growth). The gardener says two plants would cover it in 15 days. Right? How many are needed for 15 days?

> [!example]- Solution ([[Exponential Growth]])
> $r=\ln(10^4)/30=0.307$ day⁻¹, so in 15 days the population grows by $e^{15r}=100$. Two plants give only **200** by day 15: **the gardener is wrong** (doubling the start saves only one doubling time, 2.3 days). Needed: $N_0=10^4/100=$ **100 plants**.

> [!question] Q9 (2 + 2) · Why must each woman have about 2.1 children for a stable population? Two components; two big assumptions.

> [!example]- Solution ([[Net Reproductive Rate]])
> Stability needs $R_0=1$: each woman replaced by **one daughter who survives to reproduce**.
> - Component 1, **sex ratio at birth** ≈ 105 boys : 100 girls: on average 2.05 children give one daughter.
> - Component 2, **mortality before reproductive age**: some daughters die before reproducing, adding ≈ 0.05 (in low-mortality populations; much more where child mortality is high).
>
> The assumptions: (i) a **closed population** (no migration), and (ii) **constant** age-specific fertility and mortality (and sex ratio) over time, so that the population settles to a stable age distribution. A transient age structure can make a population grow even at replacement fertility (demographic momentum).

> [!question] Q10 (4) · Pixies ($K=250$) and gnomes ($K=300$) alone; mixed from 10 each, they stop at 125 pixies and 250 gnomes. Stable?

> [!example]- Solution ([[Lotka-Volterra Competition Model]])
> At equilibrium $N_P=K_P-\alpha_{PG}N_G$ ⇒ $125=250-250\alpha_{PG}$ ⇒ $\alpha_{PG}=0.5$; $N_G=K_G-\alpha_{GP}N_P$ ⇒ $250=300-125\alpha_{GP}$ ⇒ $\alpha_{GP}=0.4$. The pixie isocline runs $(250,0)$–$(0,500)$; the gnome isocline $(750,0)$–$(0,300)$. Each is outer on the other's axis ($K_P=250<750$, $K_G=300<500$): **stable** ($\alpha\alpha=0.2<1$). Intraspecific competition dominates.

> [!question] Q11 (3 + 3) · Lotka–Volterra predator–prey with density-independent and with logistic prey growth: equations, labelled phase planes (isocline intercepts) and vectors.

> [!example]- Solution ([[Lotka-Volterra Predator-Prey Model]], [[Predator-Prey Cycles]])
> **Density-independent prey:** $\dot N=rN-aNP$, $\dot P=-mP+baNP$.
> - Prey isocline: $\dot N=0$ at $P=r/a$, a **horizontal line**.
> - Predator isocline: $\dot P=0$ at $N=m/(ab)$, a **vertical line**.
> - Vectors: below $P=r/a$ the prey increase (→), above it they decrease (←); right of $N=m/ab$ the predators increase (↑), left of it they decrease (↓).
> - Going round anticlockwise (N on x, P on y): **neutral cycles** around $(m/ab,\ r/a)$, whose amplitude is set by the initial condition.
>
> **Logistic prey:** $\dot N=rN(1-N/K)-aNP$, $\dot P=-mP+baNP$.
> - Prey isocline: $P=\frac ra\big(1-\frac NK\big)$, a **line falling from $(0,r/a)$ to $(K,0)$**.
> - Predator isocline: still $N=m/(ab)$ (vertical); the two must cross, so $m/(ab)<K$.
> - Same vector directions in the four regions, but the trajectories **spiral inward**: **damped oscillations** to a stable equilibrium $\big(\tfrac m{ab},\ \tfrac ra(1-\tfrac m{abK})\big)$. Prey self-limitation stabilises the system.

## End-semester (21 Nov 2024)

> [!question] Q1 (4 × 2) · Distinguish: (a) crop rotation and slash-and-burn; (b) nitrification and denitrification; (c) overdominance and underdominance (1 locus, 2 alleles); (d) mutation accumulation and antagonistic pleiotropy.

> [!example]- Solution ([[EE10 Natural Selection]], [[Modes of Selection]])
> (a) See [[Eco-Evo Past Papers 2021 - Solved|2021]] D5b.
> (b) **Nitrification**: aerobic oxidation NH₄⁺ → NO₂⁻ (*Nitrosomonas*) → NO₃⁻ (*Nitrobacter*). N stays in the ecosystem in a mobile, leachable form. **Denitrification**: anaerobic reduction NO₃⁻ → N₂O → N₂. N is lost to the air.
> (c) **Overdominance**: the heterozygote has the highest fitness ($w_{12}>w_{11},w_{22}$). Selection keeps a **stable polymorphism** at $\hat p=\frac{w_{12}-w_{22}}{2w_{12}-w_{11}-w_{22}}$ (sickle-cell and malaria). **Underdominance**: the heterozygote is the least fit. The interior equilibrium is **unstable**, and one allele fixes depending on the starting frequency.
> (d) See [[Eco-Evo Past Papers 2022 - Solved|2022]] ES Q1b: late-acting deleterious mutations escape weak late selection (MA), against early-benefit/late-cost alleles favoured by selection (AP).

> [!question] Q2 (2) · Long-winged island birds always produce long-winged offspring, so Dr Hypotheticus infers wing length is genetic. Agree?

> [!example]- Solution ([[Heritability]])
> **No.** Parent–offspring resemblance can be **environmental**: the same island, food or rearing conditions, or maternal effects. Showing a genetic basis needs a **common-garden** or **cross-fostering** experiment (raise offspring of long- and short-winged parents in the same environment), or crosses. Also, "always long" with no variation tells nothing about heritability *within* the population.

> [!question] Q3 (2) · Mouse coat: BB brown, bb white, Bb black. Brown is three times as common as black; HWE. Frequency of B?

> [!example]- Solution
> $p^2=3\cdot2pq$ ⇒ $p=6q=6(1-p)$ ⇒ $p=6/7=$ **0.857**.

> [!question] Q4 (2) · A zoo population of rabbits, with enough genetic variation, is released into the wild with no further intervention. After several generations, will it age faster or slower than the zoo ancestors?

> [!example]- Solution
> **Faster.** In the wild, extrinsic mortality (predators, disease, weather) is high, so few individuals reach old age. Selection on late-life traits weakens, and alleles with early benefits and late costs, or late-acting deleterious mutations, spread. Early reproduction is favoured. This is the mirror of [[Eco-Evo Past Papers 2022 - Solved|2022]] ES Q7.

> [!question] Q5 (2) · Human mating is non-random (socio-economic factors, height, behaviour, often with a genetic basis), yet many human loci are in HWE. How?

> [!example]- Solution ([[Hardy-Weinberg Equilibrium]])
> Non-random mating violates HWE **only at loci that affect the traits mates are chosen on** (and loci linked to them). For the great majority of loci (blood groups, most enzymes, neutral markers) mating is **effectively random**: nobody chooses a partner by ABO type. Those loci show HW proportions. And one generation of random mating with respect to a locus restores HWE there.

> [!question] Q6 (2) · Two recessive alleles at the Valar Morgulis locus, VMA and VMB, each cut survival by ~30 % in homozygotes. VMA acts at ages 15–35, VMB at 35–55; no other fitness effects. Both at equal frequency (0.2) now. Which will be commoner in the long run?

> [!example]- Solution
> **VMB.** Its harm comes later, after much of a carrier's reproduction is complete, so it costs less fitness: the **force of selection declines with age** (the logic of mutation accumulation). VMA strikes during the main reproductive years and is selected against more strongly. Both decline, VMA faster.

> [!question] Q7 (2) · How does mapping the nutrient distribution of agricultural fields help combat eutrophication?

> [!example]- Solution
> Fertiliser is applied **only where and as much as needed**, so less surplus N and P runs off into lakes: the external load is cut at the source. See [[Eco-Evo Past Papers 2021 - Solved|2021]] D8b.

> [!question] Q8 (2) · Two reasons small populations are more vulnerable to extinction.

> [!example]- Solution ([[Demographic Genetic and Environmental Stochasticity]], [[Genetic Drift and Inbreeding Depression]], [[EE07 Conservation Biology]] §4)
> Any two:
> - **demographic stochasticity**: chance variation in births, deaths and sex ratio can wipe out a few individuals;
> - **genetic problems**: drift loses variation, and inbreeding depression lowers fitness;
> - **environmental stochasticity and catastrophes** hit all individuals at once;
> - **Allee effects**: mate finding, group defence.

> [!question] Q9 (2) · How does horizontal gene transfer complicate the study of phylogeny?

> [!example]- Solution ([[EE08 Evolution - An Introduction]], [[Extended Evolutionary Synthesis]])
> Phylogenies assume genes pass **vertically**, so a gene's tree tracks the species tree. With HGT a gene can come from a distantly related organism, so **different genes give conflicting trees**. Relationships inferred from one gene can be wrong, and especially among prokaryotes the "tree of life" becomes a **web** (network). Transferred genes must be identified and removed, or networks used.

> [!question] Q10 (2) · Alcohol tolerance by a dominant allele (AA, Aa tolerant), HWE, 19 % tolerant. Fraction of homozygotes among the tolerant?

> [!example]- Solution
> $q^2=0.81$ ⇒ $q=0.9$, $p=0.1$; $p^2=0.01$; $0.01/0.19=$ **0.053**.

> [!question] Q11 (2) · Why does a new recessive beneficial allele take a very long time to fix?

> [!example]- Solution ([[EE10 Natural Selection]])
> When rare, it exists almost only in **heterozygotes, where it is not expressed**, so selection cannot see it. Its increase per generation is $\Delta q\approx sq^2(1-q)$, which is tiny when $q$ is small. It is also likely to be **lost by drift** while rare. (A dominant beneficial allele, by contrast, rises fast at first and slows near fixation, because the recessive allele hides in heterozygotes.)

> [!question] Q12 (2) · Why does inbreeding in captive populations lower mean fitness?

> [!example]- Solution ([[Genetic Drift and Inbreeding Depression]])
> Inbreeding **increases homozygosity**. Rare **deleterious recessive alleles**, normally hidden in heterozygotes, are expressed in homozygotes (inbreeding depression), and any **heterozygote advantage** is lost. Captive populations are small and founded by few individuals, so relatedness accumulates.

> [!question] Q13 (3) · Mars colonists: a disease allele has incidence 1/6000 in the funding ethnic group and 1/500 000 in the rest of the world (both in HWE). The first settlers are all children of ethnic-group fathers and rest-of-the-world mothers; they then mate among themselves (HWE). Frequency of the condition among their offspring? (Round each step to 4 decimals.)

> [!example]- Solution
> $q_E=\sqrt{1/6000}=0.0129$; $q_W=\sqrt{1/500000}=0.0014$. Each settler got one allele from each parent's population, so the settlers' allele frequency is $q=\tfrac12(0.0129+0.0014)=0.0072$ (0.00715). In HWE their offspring are affected at $q^2=0.0072^2=$ **5.2 × 10⁻⁵ ≈ 1 in 19 300**. [!verify] Rounding $q^2$ itself to 4 decimals gives 0.0001; the unrounded value is $5.1\times10^{-5}$ (1 in 19 500). (The settlers themselves are only affected at $q_Eq_W\approx1.8\times10^{-5}$.)

> [!question] Q14 (3) · Sheep horns: one autosomal locus, the horned allele dominant in males and recessive in females. 96 % of males are horned (HWE). Fraction of horned females?

> [!example]- Solution
> Hornless males are the homozygous non-horned genotype: $q^2=0.04$ ⇒ $q=0.2$, $p=0.8$. Females are horned only when homozygous for the horned allele: $p^2=$ **0.64**.

> [!question] Q15 (2 + 2) · Scheffer et al. (2001)'s graph of turbidity against nutrients for shallow lakes, with vegetation and without, with a critical turbidity. Which puzzling limnological observation does it explain, and how?

> [!example]- Solution ([[Shallow Lake Regime Shift]], [[Alternative Stable States]], [[EE06 Eutrophication and Alternative Stable States]])
> **The puzzle:** cutting the nutrient load back to the level at which a lake used to be clear often does **not** restore clear water. Lakes **switch abruptly** between clear and turbid at similar nutrient levels; lakes with the same nutrients can be in either state.
> **The explanation:** vegetation lowers turbidity (it stabilises sediment, takes up nutrients and shelters zooplankton), and turbidity above a critical value kills the vegetation. Over a **range of nutrient levels there are two stable states**: the clear, vegetated branch and the turbid branch. As nutrients rise, the lake stays clear until turbidity on the vegetated branch reaches the critical value, then **jumps** to the turbid branch. To return, nutrients must fall much **lower** (to where the turbid branch drops below the critical value): **hysteresis**. Hence restoration needs a push (biomanipulation) as well as nutrient cuts.

## Assignment 1 (Aug 2024, 20 marks)

> [!question] A1 (1.5 + 1.5) · $\begin{pmatrix}0.4&3\\0.32&0.7\end{pmatrix}$: (a) the ratio of total sizes in successive generations at equilibrium; (b) the juvenile fraction at equilibrium.

> [!example]- Solution ([[Dominant Eigenvalue and Perron-Frobenius Theorem]], [[Stable Age Distribution]])
> $\lambda^2-1.1\lambda+(0.28-0.96)=0$ ⇒ $\lambda=\tfrac12\big(1.1+\sqrt{1.21+2.72}\big)=$ **1.541** (the total grows by this factor). The eigenvector: $(0.4-\lambda)J+3A=0$ ⇒ $A/J=0.380$ ⇒ juvenile fraction $1/1.380=$ **0.724**.

> [!question] A2 (4 × 2) · LV competition: species 1 ($r_1=1$, $K_1=200$, $\alpha_{12}=0.8$), species 2 ($r_2=0.5$, $K_2=300$, $\alpha_{21}=2$). Equilibria from (70, 175), (70, 75), (30, 120), (30, 100), with trajectories on the isocline diagrams.

> [!example]- Solution ([[Lotka-Volterra Competition Model]])
> Isoclines: species 1 runs $(200,0)$–$(0,250)$; species 2 runs $(150,0)$–$(0,300)$. **Each is outer on its own axis**, so the interior crossing at $(66.7,166.7)$ is a **saddle**: whoever gets ahead wins (founder control). A separatrix through the saddle divides the plane. Numerical integration:
> | start $(N_1,N_2)$ | outcome |
> |---|---|
> | (70, 175) | **(0, 300)**: species 2 wins |
> | (70, 75) | **(200, 0)**: species 1 wins |
> | (30, 120) | **(0, 300)** |
> | (30, 100) | **(200, 0)** |
>
> Note that (30, 100) and (30, 120) start close together but end at opposite corners: they lie on either side of the separatrix.

> [!question] A3 (3 + 3) · (a) An insect cohort life table (250 eggs; survivors 239, 210, 156, 129, 109, 76, 43, 32, 19, 9, 0 on days 1–11; eggs per capita 0.551, 0.412, 0.251, 0.99, 0.95, 0.71, 0.49, 0.135 on days 3–10). Growing or declining? (b) A mutant lives two days longer (9 survivors on days 10–12, 0.27 eggs each on days 10–12) but starts breeding a day later (0 on day 3). Beneficial or harmful?

> [!example]- Solution ([[Cohort Life Table]], [[Net Reproductive Rate]])
> $R_0=\sum l_xm_x$ with $l_x=$ survivors/250.
> (a) $R_0=$ **1.263 > 1: increasing**. Euler–Lotka gives $r=0.046$ day⁻¹; $T\approx5.1$ days.
> (b) $R_0=$ **0.944 < 1: the mutant lineage declines** ($r=-0.0095$ day⁻¹). **Harmful.** It loses day 3's large contribution ($l_3m_3=0.344$) and gains only small, late, heavily discounted output. Late reproduction counts for little when few survive to it, and late offspring also lengthen the generation time.

> [!question] A4 (3) · 10 Namibian cheetahs and 30 Sangai deer go into Gandhi Sagar in Jan 2025; LV predator–prey $\dot N=r_1N-CNP$, $\dot P=-d_2P+gCNP$ with $r_1=1.05$, $C=0.1$, $d_2=0.6$, $g=0.45$ per year. The celebration needs exactly 15 cheetahs and 18 sangai. In which year does it first happen?

> [!example]- Solution ([[Lotka-Volterra Predator-Prey Model]])
> **Never.** The LV system conserves $V=gCN-d_2\ln N+CP-r_1\ln P$ along every orbit (neutral cycles). Equilibrium: $N^*=d_2/gC=13.3$, $P^*=r_1/C=10.5$. The starting point has $V(30,10)=-2.108$; the target has $V(18,15)=-2.268$. These are **different orbits**, so the trajectory never passes through (18, 15). The target lies on an inner cycle. Numerically, the orbit from (30, 10) comes closest at about **(19.2 sangai, 18.8 cheetahs) after ~1.1 yr** (early 2026) and every period (~8.4 yr) after that, but never exactly. [!verify] If approximate numbers were acceptable, the answer would be 2026.

## Topic map
| question | topic | vault |
|---|---|---|
| MS Q1a–b, Q2, Q4, Q5; A1, A3 | survivorship, pyramids, matrices, life tables | [[EE02 Structured Population Models]] |
| MS Q8, Q9 | exponential growth, replacement fertility | [[Exponential Growth]], [[Net Reproductive Rate]] |
| MS Q3, Q10; A2 | competition, keystone predation | [[EE04 Competition and Invasions]] |
| MS Q6, Q11; A4 | predation, predator swamping, LV cycles | [[EE05 Predation]] |
| MS Q1c; ES Q7, Q15 | lakes, hysteresis | [[EE06 Eutrophication and Alternative Stable States]] |
| MS Q7; ES Q8, Q12 | passenger pigeon, small populations | [[EE07 Conservation Biology]] |
| ES Q1–Q6, Q9–Q14 | HWE, dominance, ageing, HGT | [[EE09 Hardy-Weinberg Equilibrium]], [[EE10 Natural Selection]], [[EE08 Evolution - An Introduction]] |

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | mid-sem, end-sem, assignment | [[Ecology and Evolution.pdf]], [[Biology - End Sem_2024.pdf]], [[Assignment 1.pdf]] (text + page images); scans [[EcoEvo-Midsem 2024-Sutirth.pdf]], [[EcoEvo-Endsem 2024-Sutirth.pdf]] checked to be the same papers | taught (past papers) |
> | passenger pigeon causes, restoration drawbacks, Lefkovitch matrices | [[EE07 Conservation Biology]] §3, [[Lake Restoration Methods]], [[Leslie Matrix]] (read this session) | vault |
> | numbers and simulations | `scripts/ee_qp_archive_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] The ES Q13 rounding. A4's "never" (the intended answer may be approximate).
