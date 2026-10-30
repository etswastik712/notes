"""PA14 ODE: Existence, Uniqueness and Smooth Dependence: numbers quoted in the chapter, recomputed.

    .venv/bin/python -W ignore scripts/pa14_numbers.py
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.special import ellipk

TOL = dict(rtol=1e-12, atol=1e-13)

# 1. Picard iteration for x' = x, x(0) = 1: the n-th iterate is the Taylor polynomial of e^t -------------------------------
t = sp.symbols("t")
x_k = sp.Integer(1)
print("Picard iterates for x' = x, x(0) = 1 and the error at t = 1:")
for k in range(0, 7):
    print("  k=%d  x_k(t) = %-48s  x_k(1) = %.6f  error = %.2e" % (k, sp.expand(x_k), float(x_k.subs(t, 1)), abs(float(x_k.subs(t, 1)) - np.e)))
    x_k = 1 + sp.integrate(x_k, (t, 0, t))
# contraction constant of the Picard map on C([0, a]): L = a * Lip(f); for f(x) = x on [0, 1/2], L = 1/2

# 2. Finite-time blow-up: x' = x^2, x(0) = x0 has x(t) = x0/(1 - x0 t), maximal interval (-inf, 1/x0) ---------------------
for x0 in (1.0, 2.0):
    tb = 1 / x0
    sol = solve_ivp(lambda tt, y: y ** 2, (0, 0.99 * tb), [x0], dense_output=True, **TOL)
    exact = x0 / (1 - x0 * 0.99 * tb)
    print("x' = x^2, x0 = %g: blow-up time 1/x0 = %g;  numeric x(0.99/x0) = %.6f, formula %.6f (%.1f x0)" % (x0, tb, sol.y[0, -1], exact, exact / x0))

# 3. Non-uniqueness without a Lipschitz condition: x' = sqrt(|x|), x(0) = 0 -----------------------------------------------
c = 1.0
print("x' = sqrt|x|, x(0) = 0 has x = 0 and x = t^2/4 for t >= 0 (and x = (t - c)^2/4 for t >= c: a whole family):")
tt = np.linspace(0, 3, 7)
print("  check x = t^2/4: residual |x' - sqrt|x||_max = %.1e" % np.abs(tt / 2 - np.sqrt(tt ** 2 / 4)).max())

# 4. The flow of V = y d/dx + d/dy (MT3184 HW7 Q5): theta_t(a, b) = (a + b t + t^2/2, b + t) -------------------------------
def V(_, p):
    return [p[1], 1.0]


worst = 0.0
for a, b in ((0.0, 0.0), (1.0, -2.0), (-3.0, 0.5)):
    sol = solve_ivp(V, (0, 2), [a, b], dense_output=True, **TOL)
    for tv in (0.5, 1.0, 2.0):
        exact = np.array([a + b * tv + tv ** 2 / 2, b + tv])
        worst = max(worst, np.abs(sol.sol(tv) - exact).max())
print("flow of y d/dx + d/dy: max |numeric - (a + b t + t^2/2, b + t)| over 9 test points = %.1e" % worst)

# rotation field W = -y d/dx + x d/dy: theta_t is rotation by t
W = lambda _, p: [-p[1], p[0]]
sol = solve_ivp(W, (0, 2 * np.pi), [1.0, 0.0], **TOL)
print("rotation field from (1, 0): after t = 2 pi the solution is back at (%.9f, %.9f) (periodic orbit, period 2 pi)" % tuple(sol.y[:, -1]))

# 5. Smooth dependence: for x' = x^2 the derivative with respect to x0 is 1/(1 - x0 t)^2 (variational equation) -------------
x0, tv, h = 1.0, 0.5, 1e-6
f = lambda xi: solve_ivp(lambda tt, y: y ** 2, (0, tv), [xi], **TOL).y[0, -1]
fd = (f(x0 + h) - f(x0 - h)) / (2 * h)
print("d x(0.5; x0)/d x0 at x0 = 1: finite difference %.6f, formula 1/(1 - x0 t)^2 = %.6f" % (fd, 1 / (1 - x0 * tv) ** 2))
# variational equation: y' = 2 x y, y(0) = 1, with x' = x^2
sol = solve_ivp(lambda tt, z: [z[0] ** 2, 2 * z[0] * z[1]], (0, tv), [x0, 1.0], **TOL)
print("variational equation y' = 2 x y: y(0.5) = %.6f" % sol.y[1, -1])

# 6. Pendulum theta'' = -(g/l) sin theta reduced to a first-order system (theta, omega)' = (omega, -sin theta), g/l = 1 --------
def pend(_, s):
    return [s[1], -np.sin(s[0])]


print("pendulum period (g/l = 1): small amplitude 2 pi = %.4f" % (2 * np.pi))
for th0 in (0.1, np.pi / 2, 2.5):
    ev = lambda tt, s: s[1]          # omega = 0 at a turning point; the first one (theta = -theta0) comes after HALF a period
    ev.terminal = True
    ev.direction = 1
    sol = solve_ivp(pend, (0, 50), [th0, 0.0], events=ev, **TOL)
    T_num = 2 * sol.t_events[0][0] if len(sol.t_events[0]) else float("nan")
    T_exact = 4 * ellipk(np.sin(th0 / 2) ** 2)
    print("  amplitude %.4f rad (%.0f deg): period numeric %.6f, 4 K(sin^2(theta0/2)) = %.6f" % (th0, np.degrees(th0), T_num, T_exact))
