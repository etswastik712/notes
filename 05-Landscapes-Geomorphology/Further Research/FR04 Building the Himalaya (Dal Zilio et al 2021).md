---
title: FR04 Building the Himalaya (Dal Zilio et al 2021)
aliases: [FR04, Dal Zilio 2021, Himalaya seismic cycle, Main Himalayan Thrust, building the Himalaya, tectonic to earthquake scales]
subject: landscapes
type: chapter
part: Further Research
scope: [extra-book]
by: [papers, slides]
status: draft
prereq: ["[[LS09 Faults and Earthquakes]]", "[[LS10 Folds Flexure and Mountain Building]]"]
tags: [subject/landscapes, type/chapter, extra/book, src/papers, src/slides, status/draft]
---
# FR04 · Building the Himalaya from Tectonic to Earthquake Scales (Dal Zilio et al. 2021)

◀ [[FR03 Flow at a River Bend with CCHE2D (Das and Biswal 2023)]] · [[Further Research - Landscapes Papers]] · [[Landscapes and Geomorphology - Course Map|Course Map]]

<span class="scope-extra-book">extra · paper (a review; not examinable, read for understanding)</span>

> [!summary] The paper in one paragraph
> L. Dal Zilio, G. Hetényi, J. Hubbard and L. Bollinger, **"Building the Himalaya from tectonic to earthquake scales"**, *Nature Reviews Earth & Environment* 2 (April 2021) 251–268 ([[s43017-021-00143-1.pdf]]). A review (18 pages) of how the Himalaya grew by **millions of years** of India–Eurasia convergence *and* how that convergence is released in **earthquakes** every few hundred years. The central message: the two time scales are coupled. The plate-boundary fault, the **Main Himalayan Thrust (MHT)**, developed over millions of years; the **surface morphology** shows that most convergence is accommodated on it; **GPS (tectonic geodesy)** shows that it is locked and loading elastically between earthquakes; **partial ruptures** may mostly occur in the **downdip** part of the MHT, whereas **great ($M_w\ge8$) earthquakes** are complete megathrust ruptures that release accumulated residual strain; and structures built over millions of years (segmentation along the arc) influence **where and how far** earthquakes rupture and thus **how the mountain grows**.

> [!key] After this chapter you can
> - define orogen, megathrust, seismic cycle, interseismic strain, coupling, partial versus great rupture and segmentation,
> - connect the review to the four-time-scale picture of the Himalaya in the lectures ([[LS09 Faults and Earthquakes]], slides 91–94) and to [[LS10 Folds Flexure and Mountain Building]] (critical taper) and [[LS07 Isostasy]],
> - turn the review's statements into simple numbers (recurrence time $=$ slip$/$(coupling $\times$ convergence rate), moment of a great earthquake),
> - use the paper as a *reading list* for a deeper study.

> [!warning] How much of this paper I read
> This chapter is a **guided introduction**, written from the abstract, the introduction, the "Key points" box, the glossary terms in the margins and the reference to figures; I read these carefully but did **not** read the body of the review (sections on structure, geodesy, earthquake-cycle models, segmentation and the figures' details) line by line. Every statement attributed to the paper below is from the parts I read; statements marked "mine" are my own reasoning or computation. Use the chapter to know *what to look for* when reading the review.

## 1. The setting, in the paper's own numbers
> [!example] Facts stated in the introduction
> - The Himalaya stand at **7000–8000 m**, a sharp topographic boundary between the near-sea-level **Ganges and Brahmaputra plains** to the south and the **4500–5000 m Tibetan Plateau** to the north. Underneath lies **one of the largest continental megathrusts on Earth**, and the region has large, damaging earthquakes: **2015 $M_w7.8$ Gorkha, 2005 $M_w7.6$ Kashmir, 1950 $M_w8.5$–8.7 Assam, 1934 $M_w8.4$ Bihar–Nepal, 1905 $M_w7.8$ Kangra, 1897 $M_w8.2$–8.3 Assam–Shillong Plateau.**
> - Large Himalayan earthquakes have **long recurrence intervals (hundreds of years)**; the limited instrumental record leaves "large gaps" in how long-term deformation links to hazard.
> - On geological time scales ($10^4$–$10^7$ yr) deformation is usually described as continuous and quasi-steady (viscous at depth, brittle in the upper crust), but strong ($6<M_w<7$), major ($7<M_w<8$) and great ($M_w8+$) earthquakes show that upper-crustal shortening is **episodic**.
> - The system is **non-linear and coupled across scales**: tectonics $\leftrightarrow$ surface denudation (loss of landscape mass) $\leftrightarrow$ climate, since topography and weathering alter monsoons and long-term climate.
> *Key points of the review (its box):* the Himalaya is a **subaerial orogenic wedge** with rapid shortening and thickening, **intense surface denudation** and **recurrent great earthquakes**; the Gorkha earthquake and aftershocks were monitored by **dense local networks**, giving a unique data set; observations **co-vary along strike** (segmentation).

> [!intuition] Why the Himalaya is the textbook case
> Because it is *above* sea level and densely instrumented, we can watch the same machine at all scales: from the 2015 rupture (seconds) to terraces uplifted in $10^3$–$10^4$ yr (the Sutlej terraces of slides 91–94) to the million-year growth of the range. That is the claim "tectonic to earthquake scales" in the title.

## 2. Terms to know (from the paper's margins and the vault)
> [!key] Glossary
> | Term | Meaning |
> |---|---|
> | **orogen** | a belt of crust involved in mountain building by plate convergence (the paper's margin definition) |
> | **megathrust** | the huge low-angle thrust fault at a plate boundary; here the **MHT**, which also appears as the **Main Frontal Thrust (MFT)** where it reaches the surface in the south |
> | **hanging wall** | the block above an inclined fault |
> | **seismic cycle** | interseismic (loading, years to centuries), coseismic (rupture, seconds), postseismic (relaxation, days to years) phases ([[LS09 Faults and Earthquakes]]) |
> | **coupling** | $0$ for a fault that slips steadily (aseismically) at the plate rate to $1$ for a **fully locked** fault (the paper's definition) |
> | **locked-to-creeping transition** | the down-dip band where the fault changes from locked to sliding; its **width depends on temperature** (hence on depth) and so carries information about the **local dip of the MHT** |
> | **surface denudation** | loss of landscape mass (erosion plus chemical loss): $\mathcal E$ of [[LS01 Landscapes as Physical Systems]] |
> | **blind earthquake** | a rupture that does not reach the surface (so leaves no scarp) |
> | **segmentation** | along-strike changes in structure, coupling, rupture extent that co-vary |

## 3. The scientific story (as far as I read it)
> [!example] Four claims in the abstract, each testable
> 1. **Morphology says most convergence is on the MHT.** The surface features of the range reflect slip on one plate-boundary fault that developed "in the roots of the mountain range over millions of years" (the critical-wedge picture of [[LS10 Folds Flexure and Mountain Building]]).
> 2. **Geodesy says it is loading elastically now.** At decadal scales GPS shows *elastic strain periodically released by earthquakes*. The review notes surface velocities rising from about **3 mm/yr** near the piedmont to **13–17 mm/yr** farther north (read from a garbled two-column extraction: `[verify]`), the signature of a locked MHT.
> 3. **Earthquake-cycle models suggest partial ruptures concentrate downdip, great earthquakes are complete ruptures.** Partial ruptures might mostly occur "in the downdip region of the MHT", whereas great ($M_w8+$) events are "more commonly associated with complete megathrust ruptures, which release accumulated residual strain".
> 4. **Structure inherited over millions of years controls stress accumulation, segmentation, rupture extent and location, and thus mountain growth.**

> [!derivation] 🔵 Extra (mine, `scripts/fr_numbers.py`): turning "recurrence of hundreds of years" into arithmetic
> If the fault accumulates slip at the convergence rate $V$ with coupling $\chi$ (fraction locked), the time to build up the slip $D$ of a great earthquake is $T=D/(\chi V)$:
> | slip $D$ | $V=17$ mm/yr, $\chi=1$ | $V=17$, $\chi=0.8$ | $V=20$, $\chi=1$ | $V=20$, $\chi=0.8$ |
> |---|---|---|---|---|
> | 3 m | 176 yr | 221 yr | 150 yr | 188 yr |
> | 6 m | 353 yr | 441 yr | 300 yr | 375 yr |
> | 10 m | 588 yr | 735 yr | 500 yr | 625 yr |
> This reproduces the paper's "hundreds of years", and also shows why partial coupling ($\chi<1$) lengthens recurrence. **Sizes:** the $M_w7.8$ Gorkha earthquake has $M_0=10^{1.5\times7.8+9.1}=6.3\times10^{20}$ N m; an $M_w8.5$ event releases $7.1\times10^{21}$ N m, **11 times more** (a factor $10^{1.5\times0.7}$), consistent with a *complete* rupture releasing more accumulated strain than a partial one ([[LS09 Faults and Earthquakes]], Gutenberg–Richter depth layer).

## 4. How to read the review (a reading plan)
> [!question] Questions to carry while reading the body of the paper
> 1. Where on the MHT is the **locked-to-creeping transition** under the High Himalaya, and what does it imply about the **dip** of the fault?
> 2. Which observations **co-vary along strike** (topography, seismicity, geodetic coupling, long-term uplift) and where are the proposed segment boundaries?
> 3. What do **earthquake-cycle models** assume about rheology (viscous versus elastic, rate-and-state friction) and how sensitive are their conclusions?
> 4. How is **climate/denudation** coupled to the tectonic loading (the feedback of [[LS10 Folds Flexure and Mountain Building]] slide 95)?
> 5. What evidence distinguishes **partial** from **complete** ruptures in the historical (1905–2015) and paleoseismic records?
> 6. What is *not* known, and what measurements would resolve it?

## 5. Connections
> [!connection] How this review plugs into the vault
> - **The Himalaya over four time scales (lectures):** [[LS09 Faults and Earthquakes]] (slides 91–94: terraces $10^3$–$10^4$ yr, earthquake recurrence, long-term growth); this review is the research-level version of the same story.
> - **Mountain growth and force balance:** critical taper and the sandbox, [[LS10 Folds Flexure and Mountain Building]]; maximum elevation and what limits it, [[LS06 Maximum Topography]], [[LS19 Glacial and Aeolian Landforms]] (Dielforder et al. 2020: subducting-plate shear force controls mountain height).
> - **Mantle and lithosphere rheology that sets the viscous part of the cycle:** [[LS02 Mechanics and Mathematics Toolkit]] (Maxwell time), [[LS07 Isostasy]].
> - **Surface response:** rivers cut gorges and terraces in rising rock ([[LS16 Fluvial Landscapes]]); landslides are triggered by shaking ([[LS13 Landslides]], where the 2015 Gorkha-type triggering is discussed in the Himalayan case studies).
> - **Climate coupling:** monsoon, weathering and the carbon cycle, [[Climate - Course Map]], [[LS11 Weathering and Regolith]]; the Cenozoic cooling hypothesis.
> - **Indian context:** the Himalayan front and the Deccan (a stable plate interior by comparison): [[LS18 Deccan Traps Terrain]].
> - **Mathematics:** the cycle of slow loading and sudden release is a **relaxation oscillation** (stick-slip), described by the same transfer-function/pole language as [[Fourier and Laplace Transforms]] §7; power-law earthquake statistics and extremes are in [[Probability - Course Map]] (Pareto, Gumbel, Poisson).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Priority |
> |---|---|---|
> | abstract, introduction (elevations, earthquake list, time scales), key points, margin glossary terms | [[s43017-021-00143-1.pdf]] (read) | d · paper |
> | coupling definition, locked-to-creeping transition, GPS velocity range | the same paper, read from a garbled two-column text extraction; the figures and body sections were **not** read | d · paper (`[verify]`) |
> | four-time-scale Himalaya, stick-slip, convergence 20 mm/yr | [[LS09 Faults and Earthquakes]] (slides 91–94) | a · slides |
> | recurrence table, moment ratios | my computation (`scripts/fr_numbers.py`) | extra · beyond |
>
> **Flags.** (1) This is a *guide*, not a summary of results; read the review itself for evidence and uncertainties. (2) The 3 and 13–17 mm/yr values should be checked against the printed text/figure. (3) The coupling-and-slip table assumes a uniform slip $D$ and a constant convergence rate.
