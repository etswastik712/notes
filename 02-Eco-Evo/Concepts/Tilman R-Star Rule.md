---
title: Tilman R-Star Rule
aliases: ["R*", "R-star rule", "Tilman's R* rule", "resource competition theory"]
subject: eco-evo
type: concept
scope: [taught, extra-beyond]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/beyond, src/slides, status/draft]
---
# Tilman R-Star Rule

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the rule as stated on the slide, and the experimental evidence of Tilman et al. (1981) ([[04-Competition_25-Aug_2026.pdf#page=8|slide 8]], [[04-Competition_25-Aug_2026.pdf#page=9|slide 9]])  ·  🔵 **extra · beyond:** derivation from a consumer-resource (chemostat) model; two-resource coexistence

> [!intuition] In one picture
> Whoever can get by on the least food wins: the species that can keep growing when the resource is scarcest will push the resource below the level at which anyone else can survive.

> [!key] Definition
> When species compete for one limiting resource at level $R$, each species $i$ has a break-even level $R_i^*$ at which its per capita growth is zero (growth $=$ loss). The species with the **lowest $R^*$** holds the resource at its own $R^*$, so all others have negative growth and are excluded (Tilman 1982).

## Derivation and a counterintuitive example
For per-capita growth $f_i(R)$ and loss $m_i$, species $i$ persists only if $f_i(R)>m_i$; alone it draws the resource down to $R^*_i=f_i^{-1}(m_i)$. For a Monod response $f(R)=\mu R/(k+R)$: $R^*=mk/(\mu-m)$. With two species the one with the lower $R^*$ holds $R$ at its own $R^*$, where the other has $f_j(R)<m_j$ and declines.

> [!example] The fast grower loses
> $m=0.2$. A: $\mu=0.8$, $k=2$: $R^*_A=0.667$. B: $\mu=0.6$, $k=1$: $R^*_B=0.500$. At $R=10$, A grows faster (0.667 against 0.545). In a chemostat with inflow 10, B draws $R$ down to 0.5 where A's growth is $0.8\times0.5/2.5=0.16<0.20$. A is excluded; B settles at $N_B^*=10-0.5=9.5$. Tilman's slide experiments (*Asterionella* and *Synedra* on silicate) show one diatom displacing the other, as the species with the lower silicate $R^*$ should (the slide notes its legend is inverted).

> [!extra-beyond]- 🔵 Extra (beyond): two resources
> With two essential resources a pair of species can coexist if each is limited by a *different* resource and each consumes more of the resource that limits *it* (Tilman 1982): a trade-off in requirements replaces niche separation in space or time. The $n$-species, $n$ factors form of [[Competitive Exclusion Principle]] again.

> [!pitfall] What $R^*$ needs
> Steady state, a single limiting resource, and consumers that depress the resource; it is silent about interference and about fluctuating supply. Extra supply does not change who wins (it raises $N^*=y(R_{in}-R^*)$, not the ranking), a point for lake management ([[Nutrient Limitation]], [[Carrying Capacity]]).

Used in: [[EE04 Competition and Invasions]]. Related: [[Competitive Exclusion Principle]] · [[Nutrient Limitation]] · [[Ecological Niche]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
