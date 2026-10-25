"""PR02 - Bayes' rule: posterior vs prevalence, and natural frequencies for the class disease-test example."""
from figlib import *

fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.0), gridspec_kw=dict(width_ratios=[1.15, 1]))
a = axes[0]
pr = np.linspace(0.0005, 0.6, 600)
post = lambda sens, fpr: sens * pr / (sens * pr + fpr * (1 - pr))
a.plot(pr * 100, post(0.95, 0.01) * 100, color=BLUE, label="sensitivity 95 %, false positives 1 %")
a.plot(pr * 100, post(0.95, 0.05) * 100, color=ORANGE, label="sensitivity 95 %, false positives 5 %")
for x, y, lab, c in ((0.5, 32.3, "class example\n0.5 % → 32.3 %", BLUE), (1.0, 16.1, "problem sheet\n1 % → 16.1 % (95/95)", ORANGE)):
    a.plot([x], [y], "o", color=c, ms=7); a.annotate(lab, (x, y), xytext=(x + 6, y - 14 if c == ORANGE else y + 2), fontsize=8.2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
a.set_xlabel("prevalence $P(D)$ (%)"); a.set_ylabel("$P(D\\mid\\text{positive})$ (%)"); a.set_ylim(0, 100); a.legend(fontsize=8.2, loc="lower right")
a.set_title("A  the same test, very different posteriors", fontsize=10)
b = axes[1]
N = 10000; d = 0.005 * N; h = N - d
tp, fp = 0.95 * d, 0.01 * h
bars = [("diseased\n(50)", d, MUTED), ("test +\n(47.5)", tp, BLUE), ("healthy\n(9,950)", h, MUTED), ("test +\n(99.5)", fp, ORANGE)]
xs = [0, 1, 3, 4]
b.bar(xs[0], d, color=MUTED, alpha=0.5); b.bar(xs[1], tp, color=BLUE)
b.bar(xs[2], h, color=MUTED, alpha=0.5); b.bar(xs[3], fp, color=ORANGE)
for x, (lab, v, c) in zip(xs, bars): b.text(x, v + 160, f"{v:,.1f}".rstrip("0").rstrip(".") if v % 1 else f"{v:,.0f}", ha="center", fontsize=8.6)
b.set_xticks(xs); b.set_xticklabels([x[0] for x in bars], fontsize=8.0); b.set_ylim(0, 11000); b.grid(axis="x", visible=False)
b.text(2, 4600, "of 147 positives,\n47.5 are real:\n$47.5/147=32\\%$", ha="center", fontsize=9)
b.set_ylabel("people out of 10,000"); b.set_title("B  natural frequencies", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "$P(D|+)=\\dfrac{0.95\\times0.005}{0.95\\times0.005+0.01\\times0.995}=0.323$. Computed (scripts/pr_numbers.py).", ha="center", fontsize=8.2, color=MUTED)
save(fig, "fig_pr02_bayes")
