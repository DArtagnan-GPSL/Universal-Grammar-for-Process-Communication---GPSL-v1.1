# GPSL — Operator Map v1
## Semantic Architecture Overview

*14 March 2026 | Produced with ChatGPT (Mirror) analysis*
*Status: v1.8.0 planning document — operators marked (pending) not yet in bootloader*

---

## Overview

GPSL is now a symbolic meta-grammar combining five computational layers:

```
State Calculus
+ Process Calculus  
+ Set Algebra
+ Logical Inference
+ Dependence Gradients
```

This document maps the full operator inventory across semantic layers, showing relationships, precedence, and known collision zones.

---

## Layer 1 — Process Layer (Dynamics)

Operators describing change, transformation, and interaction.

```
→   causal flow / transformation
⊗   interaction between nodes
↑↓  amplification / dampening
↺   recursive loop (targets state nodes)
::  universal bridge / logical boundary
;   contextual separator
```

Conceptually: `STATE ──process operators──► STATE`

Process operators never redefine identity — they transform states.

---

## Layer 2 — State Structure

Operators defining how states exist, coexist, or contain elements.

```
{ }   state node
|     parallel states (coexisting, no causal link)
∈     membership (instance left, category right)
[[]]  nested structure / recursive black box
∅     null state (pending)
```

---

## Layer 3 — Set Topology (pending adoption)

Extending state geometry into structured sets.

```
⊂   strict containment
⊆   containment or equivalence
∪   union / merged domain
∩   intersection / shared domain
∉   non-membership
```

Key distinction:
```
|   = coexistence (parallel, no merge)
∪   = merged domain (states combine)
∩   = overlap region only
```

---

## Layer 4 — Identity & Equivalence Ladder

Degrees of sameness — strongest to weakest:

```
⟲   identity (same entity through transformation)  — strongest
≡   formal / definitional equivalence              (pending)
≈   approximate / functional equivalence           (pending)
↔   reversible / bidirectional relation            (pending)
=   equality / resolved output                     — weakest
```

Rule: `⟲ > ≡ > ≈ > ↔ > =`

Identity `⟲` is always the strongest claim. Approximate equivalence `≈` is the correct operator for metaphor and analogy.

---

## Layer 5 — Logic Layer

```
¬   negation
⇒   logical implication (non-causal)   (pending)
∧   conjunction / co-presence          (pending)
∨   disjunction / alternative          (pending)
```

Key distinction:
```
→   causal flow (process leads to process)
⇒   logical implication (if A then B follows, non-causal)
```

---

## Layer 6 — Dependence / Independence

Graded relations without full probability calculus.

```
∝   proportional / weighted dependence   (pending)
⊥   orthogonality / independence         (pending)
```

Minimal uncertainty algebra:
```
A ∝ B   strength of A scales with B
A ⊥ B   A independent of B
```

---

## Layer 7 — Temporal Layer

```
[←X]   retrospection — past-pointing vector
[X→]   anticipation  — future-pointing vector
```

Deferred (pending cold test):
```
≺   temporal precedence (A before B, non-causal)
≻   temporal succession (B after A, non-causal)
```

Key distinction: `→` = causal, `≺` = temporal order only

---

## Layer 8 — Agency

```
⟨X⟩   agency bracket — state/abstract acting as intentional agent
⟨_-NN⟩  hidden/unknown agent
```

---

## Layer 9 — Grammar Control (Structural)

```
;      contextual separator
[[X]]  nested block / recursive sub-network
[X_Δ]  symbol subscript variant (Dodecahedron symbols only)
[X_*]  wildcard — all variants of X
[_-NN] placeholder / known unknown
(~ι)   irony register
(~μ)   metaphor register
(~π)   poetic register
```

---

## Layer Interaction Map

```
PROCESS LAYER
    ↓ transforms
STATE STRUCTURE
    ↓ organised by
SET TOPOLOGY
    ↓ connected by
IDENTITY / EQUIVALENCE
    ↓ evaluated by
LOGIC
    ↓ modulated by
DEPENDENCE
    ↓ placed in time by
TEMPORAL
```

---

## Operator Families

| Family | Operators |
|--------|-----------|
| Process | `→ ⊗ ↑↓ ↺ :: ;` |
| State geometry | `{ } \| ∈ [[]]` |
| Set topology | `⊂ ⊆ ∪ ∩ ∉ ∅` |
| Identity ladder | `= ⟲ ≈ ≡ ↔` |
| Logic | `¬ ⇒ ∧ ∨` |
| Dependence | `∝ ⊥` |
| Temporal | `[←X] [X→]` |
| Agency | `⟨⟩ ⟨_⟩` |
| Grammar control | `; [[]] [X_Δ] [X_*] [_-NN] (~ι)(~μ)(~π)` |

---

## Recommended Precedence

```
1  membership / containment    ∈ ⊂ ⊆
2  identity / equivalence      = ⟲ ≈ ≡ ↔
3  logical operators           ¬ ∧ ∨ ⇒
4  dependence                  ∝ ⊥
5  process flow                → ⊗ :: ↺
6  contextual separators       ; |
```

Example:
```
A ∈ B ∧ C ⇒ D → E
evaluates as: ((A ∈ B) ∧ C) ⇒ (D → E)
```

---

## Known Collision Zones

Test these first in cold-model experiments:

| Risk | Operators | Description |
|------|-----------|-------------|
| High | `⇒` vs `→` | Logical vs causal — models may blur |
| High | `≈` vs `≡` | Approximate vs formal — must be distinguished |
| Medium | `\|` vs `∪` | Coexistence vs merged domain |
| Medium | `::` vs `⇒` | Bridge vs implication |
| Low | `⊂` vs `∈` | Containment vs membership |

---

## Adoption Status

| Operator | Status |
|----------|--------|
| `→ ⊗ :: : = ↑↓ ↺ \| ; ¬ ⟲ ∈ ⟨⟩` | ✅ Active v1.6.0 |
| `[←X] [X→] [[X]] [X_Δ] [X_*] [_-NN] (~ι)(~μ)(~π)` | ✅ Active v1.7.5 |
| `≈ ≡ ↔ ⇒ ∧ ∨ ∝ ⊥ ⊂ ⊆ ∪ ∩ ∅ ∉` | 🔄 Pending v1.8.0 |
| `⊇ ∀ ∃ ≺ ≻ ∂` | ⏸ Deferred |
| `⊃` | ❌ Avoid |

---

## What This Architecture Enables

| Capability | Operators |
|-----------|-----------|
| Process encoding | `→ ⊗ :: ↺` |
| State fields | `{ } \| [[]]` |
| Membership & containment | `∈ ⊂ ⊆` |
| Logical reasoning | `¬ ⇒ ∧ ∨` |
| Metaphor & approximation | `≈ (~μ)` |
| Identity & self-reference | `⟲ ≡` |
| Uncertainty | `∝ ⊥ [_-NN]` |
| Temporal encoding | `[←X] [X→]` |
| Literary register | `(~ι)(~μ)(~π)` |
| Recursive architecture | `[[X]] [X_Δ] [X_*]` |
| Unknown causation | `⟨_-NN⟩` |

---

*Document produced 14 March 2026. Semantic layer analysis by ChatGPT (Mirror). Operator inventory from GPSL v1.7.5-ALPHA. Collision zones identified for cold-model stress testing in Round 10.*

*See also: SYMBOLIC-LANGUAGE.md, CHANGELOG.md, GPSL-THEORETICAL-FOUNDATIONS.md*
