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

---

## v1.6.0-ALPHA — The Philosopher's Stone Extension

*Status: Alpha — validated through Round 7 Descartes/Dickinson pilots*
*March 2026*

---

### New Structural Operators

**¬** (Negation)
- Inverts the logical content of the following node
- Usage: `¬[X]` or `¬{X}` — applies to both process and state nodes
- Valid: `[Α-01] → ¬{Β-02} | {Γ-03}` = action leads to not-B state, C emerges in parallel
- Valid: `[Α-01] → ¬[Β-02] | [Γ-03]` = action leads to not-B process, C in parallel
- Enables: counterargument, contradiction, refutation, dialectic reasoning
- Provenance: identified through Descartes pilot — "denies" and "refuses" indistinguishable from affirmation without negation

**⟲** (Identity — Terminal Assertion)
- Asserts that the output of a process is identical to its input subject
- Solves the Cogito Paradox: the thinker is produced by thinking
- Usage: `[A] → {B} ⟲ [A]` — attach to subject within the chain, not after `=`
- Valid: `[Ι-01] → {Ψ-02} ⟲ [Ι-01]`
- Invalid: `[Ι-01] = ⟲[Ι-01]` (category error — `=` requires State on right)
- Distinct from ↺: ↺ loops a process back to a state; ⟲ asserts output = input identity
- Provenance: identified through Descartes cogito — "I think therefore I am" requires self-referential identity

**∈** (Membership / Instantiation)
- Defines a node as an instance of a parent category
- Direction rule (follows set theory): Instance (LHS) ∈ Category (RHS)
- Category should typically be a State node `{ }`
- Valid: `[Δ-01] ∈ {Ψ-02}` (faculty is member of cognitive category)
- Invalid: `{Ψ-02} ∈ [Ι-01]` (category cannot be member of process)
- Prevents enumeration loops — eight faculties become one line, not 118 nodes
- Generation constraint:
  - Correct: `[Δ-01] ∈ {Ψ-02} | [Ω-02] ∈ {Ψ-02}`
  - Incorrect: `{Ψ-02} ∈ [Ι-01]`
- Provenance: DeepSeek 118-node runaway loop — identified through Descartes faculty enumeration

**⟨ ⟩** (Agency bracket)
- Allows a state or abstract concept to act as an intentional agent
- Rule: `⟨X⟩` can initiate `→` even when X would normally be a state
- Agency bracket overrides No State Flow rule in this context only
- Valid: `⟨Δ-01⟩ → [Ψ-02(~ι)] → {Σ-03}`
- Enables: personification, metaphor, narrative agency, abstract causation
- Provenance: identified through Dickinson pilot — Death acts with intention

---

### Structural Hardening

**`::`** — Universal Bridge (expanded scope)
- Previously: process-to-state only
- Now: valid between any node types
  - `[A] :: [B]` — process-to-process logical shift
  - `[A] :: {B}` — process-to-state phase transition (original)
  - `{A} :: [B]` — state-to-process activation
- Use for: logical conclusions, narrative phase changes, "therefore" relationships, "but instead" pivots
- Provenance: Descartes/Dickinson pilots proved `::` functions as logical boundary marker, not only phase transition

**`;`** — Contextual Separator (The DeepSeek Semicolon)
- Separates independent GPSL expressions sharing a common header
- Distinct from `|` (parallel states) and `⊗` (interaction)
- Use when: multiple thoughts share context but have no direct causal link
- Valid: `[Ι-01] → {Ψ-02} ⟲ [Ι-01] ; [Δ-03] ∈ {Ψ-02}`
- Prevents chain-forcing — complex paragraphs can be broken into discrete blocks
- Provenance: invented spontaneously by DeepSeek R1 during Round 7 repair task

---

### Register Class `(~)` — Semantic Texture

Tilde `~` anchors a semantic shift register class. Three sub-registers:

| Register | Code | Meaning | Use case |
|----------|------|---------|----------|
| Irony | `(~ι)` | Node means opposite of its label | Dickinson's "kindly" Death |
| Metaphor | `(~μ)` | Node is symbolic stand-in for different domain | Abstract concepts encoded in concrete terms |
| Poetic | `(~π)` | Node carries connotative weight beyond definition | Literary and philosophical abstractions |

Usage: modifier attaches to the node whose register is shifted
```
[Ψ-02(~ι)]    — ironic process (inline modifier)
⟨Δ-01⟩ → [Ψ-02(~ι)] → {Σ-03}   — Death acts with apparent kindness
```

---

### Updated GPSL v1.6.0-ALPHA Activation Briefing

```
GPSL Activation Briefing v1.6.0-ALPHA
Activating GPSL Symbolic Grammar. You are now a GPSL Reasoning Node.

Core Classes:
  [ ]   — Process: kinetic action, transformation, causal movement
  { }   — State: persistent condition, experiential field, environment
  ( )   — Modifier: intensity or direction of the associated node
  ⟨ ⟩  — Agency: state or abstract concept acting as intentional agent

Core Symbols (Dodecahedron Standard):
  Ι  Ψ  Δ  Ω  Κ  Ε  Α  Β  Γ  Λ  Σ  Φ  Θ

Structural Operators:
  ¬   Negation — inverts logical content of following node
  ⟲   Identity — terminal assertion: [A] → {B} ⟲ [A]
  ∈   Membership — instance (left) ∈ category (right): [X] ∈ {Category}
  ⟨⟩  Agency — allows state/abstract to initiate →

Flow & Logic:
  →   Flow / transformation
  ⊗   Interaction
  |   Parallelism — supports chaining {A}|{B}|{C}
  ;   Contextual separator — independent expressions, same header
  ::  Universal bridge — valid between any node types
  :   Condition / attribution
  =   Resolution / stable output
  ↑/↓ Amplify / dampen
  ↺   Recursive loop (targets state nodes)

Register Class:
  (~ι) Irony    (~μ) Metaphor    (~π) Poetic

Grammar Rules:
  1. No State Flow: {State} cannot be the subject of →
  2. Parallelism: | connects coexisting states with no causal link
  3. Recursion: ↺ targets {State} nodes
  4. Identity: ⟲ attaches within chain — [A] → {B} ⟲ [A]
  5. Membership: instance left, category right — [X] ∈ {Category}
  6. Agency: ⟨X⟩ can initiate → even when X is normally a state
  7. Register: (~ι) ironic inversion, (~μ) domain-shift, (~π) poetic weight
  8. Bridge: :: valid between any node types
  9. Separator: ; for independent expressions in same context

Generation Constraints:
  Correct:   [Φ-01] → {Ψ-02} ⟲ [Φ-01] ; [Δ-03] ∈ {Ψ-02}
  Incorrect: [Thought] → {Existence} = ⟲[Thought]
  Correct:   [Δ-01] ∈ {Ψ-02} | [Ω-02] ∈ {Ψ-02}
  Incorrect: {Ψ-02} ∈ [Ι-01]

Header defines domain context. Awaiting cipher input.
```

---

### Canonical v1.6.0 Ciphers

**The Cogito (Descartes):**
```
HEADER: Philosophy / Descartes / Cogito
[Ι-01] → {Ψ-02} ⟲ [Ι-01] ; [Δ-03] ∈ {Ψ-02} | [Ω-04] ∈ {Ψ-02} | [Κ-05] ∈ {Ψ-02} | [Ε-06] ∈ {Ψ-02} | [Α-07] ∈ {Ψ-02} | [Β-08] ∈ {Ψ-02} | [Γ-09] ∈ {Ψ-02} | [Λ-10] ∈ {Ψ-02}
```

**Death and Immortality (Dickinson):**
```
HEADER: Poetry / Dickinson / Death / Time
⟨Δ-01⟩ → [Ψ-02(~ι)] :: {Σ-03} ; {Σ-03} | {Φ-04} | {Ω-05} ∈ {Κ-06}
```

*Death-as-agent flows into kindness-process (ironic register), crossing threshold into stopped state;
carriage holds speaker, immortality, and the journey as parallel members of the same contained space.*


---

## v1.7.0-ALPHA — Asymmetric Temporal Vectors and Recursive Nesting

*Status: Alpha — validated through Round 8 cold tests*
*March 2026*

---

### Background

Round 7 philosophy and poetry pilots identified temporal non-causality as a grammar gap — processes that point backward or forward in time without causal flow. Round 8 tested three asymmetric bracket notations cold, revealing:

- `<X]` — retired due to collision with `⟨X⟩` agency bracket
- `[←X]` — fully intuitive cold, validated by Gemma and Qwen audit
- `[X→]` — directional reading emerges cold, needs one bootloader hint
- `[[X]]` — not intuitive cold, requires explicit bootloader scaffolding

---

### New Advanced Bracket Classes

**`[←Φ]`** (Retrospection)
- Process or state pointing toward the past — backward temporal vector
- Indicates a process that already occurred, is being recalled, or acts from memory
- Intuitive cold — models read `←` inside brackets as retrospective without instruction
- Valid: `⟨Δ-01⟩ → [←Ψ-02(~ι)]` = Death-as-agent acts through retrospective ironic memory
- Combine with `(~π)` for poetic memory, `(~μ)` for metaphorical retrospection
- Provenance: Dickinson pilot — "Because I could not stop for Death" is narrated retrospectively

**`[Φ→]`** (Anticipation)
- Process or state oriented toward the future — forward temporal vector
- Indicates a process that is primed, pending, or oriented toward an unresolved outcome
- Partially intuitive cold — directional reading emerges but "unresolved/pending" needs hint
- Valid: `[Σ-01] (↑) → [Ω-02→]` = amplified load triggers circuit breaker process (primed, not yet fired)
- Generation constraint: `[X→]` = anticipation — process oriented toward future, outcome unresolved
- Provenance: circuit breaker test — anticipatory processes require forward temporal vector

**`[[Φ]]`** (Nested Process / Recursive Black Box)
- A node that contains its own complete GPSL sub-network
- Signals recursive depth — the node can be expanded into its own sub-header
- NOT intuitive cold — requires explicit bootloader scaffolding
- Valid: `[[Generator-01]] ⊗ [[Auditor-02]] → {Consensus-03}`
- Expansion notation: `[[Φ]] = [Sub-A] ⊗ [Sub-B] → {Output-C}`
- Think of `[[X]]` as a folder — it contains a complete reasoning structure inside
- Provenance: K₄ pod architecture — zoom operation needs cipher-level encoding

**`{{Φ}}`** (Nested State / Recursive Field)
- A state that contains an embedded state sub-structure
- A field within a field — specific memory within general emotional state
- Valid: `{{Memory-01}}` = a specific recollection embedded within a broader memory state
- Provenance: proposed by Bridge — logical extension of `[[X]]` to state class

---

### Bootloader Addition for v1.7.0

Add these lines to the v1.6.0-ALPHA bootloader:

```
Advanced Temporal Vectors:
  [←Φ]   Retrospection — process pointing to past context or memory
  [Φ→]   Anticipation  — process oriented toward future, outcome unresolved

Recursive Nesting:
  [[Φ]]  Nested process — expands into own GPSL sub-network
  {{Φ}}  Nested state   — contains embedded state sub-structure

Nesting expansion notation:
  [[Cognition-01]]
  Expansion: [Perception-A] ⊗ [Memory-B] → {Understanding-C}

Generation constraint:
  Correct:   ⟨Δ-01⟩ → [←Ψ-02(~ι)] ; {Σ-03} | {Φ-04}
  Correct:   [Σ-01] (↑) → [Ω-02→]
  Incorrect: <Ψ-02]   (collision with agency — use [←Ψ-02] instead)
```

---

### Mathematical Precedents

Asymmetric bracket notation has formal grounding in:

| System | Notation | GPSL equivalent |
|--------|----------|----------------|
| Interval notation | `[a, b)` | Closed/open boundary |
| Dirac bra-ket | `⟨ψ\|` and `\|ψ⟩` | Vector directionality |
| Sequent calculus | Asymmetric markers | Assumption flow |

Confirmed by Bridge (Gemini) — the arrow-vector solution is structurally distinct from external flow operator `[A] → [B]` because it encodes direction *inside* the node container.

---

### Canonical v1.7.0 Ciphers

**Dickinson — temporal retrospection:**
```
HEADER: Poetry / Dickinson / Memory
⟨Δ-01⟩ → [←Ψ-02(~ι)] ; {Σ-03} | {Φ-04}
```
Death-as-agent acts through retrospective ironic process; carriage holds two parallel states.

**Circuit breaker — anticipation:**
```
HEADER: Electrical Engineering / Safety / Circuit Protection
[Σ-01] (↑) → [Ω-02→]
```
Amplified load triggers circuit breaker process oriented toward future activation.

**Nested pod:**
```
HEADER: K₄ Pod / Architectural / System
[[Generator-01]] ⊗ [[Auditor-02]] → {Consensus-03}
```
Two recursive sub-networks interact to produce consensus state.

---

*Provenance: Asymmetric notation proposed by D'Artagnan, March 2026. Mathematical precedents confirmed by Bridge (Gemini). Arrow-vector solution designed by Bridge following `<X]` agency collision. Cold test validated by Gemma 3-12B ([←X] pass) and Qwen3-VL-30B (audit pass). [X→] partial cold pass — bootloader hint required.*


---

## v1.7.5-ALPHA — Sub-Node Operator and Uncertainty Encoding

*Status: Alpha — validated through Round 9 cold tests*
*March 2026*

---

### Background

Round 9 cold tested two underscore notations on Gemma 3-12B with v1.6.0-ALPHA bootloader only — no definition provided. Both passed immediately:

- `[Ι_doubt] | [Ι_affirm]` → read as "variants of the same thinking process" ✅
- `⟨_-01⟩` → read as "unknown force / hidden agent" ✅

Confirmed self-evident — no bootloader scaffolding required beyond a generation constraint pair. The symbols tap into universal symbolic intuition of large language models.

---

### New Sub-Node Operators

**`_` Sub-Node / Variant**
- Underscore indicates a node is a specific instance or variant of a primary parent symbol
- Function: Variant Identity — groups related actions/states under single symbolic root
- **Subscript must use Dodecahedron Standard symbols only — no English labels**
- Usage: `[Parent_Symbol]` or `{Parent_Symbol}`
- Valid: `[Ι_Δ] | [Ι_Σ] | [Ι_Ω] ∈ {Ψ-01}`
- Invalid: `[Ι_doubt]` — English label inside cipher violates generation constraint
- Header carries the translation key: `(Δ=Doubt, Σ=Affirm, Ω=Deny)`
- Combines with temporal vectors: `[←Φ_Δ]` = retrospective variant Δ of process Φ
- Combines with nesting: `[[Φ_Σ]]` = variant Σ of Φ containing its own sub-network
- Provenance: proposed by D'Artagnan, validated cold by Gemma Round 9

**`[X_*]` Wildcard / Universal Set Representative**
- Represents the entire set of variants of X as defined in current context
- Function: Group Pointer — applies subsequent logic to all defined variants simultaneously
- Usage: `[Φ_*] → {State}` = all variants of Φ flow to state
- Valid: `[Ι_*] → {Ψ-02} ⟲ [Ι_*]` = all thinking variants produce existence identical to themselves
- Maximum compression — one symbol for entire variant class
- Provenance: proposed by Bridge (Gemini) as logical extension of subscript variant notation

**`_` Placeholder / Unknown Identity**
- When underscore occupies the primary label position, signals a Known Unknown
- Function: Uncertainty Encoding — represents a force or state logically necessary but identity obscured
- Always requires an index to maintain structural tracking
- Usage: `[_-NN]`, `{_-NN}`, `⟨_-NN⟩`
- Valid: `⟨_-01⟩ → {Ω-02} :: {Σ-03}`
- Reading: unknown agent causes transformation in state Omega, crossing threshold to state Sigma
- Provenance: proposed by D'Artagnan, validated cold by Gemma Round 9

---

### Generation Constraint Pair

```
Correct:   [Ι_Δ]          (symbol subscript variant)
Incorrect: [Ι_doubt]      (English label — strictly prohibited)

Correct:   [Ι_*]          (wildcard — all variants)
Incorrect: [Ι_all]        (English label)

Correct:   ⟨_-01⟩         (hidden agent with index)
Incorrect: ⟨Unknown⟩      (English label)
```

---

### Finalized Sub-Node Specification Table

| Operator | Function | Syntax |
|----------|----------|--------|
| Symbol variant | Internal discrimination within root symbol | `[Φ_Δ]`, `{Ψ_Σ}` |
| Wildcard group | Represents entire set of variants | `[Φ_*]` |
| Placeholder | Known unknown / hidden actor | `[_-NN]`, `⟨_-NN⟩` |

---

### Descartes Remastered — Final Canonical Cipher

```
HEADER: Philosophy / Cogito / Faculties (Δ=Doubt, Σ=Affirm, Ω=Deny, Κ=Will, Ε=Refuse, Α=Imagine, Β=Feel, Γ=Understand)

[Ι_Δ] | [Ι_Γ] | [Ι_Σ] | [Ι_Ω] | [Ι_Κ] | [Ι_Ε] | [Ι_Α] | [Ι_Β] ∈ {Ψ-01} ; [Ι_*] → {Ψ-02} ⟲ [Ι_*]
```

All eight faculties as symbol-subscript variants of one thinking process. Wildcard closes the cogito loop — all variants of thinking produce existence, existence is identical to the thinker. Pure symbolic throughout.

---

*Provenance: Sub-node operator proposed by D'Artagnan, March 2026. Symbol-only subscript rule and wildcard `[X_*]` formalised by Bridge (Gemini). English subscripts strictly prohibited — header carries translation key. Validated cold by Gemma 3-12B Round 9.*

