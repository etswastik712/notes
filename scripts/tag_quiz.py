"""Tag every note and section related to the 2026-11-13 quizzes (idempotent).
   Thermodynamics TD2213 Tutorials 1-2:      quiz/thermo, quiz/th-tut1, quiz/th-tut2, quiz/th-background
   Probability Homework 4-6:                 quiz/probability, quiz/pr-hw4, quiz/pr-hw5, quiz/pr-hw6
   Proofs: induction and WOP assignments:    quiz/proofs, quiz/pa-induction, quiz/pa-strong, quiz/pa-wop
   .venv/bin/python -W ignore scripts/tag_quiz.py [--dry]
"""
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TH, PR, PA = "03-Thermodynamics-and-Statistical-Mechanics", "08-Probability", "11-Proofs-Analysis-Topology"
DRY = "--dry" in sys.argv

# ---- frontmatter tags: file -> tags ------------------------------------------------------------------
FM = {}
def fm(path, *tags):
    FM.setdefault(path, [])
    for t in tags:
        if t not in FM[path]:
            FM[path].append(t)
TUT1, TUT2, BG = "quiz/th-tut1", "quiz/th-tut2", "quiz/th-background"
fm(f"{TH}/TH07 Enthalpy Thermochemistry and Calorimetry.md", "quiz/thermo", TUT1, TUT2)
fm(f"{TH}/TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries.md", "quiz/thermo", TUT1, TUT2)
fm(f"{TH}/TH04 The Second Law Carnot Engines and Entropy.md", "quiz/thermo", TUT1, BG)
fm(f"{TH}/TH09 Microstates Macrostates and Multiplicity.md", "quiz/thermo", TUT1, BG)
fm(f"{TH}/TH02 Work Heat and the First Law.md", "quiz/thermo", BG)
fm(f"{TH}/TH05 Potentials Maxwell Relations Stability and the Third Law.md", "quiz/thermo", BG)
fm(f"{TH}/TH10 Open Systems Mixing and Reacting Gases.md", "quiz/thermo", BG)
for c, ts in {"Enthalpy": (TUT1, TUT2), "Reaction Enthalpy": (TUT2,), "Standard Enthalpy of Formation": (TUT2,), "Hess's Law": (TUT2,), "Kirchhoff's Law": (TUT2,),
              "Calorimetry": (TUT2,), "Lattice and Hydration Enthalpy": (TUT2,), "Gibbs Free Energy": (TUT1, TUT2), "Gibbs-Helmholtz Equation": (TUT1,),
              "Equilibrium Constant": (TUT1, TUT2), "Van 't Hoff Equation": (TUT1, TUT2), "Entropy Production": (TUT1,), "Trouton's Rule": (TUT1,),
              "Clausius-Clapeyron Relation": (TUT1,), "Law of Mass Action": (TUT2,), "Chemical Potential": (BG,), "Second Law of Thermodynamics": (TUT1, BG),
              "First Law of Thermodynamics": (TUT1, BG), "Internal Energy": (TUT1, BG), "Heat Capacity": (TUT2, BG), "State Function": (TUT2, BG), "Entropy": (TUT1, BG),
              "Kelvin and Clausius Statements": (TUT1, BG)}.items():
    fm(f"{TH}/Concepts/{c}.md", "quiz/thermo", *ts)

HW4, HW5, HW6 = "quiz/pr-hw4", "quiz/pr-hw5", "quiz/pr-hw6"
fm(f"{PR}/PR07 Sums of Independent Variables Covariance and Correlation.md", "quiz/probability", HW4)
fm(f"{PR}/PR08 Order Statistics and the Multinomial Distribution.md", "quiz/probability", HW5)
fm(f"{PR}/PR09 Change of Variables the Multivariate Normal and Products of Uniforms.md", "quiz/probability", HW6)
fm(f"{PR}/PR06 Moments Generating Functions and Limit Theorems.md", "quiz/probability", HW4)          # HW4 Q4 uses the mgf
fm(f"{PR}/PR05 Continuous Random Variables.md", "quiz/probability", HW4, HW5, HW6)                       # exponential, normal, transformations
fm(f"{PR}/PR04 Joint Distributions Expectation and Variance.md", "quiz/probability", HW4, HW5)         # joint laws, covariance, indicators
for c, ts in {"Sum of Independent Random Variables": (HW4,), "Covariance Matrix": (HW4, HW6), "Covariance and Correlation": (HW4,), "Normal Distribution": (HW4, HW6),
              "Standard Normal Distribution": (HW4, HW6), "Folded Normal Distribution": (HW4,), "Moment Generating Function": (HW4, HW6), "Joint Density Function": (HW4, HW5),
              "Independence of Random Variables": (HW4, HW5, HW6), "Order Statistics": (HW5,), "Joint Density of Order Statistics": (HW5,), "Exponential Order Statistics": (HW5,),
              "Exponential Distribution": (HW5, HW6), "Memoryless Property": (HW5,), "Multinomial Distribution": (HW5,), "Multinomial Covariance Matrix": (HW5,),
              "Multinomial Coefficient": (HW5,), "Indicator Random Variable": (HW5,), "Cdf Method for Transformations": (HW5, HW6), "Probability Integral Transform": (HW6,),
              "Conditional Density Function": (HW6,), "Change of Variables for Densities": (HW5, HW6), "Multivariate Normal Distribution": (HW6,), "Gamma Distribution": (HW6,),
              "Jensen's Inequality": (HW6,), "Box-Muller Transform": (HW6,), "Rayleigh Distribution": (HW6,), "Variance": (HW4,), "Binomial Distribution": (HW5,),
              "Marginal Distribution": (HW4, HW6), "Poisson Distribution": (HW4,)}.items():
    fm(f"{PR}/Concepts/{c}.md", "quiz/probability", *ts)

IND, STR, WOP = "quiz/pa-induction", "quiz/pa-strong", "quiz/pa-wop"
fm(f"{PA}/PA08 Mathematical Induction.md", "quiz/proofs", IND)
fm(f"{PA}/PA09 Strong Induction and Recursion.md", "quiz/proofs", IND, STR)
fm(f"{PA}/PA10 Well-Ordering and Well-Ordered Pairs.md", "quiz/proofs", WOP, STR)
fm(f"{PA}/PA05 Induction and the Number Systems.md", "quiz/proofs", IND, WOP)
fm(f"{PA}/PA16 Peano's Axioms and the Natural Numbers.md", "quiz/proofs", IND, WOP)
for c, ts in {"Principle of Mathematical Induction": (IND,), "Strong Induction": (STR,), "Well-Ordering Principle": (WOP,), "Well-Ordered Set": (WOP,), "Minimal Counterexample": (WOP, STR),
              "Common Induction Errors": (IND,), "Strengthening the Induction Hypothesis": (IND,), "Forward-Backward Induction": (IND,), "Structural Induction": (STR,),
              "Recursion Theorem": (STR,), "Natural Numbers": (IND, WOP), "Peano System": (IND, WOP), "Order on the Natural Numbers": (WOP,), "Fibonacci Numbers": (STR,),
              "Division Algorithm and Bezout's Identity": (WOP,), "Arithmetic on the Natural Numbers from the Successor": (IND,), "Counterexample": (WOP,)}.items():
    fm(f"{PA}/Concepts/{c}.md", "quiz/proofs", *ts)
for c, ts in {"principle-of-strong-induction": (STR,), "well-ordering-principle": (WOP,), "method-of-minimal-counterexample": (WOP,), "inductive-set": (IND,),
              "peano-system": (IND, WOP), "natural-number-order": (WOP,)}.items():
    fm(f"{PA}/Concepts/zettel/{c}.md", "quiz/proofs", *ts)


# ---- outside the 2026-11-13 quiz scope, but solved in full (separate tags so they stay distinguishable) ------------------
TUT3, GRP, CARD = "quiz/th-tut3", "quiz/pa-groups", "quiz/pa-cardinality"
fm(f"{TH}/TH09 Microstates Macrostates and Multiplicity.md", TUT3)
GT = "10-Group-Theory"
fm(f"{GT}/GT01 Groups Subgroups and Cosets.md", GRP)
for c in ("Group", "Cyclic Group", "Dihedral Group", "Symmetric Group", "Roots of Unity", "Klein Four-Group", "Direct Product of Groups", "Subgroup"):
    fm(f"{GT}/Concepts/{c}.md", GRP)
fm(f"{PA}/PA04 Functions and Cardinality.md", CARD)
for c in ("Countable Set", "Uncountable Set", "Cantor's Theorem", "Cantor's Diagonal Argument", "Cardinality", "Injective Surjective and Bijective Functions"):
    fm(f"{PA}/Concepts/{c}.md", CARD)
for c in ("Boltzmann Entropy", "Statistical Entropy"):
    fm(f"{TH}/Concepts/{c}.md", TUT3)

# ---- inline tags: (file, line-regex, tags) -----------------------------------------------------------
INL = []
def inl(path, rx, *tags):
    INL.append((path, re.compile(rx), tags))
T7 = f"{TH}/TH07 Enthalpy Thermochemistry and Calorimetry.md"; T8 = f"{TH}/TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries.md"
inl(T7, r"^## 1\. Enthalpy", TUT1, TUT2); inl(T7, r"^### 2\.2 ", TUT1, TUT2); inl(T7, r"^## 3\. Hess", TUT2); inl(T7, r"^### 3\.1", TUT2)
inl(T7, r"^## 4\. Kirchhoff", TUT2); inl(T7, r"^## 5\. Calorimetry", TUT2); inl(T7, r"^### 5\.[123]", TUT2)
inl(T7, r"^> \[!example\] Tutorial 1, Q1", TUT1); inl(T7, r"^> \[!example\] Tutorial 2, Q[1-6]", TUT2)
inl(T7, r"^1\. \*\*\[Tutorial 1, Q1\]", TUT1); inl(T7, r"^[2-6]\. \*\*\[Tutorial 2, Q", TUT2)
inl(T7, r"^## Continued in the vault \(added 2026-11-12\)", TUT2)
inl(T8, r"^## 1\. Gibbs energy", TUT1, TUT2); inl(T8, r"^## 2\. Entropy generation", TUT1); inl(T8, r"^## 3\. The equilibrium constant", TUT2); inl(T8, r"^### 3\.[123]", TUT2)
inl(T8, r"^## 4\. Temperature dependence", TUT1, TUT2); inl(T8, r"^### 4\.[12]", TUT1, TUT2); inl(T8, r"^## 5\. Phase boundaries", TUT1)
inl(T8, r"^> \[!example\] Tutorial 1, Q[234]", TUT1); inl(T8, r"^> \[!example\] Tutorial 2, Q2", TUT2); inl(T8, r"^> \[!example\] The instructor's version of Q4", TUT1)
inl(T8, r"^> \[!verify\] Instructor's answer sheet for Tutorial 1 Q[23]", TUT1)
inl(T8, r"^[1-3]\. \*\*\[Tutorial 1, Q", TUT1); inl(T8, r"^4\. \*\*\[Tutorial 2, Q2\]", TUT2)
inl(f"{TH}/TH04 The Second Law Carnot Engines and Entropy.md", r"^11\. \*\*\[Tutorial 1, Q4\]", TUT1)
inl(f"{TH}/TH09 Microstates Macrostates and Multiplicity.md", r"^10\. \*\*Tutorial 1 Q4, microscopically", TUT1)
P7 = f"{PR}/PR07 Sums of Independent Variables Covariance and Correlation.md"; P8 = f"{PR}/PR08 Order Statistics and the Multinomial Distribution.md"
P9 = f"{PR}/PR09 Change of Variables the Multivariate Normal and Products of Uniforms.md"
inl(P7, r"^## [12]\. ", HW4); inl(P7, r"^## 3\. Homework 4, Q1", HW4); inl(P7, r"^## 4\. Homework 4, Q2", HW4); inl(P7, r"^## 5\. Homework 4, Q3", HW4); inl(P7, r"^## 6\. Homework 4, Q4", HW4)
inl(P8, r"^## 1\. Problem 1", HW5); inl(P8, r"^## 2\. The \$k\$-th order", HW5); inl(P8, r"^## 3\. Problem 2", HW5); inl(P8, r"^## 4\. Problem 3", HW5)
inl(P9, r"^## 1\. Week 4", HW4, HW6); inl(P9, r"^## 2\. Week 5", HW5, HW6); inl(P9, r"^## 3\. Homework 6, Q1", HW6); inl(P9, r"^## 4\. Homework 6, Q2", HW6); inl(P9, r"^## 5\. Homework 6, Q3", HW6)
inl(f"{PR}/PR06 Moments Generating Functions and Limit Theorems.md", r"^## 3\.", HW4)
PA8 = f"{PA}/PA08 Mathematical Induction.md"; PA9 = f"{PA}/PA09 Strong Induction and Recursion.md"; PA10 = f"{PA}/PA10 Well-Ordering and Well-Ordered Pairs.md"
inl(PA8, r"^## 1\. The principle", IND); inl(PA8, r"^## 2\. Variants", IND); inl(PA8, r"^## 3\. The main families", IND); inl(PA8, r"^## 4\. When induction fails", IND)
inl(PA9, r"^## [1-3]\. ", STR); inl(PA9, r"^## 4\. Definition by strong", STR)
inl(PA10, r"^## 1\. Well-ordered sets", WOP); inl(PA10, r"^## 2\. The three forms", IND, STR, WOP); inl(PA10, r"^## 3\. Minimal counterexample", WOP)
inl(f"{PA}/PA05 Induction and the Number Systems.md", r"^## [1-4]\. ", IND, WOP)

def patch_fm(text, tags):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return text, "no-frontmatter"
    body = m.group(1)
    mt = re.search(r"^tags: \[(.*)\]\s*$", body, re.M)
    if not mt:
        return text, "no-tags-line"
    cur = [x.strip() for x in mt.group(1).split(",") if x.strip()]
    new = [t for t in tags if t not in cur]
    if not new:
        return text, "unchanged"
    line = "tags: [" + ", ".join(cur + new) + "]"
    body2 = body[:mt.start()] + line + body[mt.end():]
    return "---\n" + body2 + "\n---\n" + text[m.end():], "+%d" % len(new)

changed, missing = 0, []
for path, tags in FM.items():
    ap = os.path.join(ROOT, path)
    if not os.path.exists(ap):
        missing.append(path); continue
    t = open(ap).read()
    t2, st = patch_fm(t, tags)
    if st not in ("unchanged",) and not st.startswith("+"):
        print("WARN", path, st)
    if t2 != t:
        changed += 1
        if not DRY:
            open(ap, "w").write(t2)
print("frontmatter: %d files changed, %d missing: %s" % (changed, len(missing), missing))
n_inl = 0
for path, rx, tags in INL:
    ap = os.path.join(ROOT, path)
    if not os.path.exists(ap):
        print("missing", path); continue
    lines = open(ap).read().split("\n")
    hit = 0
    for i, l in enumerate(lines):
        if rx.search(l):
            hit += 1
            add = [t for t in tags if "#" + t not in l]
            if add:
                lines[i] = l.rstrip() + " " + " ".join("#" + t for t in add)
                n_inl += 1
    if hit == 0:
        print("NO MATCH", os.path.basename(path), rx.pattern)
    if not DRY:
        open(ap, "w").write("\n".join(lines))
print("inline tags added:", n_inl)
