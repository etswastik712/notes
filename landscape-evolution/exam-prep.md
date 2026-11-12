---
id: landscape-evolution/exam-prep
aliases: ["Exam prep: Landscape Evolution (c41 - EC2123)"]
tags: [exam-prep, landscape-evolution]
trust_tier: agent_written
---

# Exam prep: Landscape Evolution (c41 - EC2123)

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
Final project presentation: Monday 16 Nov 2026, 4:15 PM, Seminar Room 32 (the post says "16th Oct", which isn't a Monday; read as 16 Nov, please confirm). Be there by 4 pm and test your slides (setup time is cut from your slot). 9 minutes, strictly under 10 slides, then 5 minutes of Q&A. Your group's problem in the order sheet: meandering and braiding rivers in the IGP. The talks are announced to the whole ECS department. Final exam: not announced yet. Past: mid-sem (open-notes, handwritten notes only, calculator allowed, no sharing; date not stated), first project presentations on 5 and 6 Oct 2026, and the day trip on Sat 7 Nov 2026 (northern leg). The teacher said a Google Sheet for pothole data and a Drive folder for photos would be added around Mon 9 Nov; neither is posted yet. See [[maps/courses/landscape-evolution]], [[landscape-evolution/2026-08-14-project-groups-and-brief]], [[landscape-evolution/2026-10-30-field-trip-7-nov-safety-and-declaration]] and [[landscape-evolution/2026-11-02-field-trip-final-list]].

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
- [[landscape-evolution/2026-11-10-knickpoint-animation-topotoolbox-getlocation]]: topotoolbox blog post and GIF on knickpoint migration under the stream power model (chi, getlocation)
- 2026-11-10 announcement (presentation logistics): no separate note, see Next assessment above.

## Must know
- GIS: a computer system to collect, manage, analyse and visualise geographic data. DEM: raster of elevations; in topotoolbox `DEM.Z` holds the value of each cell. (Classroom: QGIS and topotoolbox tutorial slides)
- Projections affect distance, shape, area and direction. DEM coordinates may be lat/lon or UTM depending on source. (Classroom: tutorial slides)
- topotoolbox workflow: `GRIDobj` (rasterise the .tif) → `inpaintnans` (fill missing values from neighbours) → `FLOWobj` (flow direction per cell, indices in `FD.ix`) → `STREAMobj` (stream network). `minarea` is the upslope area threshold that initiates a stream: smaller gives more, smaller streams. (Classroom: Topotoolbox_tut_shubhra.pdf)
- DEM sources: Copernicus GLO-30 (OpenTopography), ASTER V003/V004 (NASA EarthData); check the preview for cloud cover and voids. (Classroom: Topotoolbox_tut_shubhra.pdf)
- Knickpoint: an abrupt change in channel gradient. In the stream power model with $n = 1$, knickpoints migrate upstream at a speed set by upslope area (celerity proportional to $A^m$), so the distance travelled in a given time is proportional to $\chi$; actual celerity also needs the erosion efficiency $K$. In natural landscapes $m$ is roughly 0.3 to 0.8. (Classroom: 2026-11-10 post; topotoolbox blog "Location, location, location!", read in full)
- topotoolbox `getlocation(S, ...)` returns the places along a stream network where a measured quantity (distance from outlet by default, $\chi$, $k_{sn}$, elevation) takes given values; used to place expected knickpoints. (topotoolbox blog, linked in the 2026-11-10 post)
- Good project: one interesting question on a piece of landscape, addressed with free data, own data, simple model runs, or both. (Classroom: 2026-08-14 post)
- Presentation format (2026-11-10): 9 minutes, strictly under 10 slides, then 5 minutes of Q&A. (Classroom: 2026-11-10 post)
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
- Project talk (16 Nov): a 9-minute talk under 10 slides, then 5 minutes of Q&A. Expect questions on the problem statement, data source and method, results, and the reasoning checks the teacher stressed (mass and energy conservation, force and torque balance). Practise with [[landscape-evolution/2026-08-14-project-groups-and-brief]].
- No problem sheets or past papers have been posted for the final exam. The Deccan lecture and the field guide suggest identification questions (recognise flow types, crust/core/base, flow-top breccia, columnar jointing, boles, GPB marker flows, knickpoints, natural arches, potholes, fracture-controlled drainage, planation surfaces in the field or in photos) and cause-to-landform questions; the teacher's 2026-10-24 post stresses applying concepts in the field, and the earlier posts asked students to read Shilpa's slides and the field guide's northern leg before the 7 Nov trip.
- The teacher's 2026-11-07 post says pothole-related data will be shared (Google Sheet), so pothole questions (size, channel control by the Ghod Fault, rejuvenation at NL4) may come from your own field data.
- The tutorials suggest practical DEM tasks (extract a stream network from the Bhima DEM and explain the effect of `minarea`); practise with [[landscape-evolution/2026-08-11-qgis-and-topotoolbox-tutorials]]. For the field side practise with [[landscape-evolution/2026-11-02-deccan-next-field-guide]].
- Knickpoint tasks: explain why knickpoint travel distance is proportional to $\chi$ under the linear stream power model, and locate expected knickpoints on a stream network with `getlocation`; practise with [[landscape-evolution/2026-11-10-knickpoint-animation-topotoolbox-getlocation]].
- The 2026-11-03 reading suggests discussion questions on whether erosion rates can be compared across time scales and sampling, and how to judge the two sides of the debate; practise with [[landscape-evolution/2026-11-03-erosion-rate-debate-reading]].

## Gaps
- Date of the project presentation: the 2026-11-10 post says "16th Oct" but also "next Monday"; read as Mon 16 Nov. Confirm with the teacher or the order sheet.
- The order sheet (spreadsheet of groups and slots) lists project problems only; the time slot for your group is not in the text that was read.
- Glacial and aeolian slides (l_glacial_aolian.pdf, 90 MB, posted 2026-10-27) not read: no definitions or landforms recorded yet. See [[landscape-evolution/2026-10-27-glacial-and-aeolian-slides]].
- Slides pre_ms_landscape_26.pdf (217 MB) not read. Week-1 slides (4 Aug), updated lecture slides (11 and 22 Aug) not accessible (Drive 404), so the lecture content of August is not in the notes.
- QGIS slides had mostly pictures: the basin-analysis steps (SAGA tools used) are not recorded. The Bhima DEM and campus-hills photo not viewed.
- The two linked papers (Himalayan mountain building review, Chamoli flood reconstruction) not read.
- Erosion-rate reading (2026-11-03): only the Schildgen et al. abstract was read (full text paywalled). The Herman et al. paper is not named or linked in the post (the 2013 Nature paper is my inference from Schildgen's reference list). The Science Advances paper on time-scale-dependent glacial erosion could not be opened (Forbidden), so its findings are not recorded.
- Deccan slides: figures, maps and photos were not in the extracted text; the area/volume labels (380,000 vs 500,000 km²; 193,000 vs 439,000 km³) and the Kalsubai height (1642 vs 1646-1660 m; the field guide says 1648 m) are inconsistent or unlabelled. Laterite capping slide has only a figure. Papers cited (Kale et al., Sheth 2020) not read.
- Field guide: it was written for a 2023 event; the teacher says only the northern leg applies, but the exact stops and route for 7 Nov are not stated. Maps, photos and the morphology occurrence table symbols were not in the extracted text. The southern leg (Poladpur, Rajgad GPB, Mahabaleshwar sections) is not summarised.
- Post-trip material: the pothole data sheet and the photo Drive folder promised for about 9 Nov are not posted yet; the one attached photo (WhatsApp image, 7 Nov) was not viewed. Add your own field observations from the trip to the notes once you have them.
- Knickpoint GIF (visualfun.gif, 2026-11-10) not viewed. The post is addressed to "soumil, deep and their group", so it may not be meant for your group; it is filed anyway as course material.
- Final exam date and syllabus not announced.
<!-- /kurooto:exam-prep -->
