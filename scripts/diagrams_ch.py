"""CH - conceptual diagrams (SVG + Excalidraw).   .venv/bin/python scripts/diagrams_ch.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagrams import excalidraw, svg

SPECS = {
    "CH01 Models of Covalent Bonding": dict(
        size=(980, 520),
        nodes={
            "o": dict(x=150, y=110, w=250, h=100, text="Lewis / octet rule\nelectron pairs\nfails: BeH2, NO, SF6", color="grey"),
            "v": dict(x=490, y=70, w=290, h=100, text="VSEPR\nregions of electron density\nrepel: gives the SHAPE", color="blue"),
            "b": dict(x=490, y=250, w=290, h=110, text="Valence bond (VB)\nlocalised spin-paired bonds\npromotion, hybridisation", color="orange"),
            "h": dict(x=830, y=170, w=270, h=110, text="Hybrids\nsp, sp2, sp3, dsp3, d2sp3\ncos(theta) = S/(S-1); Bent's rule", color="orange"),
            "m": dict(x=490, y=430, w=330, h=100, text="Molecular orbital (MO)\ndelocalised orbitals, N AOs -> N MOs\nspectra, magnetism, hypervalence", color="aqua"),
            "n": dict(x=150, y=370, w=250, h=100, text="Same question,\nthree answers:\nshape, bond, energy levels", color="red"),
        },
        arrows=[("o", "v", ""), ("o", "b", ""), ("v", "b", ""), ("b", "h", ""), ("h", "v", ""), ("b", "m", "")],
        title="Models of covalent bonding in CH2113: which one answers which question",
        footer="CH-2113 slides 1-52: VSEPR (1-7), valence bond and hybridisation (8-26), molecular orbitals (27-52)",
    ),
}

if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
