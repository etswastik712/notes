"""Cross-subject links: curated bridges between notes of different subjects, added as an `## Across subjects` section.

    .venv/bin/python -W ignore scripts/cross_links.py            # dry run: list what would be added
    .venv/bin/python -W ignore scripts/cross_links.py --apply

Each PAIR is (note A, note B, reason).  The same reason is written on both sides, with the other note's subject in brackets.
A bullet is added to a note only if it does not already link to the other one (so re-running is idempotent), and it is
appended to the note's own `## Across subjects` section (created at the end of the note if missing).  Nothing is removed.
Selection rule: a bridge is listed only if it carries a *mathematical or physical identity* (the same equation, the same
object, the same selection rule), not just a shared word.  Reasons are one or two sentences and are checked by hand.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graph_colors as gc  # noqa: E402

SUBJ = {"01-Climate": "Climate", "02-Eco-Evo": "Eco-Evo", "03-Thermodynamics-and-Statistical-Mechanics": "Thermodynamics",
        "04-Evolution-of-Earth-and-Life": "Earth and Life", "05-Landscapes-Geomorphology": "Landscapes",
        "06-Quantum-Mechanics": "Quantum Mechanics", "07-Waves": "Waves", "08-Probability": "Probability",
        "09-Foundations": "Foundations", "10-Group-Theory": "Group Theory", "11-Proofs-Analysis-Topology": "Analysis",
        "12-Inorganic-Chemistry": "Chemistry", "13-Neuroscience": "Neuroscience",
        "14-Differential-Geometry": "Differential Geometry"}

PAIRS = [
    # ---- Climate <-> Thermodynamics <-> QM
    ("Greenhouse Effect", "Blackbody Radiation",
     "the emission temperature and every greenhouse model start from blackbody emission $\\sigma T^4$; the greenhouse effect is the gap between that balance and the observed surface flux"),
    ("One-Layer Greenhouse Model", "Stefan-Boltzmann Law",
     "the model closes its energy balance with $\\sigma T^4$ for the surface and for the single absorbing layer"),
    ("Effective Emission Temperature", "Stefan-Boltzmann Law",
     "$T_e=[(1-\\alpha)S/4\\sigma]^{1/4}$ is the Stefan-Boltzmann law inverted for the planet's absorbed flux"),
    ("Atmospheric Window", "Planck Law",
     "the 8-12 $\\mu$m window sits near the peak of the Planck curve of a $\\sim$288 K surface (Wien: $\\lambda_{max}\\approx10\\ \\mu$m), so it is the channel through which surface emission escapes"),
    ("Adiabatic Process and Potential Temperature", "Lapse Rate",
     "the dry adiabatic lapse rate $\\Gamma_d=g/c_p$ is the adiabatic condition $pV^\\gamma=$ const applied to a rising, hydrostatically cooled parcel"),
    ("Planck Law", "Thermal Harmonic Oscillator",
     "each mode of the radiation field is a quantum oscillator; thermal averaging over its levels gives the Planck mean energy $\\hbar\\omega/(e^{\\beta\\hbar\\omega}-1)$ and hence the Planck law"),
    ("Planck Mean Energy", "Geometric Distribution",
     "the thermal occupation number is geometric, $P(n)=(1-q)q^n$ with $q=e^{-\\beta\\hbar\\omega}$, and its mean $q/(1-q)=1/(e^{\\beta\\hbar\\omega}-1)$ is the Bose-Einstein factor in the Planck mean energy"),
    ("Partition Function", "Moment Generating Function",
     "$Z(\\beta)=\\sum_i e^{-\\beta E_i}$ is the moment generating function of the energy at $t=-\\beta$ (up to normalisation); $\\langle E\\rangle=-\\partial_\\beta\\ln Z$ and $\\mathrm{Var}\\,E=\\partial_\\beta^2\\ln Z$ are the first two cumulants"),
    ("Einstein Heat Capacity", "Third Law of Thermodynamics",
     "the gapped oscillator spectrum makes $C_V\\to0$ exponentially as $T\\to0$, which is how quantum mechanics delivers the third law for solids"),
    ("Greenhouse Gases and Absorption Bands", "Selection Rules",
     "a vibration absorbs infrared only if it changes the dipole moment, which is a symmetry statement (the mode must transform like $x$, $y$ or $z$): this is why CO$_2$, H$_2$O and CH$_4$ are greenhouse gases and homonuclear N$_2$ and O$_2$ are not"),
    ("Greenhouse Gases and Absorption Bands", "Character of a Representation",
     "which normal modes of CO$_2$, H$_2$O or CH$_4$ are infrared-active is read from the characters of the molecule's point group (the mode's irreducible representation must appear in the dipole representation)"),
    # ---- Landscapes <-> Climate <-> QM <-> Eco
    ("LS05 Shape of Planets", "Centrifugal Force and Effective Gravity",
     "the equatorial bulge of a rotating planet is the centrifugal term in the effective gravity: the surface is an equipotential of gravity plus $-\\tfrac12\\Omega^2r^2\\cos^2\\varphi$"),
    ("LS05 Shape of Planets", "CL12 Rotating Frames and the Coriolis Force",
     "the same rotating-frame mechanics that gives the Coriolis force in the atmosphere gives the flattening of the planet (centrifugal term) and the tilt of the geoid"),
    ("CL15 Monsoons", "LS10 Folds Flexure and Mountain Building",
     "the Himalaya and the Tibetan Plateau are both a tectonic product and a boundary condition of the monsoon circulation; rainfall focused on the range feeds back on erosion and isostatic uplift"),
    ("EE06 Eutrophication and Alternative Stable States", "LS11 Weathering and Regolith",
     "the phosphorus that limits lake productivity is released from apatite by weathering and delivered by erosion, so the geomorphic conveyor sets the supply side of eutrophication"),
    ("LS11 Weathering and Regolith", "CH09 Redox",
     "oxidation of Fe$^{2+}$ minerals and of sulfides is a redox reaction whose standard potentials decide which weathering reactions run; the rust-coloured regolith is an Fe(III) product"),
    ("Foucault Pendulum", "Larmor Precession",
     "both are rotating-frame effects: the pendulum plane turns at $\\Omega\\sin\\varphi$ because the Earth rotates under it, and a magnetic moment precesses at $\\omega_L=-\\gamma B$ because in the frame rotating at $\\omega_L$ the field disappears (Larmor's theorem)"),
    # ---- Probability <-> QM <-> Eco <-> Analysis
    ("Probabilists' Hermite Polynomials", "Normal Distribution",
     "the probabilists' Hermite polynomials $He_n$ are the orthogonal polynomials for the standard normal density, $\\int He_mHe_n\\,\\phi=n!\\,\\delta_{mn}$; the oscillator eigenfunctions are the physicists' version times a Gaussian"),
    ("Hermite Generating Function and Recurrences", "Moment Generating Function",
     "the generating function $e^{xt-t^2/2}=\\sum He_n(x)t^n/n!$ is the moment generating function of the standard normal, $E[e^{tZ}]=e^{t^2/2}$, read as a function of $x$"),
    ("Logistic Distribution", "Logistic Growth",
     "the solution $N(t)=K/(1+e^{-r(t-t_0)})$ of logistic growth is $K$ times the cdf of a logistic distribution with location $t_0$ and scale $1/r$, so growth quantiles are logistic quantiles"),
    ("Hilbert Space", "Cauchy Sequence",
     "a Hilbert space is a complete inner-product space: completeness means every Cauchy sequence in the norm converges, which is what licenses eigenfunction expansions"),
    ("Hilbert Space", "Metric Space",
     "the norm $\\|\\psi\\|=\\sqrt{\\langle\\psi|\\psi\\rangle}$ gives the metric $d(\\psi,\\phi)=\\|\\psi-\\phi\\|$, so a Hilbert space is a complete metric space with extra (inner-product) structure"),
    ("Continuity of Probability", "Monotone Convergence Theorem",
     "continuity from below, $P(\\cup A_n)=\\lim P(A_n)$, is the monotone convergence theorem for indicator functions"),
    ("Law of Large Numbers", "Sequence and Limit",
     "the law of large numbers is a limit theorem for the sequence of sample means; unlike the real-analysis limit it holds in probability or almost surely, not pointwise"),
    ("Leslie Matrix", "Eigenstate and Eigenvalue",
     "both are matrix eigenproblems: the dominant eigenvalue of the Leslie matrix is the growth rate, and Perron-Frobenius (a positive dominant eigenvector) is the matrix analogue of a nodeless, non-degenerate ground state"),
    # ---- Group theory <-> Chemistry <-> QM <-> Analysis
    ("Reduction of a Representation", "Reduction Formula",
     "the chemist's reduction of a reducible representation of a molecule is the group theorist's reduction formula $n_i=\\frac1{|G|}\\sum_g\\chi(g)\\chi_i(g)^*$"),
    ("Symmetry Labels a b e t", "Irreducible Representation",
     "the Mulliken labels $a$, $b$ (1-d), $e$ (2-d), $t$ (3-d) are names of irreducible representations of the molecular point group"),
    ("Ligand Group Orbitals", "Reduction Formula",
     "the symmetry-adapted ligand combinations are found by reducing the representation spanned by the ligand orbitals and projecting onto each irreducible representation"),
    ("Symmetry Labels a b e t", "Degeneracy",
     "the dimension of the irreducible representation is the degeneracy symmetry forces: $e$ levels are doubly and $t$ levels triply degenerate; any other degeneracy is accidental"),
    ("Heitler-London Wavefunction", "Singlet and Triplet States",
     "the covalent bond of H$_2$ is the spin-singlet, spatially symmetric Heitler-London combination; the triplet is antisymmetric in space and repulsive"),
    ("Bloch Theorem", "Irreducible Representation",
     "Bloch's theorem is the representation theory of the translation group: its irreducible representations are the one-dimensional characters $e^{i\\mathbf k\\cdot\\mathbf R}$, one for each crystal momentum"),
    ("Heisenberg Group", "Canonical Commutation Relation",
     "the relation $[x,p]=i\\hbar$ is the Lie algebra of the Heisenberg group; its unique irreducible unitary representation (Stone-von Neumann) is the Schrodinger representation"),
    ("Equivalence Class and Partition", "Coset",
     "the left cosets of a subgroup are the equivalence classes of $a\\sim b\\iff a^{-1}b\\in H$, so they partition the group (the heart of Lagrange's theorem)"),
    ("Equivalence Class and Partition", "Orbit-Stabiliser Theorem",
     "the orbits of a group action are the equivalence classes of $x\\sim y\\iff y=gx$; counting each class gives the orbit-stabiliser formula"),
    ("Burnside's Lemma", "Counting Principles",
     "Burnside's lemma counts distinct arrangements up to symmetry as the average number of fixed points, a counting tool used for isomers, colourings and necklaces"),
    # ---- Landscapes rivers (LS21-LS24) and the interdisciplinary chapters LSX1 / THX1
    ("Central Limit Theorem", "Random Walk",
     "the displacement of a random walk is a sum of independent steps, so it tends to a Gaussian of variance $2Dt$, which is the heat kernel"),
    ("Normal Distribution", "Diffusion Equation",
     "the normal density with variance $2Dt$ is the fundamental solution of the diffusion equation"),
    ("Gamow Factor", "Alpha Decay",
     "applied to an alpha particle in a heavy nucleus the Gamow factor gives half-lives from $10^{-7}$ s to $10^{17}$ s (a computed 24-decade span) and the exponential sensitivity to $Q$ (Geiger-Nuttall)"),
    ("QM08 Quantum Tunnelling", "LSX1 Clocks in Rocks",
     "tunnelling is why radioactive decay constants are fixed, and so why isotopic clocks work: the same barrier-penetration integral dates rocks"),
    ("Exponential Distribution", "Radioactive Decay Law",
     "each nucleus's decay time is exponential with mean $\\tau=1/\\lambda$; the decay law is its survival function and $t_{1/2}=\\tau\\ln2$ its median"),
    ("Poisson Distribution", "Radioactive Decay Law",
     "the number of decays counted in a window is Poisson with relative error $1/\\sqrt n$, which is why accelerator mass spectrometry (counting atoms) beat decay counting for radiocarbon"),
    ("Memoryless Property", "Radioactive Decay Law",
     "the half-life is constant, independent of the sample's age, because nuclear decay is memoryless"),
    ("Free Particle", "Diffusion Equation",
     "the free Schrodinger equation is the diffusion equation with imaginary diffusion constant $i\\hbar/2m$; its propagator is the heat kernel with a phase, so the packet spreads without losing norm"),
    ("Equipartition of Energy", "Brownian Motion and the Einstein Relation",
     "the thermal energy $k_BT/2$ per degree of freedom drives Brownian jitter; the Einstein relation $D=\\mu k_BT$ ties the spreading to friction"),
    ("Gumbel Distribution", "Effective Discharge",
     "annual flood maxima are modelled by the Gumbel law; the mean annual flood is the 2.33-yr event, close to the bankfull flow that does the most sediment work"),
    ("Dispersion Relation", "Froude Number and Hydraulic Jump",
     "$\\sqrt{gH}$ is the long-wave limit of the water-wave dispersion relation, and $Fr=U/\\sqrt{gH}$ compares the flow with the wave speed"),
    ("Dimensional Analysis", "Manning Equation",
     "dimensional analysis gives $\\langle U\\rangle\\propto\\sqrt{gHS}$ and shows why the Chezy and Manning coefficients are not dimensionless while Darcy-Weisbach $f$ is"),
    ("CL13 Horizontal Motion - Geostrophic Balance and Friction", "Law of the Wall",
     "the atmospheric surface layer obeys the same logarithmic profile $U=(u_*/\\kappa)\\ln(z/z_0)$ with a friction velocity and a roughness length"),
    ("Impulse Response and Green's Function", "Diffusion Equation",
     "the Gaussian heat kernel is the Green's function of $\\partial_t-D\\partial_x^2$: any initial profile spreads as its convolution with it"),
    ("TH06 From Kinetic Theory to Statistical Mechanics", "Random Walk",
     "molecular collisions are a random walk of the velocity and position of a molecule; the mean free path and collision time give $D=\\ell^2/2\\tau$"),
    ("Entropy", "Diffusion Equation",
     "a diffusing Gaussian gains differential entropy $\\tfrac12\\ln(4\\pi eDt)$, growing as $\\tfrac12\\ln t$: the standard picture of irreversible spreading"),
    ("Partition Function", "Closure Temperature",
     "the Boltzmann factor $e^{-E/RT}$ is the Arrhenius activation law behind $D=D_0e^{-E/RT}$ and hence the closure temperature of a mineral"),
    ("Fourier Transform", "Diffusion Equation",
     "in Fourier space $\\partial_tu=D\\nabla^2u$ becomes $\\dot{\\hat u}=-Dk^2\\hat u$: diffusion is a low-pass filter that kills short wavelengths first"),
    ("Binomial Distribution", "Wright-Fisher Drift as Diffusion",
     "the Wright-Fisher model samples $2N$ gene copies binomially each generation; its variance $p(1-p)/2N$ is the step variance of the diffusion of drift"),
    ("Orographic Precipitation", "Stream Power Law",
     "orographic rain raises the discharge on the windward flank, so less slope is needed to incise at the uplift rate: steady relief is lower than with uniform rain (Roe et al. 2002)"),
    ("Poisson Distribution", "Cosmogenic Nuclides",
     "counting $^{10}$Be atoms by accelerator mass spectrometry is a counting experiment: the relative error is $1/\\sqrt N$ plus the blank and standard uncertainties"),
    # ---- LS25-LS27 (water, sea level, waves, coasts)
    ("Dupuit Water Table", "Diffusion Equation",
     "linearised about a mean thickness the Boussinesq water-table equation is $\\partial_tH=D_H\\partial_x^2H$ with $D_H=K\\bar H/S_y$, the heat equation; a river-stage oscillation penetrates the bank with the thermal skin-depth formula"),
    ("Darcy's Law and Hydraulic Conductivity", "Fick's and Fourier's Laws",
     "Darcy's law $q=-K\\nabla h$ is a third instance of the flux-gradient law (after Fick and Fourier), with the conductivity built from a pore-scale Poiseuille flow"),
    ("Coastline Instability", "Diffusion Equation",
     "the shoreline obeys $\\partial_ty=\\kappa\\partial_x^2y$ with $\\kappa=2Q_0\\cos2\\alpha_0/D$, a diffusion whose sign reverses above $45^\\circ$: anti-diffusion grows capes and is ill-posed at short wavelength"),
    ("Delta Front", "Péclet Number",
     "the delta front $z=z_0e^{-u_0x/K}$ is diffusion in a frame moving at $u_0$; its length $K/u_0$ is where the Péclet number is 1"),
    ("Water Wave Dispersion", "Phase and Group Velocity",
     "$\\omega^2=gk\\tanh kh$ is a concrete dispersive medium: energy and swell move at $C_g=d\\omega/dk=\\tfrac12C$ in deep water, which sorts a storm's waves by period on arrival"),
    ("Water Wave Dispersion", "Gaussian Wave Packet",
     "a localised packet of water waves spreads by dispersion exactly as a free-particle packet does, with the deep-water $\\omega\\propto\\sqrt k$ in place of $\\omega\\propto k^2$"),
    ("Wave Energy and Power", "Normal Distribution",
     "the surface elevation of a narrow-band sea is Gaussian, so wave heights are Rayleigh distributed ($H_{1/3}=2\\sigma$) and the largest 10% of waves carry 33% of the energy"),
    ("Storm Surge", "CL12 Rotating Frames and the Coriolis Force",
     "the Coriolis force deflects the wind-driven surge, making it stronger on the right of a northern-hemisphere hurricane track where wind and forward motion add"),
    ("Drainage Density and Horton's Laws", "Counting Principles",
     "Horton's bifurcation ratio $R_b\\approx4$ is what a uniformly random binary tree gives (cycle-lemma/Catalan counting), so the law reflects branching combinatorics rather than a tuned river"),
    ("Water Balance", "CL10 Global Energy Balance and Meridional Structure",
     "the latent-heat flux of the surface energy budget is the evapotranspiration term $ET$ of the basin water balance; the two budgets are coupled through evaporation"),
    # ---- Thermo <-> Chemistry
    ("Gibbs Free Energy", "Standard Reduction Potential",
     "$\\Delta G^\\circ=-nFE^\\circ$ links a cell potential to the Gibbs free energy: the same quantity that decides spontaneity in thermodynamics is measured as a voltage"),
    # ---- Proofs / Probability / Foundations (added 2026-10-29)
    ("Catalan Numbers", "Drainage Density and Horton's Laws",
     "the number of full binary tree shapes with $m$ internal nodes is $C_m$, from the recursion $C_{n+1}=\\sum C_kC_{n-k}$; this is the counting behind the random-topology model of stream networks, where Horton's bifurcation ratio comes out near 4"),
    ("Cauchy-Schwarz Inequality", "Generalised Uncertainty Principle",
     "the uncertainty relation is Cauchy-Schwarz for the vectors $(\\hat A-\\langle A\\rangle)\\psi$ and $(\\hat B-\\langle B\\rangle)\\psi$; for random variables the same inequality is $|\\rho|\\le1$"),
    ("Sum of Independent Random Variables", "Convolution",
     "the density of $X+Y$ for independent variables is the convolution $f_X*f_Y$: the same integral, with MGFs multiplying as Fourier transforms do"),
    ("Maxwell-Boltzmann Distribution", "Rayleigh Distribution",
     "the Maxwell speed density $ax^2e^{-bx^2}$ is the 3-D relative of the Rayleigh density $xe^{-x^2/2\\sigma^2}$ of the 2-D speed of Gaussian components; both normalise by $\\int x^ke^{-x^2}\\mathrm dx$ (Quiz 1, Q3)"),
    ("Fibonacci Numbers", "Leslie Matrix",
     "Fibonacci's rabbits are a two-age-class Leslie model: $N_{t+2}=N_{t+1}+N_t$ is the matrix $\\begin{pmatrix}1&1\\\\1&0\\end{pmatrix}$ whose dominant eigenvalue is the golden ratio $\\varphi$, the asymptotic growth factor"),
    # ---- Statistical mechanics (SM01-SM07) added 2026-11-02
    ("Fermi-Dirac Distribution", "Logistic Distribution",
     "the Fermi function $1/(e^{x}+1)$ is the logistic function $\\sigma(-x)$, the CDF of the logistic distribution: the same sigmoid describes the occupation of a fermion level, the polarisation $\\tfrac12(1+\\tanh)$ of a spin-1/2 paramagnet and a logistic response curve"),
    ("Fermi-Dirac Distribution", "Logistic Growth",
     "the solution of logistic growth, $N(t)=K/(1+e^{-r(t-t_0)})$, is a Fermi function of time: carrying capacity plays the role of the single available state and $r$ of the inverse temperature"),
    ("Relative Entropy", "Akaike Information Criterion",
     "AIC estimates the expected Kullback-Leibler divergence $D(p_{\\rm true}\\|p_{\\rm model})$ up to a constant; the same functional is the free-energy excess $F[q]-F=k_BT\\,D(q\\|p)$ of a trial distribution in statistical mechanics"),
    ("Entropy of Radiation", "Effective Emission Temperature",
     "the effective emission temperature $T_e=255$ K fixes the entropy flux $\\tfrac43J/T_e$ carried by the Earth's infrared emission, 22.7 times the entropy flux $\\tfrac43J/T_\\odot$ of the absorbed sunlight"),
    ("Viscosity of a Gas", "Péclet Number",
     "the kinematic viscosity $\\nu=\\eta/\\rho$ computed from kinetic theory is the diffusivity of momentum, so the Reynolds number $UL/\\nu$ is a Péclet number for momentum transport and the Prandtl number $\\nu/D_T$ compares the two diffusivities"),
]


def find(notes, name):
    hits = [r for r, n in notes.items() if n["name"] == name or name in n["aliases"]]
    return hits


def section_add(text, bullet):
    if "## Across subjects" not in text:
        return text.rstrip("\n") + "\n\n## Across subjects\n" + bullet + "\n"
    i = text.index("## Across subjects")
    j = text.find("\n## ", i + 5)
    if j == -1:
        return text.rstrip("\n") + "\n" + bullet + "\n"
    return text[:j].rstrip("\n") + "\n" + bullet + "\n" + text[j:]


def run(apply):
    notes = gc.load_notes()
    added, skipped, missing = 0, 0, []
    for a, b, why in PAIRS:
        ha, hb = find(notes, a), find(notes, b)
        if not ha or not hb:
            missing.append((a, b, bool(ha), bool(hb)))
            continue
        ra, rb = ha[0], hb[0]
        if ra.split("/")[0] == rb.split("/")[0]:
            print("same subject (skipped):", a, "|", b)
            continue
        for src, dst, other in ((ra, rb, b), (rb, ra, a)):
            t = notes[src]["text"]
            if re.search(r"\[\[" + re.escape(other) + r"[\]|#]", t):
                skipped += 1
                continue
            dname = os.path.basename(dst)[:-3]
            sub = SUBJ[dst.split("/")[0]]
            bullet = f"- [[{dname}]] ({sub}): {why}."
            notes[src]["text"] = section_add(t, bullet)
            added += 1
            if apply:
                open(notes[src]["path"], "w", encoding="utf-8").write(notes[src]["text"])
    print(f"bullets added: {added}   already linked (skipped): {skipped}")
    for m in missing:
        print("MISSING:", m)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    run(ap.parse_args().apply)
