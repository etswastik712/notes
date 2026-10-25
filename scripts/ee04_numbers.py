"""EE04 - numbers quoted in the chapter: L-V equilibria and stability, the R* chemostat example, Park's Tribolium table.

    .venv/bin/python -W ignore scripts/ee04_numbers.py
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)
K1, K2 = 100.0, 80.0
print("== Lotka-Volterra competition (K1=100, K2=80, r1=r2=0.5)")
for nm, a12, a21 in (("A: 1 wins", 0.5, 1.5), ("B: 2 wins", 1.5, 0.5), ("C: coexist", 0.5, 0.6), ("D: priority", 1.5, 1.5)):
    d = 1 - a12 * a21
    n1, n2 = (K1 - a12 * K2) / d, (K2 - a21 * K1) / d
    # outcome from isocline intercepts
    s1_wins = K1 > K2 / a21 and K1 / a12 > K2
    s2_wins = K2 > K1 / a12 and K2 / a21 > K1
    co = K1 < K2 / a21 and K2 < K1 / a12
    pr = K1 > K2 / a21 and K2 > K1 / a12
    kind = "1 wins" if s1_wins else "2 wins" if s2_wins else "coexist" if co else "priority/unstable" if pr else "?"
    msg = f"  {nm}: a12*a21={a12 * a21:.2f}  interior point ({n1:.1f}, {n2:.1f})  intercepts: sp1 N1={K1}, N2={K1 / a12:.1f}; sp2 N2={K2}, N1={K2 / a21:.1f}  -> {kind}"
    if n1 > 0 and n2 > 0:
        r = 0.5
        J = np.array([[-r * n1 / K1, -r * a12 * n1 / K1], [-r * a21 * n2 / K2, -r * n2 / K2]])
        msg += f"  eig(J)={np.round(np.linalg.eigvals(J), 4)}"
    print(msg)
print("  coexistence conditions: a12 < K1/K2 =", K1 / K2, "and a21 < K2/K1 =", K2 / K1)
# separatrix for panel D: initial ratio
print("\n== R* chemostat example")
for nm, mu, k in (("A", 0.8, 2.0), ("B", 0.6, 1.0)):
    m = 0.2
    print(f"  {nm}: R* = m k/(mu - m) = {m * k / (mu - m):.4f}; growth at R=0.5: {mu * 0.5 / (k + 0.5):.4f}; at R=10: {mu * 10 / (k + 10):.4f}")
print("  equilibrium B: N* = R_in - R* =", 10 - 0.5)
print("\n== Park's Tribolium (slide 30)")
rows = [("cool 24C dry", 26.0, 2.6, 100, 0), ("cool 24C moist", 28.2, 45.2, 71, 29), ("moderate dry", 29.7, 18.8, 87, 13),
        ("moderate moist", 32.9, 50.1, 14, 86), ("warm 34C dry", 23.7, 9.6, 90, 10), ("warm 34C moist", 41.2, 38.3, 0, 100)]
for nm, ec, ea, wc, wa in rows:
    bigger = "confusum" if ec > ea else "castaneum"
    winner = "confusum" if wc > wa else "castaneum"
    print(f"  {nm:16s} bigger alone: {bigger:10s} wins: {winner:10s} {'<- larger equilibrium loses' if bigger != winner else ''}")
print("\n== alpha from niche overlap (toy): species using resource axis with Gaussian utilisation, widths sigma, separation d: alpha = exp(-d^2/(4 sigma^2))")
for dsig in (0.0, 0.5, 1.0, 1.5, 2.0):
    a = np.exp(-dsig ** 2 / 4)
    print(f"  d/sigma={dsig}: alpha={a:.3f}  alpha^2<1: {a * a < 1}")
print("\n== Kerala (slides 15-16): 28 alien fish + 4 macrophytes = ", 28 + 4, "alien species; established 7 ->", round(7 / 32 * 100), "% of 32")
