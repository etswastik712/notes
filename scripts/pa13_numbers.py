"""PA13 The Derivative and the Inverse Function Theorem: numbers quoted in the chapter, recomputed.

    .venv/bin/python -W ignore scripts/pa13_numbers.py
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(3)

# 1. Matrix derivatives checked by finite differences ---------------------------------------------------------------------
n = 4
X = rng.normal(size=(n, n)) + 3 * np.eye(n)
B = rng.normal(size=(n, n))
t = 1e-6
fd_det = (np.linalg.det(X + t * B) - np.linalg.det(X)) / t
fm_det = np.linalg.det(X) * np.trace(np.linalg.solve(X, B))
print("d(det)_X(B): finite difference %.8f   det(X) tr(X^-1 B) = %.8f   rel. error %.1e" % (fd_det, fm_det, abs(fd_det - fm_det) / abs(fm_det)))
fd_inv = (np.linalg.inv(X + t * B) - np.linalg.inv(X)) / t
fm_inv = -np.linalg.inv(X) @ B @ np.linalg.inv(X)
print("d(inv)_X(B) = -X^-1 B X^-1: max abs error %.1e" % np.abs(fd_inv - fm_inv).max())
fd_sq = ((X + t * B) @ (X + t * B).T - X @ X.T) / t
fm_sq = B @ X.T + X @ B.T
print("d(A A^T)_X(B) = B X^T + X B^T: max abs error %.1e" % np.abs(fd_sq - fm_sq).max())
# at A = I the differential of A -> A A^T is B -> B + B^T: its rank is n(n+1)/2, so the kernel (so(n)) has dimension n(n-1)/2
for m in (2, 3, 4, 5):
    M = np.zeros((m * m, m * m))
    for k in range(m * m):
        E = np.zeros(m * m)
        E[k] = 1
        E = E.reshape(m, m)
        M[:, k] = (E + E.T).reshape(-1)
    r = np.linalg.matrix_rank(M)
    print("  n=%d: rank of B -> B + B^T = %d = n(n+1)/2 = %d;  dim O(n) = n^2 - rank = %d = n(n-1)/2 = %d" % (m, r, m * (m + 1) // 2, m * m - r, m * (m - 1) // 2))

# 2. Banach fixed point for cos x = x on [0, 1] ---------------------------------------------------------------------------
L = np.sin(1.0)                                  # |cos'(x)| = |sin x| <= sin 1 on [0, 1]
x, k = 1.0, 0
x_star = 0.7390851332151607
errs = []
while abs(x - x_star) > 1e-12:
    x = np.cos(x)
    k += 1
    errs.append(abs(x - x_star))
print("cos x = x: Lipschitz constant L = sin 1 = %.6f; iterates from x0 = 1 reach error < 1e-12 after %d steps (limit %.13f)" % (L, k, x))
bound = np.log(1e-12 * (1 - L) / abs(np.cos(1.0) - 1.0)) / np.log(L)
print("  a-priori bound  n >= ln(eps (1-L)/|x1-x0|)/ln L = %.1f steps" % bound)
print("  error ratios of consecutive steps (first five):", [round(errs[i + 1] / errs[i], 4) for i in range(5)], " (tend to |sin x*| = %.4f)" % abs(np.sin(x_star)))

# 3. Inverse function theorem for F(x, y) = (x^2 - y^2, 2xy) (= z -> z^2) near a = (1, 0), solving F(p) = (1.1, 0.2) ------------
def F(p):
    return np.array([p[0] ** 2 - p[1] ** 2, 2 * p[0] * p[1]])


a = np.array([1.0, 0.0])
Da = np.array([[2.0, 0.0], [0.0, 2.0]])
yt = np.array([1.1, 0.2])
z = np.sqrt(complex(*yt))
print("target F(p) = (1.1, 0.2): exact principal root sqrt(1.1+0.2i) = (%.10f, %.10f)" % (z.real, z.imag))
p = a.copy()
hist = []
for it in range(8):
    p = p - np.linalg.solve(Da, F(p) - yt)         # contraction  G(p) = p - DF(a)^-1 (F(p) - y)
    hist.append(np.linalg.norm(p - np.array([z.real, z.imag])))
print("simplified Newton / contraction iterates: errors", ["%.1e" % h for h in hist])
print("  ratio of consecutive errors ~ %.3f  (contraction constant of G near the root: ||I - DF(a)^-1 DF(p*)|| = %.3f)"
      % (hist[4] / hist[3], np.linalg.norm(np.eye(2) - np.linalg.solve(Da, np.array([[2 * z.real, -2 * z.imag], [2 * z.imag, 2 * z.real]])), 2)))

# 4. Implicit function theorem: x^2 + y^2 = 1 near (0, 1) and (1, 0) -------------------------------------------------------
g = lambda x_: np.sqrt(1 - x_ ** 2)
h = 1e-6
print("implicit function y = g(x) = sqrt(1-x^2): g'(0.6) finite difference %.6f, formula -x/g = %.6f" % ((g(0.6 + h) - g(0.6 - h)) / (2 * h), -0.6 / g(0.6)))
print("  dF/dy = 2y: at (0, 1) equals 2 (theorem applies); at (1, 0) equals 0 (it does not: the circle has a vertical tangent there)")

# 5. The rank theorem on a concrete map of constant rank 1:  F(u, v) = (u + v, (u + v)^2) -----------------------------------
u, v, s, t_, a_, b_ = sp.symbols("u v s t a b")
Fm = sp.Matrix([u + v, (u + v) ** 2])
print("rank of DF:", Fm.jacobian([u, v]).rank(), " (constant, also at every point since the rows are proportional)")
phi_inv = sp.Matrix([s - t_, t_])                      # phi(u, v) = (u + v, v), inverse (s, t) -> (s - t, t)
G = sp.simplify(Fm.subs({u: phi_inv[0], v: phi_inv[1]}, simultaneous=True))
print("F o phi^-1 (s, t) =", list(G), " -> H(s) = s^2")
psi = lambda aa, bb: (aa, bb - aa ** 2)                # psi(a, b) = (a, b - a^2)
print("psi o F o phi^-1 (s, t) =", list(sp.simplify(sp.Matrix(psi(G[0], G[1])))), " = (s, 0): normal form (x^1, 0)")

# 6. Practice 2: T(x) = cos(x)/2 is a 1/2-contraction of R --------------------------------------------------------------------
x = 0.0
seq = [x]
for _ in range(9):
    x = 0.5 * np.cos(x)
    seq.append(x)
xs = seq[-1]
for _ in range(100):
    xs = 0.5 * np.cos(xs)
k, x = 0, 0.0
while abs(x - xs) >= 1e-5:
    x = 0.5 * np.cos(x)
    k += 1
print("T = cos(x)/2: iterates from 0:", [round(v, 5) for v in seq], " fixed point %.8f; steps to error < 1e-5: %d; a-priori bound %.1f"
      % (xs, k, np.log(1e-5 * 0.5 / abs(seq[1] - seq[0])) / np.log(0.5)))
