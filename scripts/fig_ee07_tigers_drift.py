"""EE07 - A the Indian tiger estimates quoted on slides 22-25 (data from the slides); B heterozygosity lost to drift (my computation)."""
from figlib import *

fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.1), gridspec_kw=dict(width_ratios=[1.15, 1]))
a = axes[0]
yrs = [1972, 2008, 2011, 2018]
val = [1827, 1411, 1706, 2967]
a.bar([1972, 2008, 2011, 2018], val, width=2.8, color=[MUTED, BLUE, BLUE, AQUA])
a.errorbar([2018], [2967], yerr=[[2967 - 2603], [3346 - 2967]], color=INK, capsize=4, lw=1.4)
a.bar([1984], [4000], width=2.8, color="white", edgecolor=MUTED, hatch="///", lw=1.0)
a.text(1984, 4060, ">4,000 by about 1984\n(questioned)", ha="center", fontsize=8.2)
for x, v in zip(yrs, val):
    if x == 2018:
        a.text(x, 3346 + 70, f"{v:,}", ha="center", fontsize=8.8, va="bottom")
    elif x == 2008:
        a.text(2009.3, v + 60, f"{v:,}", ha="right", fontsize=8.8, va="bottom")
    elif x == 2011:
        a.text(2009.9, v + 60, f"{v:,}", ha="left", fontsize=8.8, va="bottom")
    else:
        a.text(x, v + 60, f"{v:,}", ha="center", fontsize=8.8, va="bottom")
a.text(1967, 2500, "1973: Project Tiger\nlaunched, 9 reserves\n(13,017 km²)", fontsize=8.2, color=MUTED)
a.text(2000, 2250, "2006: NTCA\nlaw", fontsize=8.2, color=MUTED, ha="center")
a.set_xlim(1966, 2024); a.set_ylim(0, 4900)
a.set_xlabel("year"); a.set_ylabel("tigers in India (estimate)")
a.set_title("A  the numbers on the slides", fontsize=10)
a.grid(axis="x", visible=False)

b = axes[1]
t = np.arange(0, 201)
for Ne, c in ((10, RED), (50, ORANGE), (500, BLUE)):
    b.plot(t, (1 - 1 / (2 * Ne)) ** t, color=c, label=f"$N_e={Ne}$")
b.axhline(0.5, color=INK, lw=0.8, ls=":")
b.set_xlabel("generations"); b.set_ylabel("heterozygosity left, $H_t/H_0$")
b.legend(fontsize=8.8, loc="center right", bbox_to_anchor=(1.0, 0.33))
b.set_title("B  drift erodes variation fastest in small populations", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.04, "A: slide data (the 4,000 figure is flagged as questioned on the slide; 2018 bar shows the 2,603-3,346 range). Years between the bars are not data. B: my computation, "
         "H_t = H_0 (1 - 1/2N_e)^t.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_ee07_tigers_drift")
