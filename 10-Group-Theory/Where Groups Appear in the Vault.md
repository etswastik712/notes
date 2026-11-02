---
title: Where Groups Appear in the Vault
aliases: [group theory in other subjects, uses of group theory, symmetry across the vault]
subject: group-theory
type: moc
by: [own-notes]
status: draft
tags: [subject/group-theory, type/moc, src/own-notes, status/draft]
---
# Where Groups Appear in the Vault

> [!summary] How to use this page
> Every row is a place in another subject where a *group-theoretic idea is actually used* (found by searching the vault, then checked in the note), with the chapter of this subject where the idea is developed. The reverse pointers (a `[!connection]` callout in each of those notes) lead back here. If you read a chapter in another subject and a symmetry argument seems to come from nowhere, look it up below.

## Chemistry ([[Inorganic Chemistry - Course Map]])
| Where | Group idea | Developed in |
|---|---|---|
| [[CH03 Molecular Orbital Theory Polyatomics]], [[Ligand Group Orbitals]], [[Symmetry Labels a b e t]], [[Reduction of a Representation]] | point groups $C_{2v}\cong C_2\times C_2$ (H$_2$O), $C_{3v}\cong S_3$ (NH$_3$), $T_d\cong S_4$, $O_h$; characters, the reduction formula, symmetry labels $a,b,e,t$ (irreducible representations), SALCs | [[GT10 Symmetry Representations and Characters]] §1–§3; [[GT05 Actions Conjugation and Sylow Theorems]], [[GT06 Permutation Groups]] (the groups themselves) |
| [[CH01 VSEPR and Valence Bond Theory]] | the shape of a molecule is a point group; equivalent ligands form one orbit | [[GT05 Actions Conjugation and Sylow Theorems]] (orbits), [[GT10 Symmetry Representations and Characters]] |
| [[CH02 Molecular Orbital Theory Diatomics]] | $\sigma,\pi$ (rotation about the bond axis) and $g/u$ (inversion) labels: characters of $D_{\infty h}$ | [[GT10 Symmetry Representations and Characters]] |
| [[CH07 Main Group Cages and Clusters]] | point groups of the polyhedra: $O_h$, $I_h$, $D_{3h}$, $T_d$; the icosahedral group $I\cong A_5$ is the first non-solvable point group | [[GT06 Permutation Groups]] ($A_5$ simple), [[GT08 Solvable Groups and Complements]] |
| [[CH08 Main Group Rings and Polymers]] | $D_{3h}$ symmetry of the six-membered rings | [[GT08 Solvable Groups and Complements]] (semidirect products), [[GT10 Symmetry Representations and Characters]] |
| vibrational spectra (IR/Raman selection rules) | a mode is IR-active iff it transforms like $x,y,z$; $\Gamma_{vib}(\mathrm{NH_3})=2A_1+2E$ | [[GT10 Symmetry Representations and Characters]] §4 |
| crystal-field splitting | $d\to E+T_2$ in $O$ | [[GT10 Symmetry Representations and Characters]] §5 |

## Climate
| Where | Group idea | Developed in |
|---|---|---|
| [[CL07 Optical Properties of the Atmosphere]] | why CO$_2$ and H$_2$O absorb infrared: the dipole selection rule in group-theory language (a vibration is active if it transforms like a coordinate); linear molecules and the mutual-exclusion rule | [[GT10 Symmetry Representations and Characters]] §4 |
| [[CL12 Rotating Frames and the Coriolis Force]], [[Rotating Reference Frames]] | rotations of the plane/sphere form $SO(2)$, $SO(3)$; the Coriolis term arises from the time-dependent rotation | [[GT10 Symmetry Representations and Characters]] §6 |

## Quantum mechanics ([[Quantum Mechanics - Course Map]])
| Where | Group idea | Developed in |
|---|---|---|
| [[Parity Operator]], [[Parity Theorem]], [[QM04 The Particle in a Box]], [[QM07 The Finite Square Well]] | parity is the group $C_2=\{1,\hat P\}$; the parity theorem splits the problem into the two irreps (even, odd) | [[GT03 Cyclic and Abelian Groups and Direct Products]] (cyclic group $C_2$), [[GT10 Symmetry Representations and Characters]] §2 |
| [[Bloch Theorem]], [[QM08 Quantum Tunnelling]] §8 (Kronig–Penney) | translation by a lattice spacing generates $\mathbb Z$; its characters $e^{iqa}$ label the states; Abelian groups have 1-dimensional irreps | [[GT03 Cyclic and Abelian Groups and Direct Products]] §6, [[Fourier and Laplace Transforms]] §5.5 |
| [[Dirac Algebra]] §7 (translation operator), [[Unitary Operator]], [[Canonical Commutation Relation]] | $e^{-i\hat p\ell/\hbar}$ is a unitary representation of $(\mathbb R,+)$; $[\hat x,\hat p]=i\hbar$ central $\Rightarrow$ the Heisenberg group, nilpotent of class 2 | [[GT07 p-Groups and Nilpotent Groups]] §5, [[GT10 Symmetry Representations and Characters]] §6 |
| [[Degeneracy]], [[Isotropic Oscillator and Degeneracy]], [[Selection Rules]] | degeneracy = dimension of an irreducible representation of the symmetry group; selection rules = the product $\Gamma_a\otimes\Gamma_O\otimes\Gamma_b$ contains the trivial irrep | [[GT10 Symmetry Representations and Characters]] §2, §6 |
| identical particles (exchange symmetry) | $S_n$ acts on $n$-particle states; sign homomorphism $S_n\to\{\pm1\}$ = bosons/fermions | [[GT06 Permutation Groups]], [[GT04 Commutators Simple Groups and Composition Series]] (the abelianisation of $S_n$) |

## Foundations, probability, proofs
| Where | Group idea | Developed in |
|---|---|---|
| [[Fourier and Laplace Transforms]] | DFT matrix = character table of $\mathbb Z_N$; convolution theorem = group algebra; Fourier transform on $\mathbb R$, $S^1$, $\mathbb Z_N$ | [[GT03 Cyclic and Abelian Groups and Direct Products]], [[GT10 Symmetry Representations and Characters]] |
| [[PA03 Relations Equivalence and Order]], [[Equivalence Class and Partition]], [[Congruence Modulo n]] | cosets are the classes of the equivalence relation $x\sim y\iff x^{-1}y\in U$; $G/N$ is the quotient set $A/{\sim}$ | [[GT01 Groups Subgroups and Cosets]], [[GT02 Homomorphisms Normal Subgroups and Quotients]] |
| [[PR01 Counting and the Axioms of Probability]], [[Probability - Course Map]] | counting up to symmetry (Burnside), derangements and random permutations | [[GT05 Actions Conjugation and Sylow Theorems]], [[GT06 Permutation Groups]] |

## Landscapes ([[Landscapes and Geomorphology - Course Map]])
| Where | Group idea | Developed in |
|---|---|---|
| [[LS04 Map Projections and Reference Surfaces]], [[LS05 Shape of Planets]] | rotations of the sphere $SO(3)$; spherical harmonics $Y_\ell^m$ = irreps of dimension $2\ell+1$ | [[GT10 Symmetry Representations and Characters]] §6 |
| [[LS02 Mechanics and Mathematics Toolkit]], [[LS08 Plate Tectonics Strain Stress and Convection]] | rotating the axes of a stress/strain tensor (Mohr's circle, $e^{\pm2i\theta}$); infinitesimal rotations $\mathfrak{so}(3)$ | [[GT10 Symmetry Representations and Characters]] §6 |
| [[LS03 Digital Elevation Models and Terrain Analysis]] | translations of a grid, Fourier modes, UTM grid rotation $SO(2)$ | [[GT03 Cyclic and Abelian Groups and Direct Products]], [[Fourier and Laplace Transforms]] |

## Not (yet) used
Thermodynamics, Eco-evo, Waves and Neuroscience notes contain no group-theoretic argument at present (Waves has only a stub; normal modes of symmetric systems would use [[GT10 Symmetry Representations and Characters]]). The MT3184 Lie-group lecture notes (by another tool) are the continuous-group counterpart of this subject: see [[GT10 Symmetry Representations and Characters]] §6 and [[one-parameter-subgroup]]; the full treatment is the [[Differential Geometry - Course Map|Differential Geometry vault]] (Lie groups, Lie algebras, $\exp$, the Lie correspondence).
