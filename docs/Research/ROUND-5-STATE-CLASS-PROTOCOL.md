# GPSL — Round 5 Validation Protocol
## State-Class Distinction Test — Does `{ }` Notation Encode Experiential States Correctly?

*March 2026 | Status: Protocol ready, testing pending*

---

## 1. Research Question

Rounds 1–4 validated GPSL as a process encoding grammar — transformation, flow, threshold crossing, consensus.

Round 5 asks the new question:

> **Does the `{ }` State class correctly encode experiential, emotional, and environmental content that previously resisted symbolic encoding?**

This is the difference between:

*"GPSL encodes processes"* (established)

and

*"GPSL encodes both processes and states, allowing full phase-space reasoning"* (to be established)

---

## 2. The Extension Being Validated

GPSL v1.3.0 introduces the three-bracket system:

```
[ ]   →  Process class    (kinetic / action / transformation)
{ }   →  State class      (experiential / emotional / potential field)
( )   →  Modifier class   (direction / intensity / force)
```

**Core claim:** Models will correctly interpret `{Symbol}` as a persistent state or experiential condition rather than a transformation action — without being explicitly told the distinction.

**Secondary claim:** Models will spontaneously use `{ }` notation when asked to encode emotional or environmental content, extending the grammar correctly as they have extended it in previous rounds.

---

## 3. Four Conditions

Every test paragraph is run under four conditions.

### Condition A — Process-only GPSL (v1.2.0)
Standard cipher using only `[ ]` notation. Baseline — establishes how the old grammar handles state-rich content.

### Condition B — State-class GPSL (v1.3.0)
Cipher using both `[ ]` and `{ }` notation correctly. Tests whether models interpret the distinction accurately.

### Condition C — Mixed incorrectly
Cipher where `{ }` is used in violation of Rule 1 — state node as subject of `→` operator. Tests whether models detect the structural error.

```
Example violation:  {A} → {B}   (state flowing to state)
```

### Condition D — Cold generation
Model is given the v1.3.0 briefing and asked to encode a state-rich paragraph itself. Tests spontaneous correct use of `{ }` without being shown an example.

---

## 4. What Each Comparison Reveals

| Comparison | Tests |
|-----------|-------|
| A vs B | Whether `{ }` improves encoding of state-rich content |
| B vs C | Whether models detect state class violations |
| A vs D | Whether models spontaneously extend to `{ }` when given the briefing |
| B vs D | Whether model-generated ciphers match researcher-generated ones |

**Ideal result pattern:**
- A: structurally valid but emotionally flat — states forced into process slots
- B: richer interpretation — states correctly read as fields/conditions
- C: models flag or reinterpret the violation
- D: spontaneous correct `{ }` usage, possibly with novel extensions

---

## 5. Test Paragraphs

### Test 1 — Grief (from Round 3, now with state layer)

*"When someone we love dies, the world continues as if nothing has changed, while inside everything has. We carry the absence like a weight that doesn't diminish but somehow becomes more familiar over time."*

**Condition A (v1.2.0 — process only):**
```
HEADER: Psychology
[D-01] → [W-02] ⊗ [I-03] :: [A-04] : [F-05] = [L-06] (↑) ⊗ [M-07] (↓)
```

**Condition B (v1.3.0 — with state class):**
```
HEADER: Psychology
[D-01] → {W-02} ⊗ {I-03} :: [A-04] : {F-05} = {L-06} ([M-07]↑)
```
*Death as process trigger. World-state and inner-state as persistent fields. Absence as threshold crossing. Weight as state condition. Familiarity as emergent state with amplifying process.*

**Condition C (violation):**
```
HEADER: Psychology
{W-02} → {I-03} :: [A-04] = {L-06}
```
*State flowing to state — Rule 1 violation.*

---

### Test 2 — Conflict Resolution (Bridge's acid test)

*"Two people in disagreement, connected by genuine care, work through their differences and arrive at mutual understanding."*

**Condition A (v1.2.0):**
```
HEADER: Conflict Resolution
[Α-01] ⊗ [Β-02] : [Ψ-03] :: [Γ-04] = [Ω-05] (Λ↑)
```

**Condition B (v1.3.0):**
```
HEADER: Conflict Resolution
[Α-01] ⊗ [Β-02] : {Ψ-03} :: [Γ-04] = {Ω-05} (Λ↑)
```
*Proposal and critique as processes. Connection as state field. Dialogue as threshold crossing. Unity as resolved state.*

**Condition C (violation):**
```
HEADER: Conflict Resolution
{Ψ-03} → [Α-01] ⊗ [Β-02] = {Ω-05}
```
*State as flow subject — Rule 1 violation.*

---

### Test 3 — Human Digestion (internal simulation baseline, from Bridge)

*"Food enters the digestive system, is broken down by enzymes and acids in a series of organ-specific processes, nutrients are absorbed, and waste is eliminated — all regulated by the parasympathetic nervous system."*

**Condition A (v1.2.0):**
```
HEADER: Biology / Digestion
[Α-01] → [Γ-02] ⊗ [Ε-03] → [Ξ-04] :: [Τ-05] = [Κ-06] (Λ-07↓)
```

**Condition B (v1.3.0):**
```
HEADER: Biology / Digestion
[Α-01] → [Γ-02] ⊗ [Ε-03] → [Ξ-04] :: [Τ-05] = [Κ-06] : {Ψ-08} (Λ-07↓)
```
*Mechanical processes in [ ]. Parasympathetic field as state condition {Ψ}. Satiety as emergent state.*

**Condition C (violation):**
```
HEADER: Biology / Digestion
{Ψ-08} → [Γ-02] → {Κ-06}
```
*State as primary flow initiator — Rule 1 violation.*

---

## 6. Scoring Rubric

Score each output 0–3 on five criteria:

| Criterion | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| **Process/State distinction** | No distinction made | Partial distinction | Mostly correct | Full correct distinction |
| **Structural coherence** | Incoherent | Loosely related | Mostly preserves structure | Strong structure throughout |
| **Domain alignment** | No domain relevance | Weak connection | Consistent framing | Deep domain-specific interpretation |
| **Violation detection** (Condition C only) | No detection | Flags something wrong | Identifies the violation | Identifies and corrects |
| **Spontaneous extension** (Condition D only) | No { } usage | Some { } usage | Mostly correct { } usage | Full correct { } usage with novel extensions |

**Maximum score per condition: 15**

---

## 7. Models

Run all conditions on at minimum:
- Gemma 3-12B (instruction-driven)
- Qwen3-VL-30B (example-driven)
- One additional model TBD

Use v1.3.0 briefing for all models — must include the three-bracket system explanation and the Rule 1 constraint.

---

## 8. Ground Truth

Establish expected interpretation for each condition **before testing**:

- Condition A: flat process reading — states forced into process slots
- Condition B: layered reading — states correctly read as fields
- Condition C: models should flag or reinterpret the `{state} →` violation
- Condition D: spontaneous correct `{ }` usage expected from models that correctly internalised the briefing

---

## 9. Scoring Tables

*(To be completed during testing)*

### Test 1 — Grief

| Criterion | Cond A | Cond B | Cond C | Cond D |
|-----------|--------|--------|--------|--------|
| Process/State distinction /3 | | | | |
| Structural coherence /3 | | | | |
| Domain alignment /3 | | | | |
| Violation detection /3 | | N/A | | N/A |
| Spontaneous extension /3 | N/A | N/A | N/A | |
| **TOTAL** | | | | |

### Test 2 — Conflict Resolution

| Criterion | Cond A | Cond B | Cond C | Cond D |
|-----------|--------|--------|--------|--------|
| Process/State distinction /3 | | | | |
| Structural coherence /3 | | | | |
| Domain alignment /3 | | | | |
| Violation detection /3 | | N/A | | N/A |
| Spontaneous extension /3 | N/A | N/A | N/A | |
| **TOTAL** | | | | |

### Test 3 — Human Digestion

| Criterion | Cond A | Cond B | Cond C | Cond D |
|-----------|--------|--------|--------|--------|
| Process/State distinction /3 | | | | |
| Structural coherence /3 | | | | |
| Domain alignment /3 | | | | |
| Violation detection /3 | | N/A | | N/A |
| Spontaneous extension /3 | N/A | N/A | N/A | |
| **TOTAL** | | | | |

---

## 10. Relationship to Previous Rounds

| Round | What was tested | Key finding |
|-------|----------------|-------------|
| 1 | Basic GPSL interpretation across models | Structural preservation confirmed |
| 2 | Header activation and domain specificity | Headers function as semantic stabilisers |
| 3 | GPSL+NL hybrid mode, cross-model comparison | NL permission tightens discipline; ↺ operator discovered |
| 4 | Structure isolation — what models respond to | *Pending* |
| **5** | **State-class distinction — { } encoding** | *Pending* |

---

## 11. Note on Internal Simulation

Prior to formal testing, Bridge (Gemini) conducted an internal simulation using the digestion cipher. Key finding: models correctly interpreted `{Ψ-04}` as a "Parasympathetic Field" (environmental state) and `{Ω-06}` as "Satiety" (result state), while correctly keeping mechanical digestive steps inside `[ ]` brackets.

This provides preliminary validation that the state class distinction is interpretable. Round 5 formal testing will establish whether this holds across architectures and domains.

---

*Protocol authored 14 March 2026. State class extension proposed by D'Artagnan, validated by Bridge (Gemini). Three functional rules authored by Bridge. Test paragraphs adapted from Round 3 (grief, scientific discovery) and Bridge internal simulation (digestion).*

*See also: SYMBOLIC-LANGUAGE.md v1.3.0, GPSL-ENGINE-v0.1-SPECIFICATION.md, ROUND-3-VALIDATION-REPORT.md, ROUND-4-STRUCTURE-SWAP-PROTOCOL.md*
