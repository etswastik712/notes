#!/usr/bin/env python3
"""Week 6-7 lecture examples (MT2113): CLT approximations vs exact. Added 2026-11-21."""
import numpy as np
from scipy.stats import norm
from math import comb, factorial, floor
# Example 1: 10 fair dice, P(30 <= S <= 40)
p = np.zeros(61); p[0] = 1
for _ in range(10):
    q = np.zeros(61)
    for s in range(61):
        if p[s]:
            for f in range(1, 7):
                if s + f <= 60: q[s + f] += p[s] / 6
    p = q
exact = p[30:41].sum()
z = 0.55 / np.sqrt(35 / 120)
print(f"Ex1: exact P(30<=S<=40) = {exact:.4f}; lecture CLT with continuity correction 2*Phi({z:.4f})-1 = {2*norm.cdf(z)-1:.4f}; without correction 2*Phi({0.5/np.sqrt(35/120):.4f})-1 = {2*norm.cdf(0.5/np.sqrt(35/120))-1:.4f}")
# Example 2: 10 iid U(0,1), P(sum > 6): Irwin-Hall
n, x = 10, 6.0
F = sum((-1)**k * comb(n, k) * (x - k)**n for k in range(int(floor(x)) + 1)) / factorial(n)
print(f"Ex2: exact P(S>6) = {1-F:.4f}; lecture CLT 1-Phi(sqrt(1.2)) = {1-norm.cdf(np.sqrt(1.2)):.4f}")
# Cauchy-Schwarz sanity and Jensen example
rng = np.random.default_rng(2); X = rng.exponential(1, 10**6); Y = X + rng.normal(0, 1, 10**6)
print(f"Cauchy-Schwarz check: |E(XY)| = {abs(np.mean(X*Y)):.3f} <= sqrt(E X^2 E Y^2) = {np.sqrt(np.mean(X**2)*np.mean(Y**2)):.3f}")
print(f"Jensen g=x^2: E[g(X)] - g(E X) = Var X = {np.mean(X**2)-np.mean(X)**2:.3f} (Exp(1): 1)")
