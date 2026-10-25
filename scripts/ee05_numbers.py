"""EE05 - numbers quoted in the chapter: Lotka-Volterra predator-prey equilibria, period, conserved quantity, stability.

    .venv/bin/python -W ignore scripts/ee05_numbers.py
"""
import numpy as np
from scipy.integrate import solve_ivp

np.set_printoptions(precision=4, suppress=True)
r, p, a, m, K = 1.0, 0.02, 0.5, 0.5, 200.0
print("== LV predator-prey (r=1, p=0.02, a=0.5, m=0.5)")
Hs, Ps = m / (a * p), r / p
print("equilibrium H* = m/(ap) =", Hs, " P* = r/p =", Ps)
J = np.array([[0, -p * Hs], [a * p * Ps, 0]])
print("Jacobian eigenvalues:", np.linalg.eigvals(J), " -> +/- i sqrt(r m); period 2pi/sqrt(rm) =", 2 * np.pi / np.sqrt(r * m))
V = lambda H, P: a * p * H - m * np.log(H) + p * P - r * np.log(P)
f = lambda t, y: [r * y[0] - p * y[0] * y[1], a * p * y[0] * y[1] - m * y[1]]
sol = solve_ivp(f, (0, 60), [30, 30], rtol=1e-10, atol=1e-12, dense_output=True)
t = np.linspace(0, 60, 2000); H, P = sol.sol(t)
print("conserved V along an orbit: min/max", V(H, P).min().round(6), V(H, P).max().round(6))
print("orbit from (30,30): H range", H.min().round(1), H.max().round(1), " P range", P.min().round(1), P.max().round(1))
# period of the large orbit by successive prey maxima
idx = [i for i in range(1, len(H) - 1) if H[i] > H[i - 1] and H[i] > H[i + 1]]
print("prey maxima at t =", np.round(t[idx], 2), " period ~", np.round(np.diff(t[idx]), 2))
# phase lag: predator peak after prey peak
idxP = [i for i in range(1, len(P) - 1) if P[i] > P[i - 1] and P[i] > P[i + 1]]
print("predator maxima at t =", np.round(t[idxP], 2))
print("\n== with logistic prey (K=200)")
Hs2 = m / (a * p); Ps2 = (r / p) * (1 - Hs2 / K)
print("H* =", Hs2, " P* = (r/p)(1 - H*/K) =", Ps2, " exists iff K > m/(ap) =", Hs2)
J2 = np.array([[-r * Hs2 / K, -p * Hs2], [a * p * Ps2, 0]])
ev = np.linalg.eigvals(J2)
print("Jacobian eigenvalues:", ev, " trace", np.trace(J2).round(4), " det", np.linalg.det(J2).round(4), " spiral (complex)?", np.iscomplex(ev).any())
if np.iscomplex(ev).any():
    print("  damping envelope rate", ev.real[0].round(4), " -> amplitude halves in", round(np.log(2) / -ev.real[0], 2), "time units; oscillation period", round(2 * np.pi / abs(ev.imag[0]), 2))
g = lambda t, y: [r * y[0] * (1 - y[0] / K) - p * y[0] * y[1], a * p * y[0] * y[1] - m * y[1]]
sol2 = solve_ivp(g, (0, 80), [30, 30], rtol=1e-10, atol=1e-12, dense_output=True)
print("at t=80:", sol2.sol(80).round(2), "(equilibrium", (Hs2, Ps2), ")")
print("K threshold: predator persists only if K >", Hs2, " (K=40 -> predator dies out)")
print("\n== Gause (slide 10): 'one prey + one predator added every third day' - a rescue of the Lotka-Volterra cycle by immigration (qualitative)")
