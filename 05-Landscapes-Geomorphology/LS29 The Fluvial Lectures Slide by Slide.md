---
title: LS29 The Fluvial Lectures Slide by Slide
aliases: [LS29, fluvial slides, l_fluvial, fluvial lecture walkthrough, D8 routing, channel head, stream order, hydrograph, effective discharge, bedrock river equation]
subject: landscapes
type: chapter
chapter: 29
part: IV
scope: [taught, extra-beyond]
by: [slides, book, own-notes]
status: draft
prereq: ["[[LS03 Digital Elevation Models and Terrain Analysis]]", "[[LS12 Hillslope Transport and the Diffusion Equation]]", "[[LS16 Fluvial Landscapes]]"]
tags: [subject/landscapes, type/chapter, taught, extra/beyond, src/slides, src/book, status/draft]
---
# LS29 · The Fluvial Lectures, Slide by Slide

◀ [[LS28 Deccan Field Guide Lava Architecture and Sahyadri Stratigraphy]] · [[Landscapes and Geomorphology - Course Map|Course Map]] · [[LS99 Landscapes Practice Problems]] ▶

<span class="scope-taught">taught · the 43 fluvial slides</span> <span class="scope-extra-beyond">extra · beyond (derivations, numbers, the "why" behind each slide)</span>

> [!info] What this chapter is, and how it relates to LS16 and LS21–LS23
> The source is the fluvial lecture deck [[l_fluvial.pdf]] (43 slides, figure numbers from A&A = Anderson & Anderson, *Geomorphology*, Ch. 11–13). Every slide is discussed below, in the lecture's order, with the reasoning that the slides leave out.
> - Slides **1–15** (finding rivers in a DEM, where channels begin, networks, how rain becomes streamflow, gauging) were not covered anywhere in the vault before this chapter. They are treated in full here.
> - Slides **16–29** (floods, floodplains, braided and meandering rivers, alluvial profiles, sediment budgets) are explained here and derived in more depth in [[LS22 Floods Planform and River Profiles]] and [[LS21 River Hydraulics and Hydraulic Geometry]].
> - Slides **30–43** (bedrock rivers) are explained here and derived in full in [[LS23 Bedrock Channels and River Incision]], which also solves the slide-43 exam question.
>
> I read the slides as images. Numbers quoted "from the slide" are read off those images; anything I could not read reliably is said to be uncertain. Every number of my own is computed in `scripts/ls29_fluvial_slides_numbers.py`, and the figure is made by `scripts/fig_ls29_fluvial_slides.py`.

> [!intuition] The one-sentence story
> Water falling on a landscape runs downhill and collects. Where enough of it collects to shear the ground hard enough, a channel starts. Channels join into networks whose geometry repeats at every scale. The water arrives in pulses (floods), and the moderate, frequent floods do most of the work, shaping channels that braid or meander when they flow on their own sediment. Where the river flows on rock, its power to cut decides the long profile, and any disturbance (a fall of base level, a pulse of uplift) travels upstream as a knickpoint or waterfall.

![[fig_ls29_fluvial_slides.png]]
*Figure LS29.1.*
- *A: D8 routing on the slide-2 grid. Each arrow is the steepest-descent direction; the blue number is how many cells drain through that cell (the "accumulation").*
- *B: In the overland-flow model of §2, the distance from the divide at which flow first erodes falls steeply with hillslope gradient.*
- *C: Effective discharge: the frequency of a flow falls with its size, the transport it achieves rises, and their product (the work done) peaks at an intermediate flow.*
- *D: The steady profile of a bedrock river is concave up; a drop in base level travels upstream as a step.*

---

## 1. Where are the rivers in a DEM? (slides 1–7)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=1|slides 1–7]]* · see also [[LS03 Digital Elevation Models and Terrain Analysis]], [[LS20 GIS and TopoToolbox Practicals]]

**The question (slide 1).** A DEM is a grid of elevations. The slide shows a colour DEM next to a Google Earth image of a Deccan valley with "prominent plunge pools", and asks how to find the rivers automatically, without tracing them by hand. Manual mapping does not scale to a continent and is not reproducible: two people draw different networks. An algorithm applied to the same DEM always gives the same answer.

The idea behind every algorithm is the one physical fact we are sure of: **water flows downhill.** So, for every cell, decide where its water goes, and then count how much water passes through each cell. Cells that collect water from a large area are rivers.

### 1.1 D8: send everything to the steepest neighbour (slide 2)
A cell has 8 neighbours: 4 sharing an edge, 4 sharing a corner. The **D8** algorithm sends all of a cell's water to the neighbour with the steepest *downhill gradient*:
$$\text{gradient to neighbour}=\frac{z_{\text{cell}}-z_{\text{neighbour}}}{\text{distance}},\qquad\text{distance}=1\ \text{(edge)},\ \sqrt2\ \text{(corner)},$$
in units of the cell size. Dividing by $\sqrt2$ for the diagonal neighbours matters. A diagonal neighbour is farther away, so the same elevation drop is a gentler slope.

The direction is stored as one number per cell, a power of 2 (the "direction coding" on the slide):

| code | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 |
|---|---|---|---|---|---|---|---|---|
| direction | E | SE | S | SW | W | NW | N | NE |

Powers of 2 are used because they can be combined as bits: a code like 3 = 1 + 2 can mean "east and south-east", which some multiple-direction schemes need.

> [!example] The slide's grid, recomputed
> The left grid on slide 2 is a 6 × 6 elevation surface; its top row is 78, 72, 69, 71, 58, 49. Computing the steepest descent cell by cell (Figure LS29.1 A) reproduces the slide's flow-direction grid in **35 of 36 cells**.
>
> The odd cell is the lowest point on the bottom edge (elevation 11). None of its neighbours is lower, so D8 has nowhere to send its water inside the grid. The slide codes it 4 (south): that is the **outlet**, where water leaves the map. Every real DEM needs this rule at its edge.
>
> Counting the cells upstream of each cell (accumulation) shows the network appear. The outlet collects all 36 cells. A line of cells collecting 21 and 25 marks the main valley, while ridge cells collect only themselves (1).

The right half of slide 2 (from Huang & Lee 2013, *J. Hydrology*) runs the same method on a bigger grid: elevations → flow directions → a drainage network, drawn as numbered cells joined by arrows.

> [!pitfall] Pits stop D8
> A cell lower than all its neighbours (a **pit**) traps the water. Real pits exist (lakes, sinkholes), but most pits in a DEM are measurement errors. They are filled or breached first, as described in [[LS03 Digital Elevation Models and Terrain Analysis]]; otherwise the network breaks into fragments.

### 1.2 MFD: share the water among all downhill neighbours (slide 3)
Slide 3 reproduces Plate 3.1 of Pelletier, which compares the two schemes on Hanaupah Canyon, Death Valley:
- **Steepest descent (D8):** all the water from a cell goes to the single lowest of its eight neighbours.
- **Multiple flow direction (MFD):** the water is split among *all* the lower neighbours, weighted by slope. For this to work, cells must be processed from highest to lowest. Then all the water arriving at a cell has been counted before that cell passes its water on.

The slide's verdict: **"D8 gets stuck if flow is divergent, and there MFD is better."** The reason is geometric. On a convex hillslope or an alluvial fan, water really does spread out in several directions. D8 cannot represent that, because it forces each cell's water into one line. So D8 draws artificial parallel stripes on hillslopes, where MFD gives a smooth sheet. In valleys the flow converges anyway, and both methods agree.

Panels (b) and (c) of the plate show the contributing area for the same canyon computed both ways. The MFD map gives "substantially different and more realistic flow distribution, particularly for hillslopes and areas of distributary flow."

**Rule of thumb.** Use D8 to extract channels, because channels are single lines. Use MFD for hillslope processes and fans, where flow genuinely diverges.

### 1.3 The accumulation map (slides 4–5)
Once every cell has a direction, add up for each cell the number of cells (or the area) whose water passes through it. This is the **flow accumulation** or **contributing area** $A$. Plotted on a log colour scale (slide 4, made in QGIS; the slide points to YouTube tutorials), it looks like a river map: tiny values everywhere on hillslopes, large values along lines.

Accumulation is a stand-in for discharge, because in a uniform rainstorm every cell sends the same amount of water. That is why $A$ appears in every erosion law later in the course ($Q\propto A$, §10, §13).

Slide 5 zooms in and asks the next question: **where does the stream start?** Accumulation grows smoothly from 1 on a ridge to large values in a valley. Nothing in the map itself says "the channel begins here".

### 1.4 Where to start a channel: a threshold, and why it is only approximate (slide 6)
**The simple choice:** call a cell a channel if its accumulation exceeds a threshold, for example 1000 pixels. The slide's red network is this rule applied to the map. It is quick, but the network you get depends entirely on the number you picked:
- lower the threshold and many tiny channels appear;
- raise it and the network shrinks.

**Reality** (A&A fig. 11.19, on the slide): measured channel heads show that the contributing **source area needed to start a channel falls as the valley slope rises**. Four field areas plotted on log axes give clouds that slope downwards from about $10^4$–$10^5$ m² at gentle slopes to $10^2$–$10^3$ m² at slopes near 1. So a single area threshold cannot be right everywhere. A steep hollow needs less water to cut a channel than a gentle one. §2 explains why.

### 1.5 The result: a network and its subcatchments (slide 7)
Slide 7 shows the final stream network draped on shaded relief and, beside it, the landscape cut into **subcatchments**: one colour per stream segment, each being all the cells that drain into that segment. A subcatchment is the area that feeds one reach of river. It is the natural unit for discharge (its area times the rainfall), for sediment budgets, and for comparing basins.

---

## 2. Why channels begin where they do (slide 8)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=8|slide 8]], A&A figs. 11.16, 11.17, 11.20* · <span class="scope-extra-beyond">extra · beyond</span> *the derivation and numbers*

The slide's recipe: **"To find the beginning of a river, compute the variation in flow depth (use mass conservation and force balance), which controls the basal stress with distance. When the stress crosses a threshold, erosion starts and the channel forms."** It also asks: *"Can you write down the conservation equation for the overland flow of water?"* Here is the answer, step by step.

**Mass conservation.** Take a strip of hillslope of unit width, between $x$ and $x+\mathrm dx$ (with $x$ measured downslope from the divide), as in the slide's sketch:
- rain falls on it at rate $R$;
- water soaks into the ground at rate $I$ (infiltration);
- water flows in at the upslope side ($q(x)$, the discharge per unit width) and out at the downslope side ($q(x+\mathrm dx)$).

In steady state the water stored in the strip does not change, so inflow equals outflow:
$$q(x)+R\,\mathrm dx=q(x+\mathrm dx)+I\,\mathrm dx\quad\Longrightarrow\quad\frac{\mathrm dq}{\mathrm dx}=R-I\quad\Longrightarrow\quad q(x)=(R-I)\,x .$$
The discharge grows linearly with distance from the divide, because every metre of slope adds its own excess rain. (Overland flow exists only if $R>I$, i.e. if it rains faster than the soil can absorb: §4.)

**Force balance (how deep is the flow?).** A thin sheet of water on a slope $S$ flows steadily when gravity pulling it downslope balances friction at the bed. In Manning form ([[LS21 River Hydraulics and Hydraulic Geometry]] §5), the discharge per unit width of a sheet of depth $h$ is
$$q=\frac1n\,h^{5/3}S^{1/2}\quad\Longrightarrow\quad h=\Big(\frac{n\,q}{S^{1/2}}\Big)^{3/5}.$$
**Basal shear stress.** The weight of the water column along the slope, per unit bed area, is
$$\tau_b=\rho g\,h\,S .$$
Put the three together:
$$\tau_b(x)=\rho g\,S\Big(\frac{n(R-I)x}{S^{1/2}}\Big)^{3/5}\ \propto\ x^{3/5}\,S^{7/10}.$$
The stress **grows downslope**, because more water has collected, and **grows with slope**. The slide's lower graph (A&A fig. 11.17) shows the same thing: flow thickness and basal stress both rise with distance downslope.

**The channel head.** Soil resists erosion up to a critical shear stress $\tau_c$. Near the divide $\tau_b<\tau_c$ and the ground is not eroded; at the distance where $\tau_b=\tau_c$ the flow starts to cut and a channel begins. Solving $\tau_b(x_c)=\tau_c$:
$$x_c\ \propto\ \tau_c^{5/3}\,S^{-7/6}.$$
This is why the source area falls with slope in A&A fig. 11.19 (§1.4). On a steep slope, less accumulated water is needed to reach the critical stress, so the channel starts closer to the divide.

> [!example] Numbers (Figure LS29.1 B)
> Take rain 50 mm/hr, infiltration 10 mm/hr, Manning $n=0.04$, $\tau_c=5$ Pa.
>
> | slope | channel head $x_c$ |
> |---|---|
> | 0.05 | 241 m |
> | 0.1 | 107 m |
> | 0.2 | 48 m |
> | 0.4 | 21 m |
>
> An 8-fold steepening shortens $x_c$ 11-fold ($8^{7/6}=11.3$). The flow is only millimetres deep: 6 mm at 100 m on a 0.05 slope. Yet it exerts a few pascals on the soil, enough to move fine grains once vegetation is sparse.

> [!pitfall] What this model leaves out
> Channel heads also depend on vegetation (which raises $\tau_c$ enormously), on subsurface flow and seepage (some channels start where groundwater emerges rather than where overland flow is strong), on landslides in steep hollows, and on how frequent the big storms are. The slide's "slope (and many other factors)" means exactly this. The threshold model explains the *trend* with slope; it does not predict every channel head.

---

## 3. Stream networks reflect geology, and obey Horton's laws (slides 9–11)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=9|slides 9–11]]* · see also [[Drainage Density and Horton's Laws]]

**Slide 9: networks follow the rocks.** The slide shows an extracted network whose pattern changes across the map, and a Deccan Traps river running straight along a **joint**. Water erodes fastest where the rock is weakest, so a fracture, a fault or a soft bed is a ready-made path. A river that follows a joint is straight and turns sharply where it switches to another joint.

So the pattern of a network carries a geological signature:
- **dendritic** (tree-like) on uniform rock;
- **rectangular** on jointed rock like the Deccan basalts;
- **trellis** on folded alternating hard and soft layers.

**Slide 10: India's network.** The drainage network of the subcontinent (Himalayan and peninsular rivers) shows the same thing at continental scale: "morphology and density of stream network varies a lot".

**Slide 11: stream order and its laws.** The slide states Strahler's (1952) ordering rules, from the caption of its figure (Montgomery & Dietrich 1989, Marin County):
1. all streams without tributaries are **first order**;
2. where two streams of order $\omega$ meet, they end and a stream of order $\omega+1$ begins;
3. where two streams of unequal order meet, the lower-order one ends and the higher-order one continues through the junction.

So order increases only when two equal streams join. A stream's order measures how many levels of branching lie upstream of it, not how many tributaries it has.

**Drainage density** (sketch (a) vs (b) on the slide) is
$$D_d=\frac{\sum L}{A},$$
the total channel length per unit basin area. High $D_d$ means channels are close together, so hillslopes are short.

> [!intuition] What drainage density measures
> $1/(2D_d)$ is roughly the hillslope length: how far a raindrop travels over the ground before it reaches a channel. Erodible, poorly vegetated, impermeable ground (badlands) has very high $D_d$. Permeable or well-vegetated ground has low $D_d$, because water soaks in or is held back before it can cut a channel (compare the channel-head threshold of §2).

**Horton's laws (the slide's graph, data for Daddy's Creek, Tennessee).** Plot, against stream order $\omega$:
- the number of streams $N_\omega$;
- their mean length $\bar L_\omega$;
- their mean drainage area $\bar A_\omega$.

On a log axis all three fall on straight lines, so each changes by a constant ratio per order:
$$R_B=\frac{N_\omega}{N_{\omega+1}}\approx4.1,\qquad R_L=\frac{\bar L_{\omega+1}}{\bar L_\omega}\approx2.2,\qquad R_A=\frac{\bar A_{\omega+1}}{\bar A_\omega}\approx4.7$$
(the slide's values). Each order has about four times fewer streams than the one below, each about twice as long and draining about five times the area. The small diagram (c) shows the **law of stream numbers**, $R=N_j/N_{j+1}$, as a straight line on log axes.

> [!key] The slide's warning: "likely property of any network" (Kirchner 1993)
> Kirchner showed that randomly generated branching networks also obey Horton's laws, with ratios in the same range. A law that random networks obey cannot tell you anything about the *process* that made a particular network. Horton's ratios are therefore **descriptive** (useful for comparing basins and estimating totals), not **diagnostic**. Do not conclude from $R_B\approx4$ that a basin is "mature" or "in equilibrium".

---

## 4. How rain becomes streamflow (slides 12–13)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=12|slides 12–13]], A&A figs. 11.3, 11.5, 11.8, 11.12*

**Slide 12: three paths to the stream.** The block diagram shows rain falling on a hillslope with a permeable surface soil, an unsaturated zone and a water table. Water reaches the stream by three routes, numbered on the slide:
1. **overland flow** across the surface (fast: minutes to hours);
2. **subsurface storm flow** through the soil just below the surface (intermediate: hours to days);
3. **groundwater flow** from below the water table (slow: days to months).

The inset hydrographs make the point: rain falls in a short burst, while stream discharge rises later and falls slowly. The stream's response is the **sum of the three routes, each delayed and smeared by a different amount**. The fast route makes the peak; the slow route keeps the river flowing between storms (the **baseflow**). Rivers that flow in the dry season (the Deccan rivers after the monsoon) are fed by groundwater.

To measure this, rainfall and water level are recorded together. The photograph (A&A fig. 11.12) shows a gauge in a desert channel: the "sonic look-down sensor" of slide 13, panel (a), mounted over the channel, measures the water surface from above.

**Slide 13: rainfall and hydrographs.** The central schematic shows rainfall intensity $R$ as a block in time, with the **infiltration capacity** $I$ falling during the storm. Infiltration capacity falls during a storm because the soil fills up: the first rain soaks in fast, and as the pores fill the soil accepts water ever more slowly.

Surface runoff is produced only while $R>I$ (the shaded part of the block). This is **infiltration-excess (Hortonian) overland flow**. Discharge $Q$ then rises to $Q_{\text{peak}}$ after a **lag to peak** and recedes slowly.

> [!intuition] Why the lag, and what sets its size
> Water from the far end of the catchment takes longest to arrive. The hydrograph peak comes roughly when water from most of the basin is arriving at once. A big basin, gentle slopes or a long subsurface path give a long lag and a low, broad peak. A small steep basin with impermeable ground gives a short lag and a sharp ("flashy") peak. Urbanisation shortens the lag (paved ground has $I\approx0$), which is why cities flood.

The lower panels of the slide are field records:
- **A&A fig. 11.3:** rainfall bursts and flow depth at three points of a desert channel, where flow appears within minutes of rain and disappears again;
- **a two-season record (Nov 1997 to Mar 1998):** stream stage (red) against daily rainfall (black bars), where every rain spike produces a stage spike, and the stage stays higher after a wet spell than before it, because the ground has filled with water.

---

## 5. Measuring a river (slides 14–15)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=14|slides 14–15]]* · derivations in [[LS21 River Hydraulics and Hydraulic Geometry]] §7–8

**Slide 14: the velocity–area method (USGS, A&A fig. 12.6).** Divide the cross-section into vertical panels $i$ of width $W_i$ and depth $H_i$. Measure the mean velocity $\bar U_i$ in each panel. Then
$$Q=\sum_i\bar U_i\,W_i\,H_i .$$
Discharge is velocity times area, panel by panel, because velocity varies across the channel (slow near the banks, fast in the middle). The sketch also defines:
- the **wetted perimeter** $WP$, the length of bed and banks in contact with water;
- the **hydraulic radius** $R_h=A/WP$, which is close to the depth for a wide channel. Friction acts on the wetted perimeter, so $R_h$ is what enters the flow laws.

**"Both are dynamic" (A&A fig. 12.14).** The slide plots the bed of one gauged section on four dates in one season, with the discharge each day:

| date | discharge (cfs) |
|---|---|
| 9/9 | 635 |
| 9/15 | 6,560 |
| 10/14 | 59,600 |
| 10/26 | about 18,000 (the slide prints "18,00") |

The bed is not fixed. During the big flood it was **scoured** several metres deeper, and it filled again as the flow fell. This matters for gauging. A gauge measures only stage (water level) and converts it to discharge with a **rating curve** built from occasional velocity–area measurements. If the bed scours, the same stage means a larger discharge, so the rating curve shifts. A rating curve made at low flow underestimates flood discharge.

**Slide 15: water level from space (A&A fig. 12.12).** Satellite altimetry tracks the water level of the Ghaghara (a Ganga tributary) from about 1993 to 2002. The level swings by about 6 m every year with the monsoon, and is recorded wherever the satellite track crosses the river. This is how ungauged rivers are monitored.

**Slide 15: hydraulic geometry (A&A fig. 12.13).** At gauging stations along many rivers, width, depth and mean velocity each rise as a power of the mean annual discharge:
$$w\propto Q^{0.5},\qquad H\propto Q^{0.4},\qquad U\propto Q^{0.1}.$$
> [!derivation] Why the exponents add to 1
> Discharge is width × depth × velocity, $Q=wHU$. If $w\propto Q^b$, $H\propto Q^f$ and $U\propto Q^m$, then $Q\propto Q^{b+f+m}$, so $b+f+m=1$ necessarily. The slide's $0.5+0.4+0.1=1$ ✓.
>
> The physics is in how the 1 is shared out. Downstream, most of the extra water is accommodated by a **wider** and **deeper** channel. Velocity barely changes ($Q^{0.1}$), because the slope decreases downstream while the depth increases, and the two effects on velocity nearly cancel ([[LS21 River Hydraulics and Hydraulic Geometry]] §8). That is why a big lowland river is not much faster than a mountain stream, even though it carries a thousand times more water.

---

## 6. Floods: how often, and which ones matter (slides 16–17)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=16|slides 16–17]]* · in depth: [[LS22 Floods Planform and River Profiles]] §1

**Slide 16: a power-law tail (A&A fig. 12.16).** For five US gauges the number of days on which the discharge exceeds $Q$ falls, at high $Q$, as a power law:
$$N(Q)\propto Q^{-\alpha}.$$
The fitted exponents run from about $\alpha\approx1.05$ to $\alpha\approx3.35$. (Which exponent belongs to which gauge is hard to read on the slide image; the shallowest lines appear to be the dry-climate gauges in California and Arizona, and the steepest the Iowa gauge.)

> [!intuition] What a small exponent means
> A power law has a **heavy tail**: very large floods are rare, but not exponentially rare. With $\alpha=1$, a flood ten times bigger is only ten times rarer. With $\alpha=3$, it is a thousand times rarer. Dry-region rivers (small $\alpha$) sit near zero most of the time and are shaped by rare, enormous floods. Humid rivers (large $\alpha$) flow steadily, and the biggest floods are only modestly bigger than typical ones.

**Slide 17: effective discharge (A&A figs. 12.15, 12.17).** The slide's argument, after Wolman & Miller (1960):
- **(a)** the rate of sediment movement rises steeply with discharge (above a threshold, nothing moves);
- **(b)** the frequency of a discharge falls with its size;
- **(c)** the work done over the years by flows of a given size is rate × frequency.

The product is zero for small flows (they move nothing) and small for huge flows (they almost never happen). So it **peaks in between**. "The most sediment is transported by an intermediate level of flood: the **effective discharge**" (Figure LS29.1 C).

The slide's field example: the effective discharge is $Q=113$ m³/s, while the mean annual discharge is only $14.6$ m³/s. Flows smaller than the effective discharge are "too small to accomplish much transport"; larger ones are "too rare to accomplish much transport".

> [!key] "An empirical fact: effective discharge equals bankfull discharge!"
> The flow that just fills the channel to the top of its banks (**bankfull**) is, in many rivers, close to the effective discharge. It recurs every 1–2 years (the "2.33-year flood" of [[LS22 Floods Planform and River Profiles]] §1.2).
>
> The reason is that the channel is built by the flows that do the most work. A smaller channel would overflow during the effective flood and be eroded wider. A larger channel would not be maintained, because flows filling it would be too rare, and the channel would fill with sediment. Bankfull geometry is therefore the channel's memory of its effective discharge. That is why channel width and depth can be read as a measure of discharge (§5).

---

## 7. Sediment loads and floodplains (slides 18 and 28)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=18|slides 18]], [[l_fluvial.pdf#page=28|28]]* · in depth: [[LS22 Floods Planform and River Profiles]] §1.3, §2

**Sediment rating curve (slide 18, A&A fig. 12.18).** Suspended load plotted against water discharge on log axes follows a straight line, $Q_s\propto Q^b$. The slide's line climbs from about 3 to about $3\times10^5$ tonnes/day while discharge goes from about 4 to 2000 cfs, a slope $b\approx1.9$.

So **doubling the discharge roughly quadruples the sediment load**. Faster, deeper water lifts more sediment off the bed and keeps it suspended. The grey cloud around the line is the scatter of individual measurements; it spans more than a factor of ten at a given discharge. Part of that scatter is because the same discharge carries more sediment while a flood is rising (fresh sediment is available) than while it is falling. The dashed segments labelled $j=1,2,3$ appear to show individual events of that kind. (That reading of the dashed lines is mine; the slide does not label them.)

**Floodplains: "decanting the floodwaters" (slide 18, A&A fig. 12.19).** When a flood overtops the banks, the water spreads out of the deep, fast channel onto the wide, shallow floodplain. There it suddenly slows, because it is shallow and the vegetation is rough. Slow water cannot carry what fast water carried, so the sediment drops in order of size:
- the **coarsest** settles immediately at the bank, building raised **levees** along the channel;
- **finer** silt and clay settle farther out, in the floodplain's backswamps.

The cross-section on the slide shows exactly this: levees on both banks, the floodplain behind them, and a terrace at a higher level (an older floodplain the river has since cut below).

**Slide 28: how fast floodplains build.** This is a Bolivian Amazon foreland example: a DEM of a foreland basin with the Beni and Mamoré rivers, and two graphs.
- **(b)** The deposition rate falls with distance from the channel: about 6 cm/yr within a few hundred metres, falling to about 1 cm/yr at 3 km. This is the levee effect of slide 18 measured: most sediment drops close to the channel.
- **(c)** Deposition is **episodic**: it comes in particular years, plotted on a timeline of ENSO years, so big deposition years are tied to the climate cycle that controls flooding. (I recall this figure as Aalto et al. 2003, *Nature*; it is not named on the slide.)

---

## 8. Braided rivers (slides 19–22)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=19|slides 19–22]], A&A figs. 12.11, 12.20, 12.21* · in depth: [[LS22 Floods Planform and River Profiles]] §3

A **braided river** splits into many channels around bars of gravel and sand, which rejoin and split again (the photographs on slide 19 and the satellite images on slides 21–22). Braiding happens when four conditions come together:
- **a lot of coarse sediment**;
- **a steep slope**;
- **weak, easily eroded banks**;
- **strongly varying discharge** (glacier melt, monsoon floods).

The river cannot carry all its load through one channel. It drops bars, the bars split the flow, the new channels erode the weak banks, and the process repeats. The laboratory sequence on slide 19 (elevation and discharge at five times) shows that the pattern never settles: channels switch position constantly, while the braided *style* persists.

**"Discharge controls the width of braided rivers"** (slide 19, graph for the Tanana, Iskut and Taku rivers). The effective width rises from about 250 m to about 800 m as discharge rises from a few hundred to about 2000 m³/s. A braided river has no strong banks to confine it, so it simply spreads to whatever width its flow can wet.

**Slide 20** is a Google Earth view of the upper Bhagirathi valley around Harsil (Uttarakhand). Here a Himalayan river carrying glacial sediment braids across a wide, flat valley floor between steep rock walls. Upstream and downstream, where the valley narrows, the same river is a single channel in bedrock.

---

## 9. Meandering rivers (slides 23–25)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=23|slides 23–25]], A&A figs. 12.22–12.26* · in depth: [[LS22 Floods Planform and River Profiles]] §4

**Slide 23: meanders are self-similar.** Three rivers of very different size are drawn at different scales: the Mississippi at Point Breeze (average width 1115 m), New Fork River (16 m) and Duck Creek (2.4 m). Their bends look the same. The graph makes it quantitative: meander wavelength $L$ against channel width $W$ gives
$$L=10.9\,W^{1.01},$$
i.e. **wavelength ≈ 11 channel widths, whatever the size of the river**.

An exponent of 1 means there is no other length scale in the problem. The bend size is set only by the channel's own width, which is in turn set by the effective discharge (§6). So a photograph of meanders with no scale bar does not tell you whether it shows a creek or the Mississippi.

**Slide 24: how bends grow (A&A fig. 12.24).** In plan view, a point bar (orange) grows on the inside of each bend. The cross-section A–A′ shows why:
- the deepest part of the channel (the **thalweg**) hugs the **outer bank**, where the water is fastest and erodes the bank;
- the inner bank receives sediment and builds a **point bar**.

Water going round a bend is thrown outward. It piles up against the outer bank, then sinks there and returns along the bed towards the inside. This **helical flow** carries bed sediment from the outer bank to the inner one ([[LS22 Floods Planform and River Profiles]] §4.1). So erosion on the outside and deposition on the inside work together: the bend migrates outward and grows in amplitude while the channel keeps its width.

**Slide 25: evolution (A&A fig. 12.26).** A simulated meandering river is shown at four times (20, 40, 60, 80). The bends grow and migrate until two neighbouring bends meet. The river then takes the short cut (a **cutoff**), abandoning the loop as an **oxbow lake**. Growth lengthens the river and cutoffs shorten it, so in the long run its sinuosity fluctuates around a steady value rather than growing without limit.

---

## 10. The long profile of an alluvial river (slide 26)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=26|slide 26]], A&A figs. 12.27, 12.28, 12.31* · in depth: [[LS22 Floods Planform and River Profiles]] §5–6

The profile from source to sea is **concave up**: steep near the source, nearly flat near base level. The slide labels the slopes and bed materials along a typical profile:

| reach | slope | bed material |
|---|---|---|
| near the source | 0.02 (20 m/km) | boulders > 256 mm |
| upper river | | gravel 2–256 mm |
| middle river | 0.001 (1 m/km) | sand 0.06–2 mm |
| near the sea | 0.00001 (1 cm/km) | silt and clay < 0.06 mm |

These two trends go together. Coarse grains need a steep slope to be moved, so a reach full of boulders must be steep. Downstream, grains are worn smaller by abrasion and the coarse ones are left behind, so the bed gets finer. And the discharge grows (Hack's rule: area, and so discharge, grows with distance downstream), so a gentler slope is enough to carry the load.

**Hack's rule.** Main-stream length $L$ and drainage area $A$ are related by $L\propto A^{h}$ with $h\approx0.6$. Since $h>0.5$, basins get relatively longer and narrower as they get bigger.

**Diffusive evolution (the two graphs).** An alluvial river is **transport-limited**: its bed is its own sediment, so it lowers only as fast as it can carry sediment away. If the sediment flux is proportional to slope (more slope, more transport), then
$$q_s=-\kappa\,\frac{\partial z}{\partial x},\qquad\frac{\partial z}{\partial t}=-\frac{\partial q_s}{\partial x}=\kappa\frac{\partial^2z}{\partial x^2},$$
the **diffusion equation**, the same mathematics as hillslope creep ([[LS12 Hillslope Transport and the Diffusion Equation]]). The diffusivity $\kappa$ grows with discharge.

The slide's left graph shows profiles relaxing over time (curves labelled SL = 10 to 100). The right graph shows a profile responding to a fall in base level over 1–10 ka and then 10–100 ka. The drop does not travel upstream as a step (that would be the bedrock behaviour of §13). It spreads out, steepening the lower river first and then more and more of the profile. Diffusion **smooths** any disturbance; it never preserves a sharp knickpoint.

---

## 11. Sediment budgets: the Amazon, the Ganga–Brahmaputra and the Bengal Fan (slides 27, 29)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=27|slides 27]], [[l_fluvial.pdf#page=29|29]], A&A figs. 12.32–12.34* · in depth: [[LS22 Floods Planform and River Profiles]] §7

**Slide 27: the Amazon.** A river does not just pass sediment from the mountains to the sea. Along the way it erodes its banks, deposits bars and floodplain, and swaps sediment with them. The slide maps the Amazon basin (the Andes, the foreland basin, the Brazilian and Guiana shields) and a mainstem budget. It contains:
- a bar chart of **bank erosion and tributaries** adding sediment downstream, totalling **1290** (million tonnes/yr);
- **floodplain and bar deposition** removing it, with **209** labelled;
- a figure of **616** at the upstream end.

(The exact meaning of each label is hard to read on the slide; [[LS22 Floods Planform and River Profiles]] §7 reconstructs the budget.) The slide's point is the comparison at the bottom: **the Ganga and Brahmaputra together carry about 700 Mt/yr**, one of the largest sediment loads on Earth, because they drain the rapidly eroding Himalaya.

**Slide 29: the Bengal Fan.** Most of that sediment ends up in the Bay of Bengal, in the Bengal Fan. The slide gives its size: about 3000 km long, up to 1430 km wide, an area of 3 million km² and a sediment volume of 12.5 million km³. It asks: *how much is stored in the floodplain (the Indo-Gangetic Plains), and what is the evacuation/deposition per year?*

> [!example] A consistency check (my arithmetic)
> Turn the fan's volume into a mass, using a bulk density of about 2000 kg/m³ for compacted, porous sediment:
> $$1.25\times10^{16}\ \text{m}^3\times2000\ \text{kg/m}^3=2.5\times10^{19}\ \text{kg}.$$
> At today's supply of 700 Mt/yr ($7\times10^{11}$ kg/yr) that takes **about 36 million years**. That is comparable to the time since the Himalaya began to shed sediment on a large scale.
>
> The agreement says two things: the present-day sediment supply is not wildly unusual for the long term, and most of the eroded Himalaya now lies under the Bay of Bengal. The floodplain is a temporary store along the way. To estimate how much it holds, you would need the plains' area (several $10^5$ km²) times the thickness of young sediment, which is the slide's open question.

---

## 12. Bedrock rivers: how rock is cut, and how fast (slides 30–38)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=30|slides 30–38]], A&A Ch. 13* · in depth: [[LS23 Bedrock Channels and River Incision]] §2–4

**Slide 30: the processes.** A bedrock river cuts down only as fast as it can break rock. The slide lists the processes; all depend on the river's **stream power** (the rate at which falling water loses energy, $\rho gQS$ per unit length of channel):
- **abrasion**: sand and gravel carried by the flow grind and chip the bed, like sandpaper;
- **quarrying (plucking)**: the flow lifts out whole blocks already loosened along joints (very effective in jointed basalt);
- **hydraulic wedging**: small stones are swept into cracks and jammed there; the next lift of the block lets them drop deeper, prising it loose (slide 37's photographs show pebbles wedged under a basalt slab);
- **dissolution**: important in limestone, minor in basalt;
- **knickpoint migration**: steps in the profile that retreat upstream (§13).

**Slides 31–32: measuring long-term incision.** Caves in a valley wall were once at river level; the river has since cut down below them. Sediment washed into a cave stops being exposed to cosmic rays once it is buried. The decay of the cosmogenic nuclides produced by that exposure gives the **burial age**. The cave's height above today's river, divided by the burial age, is the incision rate.

The South Fork Kings River canyon example (slide 31, A&A fig. 13.2–3):
- caves from about 0.3 to 3 Myr old, at heights up to 400 m;
- rates from about 0.02 to 0.2 mm/yr in different periods, i.e. incision is **not steady** but comes in bursts.

Slide 32 (A&A fig. 13.21) takes the stream-power idea to the Yarlung Tsangpo gorge around Namche Barwa. Where the river's stream power peaks, the cooling ages of the rocks are youngest, i.e. those rocks have been exhumed fastest. Erosion concentrates where the river is most powerful. The same slide shows the **short-term** view (A&A fig. 13.6): in a single large flood (Supertyphoon Bilis, Taiwan), the channel walls were eroded by tens of millimetres, most of it low on the walls where the sediment-laden flow strikes. The softer schist and harder quartzite show different patterns.

**Slide 33: direct measurement (A&A fig. 13.4).**
- **Erosion holes:** drill holes in the rock and measure the surface's drop with a micrometer.
- **Erosion monuments:** fix a bar across the channel and measure down to the bed.

Both give rates over months to years, short enough to catch individual floods. The slide also lists two papers (DOIs 10.1029/GM107p0035 and 10.1002/esp.4007).

**Slide 34: abrasion and rock strength (A&A figs. 13.9–13.10).**
- **Rock strength.** In flume experiments the erosion rate falls steeply with the rock's tensile strength $\sigma_T$:
$$E=7.7\,\sigma_T^{-2.0}.$$
Twice as strong means four times slower. The reason is energy: to chip rock, an impact must store enough elastic strain energy to break it, and the energy needed per unit volume grows as $\sigma_T^2$ ([[LS23 Bedrock Channels and River Incision]] §3.2).
- **The tools-and-cover effect.** Erosion against the mass of sediment added rises, peaks (around 150–250 g in the experiment) and then falls. With little sediment there are few **tools** to strike the bed. With too much, the sediment **covers** the bed and shields it. Maximum erosion comes at an intermediate supply.

**Slide 35: flow separation and potholes (A&A fig. 13.8).** Where the bed curves sharply, the flow cannot follow the surface and separates from it, forming eddies. The eddies swirl grains in place, drilling **potholes** and cutting **flutes**. The slide shows flow past a sphere at increasing Reynolds number $Re=\rho vL/\mu$, the ratio of inertial to viscous forces. At low $Re$ the flow wraps smoothly round the sphere; at higher $Re$ it separates and sheds vortices; at very high $Re$ the wake is fully turbulent. River flow has enormous $Re$, so separation behind every bump is the rule.

**Slides 36–38: local examples.** Slide 36 shows potholes within 50–100 km of Pune, some still holding the rounded cobbles that drilled them. Slide 37 shows wedging. Slide 38 has photographs of a field visit to a basalt riverbed (a "summer talk", March 2025). The Deccan basalts are an ideal place to see bedrock-river processes: jointed flows for quarrying, vesicular flow tops that erode fast, massive cores that form steps ([[LS18 Deccan Traps Terrain]], [[LS28 Deccan Field Guide Lava Architecture and Sahyadri Stratigraphy]]).

---

## 13. The bedrock-river equation, its steady state and its waves (slides 39–40)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=39|slides 39–40]], A&A eq. 13.21, figs. 13.1, 13.18* · in depth: [[LS23 Bedrock Channels and River Incision]] §5–6

**The equation (slide 39).** Measure $x$ downstream from the divide, so the bed falls with $x$ and $\partial z/\partial x<0$. Suppose the erosion rate is proportional to the stream power per unit bed area, with an erodibility constant $k$:
$$E=k\,\frac{\rho gQS}{W},\qquad S=-\frac{\partial z}{\partial x}.$$
The bed lowers at the erosion rate, so with no uplift
$$\frac{\partial z}{\partial t}=-E=\frac{k\rho gQ}{W}\frac{\partial z}{\partial x}=C\frac{\partial z}{\partial x},\qquad C=\frac{k\rho gQ}{W}$$
(the slide's A&A eq. 13.21). This is an **advection equation**. Its solutions are $z(x,t)=f(x+Ct)$: any shape in the profile moves towards smaller $x$, i.e. **upstream**, at speed $C$, without changing shape. A waterfall is such a shape.

The slide adds that people more generally use $E=kA^m|\partial_xz|^n$, with drainage area $A$ standing in for discharge. With $n=1$ the equation stays an advection equation; with $n\ne1$, steps sharpen or spread ([[LS23 Bedrock Channels and River Incision]] §6.4).

**The slide's questions, answered.**
- *How to include uplift?* Uplift raises every point at rate $U$:
$$\frac{\partial z}{\partial t}=U+C\frac{\partial z}{\partial x}.$$
- *Steady state with constant $U$ and $k$?* Set $\partial z/\partial t=0$, which gives $S=U/C=UW/(k\rho gQ)$. Erosion everywhere just keeps pace with uplift. Since $Q$ grows downstream, $S$ falls downstream: the profile is **concave up** (Figure LS29.1 D).
- *Relation to Hack's rule?* With $Q\propto A$ and $A$ growing as a power of distance (Hack: $L\propto A^{0.6}$, so $A\propto x^{1/0.6}$), the steady slope falls as a power of distance and the profile has a definite concavity.

**Slide 40: the slope–area plot.** Since $S\propto Q^{-1}\propto A^{-1}$ (for $n=1$), more generally $S\propto A^{-m/n}$. Plotting log slope against log drainage area for points along a river gives a straight line of slope $-m/n=-\theta$, the **concavity index**. Observed values are typically 0.4–0.6.

The map and profiles on the slide show three tributaries (1, 2, 3) of different sizes with concave long profiles. The right-hand figure (Wobus et al. 2006) shows what a **transient** river looks like: a knickpoint separates a lower reach that has adjusted to a new, faster uplift (steeper for its area) from an upper reach still graded to the old rate. On a slope–area plot this appears as two parallel line segments offset from each other. On the map, the knickpoints of all tributaries lie at about the same *elevation*, because they are parts of one wave moving up the network.

**Transient response (slide 39, A&A fig. 13.18).**
- **(a) Faster uplift:** the whole profile must steepen to erode faster. The steepening starts at the outlet and moves upstream as a "wave of erosion" (curves $t=0,1,2$ approaching the final steady state).
- **(b) A sudden base-level drop:** a step appears at the outlet and migrates upstream, leaving the lowered profile behind it (Figure LS29.1 D).

In both cases the information that something changed downstream travels up the river at speed $C$. So the upper parts of a big river can be unaware of a change for millions of years.

The slide's further reading, not yet read here: Perron & Royden, *An integral approach to bedrock river profile analysis* (the $\chi$ method, [[LS23 Bedrock Channels and River Incision]] §6.1); Willett, McCoy, Perron, Goren & Chen, *Dynamic reorganization of river basins*; and a laboratory experiment.

---

## 14. Waterfalls: Niagara and the Western Ghats (slides 41–42)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=41|slides 41–42]], A&A figs. 13.14, 13.20* · in depth: [[LS23 Bedrock Channels and River Incision]] §7

**Niagara (slide 41).** The section shows a hard caprock (the Niagara limestone) over weaker shale and sandstone (Clinton and Medina formations). The plunging water and spray erode the weak rock at the foot of the fall faster than the caprock. The caprock is undercut until it collapses, the face moves back, and the cycle repeats. The fall therefore **retreats upstream while keeping its shape**, as the advection equation of §13 predicts for a step.

The map shows the gorge it has cut from the Niagara escarpment near Lewiston–Queenston back to the present Horseshoe Falls. About 11 km in about 12,500 years is roughly 0.9 m/yr (my arithmetic, with a commonly quoted gorge length and age).

**The Western Ghats (slide 42).** The slide's photographs:
- a typical **scarp** near Chandanpuri Ghat;
- a **doublet of waterfalls** near Chandanpuri Ghat;
- a **one-step** waterfall;
- a **three-step** waterfall near Kas Pathar.

The steps come from the layered lava flows. Each flow has a hard, massive core and a weak, vesicular or rubbly top. So a river descending the scarp meets hard–weak–hard–weak layers, and makes a fall at each hard core. The number of steps reflects how many flows the river crosses and how well each core resists. The scarp itself retreats like a giant waterfall ([[LS18 Deccan Traps Terrain]]).

---

## 15. The lecture's questions (slide 43)
<span class="scope-taught">taught</span> *[[l_fluvial.pdf#page=43|slide 43]]*

The three questions (what a bedrock river is, the governing equation with uplift, the steady profile with $Q\sim x^n$ and what it says about uplift, and the speed $C=k\rho gQ$ of a waterfall) are solved in full in [[LS23 Bedrock Channels and River Incision]] §11A.

That section also explains a trap in the question's sign convention. The question writes $\partial_tz=-k\rho gQ\,\partial_xz+U$, which erodes only if $x$ is measured *upstream* from the mouth. But part 2's $Q\sim x^n$ needs $x$ measured *downstream* from the divide, as in §13 here. Write the physics with the slope $S>0$ and say which way $x$ runs, and the answers are the same either way.

---

## Summary
> [!summary] The fluvial lectures in twelve lines
> - **Finding rivers:** D8 sends each cell's water to the steepest neighbour (diagonals divided by $\sqrt2$, coded 1–128); MFD shares water among downhill neighbours and is better where flow diverges. Flow accumulation ≈ contributing area ≈ discharge.
> - **Channel heads:** overland flow $q=(R-I)x$; depth from Manning; stress $\tau_b=\rho ghS\propto x^{3/5}S^{7/10}$; a channel starts where $\tau_b>\tau_c$, so $x_c\propto S^{-7/6}$ (steeper slopes need less area: A&A fig. 11.19). An area threshold is only a convenience.
> - **Networks** follow the geology (joints in the Deccan). Strahler order; drainage density $\sum L/A$; Horton ratios ($R_B\approx4$, $R_L\approx2$, $R_A\approx5$) are obeyed even by random networks, so they describe, not diagnose.
> - **Streamflow** = overland + subsurface storm flow + groundwater, each delayed differently; runoff where rain > infiltration capacity; lag to peak grows with basin size.
> - **Gauging:** $Q=\sum U_iW_iH_i$; the bed scours in floods, so rating curves shift. Hydraulic geometry $w\propto Q^{0.5}$, $H\propto Q^{0.4}$, $U\propto Q^{0.1}$, with exponents summing to 1 because $Q=wHU$.
> - **Floods:** power-law tails $N(Q)\propto Q^{-\alpha}$ (small $\alpha$ = rare giant floods dominate). Work = rate × frequency peaks at the **effective discharge**, which is about the **bankfull** discharge.
> - **Floodplains:** sediment load $\propto Q^{\approx2}$; overbank water slows and drops coarse sediment at levees, fine farther out; deposition falls with distance from the channel and is episodic.
> - **Braided** where load is high, slope steep and banks weak; width set by discharge. **Meanders** are self-similar ($L\approx11W$), grow by outer-bank erosion and point-bar deposition (helical flow), and are trimmed by cutoffs.
> - **Alluvial profiles** are concave, fining downstream; transport-limited rivers obey a diffusion equation, so base-level changes spread out.
> - **Budgets:** the Ganga–Brahmaputra carry about 700 Mt/yr; the Bengal Fan (12.5 million km³) is roughly 36 Myr of that supply.
> - **Bedrock rivers** cut by abrasion, quarrying, wedging and dissolution, at rates set by stream power, rock strength ($E\propto\sigma_T^{-2}$) and the tools-and-cover balance. Incision is measured by cave burial ages, pins and monuments.
> - **Bedrock profiles:** $\partial_tz=U+C\partial_xz$, $C=k\rho gQ/W$; steady state $S=U/C$ is concave up ($S\propto A^{-\theta}$); disturbances travel upstream as knickpoints and waterfalls (Niagara, the stepped Deccan falls).

## Practice
1. Compute the D8 direction and the accumulation for the 3 × 3 grid 9 8 7 / 8 5 4 / 7 4 1 (cell size 1). Which cell is the outlet, and how many cells drain through the centre?
2. Show from mass conservation that steady overland flow has $q=(R-I)x$. With Manning's law, show that the channel-head distance scales as $S^{-7/6}$. By what factor does $x_c$ change if the slope doubles?
3. A basin has 64 first-order streams and $R_B=4$. How many second- and third-order streams do you expect, and what is the highest order? Why does Kirchner's result limit what you can conclude from this?
4. Hydraulic geometry at a station gives $w\propto Q^{0.26}$ and $H\propto Q^{0.40}$. What must the velocity exponent be?
5. Explain, with a sketch of rate × frequency, why neither the mean flow nor the largest flood is the effective discharge. Why should the effective discharge be close to bankfull?
6. In the advection equation $\partial_tz=C\partial_xz$ ($x$ downstream from the divide), show that $z=f(x+Ct)$ is a solution and that a step moves upstream. If $C\propto Q$ and $Q$ grows downstream, does a knickpoint speed up or slow down as it climbs?
7. Estimate how long the Ganga–Brahmaputra would take to deliver the Bengal Fan's volume. List two reasons the estimate could be too short or too long.

> [!example]- Solutions
> **1.** The centre (5) drains to its steepest-descent neighbour. Edge gradients: to 4 (east) $1$, to 4 (south) $1$. Corner gradient: to 1 (south-east) $4/\sqrt2=2.83$. So it drains **south-east**, code 2.
>
> Doing the same for every cell, the water ends at the corner cell 1, which is the outlet (no lower neighbour on the grid). Cells draining through the centre: the centre itself and the cells whose steepest descent is into it: 9 (south-east, gradient $4/\sqrt2=2.83$), and both 8s (gradient 3). So 4 cells pass through the centre. The outlet collects all 9.
>
> **2.** Steady strip balance as in §2. $\tau_b=\rho gS\,(n(R-I)x/S^{1/2})^{3/5}\propto x^{3/5}S^{1-3/10}=x^{3/5}S^{7/10}$. Setting it equal to $\tau_c$ gives $x_c^{3/5}\propto S^{-7/10}$, so $x_c\propto S^{-7/6}$. Doubling $S$ multiplies $x_c$ by $2^{-7/6}=0.45$.
>
> **3.** 16 second-order, 4 third-order, 1 fourth-order: the basin is fourth order. Random networks give similar ratios, so the value says nothing about the processes or the age of this basin.
>
> **4.** $1-0.26-0.40=0.34$. (A fast-velocity exponent like this is typical of the at-a-station geometry, where a flood mostly deepens and speeds up the flow in a channel of fixed width.)
>
> **5.** Small flows are frequent but move almost nothing (below threshold, and transport rises steeply with $Q$). The largest floods move a lot but almost never happen. The product peaks at moderate floods recurring about yearly. The channel is shaped by the flows that do the most work, so its full-bank capacity matches them.
>
> **6.** $\partial_tf=Cf'$ and $\partial_xf=f'$, so the equation holds. The shape at $x+Ct$ is fixed, i.e. it sits at $x=x_0-Ct$: decreasing $x$, upstream. As the knickpoint climbs, $Q$ falls, so $C$ falls: it **slows down**. That is why knickpoints pile up in the small headwater tributaries.
>
> **7.** About 36 Myr (§11). It could be **too long** if supply was larger in the past (glacial periods, monsoon strengthening) or if part of the fan is older material from other rivers. It could be **too short** if a lot of sediment is stored on land (the Indo-Gangetic Plains, the Bengal delta) instead of reaching the fan, or if the bulk density is higher than 2000 kg/m³.

## Map of this chapter
> [!connection] How LS29 connects
> **Builds on:** [[LS03 Digital Elevation Models and Terrain Analysis]] (pits, flow routing), [[LS12 Hillslope Transport and the Diffusion Equation]] (the diffusion equation), [[LS16 Fluvial Landscapes]] (stream power).
> **Deeper versions:** [[LS21 River Hydraulics and Hydraulic Geometry]] (flow laws, gauging, hydraulic geometry), [[LS22 Floods Planform and River Profiles]] (floods, floodplains, braiding, meanders, alluvial profiles, budgets), [[LS23 Bedrock Channels and River Incision]] (processes, incision, profiles, knickpoints, the slide-43 solutions), [[LS25 Water in the Landscape]] (infiltration and runoff).
> **Field:** [[LS18 Deccan Traps Terrain]], [[LS28 Deccan Field Guide Lava Architecture and Sahyadri Stratigraphy]]; practicals in [[LS20 GIS and TopoToolbox Practicals]].
> **Concepts:** [[Drainage Density and Horton's Laws]] · [[Knickpoint]] · [[Stream Power Law]] · [[Chi Transform]]

## Provenance
> [!provenance]- Sources
> - Lecture slides [[l_fluvial.pdf]] (43 slides), read as images on 2026-11-23. Slide text, figure numbers and quoted numbers are from those images: Pelletier Plate 3.1 (slide 3), Huang & Lee 2013 (slide 2), Strahler rules and Daddy's Creek ratios (slide 11), the gauge cross-section discharges (slide 14), the hydraulic-geometry exponents (slide 15), the flood-frequency exponents (slide 16), the effective-discharge numbers (slide 17), the braided-width graph (slide 19), $L=10.9W^{1.01}$ (slide 23), bed materials and slopes (slide 26), the Amazon and Ganga–Brahmaputra figures (slide 27), the Bengal Fan dimensions (slide 29), $E=7.7\sigma_T^{-2.0}$ (slide 34).
> - Readings uncertain from the images: the assignment of flood exponents to gauges (slide 16), the dashed $j$ lines (slide 18), the labels of the Amazon budget (slide 27). These are flagged where they occur.
> - Recalled, not read here: Aalto et al. 2003 as the source of the slide-28 figure; the length and age of the Niagara gorge; Wolman & Miller 1960 as the origin of the effective-discharge argument; Kirchner 1993's result (the slide names it but does not state it).
> - My additions: all derivations (§2, §5, §6, §10, §13), the D8 recomputation, the channel-head numbers, the toy effective-discharge curve and the Bengal Fan estimate (`scripts/ls29_fluvial_slides_numbers.py`, `scripts/fig_ls29_fluvial_slides.py`).
