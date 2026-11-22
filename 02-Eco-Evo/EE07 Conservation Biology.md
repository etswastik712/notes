---
title: EE07 Conservation Biology
aliases: [EE07, Conservation biology, Project Tiger, passenger pigeon, small populations, BI2113 lecture 7]
subject: eco-evo
type: chapter
chapter: 7
part: III
scope: [taught, extra-book, extra-beyond]
by: [slides]
status: draft
prereq: ["[[EE06 Eutrophication and Alternative Stable States]]"]
tags: [subject/eco-evo, type/chapter, taught, extra/book, extra/beyond, src/slides, src/book, src/paper, src/own-notes, status/draft]
---
# EE07 · Conservation Biology

◀ [[EE06 Eutrophication and Alternative Stable States]] · [[Ecology and Evolution - Course Map|Course Map]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**: the lecture ([[07_Conservation Biology.pdf|31 slides]]) **and** the *mandatory* reading, Hunter and Gibbs (2007), *Fundamentals of Conservation Biology*, Ch. 11, "Protecting ecosystems / management of reserve areas" ([[Ch 11_Ecosystem Management_Fundamentals of Conservation Biology.pdf|reading]])
> - §1 why conserve: extinction rates; three ethics; what conservation biology is (sl. 2–8)
> - §2 vulnerability: Rabinowitz's seven forms of rarity (sl. 9–10)
> - §3 the passenger pigeon: the "complicated story" (sl. 11–14)
> - §4 why small populations are at risk: three stochasticities; minimum viable population (sl. 15)
> - §5 four things that must converge (sl. 16)
> - §6 Project Tiger: the case study, the reversals, the global view, human-animal conflict (sl. 17–30)
> - §8 reserves: selection, design, management (Hunter and Gibbs Ch. 11; mandatory)
> - §9 references (sl. 31)
>
> 🟡 **Extra · book** (the *paper* tier: no exam weight, but the instructor calls them "brilliant" and "somewhat technical, try to get a gist")
> - §3 Bucher (1992), the causes of extinction of the passenger pigeon
> - §7 Karanth and Nichols (2010), non-invasive survey methods for assessing tiger populations
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §4 extinction probability and persistence time of a stochastic population (two figures made earlier, checked), the Allee effect and a harvest "fold", genetic-drift arithmetic
> - §7 a capture-recapture worked example with its confidence interval, camera-trap detection arithmetic
> - §6 growth rates implied by the tiger counts

> [!key] After this chapter you can
> - give the three **conservation ethics** and their conclusions, and say what conservation biology draws on,
> - place a species on **Rabinowitz's grid** and say why different rarities need different action,
> - recount the **passenger pigeon** story and say why "hunting" is only part of the answer,
> - name the three **stochasticities** and define **minimum viable population**; explain the **Allee effect**,
> - describe **Project Tiger** (aims, site criteria, activities, successes, reversals, the 2006 reform, the numbers),
> - explain why counts need a **detection probability** ($N=C/p$) and how camera-trap capture-recapture works,
> - summarise how **reserves** are selected, designed (size, shape, connectivity, SLOSS) and managed.

## 1. Why conserve?
<span class="scope-taught">taught</span> *[[07_Conservation Biology.pdf#page=1|slides 1–8]]*

Slide 2: "**What is the impact of human beings on nature?** Contemporary rates of extinction are vastly greater (**100–1000 times**) than they are typical of the geological past, and they are projected to get worse. So why should we bother about it?" ([[Extinction Rates]]) The slides answer with three historical **ethics** ([[Conservation Ethics]]):

| ethic | proponent | idea | conclusion |
|---|---|---|---|
| **Romantic-transcendental preservation** | **John Muir** (1838–1914), American naturalist | "communion with nature" brings people closer to God, so it is morally superior to preserve wilderness than to destroy it; he petitioned for the National Parks bill of 1899 (Yosemite, Sequoia) | **Preserve** |
| **Resource conservation** | **Gifford Pinchot** (1865–1946), first chief of the US Forest Service; protégé of **Dietrich Brandis**, first Inspector General of Forests in India | conservation is "the art of producing from the forest whatever it can yield for the service of man"; wise, judicious use so that future generations are not shortchanged (**sustainability**): the greatest good for the greatest number for the longest time (*Bahujan Hitay, Bahujan Sukhai*) | **Economic management** |
| **Evolutionary-ecological land ethic** | **Aldo Leopold** (1887–1948) | "A thing is right when it tends to preserve the integrity, stability and beauty of the biotic community. It is wrong when it tends otherwise"; humans change from "conqueror of the land-community to plain member and citizen of it" | **Conserve** (use and manage, with responsibility, recognising the intrinsic value of other species and whole ecosystems) |

> [!intuition] Three different reasons to leave the forest standing
> A cathedral (Muir): its value is not about us. A farm (Pinchot): its value is what it yields, so don't use it up. A neighbourhood (Leopold): we belong to it, and a neighbour's health is our concern. The different premises give different policies (strict no-go parks, sustained-yield forestry, managing for the health of the whole community).

Slide 7 then defines the field: "**Conservation biologists study the properties of small and/or declining populations and their environment, and try to suggest measures to protect them in nature.** It is a vast subject that includes input from several disciplines like population ecology, economics, public policy, anthropology etc."

![[07_Conservation Biology.pdf#page=8&height=330]]
*Slide 8, "the components of conservation biology": basic biological sciences (biology, zoology, botany, ecology) and applied management sciences (wildlife, forestry, range, fisheries), fed by the physical environment (geography, chemistry, geology, physics), the social environment (political science, anthropology, sociology, economics, philosophy) and the implementational environment (law, planning, education, engineering, public health, communication, veterinary sciences).*

> [!extra-beyond]- 🔵 Extra (beyond): what "100–1000 times" means
> Palaeontological **background** extinction is often expressed as extinctions per million species-years (E/MSY). For illustration only, assume a background rate of about 1 E/MSY: a group of $10^{6}$ species then loses about **one species a year**, and 100–1000 times that is **100 to 1000 species a year**. The number moves with the assumed baseline and the group, but the factor of 100–1000 over the geological norm is what the slide asserts. The mass extinctions of [[Evolution of Earth and Life - Course Map]] are the comparison class.

## 2. Who is vulnerable? Rabinowitz's seven forms of rarity
<span class="scope-taught">taught</span> *[[07_Conservation Biology.pdf#page=9|slides 9–10]]*

Slide 9 asks what determines the vulnerability of a species to extinction and gives **Rabinowitz's classification**: cross three binary properties ([[Rabinowitz Rarity Classification]]):

- **range of distribution**: extensive or restricted;
- **habitat tolerance**: broad or narrow;
- **local population size**: large or small.

That makes $2^{3}=8$ combinations: one (extensive, broad, large) is **common**; the other seven are **forms of rarity**. Slide 10 lists them, from most common to rarest, with an animal and a plant example for each:

| range | habitat tolerance | local population | animal / plant (slide) |
|---|---|---|---|
| extensive | broad | large | house sparrow / dandelion (common) |
| restricted | broad | large | Galápagos medium ground finch / Monterey pine |
| extensive | **narrow** | large | California grey whale / Fremont cottonwood; **passenger pigeon** (slide arrow) |
| extensive | broad | **small** | **tiger** (slide arrow) / grass fern |
| restricted | narrow | large | fish crow / Haleakala silversword |
| restricted | broad | small | Tasmanian devil / *Welwitschia* |
| extensive | narrow | small | northern spotted owl / Pacific yew |
| restricted | narrow | small | mountain gorilla / *Pritchardia monroe* (rarest) |

> [!intuition] Three different roads to being rare
> A species may be *everywhere but sparse* (the tiger: extensive range, broad tolerance, but few at any place), *abundant but demanding* (the passenger pigeon: huge flocks, but needing a specific kind of mast forest), or *confined and few* (the mountain gorilla). Each calls for a different remedy (protect prey and corridors; protect the key habitat across the range; protect and monitor the last populations). The more of the three properties are on the "rare" side, the more vulnerable the species.

> [!pitfall] "Rare" and "endangered" are not the same
> The grid describes a *state*; vulnerability also depends on the threats (hunting, habitat loss). The passenger pigeon sat in a "large local population" cell, which looked safe, yet it vanished; the lecture's next section is about why.

## 3. Case study 1: the passenger pigeon, "the complicated story"
<span class="scope-taught">taught</span> *[[07_Conservation Biology.pdf#page=11|slides 11–14]]* · <span class="scope-extra-book">extra · book</span> *Bucher 1992 (paper); Murray et al. 2017*

Slide 11 is the **emotional story** (a film). Slide 12 is the **complicated** one ([[Passenger Pigeon Extinction]]):

> [!key] The puzzle (slide 12)
> "The last passenger pigeon died in **1914**. However, **1878** was the last year that the catch was sufficient for commercial viability. So there was a substantial time when there was reduced hunting pressure, and yet the population could not rebound. Other pigeon species do so routinely; these guys could not. Why?" The six candidate causes, as assessed on the slide:
> 1. **Climatic change and catastrophic events**: no records.
> 2. **Hunting by humans**: definitely part of the story, not the whole of it.
> 3. **Diseases and parasites**: no records.
> 4. **Competition with domesticated species**: does not look like the case.
> 5. **Habitat alteration coupled with social facilitation in food finding**: cutting of forests reduced food, which may have been made worse by the birds' behavioural dependence on others for finding food. "We do not know."
> 6. **Genetic issues**: next slide.

Slide 13 cites **Murray et al. (2017)**, *Science* 358: 951–954, "Natural selection shaped the rise and fall of passenger pigeon genomic diversity" (genomes of the extinct species); slide 14 asks "*how exactly did this reduced genetic diversity play a role in extinction in this particular case?*" and answers "**We have no idea.**"

> [!extra-book]+ 🟡 Extra (book): Bucher (1992), the paper in brief
> Bucher ([[Bucher_1992_The causes of extinction of the Passenger Pigeon.pdf#page=1|*Current Ornithology*, ch. 1, pp. 1–36]]) argues that the critical question is "not so much the initial population decline as the inability of the species to survive at low numbers", since feeding and nesting habitat was apparently still abundant and hunting pressure would have fallen for scarce birds. Predation alone is not a sufficient explanation. His analysis:
> - The pigeon was a **nomadic specialist** (in the sense of Andersson and Erlinge 1977): it fed on **mast** (beechnuts and acorns), produced irregularly between years and regions, in patches that were large but unpredictable, so the birds had to find them over a huge area. **Social facilitation** (following flock-mates to food, an "information centre") was essential for finding patches.
> - The **perturbations**: deforestation, introduction of domestic pigs (which eat mast) and intensive hunting reduced the size and density of mast patches; the initial decline made food finding less efficient; the chances of missing a good breeding place rose; **the decline accelerated** (a **positive feedback**).
> - The result: **minimum viable population** size was reached "when the bird was still relatively common". Below it, every group would have missed good feeding grounds for longer than it could survive. Habitat alteration "was probably enough to lead the Passenger Pigeon to extinction even without direct persecution from humans". The 1871–1880 decline was "precipitous".

> [!connection] Why a flock species can be most fragile when it is still common
> A colonial bird's per-capita success *rises* with numbers (finding food, swamping predators; compare [[Predator Satiation]]). Removing individuals therefore does more harm than the arithmetic of the kill suggests: below a threshold density, the per-capita growth rate is negative and the population cannot rebound. This is the **Allee effect** (§4.3).

## 4. Why small populations are vulnerable
<span class="scope-taught">taught</span> *[[07_Conservation Biology.pdf#page=15|slide 15]]*

> [!key] Three stochasticities and the minimum viable population
> "Small populations face risk of extinction from three kinds of stochasticities: **demographic stochasticity** (random variation in birth and death rates, sex ratio etc.); **genetic stochasticity** (genetic drift leading to inbreeding depression and loss of heterozygosity); **environmental stochasticity and natural catastrophes**." The **minimum viable population (MVP)** is "the minimum population size that will ensure, at some acceptable level of risk, that the population will persist for a specified time" ([[Demographic Genetic and Environmental Stochasticity]], [[Minimum Viable Population]]). The conventional wording (Shaffer 1981): a 99 % chance of persistence for 1,000 years.

### 4.1 Demographic stochasticity: even growing populations can die out
> [!example] Worked example 1: a population with more births than deaths
> Individuals reproduce at rate $b$ and die at rate $d$ per capita, independently. If $b>d$ the *average* population grows, but a population of $N_0$ individuals still goes extinct with probability
> $$P_{\text{ext}}=\Big(\frac db\Big)^{N_0}.$$
> For $b=1.1,\ d=1.0$ (a 10 % surplus): $N_0=1$: 0.91; $N_0=10$: 0.39; $N_0=50$: 0.0085. For $b=1.5,\ d=1.0$: $N_0=1$: 0.67; $N_0=10$: 0.017. Simulation (40,000 runs per point) agrees with these to about 0.3 percentage points (`scripts/fig_ee07_extinction_time.py`). Intuition: each individual's line of descendants dies out with probability $d/b$, and the whole population fails only if *all* $N_0$ lines do; a single founder with a 10 % growth surplus still fails nine times out of ten.

> [!intuition] Chance matters in proportion to the number of dice
> Relative demographic noise scales as $1/\sqrt N$: 32 % for 10 animals, 10 % for 100, 3 % for 1000. A million-strong population averages the noise away; a hundred cannot. Environmental stochasticity (a bad winter, a drought) acts on every individual together, so it does not average out with $N$: that is why a large population is only *much* safer, not safe.

![[fig_ee07_extinction_time.png|860]]
*Figure EE7.1. Stochastic extinction of a small population (checked simulations). Left: eventual extinction probability against initial size, line $(d/b)^{N_0}$, circles simulation. Right: mean time to extinction against carrying capacity $K$ (birth rate capped at $K$): it grows **exponentially**, approaching $e^{K\ln(b/d)}$ for large $K$ (for $b/d=1.2$ that is a factor 1.2 per extra individual, 6.2 per extra ten; at the sizes shown the factor per ten is about 4 to 5).*

> [!example] Worked example 2: how big must $K$ be?
> With $b/d=1.2$ and the birth rate capped at $K$, the mean time to extinction is about 17 time units for $K=10$, 72 for $K=20$, 294 for $K=30$, 1,299 for $K=40$ and 6,193 for $K=50$ (exact formula; simulation agrees within about 2 %). Each +10 individuals multiplies the persistence time by 4.1 to 5.0, creeping up towards the large-$K$ limit $1.2^{10}=6.2$. This is the basis of **MVP**: "persist for 1,000 years with 99 % probability" is a statement about the *tail* of these exponentials, and it needs a population several times larger than the "average" survival suggests.

### 4.2 Genetic stochasticity
> [!example] Worked example 3: drift removes variation
> In a population of effective size $N_e$ the expected heterozygosity decays as $H_t=H_0\big(1-\tfrac1{2N_e}\big)^t$ per generation ([[Genetic Drift and Inbreeding Depression]]). After 100 generations $H/H_0$ is 0.006 for $N_e=10$, 0.37 for $N_e=50$ and 0.905 for $N_e=500$; the time to lose half is about $1.39N_e$ generations (13.5, 69 and 693). Reduced diversity brings **inbreeding depression** (lower fitness from mating among relatives expressing deleterious recessives) and limits the ability to adapt (compare the founder effects of invasive species in [[EE04 Competition and Invasions]]).

![[fig_ee07_tigers_drift.png|860]]
*Figure EE7.2. Right: heterozygosity left against generations for three effective sizes (my computation). Left: the tiger estimates quoted in §6.*

### 4.3 Positive density dependence: the Allee effect
Slide 12's "social facilitation in food finding" is an example of a general phenomenon: at low density the per-capita growth rate can *fall* with falling density ([[Allee Effect]]). A standard strong-Allee model with threshold $A$ and carrying capacity $K$ is

$$\frac{dN}{dt}=rN\Big(\frac NA-1\Big)\Big(1-\frac NK\Big).$$

Below $A$ the per-capita rate is negative and the population goes extinct; between $A$ and $K$ it grows to $K$. There are three fixed points: $0$ (stable), $A$ (unstable: the **threshold**) and $K$ (stable), a bistable system like those of [[Bistability and Tipping Points]].

![[fig_ee07_allee.png|860]]
*Figure EE7.3. Left: per-capita growth with and without an Allee effect; the strong Allee effect has an extinction threshold $A$. Right: a constant harvest $H$ on a strong-Allee population ($r=0.5$, $A=20$, $K=100$; illustrative): the two equilibria approach each other and annihilate at $H=\max f=26.3$ (a fold).*

> [!example] Worked example 4: a "safe" quota that tips a population over
> With $r=0.5$, $A=20$, $K=100$ the growth rate peaks at $f_{\max}=26.3$ at $N=70.6$ (the logistic with the same $r,K$ peaks at $rK/4=12.5$). A constant harvest $H=20$ a year looks sustainable ($H<f_{\max}$) and the population settles at $N=85.9$. But there is a second, *unstable* equilibrium at $N=52.1$: a bad year that knocks the population below 52, with the quota unchanged, sends it to extinction, although 52 is far above $A=20$. At $H\ge26.3$ the two equilibria merge and vanish: the **fold**. The harvest threshold at which collapse happens is far above the "extinction threshold" without harvesting. This is the same mathematics as the shallow-lake fold of [[EE06 Eutrophication and Alternative Stable States]].

> [!intuition] How the three threats compound: the extinction vortex
> §4.1–4.3 are not three separate risks to be added up. Each one makes the others worse:
> - a smaller population loses heterozygosity faster (§4.2);
> - inbreeding lowers survival and fecundity, which shrinks the population further and lowers $b/d$;
> - a lower $b/d$ at a smaller $N$ raises the extinction probability steeply (§4.1);
> - in a social species, fewer individuals also mean a lower per-capita rate through the Allee effect (§4.3).
>
> Each turn of the loop is a step down. This is why the pigeon puzzle of §3 needs no new cause after 1878. Once a population is pushed below the size at which these feedbacks dominate, removing the original pressure (hunting) does not bring it back. The MVP is, in effect, the size above which this loop stays weak.

## 5. Four things must converge
<span class="scope-taught">taught</span> *[[07_Conservation Biology.pdf#page=16|slide 16]]*

"Four things need to converge for any conservation effort": **science**; **common sense** (self-study: Ch. 11 of Hunter and Gibbs, §8 below); **economics** ("a fascinating subject, unfortunately not a part of BIO 201"); and **politics** (the case study that follows).

## 6. Case study 2: Project Tiger
<span class="scope-taught">taught</span> *[[07_Conservation Biology.pdf#page=17|slides 17–30]]*

> [!key] The Project Tiger story (slides 18–26)
> - **Baseline.** Estimated tigers in India at the beginning of the 20th century: **40–45 thousand**; in **1972: 1,827**. Reasons: hunting, habitat destruction, loss of prey, poaching, and competition with local villagers and domestic animals (slide 18).
> - **Launch.** **1 April 1973** ([[Project Tiger]]). Aims: to ensure the maintenance of a viable population of tigers in India for scientific, economic, aesthetic, cultural and ecological values; and to preserve, for all times, areas of such biological importance as a national heritage for the benefit, education and enjoyment of the people (slide 19).
> - **Site criteria** (slide 21): little disturbance; high development potential, in that the numbers of both prey and predator were high; no drilling, mining or timber ventures; in different states, so that responsibility for management could be evenly distributed.
> - **The first nine reserves, about 13,017 km²**: Bandipur, Corbett, Kanha, Manas, Melghat, Palamau, Ranthambhore, Similipal, Sundarbans.
> - **Activities**: core and buffer areas; connecting habitats through corridors; halting cattle activity and forest harvesting; regular patrolling to discourage poachers.
> - **Result** (slide 22): numbers went up to **more than 4,000 in just 11 years**; "although this figure is questioned, there is no doubt that there was an increase in the number of tigers and many other species".
> - **Reversals**: lack of government will in the face of pressure from farmers; encroachment in buffer zones and access routes; reduction in prey from habitat loss and local hunters; accelerated poaching; lack of funds. "Although the number of reserves has risen, there are several problems facing Project Tiger" (slides 23–24 are videos).
> - **After** (slide 26): Project Tiger was replaced by the **National Tiger Conservation Authority (NTCA)** and the **Wildlife Crime Control Bureau** under the **Wild Life (Protection) Amendment Act, 2006**; better surveys using **camera traps**; in 2007 more than 40 reserves covering **37,761 km²**; **about 1,706 tigers in 2011 (1,411 in 2008)**; Madhya Pradesh lost 65 % of its tigers; Chhattisgarh, Maharashtra and Rajasthan had fewer than 100 each; **no tigers in Sariska** (Alwar); primary reason attributed: **poaching**. July 2012: the Supreme Court banned tourists in core areas of tiger reserves. The **2018** estimate: **2,967 tigers older than 1 year (2,603–3,346)** from **2,461 unique tiger photographs**.

![[fig_ee07_tigers_drift.png|860]]
*Figure EE7.2 (left panel). The counts on the slides. Compare the early-20th-century 40–45 thousand: the 2018 estimate is about 7 % of that.*

> [!example] Worked example 5: what the numbers say
> **1972 to the early 1980s:** 1,827 to "over 4,000" is a factor 2.2, an implied growth of $\ln(4000/1827)/11=0.071$ per year (7 % a year, a rate the slide itself calls questionable: counting by pugmarks was later abandoned, §7). **2008 to 2011:** $1411\to1706$ is $\times1.21$, 6.3 % per year; **2011 to 2018:** $1706\to2967$ is $\times1.74$, **7.9 % per year**, with a 95 % interval on 2018 of $-12\%/+13\%$. Part of such a rise is better surveying, so the early figures and the later figures should not be treated as one series. Reserve area grew $\times2.9$ (13,017 to 37,761 km²) between 1973 and 2007. A tiger population of a few thousand is still below 7 % of the century-old number.

**Global view and conflict (slides 27–30).** About **70 % of the world's wild tigers are in India** ("but where are the other tigers?", a video); the **Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES), 1973**, is a global treaty to protect endangered plants and animals. **Human-animal conflict** is the cost side of conservation: elephants (slide 29, with the Indian Railways measures against collisions) and a local solution (slide 30): **lemon trees in Assam** (a video) as a barrier that elephants avoid.

> [!pitfall] "Number of reserves" is not "number of tigers"
> The slide stresses that the number of reserves has risen and yet problems remain. Counting reserves (an *effort* measure) is not the same as measuring tigers (an *outcome*). The distinction is why §7 matters: an outcome needs a defensible estimator.

## 7. Counting tigers: the survey methods
<span class="scope-taught">taught</span> *[[07_Conservation Biology.pdf#page=26|slide 26]]* · <span class="scope-extra-book">extra · book</span> *Karanth and Nichols 2010 (paper)*

Slide 26 says that after the reform "**better surveys [were] undertaken using camera traps**". The instructor adds Karanth and Nichols's chapter as a paper ("somewhat technical, but try to get a gist").

> [!extra-book]+ 🟡 Extra (book): Karanth and Nichols (2010), "Non-invasive survey methods for assessing tiger populations"
> **Why it is hard.** Tigers are secretive, nocturnal, wide-ranging (daily movements of about 5–30 km; home ranges 15 to over 1,000 km²) and occur at low density (even in prime habitat about 12–18 tigers per 100 km²), in 76–159 scattered populations across a range of about 1.1 million km² in 13 countries. Visual counting methods (distance sampling) cannot be used; radio-telemetry is too costly for abundance.
> **The pugmark census.** A national "census" that claimed to identify individuals from paw prints: Karanth describes the same animal's tracks varying with substrate, moisture and pace; tests on captive tigers showed it did not work, and the **"Pugmark Census" was abandoned as a failure after about 25 years** (a Tiger Taskforce ordered its end).
> **General estimator.** $\hat N=C/\hat p$: the count $C$ divided by the **detection probability** $\hat p$. Indices (track or scat encounter rates) ignore $p$: in seven Indian reserves the scat index corresponded poorly to the camera-trap density estimate. **Capture-recapture** (mark-recapture) is the flexible framework for estimating $p$ from the frequencies with which individually identified animals are caught, for tigers (individuals), for tracks, or for habitat patches (occupancy).
> **Camera traps.** Tigers are individually identified by their **stripe patterns**; a **closed-population** survey of about **30–60 days** (to avoid births, deaths, movements) sweeps the area several times (each sweep a sampling occasion); traps must be spaced so that no tiger has zero chance of being photographed (female home ranges, 15–500 km², set the spacing). Data form a capture-history matrix; models are fitted in the software CAPTURE and MARK, and because individuals differ in capture probability the **heterogeneity model $M_h$** is often best. **Density** is $\hat N$ divided by an *effective sampled area*: the trap polygon plus a **buffer strip of half the mean maximum distance moved (MMDM)**, an ad hoc rule that the authors call "a weak link" (spatial capture-recapture is stronger). A sample result, Nagarahole: about 12 tigers per 100 km² against 11.6 predicted from prey. **Open models** over several years estimate survival and recruitment (annual survival about 0.77 in their Nagarahole series). **Occupancy** surveys (presence/absence of sign on patches, with the probability of detecting sign if present) assess distribution over big landscapes.
> **A rule of thumb for potential numbers:** tigers need about 50 ungulates a year and crop about 10 % of the prey, so about **one tiger per 500 prey animals**, which holds reasonably well where tigers are not poached (11 Indian reserves).

> [!example] Worked example 6: capture-recapture arithmetic
> **Lincoln-Petersen.** Mark $M=50$ animals and release them. Later catch $n=40$, of which $m=8$ carry marks. If the marked fraction in the sample equals the marked fraction in the population, $m/n=M/N$, so $\hat N=Mn/m=250$. The nearly unbiased **Chapman** form $\hat N=\frac{(M+1)(n+1)}{m+1}-1=231$ has standard error $\approx59$, an approximate 95 % interval of **116–347**: with only 8 recaptures the estimate is very uncertain. With $m=20$: $\hat N=99$ (SE 11, 76–121). With $m=3$: 522 (SE 213, 104–940). *The fewer the recaptures, the wider the interval.* The assumptions: a closed population, equal capture probability, marks neither lost nor overlooked. In the tiger setting the $M_h$ model handles unequal capture probabilities.
> **Detection probability.** If the per-occasion capture probability is $p=0.1$ and there are $K=10$ occasions, an animal is caught at least once with probability $p^*=1-0.9^{10}=0.651$. Counting $C=30$ distinct tigers then gives $\hat N=30/0.651=46$: a raw count of 30 would have missed a third of the animals.
> **From prey.** With prey density $D_p$ per km², "one tiger per 500 prey" predicts $D_p/5$ tigers per 100 km²: $D_p=50$ gives 10 per 100 km²; reaching the upper observed densities (12–18) needs about 60–90 prey per km².

## 8. Managing reserves (Hunter and Gibbs, Ch. 11)
<span class="scope-taught">taught</span> *mandatory reading* · [[Ch 11_Ecosystem Management_Fundamentals of Conservation Biology.pdf#page=1|Hunter and Gibbs, Ch. 11]]

The chapter treats reserves as the **coarse-filter** strategy for conserving biodiversity: protect a set of ecosystems representative of the region's diversity ([[Reserve Design and Management]]). "Reserve" is the generic term for areas in which natural ecosystems are protected from most human use; the IUCN categories range from **Ia** (strict nature reserve, mainly for science) and **Ib** (wilderness area), through **II** (national park) and **III** (natural monument), **IV** (habitat/species management area) and **V**, to **VI** (managed resource protected area). The chapter has three parts.

**1. Selecting reserves.** Priorities include centres of species diversity (hotspots), filling the gaps (placing reserves where existing ones miss ecosystems or species), and logistical questions (how many, cost, land availability).

**2. Designing reserves.** Many ideas trace to Jared Diamond (1975), who likened reserves to islands (island biogeography, species-area relationships) and proposed six principles: (1) a large reserve holds more species than a small one; (2) **a single large reserve is preferable to several small ones of equal total area** (same ecosystem type); (3) multiple small reserves should be close together; (4) clustered rather than linear arrangement; (5) corridors help dispersal; (6) reserves as circular as possible, to enhance internal dispersal and minimise edge effects.

> [!key] Large versus small, and the SLOSS debate
> **Why large reserves**: they contain a wider range of environmental conditions and hence more species; they hold species needing large home ranges (large carnivores) or living at low densities; their populations are less likely to go extinct (§4); they have *relatively less edge* (area grows as the square of the linear size, edge only linearly, so doubling a reserve's width halves its edge per unit area) and so are less open to invasion and poaching; and a catastrophe cannot disturb all of one. A reserve should exceed the **minimum dynamic area**: the smallest area holding a mosaic of patches of different disturbance and succession stages (if fires burn 1,000 ha, a reserve should be many thousands of hectares).
> **SLOSS (Single Large or Several Small)**: Simberloff and Abele (1976) doubted that a single large reserve is *always* better. Box 11.1 shows two extreme scenarios. **Nested** species lists (each larger reserve contains all species of smaller ones): with \$1.2 million at \$5,000 per ha, buying one 240-ha reserve protects **224 species**; three smaller ones of the same total cost protect only 199. **Un-nested** lists (each reserve has its own set): five small reserves costing \$750,000 harbour **709 species**, while the 240-ha reserve costing \$1.2 million holds 224. Real data are significantly nested for many taxa, but nestedness is confounded with environment: the answer depends on how species are distributed.

**3. Landscape context and connectivity.** Reserve boundaries are *permeable*: pollution, invasive species, livestock and poachers come in; clean water and breeding stock go out. Reserves are best buffered by a matrix of seminatural land and are easier to buffer if roughly circular (a circle has the least edge per area). Four kinds of movement have to be maintained: **daily** movements within a home range; **annual migrations** (for example in Tanzania, land is being protected between Lake Manyara and Tarangire so that zebras and wildebeest can reach Lake Manyara in the dry season; compare [[Serengeti Wildebeest Migration]]); **dispersal** of young animals and seeds; and **long-term range shifts** under climate change. Corridors are the tool, with trade-offs. **Zoning** (core, buffer, partial-use zones) keeps the core protected while giving local people legal uses (the chapter's Asinara marine-reserve example).

**4. Managing reserves.** "Reserve management is, first and foremost, **people management**": visitors (roads, sewage, trampling), exploitation (even where hunting is banned, fishing and deadwood collection are often allowed), and local goodwill (Chitwan, Nepal: local people may enter once a year for ten days to cut grass; ecotourism income often does not reach those who bear the costs). It also covers **natural disturbances** (fires and floods are often necessary for ecosystem function: do not suppress them), **water regimes**, and **invasive exotics and overabundant natives**.

> [!connection] Project Tiger as a reserve-design case
> The Project Tiger practices (core and buffer areas, corridors, halting cattle and forest harvesting, patrolling) are exactly the design principles of Hunter and Gibbs; the **reversals** (encroachment on buffers, prey loss to local hunters, pressure from farmers, lack of funds) are exactly their management problems: permeable boundaries and people management.

## 9. Reading tiers
<span class="scope-taught">taught</span> *[[07_Conservation Biology.pdf#page=31|slide 31]]*

| item | tier |
|---|---|
| lecture slides | syllabus |
| Hunter and Gibbs (2007), Ch. 11, "Management of reserve areas" | **mandatory**, syllabus |
| Karanth and Nichols (2010), non-invasive survey methods (a *Tigers of the World* chapter) | paper ("somewhat technical, but try to get a gist") |
| Bucher (1992), the causes of extinction of the passenger pigeon | paper ("brilliant article examining the potential causes") |

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Demographic stochasticity: small populations go extinct
> A stochastic logistic birth–death process: each individual gives birth at rate b and dies at rate d + (b−d)N/K, so the deterministic limit is logistic growth to K but every individual event is random.
>
> ![[ee_stochastic_extinction.png|720]]
>
> **Try:** With b = 0.5, d = 0.4 (net growth 0.1) and N₀ = K/2, 300 simulated replicates per K (measured while building): K = 8 → all go extinct (mean time ≈ 27); K = 20 → 93 % extinct by t = 300; K = 30 → 59 %; K = 45 → 22 %. Persistence grows steeply with K. Switch the Allee effect on and start below K/5: extinction becomes nearly certain.
>
> [▶ Open the tool in your browser](../Assets/interactive/ee_stochastic_extinction.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/ee_stochastic_extinction.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How EE07 connects
> **Builds on:** every earlier chapter: [[EE02 Structured Population Models]] (stage models identify the stage to protect, TEDs), [[EE03 Population Dynamics and Chaos]] (the logistic, density dependence, the lattice effect and extinction), [[EE04 Competition and Invasions]] (invaders and small founder populations), [[EE05 Predation]] (predators and prey, refuges), [[EE06 Eutrophication and Alternative Stable States]] (thresholds and hysteresis).
> **Concepts:** [[Extinction Rates]] · [[Conservation Ethics]] · [[Rabinowitz Rarity Classification]] · [[Passenger Pigeon Extinction]] · [[Allee Effect]] · [[Demographic Genetic and Environmental Stochasticity]] · [[Minimum Viable Population]] · [[Genetic Drift and Inbreeding Depression]] · [[Mark-Recapture Estimation]] · [[Tiger Population Surveys]] · [[Project Tiger]] · [[Reserve Design and Management]]
> **Other subjects:** [[Probability - Course Map]] (stochastic processes, sampling, estimators) · [[CL02 Observing Global Temperature]] (sampling and uncertainty in data series) · [[Evolution of Earth and Life - Course Map]] (mass extinctions) · [[Bistability and Tipping Points]]

![[EE07 From Why to What To Do.svg|760]]
*Figure EE7.4. The chapter as a chain. Editable: [[EE07 From Why to What To Do.excalidraw]].*

> [!connection] Thresholds everywhere
> The Allee threshold, the harvest fold, the shallow-lake fold and the ice-albedo fold are one mathematical picture ([[Bistability and Tipping Points]]): positive feedback at one end of the state, a threshold, and a point past which recovery needs far more than the original change. Conservation lessons recur: act before the threshold, because afterwards the cost is much higher.

## Summary
> [!summary] Cheat-sheet
> - **Why:** extinction is 100–1000× the geological rate. **Muir** (preserve), **Pinchot/Brandis** (resource conservation, *Bahujan Hitay*), **Leopold** (land ethic, conserve).
> - **Rarity** (Rabinowitz): range × habitat tolerance × local population: 8 cells, 7 forms of rarity. Pigeon: extensive, narrow, large; tiger: extensive, broad, small.
> - **Passenger pigeon:** last died 1914; commercial hunting ended ≈1878; six causes (climate, hunting, disease, competition, **habitat alteration + social facilitation**, genetics); Bucher: nomadic mast specialist, MVP reached while still common.
> - **Small populations:** demographic, genetic, environmental stochasticity; $P_{ext}=(d/b)^{N_0}$ even if $b>d$; persistence time grows like $e^{K\ln(b/d)}$; $H_t=H_0(1-1/2N_e)^t$; **Allee** threshold and harvest fold. **MVP** = size for acceptable risk over a stated time.
> - **Four things converge:** science, common sense, economics, politics.
> - **Project Tiger:** 1,827 (1972) → launch 1 April 1973, 9 reserves, 13,017 km² → >4,000 in 11 years (questioned) → reversals → 2006 NTCA → 1,411 (2008), 1,706 (2011), **2,967 (2018, 2,603–3,346; 2,461 photographs)**; 70 % of wild tigers in India; CITES 1973; human-elephant conflict.
> - **Counting:** $\hat N=C/\hat p$; pugmark census failed; **camera-trap capture-recapture** (30–60 d, stripes, $M_h$, buffer = ½ MMDM); Lincoln-Petersen $Mn/m$.
> - **Reserves:** Diamond's six principles; SLOSS; minimum dynamic area; buffers and corridors (four movement kinds); management is people management.

## Practice
1. **Ethics.** Match to Muir, Pinchot or Leopold: (a) "the art of producing from the forest whatever it can yield"; (b) "integrity, stability and beauty of the biotic community"; (c) communion with nature; (d) the greatest good for the greatest number for the longest time. What conclusion does each draw?
2. **Rarity.** Place on Rabinowitz's grid (range / tolerance / population) the passenger pigeon, the tiger and the mountain gorilla. Which is "rarest" and why?
3. **Pigeon.** Last commercial catch 1878, last bird 1914. Why does that gap argue *against* hunting as the whole story? Name the two ideas that (per the slides and Bucher) may explain why numbers could not recover.
4. **Extinction odds.** A growing population has $b=1.2$, $d=1.0$ per capita. Find the probability that a lineage started by $N_0=1,\ 5,\ 20$ individuals eventually goes extinct.
5. **Persistence.** The mean time to extinction is 72 time units at $K=20$ and rises about 4- to 5-fold for every 10 extra individuals of carrying capacity. Estimate it at $K=30$ and $K=50$, and say why the answer is not simply $1.2^{\Delta K}$ times 72.
6. **Drift.** For $N_e=25$, what fraction of the starting heterozygosity remains after 50 generations? About how many generations to lose half?
7. **Allee.** A population follows $\dot N=0.5N(N/20-1)(1-N/100)$. Without harvest, what happens from $N=15$ and from $N=30$? With a constant harvest of 20 a year, what is the *lower* (threshold) equilibrium and why does it matter?
8. **Counting.** 40 animals are marked. A later sample of 50 contains 10 marked animals. (a) The Lincoln-Petersen estimate. (b) The Chapman estimate and its standard error. (c) What happens to the interval if only 4 marked animals are recaptured?
9. **Survey design.** Why must a camera-trap survey be short (30–60 days)? Why can a simple count of pugmarks not give $N$?
10. **Reserves.** A budget buys either one 240-ha reserve or five 48-ha reserves of the same total cost. When is the single reserve better, and when are the five better?
11. **Exam-style.** "Discuss Project Tiger as a case study of conservation." Outline the aims, the design, the early success, the reversals, the reform of 2006 and what is learned about science and politics.

> [!example]- Solutions
> 1. (a) Pinchot: economic management (resource conservation); (b) Leopold: conserve (land ethic); (c) Muir: preserve; (d) Pinchot (*Bahujan Hitay, Bahujan Sukhai*).
> 2. Passenger pigeon: extensive range, narrow habitat tolerance, large local population. Tiger: extensive range, broad tolerance, small local population. Mountain gorilla: restricted range, narrow tolerance, small local population: all three properties on the "rare" side, so the **rarest** (slide 10).
> 3. After 1878 hunting could no longer pay, so pressure fell, yet the population kept falling for 36 years and never rebounded; other pigeons recover quickly. The suggested explanations: **habitat alteration** (loss of mast forests, in a species that had to find irregular mast patches) combined with **social facilitation** (food finding depends on flock size), so that a decline made the decline faster (positive density dependence, the Allee effect) and an MVP was reached while the bird was still common.
> 4. $P_{ext}=(d/b)^{N_0}=(1/1.2)^{N_0}=0.833^{N_0}$: $N_0=1$: 0.833; $N_0=5$: 0.402; $N_0=20$: 0.026.
> 5. $K=30$: $72\times4.1\approx300$ (exact 294); $K=50$: $294\times4.4\times4.8\approx6{,}200$ (exact 6,193). The asymptotic factor $1.2^{10}=6.2$ per ten individuals is reached only for large $K$: the exact sum $\sum_k(\rho^k-1)/k$ is still dominated by smaller $k$ terms at these sizes. The message is the *exponential growth* of persistence time with $K$.
> 6. $(1-1/50)^{50}=0.98^{50}=0.364$; the half-life is $\ln2/(-\ln0.98)=34.3$ generations ($\approx1.39N_e$).
> 7. Threshold $A=20$: from $N=15<20$ the population declines to 0; from $N=30$ it grows to $K=100$. With $H=20$ the equilibria solve $f(N)=20$: $N=52.1$ (unstable) and 85.9 (stable). A disturbance that takes the population below 52 *with the quota unchanged* causes extinction, though the no-harvest threshold is only 20.
> 8. (a) $\hat N=Mn/m=40\times50/10=200$. (b) Chapman: $(41)(51)/11-1=189.1$; variance $=\dfrac{(M+1)(n+1)(M-m)(n-m)}{(m+1)^2(m+2)}=\dfrac{41\times51\times30\times40}{121\times12}=1728$, SE $=41.6$ (approximate 95 % interval 108–271). (c) With $m=4$: $\hat N_{LP}=500$, Chapman $=41\times51/5-1=417$ with SE about 150: a much wider interval. Fewer recaptures, less information.
> 9. The model assumes a **closed** population (no births, deaths, immigration, emigration in the survey window): 30–60 days keeps that approximately true. A pugmark count cannot separate individuals reliably (prints vary with substrate, moisture and pace), cannot estimate how many tigers left no track, and ignores the detection probability: $N=C/p$ with $p$ unknown.
> 10. The single large reserve is better when species lists are **nested** (the big reserve holds all species of the small ones; here 224 species against 199 for three smaller ones), when species need large home ranges, and when edge effects are strong. Several small reserves are better when each holds a *different* set of species (un-nested; 709 species for \$750,000 in the chapter's second scenario), or when spreading reduces the risk of one catastrophe.
> 11. *Aims and design* (1973; viable tiger populations; core/buffer, corridors, halting cattle and forest harvesting, patrols; 9 reserves, 13,017 km²; criteria: undisturbed, high prey and predator numbers, no mining, spread across states). *Early success* (1,827 → >4,000 in 11 years, questioned). *Reversals* (political will, encroachment, prey loss, poaching, funds; Sariska lost its tigers). *Reform* (NTCA and Wildlife Crime Control Bureau, 2006; camera-trap surveys; more reserves, 37,761 km²). *Numbers* 1,411 (2008), 1,706 (2011), 2,967 (2018). *Lessons*: science (reserve design, counting with detection probability), politics (will, law, funding), local people (conflict, livelihoods), and the four-things-converge idea.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | extinction rates; three ethics; definition; components | [[07_Conservation Biology.pdf#page=2\|sl. 2–8]] | taught |
> | Rabinowitz's grid | [[07_Conservation Biology.pdf#page=9\|sl. 9–10]] | taught |
> | passenger pigeon: six causes; genetics | [[07_Conservation Biology.pdf#page=11\|sl. 11–14]] | taught |
> | stochasticities; MVP; four things | [[07_Conservation Biology.pdf#page=15\|sl. 15–16]] | taught |
> | Project Tiger; global view; conflict | [[07_Conservation Biology.pdf#page=17\|sl. 17–30]] | taught |
> | reserves: selection, design, management | Hunter and Gibbs Ch. 11 | taught (mandatory) |
> | Bucher's analysis | Bucher 1992 (paper; OCR) | extra/book |
> | survey methods; pugmark census; closed models; occupancy | Karanth and Nichols 2010 (paper; OCR) | extra/book |
> | extinction probability and persistence time; Allee and harvest fold; drift; capture-recapture example; implied tiger growth rates | computed here (`scripts/ee07_numbers.py`, `fig_ee07_*.py`, two figures made in an earlier session and checked) | extra/beyond |
>
> **Existing figures checked.** `fig_ee07_extinction_time` and `fig_ee07_allee` were made earlier; their scripts reproduce the printed values (extinction probabilities $(d/b)^{N_0}$ against simulation within about 0.3 percentage points; the exact mean persistence times against simulation within about 2 %; the Allee equilibria $52.05$ and $85.85$ at $H=20$, fold at $H=26.26$). I corrected two label positions (one outside the axes).
>
> **Read and not read.** Hunter and Gibbs Ch. 11 was read in the parts quoted (design, connectivity, management); selection and the IUCN-category table were skimmed. Bucher (a 47 MB scan) and Karanth and Nichols (garbled text layer) were OCR'd and read in the sections quoted; the Murray et al. genomics paper is only cited on the slide. Videos (slides 11, 23, 24, 27–30) are not examinable text and were not watched.
>
> **Slide notes.** Slide 10's arrows place the pigeon in the "extensive, narrow, large" cell and the tiger in "extensive, broad, small". The slide's 1,827 and ">4,000 in 11 years" are as stated there (the latter flagged as questioned); the later counts follow different survey methods.

**References.** Muir, J.; Pinchot, G.; Leopold, A. (1949) *A Sand County Almanac* · Rabinowitz, D. (1981) · Bucher, E. H. (1992) in Power (ed.) *Current Ornithology* 9, 1–36 · Murray, G. G. R. et al. (2017) *Science* 358, 951–954 · Shaffer, M. L. (1981) *BioScience* 31, 131 · Hunter, M. L. & Gibbs, J. P. (2007) *Fundamentals of Conservation Biology*, 3rd ed., Ch. 11 · Diamond, J. M. (1975) *Biol. Conserv.* 7, 129 · Simberloff, D. & Abele, L. G. (1976) *Science* 191, 285 · Pickett, S. T. A. & Thompson, J. N. (1978) *Biol. Conserv.* 13, 27 · Karanth, K. U. & Nichols, J. D. (2010) in Tilson & Nyhus (eds) *Tigers of the World*, ch. 18 · Chapman, D. G. (1951) · Lincoln, F. C. (1930) · Allee, W. C. (1931) · Wright, S. (1931) · Andersson, M. & Erlinge, S. (1977) *Oikos* 29, 591 · CITES (1973) · Wild Life (Protection) Amendment Act (2006).
