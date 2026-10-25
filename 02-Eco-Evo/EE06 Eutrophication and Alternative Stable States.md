---
title: EE06 Eutrophication and Alternative Stable States
aliases: [EE06, Eutrophication, Alternative stable states, Lake restoration, Shallow lakes, BI2113 lecture 6]
subject: eco-evo
type: chapter
chapter: 6
part: III
scope: [taught, extra-book, extra-beyond]
by: [slides]
status: draft
prereq: ["[[EE05 Predation]]"]
tags: [subject/eco-evo, type/chapter, taught, extra/book, extra/beyond, src/slides, src/book, src/paper, src/own-notes, status/draft]
---
# EE06 · Eutrophication and Alternative Stable States

◀ [[EE05 Predation]] · [[Ecology and Evolution - Course Map|Course Map]] · [[EE07 Conservation Biology]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**: the lecture of 4 Sep 2026 ([[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf|27 slides]]) **and** the *mandatory* readings: Lampert and Sommer, *Limnoecology*, §8.5.4–8.6.2, pp. 251–259 ([[Eutrophication_Limnoecology.pdf|reading]]) and Søndergaard et al. (2012), *Lake Restoration*, pp. 455–458 ([[Sondegaard et al_Lake Restoration_Encyclopedia of Lakes and Reservoirs.pdf|reading]])
> - §1 the two concepts: trophic conditions of lakes, restoration (sl. 1)
> - §2 classical (Naumann-Thienemann) and modern (continuum) lake types (sl. 2–3)
> - §3 what determines the trophic status (sl. 4–5)
> - §4 how a lake goes from oligotrophic to eutrophic (sl. 6–9)
> - §5 reversing it: Lake Washington; Lake Erie (sl. 10–13)
> - §6 "not so simple": alternative stable states, the shallow-lake feedback, the catastrophic shift (sl. 14–19)
> - §7 biomanipulation; how bad is it; the three kinds of restoration methods (sl. 20–24)
> - §8 summary and references (sl. 25–27)
>
> 🟡 **Extra · book** (the *paper* and *detailed reading* tiers: no exam weight)
> - §6 Scheffer et al. (2001), *Nature* 413 (catastrophic shifts; **Box 1**, a minimal model); Scheffer and van Nes (2007), *Hydrobiologia* 584 (shallow lakes revisited)
> - §5 "Rescue of Lake Stinko" (the Lake Washington story); Farley (2012), *Eutrophication in Freshwaters: An International Review* (detailed reading; a scan, not read)
> - the "hardcore maths" and "maths-free" suggestions at the end of the deck: Ashwin et al. (2012) and Scheffer (2009), *Critical Transitions in Nature and Society*
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §2 the Vollenweider retention-time relation worked in numbers
> - §6 the Box 1 model solved: folds, the bistable window, the size of the jumps and the "92 % rule" for restoring a lake; the signs of the feedback loop

> [!key] After this chapter you can
> - name the **classical** lake types and the **modern** continuum with its total-phosphorus classes,
> - list the **four factors** that set a lake's trophic status and the **chain of events** of eutrophication, including **internal loading**,
> - tell the **Lake Washington** story and say why recovery lags behind a cut in loading,
> - explain **alternative stable states**, **hysteresis** and a **catastrophic regime shift** for shallow lakes, with the sign-multiplication rule for the feedback loop,
> - explain **biomanipulation** and why it can work,
> - list the **physical, chemical and biological** restoration methods with their drawbacks.

## 1. Two concepts: trophic condition and restoration
<span class="scope-taught">taught</span> *[[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=1|slide 1]]*

The lecture is organised around two ideas: **trophic conditions in lake ecosystems** (how productive a lake is, and why) and **restoration of lakes** (how to reverse unwanted change). The route runs from classification, through the mechanism of change, to a case where the obvious cure does not work, and from that to the mathematics of thresholds. It is the *ecological twin* of the climate chapter on multiple steady states ([[CL04 Feedback and Multiple Steady States]]).

## 2. Lake types: from classical boxes to a continuum
<span class="scope-taught">taught</span> *[[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=2|slides 2–3]]* · *Lampert and Sommer §8.5.4*

**Classical view** (slide 2; Einar Naumann and August Thienemann): ([[Trophic State of Lakes]])

- **Oligotrophy**: little productivity and clear water.
- **Eutrophy**: high productivity and greenish water from phytoplankton.
- **Dystrophy**: low conductivity and water coloured brown by dissolved humic substances.
- then **extinction** of the lake (it fills with sediment and becomes land).

Lampert and Sommer give the original *qualitative* criteria: oligotrophic lakes have an **orthograde** oxygen profile in summer (oxygen stays high with depth) and an oxidised sediment surface, eutrophic lakes a **clinograde** profile (oxygen falls to zero in the hypolimnion) and a reduced sediment surface, with indicator organisms (the chironomid *Tanytarsus* in oligotrophic, *Chironomus*, which can survive anoxia, in eutrophic lakes).

**Modern view** (slide 3): "'Oligotrophic' and 'eutrophic' are regions of a **trophic continuum** that can be separated by established limits, such as the **$P_{tot}$ concentration during the spring circulation**", and, since trophic condition is "clearly a biological phenomenon, several criteria need to be considered". The reading's classes (total phosphorus in µg L⁻¹ at spring circulation):

| class | $P_{tot}$ (µg L⁻¹) |
|---|---|
| ultra-oligotrophic | < 5 |
| oligotrophic | 5–10 |
| mesotrophic | 10–30 |
| eutrophic | 30–100 |
| hypereutrophic | > 100 |

| characteristic (Box 8.1) | oligotrophic | eutrophic |
|---|---|---|
| morphometry | deep | shallow |
| primary production | low (50–300 mg C m⁻² d⁻¹) | high (> 1000) |
| chlorophyll *a* | 0.3–3 µg L⁻¹ | 10–500 µg L⁻¹ |
| cyanobacterial blooms | sparse | plentiful |
| hypolimnetic oxygen | little depletion; orthograde | strong, may be anoxic; clinograde |
| profundal benthos | diverse, oxygen-requiring | species-poor, tolerates low O₂ |
| fish | deep-water salmonids, coregonids | cyprinids, sunfish ("warm-water" fish) |

> [!pitfall] A single number can mislead
> The reading's own example: **Schöhsee** (mean depth 13 m, $P_{tot}\approx20$ µg L⁻¹) is *mesotrophic* by the OECD phosphorus criterion but has an anoxic hypolimnion, so it is *eutrophic* in the traditional sense. **Lake Constance** (mean depth about 100 m) had $P_{tot}\approx100$ µg L⁻¹ in 1980, which by phosphorus is eutrophic, yet the oxygen near the bottom was only about 50 % saturated at the end of summer, "mesotrophic" in the old scheme. The difference is **morphometry**: Lake Constance's enormous hypolimnion brings a big oxygen supply at spring overturn, enough to decompose the sinking organic matter, whereas Schöhsee's small hypolimnion has little. Thienemann already saw that lakes whose epilimnion-to-hypolimnion volume ratio exceeds 1 tend to be eutrophic.

> [!extra-beyond]- 🔵 Extra (beyond): the retention-time relation in numbers
> The reading quotes the OECD study (Vollenweider and Kerekes 1982): the lake concentration $P_L$ follows the inflow concentration $P_{in}$ and the theoretical **hydraulic retention time** $\tau_w$ (years) as
> $$P_L=1.55\left[\frac{P_{in}}{1+\sqrt{\tau_w}}\right]^{0.82}\quad(r^2=0.86,\ n=87).$$
> For the *same* inflow $P_{in}=50$ µg L⁻¹: $\tau_w=0.5$ yr gives $P_L=24.7$ (mesotrophic); $\tau_w=1$ yr gives 21.7; $\tau_w=10$ yr gives 11.9 (still mesotrophic); $\tau_w=100$ yr gives 5.4 (oligotrophic). A long retention time lets sedimentation remove phosphorus: big, slowly flushed lakes tolerate a given loading better than small ones (`scripts/ee06_numbers.py`).

## 3. What sets a lake's trophic status?
<span class="scope-taught">taught</span> *[[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=4|slides 4–5]]*

Slide 4 asks the question; slide 5 answers with four factors:

1. **Original basin shape**: mean depth.
2. **Nature of the drainage basin**: erosion rates; soil composition determines the nutrient inputs.
3. **Climate**: rain and snowfall; mean temperature.
4. **Human activity** (**cultural eutrophication**): fertilisers; human waste (domestic and industrial).

Lampert and Sommer give the reasons for the old observation that **large, deep lakes are less productive than small, shallow ones**: (i) with the same supply of nutrients per unit watershed area, the loading *per unit lake volume* depends on the ratio of lake volume to watershed area, so a lake that is large relative to its watershed has a low loading; (ii) in a deep lake only a small part of the epilimnion touches the sediment in summer, so little nutrient returns to the lit zone; (iii) larger lakes usually have longer retention times, and more of the nutrients are lost by sedimentation (the Vollenweider relation above).

> [!intuition] A bathtub with a slow tap and a leaky bottom
> The nutrient content of a lake is the balance of a *tap* (loading from the watershed), a *drain* (outflow, i.e. flushing) and a *leak into the mud* (sedimentation). Deep, slowly flushed basins with a small watershed have a small tap and a big leak: low nutrient concentration. Shallow lakes with big catchments have the reverse.

## 4. How a lake becomes eutrophic
<span class="scope-taught">taught</span> *[[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=6|slides 6–9]]* · *Lampert and Sommer §8.6.1*

The chain on slides 6–7 ([[Cultural Eutrophication]]):

1. **Nutrient enrichment, particularly phosphorus**: natural, or anthropogenic (urban, industrial, agricultural).
2. **Increased organic-matter production** (eutrophication proper): more **algal blooms**, including the **blue-green algae (cyanobacteria) *Anabaena*, *Microcystis***; **reduced light**; **reduction of dissolved oxygen, especially in the hypolimnion**, where a **series of anoxic reactions releases phosphorus**; an **increase in pH**.
3. **Death of fishes and other aquatic life** (a fish-kill).

Slide 8 stresses that this "is not a problem of small lakes alone" (the **Caspian Sea, 2003**).

What the reading adds ([[Eutrophication_Limnoecology.pdf#page=3|pp. 253–255]]):

- **Causes of the loading.** There is "considerable consensus" that the major cause is increased phosphorus loading: sewage, **phosphorus-containing detergents**, fertiliser and erosion. Nitrogen loading rises through fertiliser and atmospheric nitrogen oxides, but phosphorus, "unlike nitrogen, is relatively immobile once it is in the soil". For Lake Constance before treatment, detergent phosphorus and faecal phosphorus in sewage were the dominant sources. **Domestic sewage has an N:P ratio of about 4:1**, so it can push a lake from phosphorus to **nitrogen limitation** ([[Nutrient Limitation]]).
- **Cyanobacterial blooms** are the most undesirable consequence: dense surface scums, some strains **toxic or allergenic**, bad taste and odour; classic problem genera are the nitrogen-fixing *Anabaena* and *Aphanizomenon* and the non-fixing *Microcystis*, *Limnothrix* and *Planktothrix*.
- **Littoral effects.** More nutrients in the water favour **periphyton** (algae growing on plants) over **submerged macrophytes**, which are overgrown and shaded: the plants and their fauna decline.
- **Hypolimnion and sediments.** The main effect is higher oxygen consumption by decaying algae. Anoxia impoverishes the deep-water fauna and eliminates natural reproduction of fish that spawn on the bottom (lake whitefish). It also starts a chain of anaerobic reactions (nitrate ammonification, denitrification, desulfurication, methane formation). "**The release of phosphorus from the anoxic sediments (internal loading) is extremely important, as this sets in motion the self-acceleration of eutrophication**" ([[Internal Phosphorus Loading]]).
- **Fish kills.** Summer kills can follow a high pH from intense photosynthesis in lakes with high ammonium, which converts the harmless ammonium ion into toxic ammonia; winter kills occur under ice when decomposition consumes the oxygen.

> [!derivation] Why internal loading is a *feedback*
> Under oxygen the iron(III)-phosphate in the sediment holds the phosphorus; anoxia reduces Fe(III) to Fe(II) and releases phosphate (Mortimer's mechanism; the reading only says "anoxic sediments", the iron chemistry is background, see [[Inorganic Chemistry - Course Map]]). The loop is: more phosphorus → more algae → more sinking organic matter → more oxygen consumption in the hypolimnion → more anoxia → more phosphorus release → more algae. Because the effect of the phosphorus on itself has the **same sign** (+) all the way round, the loop is **reinforcing**: the lake pumps itself. The same logic as the ice-albedo feedback in [[Ice-Albedo Feedback]], with phosphorus in place of temperature.

> [!connection] Stratification matters
> The anoxic hypolimnion exists only when a lake stratifies in summer (a warm, lit, mixed epilimnion above a cold, dark hypolimnion that is cut off from the air; see [[Thermal Stratification of Lakes]]), which is why deep lakes with a large hypolimnion (Lake Constance) tolerate more phosphorus than shallow stratified ones (Schöhsee).

## 5. Reversing it: Lake Washington (and Lake Erie)
<span class="scope-taught">taught</span> *[[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=10|slides 10–13]]* · <span class="scope-extra-book">extra · book</span> *Rescue of Lake Stinko*

Slide 10 asks "how can we reverse this process?" and slide 11 tells the story of **Lake Washington, Seattle** ([[Lake Washington Recovery]]). The slide's chronology (1940s oligotrophic; 1950–60s sewage disposal in the lake; studies of causes, sewage implicated by W. T. Edmondson, 1970; sewage diverted to the sea; as phosphorus fell the lake improved; further improvement when *Daphnia* came back after the cyanobacteria disappeared; detergent makers reduced phosphate over time) is filled out by the readings:

| when | event (Lampert and Sommer; *Rescue of Lake Stinko*) |
|---|---|
| around 1900–1941 | Seattle discharges raw sewage into the lake; the last city outfall removed by 1941 |
| 1941–1953 | suburbs add ten sewage treatment plants (80 million litres per day) |
| 1955 | cloudier water; a sample holds the cyanobacterium *Oscillatoria rubescens*, new to the lake: Edmondson takes it as an alarm |
| 1958 | the first public vote for a metropolitan sewer authority ("Metro") fails in March; the second passes on 9 September (58 % of Seattle, 67 % elsewhere in the county) |
| early 1960s | transparency about 1 m, smelly blooms; the press names it "Lake Stinko" (5 Oct 1963) |
| 1964–65 | deterioration slows and stops as diversions come on line |
| 1968 | sewage diversion to Puget Sound complete; the phosphorus concentration falls to a new low equilibrium within about 2 years |
| 1970–1975 | transparency 3–4 m |
| 1976 | large *Daphnia* return; transparency **doubles to up to 10 m** |

> [!verify] The slide says "Oligotrophy → Lake Stinko"
> Slide 11 reads "Sewage disposal in the lake → Oligotrophy → Lake Stinko". Sewage makes a lake *eutrophic*; "Lake Stinko" is the eutrophic state. 'Oligotrophy' there is a slip (the lake was oligotrophic-mesotrophic *before*).

> [!key] Why the second jump?
> The jump from 3–4 m to 10 m in 1976 "was clearly not simply a direct response to the reduced phosphorus": the cleared lake allowed the return of *Daphnia*, which graze phytoplankton. Two mechanisms are given: the **disappearance of filamentous cyanobacteria** that clog *Daphnia*'s filtering apparatus (bottom-up) and **reduced predation by mysid shrimp** (top-down). The lesson of the reading: Lake Washington shows "how the structure of the food web and biotic interactions affect the success of nutrient reduction measures".

> [!extra-book]- 🟡 Extra (book): *Rescue of Lake Stinko* in one paragraph
> The article (University of Washington, from Lehman) credits "a unique blend of scientific judgment and public action": Edmondson's basic research on how algal mass tracks nutrient addition; his nine-page question-and-answer summary for the policy committee (15 questions such as "Why not poison the algae?"); the Washington legislature's enabling act; the second ballot; and "the most costly pollution control effort in the nation at that time". Its moral is the one the slide quotes in the reading list: basic research and public administration working together.

**Lake Constance** (the second case in the reading): oligotrophic with $P_{tot}\approx6$ µg L⁻¹ until 1950, 10 µg L⁻¹ by 1957 (the first plankton shifts), rising fast in the early 1970s to **87 µg L⁻¹** (winter overturn) in the early 1980s. Tertiary sewage treatment with phosphorus precipitation was built for the catchment (now about 93 % of its 1.2 million inhabitants are connected), plus low-phosphorus detergents. $P_{tot}$ then fell almost continuously to **8 µg L⁻¹ in 2006**: in the classes of §2 the lake went from oligotrophic to eutrophic and back.

**Lag.** "Even after nutrient loading has been reduced, there is often a lag in the lake's response" (reading, with the Schlachtensee, Berlin, example). Four reasons: (i) it takes **time to exchange the water**; (ii) **phosphorus stored in the sediments** during the polluted years keeps being released, and may even increase as the water concentration falls (a larger diffusion gradient); (iii) at the height of eutrophication algae may have been limited by **nitrogen or light** rather than phosphorus, so phosphorus must fall a long way before it becomes limiting; (iv) **top-down** effects: planktivorous fish that thrived during the eutrophic phase live for years and keep suppressing the grazers.

Slide 13 introduces **Lake Erie** (a video; area 25,800 km²; Lampert and Sommer: eutrophication "has even led to the eutrophication of very large lakes, such as Lake Erie and Lake Ontario") as the more modern case.

## 6. Not so simple: alternative stable states
<span class="scope-taught">taught</span> *[[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=14|slides 14–19]]* · <span class="scope-extra-book">extra · book</span> *Scheffer et al. 2001; Scheffer and van Nes 2007*

Slide 14: "if phosphate seems to be the major problem, then the solution should be simple: **reduce the phosphate level**…" Slide 15: *Not so simple after all…*

### 6.1 The data: Lake Veluwe
Slide 15 shows Fig. 4 of Scheffer et al. (2001): the cover of **charophyte vegetation in the shallow Lake Veluwe** (Netherlands) against total phosphorus. As phosphorus rose, the vegetation collapsed abruptly in the late 1960s and early 1970s (red dots, the forward switch); when the nutrient loading was then gradually reduced, the vegetation returned only in the **1990s**, at a **much lower** phosphorus concentration. Scheffer et al.: "**the restoration of clear water happens at substantially lower nutrient levels than those at which the collapse of the vegetation occurred**": **hysteresis**.

![[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=15&height=330]]
*Slide 15: Lake Veluwe (Fig. 4 of Scheffer et al. 2001).*

### 6.2 Why: a reinforcing loop (slide 16)
Slide 16 shows the shallow-lake network of Scheffer (1998): **turbidity, algae, nutrients, vegetation, waves, resuspended sediment, water depth, fish, zooplankton, allelopathic substances**. Rules given: (1) **multiply the signs** to get the interaction effect of two components along a path; (2) **vegetation and turbidity have negative effects on each other** ([[Causal Loop Diagram]]).

![[EE06 Shallow Lake Feedback Loop.svg|640]]
*Figure EE6.1. The loop reduced to four links. Editable: [[EE06 Shallow Lake Feedback Loop.excalidraw]].*

> [!key] The sign rule applied
> Turbidity lowers the light that reaches the bed ($-$), light drives vegetation ($+$), vegetation reduces sediment resuspension ($-$) and resuspension raises turbidity ($+$): the product $(-)(+)(-)(+)=+$ is a **reinforcing** feedback. The direct pair, vegetation $\to$ turbidity $(-)$ and turbidity $\to$ vegetation $(-)$, also gives $(-)(-)=+$. A loop with a positive sign pushes the system further in whichever direction it is already moving, which is what makes two states self-stabilising. Scheffer et al. list the mechanisms of the vegetation's effect: **reduction of nutrients in the water column**, **protection of grazers (*Daphnia*) against fish**, and **prevention of sediment resuspension**; **fish** maintain the turbid state because without plants they control *Daphnia* and stir the sediment while foraging.

### 6.3 The graphical model (slide 17)
Slide 17 (Fig. 5 of the paper) is a graph of turbidity against nutrient level, built on three assumptions: **(1)** turbidity increases with the nutrient level; **(2)** submerged vegetation reduces turbidity; **(3)** vegetation disappears when a **critical turbidity** is exceeded. Assumptions 1–2 give *two* equilibrium curves, a lower one with vegetation and a higher one without. Assumption 3 chooses which applies: at **low nutrient levels only the vegetated state exists**, at **the highest only the unvegetated state**, and over an **intermediate range two alternative equilibria exist**, separated by a dashed **unstable equilibrium** ([[Alternative Stable States]], [[Shallow Lake Regime Shift]]). Slide 17 labels the jump the "**catastrophic regime shift, 'tipping point'**" and comments: "although this model is very simplistic, making it more realistic does not change the qualitative conclusions".

> [!example] Worked example 1: the minimal model of Box 1, solved
> Scheffer et al. (Box 1) give a minimal model for an unwanted property $x$ (for lakes: nutrients suspended in phytoplankton, causing turbidity):
> $$\frac{dx}{dt}=a-bx+r\,f(x),\qquad f(x)=\frac{x^p}{x^p+h^p},$$
> where $a$ is the environmental driver (nutrient loading), $b$ the removal rate, $r$ the internal recycling and $p$ the steepness of the switch at the threshold $h$. For $r=0$ there is a single equilibrium $x=a/b$. Multiple stable states are possible **only if the steepest slope of the recycling term exceeds the removal rate**, $\max r f'(x)>b$: steeper Hill functions (larger $p$) give stronger hysteresis.
> **Numbers** (illustrative: $b=1,\ r=1.4,\ h=1,\ p=8$; `scripts/ee06_numbers.py`). Equilibria satisfy $a=bx-rf(x)$; the folds are where $da/dx=0$, i.e. $rf'(x)=b$, at $x=0.723$ ($a=0.626$) and $x=1.268$ ($a=0.050$). So for loading $0.05<a<0.63$ there are **three** equilibria (e.g. $a=0.4$: $x=0.40$ stable, $0.95$ unstable, $1.79$ stable) and outside it only one ($a=0.02$: $x=0.02$; $a=0.7$: $x=2.10$).
> **The jumps.** Slowly raise $a$ past 0.626 and the clear state vanishes: $x$ jumps from about 0.72 to about 2.03 (a factor of 2.8). Then lower $a$ again: the system stays turbid until $a$ falls below 0.050, where $x$ drops from 1.27 to 0.04. **To restore the clear state the loading has to be cut from 0.63 to below 0.05, i.e. by about 92 % or more**, and returning to the loading at which the collapse happened ($a=0.63$, or even 0.4) does nothing.

![[fig_ee06_hysteresis.png|860]]
*Figure EE6.2. Box 1 with the parameters above. A: the S-shaped equilibrium curve (solid stable, dashed unstable) and a slow ramp of $a$ up (orange) and down (green); the jumps are at the two folds. B: $dx/dt$ against $x$ for three loadings (one, three and one equilibria).*

> [!intuition] Resilience is the distance to the cliff
> A ball rolls in a valley (slide 18: four pictures: *clear-water lakes*; *phosphorus accumulation in agricultural soil and lake mud*; *flooding, warming, overexploitation of predators*; *turbid-water lakes*). Piling phosphorus into soil and mud does not change the lake's appearance: it only makes the valley of the clear state **shallower**, until a modest shock (a flood, a hot summer, loss of the fish-eating fish) tips the ball over the ridge into the turbid valley. The depth of the valley is the **resilience**. Scheffer et al.'s striking point is that "such catastrophic shifts occur typically quite unannounced": there is little change in the state before the fall, and "early-warning signals… are difficult to obtain".

> [!connection] The same mathematics as the ice-albedo catastrophe
> The S-curve of Fig. EE6.2A is the fold of [[Bistability and Tipping Points]]: the same shape as the energy-balance model of [[CL04 Feedback and Multiple Steady States]], with nutrient loading in place of the solar constant and clear/turbid in place of ice-free/snowball. Near a fold the restoring slope $\to0$, so the [[Relaxation Time]] diverges (critical slowing down): the one early-warning signal that theory predicts.

Slide 18 adds: "these notions have solid mathematical models backing them up; they belong to the general area of **catastrophe theory** which studies questions like why the Sahara became a desert, why coral reefs collapse, how poverty can be alleviated, how stock-market indices rise and fall; there is lots of research on how to predict such regime shifts."

> [!extra-book]+ 🟡 Extra (book): what the two papers add
> **Scheffer et al. (2001)**, "Catastrophic shifts in ecosystems": ecosystems under gradual change can switch abruptly to a contrasting state; "a loss of resilience usually paves the way for a switch", so management should aim to **maintain resilience**. Their Fig. 1: a **smooth** response (a), an **inert-then-sharp** response (b), a **folded** response (c) that produces hysteresis; shallow lakes show the pronounced hysteresis of (c), deeper lakes react smoothly (b). Other systems covered: coral reefs, oceans, forests, arid lands. They report that a temporary strong reduction of fish biomass as "shock therapy" can bring such lakes back into a permanent clear state "if the nutrient level is not too high".
> **Scheffer and van Nes (2007)**, "Shallow lakes theory revisited": the critical nutrient level for turbidity is **higher for smaller lakes** and seems likely to be affected by climate; the two-state picture is elaborated: different groups of primary producers (**charophytes, submerged angiosperms, free-floating plants, green algae, cyanobacteria**) may dominate and **each may be an alternative stable state**, so that eutrophication is a continuum of species replacements interrupted at critical points by dramatic shifts.

## 7. Reversing the trophic state: biomanipulation and restoration methods
<span class="scope-taught">taught</span> *[[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=19|slides 19–24]]* · *Søndergaard et al. 2012*

### 7.1 Biomanipulation (slides 19–20)
If the clear and turbid states are both stable, you can try to *push* a lake across the threshold instead of waiting for the loading to fall below the lower fold. Slide 19: "back to shallow lakes… how to reverse the trophic state of lakes? **Reduce the number of fishes!**" ([[Biomanipulation]]). Slide 20: **18 lakes of different shapes and sizes in the Netherlands**, studied over ten years after biomanipulation (Meijer et al. 1999): **transparency increased** after biomanipulation.

> [!intuition] Release the grazers
> Fish that eat zooplankton (and bottom-feeding fish that stir the sediment) keep *Daphnia* scarce; with fewer such fish, *Daphnia* graze the phytoplankton down, the water clears, plants recolonise, and the plants then help keep it clear (the reinforcing loop of §6.2). That is why a *temporary* fish removal can have a *permanent* effect: it moves the lake into the other basin of attraction, **if the nutrient level is not too high** (Scheffer et al.). It is the same as the Lake Washington jump when *Daphnia* returned.

### 7.2 How bad is it? (slide 21)
"According to a 2018 review on phosphorus pollution: globally, due to human activities, about **1.5 teragrams** of phosphorus (1 Tg = $10^{9}$ kg) were dumped into freshwater systems **in a year**. China contributed the most with **30 %**, followed by **India (8 %)**, the **USA (7 %)** and **Spain and Brazil (6 % each)**" (Mekonnen and Hoekstra 2018). In kilograms: China $0.30\times1.5=0.45$ Tg, India 0.12 Tg, the USA 0.11 Tg. "In many areas of the world either there's not enough water to assimilate the phosphorus or the pollution load is so huge that the water system can't assimilate everything."

### 7.3 Restoration methods (slides 22–24; Søndergaard et al. 2012, pp. 455–458)
Three tables, each with the principle and the "possible problems":

| method | principle | possible problem (slide) |
|---|---|---|
| **Physical** | | |
| sediment dredging | remove P-rich sediment to cut internal loading | relatively expensive; disposal sites needed |
| dilution / flushing | flush with nutrient-poor water to lower P | needs large amounts of nutrient-poor water |
| water-level manipulation | higher level reduces resuspension in shallow lakes; lower level favours submerged macrophytes | not always easy, or permitted |
| hypolimnetic withdrawal | outflow redirected through a pipe from the hypolimnion, where P accumulates in summer | the nutrient-rich, perhaps anoxic water harms downstream bodies |
| **Chemical** | | |
| hypolimnetic oxygenation | add oxygen or air to the hypolimnion of deep lakes to raise redox and P sorption | long-term treatment (> 10 years) often needed; permanent effects hard to obtain |
| phosphorus inactivation | Al, Fe or Ca salts bind P in the water or sediment | aluminium is toxic at low and high pH: hard in soft-water or high-pH lakes |
| **Biological** | | |
| remove zooplankton-eating fish | more large zooplankton, more grazing on phytoplankton | permanent effects may be hard to obtain |
| stock predatory fish | fish-eaters reduce planktivores | correct timing is crucial |
| introduce mussels | filter the water (often zebra mussel *Dreissena polymorpha*) | the zebra mussel is invasive and can reach very high densities with negative consequences |

> [!example] Worked example 2: choosing a method
> A shallow lake (mean depth 2 m, never stratified) has high phosphorus in the mud after decades of sewage, although the sewage has now been diverted. *Which methods address the cause?* The external load is already cut; the problem is **internal loading** from sediment P, so **sediment dredging** or **phosphorus inactivation** act on the stock. Hypolimnetic oxygenation and withdrawal are *not* options (no hypolimnion). Because the lake is shallow and probably in the turbid state, **biomanipulation** can switch it to the clear, vegetated state, and a lower water level can favour the plants. A combination is the usual answer: reduce the nutrient stock *and* push the state.

> [!connection] Invasion and restoration
> The mussel option shows the trade-off of using one species against another: *Dreissena* filters the water but is itself an invader (the problem of [[EE04 Competition and Invasions]]).

## 8. Summary and references
<span class="scope-taught">taught</span> *[[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=25|slides 25–27]]*

Slide 25 ("Summary"): fresh water is one of the most important resources on Earth; there are several threats to it, including **bad policies (for example the Aral Sea)** and **eutrophication**; eutrophication is a **complex process**, affected by multiple components of a lake with complex interactions; tackling it requires input from **scientists, politicians and, above all, the local people**.

| item | tier |
|---|---|
| lecture slides | syllabus |
| Lampert and Sommer §8.5.4–8.6.2, pp. 251–259; Søndergaard et al. (2012), pp. 455–458 | **mandatory**, syllabus |
| Farley (2012), *Eutrophication in Freshwaters*, pp. 258–271 | detailed reading (not examinable) |
| Scheffer and van Nes (2007); "Rescue of Lake Stinko"; Scheffer et al. (2001) (check Box 1) | papers (no exam weight) |
| Ashwin et al. (2012) (maths); Scheffer (2009), *Critical Transitions in Nature and Society* (maths-free) | "references not given" |

## Map of this chapter
> [!connection] How EE06 connects
> **Builds on:** [[EE05 Predation]] (food-web control of algae by zooplankton and fish: a trophic cascade) and [[EE03 Population Dynamics and Chaos]] (fixed points and stability; here with a fold).
> **Leads to:** [[EE07 Conservation Biology]] (positive feedbacks at low density, the Allee effect, are another route to two states and thresholds).
> **Concepts:** [[Trophic State of Lakes]] · [[Cultural Eutrophication]] · [[Thermal Stratification of Lakes]] · [[Internal Phosphorus Loading]] · [[Lake Washington Recovery]] · [[Alternative Stable States]] · [[Shallow Lake Regime Shift]] · [[Causal Loop Diagram]] · [[Biomanipulation]] · [[Lake Restoration Methods]] · [[Nutrient Limitation]]
> **Other subjects:** [[Bistability and Tipping Points]] · [[CL04 Feedback and Multiple Steady States]] · [[Ice-Albedo Feedback]] · [[Relaxation Time]] · [[Inorganic Chemistry - Course Map]] (phosphate, redox, iron and aluminium chemistry) · [[Proofs, Analysis and Topology - Course Map]] (fold bifurcations)

> [!connection] Climate and lakes, one template
> Ice-albedo: **ice** raises albedo, so a cold planet gets colder (reinforcing); shallow lakes: **vegetation** clears the water, so a clear lake stays clear (reinforcing). Both have two stable states, a fold, and hysteresis; both lose resilience *without* visibly changing, and both teach the same management lesson: watch the **margin** to the tipping point, not only the current state.

## Summary
> [!summary] Cheat-sheet
> - **Classical types**: oligo-, eu-, dystrophic (then lake "extinction"). **Modern**: a continuum by $P_{tot}$ at spring circulation (< 5, 5–10, 10–30, 30–100, > 100 µg L⁻¹). A single criterion can mislead (Schöhsee, Lake Constance: morphometry).
> - **Four factors**: basin shape, drainage basin, climate, human activity. Large, deep, slowly flushed lakes are less productive ($P_L=1.55[P_{in}/(1+\sqrt{\tau_w})]^{0.82}$).
> - **Eutrophication chain**: P enrichment → blooms (*Anabaena*, *Microcystis*), less light → hypolimnetic anoxia → **internal P loading** (self-acceleration) → higher pH → fish-kill. Sewage N:P ≈ 4:1.
> - **Lake Washington**: diversion complete 1968 → transparency 3–4 m → ***Daphnia* return 1976 → 10 m**. Recovery lags: water renewal, sediment P, N/light limitation, planktivorous fish.
> - **Alternative stable states**: Lake Veluwe; collapse of vegetation in the late 1960s–70s, recovery only in the 1990s at far lower P. Loop (−)(+)(−)(+) = + (vegetation ⇄ turbidity). **Box 1**: $\dot x=a-bx+rf(x)$; bistable iff $\max rf'>b$; jumps at two folds; restoring needs a much larger cut in $a$ (92 % in the example).
> - **Biomanipulation**: reduce planktivorous fish → *Daphnia* → clear water (18 Dutch lakes).
> - **Restoration**: physical (dredging, flushing, water level, withdrawal), chemical (oxygenation, P inactivation), biological (fish removal, stocking predators, mussels): each with a stated drawback.
> - **Global P**: about 1.5 Tg a year into fresh water (China 30 %, India 8 %, USA 7 %, Spain 6 %, Brazil 6 %).

## Practice
1. **Classify.** A lake has $P_{tot}=7$, another 25, another 60, another 140 µg L⁻¹ at spring circulation. Give the class of each. Why might the 25 µg L⁻¹ lake still be called eutrophic by an older limnologist?
2. **Retention time.** A reservoir receives water with $P_{in}=80$ µg L⁻¹ and has $\tau_w=2$ yr. Estimate $P_L$ from the Vollenweider relation and its class. What happens to $P_L$ if the retention time is cut to 0.25 yr (a heavily flushed lake)?
3. **Chain.** Put in order and explain the links: *anoxic hypolimnion; phosphorus enrichment; fish kill; internal P release; cyanobacterial bloom; reduced light*. Which link makes eutrophication "self-accelerating"?
4. **Lag.** A sewage diversion is completed but phosphorus in the lake takes five years to fall and algae take longer. Give four reasons for the lag (from the reading).
5. **Lake Washington.** Why is the 1976 jump in transparency (to 10 m) not explained by phosphorus alone? Name the two mechanisms given.
6. **Signs.** In the loop *turbidity → light (−) → vegetation (+) → resuspension (−) → turbidity (+)*, compute the loop sign. What would a *negative* loop imply for the lake?
7. **Box 1.** With $b=1,\ r=1.4,\ h=1,\ p=8$ the bistable window is $0.050<a<0.626$. A turbid lake is at $a=0.4$. (a) How many equilibria exist? (b) Will lowering $a$ from 0.63 to 0.4 clear the lake? (c) By what percentage must the loading fall from the collapse value to guarantee recovery?
8. **Biomanipulation.** Explain how removing fish can clear a lake for years, and say when it will *not* work.
9. **Methods.** For each lake choose a method and give its drawback: (i) a deep stratified lake with an anoxic hypolimnion; (ii) a shallow lake with a large stock of phosphorus in the mud; (iii) a lake with a large phosphorus-poor river nearby.
10. **Exam-style.** "Reducing phosphate alone is often not enough to restore a lake." Explain with the shallow-lake model, one data set and one remedy.

> [!example]- Solutions
> 1. 7: oligotrophic (5–10); 25: mesotrophic (10–30); 60: eutrophic (30–100); 140: hypereutrophic (> 100). The 25 lake (Schöhsee-like) may have an anoxic hypolimnion (clinograde oxygen profile), which in the traditional scheme makes it *eutrophic*: trophic state is a biological phenomenon, not a single concentration.
> 2. $\sqrt2=1.414$; $P_{in}/(1+\sqrt2)=80/2.414=33.1$; $33.1^{0.82}=e^{0.82\ln33.1}=e^{2.867}=17.6$; $P_L=1.55\times17.6=27$ µg L⁻¹ (mesotrophic). With $\tau_w=0.25$ yr: $\sqrt{0.25}=0.5$, $80/1.5=53.3$, $53.3^{0.82}=26.1$, $P_L=40.5$ (eutrophic): less time for sedimentation, so a higher concentration.
> 3. P enrichment → algal/cyanobacterial bloom → reduced light (and, when the algae die and sink, more oxygen demand) → anoxic hypolimnion → internal P release (and fish kill as a consequence). **Internal P release** feeds back to enrichment: it makes the process self-accelerating.
> 4. (i) the water must be exchanged; (ii) phosphorus stored in the sediment continues to be released (even faster as the water concentration falls); (iii) at peak eutrophication algae were limited by nitrogen or light, so P must fall further before it limits; (iv) long-lived planktivorous fish from the eutrophic phase keep suppressing zooplankton.
> 5. Phosphorus fell to a new low by 1970 and transparency rose to 3–4 m, but when large *Daphnia* returned in 1976 transparency doubled to up to 10 m. They returned because filamentous cyanobacteria (which clog their filters) disappeared (bottom-up) and mysid shrimp predation fell (top-down): food-web structure, not P, caused the second step.
> 6. $(-)(+)(-)(+)=+$: reinforcing (positive feedback). A negative loop would be balancing: it would push the lake back towards one state and no alternative stable state could exist.
> 7. (a) Three (0.40 stable clear, 0.95 unstable, 1.79 stable turbid). (b) No: at $a=0.4$ the turbid state is still stable; the lake stays turbid (hysteresis). (c) It must fall below 0.050: a cut of $1-0.050/0.626=92\,\%$ or slightly more (to restore without any other intervention).
> 8. Fewer planktivorous fish allow *Daphnia* to graze the phytoplankton down; the clear water lets plants return, and the plants reinforce clarity and shelter *Daphnia*, so the lake stays in the clear basin. It will fail if the nutrient level is too high (the clear state does not exist), or if fish return and the turbid state remains stable.
> 9. (i) hypolimnetic oxygenation (expensive; > 10 years of treatment, permanence uncertain) or withdrawal (the nutrient-rich anoxic water harms downstream bodies); (ii) sediment dredging (costly; disposal sites) or P inactivation with aluminium (toxic at low and high pH); (iii) dilution/flushing (needs the large amount of nutrient-poor water, which this lake has).
> 10. Loading cut alone leaves a turbid lake because the system has **hysteresis**: vegetation and turbidity reinforce one another, so at the same nutrient level there are two stable states and the clear state returns only at much lower P (Lake Veluwe: collapse late 1960s–70s; recovery 1990s). Remedy: **biomanipulation** (reduce planktivorous fish) or dredging/P-inactivation to push the lake across the threshold, *together with* nutrient reduction.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | the two concepts | [[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=1\|sl. 1]] | taught |
> | classical and modern lake types | [[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=2\|sl. 2–3]]; Lampert and Sommer §8.5.4 | taught |
> | factors; mechanism; fish-kill | [[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=4\|sl. 4–9]]; Lampert and Sommer §8.6.1 | taught |
> | Lake Washington; Lake Erie | [[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=10\|sl. 10–13]]; Lampert and Sommer §8.6.2 | taught |
> | alternative stable states; shallow-lake loop; catastrophe theory | [[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=14\|sl. 14–18]] | taught |
> | biomanipulation; global P; restoration methods | [[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=19\|sl. 19–24]]; Søndergaard et al. 2012 | taught |
> | summary and references | [[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=25\|sl. 25–27]] | taught |
> | Lake Veluwe data; Box 1; Figs. 1, 4, 5 | Scheffer et al. 2001 (paper) | extra/book |
> | critical nutrient level and lake size; alternative producer regimes | Scheffer and van Nes 2007 (abstract only) | extra/book |
> | timeline of the Lake Washington story | "Rescue of Lake Stinko" | extra/book |
> | Vollenweider examples; Box 1 solved; the 92 % rule; signs | computed here (`scripts/ee06_numbers.py`, `fig_ee06_hysteresis.py`, `diagrams_ee06.py`) | extra/beyond |
>
> **Read and not read.** Lampert and Sommer pp. 251–259 and Scheffer et al. 2001 (framework, shallow-lake paragraph, Figs. 4–5 and Box 1) were read from the text layer; "Rescue of Lake Stinko" in full. Søndergaard et al. (2012) has an unusable text layer and was **not OCR'd**: its three tables are reproduced on slides 22–24, which is what §7.3 follows. Scheffer and van Nes (2007) was read at the abstract level only; Farley (2012) (a scan, detailed reading) was not read. The Lake Erie video was not watched.
>
> **Slide notes.** Slide 11's "Oligotrophy → Lake Stinko" is a slip for eutrophy (see §5). The Scheffer 2001 Fig. 5 on slide 17 is a graphical model, not a time series; Fig. 4 on slide 15 is the Lake Veluwe data (axis: total P, mg L⁻¹; I describe it qualitatively because the exact phosphorus values at the switches were not read off).

**References.** Lampert, W. & Sommer, U. (2007) *Limnoecology*, 2nd ed., §8.5.4–8.6.2, pp. 251–259 · Søndergaard, M. et al. (2012) "Lake restoration" in *Encyclopedia of Lakes and Reservoirs*, pp. 455–458 · Scheffer, M., Carpenter, S., Foley, J. A., Folke, C. & Walker, B. (2001) *Nature* 413, 591–596 · Scheffer, M. & van Nes, E. H. (2007) *Hydrobiologia* 584, 455–466 · Scheffer, M. (1998) *Ecology of Shallow Lakes* · Edmondson, W. T. (1970) *Science* 169, 690 · Meijer, M.-L. et al. (1999) *Hydrobiologia* 408/409 · Vollenweider, R. A. & Kerekes, J. (1982) OECD · Mekonnen, M. M. & Hoekstra, A. Y. (2018) *Water Resources Research* 54, 345–358 · Farley, M. (2012) in *Encyclopedia of Lakes and Reservoirs*, pp. 258–271 · Ashwin, P. et al. (2012) *Phil. Trans. R. Soc. A* 370, 1166–1184 · Scheffer, M. (2009) *Critical Transitions in Nature and Society*.
