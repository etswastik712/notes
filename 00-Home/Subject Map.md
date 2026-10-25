---
title: Subject Map
tags: [meta, type/moc]
---
# Subject Map

How the subjects in this repository relate, and why. Interactive version: [[Subject Map.canvas|Subject Map (canvas)]]. Strength 3 = a topic cannot be understood without the other; 2 = regular exchange of tools or examples; 1 = occasional link.

**Reading the map.** Climate, Thermodynamics and Ecology/Evolution form the first phase because they share the most tools (stability and feedback, radiation, probability); Quantum Mechanics, Group Theory and Inorganic Chemistry form a tight cluster; Neuroscience is the most isolated subject (a single paper so far) and is scheduled last.

| Subject A | Subject B | Strength | Why they connect |
|---|---|---|---|
| [[Climate - Course Map\|Climate]] | [[Evolution of Earth and Life - Course Map\|Evolution of Earth and Life]] | 3 | paleoclimate, snowball Earth, faint young Sun, carbon cycle |
| [[Climate - Course Map\|Climate]] | [[Bistability and Tipping Points\|Foundations (shared tools)]] | 3 | stability, linearisation, rotating frames, Jensen |
| [[Climate - Course Map\|Climate]] | [[Thermodynamics - Course Map\|Thermodynamics and Stat. Mech.]] | 3 | radiation laws, gas law, adiabats, latent heat, entropy |
| [[Ecology and Evolution - Course Map\|Ecology and Evolution]] | [[Evolution of Earth and Life - Course Map\|Evolution of Earth and Life]] | 3 | macroevolution, extinctions, conservation |
| [[Ecology and Evolution - Course Map\|Ecology and Evolution]] | [[Bistability and Tipping Points\|Foundations (shared tools)]] | 3 | fixed points, stage-structured matrices, bistable lakes |
| [[Ecology and Evolution - Course Map\|Ecology and Evolution]] | [[Probability - Course Map\|Probability]] | 3 | stochastic population models, demography, Markov chains |
| [[Group Theory - Course Map\|Group Theory]] | [[Inorganic Chemistry - Course Map\|Inorganic Chemistry]] | 3 | MO theory, vibrational selection rules, crystal field |
| [[Probability - Course Map\|Probability]] | [[Proofs, Analysis and Topology - Course Map\|Proofs, Analysis and Topology]] | 3 | measure, convergence, limit theorems |
| [[Quantum Mechanics - Course Map\|Quantum Mechanics]] | [[Inorganic Chemistry - Course Map\|Inorganic Chemistry]] | 3 | atomic and molecular orbitals |
| [[Quantum Mechanics - Course Map\|Quantum Mechanics]] | [[Group Theory - Course Map\|Group Theory]] | 3 | symmetry, angular momentum, representations |
| [[Quantum Mechanics - Course Map\|Quantum Mechanics]] | [[Waves - Course Map\|Waves]] | 3 | wave mechanics, superposition, Schrodinger equation |
| [[Thermodynamics - Course Map\|Thermodynamics and Stat. Mech.]] | [[Probability - Course Map\|Probability]] | 3 | statistical mechanics is probability: ensembles, entropy |
| [[Thermodynamics - Course Map\|Thermodynamics and Stat. Mech.]] | [[Quantum Mechanics - Course Map\|Quantum Mechanics]] | 3 | photon statistics, Planck law, quantised energy levels |
| [[Climate - Course Map\|Climate]] | [[Inorganic Chemistry - Course Map\|Inorganic Chemistry]] | 2 | atmospheric chemistry, ozone, carbonate system |
| [[Climate - Course Map\|Climate]] | [[Ecology and Evolution - Course Map\|Ecology and Evolution]] | 2 | biosphere feedbacks, Daisyworld, regime shifts |
| [[Climate - Course Map\|Climate]] | [[Landscapes and Geomorphology - Course Map\|Landscapes and Geomorphology]] | 2 | weathering and CO2, glaciation, precipitation as a driver |
| [[Climate - Course Map\|Climate]] | [[Probability - Course Map\|Probability]] | 2 | sampling, autocorrelation, extremes in observations |
| [[Climate - Course Map\|Climate]] | [[Quantum Mechanics - Course Map\|Quantum Mechanics]] | 2 | Planck law; molecular absorption spectra |
| [[Climate - Course Map\|Climate]] | [[Waves - Course Map\|Waves]] | 2 | Rossby, gravity and Kelvin waves; Fourier methods |
| [[Evolution of Earth and Life - Course Map\|Evolution of Earth and Life]] | [[Landscapes and Geomorphology - Course Map\|Landscapes and Geomorphology]] | 2 | geology: tectonics, sedimentary record |
| [[Ecology and Evolution - Course Map\|Ecology and Evolution]] | [[Proofs, Analysis and Topology - Course Map\|Proofs, Analysis and Topology]] | 2 | chaos and bifurcations in discrete maps (May 1976) |
| [[Bistability and Tipping Points\|Foundations (shared tools)]] | [[Proofs, Analysis and Topology - Course Map\|Proofs, Analysis and Topology]] | 2 | rigour behind calculus and dynamical systems |
| [[Group Theory - Course Map\|Group Theory]] | [[Proofs, Analysis and Topology - Course Map\|Proofs, Analysis and Topology]] | 2 | abstract algebra and proof technique |
| [[Neuroscience - Course Map\|Neuroscience]] | [[Probability - Course Map\|Probability]] | 2 | neural coding, signal detection |
| [[Thermodynamics - Course Map\|Thermodynamics and Stat. Mech.]] | [[Inorganic Chemistry - Course Map\|Inorganic Chemistry]] | 2 | chemical equilibrium, redox potentials, free energy |
| [[Climate - Course Map\|Climate]] | [[Group Theory - Course Map\|Group Theory]] | 1 | IR selection rules via molecular symmetry |
| [[Ecology and Evolution - Course Map\|Ecology and Evolution]] | [[Landscapes and Geomorphology - Course Map\|Landscapes and Geomorphology]] | 1 | habitat and landscape ecology |
| [[Ecology and Evolution - Course Map\|Ecology and Evolution]] | [[Neuroscience - Course Map\|Neuroscience]] | 1 | behaviour (weak) |
| [[Landscapes and Geomorphology - Course Map\|Landscapes and Geomorphology]] | [[Probability - Course Map\|Probability]] | 1 | statistics of floods and erosion |
| [[Neuroscience - Course Map\|Neuroscience]] | [[Bistability and Tipping Points\|Foundations (shared tools)]] | 1 | bistable and critical dynamics |
| [[Neuroscience - Course Map\|Neuroscience]] | [[Thermodynamics - Course Map\|Thermodynamics and Stat. Mech.]] | 1 | energy and information (weak) |
| [[Neuroscience - Course Map\|Neuroscience]] | [[Waves - Course Map\|Waves]] | 1 | oscillations (EEG, rhythms) |
| [[Thermodynamics - Course Map\|Thermodynamics and Stat. Mech.]] | [[Waves - Course Map\|Waves]] | 1 | mode counting in cavities, sound |
| [[Waves - Course Map\|Waves]] | [[Proofs, Analysis and Topology - Course Map\|Proofs, Analysis and Topology]] | 1 | Fourier analysis |

## Degree of connection
```dataview
TABLE length(rows) AS "Notes" FROM #type/moc OR #type/chapter GROUP BY subject
```
