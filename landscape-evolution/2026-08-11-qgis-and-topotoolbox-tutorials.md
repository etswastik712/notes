---
id: landscape-evolution/2026-08-11-qgis-and-topotoolbox-tutorials
aliases: [QGIS and topotoolbox tutorials]
tags: [landscape-evolution, gis, dem, tutorial]
trust_tier: agent_written
---

# QGIS and topotoolbox tutorials (2026-08-11)

Student demos from the week-1 tutorials, plus the tutorial-prep posts of 4 and 5 Aug. Both slide sets are short; slides that were pictures only (QGIS interface, DEM figures, projection examples) had no extractable text.

## Covered

**Terminology**
- *GIS (Geographic Information System)*: a computer system used to collect, manage, analyse and visualise geographic data. (Classroom: Introduction_to_QGIS_aju.pptx)
- *DEM (Digital Elevation Model)*: a raster of elevations; in topotoolbox, `DEM.Z` stores the value of each grid cell (elevation here). (Classroom: Introduction_to_QGIS_aju.pptx; Topotoolbox_tut_shubhra.pdf)
- *Map projection*: the QGIS slides list four properties a projection affects: distance, shape, area, direction. (Classroom: Introduction_to_QGIS_aju.pptx)
- *Cell referencing*: depending on the DEM source, coordinates are lat/lon or UTM. (Classroom: Topotoolbox_tut_shubhra.pdf)

**QGIS (Aju): introduction and basic basin analysis using a DEM**
- Install from qgis.org. Interface parts named: Browser Panel, Layer Panel, Menu Bar, Map View, Tool Bar, Tool Box; plugins are managed separately.
- The SAGA toolbox for QGIS Processing (https://github.com/agiudiceandrea/qgis-processing-saga-nextgen) is needed for the basin analysis; the teacher asked for it before the Thursday tutorial.
- Then: load a DEM (the posted `Bhima.tif`), and mind the projection.

**topotoolbox in MATLAB (Shubhra)**
- Requirements: a suitable DEM as `.tif` (not `.tiff`); MATLAB 2023b or newer; toolboxes: Image Processing, Mapping and Optimization (marked very important); Statistics and Machine Learning (maybe not needed); Parallel Computing.
- Where to get DEMs: Copernicus GLO-30 via OpenTopography; ASTER DEM V004/V003 via NASA EarthData Search (choose temporal and spatial range).
- Beware shoddy DEMs: check the preview in EarthData Search; no cloud cover and no obvious gaps or voids.
- Reading: the topotoolbox blog (https://topotoolbox.wordpress.com/) and MATLAB's `help` command.
- Workflow:
  1. `GRIDobj`: rasterises the DEM (keep the .tif in the same folder as the MATLAB file).
  2. `inpaintnans`: interpolates missing values from surrounding grid values.
  3. `FLOWobj`: derives and stores the flow direction of each cell (single-direction flow, used to derive stream networks); values are stored as indices, accessible with `FD.ix`.
  4. `STREAMobj`: connects flow directions into stream networks. The `minarea` parameter is the upslope threshold area that initiates a stream: smaller `minarea` gives more, smaller streams; larger gives fewer.

## From the post
- 2026-08-04: "The slides for the first week are attached. Please keep exploring google-earth, qgis, and try the suggested exercises. Those who have access to Matlab (IISER has a licensed version) can also explore topotoolbox, which is very powerful. There are some local experts amongst us, whom I have requested to give brief demos during the tutorial on Friday. We'll also see have time for you people to discuss your finding - keep some slides ready if you have things to show." - Argha
- 2026-08-04: "Did anybody notice these small hills that are popping up literally everywhere in our campus, apparently in response to monsoon rains?! The processes operating and their shape is quite interesting!!" (photo attached)
- 2026-08-05: "As discussed, please bring your laptop with QGIS installed for the Tutorial on Thursday. Having this SAGA toolbox https://github.com/agiudiceandrea/qgis-processing-saga-nextgen will be useful. Download the attached dem. If you have any trouble in installing etc, please talk to people in my Lab (fifth floor, main building)"
- 2026-08-11: "presentation sl presentations of Aju (QGIS) & Shubhra (topotoolbox); updated lecture slides"

## Files
- [Topotoolbox_tut_shubhra.pdf](https://drive.google.com/file/d/1wfPz9TO8GO7e1t8TnztOxyFttcd3Dh5t/view?usp=drive_web)
- [Introduction_to_QGIS_aju.pptx](https://drive.google.com/file/d/1a5Us2ciz0zDBWshV0ecmReNV13VMUZK8/view?usp=drive_web)
- [Bhima.tif](https://drive.google.com/file/d/1xodK21gsyqPn1Z6WOT66aBf6Sin8ompC/view?usp=drive_web): DEM for the tutorial; binary raster, not read.
- [IMG_7687.heic](https://drive.google.com/file/d/1b63QsQ303stRGi_QgSbURbepGirM4yMw/view?usp=drive_web): photo of small campus hills; image, not viewed.
- Week-1 slides (https://drive.google.com/open?id=1dbCGqCtFprkHx70g6z1uiezJRz605YRV) and "updated lecture slides" of 11 Aug (https://drive.google.com/open?id=1IdHiPVJvXIJAiCSkgeNI63JWnzsEsUBc): not readable, Drive access returned 404.

## Related
- [[landscape-evolution/2026-10-24-geomorphic-features-of-the-deccan-traps-terrain]]: the Bhima, Krishna and Godavari headwaters there are the kind of drainage you can extract from a DEM with `FLOWobj`/`STREAMobj`.
- [[landscape-evolution/2026-08-14-project-groups-and-brief]]: the project is expected to use freely available data such as DEMs.
