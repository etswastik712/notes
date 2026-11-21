---
id: landscape-evolution/2026-11-18-fluvial-landscapes-lecture-slides
aliases: [Fluvial landscapes lecture slides (2026-11-18)]
tags: [landscape-evolution, fluvial, bedrock-rivers, drainage-networks]
trust_tier: agent_written
---

# Fluvial landscapes lecture slides (2026-11-18)

Slides l_fluvial.pdf for the lectures on fluvial landscapes. Figure numbers refer to A&A (the course textbook; chapters 11 to 13). The slides are text-light: all equations and most figures are images and did not come through in the extracted text, so they are marked "(equation on slide)" instead of being reconstructed. (Classroom: 2026-11-19-l-fluvial-1zR6Ym.pdf)

## Covered

### 1. Finding rivers in a DEM
- Need automated algorithms rather than manual mapping.
- D8 routing: a steepest-descent algorithm; uses the elevations of the 8 neighbours to compute the gradient. D8 gets stuck if flow is divergent; there MFD is better.
- MFD (multiple flow direction): distributes the flow among downhill neighbours (see Pelletier).
- Accumulation map (e.g. in QGIS) from D8 gives the stream network.
- Where does a channel head start? Simple approximate choice: an area/accumulation threshold, e.g. 1000 pixels. In reality slope (and many other factors) controls the total source area needed to start a channel (A&A fig 11.19).
- Physically: compute the variation of flow depth with distance (mass conservation and force balance), which controls the basal stress. When the stress crosses a threshold, erosion starts and the channel forms (A&A fig 11.16, 17, 20). Slide question: write down the conservation equation for overland flow of water.
- Output: final stream network and the subcatchments of individual streams.

### 2. Stream networks
- The network reflects the underlying topography and geology (rock types, structures); example: a river following a joint in the Deccan Traps.
- Morphology and density of the network vary a lot.
- Stream order and its associated rules; likely a property of any network (Kirchner, 1993).

### 3. Streamflow and floods
- Streamflow is generated as a response to rainfall; measured as water level together with precipitation (A&A fig 11.12); rainfall and hydrographs (A&A 11.3, 5, 8).
- Stream cross-section and streamflow measurements; both are dynamic (fig 12.14). Water-level variation from satellite data (fig 12.12).
- Streamflow depends on width, depth and velocity of the flow (fig 12.13).
- Frequency distribution of floods has a power-law tail at high discharge (fig 12.16).
- Sediment discharge depends on both the magnitude and the frequency of floods. The most sediment is transported by an intermediate flood, the *effective discharge* (figs 12.15, 12.17).
- Empirical fact: effective discharge equals bankfull discharge.
- Sediment load with discharge (fig 12.18); floodplains (fig 12.19).

### 4. River planform
- Braided rivers (fig 12.11, 20, 21): discharge controls the width of braided rivers.
- Meandering and self-similarity (fig 12.22, 23). Erosion and deposition work together to make meanders grow in amplitude (fig 12.24). Evolution of meandering rivers (fig 12.26).

### 5. Long profile, sediment budgets
- River profile, Hack's rule, and diffusive evolution of alluvial, transport-limited rivers (fig 12.27, 28, 31).
- Amazon sediment budget (fig 12.32 to 34): figures on the slide 1290, 616 and 209 (Mt/yr; which arrow each belongs to is in the figure). Ganga and Brahmaputra together: about 700 Mt/yr.
- Bengal Fan: length about 3000 km, width up to 1430 km, area 3 million km$^2$, sediment volume 12.5 million km$^3$.
- Open slide question: how much is stored in the flood plain (Indo-Gangetic Plains), and what are the evacuation/deposition rates per year? Reading: Eos, "The search for the severed head of the Himalayas".

### 6. Bedrock rivers
- Erosion mechanisms (stream-power dependent): abrasion, quarrying, hydraulic wedging, dissolution. Knickpoint migration.
- Measuring long-term incision (fig 13.2-3); long-term incision and stream power (fig 13.21); short-term incision during a large flood (fig 13.6); direct measurement (fig 13.4).
- Abrasion rate depends on rock strength and sediment concentration (fig 13.9-10). Abrasion and flow curvature/separation (fig 13.8); flow around a sphere at increasing Reynolds number, $Re = \rho v L/\mu$ (turbulence). Potholes in the neighbourhood (50 to 100 km). Wedging (fig 13.12).
- In the absence of uplift a bedrock river evolves obeying an advection equation (equation on slide). More generally, erosion rate $\sim k\,A(x)^m\,|\partial_x z|^n$.
- Slide questions: how to include uplift in the equation? What is the steady-state profile for steady uplift and constant $k$? Related to Hack's rule (catchment area vs slope).
- Transient response of a bedrock river profile (fig 13.18); concave-up channel long profile (fig 13.1); Niagara Falls and its headward march (fig 13.14, 13.20).
- Local examples: a typical scarp near Chandanpuri Ghat, a doublet of waterfalls there (one-step waterfall), a three-step waterfall near Kas Pathar; Dabhosa falls, Nashik, with prominent plunge pools.
- Further reading: Perron & Royden, "An integral approach to bedrock river profile analysis"; Willett, McCoy, Perron, Goren & Chen, "Dynamic Reorganization of River Basins"; DOIs 10.1029/GM107p0035 and 10.1002/esp.4007.

### 7. Problem sheet on the last slides
1. What is a bedrock river? Where in India can one find them? Argue that the evolution of a bedrock river long profile $z(x)$ in a region undergoing uplift $U$ is governed by the equation on the slide, where $x$ is distance along the river, $k$ bedrock erodibility, $\rho$ density of water and $Q$ river discharge; ignore the variation of river width with $x$. (1+1+2)
2. What is the steady-state shape of this river when discharge $Q \sim x^n$? Can one infer uplift rate in a region by studying bedrock river profiles? What are the potential sources of error? (2+1+1)
3. Assuming $Q$ does not change much over a small stretch, show that a waterfall in this river moves headward (upstream) with the speed given on the slide. (2)

Practice pattern: these three questions practise deriving the profile evolution from stream power (erosion proportional to a power of $Q$ and slope, plus uplift), solving for the steady state, and the knickpoint celerity (see [[landscape-evolution/2026-11-10-knickpoint-animation-topotoolbox-getlocation]]).

## From the post
"lecture slides for the lectures on fluvial landscapes attached"

## Files
- [l_fluvial.pdf](https://drive.google.com/file/d/1zR6YmxPiDurPChPJqXD5s2rtxYMd6Qfj/view?usp=drive_web): read in full as text (7785 characters); equations and figures are images and were not read.

## Related
- [[05-landscapes-geomorphology/ls22-floods-planform-and-river-profiles]]: your notes on floods, planform and river profiles (sections 3 to 5)
- [[05-landscapes-geomorphology/ls23-bedrock-channels-and-river-incision]]: your notes on bedrock channels and incision (section 6)
- [[05-landscapes-geomorphology/ls21-river-hydraulics-and-hydraulic-geometry]]: flow width, depth, velocity
- [[05-landscapes-geomorphology/concepts/stream-power-law]]: the erosion law used for bedrock rivers
- [[05-landscapes-geomorphology/concepts/drainage-density-and-hortons-laws]]: stream order and network density
- [[05-landscapes-geomorphology/concepts/braided-rivers]]: braided planform
- [[05-landscapes-geomorphology/concepts/meandering-and-point-bars]]: meander growth
- [[05-landscapes-geomorphology/concepts/overland-flow-and-runoff-mechanisms]]: overland flow and channel initiation
- [[05-landscapes-geomorphology/concepts/pothole-networks]]: potholes under abrasion
- [[landscape-evolution/2026-08-11-qgis-and-topotoolbox-tutorials]]: D8 flow routing and accumulation threshold in practice

<!-- kurooto:material5b76e0d0 -->
Textbook: [[landscape-evolution/books/l-fluvial|l_fluvial]] (its concepts are listed there).
<!-- /kurooto:material5b76e0d0 -->
