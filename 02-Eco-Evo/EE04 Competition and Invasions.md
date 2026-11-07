---
title: EE04 Competition and Invasions
aliases: [EE04, Competition, Lotka-Volterra competition, niche, invasive species, BI2113 lecture 4]
subject: eco-evo
type: chapter
chapter: 4
part: II
scope: [taught, extra-book, extra-beyond]
by: [slides]
status: draft
prereq: ["[[EE03 Population Dynamics and Chaos]]"]
tags: [subject/eco-evo, type/chapter, taught, extra/book, extra/beyond, src/slides, src/book, src/paper, src/own-notes, status/draft]
---
# EE04 · Competition and Invasions

◀ [[EE03 Population Dynamics and Chaos]] · [[Ecology and Evolution - Course Map|Course Map]] · [[EE05 Predation]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**: the lecture of 25 Aug 2026 ([[04-Competition_25-Aug_2026.pdf|31 slides]]) **and** the *mandatory* reading, "relevant sections" of Molles Ch. 13 ([[Ch 13_Ecology Concepts and Applications.pdf|reading]]; the deck does not say which sections are relevant, see §8)
> - §1 what competition is; intra- and interspecific (sl. 1–6)
> - §2 Gause's principle of competitive exclusion; Tilman's experiments (sl. 7–8)
> - §3 the $R^*$ rule for exploitative competition (sl. 9)
> - §4 the Lotka-Volterra competition model, its isoclines and the four outcomes (sl. 10–12)
> - §5 invasive species as super-competitors: Kerala, control, water hyacinth (sl. 13–17)
> - §6 the competition avoiders: the niche, niche partitioning (spatial, temporal, morphological, conditional) (sl. 18–30)
> - §8 the reading slide (sl. 31)
>
> 🟡 **Extra · book**
> - §5 Sakai et al. (2001), *Annu. Rev. Ecol. Syst.* 32: the population biology of invasive species (the *paper* tier; "a nice review of the basic biology of invasive species")
> - §4, §6 further parts of Molles Ch. 13 (13.1 intraspecific competition and self-thinning; 13.4 field experiments) whose tier is not stated
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §3 derivation of $R^*$ from a consumer-resource model; a chemostat simulation in which the *faster-growing* species loses
> - §4 stability by the Jacobian; the condition $\alpha_{12}\alpha_{21}<1$; four outcomes from the isocline intercepts
> - §6 niche overlap as $\alpha$ (a Gaussian-utilisation example)

> [!key] After this chapter you can
> - define **competition**, separate intra- from interspecific, and say what the latter requires (a shared, limiting resource; no eating),
> - state **Gause's principle** and Tilman's **$R^*$ rule**, and explain why a single limiting resource allows only one winner,
> - write the **Lotka-Volterra competition equations**, draw the zero-growth **isoclines**, and name the four outcomes with their conditions,
> - explain why invasive species behave like super-competitors, with the Kerala example,
> - define the **niche** (two meanings) and give an example of each kind of **niche partitioning**,
> - reconcile "exclusion in 3 of 4 L-V regions" with "similar species coexist in nature".

## 1. What competition is
<span class="scope-taught">taught</span> *[[04-Competition_25-Aug_2026.pdf#page=1|slides 1–6]]*

Slide 1 repeats the domain of BI2113 (the ladder of EE01, [[Levels of Biological Organisation]]): this lecture is about the **interactions** between populations within a community, here **competition**.

> [!key] Definition and types (slides 3–6)
> **Competition** is "any use or defence of a resource by one individual that reduces the availability of that resource to other individuals": two groups use the same limited resource, or seek it, to the detriment of one or both ([[Competition]]).
> - **Intraspecific** (between members of one species): the density-dependent fall in growth rate already met in [[EE03 Population Dynamics and Chaos|EE03]] ($r'=r(1-N/K)$ is intraspecific competition), and **competition for mates** (the slide shows a video of antelope males).
> - **Interspecific** (between members of different species): "two populations of different species competing with each other for the same limiting resource. If the species do not affect each other, then there is **no competition**." Two features: it is **non-trophic** (one species does not eat the other) and it **reduces the population growth rate or equilibrium number** of both or at least one of the populations.

> [!intuition] Competing is not fighting
> Two shops on one street compete if the number of customers is limited, whether or not the owners ever meet. What matters is *the shared, limited resource*. Ecologists distinguish *exploitation* (using up the resource) from *interference* (blocking access), but the models of this lecture are about the first kind: the resource level is lowered by every user.

> [!extra-book]- 🟡 Extra (book): Molles §13.1
> Molles also treats *intraspecific* competition in crowded plant stands (self-thinning) and experimental studies. This is in the same chapter but is not developed on the slides.

## 2. Early experiments: Gause's principle
<span class="scope-taught">taught</span> *[[04-Competition_25-Aug_2026.pdf#page=7|slides 7–8]]*

**Gause's experiments.** Slide 7 shows two *Paramecium* species in culture: grown **separately** both rise to a carrying capacity; grown in a **mixed culture**, *P. aurelia* continues to increase while *P. caudatum* declines. Conclusion, stated on the slide:

> [!key] The competitive exclusion principle
> "**No two species with the same niche can co-exist.**" ([[Competitive Exclusion Principle]]) Equivalent working statement: two species competing for the *same* limiting resource cannot coexist at constant population sizes; the better competitor eliminates the other.

**Tilman et al. (1981).** Slide 8 shows the later, more mechanistic experiments on freshwater diatoms (*Asterionella* and *Synedra*, competing for silicate): each species grown alone (panels a, b), then together (panel c). In pure culture each species draws the silicate down to a low steady level; in mixed cultures one species displaces the other. The conclusion on the slide is the single-resource version of Gause: "**two species cannot coexist on a single limiting resource**." The slide notes that the legend of the original Fig. 6 "should be inverted" (the symbols for the two species are swapped in the figure).

> [!verify] Which diatom wins
> Because the slide says its legend is wrong, I do not state from the figure which of *Asterionella* and *Synedra* excluded the other. The $R^*$ rule (§3) says it is the one that holds silicate at the lower level when alone; the original paper (Tilman et al. 1981) would settle it.

## 3. Tilman's $R^*$ rule
<span class="scope-taught">taught</span> *[[04-Competition_25-Aug_2026.pdf#page=9|slide 9]]* · <span class="scope-extra-beyond">extra · beyond</span> *derivation*

Slide 9 states the rule for **exploitative competition** (Tilman 1982):

> [!key] The $R^*$ rule
> "When two or more species are limited by the same resource, the species that can maintain a **positive per capita growth rate at the lowest resource level** will exclude all other species." ([[Tilman R-Star Rule]]) Each species $i$ has a break-even resource level $R^*_i$ at which its growth exactly balances its losses; the species with the smallest $R^*$ wins.

> [!derivation] Why the lowest $R^*$ wins
> Let species $i$ have per-capita growth $f_i(R)$ (increasing in the resource level $R$) and loss rate $m_i$:
> $$\frac{dN_i}{dt}=N_i\big[f_i(R)-m_i\big],\qquad \frac{dR}{dt}=S(R)-\sum_iN_if_i(R)/y.$$
> $N_i$ grows only while $f_i(R)>m_i$, so it can persist only if the resource stays above its break-even level $R^*_i=f_i^{-1}(m_i)$. Alone, species $i$ draws the resource down until $R=R^*_i$ (then $dN_i/dt=0$). Now put species 1 and 2 together with $R^*_1<R^*_2$. Species 1 pushes $R$ down towards $R^*_1$; but at any $R<R^*_2$, $f_2(R)-m_2<0$, so species 2 *declines* even though it is still eating. Species 2 can therefore never persist with species 1. With a Monod response $f(R)=\mu R/(k+R)$ and loss $m$: $R^*=\dfrac{mk}{\mu-m}$.

![[fig_ee04_rstar.png|820]]
*Figure EE4.1. A toy chemostat (my construction). Species A grows faster at high resource but has the higher $R^*$ (0.67); species B has the lower $R^*$ (0.50) and drives the resource down to 0.5, below which A cannot grow.*

> [!example] Worked example 1: the faster grower loses
> $m=0.2$. Species A: $\mu=0.8$, $k=2$ gives $R^*_A=0.2\times2/(0.8-0.2)=0.667$. Species B: $\mu=0.6$, $k=1$ gives $R^*_B=0.2\times1/(0.6-0.2)=0.500$. At a rich resource ($R=10$) A grows faster ($0.667$ against $0.545$). But B reduces $R$ to 0.5, where A's growth is $0.8\times0.5/2.5=0.16<0.20=m$: A declines to extinction, and B settles at $N_B^*=R_{in}-R^*=9.5$. **What matters is not who is fastest when food is plentiful but who can live on the least.**

> [!intuition] The last one at the table
> Imagine a buffet that closes as people eat. The ones who can still feel full on the smallest scraps are the ones left when the dishes are nearly empty. Everyone else, however fast they ate at the start, leaves hungry.

> [!connection] Same idea, other places
> The $R^*$ rule is Gause's principle with a mechanism. It is also why the *carrying capacity* of the environment for each species is tied to its resource requirement ([[Carrying Capacity]]), and why in lakes the species that wins at low phosphorus is not the one that wins at high ([[Nutrient Limitation]], [[EE06 Eutrophication and Alternative Stable States]]).

## 4. The Lotka-Volterra competition model
<span class="scope-taught">taught</span> *[[04-Competition_25-Aug_2026.pdf#page=10|slides 10–12]] · Molles §13.3*

Slide 10 extends the logistic equation of EE03 to two species ([[Lotka-Volterra Competition Model]]):

$$\frac{dN_1}{dt}=\frac{r_1N_1\,(K_1-N_1-\alpha_{12}N_2)}{K_1},\qquad \frac{dN_2}{dt}=\frac{r_2N_2\,(K_2-N_2-\alpha_{21}N_1)}{K_2}$$

where $\alpha$ "is the **coefficient of competition** and denotes the effect of adding one individual of species 2 on the growth rate of species 1". Molles (§13.3) is more precise: $\alpha_{12}$ is the effect of one individual of species 2 on species 1 *relative to the effect of one individual of species 1*: interspecific effects are measured in **intraspecific equivalents**. If $\alpha_{12}>1$ an individual of species 2 hurts species 1 *more* than a conspecific does; if $\alpha_{12}<1$, less. With $\alpha=0$ the species ignore each other and each follows its own logistic.

### 4.1 Isoclines and the four outcomes
Setting each growth rate to zero gives two straight **zero-growth isoclines** ([[Phase Plane and Isoclines]]):

$$\frac{dN_1}{dt}=0:\ N_1=K_1-\alpha_{12}N_2\qquad\qquad \frac{dN_2}{dt}=0:\ N_2=K_2-\alpha_{21}N_1.$$

Above (outside) its isocline a species decreases; below it increases (Molles Fig. 13.14). Species 1's line meets the $N_1$ axis at $K_1$ and the $N_2$ axis at $K_1/\alpha_{12}$; species 2's line meets the $N_2$ axis at $K_2$ and the $N_1$ axis at $K_2/\alpha_{21}$. Which line lies outside the other decides the outcome (slide 11 shows three of the four pictures: "species $i$ wins", "stable equilibrium", "unstable equilibrium"):

| outcome | intercept conditions | in words |
|---|---|---|
| species 1 wins | $K_1>K_2/\alpha_{21}$ and $K_1/\alpha_{12}>K_2$ | 1 hurts 2 more than 2 hurts 1 |
| species 2 wins | $K_2>K_1/\alpha_{12}$ and $K_2/\alpha_{21}>K_1$ | the reverse |
| **stable coexistence** | $K_1<K_2/\alpha_{21}$ and $K_2<K_1/\alpha_{12}$, i.e. $\alpha_{12}<K_1/K_2$, $\alpha_{21}<K_2/K_1$ | each limits itself more than the other |
| unstable equilibrium | $K_1>K_2/\alpha_{21}$ and $K_2>K_1/\alpha_{12}$ | each limits the other more than itself: the starting ratio decides the winner |

![[fig_ee04_lv.png|900]]
*Figure EE4.2. The four outcomes in the $(N_1,N_2)$ plane for $K_1=100$, $K_2=80$ (my construction). Blue: species 1's isocline; orange: species 2's. Grey curves are trajectories. Filled dots are stable equilibria, open dots unstable.*

> [!example] Worked example 2: a coexistence equilibrium, and an unstable one
> **Panel C:** $\alpha_{12}=0.5$, $\alpha_{21}=0.6$. The conditions $\alpha_{12}<K_1/K_2=1.25$ and $\alpha_{21}<K_2/K_1=0.8$ hold. Solve the isocline pair: $N_1^*=\dfrac{K_1-\alpha_{12}K_2}{1-\alpha_{12}\alpha_{21}}=\dfrac{100-40}{0.70}=85.7$, $N_2^*=\dfrac{K_2-\alpha_{21}K_1}{1-\alpha_{12}\alpha_{21}}=\dfrac{80-60}{0.70}=28.6$. Check: $100-0.5(28.6)=85.7$ ✓. Each species is *below* its own carrying capacity (85.7 against 100; 28.6 against 80) because of the other.
> **Panel D:** $\alpha_{12}=\alpha_{21}=1.5$: the interior point $(16,56)$ is a **saddle**; trajectories are drawn toward one axis or the other, depending on which species starts relatively more abundant (a **priority effect**). Both single-species states $(100,0)$ and $(0,80)$ are stable.

> [!derivation] Stability of the coexistence point
> At the interior equilibrium the Jacobian is $J=\begin{pmatrix}-r_1N_1^*/K_1&-r_1\alpha_{12}N_1^*/K_1\\-r_2\alpha_{21}N_2^*/K_2&-r_2N_2^*/K_2\end{pmatrix}$. Its trace is negative, and
> $$\det J=\frac{r_1r_2N_1^*N_2^*}{K_1K_2}\,\big(1-\alpha_{12}\alpha_{21}\big).$$
> The point is stable ($\det>0$, $\mathrm{tr}<0$) **iff $\alpha_{12}\alpha_{21}<1$**, the geometric mean of the interspecific effects must be weaker than the intraspecific effect (see [[Fixed Points and Linear Stability]] for the 2-D criterion). For panel C the eigenvalues are $-0.50$ and $-0.107$ (a relaxation time of about 9 time units for the slower one); for panel D, $\alpha_{12}\alpha_{21}=2.25>1$ and the eigenvalues are $+0.07$ and $-0.50$ (a saddle).

> [!key] Main message (slide 12)
> "**In 3 out of 4 conditions the model predicts that one species would drive another to extinction.** As noted earlier, this result agrees well with at least some experiments [Gause, Tilman, Park]. What about real life? Ans: **it is complicated…**" Only when *each species limits itself more than it limits the other* does the model allow coexistence.

> [!pitfall] Common slips
> - $\alpha_{12}$ is the effect of species **2 on 1** (second index = the source). Mixing up the order reverses which isocline is which.
> - Unequal $K$ matters: the coexistence thresholds are $K_1/K_2$ and $K_2/K_1$, not 1, unless $K_1=K_2$.
> - $\alpha$ can exceed 1 without implying exclusion if the other $\alpha$ is small enough that $\alpha_{12}<K_1/K_2$.
> - Exclusion in the model takes time: the loser declines gradually along the trajectory.

> [!extra-book]- 🟡 Extra (book): Molles Ch. 13 on models and experiments
> Molles opens §13.3 with Mertz's (1972) summary of the *Tribolium* "model" (an abstraction, not a facsimile, of nature; partly empirical, partly deductive; used to get insights into nature) and then develops the same logistic extension and isocline argument as the slides, followed by laboratory models (Gause's *Paramecium*, Park's *Tribolium*) and field studies. §13.2 on competitive exclusion illustrates niche overlap with the **feeding niches of Darwin's finches**.

## 5. Super-competitors: invasive species
<span class="scope-taught">taught</span> *[[04-Competition_25-Aug_2026.pdf#page=13|slides 13–17]]* · <span class="scope-extra-book">extra · book</span> *Sakai et al. 2001*

Slide 13 turns from the lab to the real world: **invasive species** as "the case of the super-competitors" (a short film on the threat). In the L-V language, an invader that arrives without its natural enemies and with a high resource-use efficiency has a large $\alpha_{\text{invader}\to\text{native}}$ and a small $\alpha_{\text{native}\to\text{invader}}$: the model's species-1-wins region ([[Invasive Species]]).

> [!example] Worked example 3: Kerala after the floods (slide 14)
> The **2018 and 2019 floods in Kerala** carried aquaculture and aquarium fishes into open waters: the **arapaima** (*Arapaima gigas*, can reach 200 kg) and the **alligator gar** (can reach 137 kg, caught from the Kurumali River). The **2021 update** (Raj et al., *Aquatic Ecosystem Health & Management* 24(2): 64–75): a survey of **44 rivers and 53 reservoirs** found **28 alien fish species and four alien aquatic weeds (macrophytes)**, of which **7 have established natural populations**; the main routes were the **aquarium trade and aquaculture**. Reading in model terms: the many aliens that appear but do not persist correspond to introductions that fall in the "native wins" region; the seven established ones are those for which the invader's effective $\alpha$ is large enough or the native's resistance too low.

**Control and use (slides 15–17).** Slide 15 raises the human angle, *controlling* invasive species; slide 16 describes **uses of the water hyacinth in India**: Kottapuram Integrated Development Society (KIDS) in Kerala (300 women in Paravur trained to make crafts), the Assam State Rural Livelihoods Mission (mats, baskets, handicrafts) and Shantipur in West Bengal (cotton sarees woven from a 30:70 mix with cotton). Slide 17 lists two self-study cases (**Asian carps**, with a 2017 *Guardian* update on the Great Lakes, and the alga ***Caulerpa taxifolia***). These slides turn a pest into a resource.

> [!pitfall] A model is not a manual
> The super-competitor picture is a *qualitative* summary. Whether an introduced species becomes invasive also depends on how many individuals arrive and how often, on whether the new site is disturbed, and on genetic and demographic accidents at low numbers (the paper below). Competition is one of several mechanisms.

> [!extra-book]+ 🟡 Extra (book): Sakai et al. (2001), "The population biology of invasive species"
> A review by fifteen population biologists ([[Sakai+_AREES_2001_The Population biology of invasive species.pdf#page=1|Annu. Rev. Ecol. Syst. 32: 305–332]]): contributions from **population biology** can help understand and manage invasiveness; invasive species are also natural experiments in rapid evolution.
> - **Life-history traits.** Baker's "ideal weed" (1965, 1974: sexual and asexual reproduction, fast growth to maturity, plasticity and tolerance of heterogeneity); more recent comparisons find that no simple trait list predicts success, though some patterns hold (e.g. discriminant analysis classified 86 % of woody invaders correctly using vegetative reproduction and other traits); successful colonists are often *r*-selected; Newsome and Noble's "gap grabbers, competitors, survivors, swampers".
> - **Introduction.** Most long-distance introductions are the direct or indirect result of human activity, deliberate (forage, ornamentals, the pet trade) or accidental (ballast water, crop seed).
> - **Colonisation and establishment.** Isolated individuals that can self-fertilise, or that have several reproductive modes, are good colonists; small founding populations suffer demographic accidents and **bottlenecks**.
> - **Genetics and evolution.** A founding bottleneck reduces genetic diversity (Argentine ants are less diverse in the introduced than in the native range); this risks **inbreeding depression** and limits adaptive evolution; **lag times** between arrival and spread may reflect the time evolution needs.
> - **Invasibility of communities** is an *emergent* property, shaped by species interactions, mutualisms, disturbance and habitat fragmentation; models of range expansion help to predict spread.
> - **Management.** Demographic (life-cycle) models identify the stage at which control is most effective, which is the stage-structured idea of [[EE02 Structured Population Models]] ([[Population Biology of Invasions]]).

## 6. The competition avoiders: niches and partitioning
<span class="scope-taught">taught</span> *[[04-Competition_25-Aug_2026.pdf#page=18|slides 18–30]]*

Slide 18 states the puzzle: despite the glaring examples of invaders, "in nature **lots of species with similar niches do seem to coexist**. How is that possible?" Before answering, the slide asks: *what is a niche?*

### 6.1 The niche
Slide 19: **the ecological niche is an $n$-dimensional hypervolume** ([[Ecological Niche]]). The three examples (taken from Begon and Townsend, the same chapter as the EE02 temperature self-study) have one, two and three axes: (a) the range of **temperature** at which Alpine plant species achieve net photosynthesis at low light; (b) for the sand shrimp *Crangon septemspinosa*, the fate of egg-bearing females over **temperature and salinity**; (c) a diagrammatic niche for an aquatic organism as a volume defined by **temperature, pH and food availability**.

Two meanings (slides 20–21; after Schoener, *Ecological Niche*):

> [!key] Two definitions of "niche"
> **Population-persistence niche** (Hutchinson): "a quantitative description of the range of environmental conditions that allow a population to persist in some location", where *persist* means **positive growth rate**. **Resource-utilisation niche** (MacArthur, Levins): focuses entirely on "what members of a species population in some locality *actually do*, in particular how they use resources". Typical axes (slide 22): **habitat** (micro- such as height in vegetation; macro- such as vegetation zone), **food type** (size, hardness) and **time** (daily and seasonal activity).

Slide 23 quotes Hairston (1995): "Ecology's love-hate relationship with the niche concept has been long and not especially pretty." The concept is useful but slippery (the persistence niche is about *where a species can live*, the utilisation niche about *what it does*, and the two need not coincide).

### 6.2 Partitioning the niche
Slide 24–25: **coexistence is possible if there is a separation (partitioning) of the niche**: resource partitioning that is **spatial, temporal or morphological**, or **conditional niche differentiation**.

> [!intuition] Partitioning in the L-V picture
> Competition coefficients measure overlap. If two species use a resource axis with bell-shaped utilisation curves of width $\sigma$ whose centres are $d$ apart, the overlap is $\alpha=\exp\!\big(-d^2/4\sigma^2\big)$: 1 for identical species, 0.78 when $d=\sigma$, 0.37 when $d=2\sigma$ (my illustration of the MacArthur-Levins idea). Partitioning lowers $\alpha$ until $\alpha_{12}\alpha_{21}<1$ and the coexistence conditions of §4 hold. Separation turns "3 of 4 exclusion" into coexistence by *changing the parameters*, not by changing the model.

| type | example (slide) | what separates the species |
|---|---|---|
| **spatial** | *Paramecium caudatum* and *P. bursaria* (Gause) | *P. caudatum* feeds in the **top** layers of the culture, *P. bursaria* in the **bottom**: they coexist (slide 26) |
| **spatial** | Connell's barnacles, *Balanus balanoides* and *Chthamalus stellatus* (slide 27) | vertical zones of a rocky shore |
| **temporal** | common spiny mouse (*Acomys cahirinus*) and golden spiny mouse (*A. russatus*) | one nocturnal, one diurnal (slide 28) |
| **morphological** | Galápagos finches; character displacement (slide 29) | beak size differs where species co-occur |
| **conditional** | *Tribolium confusum* and *T. castaneum* (Park) | the winner depends on temperature and humidity (slide 30) |

**Connell's barnacles (slide 27).** On a rocky shore *Chthamalus* occupies the **upper** intertidal zone and *Balanus* the **middle** and lower. The slide's explanation by zone: in the upper zone *Balanus* **desiccates**, which allows *Chthamalus* to thrive; in the middle zone, where it can survive, *Balanus* **outcompetes** *Chthamalus* for space; in the lower zone *Balanus* is subject to **predation**. The slide asks "why such a distribution?": the answer is an interplay of the **physical limits** on one species (above) and **competition** with it (below). The niche a species *occupies* (realised) is narrower than the one it *could* occupy (fundamental).

**Spiny mice (slide 28).** The two species coexist in the deserts of Israel and overlap in habitat (rocky areas), food (they prefer arthropods) and reproductive season. When the common spiny mouse was **experimentally removed**, the golden spiny mouse **became nocturnal** (Shkolnik 1971; Kronfeld-Schor and Dayan 1999): evidence that the diurnal habit is a *consequence* of competition, i.e. the temporal separation was *induced*.

**Character displacement (slide 29).** "The phenomenon by which character traits of two or more closely related species differ **more when they occur together** than when they occur in different geographical areas" ([[Character Displacement]]). The slide's figure shows beak-depth distributions of Galápagos ground finches (*Geospiza fuliginosa*, *G. fortis*, *G. magnirostris*) on several islands (Pinta and Marchena; Floreana and San Cristóbal; Daphne; Los Hermanos): the distribution on an island depends on which other species are present.

![[04-Competition_25-Aug_2026.pdf#page=29&height=360]]
*Slide 29: beak depth of Galápagos ground finches on different islands.*

### 6.3 Conditional outcomes: Park's flour beetles
Slide 30 reproduces the table of **Thomas Park (1954, 1962)**: *Tribolium confusum* and *T. castaneum*, at **cool (24 °C), moderate or warm (34 °C)** temperature and **dry (30 % RH) or moist (70 % RH)** conditions. "Equilibrium population size" is the number of adults, larvae and pupae per gram of flour of each species when it is grown alone; "contests won" is the percentage of 20–30 two-species contests won.

| condition | alone: *confusum* / *castaneum* | contests won: *confusum* / *castaneum* |
|---|---|---|
| cool, dry | 26.0 / 2.6 | 100 / 0 |
| cool, moist | 28.2 / **45.2** | **71** / 29 |
| moderate, dry | 29.7 / 18.8 | 87 / 13 |
| moderate, moist | 32.9 / 50.1 | 14 / 86 |
| warm, dry | 23.7 / 9.6 | 90 / 10 |
| warm, moist | **41.2** / 38.3 | 0 / **100** |

> [!example] Worked example 4: reading Park's table
> (i) The **same two species** reach opposite outcomes in different physical conditions: *confusum* wins cool-dry (100 %), *castaneum* wins warm-moist (100 %). That is **conditional** niche separation; in a fluctuating environment neither wins permanently, and the loser can persist. (ii) **A higher equilibrium size does not guarantee victory** (the slide's own point): in *cool, moist* conditions *castaneum* reaches 45.2 against 28.2 when alone yet loses 71 to 29; in *warm, moist* conditions *confusum* is larger (41.2 against 38.3) and loses all 20–30 contests. In L-V terms, $K$ (the single-species equilibrium) is only half of the story: the competition coefficients decide the contest.

> [!pitfall] Do not read "alone" and "together" the same way
> A species' own carrying capacity $K_i$ tells you how it does with no competitor. Whether it wins also depends on $\alpha$, which here changes with temperature and humidity. Predicting a winner from the biggest $K$ is the commonest wrong answer.

## 7. Reconciling exclusion and coexistence
![[EE04 Exclusion or Coexistence.svg|760]]
*Figure EE4.3. Exclusion and coexistence in one picture. Editable: [[EE04 Exclusion or Coexistence.excalidraw]].*

- **Exclusion** is expected when two species share *one* limiting resource and the same niche (Gause, $R^*$), when each hurts the other more than itself ($\alpha_{12}\alpha_{21}>1$, or one-sided), and when a super-competitor arrives without enemies (invasions).
- **Coexistence** is expected when niches are **partitioned** (space, time, morphology), when each species is limited chiefly by *itself* ($\alpha_{12}\alpha_{21}<1$) or when the environment **changes the winner** over time or place (conditional).
- The lecture's lesson (slide 12 and the pedagogical stance of EE01): the **model gives a precise question** (what must be true for coexistence?), and the answer in nature is found by testing *which* of those conditions holds, in experiments such as Gause's, Connell's, Park's and the spiny-mouse removal.

## 8. Reading tiers
<span class="scope-taught">taught</span> *[[04-Competition_25-Aug_2026.pdf#page=31|slide 31]]*

| item | tier |
|---|---|
| lecture slides | syllabus |
| "Relevant sections of Chapter 13", Molles | **mandatory**, syllabus |
| Sakai et al. (2001), *Annu. Rev. Ecol. Syst.* 32: 305–332 | paper ("a nice review of the basic biology of invasive species") |

> [!verify] Which sections of Molles Ch. 13 are "relevant"?
> The deck says only "relevant sections". By the slide content, §13.2 (competitive exclusion and niches) and §13.3 (the L-V model and laboratory models) are clearly relevant; §13.1 (intraspecific competition) and §13.4 (field experiments) are probably background. This chapter treats the first two as syllabus and notes the others; ask the instructor if the exam might draw on them.

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Two competitors: isoclines decide who wins
> Lotka–Volterra competition: dN₁/dt = r₁N₁(K₁ − N₁ − α₁₂N₂)/K₁ and the mirror equation for species 2.
>
> ![[ee_competition.png|720]]
>
> **Try:** K₁ = 100, K₂ = 80, α₁₂ = 0.5, α₂₁ = 0.6 → stable coexistence at (85.7, 28.6). Set both α = 1.5 → saddle at (16, 56): click on either side of the separatrix and watch the winner change.
>
> [▶ Open the tool in your browser](../Assets/interactive/ee_competition.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/ee_competition.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How EE04 connects
> **Builds on:** [[EE03 Population Dynamics and Chaos]] (the logistic is the one-species limit of L-V) and [[EE02 Structured Population Models]] (stage models identify the best control stage for invaders).
> **Leads to:** [[EE05 Predation]] (a different two-species interaction with the same phase-plane tools; Gause's predator-prey experiments) → [[EE06 Eutrophication and Alternative Stable States]] ($R^*$ and nutrient limitation; invasive mussels as a restoration tool) → [[EE07 Conservation Biology]] (invaders and endangered natives).
> **Concepts:** [[Competition]] · [[Competitive Exclusion Principle]] · [[Tilman R-Star Rule]] · [[Lotka-Volterra Competition Model]] · [[Phase Plane and Isoclines]] · [[Invasive Species]] · [[Population Biology of Invasions]] · [[Ecological Niche]] · [[Niche Partitioning]] · [[Character Displacement]]
> **Other subjects:** [[Fixed Points and Linear Stability]] (2-D stability) · [[Jensen Inequality]] (fluctuating environments can favour coexistence) · [[Evolution of Earth and Life - Course Map]] (character displacement and speciation) · [[Bistability and Tipping Points]] (the priority effect of panel D is bistability)

> [!connection] Bistability in disguise
> Panel D of Fig. EE4.2 has two stable states (species 1 alone, species 2 alone) separated by a saddle: the same structure as the two climates of [[CL04 Feedback and Multiple Steady States]] and the two lake states of EE06. Which state a system ends up in then depends on its **history** (the initial ratio), the signature of a priority effect.

## Summary
> [!summary] Cheat-sheet
> - **Competition**: any use or defence of a resource that reduces its availability to others. Intra- vs interspecific; interspecific is *non-trophic* and lowers growth or equilibrium of at least one species.
> - **Gause**: no two species with the same niche can coexist (*P. aurelia* beats *P. caudatum*). **Tilman**: two species cannot coexist on a single limiting resource.
> - **$R^*$**: the species that keeps positive growth at the lowest resource level excludes the rest; $R^*=mk/(\mu-m)$ for a Monod response. The *fastest grower at high food* can lose.
> - **L-V**: $\dot N_1=r_1N_1(K_1-N_1-\alpha_{12}N_2)/K_1$ and the same with 1↔2. Isoclines $N_1=K_1-\alpha_{12}N_2$, $N_2=K_2-\alpha_{21}N_1$. **Four outcomes**: 1 wins, 2 wins, stable coexistence ($\alpha_{12}<K_1/K_2$, $\alpha_{21}<K_2/K_1$; $\alpha_{12}\alpha_{21}<1$), unstable (priority). **3 of 4 exclusion.**
> - **Invasives** as super-competitors: Kerala (arapaima to 200 kg, alligator gar to 137 kg; 28 alien fish + 4 weeds; 7 established; aquarium trade and aquaculture); control: water-hyacinth crafts (Kottapuram, Assam, Shantipur).
> - **Niche**: $n$-dimensional hypervolume; persistence niche (Hutchinson) vs resource-utilisation niche (MacArthur, Levins). **Partitioning** (spatial: *Paramecium*, Connell's barnacles; temporal: spiny mice; morphological: character displacement; conditional: Park's *Tribolium*).
> - **Higher equilibrium size does not guarantee winning** (Park: cool-moist and warm-moist).

## Practice
1. **Definitions.** What two features distinguish interspecific competition? Why is a predator eating its prey not competition? Give one example of intraspecific competition other than density-dependent growth.
2. **$R^*$.** Species X: $\mu=1.0$, $k=3$; species Y: $\mu=0.5$, $k=0.5$; both have loss rate $m=0.2$. (a) Find $R^*_X$ and $R^*_Y$. (b) Which wins on a single resource? (c) Which grows faster at $R=20$? (d) Explain in two sentences why (b) and (c) differ.
3. **Isoclines.** $K_1=120$, $K_2=90$, $\alpha_{12}=0.6$, $\alpha_{21}=0.5$. (a) Intercepts of both isoclines. (b) Is coexistence stable? (c) Equilibrium numbers.
4. **Outcome.** For $K_1=K_2=100$ and $\alpha_{12}=2$, $\alpha_{21}=0.4$, name the outcome from the intercepts and say who is excluded.
5. **Priority effect.** For $K_1=K_2=100$ and $\alpha_{12}=\alpha_{21}=1.5$: (a) the interior equilibrium; (b) is it stable? (c) which species wins if it starts with $N_1=60$, $N_2=10$ (reason from the isoclines)?
6. **Meaning of $\alpha$.** Interpret $\alpha_{12}=0$, $\alpha_{12}=1$ and $\alpha_{12}=3$ in words.
7. **Park.** Using the Tribolium table, in which conditions does the species with the larger single-species equilibrium lose? What does this say about predicting competition from $K$ alone?
8. **Invasion.** An aquarium fish is released in many ponds. Name three features of the *invader* and two of the *community* that Sakai et al. say affect success, and say why most introductions fail.
9. **Exam-style.** "In three out of four regions the Lotka-Volterra competition model predicts exclusion, yet many similar species coexist. Resolve this." Outline an answer with two mechanisms and one experiment each.
10. **Discussion.** A conservation agency proposes to feed an endangered native fish more food to help it against an invader sharing its single limiting food. Use the $R^*$ rule to say whether this should work.

> [!example]- Solutions
> 1. (i) It is **non-trophic** (neither eats the other); (ii) it **reduces the growth rate or equilibrium number** of at least one population, because they share a limiting resource. Predation is a *trophic* interaction (one species consumes the other, EE05). Intraspecific example: competition for mates (males of one species for females).
> 2. (a) $R^*_X=0.2\times3/(1.0-0.2)=0.75$; $R^*_Y=0.2\times0.5/(0.5-0.2)=0.333$. (b) **Y wins** (lower $R^*$). (c) At $R=20$: $f_X=1.0\times20/23=0.870$; $f_Y=0.5\times20/20.5=0.488$, so X grows faster. (d) X is quick when food is abundant but needs more food just to break even; Y can maintain itself on less, so as the shared resource is drawn down, only Y still grows, and it excludes X.
> 3. (a) Species 1: $N_1$-intercept $K_1=120$, $N_2$-intercept $K_1/\alpha_{12}=200$. Species 2: $N_2$-intercept $K_2=90$, $N_1$-intercept $K_2/\alpha_{21}=180$. (b) $\alpha_{12}<K_1/K_2=1.33$ ✓ and $\alpha_{21}<K_2/K_1=0.75$ ✓ ($\alpha_{12}\alpha_{21}=0.30<1$): **stable coexistence**. (c) $N_1^*=(120-0.6\times90)/(1-0.30)=66/0.7=94.3$; $N_2^*=(90-0.5\times120)/0.7=30/0.7=42.9$.
> 4. Species 1's isocline: $N_1$-intercept 100, $N_2$-intercept $K_1/\alpha_{12}=50$. Species 2's: $N_2$-intercept 100, $N_1$-intercept $K_2/\alpha_{21}=250$. Species 2's line is outside species 1's on both axes ($100>50$ and $250>100$): **species 2 wins**, species 1 is excluded.
> 5. (a) $N^*=100/(1+1.5)=40$ each. (b) $\alpha_{12}\alpha_{21}=2.25>1$: unstable (saddle). (c) The starting ratio $N_1/N_2=6$ is far above 1, so species 1 starts well to the right of the separatrix (the line $N_1=N_2$ through the saddle): **species 1 wins**, species 2 is excluded.
> 6. $\alpha_{12}=0$: species 2 has no effect on species 1 (no competition from 2). $\alpha_{12}=1$: one individual of species 2 counts exactly as one of species 1 (they are ecological equivalents for species 1). $\alpha_{12}=3$: one individual of species 2 suppresses species 1 as much as three of its own.
> 7. *Cool-moist* (castaneum larger alone, 45.2 against 28.2, but *confusum* wins 71 %) and *warm-moist* (*confusum* larger, 41.2 against 38.3, but *castaneum* wins 100 %). The outcome is decided by the competition coefficients (and the physical conditions that change them), not by the single-species equilibria.
> 8. *Invader* (Sakai et al.): high reproductive output or ability to self-fertilise; rapid growth, plasticity and tolerance of environmental stress; association with humans or repeated introductions (propagule pressure); genetic variation (or the evolutionary potential to adapt). *Community*: few natural enemies or competitors for the invader; disturbance and fragmentation; the presence of mutualists. Most introductions fail because small founding populations suffer demographic accidents, bottlenecks and inbreeding, and do not match the new environment.
> 9. (i) **Niche partitioning:** species with similar needs use different parts of the resource axis in space, time or body size. This reduces $\alpha$ until $\alpha_{12}\alpha_{21}<1$. Experiment: Gause's *P. caudatum* and *P. bursaria* (top vs bottom layers) coexist; or the spiny-mouse removal experiment. (ii) **Conditional outcomes:** the winner depends on temperature and humidity. Experiment: Park's *Tribolium* (cool-dry: *confusum* 100 %; warm-moist: *castaneum* 100 %). (Others: character displacement; Connell's barnacles.)
> 10. Under the $R^*$ rule the winner is the species with the lower break-even level on that resource. Extra food raises the supply but *does not change either $R^*$*: the invader still pushes the resource down to its own (lower) $R^*$ at equilibrium, below the native's break-even, so the native is still excluded. Feeding changes the *number* of invaders at equilibrium ($N^*=y(R_{in}-R^*)$), not the outcome. The remedy has to change a species' traits or add a second limiting resource or a niche difference, or remove the invader.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | competition: definition, types | [[04-Competition_25-Aug_2026.pdf#page=3\|sl. 3–6]] | taught |
> | Gause; Tilman et al. 1981 | [[04-Competition_25-Aug_2026.pdf#page=7\|sl. 7–8]] | taught |
> | $R^*$ rule | [[04-Competition_25-Aug_2026.pdf#page=9\|sl. 9]] | taught |
> | L-V competition, isoclines, main message | [[04-Competition_25-Aug_2026.pdf#page=10\|sl. 10–12]]; Molles §13.3 | taught |
> | invasive species, Kerala, hyacinth, self-study cases | [[04-Competition_25-Aug_2026.pdf#page=13\|sl. 13–17]] | taught |
> | niche; partitioning; conditional | [[04-Competition_25-Aug_2026.pdf#page=18\|sl. 18–30]]; Molles §13.2–13.3 | taught |
> | the invasion paper | Sakai et al. 2001 (paper) | extra/book |
> | derivation of $R^*$; chemostat example; Jacobian; $\alpha$ from overlap | computed here (`scripts/ee04_numbers.py`, `fig_ee04_*.py`) | extra/beyond |
>
> **Read and not read.** Molles Ch. 13 was read for §13.2–13.3 (text layer fine); §13.1 and §13.4 were only skimmed. Sakai et al. was read for the structure, the life-history, genetics and conclusion sections (about a third of the paper) and the main claims quoted. The Tilman et al. (1981) paper is not in the folder; §2 uses the slide's figure only.
>
> **Slide notes.** Slide 8's figure legend is flagged on the slide as inverted. Slide 11 shows three of the four L-V panels; the fourth ("species 2 wins") is the mirror image of the first. In slide 27 the label for the lowest zone is "*Balanus* is subject to predation in the lower tidal zone" (as written on the slide).

**References.** Gause, G. F. (1934) *The Struggle for Existence* · Tilman, D. (1982) *Resource Competition and Community Structure* · Tilman et al. (1981), as cited on slide 8 (the full reference is not on the slide and the paper is not in the folder) · Lotka, A. J. (1925) · Volterra, V. (1926) · Hutchinson, G. E. (1957) *Cold Spring Harb. Symp.* 22, 415 · MacArthur, R. & Levins, R. (1967) · Schoener, T. W. (2009) "Ecological niche" in *The Princeton Guide to Ecology* · Hairston, N. G. Jr. (1995) · Connell, J. H. (1961) *Ecology* 42, 710 · Park, T. (1954) *Physiol. Zool.* 27, 177; (1962) *Science* 138, 1369 · Shkolnik, A. (1971); Kronfeld-Schor, N. & Dayan, T. (1999) · Raj, S. et al. (2021) *Aquat. Ecosyst. Health Manag.* 24(2), 64–75 · Sakai, A. K. et al. (2001) *Annu. Rev. Ecol. Syst.* 32, 305–332 · Molles, M. C. (2022) *Ecology: Concepts and Applications*, 9th ed., Ch. 13 · Mertz, D. B. (1972) *Q. Rev. Biol.*
