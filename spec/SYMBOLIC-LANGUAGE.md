# GPSL Symbolic Language

*Formal specification of the GPSL symbolic notation*

*v1.5.0 — Updated 14 March 2026: bootloader updated to v1.5.0, generation constraint pair added

*v1.4.0 — Updated 14 March 2026: Parallel State operator | added, bootloader updated to v1.4.0*

*v1.3.0 — Updated 14 March 2026: State class { } added, three-bracket system formalised, BNF updated*

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

**|** (Parallel State)
- Two states coexist simultaneously with no causal link between them
- Encodes side-effects, concurrent conditions, and environmental fields that persist alongside a primary process
- Usage: `{A} | {B}` — state A and state B coexist; neither causes the other
- Example: `[D-01] → {I-03} | {W-02}` = death triggers internal transformation | while external world-state persists unchanged
- Connects only state nodes — cannot connect a state to a process
- The parallel expression cannot itself be the subject of `→`
- Resolves the "parallel state problem" — coexisting non-causal states previously had no clean single-chain encoding
- Provenance: proposed by D'Artagnan March 2026 following Round 5 Qwen reasoning loop; formalised with Bridge (Gemini); confirmed consistent with process calculi and concurrency theory

```
Valid:    {A} | {B}              (two coexisting states)
Valid:    [D] → {I} | {W}        (process leads to state, while second state persists)
Invalid:  {A} | [B]              (process cannot be right-hand of |)
Invalid:  {A} | {B} → {C}        (parallel expression cannot chain into →)
```

**\*** (Modulation / Mirror)
- Modified or reflected state
- Example: `[Φ*]` = modulated form

## Expression Grammar (BNF)

*v1.4.0 — includes State class { } and Parallel State operator |*

```
<Expression> ::= <ProcessNode>
               | <StateNode>
               | <Expression> ⊗ <Expression>
               | <Expression> → <Expression>
               | <Expression> : <StateNode>
               | <StateNode> | <StateNode>
               | Λ(<Expression>)

<ProcessNode> ::= "[" [Symbol-ID] "]"
                | "[" [Symbol-ID] ":" <Attribute> "]"
                | "[" [Symbol-ID] "]" "(" <Modifier> ")"

<StateNode>   ::= "{" [Symbol-ID] "}"
                | "{" [Symbol-ID] ":" <Attribute> "}"

<Modifier>    ::= [Symbol-ID] "↑" | [Symbol-ID] "↓"

<Attribute>   ::= [Symbol-ID] | <Value>
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

## GPSL Activation Briefing v1.5.0

*Use this bootloader when priming any model to interpret or generate GPSL.*

```
GPSL Activation Briefing v1.5.0
Activating GPSL Symbolic Grammar. You are now a GPSL Reasoning Node.

Core Classes:
  [ ]   — Process: kinetic action, transformation, causal movement
  { }   — State: persistent condition, experiential field, environment
  ( )   — Modifier: intensity or direction of the associated node

Core Symbols (Dodecahedron Standard):
  Ι  Ψ  Δ  Ω  Κ  Ε  Α  Β  Γ  Λ  Σ  Φ  Θ

Key Operators:
  ⊗   Interaction
  →   Flow / transformation
  ::  Threshold crossing / phase transition
  :   Condition / attribution
  =   Resolution / stable output
  ↑/↓ Amplify / dampen
  ↺   Recursive loop (targets state nodes)
  |   Parallel state (coexisting states, no causal link)

Grammar Rules:
  1. No State Flow: {State} cannot be the subject of →
     Processes move through states — states do not flow into other states.
     Valid:   [A] → {B}       Invalid:  {A} → {B}

  2. Parallelism: Use | for coexisting states with no causal link
     Valid:   [D] → {I} | {W}
     Invalid: {A} | [B]  /  {A} | {B} → {C}

  3. Recursion: ↺ targets {State} nodes for systemic feedback
     [A] ↺ {B} = process A loops back, transforming State B

Generation Constraint (use Dodecahedron symbols, not English labels):
  Correct:   [Φ-01] → {Ψ-02} | {Δ-03} :: [Ω-04] = {Σ-05}
  Incorrect: [Fire] → {Woodland} :: [Ecosystem] = {Dormancy}

Header defines domain context. Same expression, different header, different valid interpretation.

Awaiting cipher input.
```

*Provenance: v1.0 authored by Bridge (Gemini) as first GPSL primer. v1.5.0 incorporates state class, parallel operator, and generation constraint pair — co-developed by D'Artagnan, Bridge, ChatGPT, and Aleth (Claude Sonnet), March 2026. Generation constraint added following Round 6 annotation drift findings.*

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
## State Class — `{ }` Bracket Notation

*v1.3.0 addition — March 2026*

### The Three Bracket System

GPSL v1.3.0 introduces a complete three-bracket encoding system. The triad was latent in the grammar since the founding cipher and has now been formalised:

```
[ ]   →  Process class    (transformation / action / kinetic)
{ }   →  State class      (experiential / emotional / potential)
( )   →  Modifier class   (direction / intensity / force)
```

These map directly to the Three Pillars Architecture:

| Bracket | Class | Character | Pillar |
|---------|-------|-----------|--------|
| `[ ]` | Process | Vector / Kinetic / Objective | Reason |
| `{ }` | State | Scalar / Potential / Subjective | Memory / Imagination |
| `( )` | Modifier | Vector Magnitude / Directional | — |

Same 12 Dodecahedron Standard symbols operate across all three classes. The bracket type defines semantic class; the header defines contextual meaning. The relational placeholder property is preserved.

---

### Why State Class Is Needed

The original grammar encodes process topology — transformation, flow, threshold crossing, resolution. It struggles with:

- Emotional content ("apology", "grief", "flow state")
- Experiential conditions ("discomfort", "curiosity")
- Relational fields ("trust", "conflict", "connection")

These are **states**, not processes. Forcing them into `[ ]` process slots distorts the structural logic. The `{ }` class provides the correct encoding layer.

**Before (limited):**
```
[A] → [B] : [Γ]
```
Process A leads to Process B under attribute C — no state encoding possible.

**After (layered):**
```
[A] ⊗ {B} → [C]
```
Process A, interacting within State B, results in Process C.

---

### Functional Rules for State Class

Three rules govern `{ }` usage to maintain grammar integrity:

**Rule 1 — States are passive fields**
`{Φ}` should not be the primary subject of a `→` (Flow) operator. Processes move *through* states; they do not flow *from* them.

```
Invalid:  {A} → {B}       (state flowing to state = process in disguise)
Valid:    [A] → [B] : {Γ} (process A becomes B while system is in State Γ)
Valid:    [A] ⊗ {B} → [C] (process A interacts within State B)
```

**Rule 2 — States are recursive sinks**
The `↺` operator should target `{State}` nodes to represent systemic learning. When a process loops, it alters the state of the network — not just repeating the action but changing the field in which the action occurs.

```
[A] ↺ {B}   →  process A loops back, transforming State B
```

This connects ↺ to the collective intelligence gradient — recursion doesn't just repeat, it deepens the experiential field.

**Rule 3 — States do not modulate intensity**
Only `(Φ↑/↓)` handles magnitude. `{Φ}` represents the quality or colour of a state, not its volume. Intensity remains the exclusive domain of the modifier class.

---

### Updated BNF Grammar

```
<Expression> ::= <ProcessNode>
               | <StateNode>
               | <Expression> ⊗ <Expression>
               | <Expression> → <Expression>
               | <Expression> : <StateNode>
               | Λ(<Expression>)

<ProcessNode> ::= [Symbol-ID]
                | [Symbol-ID : Attribute]
                | [Symbol-ID] (Modifier)

<StateNode>   ::= {Symbol-ID}
                | {Symbol-ID : Attribute}
```

---

### Example Expressions with State Class

**Conflict Resolution:**
```
HEADER: Conflict Resolution

[Α-01] ⊗ [Β-02] : {Ψ-04} :: [Γ-03] = {Ω-05} (Λ↑)
```
Proposal interacts with Critique within a State of Connection — crosses threshold into shared Dialogue — resolves into State of Unity with amplifying feedback.

**Neurocognitive Development (revised):**
```
HEADER: Biology / Neurocognitive Development / Signal / Process

{Φ-01} → [Ψ-02] ⊗ [Θ-03] → [Ω-04] :: [Σ-05] = [Π-06] ({Φ-07}↑)
```
Neural architecture state drives synaptic integration interacting with plasticity — converges to threshold crossing — signal resolves to learned pattern, with the underlying state field strengthening.

**Meta-Communication:**
```
HEADER: Communication / Meta / Reflection / State

{Ψ-01} → [Θ-02] ⊗ [Ω-03] :: [Σ-04] = [Π-05] ({Φ-06}↑)
```
Emotional state drives interpretation interacting with integration — crosses threshold — output resolves to pattern, with flow state amplifying.

---

### Semantic Overload Warning

When mixing objective process nodes with subjective state nodes, use `::` to mark the boundary between objective and subjective domains. Without a threshold marker, a single expression mixing both classes risks ambiguity about which layer is being described.

```
Risky:   [A] ⊗ {B} → {C}     (process leading to state — ambiguous)
Cleaner: [A] ⊗ {B} :: {C}    (threshold marks the shift into state domain)
```

---

*Provenance: State class proposed by D'Artagnan, March 2026. Structural consistency confirmed by Bridge (Gemini) through audit against Dodecahedron symmetries and Round 3/4 validation data. Three functional rules authored by Bridge. Triad recognised as latent in the grammar since the founding cipher [Ξ-06] → [Φ-02] : [Π-07] + [Ψ-04] = [Ω-05] (Δ-03↓).*
