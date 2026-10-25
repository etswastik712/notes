---
title: Modelling Relation
aliases: ["Rosen modelling relation", "modeling relationship"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Modelling Relation

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** Rosen's modelling relationship (Simeonov 2010, Fig. 1) as the frame for the whole lecture ([[04_PopDyn_Chaos_18Aug_2026.pdf#page=5|slide 5]])

> [!intuition] In one picture
> A model is a second system built so that its *reasoning* mirrors nature's *causation*. We translate nature in, reason inside the model, translate the answer back, and check that it matches what nature does.

> [!key] Definition
> In Rosen's **modelling relation** a natural system $N$ (events $A\to B$ linked by causal entailment) is mapped by an *encoding* to a formal system (states $A'\to B'$ linked by inference) and the result is *decoded* back. The model is good when the diagram commutes: $\mathrm{decode}(\mathrm{infer}(\mathrm{encode}(A)))\approx B$.

## The diagram as a test
Write $c$ for causal entailment in the natural system $N$ (what the world does), $\varepsilon$ for encoding $N\to F$, $i$ for inference inside the formal system $F$, and $\delta$ for decoding $F\to N$. A model is good when the diagram **commutes approximately**: $\delta\circ i\circ\varepsilon\approx c$. Two kinds of failure are different in kind and are repaired differently. *Encoding failures* drop a variable that matters (space, age structure, delays, integer numbers). *Inference failures* use an equation form that does not follow from the assumptions.

> [!example] One model, three checks
> Exponential growth: $\varepsilon$ = count 996 plants, estimate $\lambda=2.4177$; $i$: $N_t=N_0\lambda^t$; $\delta$: "1.16 million after 8 years". The prediction fails because $\varepsilon$ left out density dependence ([[Logistic Growth]]), not because the arithmetic is wrong. The Hassell model fitted with one lag finds simple damping where $\varepsilon$ dropped lagged densities ([[Time-Series Reconstruction]]); a real-valued chaotic map is an encoding error about whole animals ([[Lattice Effect]]).

> [!pitfall] A good fit is not a true model
> Agreement along the loop shows the model is *adequate for that purpose*, not that its parts are real. Different formal systems can fit the same data; comparing them is model selection ([[Akaike Information Criterion]]) and, in the vault's language, [[Strong Inference]]. The ideal of a single nomothetic law ([[Nomothetic versus Idiographic Science]]) is rare in ecology; the loop is how oversimplified models are used honestly.

The same picture covers the vault's physics: the energy-balance model of [[CL01 Earth as a System]] is an $\varepsilon$ that deliberately drops almost everything.

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Exponential Growth]] · [[Lattice Effect]] · [[Strong Inference]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
