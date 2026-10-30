"""PA15 Covering Spaces and the Fundamental Group: numbers quoted in the chapter, recomputed.

    .venv/bin/python -W ignore scripts/pa15_numbers.py
"""
import numpy as np

T = np.linspace(0, 1, 200001)


def lift_end(loop):
    """Lift of a loop in S^1 = {|z| = 1} through p(t) = exp(2 pi i t), starting at 0: the continuous argument, unwrapped."""
    ang = np.unwrap(np.angle(loop)) / (2 * np.pi)
    return ang[-1] - ang[0]


def winding(loop):
    """Winding number around 0 of a closed curve in C \\ {0}: end of the lift of loop / |loop|."""
    return lift_end(loop / np.abs(loop))


# 1. Winding numbers (= the class in pi_1(S^1) = Z via path lifting) --------------------------------------------------------
loops = {
    "e^{2 pi i 3 t}": np.exp(2j * np.pi * 3 * T),
    "e^{-2 pi i 2 t}": np.exp(-2j * np.pi * 2 * T),
    "wobbly loop e^{2 pi i (3t + 0.2 sin 2 pi t)}": np.exp(2j * np.pi * (3 * T + 0.2 * np.sin(2 * np.pi * T))),
    "unit circle centred at 0.5": 0.5 + np.exp(2j * np.pi * T),
    "circle of radius 0.3 centred at 0.5": 0.5 + 0.3 * np.exp(2j * np.pi * T),
    "circle of radius 1 centred at 0.99": 0.99 + np.exp(2j * np.pi * T),
    "circle of radius 1 centred at 1.01": 1.01 + np.exp(2j * np.pi * T),
}
print("winding numbers (end of the lift through R -> S^1):")
for name, z in loops.items():
    w = winding(z)
    print("  %-48s %+.6f" % (name, w))

# a torus loop (e^{2 pi i t}, e^{4 pi i t}) has class (1, 2) in pi_1(T^2) = Z^2
c1, c2 = lift_end(np.exp(2j * np.pi * T)), lift_end(np.exp(4j * np.pi * T))
print("loop (e^{2 pi i t}, e^{4 pi i t}) in T^2 = S^1 x S^1: class (%.0f, %.0f) in Z^2" % (c1, c2))

# z -> z^k induces multiplication by k on pi_1(S^1) = Z
for k in (2, 3, 5):
    z = np.exp(2j * np.pi * T)
    print("  z -> z^%d sends the generator (class 1) to class %.0f" % (k, lift_end(z ** k)))

# 2. SU(2) -> SO(3): the 2-sheeted covering, checked on random unit quaternions -----------------------------------------------
def R(q):
    w, x, y, z = q
    return np.array([
        [1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
        [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
        [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)],
    ])


def qmul(a, b):
    w1, x1, y1, z1 = a
    w2, x2, y2, z2 = b
    return np.array([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2, w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2, w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2])


rng = np.random.default_rng(5)
err_hom = err_orth = err_det = err_pm = 0.0
for _ in range(1000):
    a = rng.normal(size=4)
    a /= np.linalg.norm(a)
    b = rng.normal(size=4)
    b /= np.linalg.norm(b)
    err_hom = max(err_hom, np.abs(R(qmul(a, b)) - R(a) @ R(b)).max())
    err_orth = max(err_orth, np.abs(R(a) @ R(a).T - np.eye(3)).max())
    err_det = max(err_det, abs(np.linalg.det(R(a)) - 1))
    err_pm = max(err_pm, np.abs(R(-a) - R(a)).max())
print("SU(2) = unit quaternions -> SO(3), 1000 random pairs: max |R(ab) - R(a)R(b)| = %.1e, orthogonality error %.1e, |det - 1| %.1e, |R(-a) - R(a)| = %.1e"
      % (err_hom, err_orth, err_det, err_pm))
# the loop in SO(3): rotation by 2 pi t about z, lifts to q(t) = (cos pi t, 0, 0, sin pi t), which ends at -1, not +1
q1 = np.array([np.cos(np.pi), 0, 0, np.sin(np.pi)])
print("loop t -> rotation by 2 pi t about the z-axis: R(1) - I = %.1e (a closed loop in SO(3)), but its lift q(1) = (%.3f, %.3f, %.3f, %.3f) = -1 != +1" % (np.abs(R(q1) - np.eye(3)).max(), *q1))
q2 = np.array([np.cos(2 * np.pi), 0, 0, np.sin(2 * np.pi)])
print("  going around twice (t in [0, 2]): the lift ends at q(2) = (%.3f, %.3f, %.3f, %.3f) = +1: a closed loop in S^3, null-homotopic, so the class has order 2" % tuple(q2))

# 3. Sheets of S^n -> RP^n and the Z^n lattice quotient ------------------------------------------------------------------------
x = rng.normal(size=4)
x /= np.linalg.norm(x)
print("S^3 -> RP^3: the fibre over [x] is {x, -x}: 2 sheets; R^2 -> T^2: fibre Z^2 (countably many sheets)")
