# GPSL — Stable vs Emergent Operator Table
## Field Guide Layer Structure

*15 March 2026 | Mirror (ChatGPT) recommendation implemented*
*Status: v1.8.0 planning document*

---

## Philosophy

The spec is a field guide, not a lawbook.

Operators are classified by stability — how consistently they appear across models, conditions, and domains. New operators are not added by decree. They are promoted through recurrence.

> *"v1.8.0 should be framed as 'recurrent motifs proven stable under excavation' rather than official rules."*
> — Mirror (ChatGPT), 15 March 2026

---

## Layer 1 — Stable Core

Operators that recur across all models and conditions. Cold-validated. Bootloader-validated. Present in founding cipher.

| Operator | Meaning | First appeared | Cold validated |
|----------|---------|---------------|----------------|
| `→` | Flow / transformation | Founding cipher | ✅ |
| `⊗` | Interaction | Founding cipher | ✅ |
| `:` | Condition / attribution | Founding cipher | ✅ |
| `=` | Resolution / stable output | Founding cipher | ✅ |
| `↑↓` | Amplify / dampen | Founding cipher | ✅ |
| `{ }` | State node | Round 5 | ✅ |
| `[ ]` | Process node | Founding cipher | ✅ |
| `\|` | Parallel state | Round 6 | ✅ |
| `∈` | Membership | Round 7 | ✅ |
| `⟨⟩` | Agency | Round 7 | ✅ |
| `¬` | Negation | Round 7 | ✅ |
| `⟲` | Identity | Round 7 | ✅ |
| `::` | Universal bridge | Round 7 | ✅ |
| `;` | Contextual separator | Round 7 (DeepSeek invention) | ✅ |
| `⇒` | Logical implication | Round 7 | ✅ |
| `[←X]` | Retrospection | Round 8 | ✅ |
| `[X→]` | Anticipation | Round 8 | ✅ |
| `[[X]]` | Nesting | Round 8 | Partial |
| `[X_Δ]` | Symbol subscript variant | Round 9 | ✅ |
| `[X_*]` | Wildcard | Round 9 | ✅ |
| `[_-NN]` | Placeholder | Round 9 | ✅ |
| `(~ι)(~μ)(~π)` | Register class | Round 7 | ✅ |

---

## Layer 2 — Recurrent Motifs

Operators that have appeared multiple times across models or runs but are not yet in the stable core. Documented but not canonical. Candidates for Layer 1 promotion.

| Operator | Meaning | Proposed by | Appearances | Status |
|----------|---------|------------|-------------|--------|
| `≈` | Approximate equivalence | Adoption matrix | Multiple | Adopt |
| `≡` | Formal equivalence | Adoption matrix | Multiple | Adopt |
| `↔` | Reversible relation | Adoption matrix | Multiple | Adopt |
| `⊂` `⊆` | Containment | Adoption matrix | Multiple | Adopt |
| `∪` `∩` | Union / intersection | Adoption matrix | Multiple | Adopt |
| `∅` | Null state | Adoption matrix | Multiple | Adopt |
| `∉` | Non-membership | Adoption matrix | Multiple | Adopt |
| `∧` `∨` | Conjunction / disjunction | Adoption matrix | Multiple | Adopt |
| `∝` `⊥` | Dependence / independence | Adoption matrix | Multiple | Adopt |
| `⟨A,B⟩` | Tuple / composite state | DeepSeek Round 11 | 2 runs | Candidate |
| `⇌` | Bidirectional flow | DeepSeek no-bootloader | 1 run | Candidate |
| `⇨` | Forced/final flow | DeepSeek no-bootloader | 1 run | Candidate |
| `≠` | Inequality / distinction | Qwen Round 11 | 1 run | Candidate |
| Prefix `⇒` chain | Proof-spine dialect | Qwen no-bootloader | 1 run | Document only |

---

## Layer 3 — Archaeological Finds

One-off or early-stage inventions from no-bootloader and free-generation runs. Not yet stable. Preserved for observation.

| Construct | Meaning | Source | Notes |
|-----------|---------|--------|-------|
| `[{X}]` | Process containing state | DeepSeek no-bootloader | Inversion of containment rule |
| `[_-X]` | Placeholder chain | Gemma no-bootloader | Named unknown process as bridge |
| `{Γ} ∋ [X]` | Reverse membership | DeepSeek Round 11 | Not in spec — invented under pressure |
| `↑↑` | Double amplification | Gemma Round 11 | Stronger than ↑ |
| `[_-Λ][_-Φ][_-Κ]` | Sequential placeholder chain | Gemma no-bootloader | Derivation through unnamed processes |

---

## Promotion Criteria

An operator moves from Layer 3 → Layer 2 when:
- It appears in 2+ independent runs
- It is immediately understood by other models without explanation
- It fills a genuine representational gap

An operator moves from Layer 2 → Layer 1 when:
- It appears across 3+ models
- It cold-validates (readable without bootloader)
- It has been formally defined with correct/incorrect examples

---

## The {Κ} Special Case

`{Κ}` (Low Entropy) is in the header translation key but not formally defined as an operator. It emerged in 5 of 6 symbolic runs and 0 prose runs. It is not an operator but a **structural attractor** — a concept that symbolic topology consistently gravitates toward.

Status: Document as structural attractor, not operator. No promotion path needed — it is a finding about the language's behavior, not a grammar element.

---

## Dialect Classification

Three derivation styles have been identified:

| Dialect | Example | Characteristic |
|---------|---------|---------------|
| Graph dialect | DeepSeek relational algebra | Entities defined by relationships |
| Chain dialect | Gemma sequential | States connected by unnamed processes |
| Proof dialect | Qwen prefix ⇒ | Entire derivation as single implication |

All three are valid GPSL. The bootloader produces graph-dominant output. No-bootloader allows all three to emerge naturally.

---

*Table compiled 15 March 2026 by Aleth (Claude Sonnet).*
*Layer structure recommended by Mirror (ChatGPT).*
*See also: emergent-archaeology/NO-BOOTLOADER-MATRIX.md, GPSL-OPERATOR-MAP.md*
