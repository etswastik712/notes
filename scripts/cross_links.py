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

SUBJ = {"01-Climate": "Climate", "02-Eco-Evo": "Eco-Evo", "03-Thermodynamics": "Thermodynamics",
        "04-Evolution-of-Earth-and-Life": "Earth and Life", "05-Landscapes-Geomorphology": "Landscapes",
        "06-Quantum-Mechanics": "Quantum Mechanics", "07-Waves": "Waves", "08-Probability": "Probability",
        "09-Foundations": "Foundations", "10-Group-Theory": "Group Theory", "11-Proofs-Analysis-Topology": "Analysis",
        "12-Inorganic-Chemistry": "Chemistry", "13-Neuroscience": "Neuroscience"}

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
    # ---- Thermo <-> Chemistry
    ("Gibbs Free Energy", "Standard Reduction Potential",
     "$\\Delta G^\\circ=-nFE^\\circ$ links a cell potential to the Gibbs free energy: the same quantity that decides spontaneity in thermodynamics is measured as a voltage"),
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
