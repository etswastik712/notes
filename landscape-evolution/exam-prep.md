---
id: landscape-evolution/exam-prep
aliases: ["Exam prep: Landscape Evolution (c41 - EC2123)"]
tags: [exam-prep, landscape-evolution]
trust_tier: agent_written
---

# Exam prep: Landscape Evolution (c41 - EC2123)

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
Not announced yet. Past: mid-sem (open-notes, handwritten notes only, calculator allowed, no sharing; date not stated in Classroom) and project presentations on 5 and 6 Oct 2026. Upcoming, not an assessment: day trip on Sat 7 or 14 Nov 2026 (date to be fixed). See [[maps/courses/landscape-evolution]].

## Covered so far
- [[landscape-evolution/2026-08-11-qgis-and-topotoolbox-tutorials]]: GIS/DEM basics, QGIS with SAGA, topotoolbox workflow (GRIDobj, inpaintnans, FLOWobj, STREAMobj)
- [[landscape-evolution/2026-08-14-project-groups-and-brief]]: project format and what makes a good project question
- [[landscape-evolution/2026-09-03-himalaya-reading-and-slides]]: Himalayan mountain building and the Chamoli flood (readings and slides, not yet read)
- [[landscape-evolution/2026-10-24-geomorphic-features-of-the-deccan-traps-terrain]]: Deccan Traps terrain: Konkan belt, Western Ghats escarpment, plateaus, and the four controls (eruptive style, lithology, tectonics, monsoon erosion)
- [[landscape-evolution/2026-10-27-glacial-and-aeolian-slides]]: glacial and aeolian slides (90 MB file, not read)

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
- Planation surfaces at about 1,330, 1,225, 1,000, 920, 700 and 600 m amsl, produced by etchplanation, scarp-retreat pediplanation, differential erosion and Quaternary block displacement.
- Project reasoning pointers (2026-10-06): conserve mass and energy; balance forces and torques.

## Typical questions
Not known yet; no problem sheets or past papers have been posted. The Deccan lecture suggests identification questions (recognise flow types, jointing, boles, knickpoints, potholes, planation surfaces in the field or in photos) and cause-to-landform questions; the teacher's 2026-10-24 post stresses applying concepts in the field. The tutorials suggest practical DEM tasks (extract a stream network from the Bhima DEM and explain the effect of `minarea`); practise with [[landscape-evolution/2026-08-11-qgis-and-topotoolbox-tutorials]].

## Gaps
- Glacial and aeolian slides (l_glacial_aolian.pdf, 90 MB, posted 2026-10-27) not read: no definitions or landforms recorded yet. See [[landscape-evolution/2026-10-27-glacial-and-aeolian-slides]].
- Slides pre_ms_landscape_26.pdf (217 MB) not read. Week-1 slides (4 Aug), updated lecture slides (11 and 22 Aug) not accessible (Drive 404), so the lecture content of August is not in the notes.
- QGIS slides had mostly pictures: the basin-analysis steps (SAGA tools used) are not recorded. The Bhima DEM and campus-hills photo not viewed.
- The two linked papers (Himalayan mountain building review, Chamoli flood reconstruction) not read.
- Deccan slides: figures, maps and photos were not in the extracted text; the area/volume labels (380,000 vs 500,000 km²; 193,000 vs 439,000 km³) and the Kalsubai height (1642 vs 1646-1660 m) are inconsistent or unlabelled. Laterite capping slide has only a figure. Papers cited (Kale et al., Sheth 2020) not read.
- No notes yet on what was taught in the field trip of 2026-10-24.
- Final exam date and syllabus not announced.
<!-- /kurooto:exam-prep -->
