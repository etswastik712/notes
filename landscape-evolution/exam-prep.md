---
id: landscape-evolution/exam-prep
aliases: ["Exam prep: Landscape Evolution (c41 - EC2123)"]
tags: [exam-prep, landscape-evolution]
trust_tier: agent_written
---

# Exam prep: Landscape Evolution (c41 - EC2123)

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
Not announced yet. Past: mid-sem (open-notes, handwritten notes only, calculator allowed, no sharing; date not stated in Classroom) and project presentations on 5 and 6 Oct 2026. Upcoming, not an assessment: day trip on Sat 7 Nov 2026 (about 6:00 to 18:00); the final list was posted 2026-11-02 and you are on it. The teacher wants the Deccan slides and the field guide (northern leg only) read before the trip. See [[maps/courses/landscape-evolution]], [[landscape-evolution/2026-10-30-field-trip-7-nov-safety-and-declaration]] and [[landscape-evolution/2026-11-02-field-trip-final-list]].

## Covered so far
- [[landscape-evolution/2026-08-11-qgis-and-topotoolbox-tutorials]]: GIS/DEM basics, QGIS with SAGA, topotoolbox workflow (GRIDobj, inpaintnans, FLOWobj, STREAMobj)
- [[landscape-evolution/2026-08-14-project-groups-and-brief]]: project format and what makes a good project question
- [[landscape-evolution/2026-09-03-himalaya-reading-and-slides]]: Himalayan mountain building and the Chamoli flood (readings and slides, not yet read)
- [[landscape-evolution/2026-10-24-geomorphic-features-of-the-deccan-traps-terrain]]: Deccan Traps terrain: Konkan belt, Western Ghats escarpment, plateaus, and the four controls (eruptive style, lithology, tectonics, monsoon erosion)
- [[landscape-evolution/2026-10-27-glacial-and-aeolian-slides]]: glacial and aeolian slides (90 MB file, not read)
- [[landscape-evolution/2026-10-30-field-trip-7-nov-safety-and-declaration]]: logistics and safety rules for the 7 Nov trip (no exam content)
- [[landscape-evolution/2026-11-02-deccan-next-field-guide]]: field guide for the trip: lava flow internal structure, Sahyadri Group stratigraphy and GPB markers, northern-leg stops NL1 to NL4
- [[landscape-evolution/2026-11-02-field-trip-final-list]]: final participant list (logistics only)
- [[landscape-evolution/2026-11-03-erosion-rate-debate-reading]]: reading list on late-Cenozoic erosion-rate change: Herman et al. (thermochronology), Schildgen et al. 2018 (spatial correlation bias), glacial erosion time-scale bias

## Must know
- GIS: a computer system to collect, manage, analyse and visualise geographic data. DEM: raster of elevations; in topotoolbox `DEM.Z` holds the value of each cell. (Classroom: QGIS and topotoolbox tutorial slides)
- Projections affect distance, shape, area and direction. DEM coordinates may be lat/lon or UTM depending on source. (Classroom: tutorial slides)
- topotoolbox workflow: `GRIDobj` (rasterise the .tif) → `inpaintnans` (fill missing values from neighbours) → `FLOWobj` (flow direction per cell, indices in `FD.ix`) → `STREAMobj` (stream network). `minarea` is the upslope area threshold that initiates a stream: smaller gives more, smaller streams. (Classroom: Topotoolbox_tut_shubhra.pdf)
- DEM sources: Copernicus GLO-30 (OpenTopography), ASTER V003/V004 (NASA EarthData); check the preview for cloud cover and voids. (Classroom: Topotoolbox_tut_shubhra.pdf)
- Good project: one interesting question on a piece of landscape, addressed with free data, own data, simple model runs, or both. (Classroom: 2026-08-14 post)
- Trap: from Swedish trappa, "stair". Successive lava flows → horizontal basalt layers → differential weathering/erosion → step-like slopes. (Classroom: Deccan Traps slides)
- Major features: Konkan Coastal Belt (under 100 km wide, under 100 m asl, short steep westward rivers with rapid headward incision, Panvel Flexure and N-S faults); Western Ghats Escarpment (about 1,200 km long, crest 500-1700 m, exposes stacked subhorizontal flows, major drainage divide, formed by post-Cretaceous rifting and scarp retreat); Deccan and Malwa plateaus. (Classroom: Deccan Traps slides)
- Four controls over about 66 Myr: (1) effusion rate and flow type, (2) lithology and differential resistance, (3) structural/tectonic uplift, (4) monsoonal climate and erosion, each with its resulting landform (table in the lecture note).
- Effusion rate to landform: under 10 m³/s compound hummocky pāhoehoe (tumuli, inflation clefts); 10-1,000 m³/s channelized, transitional pāhoehoe-to-ʻaʻā; 1,000-100,000+ m³/s massive sheet flows (plateaus, sheer escarpments).
- Columnar jointing comes from thermal contraction on cooling and controls cliff collapse and scarp retreat.
- Boles (interflow horizons) form either as paleosols from in-situ weathering of flow tops, or as ash-fall deposits. Intertrappean beds are 1 to over 20 m of sediment between flows.
- Eastward tilt gives an asymmetric divide: Godavari, Krishna and Bhima start near the Ghats crest and flow over 700 km east to the Bay of Bengal.
- Planation surfaces at about 1,330, 1,225, 1,000, 920, 700 and 600 m amsl, produced by etchplanation, scarp-retreat pediplanation, differential erosion and Quaternary block displacement. (The field guide gives three surfaces: Pune-Indore 550 ± 50 m, Ahmednagar 700 ± 50 m, highland about 1000 m in the north and about 1200 m in the south.)
- A frozen lava lobe has three layers: crust (vesicular, glassy tachylitic rind), core (crystallinity highest toward the medial cooling isotherm) and base (often with pipe vesicles). A lava flow consists of many lobes; a vent's many flows form a flow-field. Flow-field architecture is braided, ponded or tabular, set by emplacement rate, substrate topography and viscosity/strain. (Classroom: Deccan Next field guide)
- Lobe morphology (pāhoehoe, ʻaʻā, hummocky, sheet, slabby, rubbly) is a continuous variation of emplacement rate, vapour loss, lateral movement and cooling, not different "lava types"; lateral transitions are normal. Most flood-basalt lavas are pāhoehoe types. (Classroom: Deccan Next field guide)
- Field markers: the four giant plagioclase basalt (GPB, megacryst) horizons Thalghat (M1), Ghoti (M2), Giravali (M3) and Rajgad (M4) are regionally traceable. Giravali separates the Kalsubai and Lonavala subgroups where the Bhimashankar Member pinches out. (Classroom: Deccan Next field guide)
- Sahyadri Group order, bottom to top: Kalsubai (Salher, Nashik, Malshej), Lonavala (Indrayani, Bushe), Wai (Poladpur, Purandargarh, Mahabaleshwar). Ages about 66.4 Ma (Salher) to 65.4 Ma (Mahabaleshwar). (Classroom: Deccan Next field guide)
- Northern leg stops: NL1 Rajgurunagar Ghat (tabular sheet flow, FTB, trapped lobe, fracture zones versus cooling joints); NL2 Ane Ghat (braided lobate flows; Giravali megacryst flow; natural arch on a knick zone of an entrenched meander); NL3 Mandhol Dam (rejuvenated entrenched channel, fracture-controlled rectilinear drainage, hanging tributaries, taken as evidence of recent uplift of the Kanhoor block); NL4 Kukdi river bed at Nighoj (potholes over 10 m wide, channel along the Ghod Fault of the Kurduwadi Lineament, rejuvenation). (Classroom: Deccan Next field guide)
- Project reasoning pointers (2026-10-06): conserve mass and energy; balance forces and torques.
- Spatial correlation bias (Schildgen et al. 2018): of 30 locations with reported accelerated late-Cenozoic erosion, 23 show increases that result from combining data with disparate exhumation histories, which turns spatial erosion-rate variation into an apparent temporal increase; 4 are explained by changed tectonic boundary conditions; 3 record climatically induced acceleration from localized glacial valley incision. Conclusion: thermochronology currently has insufficient resolution to say whether late-Cenozoic climate change altered erosion rates globally. (Classroom: 2026-11-03 post; Nature 559, 89-93 abstract)
- The earlier compilation (Herman et al. 2013, as cited by Schildgen et al.) inferred a nearly twofold increase in erosion rate in mountainous landscapes over late-Cenozoic times; sedimentation-rate records are criticised for preservation biases, depositional hiatuses and varying measurement intervals. (Schildgen et al. 2018 abstract)

## Typical questions
Not known yet; no problem sheets or past papers have been posted. The Deccan lecture and the field guide suggest identification questions (recognise flow types, crust/core/base, flow-top breccia, columnar jointing, boles, GPB marker flows, knickpoints, natural arches, potholes, fracture-controlled drainage, planation surfaces in the field or in photos) and cause-to-landform questions; the teacher's 2026-10-24 post stresses applying concepts in the field, and the 2026-10-30 and 2026-11-02 posts ask students to read Shilpa's slides and the field guide's northern leg before the 7 Nov trip. The tutorials suggest practical DEM tasks (extract a stream network from the Bhima DEM and explain the effect of `minarea`); practise with [[landscape-evolution/2026-08-11-qgis-and-topotoolbox-tutorials]]. For the field side practise with [[landscape-evolution/2026-11-02-deccan-next-field-guide]]. The 2026-11-03 reading suggests discussion questions on whether erosion rates can be compared across time scales and sampling, and how to judge the two sides of the debate; practise with [[landscape-evolution/2026-11-03-erosion-rate-debate-reading]].

## Gaps
- Glacial and aeolian slides (l_glacial_aolian.pdf, 90 MB, posted 2026-10-27) not read: no definitions or landforms recorded yet. See [[landscape-evolution/2026-10-27-glacial-and-aeolian-slides]].
- Slides pre_ms_landscape_26.pdf (217 MB) not read. Week-1 slides (4 Aug), updated lecture slides (11 and 22 Aug) not accessible (Drive 404), so the lecture content of August is not in the notes.
- QGIS slides had mostly pictures: the basin-analysis steps (SAGA tools used) are not recorded. The Bhima DEM and campus-hills photo not viewed.
- The two linked papers (Himalayan mountain building review, Chamoli flood reconstruction) not read.
- Erosion-rate reading (2026-11-03): only the Schildgen et al. abstract was read (full text paywalled). The Herman et al. paper is not named or linked in the post (the 2013 Nature paper is my inference from Schildgen's reference list). The Science Advances paper on time-scale-dependent glacial erosion could not be opened (Forbidden), so its findings are not recorded.
- Deccan slides: figures, maps and photos were not in the extracted text; the area/volume labels (380,000 vs 500,000 km²; 193,000 vs 439,000 km³) and the Kalsubai height (1642 vs 1646-1660 m; the field guide says 1648 m) are inconsistent or unlabelled. Laterite capping slide has only a figure. Papers cited (Kale et al., Sheth 2020) not read.
- Field guide: it was written for a 2023 event; the teacher says only the northern leg applies, but the exact stops and route for 7 Nov are not stated (the post only says "northern leg"). Maps, photos and the morphology occurrence table symbols were not in the extracted text. The southern leg (Poladpur, Rajgad GPB, Mahabaleshwar sections) is not summarised.
- Final exam date and syllabus not announced.
<!-- /kurooto:exam-prep -->
