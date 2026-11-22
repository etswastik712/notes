---
title: Eco-Evo Past Papers 2023 - Solved
aliases: [BI2113 2023, eco evo midsem 2023, eco evo endsem 2023]
subject: eco-evo
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/eco-evo, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# Eco-Evo Past Papers 2023 (BI2113): Mid-sem and End-sem, Solved

[[Ecology and Evolution - Course Map|Course Map]] · [[Eco-Evo Exam Prep]] · other years: [[Eco-Evo Past Papers 2021 - Solved|2021]] · [[Eco-Evo Past Papers 2022 - Solved|2022]] · [[Eco-Evo Past Papers 2024 - Solved|2024]] · [[Eco-Evo Past Papers 2025 - Solved|2025]]

<span class="scope-taught">taught · past papers (Sutirth Dey)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> From the Drive **Question Paper Archive → Sem-3 → BI2113**, downloaded 2026-11-22 to `biology/eco-evo/lecture-notes-slides/past-papers/qp-archive/BI2113/`. Both are phone scans, read as page images:
> - [[eco_evo_midsem_2023_sutirth_compressed.pdf]]: **mid-sem**, 18 Sep 2023, 40 marks, 14 questions;
> - [[eco_evo_endsem_2023_sutirth_compressed.pdf]]: **end-sem**, 22 Nov 2023, 40 marks, 14 questions.
>
> No keys: solutions mine. Numbers: `scripts/ee_qp_archive_numbers.py`.

## Mid-semester (18 Sep 2023)

> [!question] Q1 (5 × 1) · Define: (a) $Q_{10}$; (b) transpiration; (c) top-down regulation of population size; (d) stable age distribution; (e) mean residence time (MRT) of an element.

> [!example]- Solution ([[EE02 Structured Population Models]], [[Stable Age Distribution]], [[Lake Washington Recovery]])
> (a) The factor by which a biological rate increases for a **10 °C rise** in temperature, $Q_{10}=(R_2/R_1)^{10/(T_2-T_1)}$; often ≈ 2.
> (b) Loss of water **vapour from plants**, mainly through the stomata of leaves. It pulls water up the xylem and returns it to the atmosphere.
> (c) Population size held down by **consumers at the trophic level above** (predators, parasites, grazers), rather than by its own resources (bottom-up).
> (d) In a population with constant age-specific survival and fecundity, the **proportions in each age class become constant** over time, while the total grows by $\lambda$ per step: the dominant eigenvector of the Leslie matrix.
> (e) The **average time an atom of the element spends in a reservoir** before leaving it: MRT = stock / throughput flux (at steady state). E.g. the P in a lake: total P ÷ P outflow per year.

> [!question] Q2 (2) · "All populations (plants, animals, microbes) are under some form of environmental control (biotic or abiotic or both)." Agree or disagree?

> [!example]- Solution ([[Density Dependence]], [[Exponential Growth]])
> **Agree.** No population grows exponentially for long: at even modest $r$ it would outstrip any finite resource within a few hundred generations. Every population that persists is therefore bounded by something: resources, predators, disease (biotic), or weather and disturbance (abiotic). The control need not be **density-dependent regulation** towards a fixed equilibrium. Some populations fluctuate widely under density-independent weather and stay bounded only on average. But some control always exists.

> [!question] Q3 (2) · Must a prey trait that helps avoid detection by predators be a product of coevolution?

> [!example]- Solution
> **No.** Coevolution needs reciprocal adaptation in both lineages. The trait could have evolved against other predators, or for other reasons. Same question as [[Eco-Evo Past Papers 2022 - Solved|2022]] MS Q3.

> [!question] Q4 (2) · The return map ($x_{t+1}$ against $x_t$) of the discrete logistic $x_{t+1}=rx_t(1-x_t)$, with the 45° line meeting it at A. The coordinates of A in terms of $r$?

> [!example]- Solution ([[Cobweb Diagram]], [[EE03 Population Dynamics and Chaos]])
> A is the non-trivial fixed point: $x=rx(1-x)$ ⇒ $x^*=1-\dfrac1r$. So **A $=\big(1-\tfrac1r,\ 1-\tfrac1r\big)$** (exists for $r>1$; stable for $1<r<3$ since the slope there is $2-r$).

> [!question] Q5 (2) · In tropical areas birds generally have lower population densities than mammals of the same size. Why?

> [!example]- Solution
> **Energetics.** Birds have higher body temperatures and mass-specific metabolic rates than mammals of the same mass, plus the cost of flight. Each individual needs more energy, so the same resource supports fewer of them. Many tropical birds are also **territorial**, and many feed on fruit or insects (patchy, higher trophic levels), which lowers density further. [!verify] General knowledge; not in this year's slides.

> [!question] Q6 (2) · Two beetle populations of one species, one from Central African rainforest, one from Canadian fields, which show the *reverse* temperature-size rule. How do you tell them apart?

> [!example]- Solution ([[EE02 Structured Population Models]] temperature reading)
> The **temperature-size rule**: ectotherms reared colder reach a larger final size. In the **reverse** rule, size *increases* with temperature, so **the larger beetles are the African (warm) population and the smaller ones the Canadian**. (Rear both at a common temperature to confirm the difference is genetic; tolerance of freezing or chilling would also separate them.)

> [!question] Q7 (2) · *E. coli*: 377 million/ml at 10:00, 415 million/ml at 10:08, density-independent growth. When does it reach 1660 million/ml?

> [!example]- Solution ([[Exponential Growth]])
> $r=\ln(415/377)/8=0.0120$ min⁻¹; $t=\ln(1660/377)/r=123.5$ min ⇒ **≈ 12:03–12:04 PM**. (Doubling time 57.7 min.)

> [!question] Q8 (2) · Why are large carnivores typically rare?

> [!example]- Solution ([[EE07 Conservation Biology]])
> Only ~10 % of the energy at one trophic level reaches the next, so very little energy is available at the top. Large bodies need a lot of energy each. Together these give **few individuals spread over large home ranges**, which also makes large carnivores vulnerable to extinction (Project Tiger's reasoning).

> [!question] Q9 (3) · A campus butterfly breeds once a year (adults die after laying; eggs hatch next year). Larvae: 16 000 m⁻² in 2022, 20 000 m⁻² in 2023; spraying starts at 100 000 m⁻². Density-independent growth at a constant rate: in which year does spraying start?

> [!example]- Solution ([[Exponential Growth]])
> Discrete, non-overlapping generations: $\lambda=20000/16000=1.25$. $20000\times1.25^n\ge100000$ ⇒ $n\ge\ln5/\ln1.25=7.21$ ⇒ $n=8$. (2030: 95 367 < 10⁵; 2031: 119 209.) **2031.**

> [!question] Q10 (3) · Species X (model) and Y (Batesian mimic) share no resources. A virus makes X decline drastically. Effect on Y?

> [!example]- Solution ([[Mimicry]])
> **Y declines.** Batesian protection is **negatively frequency-dependent**: it works because predators that sample the pattern usually get the distasteful model. With few models, predators meet mostly palatable mimics, learn (or never learn to avoid) the pattern, and eat Y. Y loses its protection even though it does not compete with X.

> [!question] Q11 (3) · How does integerisation kill deterministic chaos in simple models, and why does it not rule out complex dynamics?

> [!example]- Solution ([[Lattice Effect]], [[Deterministic Chaos]])
> Population sizes are integers and bounded, so the model has **finitely many states**. A deterministic trajectory must eventually **revisit a state**, and then repeats forever: it is **periodic** (pigeonhole). Strict chaos (aperiodic for ever) is impossible. But the cycles can have **very long periods and long transients** that look chaotic. With noise (demographic stochasticity), a nonlinear model near a chaotic regime still produces irregular, complex fluctuations (Henson et al. 2001's lattice effect in *Tribolium*).

> [!question] Q12 (3) · Butterflies, continuous logistic, $K=500$, $r=0.1$: maximum $dN/dt$ (derive the $N$ first).

> [!example]- Solution
> $N=K/2=250$; $(dN/dt)_{max}=rK/4=$ **12.5**. Same question as [[Eco-Evo Past Papers 2021 - Solved|2021]] D7.

> [!question] Q13 (3 + 1) · Modified logistic: per-capita growth $\frac1N\frac{dN}{dt}$ rises linearly from $-r$ at $N=0$ to $+r$ at $N=M$, then falls with the opposite slope, crossing zero at A (rising) and B (falling). (a) Differential equations and expressions for A and B. (b) Stability of A and B.

> [!example]- Solution ([[Allee Effect]], [[Logistic Growth]])
> (a) Slope $2r/M$.
> - $N\le M$: $\dfrac{dN}{dt}=N\Big(-r+\dfrac{2r}{M}N\Big)=rN\Big(\dfrac{2N}{M}-1\Big)$, zero at **$A=M/2$**.
> - $N\ge M$: $\dfrac{dN}{dt}=N\Big(r-\dfrac{2r}{M}(N-M)\Big)=rN\Big(3-\dfrac{2N}{M}\Big)$, zero at **$B=3M/2$**.
>
> (b) **A is unstable**: per-capita growth is negative below and positive above it, so the population moves away. This is an **Allee threshold**. **B is stable**: positive below, negative above, so it acts as the carrying capacity. $N=0$ is also stable.

> [!question] Q14 (5) · Varanasi, 1000 BC: the crops are **phosphorus**-deficient and there are no fertilisers. What do you advise?

> [!example]- Solution ([[Nutrient Limitation]])
> Phosphorus has **no atmospheric source**: nothing fixes it, so it must be brought in or recycled.
> - **Bones**, crushed or burnt into bone ash (calcium phosphate), the classic early P fertiliser.
> - **Dung, urine and night soil**, composted; animal penning on fields.
> - **Wood and crop ash.**
> - **Fish and fish waste**; bird and bat guano from caves.
> - **Flood silt**: farm the Ganga's annually flooded plains, or carry silt and pond mud to the fields.
> - **Stop losses**: prevent soil erosion (bunds, terraces, cover), and keep crop residues on the land rather than exporting them.
> - Lime acid soils so the P is more available. (Mycorrhiza-friendly practices help uptake.)

## End-semester (22 Nov 2023)

> [!question] Q1 (2 × 2) · Distinguish: (a) microevolution and macroevolution; (b) nitrogen fixation and denitrification.

> [!example]- Solution ([[EE08 Evolution - An Introduction]])
> (a) **Microevolution**: changes in allele frequencies within a population over generations (selection, drift, mutation, gene flow), observable directly. **Macroevolution**: evolution at and above the species level over long times: speciation, origin of higher taxa and novel body plans, diversification and extinction, seen in phylogenies and the fossil record.
> (b) Fixation: N₂ → NH₃ (nitrogenase; *Rhizobium*, cyanobacteria). Denitrification: NO₃⁻ → N₂ by anaerobic bacteria, returning N to the air. See [[Eco-Evo Past Papers 2021 - Solved|2021]] D5c.

> [!question] Q2 (2) · "Natural selection is not necessarily a 'struggle for existence'." Agree or disagree, with reasons.

> [!example]- Solution ([[Natural Selection]], [[Fitness and Relative Fitness]])
> **Agree.** Selection needs only heritable variation in **reproductive success**, not death or direct conflict.
> - Genotypes can differ in **fecundity**, fertility, mating success (sexual selection) or developmental speed while all of them survive.
> - Selection works even when resources are abundant and no one starves: *relative* reproductive output decides.
> - Darwin himself used "struggle" in a "large and metaphorical sense", including dependence of one being on another and success in leaving progeny.

> [!question] Q3 (2) · Moths breeding once a year grow 15 % a year (exponential). Years to double?

> [!example]- Solution
> $1.15^n=2$ ⇒ $n=\ln2/\ln1.15=4.96$ ⇒ **5 years**.

> [!question] Q4 (2) · What role did the Dalai Lama play in tiger conservation in India?

> [!example]- Solution ([[Project Tiger]])
> In **2006** the Dalai Lama publicly urged Tibetans **not to wear or trade the skins of tigers, leopards and otters** (used as trim on traditional *chuba* robes). Tibetans responded with mass **burnings of skins** in Tibet and exile communities. This cut a major market that was driving the poaching of Indian tigers and leopards (much of it smuggled through Nepal to Tibet). [!verify] General knowledge; not in this year's slides.

> [!question] Q5 (2) · The Serengeti's millions of wildebeest were expected to harm other species, yet they increased biodiversity. How?

> [!example]- Solution ([[EE01 Introduction to Biology and Ecological Thinking]] §2.4)
> - Grazing removes the grass fuel, so **fewer fires**, tree recruitment and more woody habitat.
> - Grazing lawns of short, nutritious grass **facilitate smaller grazers** (gazelles).
> - Dung and urine recycle nutrients.
> - Calves and the sick feed predators.
> - River-crossing **carcasses** subsidise fish, crocodiles and scavengers and supply phosphorus over years (Subalusky et al. 2017).
>
> The result is a more heterogeneous, richer system.

> [!question] Q6 (2) · Two criteria used to choose the first nine Project Tiger reserves.

> [!example]- Solution ([[EE07 Conservation Biology]], [[Project Tiger]])
> From the slide's site criteria:
> - **little disturbance**;
> - **high numbers of both prey and predator** ("high development potential");
> - **no drilling, mining or timber operations**;
> - spread **across different states**, to share management responsibility.
>
> The nine: Bandipur, Corbett, Kanha, Manas, Melghat, Palamau, Ranthambhore, Similipal, Sundarbans.

> [!question] Q7 (2) · Protecting turtle eggs and helping hatchlings reach the sea is unlikely to conserve the turtles (Crowder et al. 1994). Why?

> [!example]- Solution ([[Loggerhead Turtle and Turtle Excluder Devices]], [[Sensitivity and Elasticity of Growth Rate]])
> In the stage matrix, $\lambda$ is **least sensitive to egg and hatchling survival and most sensitive to large-juvenile (and subadult) survival**. The early stages already have high losses that are compensated by huge numbers, and each egg has low reproductive value. Even 100 % egg survival cannot make $\lambda>1$. The decline comes from large juveniles drowning in shrimp trawls; **turtle excluder devices** target that stage.

> [!question] Q8 (2 + 1) · Two ways hypolimnetic oxygenation helps restore eutrophic lakes. Why is it not a preferred method?

> [!example]- Solution ([[Lake Restoration Methods]], [[Internal Phosphorus Loading]], [[Thermal Stratification of Lakes]])
> **Helps:**
> - an oxic sediment surface keeps **phosphate bound to iron(III)** in the sediment, which cuts **internal P loading**;
> - it restores oxygen to the deep water for **cold-water fish and zooplankton** (a daytime refuge);
> - it stops the build-up of NH₄⁺, H₂S, Fe²⁺ and Mn²⁺.
>
> **Not preferred:** it is **expensive** and must run for a **long time** (more than 10 years, permanence uncertain, per the slides). It works only in **deep, stratified** lakes, and it treats a symptom: the external load still has to be cut.

> [!question] Q9 (3) · Mendel's first law (segregation of the two alleles in gamete formation) resolved which critical issue with Darwin's theory?

> [!example]- Solution ([[Blending Inheritance]], [[Hardy-Weinberg Equilibrium]])
> The **loss of variation under blending inheritance** (Jenkin's objection). If offspring were the average of their parents, the variance of a trait would **halve every generation** under random mating. A new favourable variant would be diluted out before selection could act, and the variation selection needs would vanish. With particulate genes that segregate intact, alleles are **not diluted**: a recessive allele reappears unchanged, and allele frequencies (and so variation) are conserved from generation to generation (Hardy–Weinberg) unless selection or drift change them.

> [!question] Q10 (3) · HWE; pink-eyed heterozygotes are 34.32 % of the population; red is the more common homozygote colour. Frequency of the red allele?

> [!example]- Solution
> $2pq=0.3432$ ⇒ $p(1-p)=0.1716$ ⇒ $p=\dfrac{1+\sqrt{1-0.6864}}2=\dfrac{1+0.56}2=$ **0.78** (the larger root, since red is commoner).

> [!question] Q11 (3) · Three reasons conservation biologists prefer large reserves to small ones.

> [!example]- Solution ([[Reserve Design and Management]], [[Minimum Viable Population]])
> Any three:
> - **larger populations**: less demographic and genetic stochasticity, less inbreeding, lower extinction risk;
> - **more species** (species–area relation, $S=cA^z$);
> - **less edge per area** (fewer edge effects: poaching, livestock, invasives, microclimate);
> - room for **wide-ranging species** (tigers, elephants);
> - a **minimum dynamic area** that holds patches at all stages of disturbance;
> - more habitat types.

> [!question] Q12 (4) · All rooted vegetation is removed from a shallow temperate lake. Two ways this changes turbidity (the full sequence, saying whether turbidity rises or falls).

> [!example]- Solution ([[Shallow Lake Regime Shift]], [[Alternative Stable States]])
> Each route ends with turbidity **rising**:
> 1. **Sediment stability**: roots and stems no longer anchor sediment or damp waves. Wind and bottom-feeding fish **resuspend sediment**, so turbidity **increases**.
> 2. **Nutrients**: macrophytes no longer take up N and P (or suppress algae by shading and allelopathy). Nutrients go to **phytoplankton**, which bloom, so turbidity **increases**.
> 3. **Refuge**: zooplankton (*Daphnia*) lose their daytime refuge from planktivorous fish. Grazing on algae falls, algae increase, and turbidity **increases**.
>
> The turbid state is then self-reinforcing (no light for plants to return).

> [!question] Q13 (4) · Mice coat colour: black (homozygote) 0.0625, grey (heterozygote) 0.3750, white (homozygote) 0.5625; survival to adulthood 0.8, 0.2, 0.5. Long-run phenotype frequencies?

> [!example]- Solution ([[EE10 Natural Selection]], [[Modes of Selection]])
> Black-allele frequency $p=0.25$. The heterozygote has the lowest fitness, which is **underdominance**. The unstable equilibrium is $\hat p=\dfrac{w_{12}-w_{22}}{2w_{12}-w_{11}-w_{22}}=\dfrac{-0.3}{-0.9}=0.333$. Starting at $p=0.25<0.333$, the black allele declines to **0**. In the long run all mice are **white: black 0, grey 0, white 1**.

> [!question] Q14 (2 + 2) · *Paramecium caudatum* ($K=70$/ml) and *Stylonychia mytilus* ($K=11$/ml); $\alpha_{PS}=5.5$ (effect of *Stylonychia* on *Paramecium*), $\alpha_{SP}=0.12$. (a) The outcome. (b) With $K_S=20$ and $\alpha_{SP}=0.2$?

> [!example]- Solution ([[Lotka-Volterra Competition Model]])
> (a) The *Paramecium* isocline runs from $(N_P,N_S)=(70,0)$ to $(0,70/5.5=12.7)$; the *Stylonychia* isocline from $(11/0.12=91.7,0)$ to $(0,11)$. They cross: each is outer on the other's axis. **Stable coexistence** ($\alpha\alpha=0.66<1$) at $N_P^*=\dfrac{70-5.5\cdot11}{0.34}=$ **27.9**, $N_S^*=\dfrac{11-0.12\cdot70}{0.34}=$ **7.6** per ml.
> (b) The *Stylonychia* isocline is now $(100,0)$–$(0,20)$: **entirely outside** *Paramecium*'s ($100>70$, $20>12.7$). **Stylonychia wins; Paramecium is excluded.**

## Topic map
| question | topic | vault |
|---|---|---|
| MS Q1, Q6 | temperature, definitions | [[EE02 Structured Population Models]] |
| MS Q4, Q11, Q13 | maps, lattice effect, Allee | [[EE03 Population Dynamics and Chaos]], [[Allee Effect]] |
| MS Q7, Q9, Q12; ES Q3 | exponential and logistic growth | [[Exponential Growth]], [[Logistic Growth]] |
| MS Q3, Q10 | mimicry, coevolution | [[EE05 Predation]] |
| MS Q14; ES Q8, Q12 | nutrients, lakes | [[EE06 Eutrophication and Alternative Stable States]] |
| ES Q4, Q6, Q7, Q11 | conservation | [[EE07 Conservation Biology]] |
| ES Q2, Q9, Q10, Q13 | selection, inheritance, HWE | [[EE08 Evolution - An Introduction]], [[EE09 Hardy-Weinberg Equilibrium]], [[EE10 Natural Selection]] |
| ES Q14 | competition | [[EE04 Competition and Invasions]] |

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | questions | [[eco_evo_midsem_2023_sutirth_compressed.pdf]], [[eco_evo_endsem_2023_sutirth_compressed.pdf]] (Drive QP archive, 2026-11-22; scans) | taught (past papers) |
> | temperature-size rule, Project Tiger criteria, Crowder turtles, restoration drawbacks, lattice effect | [[EE02 Structured Population Models]], [[EE07 Conservation Biology]], [[Loggerhead Turtle and Turtle Excluder Devices]], [[Lake Restoration Methods]], [[Lattice Effect]] (read this session) | vault |
> | numbers | `scripts/ee_qp_archive_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] MS Q5 (bird densities) and ES Q4 (Dalai Lama, 2006) are general knowledge.
