#!/usr/bin/env python3
"""CH11 (ligand-field theory) checks: reduce the sigma and pi reducible representations of an octahedral ML6 in Oh,
SALC normalisation, electron counts. Added 2026-11-21.  .venv/bin/python -I scripts/ch11_numbers.py"""
import numpy as np
# Oh classes: E, 8C3, 6C2, 6C4, 3C2(=C4^2), i, 6S4, 8S6, 3sh, 6sd
order = np.array([1, 8, 6, 6, 3, 1, 6, 8, 3, 6]); h = order.sum()
irreps = {
 "A1g": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "A2g": [1, 1, -1, -1, 1, 1, -1, 1, 1, -1],
 "Eg": [2, -1, 0, 0, 2, 2, 0, -1, 2, 0], "T1g": [3, 0, -1, 1, -1, 3, 1, 0, -1, -1],
 "T2g": [3, 0, 1, -1, -1, 3, -1, 0, -1, 1], "A1u": [1, 1, 1, 1, 1, -1, -1, -1, -1, -1],
 "A2u": [1, 1, -1, -1, 1, -1, 1, -1, -1, 1], "Eu": [2, -1, 0, 0, 2, -2, 0, 1, -2, 0],
 "T1u": [3, 0, -1, 1, -1, -3, -1, 0, 1, 1], "T2u": [3, 0, 1, -1, -1, -3, 1, 0, 1, -1]}
def reduce(chi):
    return {k: int(round((order * np.array(chi) * np.array(v)).sum() / h)) for k, v in irreps.items() if round((order * np.array(chi) * np.array(v)).sum() / h)}
G_sigma = [6, 0, 0, 2, 2, 0, 0, 0, 4, 2]          # vectors left unmoved (Huheey Fig. 11.18)
G_pi = [12, 0, 0, 0, -4, 0, 0, 0, 0, 0]          # two perpendicular vectors per ligand (Fig. 11.24)
print("h =", h)
print("Gamma_sigma ->", reduce(G_sigma), "(Huheey/S&A: a1g + eg + t1u)")
print("Gamma_pi    ->", reduce(G_pi), "(Huheey: t1g + t2g + t1u + t2u)")
print("SALC normalisation (overlap neglected): a1g 1/sqrt6 =", round(1/np.sqrt(6), 4), "; t1u 1/sqrt2 =", round(1/np.sqrt(2), 4),
      "; eg (x2-y2) 1/2 =", 0.5, "; eg (z2) 1/sqrt12 =", round(1/np.sqrt(12), 4))
v = np.array([2, 2, -1, -1, -1, -1]); print("  check (2,2,-1,-1,-1,-1)/sqrt12 has norm", np.linalg.norm(v / np.sqrt(12)))
print("=== electron counts (sigma-only octahedral: 6 bonding MOs a1g+t1u+eg hold the 12 ligand electrons)")
for name, d, lowspin in [("[Co(NH3)6]3+ (d6, low spin)", 6, True), ("[CoF6]3- (d6, high spin)", 6, False), ("[Mo(CO)6] (d6)", 6, True)]:
    cfg = "t2g^6" if lowspin else "t2g^4 eg*^2"
    print(f"  {name}: {12+d} electrons: a1g^2 t1u^6 eg^4 + {cfg}; unpaired {0 if lowspin else 4}")
print("  [CoCl4]2- (Td, d7): 8 + 7 = 15 electrons; 12 fill through e; 3 unpaired in t2* (Huheey p.418)")
print("  square planar d8: 8 + 8 = 16 electrons fill the 8 lowest MOs: diamagnetic (Huheey p.418)")
print("=== a two-level picture of pi effects (illustrative, energies in eV)")
Ed = -10.0
for lab, Eл, beta in [("pi donor (filled ligand p below d)", -14.0, 1.0), ("pi acceptor (empty pi* above d)", -6.0, 1.0)]:
    M = np.array([[Ed, beta], [beta, Eл]]); w = np.linalg.eigvalsh(M)
    t2g = w[1] if Eл < Ed else w[0]
    print(f"  {lab}: metal t2g level {Ed} -> {t2g:.3f} eV (shift {t2g-Ed:+.3f}); with eg* fixed, Delta_O changes by {-(t2g-Ed):+.3f}")
