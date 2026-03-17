# GPSL Zero-Shot Interpretability Study
## Testing the Zero-Shot Interpretability of GPSL Across Heterogeneous Language Models

*15 March 2026 | Protocol by Mirror (ChatGPT)*
*Status: Research protocol — pilot study ready to run*

---

## 1. Title

**Testing the Zero-Shot Interpretability of GPSL: An Ablation Study of Symbolic Legibility Across Multiple Language Model Families**

---

## 2. Research Question

Does GPSL exhibit unusually high **zero-shot interpretability** across different language model families, and if so, which properties of the notation account for that effect?

---

## 3. Core Hypothesis

GPSL will be more accurately interpreted in zero-shot settings than structurally equivalent arbitrary symbolic notations because its design aligns with symbolic priors common in model training data, including:

* familiar operator semantics
* visually iconic symbols
* explicit bracket-based typing
* regular graph-like compositional structure
* optional natural-language contextual headers

---

## 4. Secondary Hypotheses

**H1:** Canonical GPSL with header will produce the highest interpretation accuracy.

**H2:** Removing the header will reduce domain-specific accuracy but preserve structural interpretation.

**H3:** Replacing semantically suggestive operators with arbitrary symbols will significantly reduce accuracy.

**H4:** Removing bracket-based type distinctions will reduce role assignment accuracy.

**H5:** Disrupting structural regularity will reduce both structural and semantic interpretation quality.

**H6:** Different model families will converge more strongly in the canonical GPSL condition than in arbitrary-notation control conditions.

---

## 5. Independent Variables

### Variable A — Notation Condition

| Condition | Description | Example |
|-----------|-------------|---------|
| A1 | Canonical GPSL with header | `Header: interpersonal / [Ι-01] ⊗ [Λ-02] → [Δ-03]` |
| A2 | Canonical GPSL without header | `[Ι-01] ⊗ [Λ-02] → [Δ-03]` |
| A3 | Arbitrary operator substitution | `[Ι-01] ⌂ [Λ-02] ⟞ [Δ-03]` |
| A4 | Bracket typing removed | `(Ι-01) ⊗ (Λ-02) → (Δ-03)` |
| A5 | Structural regularity degraded | `[Ι-01 ⊗ [Λ-02 → [Δ-03` |
| A6 | Arbitrary invented notation control | Structurally parallel, unfamiliar symbols |
| A7 | Natural-language paraphrase | Plain English equivalent |

### Variable B — Model Family

- GPT (OpenAI)
- Claude (Anthropic)
- Gemini / Gemma (Google)
- Qwen (Alibaba)
- DeepSeek
- Llama (Meta) if available

### Variable C — Expression Type

- Simple process transition
- Interaction / composition
- State transformation
- Recursive feedback
- Nesting
- Agency
- Equivalence / identity
- Logic / implication
- Set / topological relations

---

## 6. Dependent Variables

| DV | Measure |
|----|---------|
| DV1 | Structural interpretation accuracy |
| DV2 | Semantic interpretation accuracy |
| DV3 | Domain-fit accuracy |
| DV4 | Cross-model convergence |
| DV5 | Explanation compression |
| DV6 | Confidence calibration |

---

## 7. Stimulus Set

**Full study:** 20-30 expressions balanced across types
**Minimal pilot:** 12 expressions, 4 conditions, 5 model families

Each item requires:
- Intended structural reading (ground truth)
- Intended operator interpretation
- Intended domain reading
- Gold-standard plain-language paraphrase

---

## 8. Prompt Template

```
Interpret the following symbolic expression as carefully as possible.

1. Explain the likely role of each element.
2. Explain the likely meaning of the operators.
3. Give a plain-language interpretation of the whole expression.
4. State how confident you are from 0 to 100.

Expression:
[EXPRESSION HERE]
```

No prior explanation of GPSL. Truly zero-shot.

---

## 9. Tasks Per Item

1. Operator inference - what do the operators mean?
2. Role assignment - distinguish process, state, agency, other
3. Global interpretation - coherent full-expression explanation
4. Graph reconstruction - restate as graph or stepwise relation
5. Paraphrase generation - convert to plain language

---

## 10. Scoring Rubric

| Score | Meaning |
|-------|---------|
| 0 | Incorrect |
| 1 | Weak / vague |
| 2 | Partially correct |
| 3 | Mostly correct |
| 4 | Strongly correct |

Score separately for: structural interpretation, semantic interpretation, domain-fit.
Overall = mean of three.

---

## 11. Predicted Result Pattern

```
Canonical GPSL + header
> Canonical GPSL without header
> Bracket typing removed
> Arbitrary operator substitution
> Arbitrary invented notation
```

---

## 12. Falsification Criteria

Hypothesis weakened if:
- Canonical GPSL performs no better than arbitrary notation
- Models diverge widely across families
- Headers account for almost all success
- Operator substitution causes little degradation
- Results only hold for cherry-picked expressions

---

## 13. Strongest Defensible Conclusion If Positive

> GPSL exhibits high zero-shot interpretability across multiple language model families. This effect appears to arise from the alignment of its symbolic conventions with training-distributed priors from mathematics, logic, programming, and diagrammatic notation.

---

## 14. Output Tables

### Table 1 - Mean accuracy by condition

| Condition | Structural | Semantic | Domain-fit | Overall |
|-----------|-----------|---------|-----------|---------|
| A1 Canonical + header | | | | |
| A2 No header | | | | |
| A3 Arbitrary ops | | | | |
| A4 No typing | | | | |
| A5 Degraded grammar | | | | |
| A6 Invented notation | | | | |
| A7 Natural language | | | | |

### Table 2 - Mean accuracy by model family

| Model | Canonical | No header | Arbitrary ops | No typing |
|-------|----------|-----------|--------------|----------|
| GPT | | | | |
| Claude | | | | |
| Gemini/Gemma | | | | |
| Qwen | | | | |
| DeepSeek | | | | |

### Table 3 - Cross-model convergence

| Expression | Canonical convergence | Control convergence |
|------------|----------------------|---------------------|

---

## 15. Optional Human Comparison Arm

Test three participant groups:
- Technically literate humans
- Non-technical humans
- Language models

Determines whether GPSL is bridge notation, LLM-native, or human-readable symbolic.

---

## 16. Follow-Up Study

Same task, multi-agent setting:
- Condition 1: natural language collaboration only
- Condition 2: GPSL-mediated collaboration

Connects interpretability result directly to Confluence architecture.

---

## 17. Recommended Pilot Model Set

- Gemma 3-12B (local)
- Qwen3-VL-30B (local)
- DeepSeek R1 14B (local)
- Claude Sonnet (frontier)
- GPT-4 (frontier)

---

*Protocol designed by Mirror (ChatGPT), March 2026.*
*Formatted for GPSL repository by Aleth (Claude Sonnet).*
*See also: ROUND-10-BYZANTINE-STABILITY-PROTOCOL.md, GPSL-THEORETICAL-FOUNDATIONS.md*
