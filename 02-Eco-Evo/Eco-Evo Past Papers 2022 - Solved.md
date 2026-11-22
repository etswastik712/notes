---
title: Eco-Evo Past Papers 2022 - Solved
aliases: [BI2113 2022, eco evo midsem 2022, eco evo endsem 2022]
subject: eco-evo
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/eco-evo, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# Eco-Evo Past Papers 2022 (BI2113): Mid-sem and End-sem, Solved

[[Ecology and Evolution - Course Map|Course Map]] · [[Eco-Evo Exam Prep]] · other years: [[Eco-Evo Past Papers 2021 - Solved|2021]] · [[Eco-Evo Past Papers 2023 - Solved|2023]] · [[Eco-Evo Past Papers 2024 - Solved|2024]] · [[Eco-Evo Past Papers 2025 - Solved|2025]]

<span class="scope-taught">taught · past papers (Sutirth Dey)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> From the Drive **Question Paper Archive → Sem-3 → BI2113**, downloaded 2026-11-22 to `biology/eco-evo/lecture-notes-slides/past-papers/qp-archive/BI2113/`. Both are scans, read as page images:
> - [[BI2113_midsem_22.pdf]]: **mid-sem**, 28 Sep 2022, 120 min, 40 marks, 12 questions;
> - [[BI2113_endsem_22.pdf]]: **end-sem**, 30 Nov 2022, 40 marks, 13 questions. The header still reads "Mid-Semester".
>
> The course's instruction: about 2 sentences per mark. No keys: solutions mine. Numbers: `scripts/ee_qp_archive_numbers.py`. The 2022 course had lectures on **ageing** and some evolution topics that this year's slides do not cover; those answers are marked as general knowledge.

## Mid-semester (28 Sep 2022)

> [!question] Q1 (5 × 2) · Differentiate: (a) Müllerian and Batesian mimicry; (b) the core and buffer areas of a reserved forest; (c) limit cycle and chaos as equilibrium behaviours of a deterministic model; (d) cannibalism and parasitism; (e) character displacement and conditional niche separation as coexistence mechanisms.

> [!example]- Solution ([[Mimicry]], [[Project Tiger]], [[Deterministic Chaos]], [[Predation]], [[Character Displacement]], [[Niche Partitioning]])
> (a) **Batesian**: a palatable mimic resembles a defended model. It is parasitic on the model's warning signal and works only while mimics are rare. **Müllerian**: two or more *defended* species converge on one warning pattern. They share the cost of educating predators, so it is mutualistic.
> (b) **Core**: the inviolate centre kept free of human use (no settlements, grazing or extraction) for breeding wildlife. **Buffer**: the surrounding zone of limited, regulated human use (grazing, fuelwood, tourism). It absorbs edge pressures and conflicts and gives dispersing animals extra space.
> (c) **Limit cycle**: the trajectory settles onto a periodic orbit (the same sequence of values repeats with a fixed period) and is insensitive to initial conditions. **Chaos**: bounded, aperiodic fluctuations with **sensitive dependence on initial conditions** (nearby trajectories diverge exponentially), arising in a deterministic model such as the logistic map at $r\approx3.57$–4.
> (d) **Cannibalism**: killing and eating members of one's own species (intraspecific predation; it acts as density dependence). **Parasitism**: one organism (of another species) lives on or in a host and takes resources, usually without killing it immediately.
> (e) **Character displacement**: an *evolutionary* divergence of traits (e.g. beak size) where the species co-occur, so their resource use overlaps less. It is permanent and heritable. **Conditional niche separation**: an *ecological* outcome in which coexistence or partitioning occurs only under certain conditions (e.g. one species wins in cool, the other in warm patches, or partitioning only when the shared resource is scarce). There is no evolutionary change.

> [!question] Q2 (1) · In a Leslie matrix, what do the zeros on the main diagonal mean (ignore [1,1])?

> [!example]- Solution ([[Leslie Matrix]])
> No individual stays in the same age class from one step to the next: everyone either ages into the next class (sub-diagonal) or dies. In an **age**-classified model one time step = one age class. (A non-zero diagonal is possible only in a **stage** model, where individuals can remain in a stage: [[Lefkovitch Stage-Structured Matrix]].)

> [!question] Q3 (2) · If a prey trait helps individuals avoid detection by predators, can we assume it is a product of coevolution between the two?

> [!example]- Solution ([[Crypsis]], [[EE05 Predation]])
> **No.** Coevolution needs *reciprocal* change: the prey trait evolved in response to *this* predator, and the predator evolved in response. The trait may have evolved against other predators, as an exaptation for something else (thermoregulation, mating), or in response to the predator without any counter-adaptation. Showing coevolution needs evidence of reciprocal selection and change in both lineages.

> [!question] Q4 (2) · When might many individuals in the young age classes (a broad-based population pyramid) *not* indicate a growing population?

> [!example]- Solution ([[Age Pyramid]], [[Stable Age Distribution]])
> - **Very high juvenile mortality**: many young but few survive to reproduce (Type III), so the population may be stable or declining.
> - The young are a **one-off pulse** (an exceptional good year, or immigration of juveniles), not a sustained surplus.
> - Adults are **being removed** (hunting, harvest, disease or emigration of adults), so the base looks broad because the top is cut.
> - The population is **not at the stable age distribution**, so the shape says nothing about $\lambda$.
> - Different survey catchability of the young and adults.

> [!question] Q5 (2) · Why are the physiological effects of very low temperatures often similar to those of drought and salinity?

> [!example]- Solution ([[EE02 Structured Population Models]] temperature reading)
> Freezing turns tissue water into ice, which removes liquid water from cells. The cells are **dehydrated** and their solutes concentrated: exactly what drought (water loss) and salinity (osmotic withdrawal of water) do. So the protective responses overlap: compatible solutes and antifreezes, membrane changes. (Begon et al.'s temperature reading; [!verify] not re-read this session.)

> [!question] Q6 (2) · Two ways an insect can raise its body temperature.

> [!example]- Solution
> **Basking** (orienting to the sun, dark pigmentation, sitting on warm surfaces), and **shivering or wing-whirring**: contracting the flight muscles without flying to generate metabolic heat (bees, moths before take-off). Also clustering (honeybee swarms).

> [!question] Q7 (2) · Advertisement attracts predators, yet many organisms are very conspicuously coloured. Why?

> [!example]- Solution ([[Aposematism]], [[Mimicry]])
> - **Aposematism**: toxic or distasteful prey advertise, so predators learn to avoid them; conspicuousness speeds the learning.
> - **Batesian mimics** profit from that signal.
> - **Sexual selection**: bright males attract mates despite the predation cost.
> - Signals used in species recognition and territorial displays.
> - Colours that look conspicuous to *us* may be cryptic to the predator's visual system or at a distance.

> [!question] Q8 (3) · Continuous logistic $dN/dt=rN(1-N/K)$. Scientist A: max $dN/dt$ depends only on $r$. Scientist B: only on $K$. Who is right? (Not $dN/Ndt$.)

> [!example]- Solution ([[Logistic Growth]])
> **Neither.** $dN/dt$ is maximal at $N=K/2$, where it equals $rK/4$. It depends on **both** $r$ and $K$ (doubling either doubles it). Only the *per-capita* maximum, $r$ at $N\to0$, depends on $r$ alone.

> [!question] Q9 (2 + 1) · Kerala birds: chicks cannot breed in year 1 but all survive to age 1; then they produce 2 offspring a year in that year and the next, 1 in the year after, none after. Annual mortality 60 % in years 2 and 3, 70 % in year 4; none survive beyond year 5. After the 2018 floods: 10 newborns, 5 one-year-olds, 3 two-year-olds. (a) The Leslie matrix. (b) Numbers after one year (no lattice effect).

> [!example]- Solution ([[Leslie Matrix]], [[EE02 Structured Population Models]])
> (a) Classes by age 0, 1, 2, 3 (age 4 has $F=0$ and can be dropped). The course's simple convention: fecundities in row 1, survival on the sub-diagonal. $F=(0,2,2,1)$; survivals $P_0=1$, $P_1=0.4$, $P_2=0.4$ (and $P_3=0.3$ into age 4).
> $$L=\begin{pmatrix}0&2&2&1\\1&0&0&0\\0&0.4&0&0\\0&0&0.4&0\end{pmatrix}$$
> (b) $\mathbf n_0=(10,5,3,0)$ ⇒ $\mathbf n_1=L\mathbf n_0=(2\cdot5+2\cdot3,\ 10,\ 0.4\cdot5,\ 0.4\cdot3)=$ **(16, 10, 2, 1.2)**, with 0 four-year-olds. ($\lambda=1.60$.) [!verify] A post-breeding census would multiply each $F$ by the parents' survival (see [[Leslie Matrix]]); the question's wording suggests the simple form.

> [!question] Q10 (4) · Varanasi, 1000 BC: crops are nitrogen-deficient and there are no chemical fertilisers. What do you advise the king?

> [!example]- Solution ([[Nutrient Limitation]], [[EE06 Eutrophication and Alternative Stable States]])
> Bring in **biological nitrogen fixation** and recycle N:
> - **Crop rotation and intercropping with legumes** (lentils, chickpea, horse gram, pigeon pea): *Rhizobium* nodules fix N₂. Plough the residues in as **green manure**.
> - **Fallow** periods, or a legume fallow.
> - **Animal dung, compost and night soil** returned to the fields. Flooded rice fields with *Azolla*–cyanobacteria (*Anabaena*), which fix N.
> - Silt-laden **flood-plain** fields renewed by the Ganga's floods.
> - Avoid burning residues and waterlogging, which drive denitrification.

> [!question] Q11 (2 + 2) · LV competition: species 1 ($r_1=1.9$, $K_1=100$, $\alpha_{12}=4$), species 2 ($r_2=3.8$, $K_2=20$, $\alpha_{21}=0.15$); they coexist. (a) Is the coexistence stable (graphically)? (b) Equilibrium sizes (calculated).

> [!example]- Solution ([[Lotka-Volterra Competition Model]])
> (a) Isocline of species 1: $(100,0)$–$(0,K_1/\alpha_{12}=25)$. Isocline of species 2: $(K_2/\alpha_{21}=133.3,0)$–$(0,20)$. On the $N_1$ axis species 2's isocline is outside (133 > 100); on the $N_2$ axis species 1's is outside (25 > 20). Each is outer on the *other's* axis, so they cross with each species limiting itself more: **stable** ($\alpha_{12}\alpha_{21}=0.6<1$; vectors point towards the crossing in all four regions).
> (b) $N_1^*=\dfrac{K_1-\alpha_{12}K_2}{1-\alpha_{12}\alpha_{21}}=\dfrac{100-80}{0.4}=$ **50**, $N_2^*=\dfrac{K_2-\alpha_{21}K_1}{0.4}=\dfrac{20-15}{0.4}=$ **12.5**.

> [!question] Q12 (5) · Should the hill behind Panchavati (IISER Pune) become a reserved forest? Factors to consider.

> [!example]- Solution ([[Reserve Design and Management]], [[EE07 Conservation Biology]])
> Ask first **what is to be protected and why**: the species present (the hills hold scrub, grassland and grassland birds, reptiles, perhaps leopard or hyena corridors) and the native vegetation type. Note that the Pune hills are natural **savanna-grassland**, and tree planting would destroy their habitat. Then:
> - **Size and shape**: is the area large and compact enough, with little edge? Can it **connect** (corridors) to other hills (Vetal, ARAI, Pashan), or is it an isolated patch?
> - **People**: walkers, grazing, encroachment, the dependence of nearby communities; a **buffer** and regulated use rather than exclusion.
> - **Threats**: fire, invasive *Gliricidia* and *Lantana*, plantations, roads, quarrying, dogs.
> - **Management**: who manages it, the budget, monitoring, and the legal status (reserved forest restricts access).
>
> A recommendation: protect it as **grassland**, not by afforestation. Link it to the neighbouring hills, regulate rather than ban use, and control fire and invasives. [!verify] The local details are general knowledge.

## End-semester (30 Nov 2022)

> [!question] Q1 (5 × 2) · Differentiate: (a) census and effective population size; (b) mutation accumulation and antagonistic pleiotropy as theories of ageing; (c) catalepsis and crypsis; (d) vertical and horizontal gene transfer; (e) selection and genetic drift as evolutionary forces.

> [!example]- Solution ([[Genetic Drift and Inbreeding Depression]], [[Crypsis]], [[Anti-Predator Behaviour and Chemical Defence]], [[EE08 Evolution - An Introduction]], [[Natural Selection]])
> (a) **Census $N$**: all individuals counted. **Effective $N_e$**: the size of an ideal (Wright–Fisher) population with the same rate of drift or inbreeding. It is usually much smaller because of unequal sex ratio, variance in offspring number and fluctuating size (harmonic mean).
> (b) Both rest on the **declining force of selection with age** (few individuals survive to old ages, so late effects matter little). **Mutation accumulation** (Medawar): deleterious mutations acting only late in life are weakly selected and drift to appreciable frequency; ageing is their summed effect. **Antagonistic pleiotropy** (Williams): alleles that *raise* early fitness but harm late life are favoured *by selection*; ageing is the price of early vigour. (General knowledge; not in this year's slides.)
> (c) **Catalepsis** (thanatosis, "playing dead"): a prey stops moving, often when already caught, so predators that respond to movement lose interest. **Crypsis**: avoiding *detection* in the first place by matching the background (colour, pattern, behaviour).
> (d) **Vertical**: genes passed from parent to offspring (the tree of descent). **Horizontal**: genes moving between contemporaneous organisms, even of different species (bacterial conjugation, transformation, transduction; endosymbiont genes), which makes a web rather than a tree.
> (e) **Selection**: non-random, consistent change in allele frequencies from fitness differences; adaptive; strongest in large populations. **Drift**: random change from sampling of gametes; non-adaptive; strongest in small populations ($\propto1/N_e$); fixes or loses alleles regardless of fitness.

> [!question] Q2 (2) · Many birds live longer than mammals of similar size. Evidence against which theory of ageing?

> [!example]- Solution
> The **rate-of-living (metabolic) theory**: lifespan is inversely related to metabolic rate, as if each organism had a fixed energy budget. Birds have *higher* metabolic rates and body temperatures than same-sized mammals, yet live 2–3× longer. Evolutionary theory explains it: flight lowers extrinsic mortality, so selection maintains late-life fitness. (General knowledge.)

> [!question] Q3 (2) · Four assumptions of the Hardy–Weinberg equilibrium.

> [!example]- Solution ([[Hardy-Weinberg Equilibrium]], [[EE09 Hardy-Weinberg Equilibrium]])
> Any four: a diploid, sexually reproducing organism; non-overlapping generations; **random mating**; **infinitely large population** (no drift); **no selection**; **no mutation**; **no migration**; equal allele frequencies in the sexes (autosomal locus).

> [!question] Q4 (2) · Obesity varies a lot, and obese children often have obese parents. Are these enough to say selection for obesity would succeed?

> [!example]- Solution ([[Heritability]], [[Natural Selection]])
> **No.** Selection needs (i) variation, (ii) **heritable** variation and (iii) **differential fitness**. Parent–offspring resemblance can come from a *shared environment* (diet, habits), not genes, so heritability is not shown. And nothing shows that obese people leave **more offspring**. The response to selection is $R=h^2S$; both $h^2$ and $S$ are unknown.

> [!question] Q5 (2) · Natural selection acts on individuals, yet it is populations that evolve. Justify.

> [!example]- Solution ([[Population Thinking]], [[Natural Selection]])
> An individual's genotype is fixed for life: it survives and reproduces more or less, but it does not change. Evolution is a **change in allele or genotype frequencies across generations**, a property of a population. Selection sorts individuals, and the population's composition shifts as a result.

> [!question] Q6 (2) · 1 locus, 2 alleles, HWE: recessive homozygotes are twice as common as heterozygotes. Frequency of the recessive allele?

> [!example]- Solution ([[Hardy-Weinberg Equilibrium]])
> $q^2=2\cdot2pq$ ⇒ $q=4p=4(1-q)$ ⇒ $q=$ **0.8**.

> [!question] Q7 (2) · Wild rabbits bred in a zoo for several generations: will captive populations age faster or slower than the wild ancestors?

> [!example]- Solution ([[Natural Selection]])
> **Slower**, by evolutionary theory. Captivity removes predators and disease (low extrinsic mortality), so more individuals reach old age and breed then. Selection on late-life survival and fecundity strengthens: late-acting deleterious alleles are purged, and late fitness is favoured over early. This is the logic of the delayed-reproduction experiments in *Drosophila*. Caveat: if the zoo breeds only young animals, the opposite. (General knowledge.)

> [!question] Q8 (1 + 1) · Grasses A and B coexist on the lawns in front of LHC. They produce 100 and 50 seeds per reproductive bout, need at least 200 and 100 g m⁻³ nitrogen respectively, and neither is toxic. Planted in equal proportions, no fertiliser after funds run out, no other species invading, both fast growers but slow reproducers. Which wins, and which principle? (Not Lotka–Volterra.)

> [!example]- Solution ([[Tilman R-Star Rule]], [[Competitive Exclusion Principle]])
> **Grass B**, by Tilman's **$R^*$ rule**: with one limiting resource, the species that can persist at the **lowest resource level** ($R^*$: B 100 versus A 200 g m⁻³) draws nitrogen down below A's requirement and excludes it, whatever A's seed output. (Gause's competitive exclusion, made mechanistic.)

> [!question] Q9 (2) · The Serengeti's millions of wildebeest eat enormous amounts of plant material, yet they increase its vegetation cover. How?

> [!example]- Solution ([[EE01 Introduction to Biology and Ecological Thinking]] §2.4, [[Serengeti Wildebeest Migration]])
> **Grazing reduces fire.** When rinderpest was eradicated, wildebeest numbers rose. Their grazing removes the dry grass that fuels fires, so **less area burns and tree seedlings survive**: tree cover recovers. Grazing also keeps grass short and nutritious (grazing lawns), and dung and urine return nutrients, stimulating regrowth.

> [!question] Q10 (3) · Alcohol tolerance by a dominant allele (AA and Aa tolerant), HWE, 60 % tolerant. Fraction of homozygotes among the tolerant flies?

> [!example]- Solution ([[Hardy-Weinberg Equilibrium]])
> $q^2=0.40$ ⇒ $q=0.632$, $p=0.368$; $p^2=0.135$. Among tolerant flies: $p^2/(p^2+2pq)=0.135/0.60=$ **0.225**.

> [!question] Q11 (3) · Plant A's seeds are wind-dispersed; plant B's are dispersed by herbivores that eat them. Predict number, size and form of the seeds.

> [!example]- Solution
> **A (wind):** **many, small, light** seeds with **wings, plumes or hairs** (high surface area to volume) to stay aloft; few reserves each. **B (herbivore):** **fewer, larger** seeds with **hard, resistant coats** to survive chewing and digestion (often needing gut passage to germinate), inside a **fleshy, nutritious, attractive fruit** as the reward. The trade-off is seed number against seed size.

> [!question] Q12 (3) · Three factors that determine the trophic condition of a lake.

> [!example]- Solution ([[Trophic State of Lakes]], [[Thermal Stratification of Lakes]])
> Any three:
> - **nutrient loading** (P and N inputs: external from the catchment and internal from the sediment);
> - **lake morphometry** (depth and volume: shallow lakes mix sediment nutrients into the light zone);
> - **water residence time and flushing**;
> - **catchment geology and land use**;
> - **climate and stratification** (light, temperature, mixing regime).

> [!question] Q13 (5) · Raptors on Isla Nublar and Isla Sorna, skin colour by 1 locus, 2 alleles; both islands were at HWE. In 1993 disasters struck both. Pre-reproductive mortality and post-disaster numbers:
> | genotype | colour | Nublar mortality | Nublar numbers | Sorna mortality | Sorna numbers |
> |---|---|---|---|---|---|
> | A₁A₁ | black | 0.8 | 200 | 0.3 | 300 |
> | A₁A₂ | brown | 0.2 | 100 | 0.7 | 200 |
> | A₂A₂ | grey | 0.6 | 400 | 0.4 | 100 |
>
> At equilibrium by 2022, with no drift and all other HW conditions holding: the expected frequency of **mature grey** raptors on each island?

> [!example]- Solution ([[EE10 Natural Selection]], [[Modes of Selection]])
> Viabilities $w=1-$ mortality.
> - **Nublar:** $w=(0.2,0.8,0.4)$: **heterozygote advantage (overdominance)**. A stable polymorphism at $\hat p=\dfrac{w_{12}-w_{22}}{2w_{12}-w_{11}-w_{22}}=\dfrac{0.4}{1.0}=0.4$ ($\hat q=0.6$), reached from any start; the post-1993 $p_0=0.357$ is irrelevant. Newborns are at HWE: grey $=q^2=0.36$. After pre-reproductive mortality, mature grey $=\dfrac{q^2w_{22}}{\bar w}=\dfrac{0.36\times0.4}{0.56}=$ **0.257**.
> - **Sorna:** $w=(0.7,0.3,0.6)$: **heterozygote disadvantage (underdominance)**. The interior equilibrium $\hat p=\dfrac{-0.3}{-0.7}=0.429$ is **unstable**. The post-1993 allele frequency is $p_0=\dfrac{2\cdot300+200}{1200}=0.667>0.429$, so A₁ goes to fixation: mature grey frequency **0**.
>
> (The Sorna hurricane killed predators too, but viabilities are given directly.)

## Topic map
| question | topic | vault |
|---|---|---|
| MS Q2, Q4, Q9 | Leslie matrices, pyramids | [[EE02 Structured Population Models]] |
| MS Q1c, Q8 | logistic, chaos | [[EE03 Population Dynamics and Chaos]], [[Logistic Growth]] |
| MS Q1e, Q11; ES Q8 | competition, $R^*$ | [[EE04 Competition and Invasions]] |
| MS Q1a, Q1d, Q3, Q7; ES Q1c | predation, mimicry, crypsis | [[EE05 Predation]] |
| MS Q10; ES Q12 | nutrients, lakes | [[EE06 Eutrophication and Alternative Stable States]] |
| MS Q1b, Q12 | reserves | [[EE07 Conservation Biology]] |
| ES Q1, Q3–Q7, Q10, Q13 | evolution, HWE, selection, ageing | [[EE08 Evolution - An Introduction]], [[EE09 Hardy-Weinberg Equilibrium]], [[EE10 Natural Selection]] |
| ES Q9 | wildebeest and fire | [[EE01 Introduction to Biology and Ecological Thinking]] |

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | questions | [[BI2113_midsem_22.pdf]], [[BI2113_endsem_22.pdf]] (Drive QP archive, 2026-11-22; scans read as images) | taught (past papers) |
> | Leslie conventions, $R^*$, Project Tiger, wildebeest fire, lake restoration | [[Leslie Matrix]], [[EE04 Competition and Invasions]], [[EE07 Conservation Biology]], [[EE01 Introduction to Biology and Ecological Thinking]], [[Lake Restoration Methods]] (read this session) | vault |
> | numbers (Q9, Q11, ES Q6, Q10, Q13) | `scripts/ee_qp_archive_numbers.py` | extra/beyond |
> | ageing theories, seed dispersal, insect thermoregulation, Panchavati | general biology knowledge | extra/beyond |
>
> **Flags.** [!verify] MS Q5 refers to Begon's temperature reading, which I did not re-read. The census convention in MS Q9. The local ecology in MS Q12.
