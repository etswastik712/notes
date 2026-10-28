"""Figures for the Fourier and Laplace chapter.   .venv/bin/python -W ignore scripts/fig_ft.py"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *
from scipy import signal

def fig_ft01_gibbs():
    x = np.linspace(-math.pi, math.pi, 4001)
    sq = np.sign(np.sin(x))
    fig, ax = plt.subplots(1, 3, figsize=(11.5, 3.5))
    a = ax[0]; a.plot(x, sq, color=MUTED, lw=1.2)
    for N, c in [(1, BLUE), (3, ORANGE), (10, AQUA)]:
        S = sum(4 / (math.pi * n) * np.sin(n * x) for n in range(1, 2 * N, 2)); a.plot(x, S, color=c, lw=1.4, label=f"{N} term{'s' if N>1 else ''}")
    a.legend(fontsize=8, loc="lower right"); a.set_title("Partial sums", fontsize=10); a.set_xlabel("$x$")
    b = ax[1]; xz = np.linspace(0, 0.5, 2000)
    for N, c in [(5, BLUE), (20, ORANGE), (80, AQUA)]:
        S = sum(4 / (math.pi * n) * np.sin(n * xz) for n in range(1, 2 * N, 2)); b.plot(xz, S, color=c, lw=1.4, label=f"N = {N}")
    b.axhline(1, color=MUTED, lw=1); b.axhline(1.179, color=RED, ls="--", lw=1); b.text(0.27, 1.19, "1.179 (8.95 % of the jump)", color=RED, fontsize=8)
    b.legend(fontsize=8, loc="lower right"); b.set_title("Zoom at the jump", fontsize=10); b.set_xlabel("$x$ (zoom at the jump)")
    c_ = ax[2]; Ns = np.arange(1, 61, 3); xs = np.linspace(0, math.pi, 40001)
    err = [np.sqrt(np.mean((sum(4 / (math.pi * n) * np.sin(n * xs) for n in range(1, 2 * N, 2)) - 1) ** 2)) for N in Ns]
    mx = []
    for N in Ns:
        xf = np.linspace(0, 3 * math.pi / (2 * N), 4000); mx.append(max(sum(4 / (math.pi * n) * np.sin(n * xf) for n in range(1, 2 * N, 2))) - 1)
    c_.plot(Ns, err, "o-", color=BLUE, ms=4, label="rms error over $(0,\\pi)$ (shrinks)"); c_.plot(Ns, mx, "s-", color=RED, ms=4, label="peak overshoot (stays 0.179)")
    c_.set_ylim(0, 0.5); c_.set_xlabel("number of terms $N$"); c_.legend(fontsize=8); c_.set_title("Mean-square yes, uniform no", fontsize=10)
    save(fig, "fig_ft01_gibbs")

def fig_ft02_pairs():
    x = np.linspace(-6, 6, 2001); k = np.linspace(-8, 8, 2001)
    rows = [("Gaussian ($\\sigma=0.8$)", np.exp(-x**2 / (2 * .64)), .8 * np.exp(-.64 * k**2 / 2), BLUE),
            ("rectangle ($|x|<1.3$)", (np.abs(x) < 1.3) * 1.0, np.sqrt(2 / math.pi) * np.sinc(1.3 * k / math.pi) * 1.3, ORANGE),
            ("two-sided exponential", np.exp(-1.3 * np.abs(x)), np.sqrt(2 / math.pi) * 1.3 / (1.3**2 + k**2), AQUA)]
    fig, ax = plt.subplots(3, 2, figsize=(8.6, 6.4))
    for i, (nm, f, F, c) in enumerate(rows):
        ax[i, 0].plot(x, f, color=c); ax[i, 0].set_ylabel(nm, fontsize=8.5); ax[i, 1].plot(k, F, color=c)
        ax[i, 0].set_xlim(-6, 6); ax[i, 1].set_xlim(-8, 8)
    ax[0, 0].set_title("$f(x)$ (what you see in space or time)"); ax[0, 1].set_title("$\\tilde f(k)$ (which waves it contains)")
    ax[2, 0].set_xlabel("$x$"); ax[2, 1].set_xlabel("$k$")
    save(fig, "fig_ft02_pairs")

def fig_ft03_uncertainty():
    fig, ax = plt.subplots(1, 3, figsize=(11.6, 3.6))
    x = np.linspace(-8, 8, 2000); k = np.linspace(-8, 8, 2000)
    for sg, c in [(0.5, BLUE), (1.0, ORANGE), (2.0, AQUA)]:
        ax[0].plot(x, np.exp(-x**2 / (2 * sg * sg)), color=c, label=f"$\\sigma={sg}$")
        ax[1].plot(k, np.exp(-sg * sg * k * k / 2), color=c, label=f"$\\sigma={sg}$")
    ax[0].legend(fontsize=8); ax[0].set_title("Narrow in $x$ ...", fontsize=10); ax[0].set_xlabel("$x$")
    ax[1].legend(fontsize=8); ax[1].set_title("... broad in $k$ (peak-normalised)", fontsize=10); ax[1].set_xlabel("$k$")
    vals = [0.5, math.pi / 6, 0.5476, 1 / math.sqrt(2)]
    ax[2].bar(range(4), vals, color=[BLUE, ORANGE, AQUA, VIOLET], width=.6); ax[2].axhline(.5, color=RED, ls="--", lw=1)
    for i, v in enumerate(vals): ax[2].text(i, v + .01, f"{v:.3f}", ha="center", fontsize=8)
    ax[2].set_xticks(range(4)); ax[2].set_xticklabels(["Gaussian", "sech", "triangle", "$e^{-|x|}$"], fontsize=8.5); ax[2].set_ylim(0.4, .8)
    ax[2].set_title("$\\Delta x\\,\\Delta k\\geq\\frac{1}{2}$, equality only for a Gaussian", fontsize=10)
    save(fig, "fig_ft03_uncertainty")

def fig_ft04_aliasing():
    fs = 10.0; t = np.linspace(0, 2, 2001); ts = np.arange(0, 2, 1 / fs)
    fig, ax = plt.subplots(1, 2, figsize=(10.4, 3.6))
    ax[0].plot(t, np.sin(2 * math.pi * 9 * t), color=MUTED, lw=1, label="true 9 Hz")
    ax[0].plot(t, -np.sin(2 * math.pi * 1 * t), color=ORANGE, lw=1.6, label="alias: 1 Hz")
    ax[0].plot(ts, np.sin(2 * math.pi * 9 * ts), "o", color=BLUE, ms=5, label="samples at 10 Hz"); ax[0].legend(fontsize=7.5, loc="lower right", framealpha=.9); ax[0].set_xlabel("time (s)")
    ax[0].set_title("Sampling a 9 Hz wave at 10 Hz")
    f = np.linspace(0, 20, 400); tr = np.abs(((f + fs / 2) % fs) - fs / 2)
    ax[1].plot(f, tr, color=BLUE); ax[1].axvline(fs / 2, color=RED, ls="--", lw=1); ax[1].text(5.3, 0.3, "Nyquist $f_s/2$", fontsize=8, color=RED)
    ax[1].plot([9], [1], "o", color=ORANGE); ax[1].set_xlabel("true frequency (Hz)"); ax[1].set_ylabel("apparent frequency (Hz)"); ax[1].set_title("Folding: everything above $f_s/2$ is mirrored down")
    save(fig, "fig_ft04_aliasing")

def fig_ft05_window():
    N = 256; n = np.arange(N); f1, f2 = 20.3, 27.0
    y = np.sin(2 * math.pi * f1 * n / N) + 0.01 * np.sin(2 * math.pi * f2 * n / N)
    fig, ax = plt.subplots(1, 2, figsize=(10.2, 3.6))
    for nm, w, c in [("rectangular", np.ones(N), ORANGE), ("Hann", np.hanning(N), BLUE)]:
        Y = np.abs(np.fft.rfft(y * w, 4096)); Y /= Y.max(); fr = np.fft.rfftfreq(4096, 1 / N)
        ax[0].plot(fr, 20 * np.log10(Y + 1e-9), color=c, lw=1.2, label=nm)
    ax[0].set_xlim(0, 60); ax[0].set_ylim(-110, 3); ax[0].axvline(f2, color=MUTED, ls=":", lw=1); ax[0].text(f2 + .5, -20, "weak tone\n(-40 dB) at 27", fontsize=8, color=MUTED)
    ax[0].set_xlabel("frequency (cycles per record)"); ax[0].set_ylabel("dB"); ax[0].legend(fontsize=8); ax[0].set_title("Leakage: the window sets what you can see")
    ax[1].plot(n, np.hanning(N), color=BLUE, label="Hann"); ax[1].plot(n, np.ones(N), color=ORANGE, label="rectangular"); ax[1].legend(fontsize=8); ax[1].set_title("The windows"); ax[1].set_xlabel("sample")
    save(fig, "fig_ft05_window")

def fig_ft06_diffusion_dispersion():
    fig, ax = plt.subplots(1, 3, figsize=(11.6, 3.6))
    x = np.linspace(-60, 60, 800); D = 0.01
    for t, c in [(0, BLUE), (1e3, ORANGE), (1e4, AQUA), (1e5, VIOLET)]:
        s = math.sqrt(25 + 2 * D * t); ax[0].plot(x, 5 / s * np.exp(-x**2 / (2 * s * s)), color=c, label=f"t = {t:g} yr")
    ax[0].legend(fontsize=7.5); ax[0].set_xlabel("$x$ (m)"); ax[0].set_title("Diffusion: Gaussian kernel, $\\sigma^2=\\sigma_0^2+2Dt$")
    kk = np.linspace(0, 2, 200)
    ax[1].plot(kk, np.sqrt(kk), color=BLUE, label="deep water $\\sqrt{gk}$"); ax[1].plot(kk, kk, color=MUTED, label="sound/light $\\omega=ck$")
    ax[1].plot(kk, kk**2 / 2, color=ORANGE, label="quantum $\\omega=\\hbar k^2/2m$"); ax[1].set_ylim(0, 2); ax[1].legend(fontsize=7.5); ax[1].set_xlabel("$k$"); ax[1].set_ylabel("$\\omega$"); ax[1].set_title("Dispersion relations $\\omega(k)$")
    lam = np.logspace(0, 3.5, 100); ax[2].loglog(lam, lam**2 / (4 * math.pi**2 * D), color=BLUE); ax[2].set_xlabel("wavelength (m)"); ax[2].set_ylabel("decay time (yr)")
    ax[2].plot([100], [100**2 / (4 * math.pi**2 * D)], "o", color=ORANGE); ax[2].annotate("100 m: 25 kyr", (100, 2.5e4), xytext=(8, -16), textcoords="offset points", fontsize=8)
    ax[2].set_title("Hillslope diffusion: $\\tau=\\lambda^2/4\\pi^2D$ ($D=0.01$)")
    save(fig, "fig_ft06_diffusion_dispersion")

def fig_ft07_laplace():
    fig, ax = plt.subplots(1, 3, figsize=(11.8, 3.7))
    a = ax[0]; a.axhline(0, color=MUTED, lw=1); a.axvline(0, color=MUTED, lw=1)
    for z, c in [(0.2, BLUE), (0.707, ORANGE), (2.0, AQUA)]:
        r = np.roots([1, 2 * z, 1]); a.plot(r.real, r.imag, "x", color=c, ms=9, mew=2, label=f"$\\zeta={z}$")
    a.axvspan(-2, 0, color=AQUA, alpha=.06); a.set_xlim(-4, 1.5); a.set_ylim(-1.5, 1.5); a.set_xlabel("Re $s$ (decay rate)"); a.set_ylabel("Im $s$ (frequency)")
    a.legend(fontsize=8, loc="upper left"); a.set_title("Poles of $1/(s^2+2\\zeta s+1)$")
    b = ax[1]; tt = np.linspace(0, 20, 2000)
    for z, c in [(0.2, BLUE), (0.707, ORANGE), (2.0, AQUA)]:
        t, y = signal.step(signal.TransferFunction([1], [1, 2 * z, 1]), T=tt); b.plot(t, y, color=c, label=f"$\\zeta={z}$")
    b.axhline(1, color=MUTED, lw=1, ls=":"); b.set_xlabel("$t$"); b.set_title("Step responses: overshoot $e^{-\\pi\\zeta/\\sqrt{1-\\zeta^2}}$"); b.legend(fontsize=8)
    c_ = ax[2]; w = np.logspace(-2, 2, 300)
    c_.loglog(w, 1 / np.sqrt(1 + w**2), color=BLUE, label="$1/(1+\\tau s)$, relaxation (LS01)")
    for z, c in [(0.2, ORANGE), (0.707, AQUA)]:
        H = 1 / np.abs(1 - w**2 + 2j * z * w); c_.loglog(w, H, color=c, label=f"oscillator $\\zeta={z}$")
    c_.set_ylim(1e-4, 10); c_.set_xlabel("$\\omega\\tau$"); c_.set_title("Frequency response $|H(i\\omega)|$"); c_.legend(fontsize=7.5, loc="lower left")
    save(fig, "fig_ft07_laplace")

def fig_ft08_dft_characters():
    N = 8; n = np.arange(N); F = np.exp(-2j * np.pi * np.outer(n, n) / N)
    fig, ax = plt.subplots(1, 3, figsize=(11, 3.5))
    ax[0].imshow(F.real, cmap="RdBu", vmin=-1, vmax=1); ax[0].set_title("Re of the DFT matrix $\\omega^{jk}$\n(rows = characters of $\\mathbb{Z}_8$)", fontsize=9.5); ax[0].grid(False)
    ax[1].imshow(F.imag, cmap="RdBu", vmin=-1, vmax=1); ax[1].set_title("Im of the DFT matrix", fontsize=9.5); ax[1].grid(False)
    G = np.abs(F @ F.conj().T) / N; ax[2].imshow(G, cmap="Greys", vmin=0, vmax=1); ax[2].set_title("$|FF^\\dagger|/N$: orthogonality = identity", fontsize=9.5); ax[2].grid(False)
    for a in ax: a.set_xticks(range(N)); a.set_yticks(range(N))
    save(fig, "fig_ft08_dft_characters")

if __name__ == "__main__":
    for f in (fig_ft01_gibbs, fig_ft02_pairs, fig_ft03_uncertainty, fig_ft04_aliasing, fig_ft05_window, fig_ft06_diffusion_dispersion, fig_ft07_laplace, fig_ft08_dft_characters): f()
