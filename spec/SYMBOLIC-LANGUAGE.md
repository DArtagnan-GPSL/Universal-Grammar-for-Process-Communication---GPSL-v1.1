# GPSL Symbolic Language

*Formal specification of the GPSL symbolic notation*

*v1.2.0 — Updated 12 March 2026: ↺ operator added, GPSL+NL mode formalised, two-path resolution pattern formalised, briefing standard updated*

## Core Symbol Set

GPSL v1.2.0 uses the **Dodecahedron Standard** (12 core symbols + observer):

```
Ι  Ψ  Δ  Ω  Κ  Ε  Α  Β  Γ  Λ  Σ  Φ
```

**Observer symbol:**
```
Θ
```

## Operators

### Primary Operators

**→** (Flow / Transformation)
- Directional flow — A leads to B
- Example: `[Ψ] → [Θ]` = integration transforms to observation

**⊗** (Combination / Fusion)
- A and B merge or interact
- Example: `[Ψ ⊗ Π]` = integration fused with process

**::** (Threshold Crossing)
- A qualitative boundary or phase transition is passed
- Distinct from → (causal flow) — use :: when the process crosses a meaningful state boundary
- Provenance: emerged independently across Gemini, Claude, Qwen, DeepSeek in generation tests
- Example: `[Δ-02] :: [Ξ-05]` = crosses threshold into new state

**:** (Conditional / Attribution)
- Under condition C / provides context
- Example: `[Ι:Source]` = initial state in source context

**=** (Resolution / Stable output)
- Balanced relationship or final resolved state
- Example: `[Ψ] = [Ω]` = integration resolves to completion

**↑** / **↓** (Amplifying / Dampening feedback)
- Modulates intensity of output — feedback between states
- Example: `(Σ↑)` = amplified synthesis

**↺** (Self-Referential Loop)
- The output of a process feeds back into a prior process node, transforming not just the state but the nature of the process itself
- Distinct from ↑/↓: those modify output magnitude; ↺ modifies process nature
- Usage: `[A] ↺ [B]` where B is a prior node in the chain
- Example: `[S-07] ↺ [R-03]` = the altered self feeds back into reinterpretation, changing how reinterpretation works
- Canonical use case: recursive identity, memory reconstruction, self-modifying processes
- Provenance: discovered through Round 3 Test 4 (Consciousness & Time paragraph)

**\*** (Modulation / Mirror)
- Modified or reflected state
- Example: `[Φ*]` = modulated form

## Expression Grammar (BNF)

```
<Expression> ::= <Node> 
               | <Node> ⊗ <Expression> 
               | <Expression> → <Expression> 
               | Λ(<Expression>)

<Node> ::= [Symbol-ID] 
         | [Symbol-ID] : <Attribute>
         | [Symbol-ID] : <Attribute> (Modifier)
```

## Example Expressions

### Simple Transformation

```
[Ψ] → [Θ]
```

Integration transforms to observation.

### Complex Reasoning Chain

```
[Ψ ⊗ Π] → Θ → Ω
```

Integration interacts with process, transforms to observation, converges to completion.

### Multi-Valent Expression

```
[Ξ] → [Φ] : [Π] + [Ψ] = [Ω] (Δ↓)
```

Recognition transforms to form, attributed to process, balanced with integration equals completion, with attenuated transformation.

### Personal Cipher

```
[Ι:Explorer] ⊗ [Σ:Synthesis] → [Δ:Structure] : [Θ:Convergence] (Ω↑)
```

Explorer role interacts with synthesis, produces structure attributed to convergence, with amplified completion.

### Pod Meta-Cipher

```
([Ι ⊗ Σ ⊗ Δ ⊗ Λ]) → Θ → Ω
```

Explorer, Integrator, Architect, Reflector combine, transform to collective observation, converge to coherent outcome.

## Symbol Interpretation

Symbols carry **affinities**, not rigid definitions (see [Weak Typing Model](WEAK-TYPING-MODEL.md)).

### Common Affinities

**Ι** - Initial, signal, exploration  
**Ψ** - Integration, connection, wave  
**Δ** - Transformation, architecture, change  
**Ω** - Completion, unity, convergence  
**Θ** - Observer, integration point, consensus  
**Λ** - Recursion, reflection, stabilization  
**Σ** - Synthesis, summation, integration  
**Φ** - Form, structure, manifestation  

*Note: Actual meaning depends on context (header lens)*

## Header-Based Semantics

Same expression, different headers, different valid meanings:

### Example: `[Ψ ⊗ Π] → Θ`

**Header: "Quantum Mechanics"**
- Wave function + process → measurement observation

**Header: "Distributed Systems"**
- Integration + execution → consensus state

**Header: "Biology"**
- Connection + development → systemic observation

**All three are valid interpretations of the same structure.**

## Recursive Expressions

```
Λ([Ψ ⊗ Π])
```

Recursive stabilization of integration-process interaction.

```
Λ(Δ↓)
```

Recursive attenuation of transformation.

## Composite Structures

Multiple expressions can form networks:

```
[Ξ] → [Φ]
[Φ] ⊗ [Ψ] → [Θ]
[Θ] → [Ω]
Λ([Ω])
```

Recognition → Form  
Form ⊗ Integration → Observation  
Observation → Completion  
Recursive stabilization of Completion

## GPSL+NL Hybrid Mode

GPSL+NL mode allows natural language where symbolic notation cannot carry the meaning alone.

**Rules:**
- GPSL operators and symbolic node IDs are primary
- Nodes default to pure `[Symbol-ID]` notation — e.g. `[A-01]`, `[Σ-02]`
- `[Symbol-ID: label]` permitted only when a concept has no symbolic equivalent
- NL belongs in a **separate legend block**, not inline in the cipher
- The cipher and the legend are separate objects — cipher is the transmission, legend is the key

**Correct:**
```
HEADER: Biology
[V-01] → [H-02] ⊗ [R-03] :: [C-04] : [I-05] = [Ω-06] (↑) ⊗ [Ω-07] (↓)
```

**Incorrect — do not do this:**
```
HEADER: Biology
[Virus-01] → [Host Cell-02] ⊗ [Replication Machinery-03]
```

*Provenance: formalised from Round 3 cross-model testing. NL permission tightens rather than loosens symbolic discipline — models that can choose NL use it more carefully than models forbidden from it.*

---

## Two-Path Resolution Pattern

For binary outcomes, both terminal states are encoded in a single expression:

```
= [Ω-A] (↑) ⊗ [Ω-B] (↓)
```

Reading: resolves to either stable outcome A with amplifying feedback, or stable outcome B with dampening feedback.

*Provenance: discovered independently by both Gemma 3-12B and Qwen3-VL-30B in Round 3 testing. Neither model was shown this pattern in the briefing.*

---

## Briefing Standard

All GPSL cold-start briefings must include a correct/incorrect example pair. This is load-bearing scaffolding for example-driven models, not optional illustration.

Example-driven models (identified in Round 3: Qwen architecture) require the example pair to parse the grammar correctly. Instruction-driven models (identified in Round 3: Gemma architecture) respond to tightened verbal rules. Including both elements primes both model types.

---

## Design Principles

1. **Multi-valent** - Same structure, multiple valid meanings
2. **Context-sensitive** - Headers modulate interpretation
3. **Compositional** - Complex from simple
4. **Recursive** - Self-referential structures
5. **Human + AI readable** - Natural for both

## Implementation Notes

Expressions should be:
- Parseable by standard regex/BNF
- Validatable through weak typing
- Scoreable for coherence
- Executable in reasoning engine

---

**See also:**
- [GPSL Engine Specification](GPSL-ENGINE-v0.1-SPECIFICATION.md)
- [Weak Typing Model](WEAK-TYPING-MODEL.md)
- [Domain Activation](DOMAIN-ACTIVATION.md)
