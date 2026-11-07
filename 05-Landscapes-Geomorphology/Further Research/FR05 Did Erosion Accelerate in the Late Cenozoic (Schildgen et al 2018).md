---
title: FR05 Did Erosion Accelerate in the Late Cenozoic (Schildgen et al 2018)
aliases: [FR05, Schildgen 2018, Herman 2013, erosion rate debate, spatial correlation bias, time scale bias, late-Cenozoic erosion, thermochronology erosion rates]
subject: landscapes
type: chapter
part: Further Research
scope: [extra-book]
by: [papers, reading-list]
status: draft
prereq: ["[[LSX1 Clocks in Rocks]]", "[[LS14 Glaciers Mass Balance and Ice Flow]]"]
tags: [subject/landscapes, type/chapter, extra/book, src/papers, status/draft]
---
# FR05 · Did Erosion Accelerate in the Late Cenozoic? (Schildgen et al. 2018 against Herman et al. 2013)

◀ [[FR04 Building the Himalaya (Dal Zilio et al 2021)]] · [[Further Research - Landscapes Papers]] · [[Landscapes and Geomorphology - Course Map|Course Map]]

<span class="scope-extra-book">extra · paper (a reading-list debate; not examinable as far as is known)</span>

> [!warning] How much of this I read (added 2026-11-07)
> The instructor's post of 3 Nov ([[landscape-evolution/2026-11-03-erosion-rate-debate-reading|reading-list note]]) names **three** items and attaches **no file**: (1) "a paper by Herman and others on 'recent' variation of erosion rate on a global scale (application of thermochronological data)", (2) the opposing view, Schildgen et al., (3) a *Science Advances* paper on time-scale-dependent estimates of glacial erosion. **Only (2) is characterised here, from its abstract and from press/repository summaries retrieved in this session** (the Nature page is behind a paywall; the full text and the figures were **not read**). (1) is identified from Schildgen's reference list as Herman et al., *Nature* 504 (2013) 423–426 (an **inference** by the other tool, not confirmed by the post); (3) is identified from the DOI as Ganti et al., *Science Advances* 2 (2016) e1600204 (also an inference): neither was read, so **nothing about their content is claimed**. Treat this as a **guide to the argument**, to be upgraded after reading the papers.

> [!key] The question and the three papers
> **Did global erosion rates in mountain belts rise in the late Cenozoic (the last few million years) as the climate cooled and glaciated?** *Herman et al.* (as described by Schildgen's abstract): a global compilation of **thermochronology** data suggested a **nearly two-fold increase**. *Schildgen, van der Beek, Sinclair and Thiede (2018), Nature 559, 89–93:* "Spatial correlation bias in late-Cenozoic erosion histories derived from thermochronology": of the **30 locations** with reported accelerated late-Cenozoic erosion, in **23** the increase is a **spatial correlation bias** (data with disparate exhumation histories combined, so spatial variation in erosion rate is turned into an apparent temporal increase), in **4** it can be explained by **changes in tectonic boundary conditions**, and in **3** a **climatically induced acceleration** is recorded, driven by **localised glacial valley incision**. Conclusion: thermochronology data currently have **insufficient resolution** to assess a global climate effect; a synthesis of **local** findings with location-specific information is suggested. (Background in the abstract: sedimentation-rate records suggested a global increase, but others argue that the sedimentary increases come from preservation biases, hiatuses and varying measurement intervals.) *Ganti et al. (2016)*: about the **dependence of glacial erosion-rate estimates on the averaging interval** (title/DOI only).

## 1. Why a rate depends on the interval and the sample
A thermochronometer gives the **time $t$** since the rock cooled through a **closure temperature** ([[Closure Temperature]], [[Thermochronology]], [[LSX1 Clocks in Rocks]]); with a geothermal gradient this converts to an **exhumation depth $z_c$**, so the mean rate over $[0,t]$ is $\varepsilon=z_c/t$. Two consequences (the lecture-level statements of the abstract: "a measured erosion rate depends on the interval and the sampling over which it is averaged; spatial variation can look like temporal change; thermochronology resolution limits what can be concluded"):
- **Averaging.** A rate is a mean over the interval it spans; short intervals see bursts (glacial valley incision), long intervals smooth them out.
- **Spatial correlation bias** 🔵 (a toy of mine): take two places with **constant** exhumation, $0.2$ mm/yr and $1.0$ mm/yr, and one closure depth $z_c=4$ km (assumed). The slow place records an age $4\ \text{km}/0.2\ \text{mm yr}^{-1}=20$ Ma, the fast place $4$ Ma. Pool the two data sets **by age**: the young age bin ($<5$ Ma) contains only the fast place ($1.0$ mm/yr) and the old bin ($15$–$25$ Ma) only the slow place ($0.2$ mm/yr): the pooled record shows a **five-fold "acceleration" towards the present**, although **neither place ever changed**. This is the mechanism named in the paper's title, in its simplest possible form.

## 2. What it means for the vault
- **Glaciers and erosion:** the three climatically driven cases are tied to **glacial valley incision**, the process of [[LS14 Glaciers Mass Balance and Ice Flow]] and [[LS19 Glacial and Aeolian Landforms]]; the 2025/26 lecture on glacial and aeolian landforms ([[landscape-evolution/2026-10-27-glacial-and-aeolian-slides|slides]], 90 MB, **not read** by the other tool) is the context.
- **Other erosion-rate methods** (different time scales): [[Cosmogenic Erosion Rate]], [[Cosmogenic Nuclides]]; see also the sediment-flux estimates in [[LS24 Sediment Transport Mechanics]].
- **Climate side:** the orbital and glacial cycles of [[CL17 Orbital Forcing and Glacial Cycles]] are the *forcing* whose erosional response is debated here.
- **Statistics:** pooling heterogeneous samples is a Simpson-paradox-type error ([[Probability - Course Map]], [[PR02 Conditional Probability Bayes Rule and Independence]]).

## Practice
1. In the toy of §1, what would a **time-resolved** record of each place (many closure systems with different depths) show, and why does that remove the bias?
2. A glacial valley erodes $2$ km in $0.4$ Myr; the mean rate over $10$ Myr is $0.3$ mm/yr. Find the rate during the glacial episode and the fraction of the 10-Myr total it explains.
3. State in one sentence why Schildgen et al. conclude that "insufficient resolution" is the honest answer.

> [!example]- Solutions
> 1. Each place would show a constant rate through time; pooling is then harmless because the comparison is made *within* each place.
> 2. $2$ km $/0.4$ Myr $=5$ mm/yr ($5$ km/Myr); the 10-Myr total is $0.3\times10=3$ km, so the episode accounts for $2/3$ of it (the rate over the rest is $1$ km $/9.6$ Myr $=0.10$ mm/yr).
> 3. Because the signal they can resolve (differences between interval averages at different places) is of the same size as the bias from combining places.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Priority |
> |---|---|---|
> | the debate, the three items, the dates | [[landscape-evolution/2026-11-03-erosion-rate-debate-reading\|the instructor's post, via the other tool's note]] (no files attached) | taught (reading list) |
> | Schildgen et al. 2018: 30 locations, 23 / 4 / 3, conclusion, background | abstract and summaries retrieved by web search this session: [aminer record](https://aminer.org/pub/5c0f84a9da562944ac8efdea/spatial-correlation-bias-in-late-cenozoic-erosion-histories-derived-from-thermochronology), [GFZ press release](https://www.gfz.de/en/press/news/details/what-does-global-climate-have-to-do-with-erosion-rates) | d · paper (abstract level) |
> | Herman et al. 2013, Ganti et al. 2016 | identified only by the other tool from a reference list and a DOI; **not read** | — |
> | toy model of spatial correlation bias, glacial-episode arithmetic | my computation | extra · beyond |
>
> **Flags.** The press summaries differ in how they tally the 30 locations (27 "erroneous" = 23 + 4 tectonic); the abstract's 23 / 4 / 3 is used. The Nature paper's full text was not accessible.
