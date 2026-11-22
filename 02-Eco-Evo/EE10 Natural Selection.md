---
title: EE10 Natural Selection
aliases: [EE10, natural selection, selection, Darwin's finches, Daphne Major, directional selection, stabilizing selection, disruptive selection, BI2113 lecture 10]
subject: eco-evo
type: chapter
chapter: 10
part: IV
scope: [taught, extra-book, extra-beyond]
by: [slides]
status: draft
prereq: ["[[EE09 Hardy-Weinberg Equilibrium]]", "[[EE08 Evolution - An Introduction]]"]
tags: [subject/eco-evo, type/chapter, taught, extra/book, extra/beyond, src/slides, src/book, src/own-notes, status/draft]
---
# EE10 · Natural Selection

◀ [[EE09 Hardy-Weinberg Equilibrium]] · [[Ecology and Evolution - Course Map|Course Map]] · wrap-up: [[Ecology and Evolution - Course Map#Course wrap-up (lecture of 13 Nov 2026)|Putting it all together]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**: the lecture ([[Selection_Class Lecture.pdf|16 slides]]) **and** the *mandatory* reading, Freeman & Herron, *Evolutionary Analysis* 5th ed., **Ch. 3** "Evolution by natural selection" ([[Ch3 from Evolutionary Analysis_5ed_Freeman and Herron.pdf|reading]]; the lecture: "would give a nice, more rigorous account of this study. Read it to internalize the concepts").
> - §1 definition; natural vs artificial selection (sl. 1)
> - §2 the Galápagos finches on Daphne Major, through Darwin's four postulates (sl. 2–3 videos; Freeman & Herron §3.2, §3.4)
> - §3 the lessons of Daphne Major (sl. 3)
> - §4 directional, stabilizing and disruptive selection (sl. 4–7)
> - §5 the nature of selection: individuals vs populations, phenotypes vs genes, the "mess" (sl. 8–10; F&H §3.5)
> - §6 what selection is not: not forward-looking, not progressive, not perfect, yet able to make new traits (sl. 11–15)
>
> 🟡 **Extra · book**: heritability and the parent–offspring regression with its pitfalls (F&H pp. 84–85); the 1980/82, 1983 and 2003–04 episodes and thirty-year trends (F&H pp. 88–90).
>
> 🔵 **Extra · beyond**: §7 the **one-locus selection model** (how selection enters the HW cycle of [[EE09 Hardy-Weinberg Equilibrium]]), dominance and the speed of selection, heterozygote advantage and disadvantage, the breeder's equation; the interactive tool. All numbers in `scripts/ee08_10_numbers.py`.

> [!key] After this chapter you can
> - define natural selection (Zimmer & Emlen) and say why "artificial" selection is not a different process,
> - test **Darwin's four postulates** on the Daphne Major finches with the Grants' data, and state the **three lessons** the lecture draws,
> - draw and distinguish **directional, stabilizing and disruptive** selection,
> - explain "selection acts on individuals/phenotypes, evolution happens in populations/allele frequencies", and why **heritability** decides whether selection causes evolution,
> - explain why selection is **always behind**, **not progressive**, works with **what is available**, and still produces **new traits**,
> - *(beyond)* write $\Delta p$ for one locus and use it for dominant, recessive, additive, over- and underdominant fitnesses.

> [!intuition] The one-sentence story
> In a drought year on a tiny Galápagos island, the finches with deep beaks could crack the only seeds left and the others starved; because beak depth is heritable, the next generation had deeper beaks — selection happened to individuals, evolution happened to the population, and when the rains returned the direction reversed.

## 1. What natural selection is
<span class="scope-taught">taught</span> *[[Selection_Class Lecture.pdf#page=1|slide 1]]*

> [!key] Definition (Zimmer and Emlen 2013, slide 1)
> **Natural selection is the differential survival and reproduction of individuals due to differences in phenotype.**

The lecture adds that the distinction between natural and artificial selection "is rather… artificial and persists in the literature primarily due to historical reasons"; modern books often drop it. Freeman & Herron open Chapter 3 the same way: Darwin "realized that a process much like artificial selection happens automatically in nature" (p. 77).

> [!key] Darwin's four postulates and the consequence (Freeman & Herron p. 77)
> 1. Individuals within a population **differ** from one another.
> 2. The differences are, at least in part, **passed from parents to offspring**.
> 3. Some individuals are **more successful at surviving and reproducing** than others.
> 4. The successful individuals are **not merely lucky**: they succeed because of the variant traits they inherited and will pass on.
>
> If all four hold, **the composition of the population inevitably changes** from one generation to the next. (Compare Darwin's chain of observations and inferences in [[EE08 Evolution - An Introduction]] §4.)

## 2. The finches of Daphne Major
<span class="scope-taught">taught</span> *[[Selection_Class Lecture.pdf#page=2|slides 2–3]] (HHMI and Princeton videos)* · <span class="scope-extra-book">extra · book (mandatory)</span> *Freeman & Herron §3.4, pp. 81–90 (read)*

Daphne Major is a tiny island in the Galápagos; its **medium ground finch**, *Geospiza fortis*, has been monitored every year since **1973** by Peter and Rosemary Grant and their team (a population of about 1200; by 1977 most birds were marked and measured). The lecture calls this "one of the greatest and most famous pieces of work in evolution in the twentieth century". Freeman & Herron test each postulate:

| postulate | the Daphne Major evidence (F&H pp. 83–89) |
|---|---|
| 1. variation | wing, tail and beak measurements of every bird: **beak depth varies** (a roughly bell-shaped distribution, ~7–11 mm in the 1976 sample; Fig. 3.10) |
| 2. heritability | Boag's parent–offspring comparison: deep-beaked parents have deep-beaked chicks (Fig. 3.11). Keller et al., after DNA checks showed **20 % of chicks had extra-pair fathers** and excluding them: heritability of beak depth **$h^2=0.65\pm0.15$** (Computing Consequences 3.1) |
| 3. differential survival | the **1977 drought**: **24 mm** of rain instead of the usual **130 mm**; no breeding; **84 % of *G. fortis* disappeared** in 20 months, most of starvation (38 emaciated birds found dead). Mortality on this scale is normal: 89 % of *G. conirostris* die before breeding; 19 % and 25 % of *G. fortis* died in the 1980 and 1982 droughts |
| 4. non-random survival | the soft small seeds went first; then the large, hard fruits of ***Tribulus cistoides*** were the main food, which only **large birds with deep beaks** can crack. Survivors (random sample of 90) had **deeper beaks and larger bodies** than the pre-drought population (Fig. 3.14) |
| the consequence | chicks hatched in **1978** had deeper beaks, on average, than those of **1976** (Fig. 3.15): **the population evolved** |

Then the direction **reversed**. In **1983** an El Niño brought **1359 mm** of rain ("almost 57 times as much as in 1977"; $1359/24=56.6$): small soft seeds became superabundant and **smaller** birds were favoured (Gibbs and Grant 1987). Over thirty years the population's beak size rose in 1977, stayed high until the mid-1980s, returned to its starting value, and in the **2003–04 drought** — as bad as 1977 — evolved toward **smaller** beaks, because the newly arrived large ground finch *G. magnirostris* took the large *Tribulus* seeds. By 2001 the average bird had a sharper beak and a smaller body than in the mid-1970s (F&H pp. 88–90).

> [!example] 🔵 How much evolution? The breeder's equation (extra · beyond)
> The response of the mean to one round of selection is $R=h^2S$, where $S$ is the **selection differential** (mean of the breeders minus the population mean). Why the factor $h^2$: the survivors' beaks are deeper partly because of their genes and partly because of luck in development (food as a chick, for instance). Only the genetic part is passed on, and $h^2$ is the fraction of the variation that is genetic (additive). So the offspring keep that fraction of their parents' advantage. With $h^2=0$ the offspring regress all the way back to the old mean, which is the bounce-back of §5. With $h^2=0.65$, a differential of $S=0.5$ mm in beak depth would shift the next generation by $R=0.33$ mm; $S=0.25$ mm gives $R=0.16$ mm. *The $S$ values here are illustrative; F&H's Chapter 3 reports the distributions but these pages do not give the 1977 differential.* The equation and its derivation belong to quantitative genetics (Freeman & Herron's later chapter, not read).

## 3. Lessons from Daphne Major
<span class="scope-taught">taught</span> *[[Selection_Class Lecture.pdf#page=3|slide 3]]*

1. **Evolution can occur very rapidly and dramatically.**
2. **Sources of selection often shift**, so evolution reverses itself or takes new directions.
3. **The see-saw of selection** in changing environments may give the impression of **stately gradual change**: the fossil record usually lacks the resolution to see "zig-zaggy" evolution. A fossil bed typically mixes thousands of years of individuals. Over such a span the up-and-down swings largely cancel, and only the small *net* drift remains visible. Slow change in the record is therefore compatible with fast change in each generation.

F&H add: small changes over short spans **accumulate** into larger changes over long spans (p. 90).

## 4. Three modes of selection
<span class="scope-taught">taught</span> *[[Selection_Class Lecture.pdf#page=4|slides 4–7]]*

| mode | who survives / reproduces best | effect on the trait distribution (gen $t$ → gen $t+x$) | example |
|---|---|---|---|
| **directional** | one extreme | the mean shifts | beak depth in 1977 (deeper) and in 1983 / 2004 (smaller) |
| **stabilizing** | intermediates | mean unchanged, **variance shrinks** | *(classic textbook case, human birth weight; not on the slides)* |
| **disruptive** | both extremes | variance grows; can split the distribution | *(e.g. two seed types with no intermediate; not on the slides)* |

![[fig_ee10_selection_modes.png|640]]
*Figure EE10.1. The three modes as a fitness function $w(z)$ acting on a normal trait distribution (before: grey; after selection: colour). Directional: the mean moves; stabilizing: the variance falls; disruptive: the variance rises. Made with `scripts/fig_ee10.py` (extra · beyond).*

## 5. The nature of selection
<span class="scope-taught">taught</span> *[[Selection_Class Lecture.pdf#page=8|slides 8–10]]* · <span class="scope-extra-book">extra · book</span> *F&H §3.5, pp. 90–91*

- **Selection acts on individuals, but its effects are seen on the population** (sl. 8). "A given individual either survives or dies… the population evolves." No finch's beak grew from the effort of cracking *Tribulus*; the average rose because more small-beaked birds died (F&H p. 90). A tan is not inherited; a heritable *tanning capacity* is.
- **Selection acts on phenotypes, but change happens only when allele frequencies change** (sl. 9). We identify selection by changes in allele or genotype frequencies. If beak variation had been entirely environmental ($h^2=0$), the drought would still have killed the small-beaked birds, but the next generation would have bounced back: **no evolution** (F&H Fig. 3.18).
- **"The mess that is natural selection"** (sl. 10): the cycle genes → genotype → (with the **biotic and abiotic environment**) phenotype → selection → meiosis → fertilisation → genes, with **chance** tempering every step. The wrap-up lecture's caption: "**Selection acts on phenotypes; genotypes get selected; genes get differentially transmitted to the offspring**" ([[Putting it all together_13-11-2026.pdf#page=13|wrap-up slide 13]]).

> [!pitfall] Natural selection is not evolution
> Selection is one cause of evolution (with drift, mutation, migration, non-random mating: the broken HW assumptions of [[EE09 Hardy-Weinberg Equilibrium]]); and selection without heritable variation produces no evolution. The wrap-up lecture lists "natural selection is not evolution" among its chief messages ([[Putting it all together_13-11-2026.pdf#page=13|slide 13]]).

## 6. What selection is not
<span class="scope-taught">taught</span> *[[Selection_Class Lecture.pdf#page=11|slides 11–15]]* · <span class="scope-extra-book">extra · book</span> *F&H pp. 91–92*

- **Selection is always behind** (sl. 11). It changes gene frequencies *after* exposure: the 1978 finches were adapted to the 1977 drought, not to whatever came next. Selection **cannot anticipate** the environment; if the environment changes too fast, the population may go extinct. New mutations do not arise to solve problems. Evolving populations "always lag at least a generation behind" (F&H p. 91).
- **Selection is not progressive** (sl. 12). Organisms "devolve" as often as they evolve (parasitism is a common way of life); adaptation happens by character **gain, loss and modification**.
- **Selection acts with whatever is available** (sl. 13–14). It operates on **pre-existing variation**, often imperfect; characters co-opted for new uses are **preadaptations**. "There is no grand design… no betterment of species… no concept of perfection." Slide 14: male mosquitofish, *Gambusia affinis*, whose **gonopodia attract mates but hinder escape**; the male from a high-predation population has the smaller one — a trade-off, not an optimum.
- **New traits can still evolve** (sl. 15) through **mutation and recombination**: selection generates no variation itself, but sorts among the new combinations those processes create. F&H's example: the Illinois corn oil experiment, running since 1896 with 163 ears — oil content rose from 4–6 % to about 20 % in 100 generations, far beyond the range in the starting population (p. 92).

## 7. One-locus selection: the HW cycle with fitness
<span class="scope-taught">beyond</span> <span class="scope-extra-beyond">extra · beyond</span> *standard population genetics; derivation mine, numbers in `scripts/ee08_10_numbers.py`*

Hartl's split of the life cycle ([[EE09 Hardy-Weinberg Equilibrium]] §6) tells us where to put selection: zygotes form in HW proportions, then survive to breed in proportion to their **fitnesses** $w_{11},w_{12},w_{22}$:
$$p'=\frac{p^2w_{11}+pq\,w_{12}}{\bar w},\qquad \bar w=p^2w_{11}+2pq\,w_{12}+q^2w_{22},$$
$$\boxed{\Delta p=\frac{pq\,[\,p(w_{11}-w_{12})+q(w_{12}-w_{22})\,]}{\bar w}}.$$
$\Delta p$ carries the factor $pq$: selection is slow when either allele is rare, because there is little variation to act on.

> [!example] How long does an advantageous allele take to spread? ($s=0.1$, $p$ from 0.01 to 0.99)
> | favoured allele $A_1$ is… | fitnesses $w_{11}:w_{12}:w_{22}$ | generations |
> |---|---|---|
> | additive (heterozygote halfway) | $1:0.95:0.9$ | **175** |
> | dominant | $1:1:0.9$ | **1075** |
> | recessive | $1:0.9:0.9$ | **981** |
>
> A **dominant** favoured allele spreads fast at first, because a rare allele sits almost entirely in heterozygotes (HW property 5) and a dominant allele shows its full advantage there. But it stalls at the end: the last recessive $A_2$ alleles hide in heterozygotes, invisible to selection (property 5 of HW). A **recessive** favoured allele is invisible when rare and stalls at the start. Additive is fastest overall.

> [!example] Balancing and disruptive selection at one locus
> **Heterozygote advantage** ($w_{11}=1-s$, $w_{12}=1$, $w_{22}=1-t$): a stable internal equilibrium $p^*=t/(s+t)$; with $s=0.2$, $t=0.1$: $p^*=1/3$, reached from $p=0.9$ (the script returns 0.3333 after 500 generations). This **maintains variation** — the classic human case, sickle-cell haemoglobin in malarial regions, is named here from general knowledge. **Heterozygote disadvantage** ($1:0.9:1$): $p=0.5$ is an *unstable* equilibrium; from $p=0.51$ the population goes to fixation of $A_1$ — the one-locus version of disruptive selection, with a threshold like the Allee effect ([[Allee Effect]]).


## 8. Reading tiers and suggested reading
<span class="scope-taught">taught</span> *[[Selection_Class Lecture.pdf#page=16|slide 16]], [[Selection_Class Lecture.pdf#page=2|slide 2]]; [[Putting it all together_13-11-2026.pdf#page=14|wrap-up slides 14–15]]*

| item | tier |
|---|---|
| lecture slides | syllabus |
| Freeman & Herron, *Evolutionary Analysis*, Ch. 3 | **mandatory** |
| HHMI *The Origin of Species: The Beak of the Finch* video and activities; Princeton 2017 news story (a new species in two generations) | in the lecture ("nothing to do with the exams" for the activities) |
| Weiner, *The Beak of the Finch* (Pulitzer 1995) | for fun ("a superb read") |
| Ridley, *Evolution* (2004): "glamour-less and outdated, but perhaps the most rigorous"; Freeman & Herron: "glamorous, up-to-date, mostly good. Recommended" | serious textbooks (wrap-up) |

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: One-locus selection with drift
> Zygotes form in Hardy–Weinberg proportions and survive with fitnesses w11 = 1, w12 = 1 − hs, w22 = 1 − s (allele A1 favoured when s > 0; h is the dominance of the deleterious allele A2), or choose heterozygote advantage/disadvantage.
>
> ![[ee_selection.png|720]]
>
> **Try:** With s = 0.1 and p0 = 0.01: h = 0.5 (additive) takes 175 generations to reach p = 0.99; h = 0 (A1 dominant) and h = 1 (A1 recessive) take about 1000 (the script values are 1075 and 981). Choose 'heterozygote advantage' with s = 0.2, t = 0.1: every run settles at p* = 1/3. Set N = 20: drift can lose even a favoured allele.
>
> [▶ Open the tool in your browser](../Assets/interactive/ee_selection.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/ee_selection.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How EE10 connects
> **Builds on:** [[EE09 Hardy-Weinberg Equilibrium]] (the null model selection departs from), [[EE08 Evolution - An Introduction]] (Darwin's logic). **Ecology chapters seen again:** [[EE05 Predation]] (predators as agents of selection: the *Gambusia* gonopodium), [[EE04 Competition and Invasions]] (*G. magnirostris* changing selection on *G. fortis* in 2004: competition as a selective force), [[EE07 Conservation Biology]] (environment changing faster than selection can follow → extinction).
> **Concepts:** [[Natural Selection]] · [[Modes of Selection]] · [[Heritability]] · [[Darwin's Finches on Daphne Major]] · [[Fitness and Relative Fitness]] · [[Hardy-Weinberg Equilibrium]] · [[Population Thinking]]
> **Other subjects:** [[CL20 ENSO and the Walker Circulation]] (the 1983 El Niño that reversed selection) · [[Probability - Course Map]] (regression of offspring on parents; replicate stochastic trajectories)

## Summary
> [!summary] Cheat-sheet
> - **Natural selection** = differential survival and reproduction due to phenotype differences. Natural vs artificial: a historical distinction.
> - **Four postulates**: variation, heritability, differential success, non-random success → the population changes.
> - **Daphne Major** (*G. fortis*, Grants since 1973): 1977 drought 24 vs 130 mm, 84 % died, *Tribulus* → deeper beaks; $h^2=0.65$; 1978 chicks deeper-beaked; 1983 El Niño 1359 mm → smaller; 2004 drought + *G. magnirostris* → smaller.
> - **Lessons**: rapid; reversible; zig-zags look gradual in fossils.
> - **Modes**: directional (mean moves), stabilizing (variance falls), disruptive (variance rises).
> - Acts on **individuals/phenotypes**; evolution = change in **populations/allele frequencies**; needs heritability.
> - **Always behind; not progressive; works with what is available (preadaptations, trade-offs: *Gambusia*); new traits via mutation + recombination.**
> - *(beyond)* $\Delta p=pq[p(w_{11}-w_{12})+q(w_{12}-w_{22})]/\bar w$; dominance slows the end, recessivity the start; overdominance $p^*=t/(s+t)$.

## Practice
1. State Darwin's four postulates and show how the Grants tested each on Daphne Major.
2. Why did the 1977 drought favour deep beaks? Why did 1983 favour small birds?
3. The heritability estimate rose once extra-pair chicks were excluded? Explain how misidentified paternity biases a parent–offspring regression, and in which direction.
4. Sketch the trait distribution before and after (a) directional, (b) stabilizing, (c) disruptive selection.
5. "Finch beaks grew larger because the birds needed to crack hard seeds." Correct this.
6. Two populations experience the same selective deaths, but in one $h^2=0$ and in the other $h^2=0.65$. Compare the next generation.
7. Explain "selection is always behind" with the 2003–04 drought.
8. Why is a dominant advantageous allele slow to reach fixation? Compute $\Delta p$ for $w=1:1:0.9$ at $p=0.5$ and at $p=0.95$.
9. With $w_{11}=0.7$, $w_{12}=1$, $w_{22}=0.9$, find the equilibrium and say whether it is stable.
10. **Exam-style.** "Natural selection is not evolution." Discuss with the finch study and the lecture's slides on the nature of selection.

> [!example]- Solutions
> 1. §2 table.
> 2. Drought: few seeds, the small soft ones eaten first, then only large hard *Tribulus* fruits remained, which only deep, large beaks can crack; large birds also win fights over food. 1983: small soft seeds superabundant, which small birds with shallow beaks harvest more efficiently.
> 3. A chick fathered by an extra-pair male is plotted against a social father it is unrelated to, adding noise that flattens the regression: misidentified paternity **underestimates** heritability (F&H p. 84). Excluding the 20 % extra-pair chicks gave 0.65.
> 4. Figure EE10.1.
> 5. Individuals did not change their beaks; more small-beaked birds died and the survivors' (heritable) deep beaks were passed on. The population's mean changed.
> 6. $h^2=0$: the next generation's distribution returns to the pre-selection one (no evolution). $h^2=0.65$: the offspring mean shifts by $0.65S$.
> 7. The 1978–2003 population was shaped by earlier conditions; in 2004 the arrival of *G. magnirostris* changed which seeds were available to *G. fortis*, so the large beaks favoured in 1977 were now a disadvantage. Selection responded only after the deaths.
> 8. With $A_1$ dominant, $A_2$ is hidden in heterozygotes when rare. $\Delta p=pq[p\cdot0+q\cdot0.1]/\bar w=0.1pq^2/\bar w$. At $p=0.5$: $\bar w=0.975$, $\Delta p=0.0128$; at $p=0.95$: $\bar w=0.99975$, $\Delta p=0.1\times0.95\times0.0025/0.99975=2.4\times10^{-4}$.
> 9. Overdominance with $s=0.3$, $t=0.1$: $p^*=0.1/0.4=0.25$, **stable**.
> 10. Selection changes the phenotype distribution within a generation; evolution requires the change to be inherited (heritability) and is measured in allele/genotype frequencies; other forces also cause evolution. Finches: selection in 1977 (deaths) → evolution because $h^2=0.65$ → 1978 chicks deeper-beaked; reversals show selection tracks the environment with a lag.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | definition, natural vs artificial | [[Selection_Class Lecture.pdf#page=1\|sl. 1]] (Zimmer & Emlen 2013) | taught |
> | finch videos, readings, Daphne lessons | [[Selection_Class Lecture.pdf#page=2\|sl. 2–3]] | taught |
> | modes of selection | [[Selection_Class Lecture.pdf#page=4\|sl. 4–7]] | taught |
> | individuals vs populations; phenotypes vs alleles; the "mess" diagram | [[Selection_Class Lecture.pdf#page=8\|sl. 8–10]] | taught |
> | always behind, not progressive, what is available, *Gambusia*, new traits | [[Selection_Class Lecture.pdf#page=11\|sl. 11–15]] | taught |
> | four postulates; Daphne Major study; heritability; droughts and El Niño; trends to 2004; nature of selection; corn oil | Freeman & Herron Ch. 3, pp. 77–92 (OCR of the scan; §3.2, §3.4, §3.5 read; §3.1, §3.3, §3.6–3.7 not read) | taught (mandatory reading) |
> | chief messages on selection; reading list | [[Putting it all together_13-11-2026.pdf#page=13\|wrap-up sl. 13–15]] | taught |
> | breeder's equation example ($S$ illustrative), one-locus model, dominance timings, over/underdominance | `scripts/ee08_10_numbers.py`, `scripts/fig_ee10.py` | extra/beyond |
>
> **Read and not read.** Slide 10's diagram is a cycle of rotated text boxes; its reading here follows the wrap-up lecture's clean version (slide 13). F&H page numbers are the printed ones (OCR page index + 72, checked against the running heads on pp. 87, 89, 91). Stabilizing and disruptive examples and the sickle-cell case are general knowledge, labelled as such. The videos, the Princeton story and Weiner's book were not consulted.
