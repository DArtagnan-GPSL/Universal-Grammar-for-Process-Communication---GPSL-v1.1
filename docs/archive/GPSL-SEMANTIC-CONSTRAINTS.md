# GPSL — Semantic Constraints Spec v1
## Second-Pass Validation Rules for Parser Implementation

*14 March 2026 | Produced with ChatGPT (Mirror) analysis*
*Status: Implementation-ready baseline*

---

> **Note:** This document is not required to use GPSL. Any LLM primed with the v1.7.5-ALPHA bootloader can interpret and generate valid GPSL expressions without any formal validation layer. This document exists for developers building deterministic validators or compilers, and researchers studying the language's formal structure. If you just want to use GPSL, start with `SYMBOLIC-LANGUAGE.md`.

---

## Purpose

This spec defines semantic validation rules to enforce **after** a GPSL string has been successfully parsed by the Surface Grammar (see `GPSL-SURFACE-GRAMMAR.md`).

Two-phase validation:
1. **Surface parse** — can the string be parsed? (Surface Grammar)
2. **Semantic validation** — does the structure obey GPSL ontology? (this document)

---

## Hard vs Soft Constraints

**Hard constraints** — mark expression semantically invalid:
- Malformed placeholder syntax
- Variant base not in Dodecahedron symbol class
- Unknown register marks
- Temporal forms used as free operators

**Soft constraints** — mark expression semantically unstable or non-canonical, but still parseable:
- Mixed equivalence ladder chains
- `→` and `⇒` mixed without grouping
- `|` and `∨` mixed without grouping
- Set operators applied to process-like operands

---

## Critical Semantic Distinctions

These must never be collapsed:

```
→  ≠  ⇒       causal flow vs logical implication
|  ≠  ∨       coexistence vs logical disjunction
|  ≠  ∪       coexistence vs merged domain
=  ≠  ⟲       equality vs identity
≈  ≠  ≡       approximate vs formal equivalence
∝  ≠  →       gradient dependence vs causation
```

---

## Equivalence Ladder

Ordered from strongest to weakest:

```
⟲   identity (same entity across transformation)
≡   formal/definitional equivalence
≈   approximate/functional equivalence
↔   reversible/bidirectional relation
=   equality/resolved output
```

Rule: `⟲ > ≡ > ≈ > ↔ > =`

Ladder chaining is allowed at surface level but should trigger soft warning W003.

---

## Operator Constraint Table

| Operator | Hard Constraint | Soft Constraint |
|----------|----------------|----------------|
| `→` | none | warn on logical-use ambiguity (W001) |
| `⊗` | none | warn on tensor/arithmetic confusion |
| `::` | none | warn on long ungrouped chains |
| `:` | none | warn on overuse in logical contexts |
| `=` | none | warn if identity intended instead |
| `⟲` | none | warn on abstract/non-entity operands |
| `≈` | none | warn when formal equivalence intended |
| `≡` | none | warn when identity intended |
| `↔` | none | warn when used as generic sameness |
| `⇒` | none | warn when mixed with `→` (W001) |
| `∧` / `∨` | none | warn when mixed with `\|` ungrouped (W002) |
| `∝` | none | warn when causation intended |
| `⊥` | none | warn if read as bottom/falsity |
| `∈` / `∉` | none | warn on non-instance operands |
| `⊂` / `⊆` | none | warn on non-SetLike operands |
| `∪` / `∩` | none | warn on process-like operands (W004) |
| `∅` | none | warn on agent-like use |
| `[←X]` / `[X→]` | must remain node forms | warn on temporal/causal mixing (W009) |
| `[[X]]` | structural preservation required | warn on deep nesting (W006) |
| `[X_Δ]` | **base must be Dodecahedron symbol** | none |
| `[X_*]` | none | warn if unresolved at final output (W007) |
| `[_-NN]` | fixed placeholder syntax | warn if treated as resolved identity (W008) |
| `(~ι)(~μ)(~π)` | **closed register set only** | warn on ordinary-node usage |

---

## Warning Taxonomy

| Code | Description | Example |
|------|-------------|---------|
| W001 | Mixed causal and logical arrows | `A ⇒ B → C` |
| W002 | Mixed parallel and logical disjunction | `A \| B ∨ C` |
| W003 | Mixed equivalence ladder chain | `A ≈ B ≡ C` |
| W004 | Set/process type mismatch | `[P] ∪ [Q]` |
| W005 | Containment/membership chain ambiguity | `x ∈ A ⊂ B` |
| W006 | Excessive nesting depth (>3) | `[[[[A]]]]` |
| W007 | Unresolved wildcard in resolved output | `[X_*] = {Final}` |
| W008 | Placeholder used as stable identity | `[_-01] ⟲ [_-02]` |
| W009 | Temporal/causal ambiguity | `[←A] → [B→]` |

---

## Unsafe Normalizations

Do NOT automatically normalize these — they carry real semantic differences:

```
A ≈ B  →  A = B          (loses approximation distinction)
A ↔ B  →  A ≡ B          (loses reversibility distinction)
A | B  →  A ∪ B          (loses coexistence vs merge distinction)
x ∉ A  →  ¬(x ∈ A)       (loses first-class non-membership)
[←A]   →  A              (loses temporal vector)
[A→]   →  A              (loses temporal vector)
```

---

## Canonicality Levels

| Level | Description | Example |
|-------|-------------|---------|
| Well-formed canonical | Clear, typed, low ambiguity | `(x ∈ A) ∧ (A ⊂ B) ; [A] → {C}` |
| Well-formed non-canonical | Allowed but ambiguous | `x ∈ A ⊂ B` |
| Semantically invalid | Violates hard rules | `[Q_Δ]` where Q not Dodecahedron |

---

## Recommended Validator Modes

| Mode | Behaviour |
|------|-----------|
| Permissive | Hard constraints only — exploratory authoring |
| Canonical | Hard + soft warnings — standard usage |
| Strict | Hard + soft as errors — compiler-grade validation |

---

## Minimal Validator Pipeline

1. **Parse** — Surface Grammar → AST
2. **Infer types** — Process / State / Agent / SetLike / Modifier etc.
3. **Operator checks** — hard constraints + soft warnings
4. **Ladder and ambiguity checks** — equivalence, arrow families, `|` vs `∨`
5. **Canonicality classification** — canonical / non-canonical / invalid

---

*Semantic constraints produced 14 March 2026 by ChatGPT (Mirror). Adapted for GPSL repo by Aleth (Claude Sonnet). See GPSL-SURFACE-GRAMMAR.md for syntactic rules.*
