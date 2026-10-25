---
title: Reanalysis Data
aliases: [reanalysis, ERA5]
subject: climate
type: concept
scope: [extra-beyond]
by: [web]
status: draft
tags: [subject/climate, type/concept, extra/beyond, src/web, status/draft]
---
# Reanalysis Data

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** entire note (the course uses ERA5 maps from Climate Reanalyzer without explaining reanalysis, 21 Oct p4–19).

> [!intuition] In one picture
> Observations are GPS fixes along a journey; a weather model is the road map. A reanalysis uses the map to fill in everything between the fixes, so you get a continuous, physically consistent picture of the atmosphere at every place and time.

> [!key] Definition
> A **reanalysis** is a long, consistent record of the atmosphere produced by running a *fixed* numerical weather-prediction model and **assimilating** all available observations (surface stations, radiosondes, aircraft, satellites) at each analysis time. It gives gridded $u,v,w,T,q,p,\dots$ everywhere and everywhen, including unobserved places.

- **ERA5** (ECMWF, 0.25°–0.5° grid, hourly, 1940–present) is the dataset behind the "Climate Reanalyzer" maps (University of Maine) shown in class.
- **Strengths:** complete coverage; consistent physics; derived fields such as vertical velocity $w$ and the energy budget are available.
- **Cautions:** quantities that are not directly observed (e.g. $w$, precipitation, cloud) depend on the model; trends can be affected by changes in the observing system.
- **Climatologies** (annual, DJF, JJA) in [[Zonal-Mean Zonal Wind]] are averages of reanalysis fields.

Links: [[CL14 Observed Winds - Jets, Trades and the ITCZ]], [[CL02 Observing Global Temperature]] (temperature measurement and reanalysis), [[Probability - Course Map]] (data assimilation is Bayesian estimation).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
