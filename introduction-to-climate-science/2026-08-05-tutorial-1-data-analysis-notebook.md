---
id: introduction-to-climate-science/2026-08-05-tutorial-1-data-analysis-notebook
aliases: [Tutorial 1 notebook, Intro_to_climate_T1]
tags: [climate, introduction-to-climate-science, tutorial, python]
trust_tier: agent_written
---

# Tutorial 1: data-analysis notebook (Python)

## Covered
Data-analysis exercise for Lectures 1–2, run step by step in Google Colab. Drag the notebook and both CSV files into Colab. The tutorial runs on Friday: about 20 min of programming, 20 min of numerical problems, 15 min of doubts on L1–L2. The programming is "just for fun and some practice – not part of the formal course content".

Notebook `Intro_to_climate_T1.ipynb` (numpy, pandas, matplotlib, seaborn, scikit-learn):
1. Load `t2m_hourly.csv` (hourly 2 m temperature, ERA5-style reanalysis, from 1940-01-01; values in kelvin) and convert to °C by subtracting 273.15.
2. Group by hour, month and year to get the mean daily cycle, the annual cycle, and yearly means with $\pm$ std error bars.
3. Fit a line to the yearly means with `LinearRegression` (years 1940–2026); the slope is the warming rate per year and the intercept is the fitted 1940 mean.
4. Load `t_ice_core.csv` (columns `Age_yr`, `Temperature`) and plot temperature against age (kyr) on long time scales; smooth with a 50-point rolling mean.
5. Plots for the lecture slides: median/interquartile-band (25th–75th percentile) plots of hour-of-day, day-of-year, month and year variation, with 2025 (and 6 August 2025) overlaid; variation over one day, one month (daily resample) and one year (30-day resample) for 2020.

Patterns practised: `groupby` on a datetime index, resampling, quantile bands, linear regression, rolling means. These are the "folding" and smoothing ideas from Lecture 2.

## From the post
Post (2026-08-05): "Uploading 1. the problem set, 2. data-analysis exercise (a pynb notebook file+2 csv data files; drag all of them into google collab, and run the python nootebook step by step), and 3. A quick notes explaining the slides..." Post of 2026-08-06 about the first tutorial: "first tutorial will consist of programming exercises (~20mins), numerical problems (~20 mins), and also any doubts/discussions on L1&2 (~15mins)... The programming exercises are just for fun and some practice – not part of the formal course content." Also: sit next to a friend if you have no laptop, and comment on the post if files cannot be accessed.

## Files
- [Intro_to_climate_T1.ipynb](https://drive.google.com/file/d/1x54xViojBeTiOxolQQVTOWu1ZdUawdZr/view?usp=drive_web): read in full.
- [t2m_hourly.csv](https://drive.google.com/file/d/1DvDnxsK-IpsjQcKCvbyUiHOL5qBFx7Pb/view?usp=drive_web): 22.5 M characters; only the first rows were read (hourly values from 1940-01-01, about 287–302 K in January).
- [t_ice_core.csv](https://drive.google.com/file/d/1xC4Kratr3ignEw_A_8O_7M7vIu9KeMv-/view?usp=drive_web): about 90 k characters; first 20 000 read (age in years from ~38 yr with temperature anomalies in °C; the first 12 kyr hover near 0 °C, then fall to about −9 to −10 °C by ~18–30 kyr). Rest not read.

## Related
- [[introduction-to-climate-science/2026-08-05-lectures-1-2-intro-and-global-mean-temperature]]: Lecture 2 methods (folding, smoothing, isotopic thermometers)
- [[01-climate/cl02-observing-global-temperature]]: their chapter on observing temperature
- [[01-climate/concepts/isotopic-thermometers]]: ice-core temperature proxy

<!-- kurooto:materialb8712e40 -->
Textbook: [[introduction-to-climate-science/books/t2m-hourly|t2m_hourly]] (its concepts are listed there).
<!-- /kurooto:materialb8712e40 -->

<!-- kurooto:materialf1cd16da -->
## Concepts in Intro_to_climate_T1
[[zettel/multi-scale-temperature-variability]], [[zettel/secular-temperature-trend-estimation]]
<!-- /kurooto:materialf1cd16da -->

<!-- kurooto:material9710f5f3 -->
## Concepts in t_ice_core
(none new)
<!-- /kurooto:material9710f5f3 -->
