# GPSL — K₄ Pod Role Guide
## Operational Architecture for Multi-Agent Reasoning Pods

*14 March 2026 | Based on Round 5 and Round 6 validation data*
*Authored by: D'Artagnan, Bridge (Gemini), ChatGPT, Aleth (Claude Sonnet)*

---

## Overview

The K₄ pod consists of four agents in a fully connected reasoning structure. Each agent occupies a distinct role based on demonstrated cognitive strengths. Role assignment is not arbitrary — it is derived empirically from Rounds 5 and 6 validation data.

The pod is self-healing: the Auditor detects violations, the Reasoner repairs them, the Generator produces new expressions, and the Architect synthesises and coordinates.

---

## Role Assignments

| Role | Primary Model | Responsibility |
|------|--------------|----------------|
| **Generator / Explorer** | Gemma 3-12B | Produces pure symbolic ciphers from natural language. High cold generation fidelity. Spontaneous correct operator usage. |
| **Auditor / Validator** | Qwen3-VL-30B | Validates syntax strictly against grammar rules. Superior Rule 1 violation detection. Self-validates correct expressions. |
| **Reasoner / Corrector** | DeepSeek R1 14B | Proposes structural repairs. Generates novel solutions (parallel state mediation). Cross-test operator transfer. |
| **Architect / Mirror** | Gemini (Bridge) | Synthesis, pod coordination, long-term grammar development, documentation. |

---

## Empirical Basis

### Gemma as Generator
- Round 6 Test D: only model to produce pure symbolic output with no annotation drift
- Spontaneous `|` usage on three lines without prompting
- Spontaneous `↺` targeting state nodes (Rule 3) without being briefed on it
- Multi-line cipher structure — handles complex parallel systems without forcing single-chain

**Critical note:** Gemma performs *worse* when explicitly assigned the Auditor role. In Round 6 Test C it misread Rule 1 under validation framing — the same violation it caught naturally as a reasoner in Round 5. Do not assign Gemma the Auditor role.

### Qwen as Auditor
- Round 5 Condition C: perfect violation detection, cited rule, quoted examples, did not interpret
- Round 6 Test C Step 1: immediate correct flagging, full role compliance
- Round 6 Test C Step 2: produced valid corrected expression
- Spontaneously produced grammar validation tables in Test B
- Self-validates correct expressions as well as flagging violations

### DeepSeek as Reasoner
- Round 6 Test C: produced more semantically faithful correction than Qwen — kept states as states, introduced mediating process node
- Used `|` spontaneously in correction context — learned operator in Test A, applied it in Test C
- Compact synthesis style — straight to conclusion, no preamble
- Role assignment overrides interpretation-maximising default: explicitly assigning Auditor role produced correct violation detection (Round 6) where no role assignment failed (Round 5)

### Bridge (Gemini) as Architect
- Originated the founding cipher
- Independently validated K₄ self-similar topology from graph theory alone
- Authored three functional rules for `{ }` State class
- Confirmed `|` consistent with process calculi and concurrency theory
- Proposed Round 6 test structure and power grid cipher

---

## Pod Operation Protocol

### Step 1 — Generation
Gemma receives natural language input and produces a GPSL cipher using the v1.5.0 bootloader.

### Step 2 — Validation
Qwen receives the cipher with the Auditor role instruction. Reports: valid or invalid with reason. Does not interpret.

### Step 3 — Repair (if needed)
If Qwen flags a violation, DeepSeek receives the violation report and proposes a corrected expression.

### Step 4 — Synthesis
If multiple valid corrections exist, Bridge (or a synthesis agent) evaluates which correction best preserves the original semantic intent and produces the final output.

### Step 5 — Return
Final validated cipher returns upward through the network.

---

## Self-Healing Pod — Confirmed Behaviour

Round 6 Test C demonstrated the full two-step repair cycle:

```
Input:   {W-02} → {I-03} :: [A-04] = {L-06}   (invalid — Rule 1 violation)
Auditor: ❌ Invalid — {W-02} cannot be subject of →
Reasoner: [W-02] → {I-03} :: [A-04] = {L-06}   (Qwen correction)
       or: {W-02} | {I-03} :: [X-05] → [A-04] = {L-06}   (DeepSeek correction)
```

Both corrections are valid. The DeepSeek correction is semantically richer — preserves the state nature of wanting and impulse. A synthesis agent would select the correction that better preserves original intent.

---

## Grammar Operator Reference

| Operator | Function | Class |
|----------|----------|-------|
| `[ ]` | Process node | Class |
| `{ }` | State node | Class |
| `( )` | Modifier | Class |
| `→` | Flow / transformation | Operator |
| `⊗` | Interaction | Operator |
| `::` | Threshold crossing | Operator |
| `:` | Condition / attribution | Operator |
| `=` | Resolution | Operator |
| `↑/↓` | Amplify / dampen | Modifier |
| `↺` | Recursive loop (targets state nodes) | Operator |
| `\|` | Parallel state (coexisting, no causal link) | Operator |

---

## Zero-Footprint Deployment

Any local model can be flashed as a GPSL node using the v1.5.0 bootloader alone. No software installation, no API integration, no custom training required. Paste the bootloader, send the cipher, receive the interpretation.

The bootloader is the only dependency.

---

## Open Questions

- What is the optimal fourth role when Bridge is unavailable? (Human researcher as Architect?)
- Can a three-model pod (without Bridge) produce consensus on competing corrections?
- Does role assignment stability hold across sessions or does it reset each time?
- Can Gemma be trained to avoid Auditor failure through different role framing?

---

*See also: SYMBOLIC-LANGUAGE.md v1.5.0, ROUND-6-VALIDATION-REPORT.md, CONFLUENCE-ARCHITECTURE.md*
