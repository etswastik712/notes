---
title: LS13 Landslides
aliases: [LS13, Landslides]
subject: landscapes
type: chapter
chapter: 13
part: VII
scope: [taught, extra-book, extra-beyond]
by: [slides, ai-notes, book]
status: draft
tags: [subject/landscapes, type/chapter, taught, extra/book, extra/beyond, src/slides, src/ai-notes, src/book, status/draft]
---
# LS13 · Landslides

◀ [[LS12 Hillslope Transport and the Diffusion Equation]] · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: [[LS14 Glaciers Mass Balance and Ice Flow]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught**: slides 123–137 of [[pre_ms_landscape_26.pdf|the EC2123 pre-midsem deck]] (Argha Banerjee, IISER Pune; 153 slides). Boxes marked 🟢 **In the slides** derive what the slides derive; boxes marked 🖼 **Reading the diagram** explain each slide figure panel by panel and sit directly under the slide image.
> 🔵 **Extra · beyond**: boxes marked 🔵 **Extra** complete derivations the slides only quote (from Anderson and Anderson, *Geomorphology: the Mechanics and Chemistry of Landscapes*, and Turcotte and Schubert, *Geodynamics*); 🛠 **Tool** boxes derive a mathematical tool from 12th-grade material; 🧮 **Worked example** boxes calibrate orders of magnitude.
> This chapter has 4 sections, 3 derivation boxes, 2 redrawn figures and 11 slide images.

> [!key] After this chapter you can
> - derive infinite-slope stability with pore pressure,
> - distinguish loose and dense initiation,
> - describe size distribution and runout,
> - read the case studies (Kedarnath, Kerala, Mars, Moon).

> [!intuition] The one-sentence story
> A slope fails when driving stress exceeds the friction and cohesion resisting it; pore pressure lowers the threshold, and runout and size distributions follow.

```mermaid
flowchart LR
  A["infinite slope: driving vs resisting"] --> B["pore pressure"]
  B --> C["initiation: loose vs dense"]
  C --> D["size distribution, runout"]
  D --> E["case studies"]
```
*Concept map: every box is a section of this chapter.*

*[Slides 123–137]*


## Infinite-slope stability (slides 123–124)

> [!figure]- 🖼 Slides 123–124: open to see the slides this section explains
> ![[pre_123.jpg|300]] ![[pre_124.jpg|300]]

Landslides are fast, intermittent failures of steep slopes (slide 123: two road-cut failures in soil, one with a curved head scarp and a lobe at the base).


![[ls_fig27.png]]
*Figure LS13.1. Slide 124: a block on an incline. Components of the weight along and normal to the slope; the normal force $N=mg\cos\theta$ and friction resist.*


> [!derivation] 🟢 In the slides: Slide 124: threshold slope; failure with pore fluid
> *Block.* On a plane of angle $\theta$ the weight $mg$ resolves into $mg\sin\theta$ along the slope (driving) and $mg\cos\theta$ normal to it, balanced by $N=mg\cos\theta$. The shear stress on the plane is $\tau=mg\sin\theta/A$ and the normal stress $\sigma=N/A$. The material fails when the frictional strength is reached (slide: “material at failure”):
>
>
> $$
> \tau=\sigma\tan\phi \Longrightarrow \tan\theta_c=\tan\phi,\quad\theta_c=\phi
> $$
>
>
> (the *angle of repose*, independent of mass). *Infinite slab* of thickness $h$ (weight per area $\rho gh$): $\tau=\rho gh\sin\theta\cos\theta$ and $\sigma=\rho gh\cos^2\theta$ (weight component normal to the slope, spread over the area $1/\cos\theta$), so again $\tau/\sigma=\tan\theta$. *Pore fluid*: water in the pores at pressure $P_w$ carries part of the normal load; only the *effective stress* $\sigma-P_w$ presses the grains together (Terzaghi's principle), so the frictional strength is $\tau=(\sigma-P_w)\tan\phi$ (the slide's second equation). With cohesion $C$, the *factor of safety* is
>
>
> $$
> \mathrm{FS}=\frac{C+(\rho gh\cos^2\theta-P_w)\tan\phi}{\rho gh\sin\theta\cos\theta},\qquad\text{failure when FS}\le1 . \tag{26}
> $$
>
>
> *Saturated, cohesionless, seepage parallel to the slope, water table at the surface*: $P_w=\rho_wgh\cos^2\theta$, so FS $=(1-\rho_w/\rho)\tan\phi/\tan\theta$ and
>
>
> $$
> \tan\theta_c=\Big(1-\frac{\rho_w}\rho\Big)\tan\phi .
> $$
>
>
> For $\rho=2000$: $\theta_c$ is about half of $\phi$ in tangent: $\phi=35^\circ\to19^\circ$; $\phi=30^\circ\to16^\circ$. *Liquefaction*: if $P_w\to\sigma$ the effective stress and strength vanish ($\tau\to0$): the soil behaves as a fluid, as in the car sunk in the slide (photograph).


![[ls_fig28.png]]
*Figure LS13.2. Slide 124 (A&A Fig. 10.27): failure angle against angle of internal friction. Grey band: typical soils ($\phi=20^\circ$–$40^\circ$). The saturated curve uses $\rho_w/\rho=0.5$.*


> [!derivation] 🔵 Extra (not derived in the slides): Newmark sliding block: how earthquakes trigger slides
> A block on a slope with $\theta<\phi$ is stable. Let the ground accelerate down-slope with $a_s$; in the frame of the block a pseudo-force $ma_s$ acts up-slope or down-slope depending on sign; the block slips when the net down-slope force exceeds friction: $m(g\sin\theta+a_s)>mg\cos\theta\tan\phi$, i.e. $a_s>a_c=g(\cos\theta\tan\phi-\sin\theta)=g\cos\theta(\tan\phi-\tan\theta)$. The *critical acceleration* $a_c$ vanishes as $\theta\to\phi$. Example: $\phi=35^\circ$, $\theta=30^\circ$: $a_c=9.8\times0.866\times(0.700-0.577)=1.0$ m s$^{-2}=0.11g$. Strong shaking ($0.2$–$0.5g$) routinely exceeds this on steep slopes; the block moves during the intervals of $a_s>a_c$ (Newmark displacement $=\iint(a_s-a_c) \mathrm{d} t^2$). This is why the 2015 Gorkha earthquake triggered $\sim25 000$ landslides (§13.4).


<!-- ls-depth:LS13:1 -->
> [!derivation] 🔵 Extra (computed): three numbers every slope should be checked against
> **(1) Water halves the stable angle.** For a cohesionless slope with the water table at the surface and seepage parallel to the slope, the factor of safety is $\mathrm{FS}=(1-\rho_w/\rho)\tan\phi/\tan\theta$ (derived above), so the critical angle is $\tan\theta_c=(1-\rho_w/\rho)\tan\phi$. For a saturated density $\rho=2000$ kg/m³ the factor is $\tfrac12$: $\phi=20^\circ\to\theta_c=10.3^\circ$; $\mathbf{30^\circ\to16.1^\circ}$; $35^\circ\to19.3^\circ$; $40^\circ\to22.8^\circ$ (dry: $\theta_c=\phi$). *A slope that is perfectly stable in the dry season at $30^\circ$ is **unstable** once saturated above $16^\circ$.* This is the quantitative reason landslides cluster in the monsoon.
> **(2) Cohesion sets a maximum soil depth.** With cohesion $c$ the slope $\theta>\phi$ is stable only to a depth $z_c=\dfrac{c}{\rho g\cos^2\theta\,(\tan\theta-\tan\phi)}$ (set FS $=1$ in $\mathrm{FS}=\dfrac{c+\rho gz\cos^2\theta\tan\phi}{\rho gz\sin\theta\cos\theta}$). For $\rho=1800$, $\phi=30^\circ$: with $c=5$ kPa, $\theta=35^\circ$: **$z_c=3.4$ m**; $\theta=40^\circ$: $1.8$ m; $\theta=45^\circ$: $1.3$ m; for $c=2$ kPa: $1.4$, $0.7$, $0.5$ m. So **steep soil-mantled slopes can carry only a thin regolith**, and the typical landslide is 1–3 m deep, a scale set by the competition of cohesion and weight, not by the slope length.
> **(3) Size distribution.** Inventories give a power-law *density* of landslide area, $p(A)\propto A^{-2.4}$ (exponent recalled from Malamud et al. 2004, `[verify]`; the cumulative exponent is $\beta=1.4$). By the event-size argument of [[LS01 Landscapes as Physical Systems]], a quantity $\propto A^q$ has a total $\int A^{q}A^{-2.4}\,\mathrm dA\propto A^{q-1.4}$: the **total area** ($q=1$) is dominated by the *many small* slides (contribution falls as $A^{-0.4}$); the **volume** ($V\propto A^{1.5}$, so $q=1.5$) has exponent $+0.1$, i.e. it is *marginally* dominated by the largest events (a factor $\sim2.5$ across four decades of $A$): *neither the smallest nor the largest slides alone control erosion; the whole range matters.*

> [!question] Check yourself (answers below)
> 1. A slope of $25^\circ$ with $\phi=35^\circ$ is stable when dry. What happens when saturated ($\rho=2000$)?
> 2. If cohesion doubles, how does the critical depth change?
> 3. Why do many landslides on the Deccan basalt (Irshalwadi, [[LS18 Deccan Traps Terrain]]) fail along the contact between soil and weathered rock?
> 4. What does the power-law exponent say about the contribution of small versus large landslides to total area?
> *Answers.* (1) $\theta_c=19.3^\circ<25^\circ$: it fails. (2) $z_c\propto c$: doubles. (3) A contrast in permeability and strength at a weathered horizon (bole, [[interflow-horizons]]) lets water pool and pore pressure build exactly at the potential failure plane. (4) With exponent $2.4$ (density), small slides dominate the total area; large ones matter most for the sediment volume only marginally.

> [!connection] Where else this appears
> - **Mohr–Coulomb and pore pressure:** [[LS02 Mechanics and Mathematics Toolkit]] (derivation), [[LS06 Maximum Topography]] (frictional limit), [[LS09 Faults and Earthquakes]] (earthquake triggering).
> - **Power laws and event-size arguments:** [[Pareto Distribution|Pareto]], [[Probability - Course Map]]; [[LS01 Landscapes as Physical Systems]].
> - **Deccan terrain** as a landslide setting (weak boles, steep escarpment, monsoon): [[LS18 Deccan Traps Terrain]], [[interflow-horizons]], [[trap-topography]].


## Initiation: loose versus dense soil (slide 126, left)


![[pre_126.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 126: Iverson et al. (2000), USGS debris-flow flume (Oregon)
> Photograph: the $95$-m-long inclined concrete flume with a loaded soil bed and an inlet at the head-gate. Plots (A&A Fig. 10.30) of displacement (top) and pore-pressure head (bottom, at $30$, $50$, $67$ cm depth) against time after water is applied. (a) *Loose* soil (porosity $0.52$): nothing happens for $48$ minutes, then failure is sudden: a displacement of $\sim2$ m in *3 seconds*, with pore pressure rising during the failure. (b) *Dense* soil (porosity $0.41$, only $\sim10 %$ denser by weight): the same displacement takes $\sim15$ minutes, in many small steps, each associated with a drop in pore pressure (vertical lines link events). Explanation: loose granular material *contracts* when sheared, squeezing the pore water and raising $P_w$; by (26) the strength falls, shear continues and $P_w$ rises further: a runaway feedback (liquefaction). Dense material *dilates*, opening pores, which *lowers* $P_w$ and strengthens it: the failure is stabilised and self-limiting. A 10 % change in density therefore changes the failure mode from catastrophic to gradual.


## Size distribution and runout (slides 126, 136)


![[pre_126.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 126 (right) and slide 136
> Slide 126: (left) a sand-pile analogue in a plexiglass slot ($38\times51$ cm): grains added, a slider moved downward, avalanches weighed; (a,b) profile shapes after successive events (scarps and steep toes); (c,d) avalanche mass ($\mathrm{g}$) per event against boundary drop ($\mathrm{cm}$): sizes vary widely; (right) A&A Fig. 10.37: probability distribution of landslide areas $A$ in New Zealand's Southern Alps: a straight line on log–log above the dashed line ($A\sim10^{-2}$ km$^2$) — a power law; below it the curve rolls over because small slides are not detected or mapped. Slide 136: the 2015 Gorkha inventory: (A) probability density $p(A)$ (m$^{-2}$) against area $A$ (m$^2$): $\log_{10}p=(-2.47\pm0.11)\log_{10}A+(4.68\pm0.54)$ (this study) and $(-2.49\pm0.13)\log_{10}A+(5.54\pm0.69)$ (Martha et al. 2016); (B) histograms of slope: landslide slopes $39.5^\circ\pm9.1^\circ$ (blue) versus general hillslopes $27.5^\circ\pm13.7^\circ$ (red): slides occur on steeper-than-average slopes; (C) runout length (m) against volume ($\mathrm{km^3}$, $10^{-6}$–$10^{1}$): large landslides (red, Legros 2002), debris flows (open circles) and Gorkha slides (small black); runout increases with volume roughly as $V^{1/3}$, and the largest events travel unusually far.


> [!derivation] 🔵 Extra (not derived in the slides): Consequences of a power-law size distribution; Heim's ratio
> If $p(A)\propto A^{-\beta}$ with $\beta\approx2.5$ and volume scales as $V\propto A^{\gamma}$ with $\gamma\approx1.5$ (thin slab: volume $\sim A\times$ thickness with thickness $\propto A^{1/2}$), then $p(V) \mathrm{d} V=p(A) \mathrm{d} A$ gives $p(V)\propto V^{-\beta_V}$ with $\beta_V=1+(\beta-1)/\gamma=1+1.5/1.5=2$. The mass carried by events of volume in $[V,V+\mathrm{d} V]$ is $V p(V) \mathrm{d} V\propto V^{1-\beta_V}\mathrm{d} V=V^{-1}\mathrm{d} V$: every logarithmic bin of volume contributes equally: the rare huge slides move as much total mass as the many small ones. (If $\beta_V<2$ the biggest events would dominate; if $\beta_V>2$ the small ones.)
> *Runout.* A frictional block sliding a horizontal distance $L$ after falling a height $H$ dissipates $mgH=f mgL$, so $H/L=f$ (Heim's ratio: the apparent friction $f_\mathrm{eff}=H/L$). The tangent of the angle from the crest to the toe of the deposit is thus an effective friction coefficient; for very large, long-runout landslides it is $\sim0.1$–$0.2$, far below laboratory values $0.6$: fluidisation, lubrication (pore pressure), trapped air or rock-avalanche granular flow reduce the friction with volume (slide 136(C)). Same argument, again, as $\Delta h/R\sim f$ of Chapter 6.


## Case studies (slides 4, 127–137)

> [!figure]- 🖼 Slides 4–127: open to see the slides this section explains
> ![[pre_004.jpg|300]] ![[pre_005.jpg|300]] ![[pre_006.jpg|300]] ![[pre_007.jpg|300]] ![[pre_008.jpg|300]] ![[pre_009.jpg|300]] ![[pre_010.jpg|300]] ![[pre_011.jpg|300]]


| Event (slide) | Type / place | What the slide shows |  |
|---|---|---|---|
| Irshalwadi (4, 127) | rock–soil debris slide, Raigad (Western Ghats) | Photo (slide 4). Slide 127: news headline: of the $228$ inhabitants of $43$ families, $144$ (including $23$ children) survived; the bodies of $57$ of those killed are still buried |  |
| Taliye, Mahad (127) | debris flow, Raigad | Headline dated 24 Jul 2021: $49$ dead, $47$ missing |  |
| Malin, Pune (127) | mudslide | 31 Jul 2014: “probably killed over 100 people” |  |
| Landslide Atlas of India (127) | inventory 1998–2022 (NRSC) | Yellow polygons cluster in three provinces: NW Himalaya, NE Himalaya, Western Ghats |  |
| Google-Earth views (128, 129) | hillslope scars and deposit fans | Head scarps and downslope debris tongues on forested Deccan slopes |  |
| Dharali, Uttarakhand (130) | debris flow / flash flood, 5 Aug 2025 | Pre- and post-event PlanetLabs and Sentinel-2 images: debris-flow source zone (red dashed), inundation, debris fan over the settlement; NRSC images of 13 Jun 2024 and 7 Aug 2025 show the river valley filled with sediment |  |
| Chamoli flood (131–132) | rock–ice avalanche, 7 Feb 2021, Ronti Gad/Tapovan | Frames A–J (Shugar et al., *Science*) with timestamps $t_1\sim10{:}30$ IST ($+14$ s), $t_2\sim10{:}38$ ($+34$ s), $t_3\sim10{:}39$ ($+57$ s), $t_4\sim10{:}41$ ($+8$, $+15$, $+26$ s): dust cloud, debris flow, then damage at the hydropower dam. Slide 132: 3-D view of Ronti Peak, before/after satellite images (1 Jan, 5 Feb, 10 Feb 2021), sketch of the detached block (glacier ice over rock; the slide marks $\sim5\times10^6$ m$^3$) and DEM-difference profiles (2015 vs 2021) across the scar |  |
| Massive slides (133–134) | A\ | A Figs. 10.34, 10.36; Sabche cirque (Annapurna) | Slide 133: a very large debris flow scar (scale 4 km) and a huge rock avalanche deposit beside glaciers. Slide 134: the Sabche rock-avalanche, $\sim$AD 1200, volume $\sim2\times10^{10}$ m$^3$ ($\sim4000\times$ Chamoli), with dating sites ($^{36}$Cl exposure, IRSL, $^{14}$C), the Pokhara conglomerate in the Seti valley, head scarp, breccia facies; the slide comments it “might have reduced the number of 8000-ers by one” |
| Gorkha 2015 (135–137) | earthquake-triggered, $\sim25 000$ slides | Inventory map (Kathmandu, Barpak epicentre, mapped areas); slope and size statistics (slide 136); slide 137: horizontal peak ground velocity (PGV, cm s$^{-1}$) map and the landslide density against distance, with three peaks correlated with PGV, lithology and topography |  |

*Landslide case studies on the slides.*


**Scale comparison.** Volumes span nine orders of magnitude: a road-cut failure $\sim10^2$ m$^3$, Chamoli $\sim10^{6}$–$10^{7}$ m$^3$, Sabche $\sim2\times10^{10}$ m$^3$. By $L\propto V^{1/3}$ a factor $10^{9}$ in volume is $10^3$ in runout.


> [!intuition] Rain, shaking, and human location
> Two triggers: (1) heavy rain raises $P_w$ ((26): strength falls); (2) shaking supplies $a_s>a_c$ (Newmark). The Western Ghats events (Irshalwadi, Taliye, Malin) are rain-triggered failures of weathered basalt regolith on steep slopes ($30^\circ$–$40^\circ$) above the friction angle of saturated soil ($\theta_c\approx16^\circ$–$19^\circ$ for cohesionless soil, so cohesion of roots and rock structure carries the slope until rain erodes it); the Himalayan ones add high relief, glaciers and earthquakes.

## Further slides explained one by one
<span class="scope-taught">taught</span> *the slides of this chapter's range that carry no derivation of their own; each image is followed by what it shows*

![[pre_125.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 125: USGS flume experiment: loose and dense soil
> *Left:* the 95-m-long steep flume at the USGS in Oregon with a debris-flow experiment on 13 Sept 2001. *Right:* (a) loose soil (porosity 0.52): displacement and pore-water pressure head against time: after about 48 minutes of wetting the pressure builds and, within seconds, the slope fails suddenly and catastrophically (displacement jumps); (b) dense soil (porosity 0.41): over four hours the displacement creeps up gradually and the pressure head stays low. Loose soil contracts when sheared, raising pore pressure and liquefying; dense soil dilates and drains. (A&A Fig. 10.30)

![[pre_127.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 127: Landslide Atlas of India
> *Left:* NRSC map of India with the landslide inventory 1998–2022 (yellow): clusters in the NW and NE Himalaya and the Western Ghats. *Right:* three news items: the Taliye (Raigad) landslide of July 2021 (49 dead), the Irshalwadi landslide (2023), and the Malin (Pune) landslide of 2014, a mass-fatality mudslide: why landslides matter in India.

![[pre_128.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 128: Irshalwadi landslide: satellite view
> A satellite image of the hillside above the village after the July 2023 failure: a long, narrow debris track running down a forested basalt slope and spreading into a fan of debris below.

![[pre_129.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 129: Irshalwadi landslide: the source catchment
> A second Google-Earth view of the same hillside (terraced basalt slopes, forest and cleared land) with the village location marked at the left: the slope above is the source of the debris flow.

![[pre_130.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 130: Dharali disaster, Uttarakhand, 5 August 2025
> False-colour Sentinel-2 imagery before and after the event (red = vegetation): pre-event (left) shows the settlement of Dharali beside the stream; post-event shows the debris-flow track, deposit and the inundated settlement. *Right:* two high-resolution images (13 June 2024 and 7 Aug 2025) with Dharali circled. The slide points to the Landslide Blog article for the cause (a flood/debris flow from the tributary catchment).

![[pre_131.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 131: Chamoli flash flood, Feb 2021 (Ronti Gad, Tapovan)
> Ten video frames (A–J) with times in IST (≈10:30 on 7 Feb 2021) from $t_0+14$ s to $t_0+57$ s: a dust and debris cloud rushes down the Ronti Gad valley and across the Tapovan dam: the rock–ice avalanche from the slope above transformed into a flash flood. The slide cites Shugar et al., *Science* 2021 for the detailed reconstruction.

![[pre_132.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 132: Chamoli rock–ice avalanche: source and path
> Figures from Shugar et al. (*Science* 2021): a 3-D view of the Ronti peak slope that failed; satellite images before/after (E, F show the cross-section of the detached rock-and-glacier-ice block); elevation-change profiles along the path (G–J) showing the thickness removed from the source and deposited below. The orange label gives the source volume of order $2.7\times10^7$ m³ (`[verify]` the exponent).

![[pre_133.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 133: Massive debris flows and rock avalanches (A&A Figs 10.34, 10.36)
> Examples of very large mass movements: an oblique aerial photo of a lobate rock-avalanche deposit spreading across a desert valley floor (bottom left), a grey-scale view of another long-runout deposit (top left), and Google-Earth views of glacier-covered terrain with debris sheets (right). They show how the runout of large landslides greatly exceeds the fall height.

![[pre_134.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 134: A giant prehistoric rock avalanche near Pokhara, Nepal
> A map from a *Nature* paper on dated deposits of a huge prehistoric rock avalanche in the Pokhara valley (carbonate-rich Tethyan Himalaya above, High Himalayan gneisses and Lesser Himalayan metasediments below; symbols mark exposure-age, luminescence and radiocarbon samples; the deposits are mapped in yellow and green: breccia, conglomerate, terrace deposits). The orange note dates the event to about 1200 AD and speculates its size might have removed a summit from the list of 8000-m peaks (`[verify]` against the paper).

![[pre_135.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 135: Landslides triggered by the 2015 Gorkha earthquake (Roback et al. 2018)
> Fig. 1 of the study: a satellite image of central Nepal with the mapped area (blue outline), the landslides (yellow) and obscured areas (purple), the epicentres of the 25 April (M7.8) and 12 May (M7.3) shocks, and Kathmandu, Barpak, Bhote Koshi and Langtang marked; (B) the inventory over topography; (C) before/after imagery near Barpak showing coseismic landslide scars.

![[pre_136.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 136: Landslide statistics
> (A) Probability density of landslide area on log–log axes: a power-law tail with a rollover at small areas, fitted by $\log p=-2.47+0.11\log A-\dots$ with a slope near $-2.5$ for large landslides. (B) Slope histograms: landslide source slopes (mean $39.5\pm9.1^\circ$) against all hillslopes ($27.5\pm13.7^\circ$): failures preferentially occur on steeper slopes. (C) Runout length against landslide volume: runout grows with volume and debris flows run farther than ordinary landslides.

![[pre_137.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 137: 25,000 landslides and the ground motion (Gorkha 2015)
> Map of landslide density across central Nepal against average horizontal peak ground velocity (colour scale 0–70 cm/s), with the April 25 epicentre and the 12 May shock, the main thrusts and a shaded fault-plane projection; (c) landslide counts along a profile away from the epicentre show three peaks: failures correlate with shaking intensity and also with topography (Geophys. Res. Lett. 2022).


## Map of this chapter
> [!connection] How LS13 connects
> **Previous:** [[LS12 Hillslope Transport and the Diffusion Equation]] · **Next:** [[LS14 Glaciers Mass Balance and Ice Flow]].
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides 123–137 (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].

<!-- ls-depth:LS13:2 -->
> [!provenance]- Depth-layer sources (added 2026-10-28)
> | Topic | Source | Priority |
> |---|---|---|
> | FS formulas, critical angles and depths | the chapter's own derivation (a/b: AI notes after A&A ch. 10); numbers computed in `scripts/ls_depth_numbers.py` (`LS13`); densities and $c$ values are illustrative | extra · beyond |
> | landslide area exponent 2.4, event-size integral | recalled (Malamud et al. 2004); not checked against a page | not checked (`[verify]`) |

## Continued in the vault (added 2026-10-29)
- Landslide dams and their effect on bedrock-river profiles: [[LS23 Bedrock Channels and River Incision]] §8.
