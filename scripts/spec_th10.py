"""Concept notes for TH10 (open systems, mixing, reacting gases).   .venv/bin/python -W ignore scripts/spec_th10.py"""
from mkconcept import write

CH = "TH10 Open Systems Mixing and Reacting Gases"
T, EBY = "taught", "extra-beyond"
BY = ["lecture-notes", "own-notes"]
BH = "[[Bhagwat.pdf#page=1|Bhagwat notes]]"

ITEMS = [
    dict(title="Open System Energy Balance", aliases=["big equation", "energy balance of an open system", "flow work", "steady-flow enthalpy balance", "throttling", "tank filling"], scope=[T, EBY], by=BY,
         syl={T: f"{BH}, p. 1: $\\mathrm dU^{{\\rm t}}/\\mathrm dt=\\dot Q-P\\,\\mathrm dV^{{\\rm t}}/\\mathrm dt+\\dot n(U+PV)+\\dot W$ and its closed, no-work case.", EBY: "the steady-flow form, the entropy balance examples (heater, throttle, tank filling) (mine, checked)."},
         intuition="Energy in minus energy out equals energy accumulated: heat crosses the boundary, work crosses it, and **matter carries $U+PV=H$ across it** (its energy plus the work of pushing it in).",
         key="$\\dfrac{\\mathrm dU^{\\rm t}}{\\mathrm dt}=\\dot Q-P\\dfrac{\\mathrm dV^{\\rm t}}{\\mathrm dt}+\\dot n(U+PV)+\\dot W$, with $\\dot n$ the net molar inflow and $\\dot W$ all non-$PV$ work. Closed, no work: the first law. **Steady flow:** $\\sum\\dot nH_{\\rm in}-\\sum\\dot nH_{\\rm out}+\\dot Q+\\dot W=0$. Entropy: $\\mathrm dS^{\\rm t}/\\mathrm dt=\\dot Q/T+\\dot nS+\\dot S_{\\rm gen}$, $\\dot S_{\\rm gen}\\ge0$.",
         body="**Throttle** ($\\dot Q=\\dot W=0$): $H_{\\rm in}=H_{\\rm out}$, $T$ unchanged for an ideal gas, $\\dot S_{\\rm gen}=\\dot nR\\ln(P_{\\rm in}/P_{\\rm out})$ ($10\\to1$ bar, 1 mol s$^{-1}$: $19.15$ W K$^{-1}$). **Tank filling** (rigid, adiabatic, evacuated): $U_{\\rm final}=NH_{\\rm line}$, $T_f=\\gamma T_{\\rm line}$ ($420$ K for a 300 K diatomic line). **Heater** 300→600 K, 1 mol s$^{-1}$: $\\dot Q=8730$ W.",
         used=[CH, "TH02 Work Heat and the First Law"], related=["Entropy Production", "Enthalpy", "First Law of Thermodynamics", "Joule-Thomson Effect", "Gibbs Free Energy"]),
    dict(title="Entropy of Mixing of Ideal Gases", aliases=["Delta S_mix", "Gibbs energy of mixing", "mixing of ideal gases", "-R sum n ln x", "isothermal expansion into the partial pressure"], scope=[T, EBY], by=BY,
         syl={T: f"{BH}, pp. 3–4: $\\Delta S_i=-n_iR\\ln x_i$, $\\Delta H_{{\\rm mix}}=0$, $\\Delta G_{{\\rm mix}}=RT\\sum n_i\\ln x_i$.", EBY: "numbers for air and $N$ components, the work to separate air (mine, checked)."},
         intuition="Each gas, after mixing, occupies the whole volume at its **partial pressure** $x_iP$: mixing is an isothermal expansion of each gas from $P$ to $x_iP$. Nothing exchanges energy; the entropy rises because each molecule has more room.",
         key="$\\Delta S_{\\rm mix}=-R\\sum_in_i\\ln x_i=-nR\\sum x_i\\ln x_i>0$; $\\Delta H_{\\rm mix}=0$ (ideal gas: $\\mathrm dH=T\\mathrm dS+V\\mathrm dP=0$ at constant $T$); $\\Delta G_{\\rm mix}=RT\\sum n_i\\ln x_i<0$; $\\mu_i=\\mu_i^\\circ+RT\\ln(x_iP/P^\\circ)$. Maximum $R\\ln N$ at equal fractions.",
         body="Numbers at 298.15 K: equimolar binary $5.763$ J mol$^{-1}$K$^{-1}$, $\\Delta G=-1.718$ kJ mol$^{-1}$; air-like $0.79/0.21$: $4.273$, $-1.274$ kJ mol$^{-1}$ (the minimum work to separate air). For *identical* gases $\\Delta S=0$: the Gibbs paradox.",
         used=[CH, "TH05 Potentials Maxwell Relations Stability and the Third Law"], related=["Gibbs Paradox", "Chemical Potential", "Gibbs Free Energy", "Entropy Production", "Maxwell Relations"]),
    dict(title="Extent of Reaction", aliases=["reaction coordinate", "advancement of a reaction", "n_i = n_i0 + nu_i xi", "driving force of a reaction", "limiting reagent"], scope=[T, EBY], by=BY,
         syl={T: f"{BH}, p. 4: $n_i=n_i^0+\\nu_i\\varepsilon$, $\\mathrm dG^{{\\rm t}}=\\sum\\mu_i\\mathrm dn_i=(\\sum\\nu_i\\mu_i)\\mathrm d\\varepsilon$.", EBY: "the interior minimum of $G(\\varepsilon)$ and the numerical tables (mine)."},
         intuition="One number, $\\varepsilon$, counts how far the reaction has gone: every species changes by $\\nu_i\\varepsilon$ moles; the Gibbs energy of the whole mixture, as a function of $\\varepsilon$, is a bowl and equilibrium is the bottom.",
         key="For $\\sum\\nu_iA_i=0$ ($\\nu<0$ reactants): $n_i=n_i^0+\\nu_i\\varepsilon$. At constant $T,P$: $(\\partial G^{\\rm t}/\\partial\\varepsilon)_{T,P}=\\sum_i\\nu_i\\mu_i=\\Delta_rG=RT\\ln(Q/K)$; zero at equilibrium.",
         body="$\\mathrm{SO_2}+\\tfrac12\\mathrm{O_2}\\rightleftharpoons\\mathrm{SO_3}$ from $1$ mol SO$_2$ and $\\tfrac12$ mol O$_2$: moles $(1-\\varepsilon,\\tfrac{1-\\varepsilon}2,\\varepsilon)$. $\\partial G/\\partial\\varepsilon\\to-\\infty$ at $\\varepsilon\\to0$ and $+\\infty$ at the end: the minimum is interior (entropy of mixing), so no ideal-gas reaction goes to completion.",
         used=[CH, "TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries"], related=["Equilibrium Constant", "Law of Mass Action", "Chemical Potential", "Pressure Dependence of Chemical Equilibrium", "Gibbs Free Energy"]),
    dict(title="Pressure Dependence of Chemical Equilibrium", aliases=["Le Chatelier's principle for pressure", "K = prod x^nu (P/P0)^(sum nu)", "inert gas and equilibrium", "effect of pressure on equilibrium composition"], scope=[T, EBY], by=BY,
         syl={T: f"{BH}, pp. 4–5: if $\\sum\\nu_i=0$ the pressure factors cancel; $\\sum\\nu_i=-\\tfrac12$: $K\\propto P^{-1/2}$, higher $P$ pushes the reaction forward.", EBY: "inert gas at constant $P$ versus constant $V$, the $\\Delta\\nu=0,+1$ examples, tables (mine)."},
         intuition="$K$ depends on temperature only, but the **composition** that satisfies it depends on pressure through the number of moles of gas: squeezing favours the side with fewer moles.",
         key="$K=\\prod_i(x_iP/P^\\circ)^{\\nu_i}=\\big[\\prod x_i^{\\nu_i}\\big](P/P^\\circ)^{\\sum\\nu_i}$. $\\Sigma\\nu<0$: higher $P$ favours products; $\\Sigma\\nu>0$: reactants; $\\Sigma\\nu=0$: no effect. Inert gas at constant total $P$ lowers all partial pressures (acts like lower $P$); at constant $V$ and $T$ it changes nothing.",
         body="$K=10$ (illustrative), SO$_2$/SO$_3$: $\\varepsilon_{\\rm eq}=0.5707,\\ 0.7645,\\ 0.8819,\\ 0.9547$ at $0.1,\\ 1,\\ 10,\\ 200$ bar; with $3$ mol inert at 1 bar: $0.6667$. N$_2$O$_4\\rightleftharpoons2$NO$_2$ ($K=0.15$): $\\varepsilon=\\sqrt{K/(K+4P)}=0.522,\\ 0.190,\\ 0.061$ at $0.1,\\ 1,\\ 10$ bar.",
         used=[CH, "TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries"], related=["Extent of Reaction", "Equilibrium Constant", "Van 't Hoff Equation", "Law of Mass Action", "Chemical Potential"]),
]

if __name__ == "__main__":
    write("03-Thermodynamics-and-Statistical-Mechanics", "thermo", ITEMS)
