"""PR - conceptual diagrams (SVG + Excalidraw).   .venv/bin/python scripts/diagrams_pr.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagrams import excalidraw, svg

SPECS = {
    "PR03 The Discrete Distribution Family": dict(
        size=(940, 520),
        nodes={
            "B": dict(x=170, y=110, w=240, h=84, text="Bernoulli(p)\none trial, 0 or 1\nmean p, var p(1-p)", color="blue"),
            "Bi": dict(x=470, y=110, w=250, h=84, text="Binomial(n, p)\nsum of n independent\nmean np, var np(1-p)", color="blue"),
            "Po": dict(x=790, y=110, w=240, h=84, text="Poisson(lambda)\nlimit n -> inf, np -> lambda\nmean = var = lambda", color="aqua"),
            "G": dict(x=170, y=290, w=240, h=84, text="Geometric(p)\ntrials to first success\nmean 1/p, var (1-p)/p^2", color="orange"),
            "NB": dict(x=470, y=290, w=250, h=84, text="Negative binomial(k, p)\nsum of k geometrics\nmean k/p, var k(1-p)/p^2", color="orange"),
            "H": dict(x=790, y=290, w=240, h=84, text="Hypergeometric\nsampling WITHOUT replacement\nmean n w/(w+b)", color="grey"),
            "U": dict(x=170, y=450, w=240, h=70, text="Discrete uniform\non {1,...,n}: 1/n", color="grey"),
        },
        arrows=[("B", "Bi", "sum"), ("Bi", "Po", "limit"), ("B", "G", "wait"), ("G", "NB", "sum"), ("Bi", "H", "w/o replacement")],
        title="The discrete catalogue: what each distribution counts and how they are related",
        footer="MT2113 class notes 20 Aug - 9 Sep 2026: Bernoulli, binomial, hypergeometric, uniform, geometric, negative binomial, Poisson (limit of Binomial(n, c/n))",
    ),
}

if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
