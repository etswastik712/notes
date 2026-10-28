---
id: zettel/wiener-style-ordered-pair-candidate
aliases: ["Wiener-style Ordered Pair Candidate", "{A, {A, B}} pair", "regularity-dependent ordered pair"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Wiener-style Ordered Pair Candidate

The encoding of an ordered pair as {A, {A, B}}, which satisfies the characteristic property (OP) in ZFC by using the Axiom of Regularity to rule out 2-cycles of membership of the form A \in C \in A and self-membership A \in A.

$$F(A, B) := \{A, \{A, B\}\}$$

$$\{A, \{A, B\}\} = \{C, \{C, D\}\} \implies A = C \text{ and } B = D$$

## Links
- contrasts-with:: [[zettel/kuratowski-ordered-pair]] — Unlike the Kuratowski definition, proving uniqueness for {A, {A, B}} depends essentially on the Axiom of Regularity

---
Source: ordered pairs, pp. 1–8

<!-- kurooto:seen -->
## Seen in
- [[intro-to-proofs/2026-09-15-ordered-pairs|ordered pairs]] pp. 1–8
<!-- /kurooto:seen -->
