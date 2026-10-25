---
title: Tiger Population Surveys
aliases: ["camera trap", "non-invasive survey", "pugmark census"]
subject: eco-evo
type: concept
scope: [taught, extra-book]
by: [slides, karanth]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/book, src/slides, src/paper, status/draft]
---
# Tiger Population Surveys

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the slide notes that after 2006 better surveys were done using camera traps (2018: 2,461 unique tiger photographs) ([[07_Conservation Biology.pdf#page=26|slide 26]])  ·  🟡 **extra · book:** Karanth and Nichols (2010), 'Non-invasive survey methods for assessing tiger populations'

> [!intuition] In one picture
> Count tigers without touching them: each tiger has unique stripes, so photographs act as marks.

> [!key] Definition
> Counting by signs (pugmarks) cannot separate individuals reliably; **camera-trap capture-recapture** photographs striped flanks and treats individuals as marked animals ([[Mark-Recapture Estimation]]), allowing for unequal capture probabilities, giving density estimates with confidence intervals (2018 national estimate 2,967, range 2,603-3,346). Sign-based occupancy models cover large areas.

## From pugmarks to camera traps
Karanth and Nichols (2010): tigers are secretive, nocturnal and wide-ranging (home ranges 15 to over 1,000 km²; 5–30 km a day) at low densities (at best 12–18 per 100 km²), in 76–159 scattered populations over about 1.1 million km² across 13 countries; distance sampling and radio-telemetry cannot supply abundance. Prey-based rule of thumb: one tiger per 500 prey animals.

> [!example] The estimator in practice
> **Pugmark census:** abandoned after about 25 years because prints vary with substrate, moisture and pace; it ignores $p$. **Camera-trap capture-recapture:** a closed survey of **30–60 days**; the stripe pattern identifies each tiger; traps spaced so no tiger has zero chance (female home ranges 15–500 km² set the spacing); data form a capture-history matrix analysed in CAPTURE or MARK; the **heterogeneity model $M_h$** is usually best. **Density:** $\hat N$ over the trap polygon plus a buffer of **half the mean maximum distance moved** (an ad hoc step the authors call a weak link). Examples: Nagarahole 11.9 tigers per 100 km² against 11.6 predicted from prey; Kaziranga 16.8 against 12.8. National 2018: 2,967 tigers (2,603–3,346) from 2,461 unique photographs (slide 26).
> **Beyond one season:** open models over years give annual survival (about 0.77 in the Nagarahole series) and recruitment. **Occupancy** surveys (patches with sign; detection probability of sign) cover large landscapes when counts are impossible.

> [!pitfall] Indices are not abundances
> Track and scat encounter rates correspond poorly to camera-trap densities across reserves (the authors' table of seven reserves), so they can be used within a site over time but not across sites. Counts must always carry a detection probability: $N=C/p$ ([[Mark-Recapture Estimation]]).

Context: [[Project Tiger]]; analysis and risk: [[Minimum Viable Population]].

Used in: [[EE07 Conservation Biology]]. Related: [[Mark-Recapture Estimation]] · [[Project Tiger]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
