"""CL02 - 'folding or Fourier transforming can reveal periodicity in noisy data' (Argha L2 slide 19) on SYNTHETIC hourly data.

Synthetic Pune-like record, NOT measurements:
  T(t) = 24.5 + 3.5 cos(2pi (d - 125)/365.25)         annual cycle (peak in early May)
              + 6.0 cos(2pi (h - 14)/24) + 1.2 cos(2pi (h - 14)/12)   daily cycle with a 12 h harmonic
              + AR(1) 'weather' noise (sd 1.8 K, memory 2 days)
Panels: 45-day hourly snippet; the data folded modulo 24 h (mean +/- sd by hour); FFT amplitude spectrum.
Prints the recovered amplitudes next to the ones put in.
"""
from figlib import *

rng = np.random.default_rng(42)
years = 10
n = 3652 * 24                                   # 3652 whole days of hourly samples (~10 yr)
t = np.arange(n) / 24.0                         # days
h = (np.arange(n) % 24).astype(float)           # hour of day (integer hours)
A_y, A_d, A_d2, T0, SD, TAU = 3.5, 6.0, 1.2, 24.5, 1.8, 2.0
phi = np.exp(-1 / (TAU * 24))                   # hourly AR(1) coefficient for a 2-day memory
e = np.zeros(n)
w = rng.normal(0, SD * np.sqrt(1 - phi**2), n)
for i in range(1, n):
    e[i] = phi * e[i - 1] + w[i]
T = T0 + A_y * np.cos(2 * np.pi * (t - 125) / 365.25) + A_d * np.cos(2 * np.pi * (h - 14) / 24) + A_d2 * np.cos(2 * np.pi * (h - 14) / 12) + e

# fold by hour of day
hh = np.arange(24)
comp = T.reshape(-1, 24).T
m, s = comp.mean(axis=1), comp.std(axis=1)
# the folded mean also contains the annual cycle averaged out; the diurnal amplitude is (max-min)/2 of the composite
print(f"folded composite: peak {m.max():.1f} C at {int(m.argmax())} h, trough {m.min():.1f} C at {int(m.argmin())} h, half-range {(m.max()-m.min())/2:.2f} (input fundamental {A_d}, plus harmonic)")
# FFT amplitude spectrum
X = np.fft.rfft(T - T.mean())
f = np.fft.rfftfreq(n, d=1.0 / 24)               # cycles per day
amp = 2 * np.abs(X) / n
k_y = np.argmin(abs(f - 1 / 365.25)); k_d = np.argmin(abs(f - 1.0)); k_d2 = np.argmin(abs(f - 2.0))
print(f"FFT amplitude: annual {amp[k_y]:.2f} (in {A_y}), daily {amp[k_d]:.2f} (in {A_d}), 12 h {amp[k_d2]:.2f} (in {A_d2});  noise floor median {np.median(amp[(f>3)&(f<10)]):.3f}")

fig, axs = plt.subplots(1, 3, figsize=(11.6, 3.5))
ax = axs[0]
k = (t > 120) & (t < 165)
ax.plot(t[k], T[k], color=BLUE, lw=0.8)
ax.set_xlabel("day of record")
ax.set_ylabel("T (°C)")
ax.set_title("1  hourly data: noisy", fontsize=10)
ax = axs[1]
ax.fill_between(hh, m - s, m + s, color=ORANGE, alpha=0.2, lw=0)
ax.plot(hh, m, color=ORANGE, lw=2)
ax.set_xlabel("hour of day")
ax.set_title("2  folded modulo 24 h: the daily cycle appears", fontsize=10)
ax.set_xlim(0, 23)
ax = axs[2]
ax.loglog(f[1:], amp[1:], color=INK, lw=0.8)
for kk, lab, dx in [(k_y, "1 yr", 1.4), (k_d, "1 day", 1.4), (k_d2, "12 h", 1.4)]:
    ax.plot([f[kk]], [amp[kk]], "o", color=RED, ms=5)
    ax.annotate(lab, (f[kk], amp[kk]), xytext=(5, 4), textcoords="offset points", fontsize=8.5)
ax.set_xlabel("frequency (cycles per day)")
ax.set_ylabel("amplitude (°C)")
ax.set_title("3  Fourier spectrum: peaks above the noise", fontsize=10)
fig.suptitle("Synthetic Pune-like temperature record (not measurements): three ways of looking at the same noisy series", fontsize=10.5, y=1.02)
fig.tight_layout()
save(fig, "fig_cl02_fold_fft")
