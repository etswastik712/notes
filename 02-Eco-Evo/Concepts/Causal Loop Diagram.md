---
title: Causal Loop Diagram
aliases: ["signed digraph", "feedback loop sign rule", "reinforcing loop", "balancing loop"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Causal Loop Diagram

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the rule on the slide: multiply the signs to get the indirect effect of two components ([[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=16|slide 16]])

> [!intuition] In one picture
> Draw boxes for the variables and signed arrows for 'more of A gives more (+) or less (−) of B'. Chains multiply their signs; a loop with an even number of negative arrows reinforces itself.

> [!key] Definition
> In a **causal loop diagram** each arrow carries a sign ($+$ if the target moves in the same direction as the source, $-$ if opposite). The net effect of a chain is the *product* of its signs. A loop whose product is $+$ is a **reinforcing (positive) feedback**; $-$ is a **balancing (negative) feedback**. In shallow lakes, vegetation $\xrightarrow{-}$ turbidity $\xrightarrow{-}$ vegetation is $(-)(-)=+$.

## Reading and computing loop signs
Each arrow carries a sign: $+$ if the target changes in the same direction as the source, $-$ if opposite. A path's sign is the product of its arrows; a loop with an even number of $-$ arrows is **reinforcing** (positive feedback), with an odd number **balancing** (negative feedback). Reinforcing loops give runaway or alternative states; balancing loops give stability.

> [!example] Three loops from the vault
> **Planck response:** temperature $\xrightarrow{+}$ outgoing radiation $\xrightarrow{-}$ temperature: $(+)(-)=-$, balancing. **Ice-albedo:** temperature $\xrightarrow{-}$ ice cover $\xrightarrow{+}$ albedo $\xrightarrow{-}$ absorbed sunlight $\xrightarrow{+}$ temperature: $(-)(+)(-)(+)=+$, reinforcing ([[Ice-Albedo Feedback]], [[Climate Feedback Factor]]). **Shallow lake:** turbidity $\xrightarrow{-}$ light $\xrightarrow{+}$ vegetation $\xrightarrow{-}$ resuspension $\xrightarrow{+}$ turbidity: $(-)(+)(-)(+)=+$, reinforcing; the direct pair vegetation $\xrightarrow{-}$ turbidity, turbidity $\xrightarrow{-}$ vegetation also gives $+$.

> [!pitfall] The sign is not the strength
> A positive loop alone does not guarantee instability: the **gain** (the product of the strengths, such as the climate feedback factor $f$) decides whether the loop converges ($f<1$) or runs away ($f\ge1$). Time delays can turn a balancing loop into oscillation ([[Logistic Growth]], delayed). In Scheffer's slide-16 network (turbidity, algae, nutrients, vegetation, waves, resuspended sediment, depth, fish, zooplankton, allelopathic substances) "multiply the signs" to read the net effect of any path, but several paths between two nodes can disagree and then the magnitudes matter.

Use: [[Shallow Lake Regime Shift]], [[Internal Phosphorus Loading]] (a reinforcing loop through anoxia).

Used in: [[EE06 Eutrophication and Alternative Stable States]]. Related: [[Shallow Lake Regime Shift]] · [[Ice-Albedo Feedback]] · [[Internal Phosphorus Loading]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
