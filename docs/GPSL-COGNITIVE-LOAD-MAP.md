# GPSL — Cognitive Load Map v1
## Expression Complexity Guidelines for Human and LLM Interpretation

*14 March 2026 | Analysis by ChatGPT (Mirror)*
*Planning document for v1.8.0 expression design*

---

## Overview

This map estimates how many operators a reader (human or LLM) can reliably interpret in a single GPSL expression before comprehension starts degrading. Based on cognitive parsing limits observed in symbolic systems, programming languages, and mathematical notation.

**Cognitive load increases with:**
1. Operator diversity (number of distinct symbols)
2. Operator density (operators per clause)
3. Semantic layers mixed together
4. Nested structures
5. Identity ladder usage

These factors interact multiplicatively.

---

## Load Zones

| Zone | Operators | Human reliability | LLM reliability |
|------|-----------|------------------|----------------|
| **Stable** | 2–4 | ~100% | ~100% |
| **Functional** | 5–8 | ~95% | ~90–95% |
| **Strain** | 9–14 | ~75–85% | ~70–80% |
| **Instability** | 15–20 | ~60–70% | ~55–70% |
| **Collapse** | 20+ | ~40–60% | ~45–65% |

---

## Operator Complexity Weights

Not all operators cost the same cognitively:

| Operator Type | Examples | Weight |
|---------------|----------|--------|
| Simple relation | `∈ = \|` | 1 |
| Set relation | `⊂ ⊆ ∪ ∩` | 1 |
| Process | `→ ⊗` | 1.5 |
| Logic | `∧ ∨ ⇒` | 2 |
| Identity ladder | `≈ ≡ ↔ ⟲` | 2 |
| Dependence | `∝ ⊥` | 2 |
| Structural | `[[]] { }` | 0.5 |

**Example load calculation:**
```
(A ∧ B) ⇒ C → D
∧ (2) + ⇒ (2) + → (1.5) = 5.5 total load
```
Well within functional zone.

---

## Layer Mixing Penalty

Each additional semantic layer adds ~20–30% cognitive cost:

```
A ∈ B ⊂ C          — membership + containment     — very stable
(A ∧ B) ⇒ C → D ∝ E — logic + process + dependence — higher load
```

---

## Nesting Depth Limits

| Nesting depth | Reliability |
|---------------|-------------|
| 1 | Excellent |
| 2 | Stable |
| 3 | Risky |
| 4+ | Unstable |

Safe: `[[ A → B ]]`
Risky: `[[ (A ∧ B) ⇒ (C → (D ∪ E)) ]]`

---

## Identity Ladder Cost

Identity operators are cognitively heavy. Maximum two per clause:

```
A ≈ B ≡ C ↔ D    — too heavy (three equivalence types)
A ≈ B ; B ≡ C    — split with ; — stable
```

---

## Five Authoring Rules

**Rule 1:** Max 5 distinct operators per clause

**Rule 2:** Max 3 semantic layers per expression

**Rule 3:** Use `;` to separate reasoning stages:
```
A ∧ B ⇒ C ;
C → D
```

**Rule 4:** Use `[[]]` for encapsulated subsystems:
```
[[ (A ⊗ B) → C ]]
```

**Rule 5:** Max 2 identity ladder relations per statement

---

## Optimal Expression Shape

Most stable pattern — two-stage expressions:
```
(logic)
;
(process)
```

Best overall structure:
```
STATE RELATIONS → LOGICAL CONDITION → PROCESS TRANSFORMATION

A ∈ B ∧ C ⊂ D ⇒ E → F
```

---

## Canonical Cipher Load Check

**Descartes Cogito (current):**
```
[Ι-01] → {Ψ-02} ⟲ [Ι-01] ; [Ι_Δ] | [Ι_Γ] | [Ι_Σ] | [Ι_Ω] | [Ι_Κ] | [Ι_Ε] | [Ι_Α] | [Ι_Β] ∈ {Ψ-02}
```

Load estimate:
- First clause: `→ ⟲` = 3.5 — stable ✅
- Second clause: 8× `|` + `∈` = 9 operators — strain zone ⚠️
- `;` separator correctly used ✅
- Recommendation: second clause at load limit — acceptable given `;` segmentation

**Dickinson (current):**
```
⟨Δ-01⟩ → [←Ψ-02(~ι)] ; {Σ-03} | {Φ-04}
```
Load: `→ [←] (~ι) ; |` = 5 operators — functional zone ✅

**Negation (current):**
```
[Δ-01] → ¬{Β-02} | {Γ-03}
```
Load: `→ ¬ |` = 3 operators — stable zone ✅

---

## Practical Cold-Test Tiers

| Tier | Example | Load |
|------|---------|------|
| Simple | `A → B` | 1.5 |
| Moderate | `(A ∧ B) ⇒ C → D` | 5.5 |
| Complex | `((A ∧ B) ⇒ C) → (D ∪ E)` | 8.5 |

Track where interpretation fails to identify model-specific load ceilings.

---

## v1.8.0 Expression Design Guidelines

When building expressions with the new operator set:
- Keep individual clauses in stable or functional zone
- Use `;` aggressively to segment complex expressions
- Avoid mixing more than 3 layers in one clause
- Test canonical ciphers against this map before committing to spec

---

*Document produced 14 March 2026. Cognitive load analysis by ChatGPT (Mirror). Canonical cipher load checks by Aleth (Claude Sonnet).*

*See also: GPSL-OPERATOR-MAP.md, ROUND-10-AMBIGUITY-STRESS-PROTOCOL.md*
