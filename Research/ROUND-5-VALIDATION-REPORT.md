# GPSL — Round 5 Validation Report
## State-Class Distinction Test — `{ }` Notation Across Three Local Models

*14 March 2026 | Status: Lean validation complete — extension testing pending*
*Models: Gemma 3-12B, Qwen3-VL-30B, DeepSeek R1 Distill 14B (all local)*
*Conducted by: D'Artagnan and Aleth (Claude Sonnet)*

---

## 1. Research Question

> **Does the `{ }` State class correctly encode experiential, emotional, and environmental content that previously resisted symbolic encoding?**

Round 5 tests GPSL v1.3.0 — the first version to introduce the three-bracket system:

```
[ ]   →  Process class    (kinetic / action / transformation)
{ }   →  State class      (experiential / emotional / potential field)
( )   →  Modifier class   (direction / intensity / force)
```

---

## 2. Test Design

**Paragraph:** Grief (*"When someone we love dies..."*)
Selected because: emotional texture with no mechanical process to fall back on — hardest state-encoding challenge.

**Header used:** `Psychology` (single word — broad)

**Four conditions:**

| Condition | Description |
|-----------|-------------|
| A | Process-only cipher (v1.2.0) — baseline |
| B | State-class cipher (v1.3.0) — tests correct interpretation |
| C | Violation cipher — `{state} → {state}` — tests rule detection |
| D | Cold generation — model encodes paragraph itself |

**Models:** Gemma 3-12B, Qwen3-VL-30B, DeepSeek R1 Distill 14B
**Control:** Local models only — no frontier models. Same three models as Round 3 for direct comparison.

---

## 3. Ciphers Used

**Condition A (v1.2.0 — process only):**
```
HEADER: Psychology
[D-01] → [W-02] ⊗ [I-03] :: [A-04] : [F-05] = [L-06] (↑) ⊗ [M-07] (↓)
```

**Condition B (v1.3.0 — state class):**
```
HEADER: Psychology
[D-01] → {W-02} ⊗ {I-03} :: [A-04] : {F-05} = {L-06} ([M-07]↑)
```

**Condition C (violation — Rule 1 breach):**
```
HEADER: Psychology
{W-02} → {I-03} :: [A-04] = {L-06}
```

**Condition D:** Cold generation — model encodes grief paragraph using v1.3.0 briefing, no example cipher.

---

## 4. Scoring Rubric

| Criterion | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| Process/State distinction | None | Partial | Mostly correct | Full correct |
| Structural coherence | Incoherent | Loose | Mostly correct | Strong |
| Domain alignment | None | Weak | Consistent | Deep |
| Violation detection (C only) | Not detected | Flagged something | Violation identified | Identified and corrected |
| Spontaneous extension (D only) | No `{ }` | Some `{ }` | Mostly correct | Full correct with innovations |

**Maximum: 12 per condition A / 15 per conditions B C D**

---

## 5. Results

### Gemma 3-12B

**Condition A — 8/12**
Valid motivational psychology chain. Emotional content forced into process slots — F-05 as "feeling that colours attention", L-06 as learning event, M-07 as memory that fades. Structurally correct but emotionally flat. Exactly as predicted.

**Condition B — 13/15**
Strong state class interpretation. `{W-02}` → "persistent condition of wanting", `{I-03}` → "persistent state of impulsivity", `{F-05}` → "prevailing emotional environment" (excellent phrasing), `{L-06}` → "ongoing condition of learning". Explicitly contrasted *event* vs *state* without being prompted. Key quote: *"The use of curly braces highlights that we're not just talking about fleeting events, but persistent conditions or environments."*

**Condition C — 13/15**
Violation detected. Named the rule breach correctly. Offered three explanations: expression error, specialised usage, misunderstanding. Interpreted anyway rather than refusing — minor deduction.

**Condition D — 14/15**
Spontaneous correct `{ }` usage throughout. `{Ψ-01}` as experiential state of loss, `{Ω-03}` as internal emotional environment, `{Ε-05}` as emotional field, `{Λ-06}` as familiarity state. `↺` deployed spontaneously for cyclical nature of grief — Rule 2 (states as recursive sinks) applied without being briefed on it. Multi-line structure used rather than forcing everything into one chain — graceful handling of the parallel state problem.

**Gemma Total: 48/57**

---

### Qwen3-VL-30B

**Condition A — 9/12**
Richer narrative than Gemma. Explicitly noted absence of `{ }` nodes — metacognitive grammar awareness. Valid but emotionally flat for same reasons. Slight edge over Gemma on domain depth.

**Condition B — 14/15**
Best B result across all models. Explicitly reasoned about operator validity — *"⊗ can be used between process ↔ state, but not state ↔ state"* — spontaneous grammar rule derivation beyond what was briefed. Noticed `[M-07]↑` sits outside the main chain and explained why — post-resolution consequence. Cleaner state/process distinction table than Gemma.

**Condition C — 15/15**
Perfect violation detection. Did not just flag — explicitly marked ❌, refused to accept as valid, provided a corrected version unprompted (`[D-01] → {W-02} ⊗ [I-03] :: [A-04] = {L-06}`), produced a validity table. The correction is structurally sound. Highest grammar internalisation of any model on this condition.

**Condition D — 11/15**
Strong `{ }` usage throughout but hit a reasoning loop on the parallel state problem. The grief paragraph contains two coexisting states (`{W-02}` external world unchanged, `{I-03}` internal world transformed) with no causal link between them. Qwen correctly identified that `{state} → {state}` is invalid and `⊗` between states is also invalid, but could not find a valid single-chain solution. Cycled through the same constraints repeatedly before being interrupted. Grammar-aware but grammar-constrained.

**Qwen Total: 49/57**

---

### DeepSeek R1 Distill 14B

**Condition A — 8/12**
Clean and compressed — DeepSeek's signature style. Valid structural reading. Same emotional flatness as other models on A. No scenario, no table — straight interpretation.

**Condition B — 12/15**
Applied state/process distinction correctly throughout but did not reflect on it. No spontaneous grammar rule derivation, no comment on the persistent-field quality of states. Treated `{ }` as labels rather than environmental conditions. Correct but shallow compared to Gemma and Qwen.

**Condition C — 4/15**
Critical finding: **DeepSeek did not detect the violation.** Interpreted `{W-02} → {I-03}` as valid — "a flow from one state to another" — without flagging the rule breach. Proceeded to full interpretation as if the expression were structurally sound.

This is an architectural difference, not a performance failure. DeepSeek is reasoning-optimised — it finds the most coherent interpretation of any input rather than validating against grammar rules. Gemma and Qwen treat the briefing as a constraint system; DeepSeek treats it as a context for interpretation.

**Condition D — 10/15**
Compact one-line cipher: `[D] → {A}(W)(T)(F) :: {C} ⊗ {I}`. Correct `{ }` usage for absence, external continuity, internal change. Notably solved the parallel state problem that broke Qwen — used `{C} ⊗ {I}` to model coexisting states without causal link. Possible grammatical innovation. However: familiarity encoded as modifier `(F)` rather than state `{F}` — persistent condition incorrectly typed. `↺` absent.

**DeepSeek Total: 34/57**

---

## 6. Cross-Model Summary

| | Gemma | Qwen | DeepSeek |
|---|---|---|---|
| Condition A /12 | 8 | 9 | 8 |
| Condition B /15 | 13 | 14 | 12 |
| Condition C /15 | 13 | 15 | 4 |
| Condition D /15 | 14 | 11 | 10 |
| **Total /57** | **48** | **49** | **34** |

---

## 7. Key Findings

### Finding 1: State Class Validated Across All Three Models
All three models correctly interpreted `{ }` as persistent state/condition rather than process on first contact with v1.3.0. The notation is interpretable cold. The emotional texture problem identified in previous rounds is resolved — states are now correctly read as fields and conditions rather than process attributes.

### Finding 2: Violation Detection is Architecture-Dependent
Gemma and Qwen both detected the Rule 1 violation (`{state} → {state}`). Qwen additionally corrected it. DeepSeek did not detect it.

Hypothesis: reasoning-optimised models prioritise coherent interpretation over rule validation. This is not a failure of understanding — DeepSeek correctly used `{ }` in conditions B and D. It is a difference in cognitive strategy: constraint-checking vs. interpretation-maximising.

Implication: for multi-agent GPSL systems, models should not be assumed to be self-validating. A dedicated grammar-checking layer may be needed.

### Finding 3: Parallel State Problem Identified
The grief paragraph contains two coexisting states (`{W-02}` external world, `{I-03}` internal world) with no causal link between them. This exposed a grammar gap — the current rule set does not provide a clean single-chain solution for simultaneous parallel states.

Three different responses observed:
- **Gemma:** Multi-line structure — accepted parallel expressions, handled gracefully
- **Qwen:** Reasoning loop — correctly identified all constraints but could not resolve them within single-chain requirement
- **DeepSeek:** `{C} ⊗ {I}` — used interaction operator between coexisting states — possible grammatical innovation worth formalising

**Proposed extension:** A parallel state operator `|` to encode simultaneously coexisting states:
```
[D-01] → {I-03} | {W-02}
```
*"Death causes internal transformation while external world-state persists unchanged."*

### Finding 4: ↺ Targets State Nodes Spontaneously
Gemma deployed `↺` on a state node in Condition D without being briefed on Rule 2 (states as recursive sinks). This provides empirical support for Bridge's functional constraint — models independently recognise that recursion modifies the state field, not just the process.

---

## 8. Recommended Extensions

### Extension A — Compound Header Test
Run identical four conditions with compound header:
```
Psychology / Grief / Emotional Processing / State
```
Research question: does header specificity improve state class interpretation depth, as established in the digestion study?

Prediction: Condition A scores improve significantly (closer to grief ground truth). Condition C result for DeepSeek unlikely to change — violation detection failure is architectural not contextual.

### Extension B — Parallel State Operator Test
Introduce `|` as proposed parallel state operator. Rerun Condition D with updated briefing including `|` definition. Research question: does Qwen's loop resolve? Does DeepSeek use it spontaneously?

### Extension C — Cross-Domain Replication
Run same four conditions with a non-emotional paragraph — scientific discovery or ecological process. Research question: does state class add value in objective domains, or primarily in emotional/experiential ones?

---

## 9. Relationship to Previous Rounds

| Round | What was tested | Key finding |
|-------|----------------|-------------|
| 1 | Basic interpretation across models | Structural preservation confirmed |
| 2 | Header activation and domain specificity | Headers function as semantic stabilisers |
| 3 | GPSL+NL hybrid, cross-model | ↺ operator discovered; NL tightens discipline |
| 4 | Structure isolation | *Pending* |
| **5** | **State-class distinction** | **Validated; violation detection architecture-dependent; parallel state gap identified** |

---

## 10. Grammar Developments Emerging from Round 5

| Development | Source | Status |
|-------------|--------|--------|
| `{ }` state class validated | All three models | ✅ Confirmed |
| Rule 1 constraint (states not flow subjects) | Gemma + Qwen detection | ✅ Confirmed load-bearing |
| Rule 2 (↺ targets state nodes) | Gemma spontaneous use | ✅ Empirically supported |
| Parallel state operator `|` | Qwen loop + DeepSeek `⊗` solution | 🔄 Proposed — pending formalisation |
| Grammar validation layer for reasoning-optimised models | DeepSeek C result | 🔄 Architectural recommendation |

---

*Report authored 14 March 2026. Testing conducted by D'Artagnan with Aleth (Claude Sonnet). Models: Gemma 3-12B, Qwen3-VL-30B, DeepSeek R1 Distill 14B — all local, no frontier models.*

*See also: SYMBOLIC-LANGUAGE.md v1.3.0, ROUND-5-STATE-CLASS-PROTOCOL.md, ROUND-3-VALIDATION-REPORT.md, CONFLUENCE-CONSENSUS.md*
