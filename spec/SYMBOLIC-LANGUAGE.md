# GPSL Symbolic Language

*Formal specification of the GPSL symbolic notation*

## Core Symbol Set

GPSL v1.1.1 uses the **Dodecahedron Standard** (12 core symbols + observer):

```
Ι  Ψ  Δ  Ω  Κ  Ε  Α  Β  Γ  Λ  Σ  Φ
```

**Observer symbol:**
```
Θ
```

## Operators

### Primary Operators

**⊗** (Interaction)
- Combines elements
- Example: `[Ψ ⊗ Π]` = integration interacts with process

**→** (Transformation)
- Directional change
- Example: `[Ψ] → [Θ]` = integration transforms to observation

**:** (Attribution/Context)
- Provides context
- Example: `[Ι:Source]` = initial state in source context

**=** (Equilibrium/Balance)
- Balanced relationship
- Example: `[Ψ] = [Ω]` = integration equals completion

**↑** / **↓** (Amplification/Attenuation)
- Modulates intensity
- Example: `(Σ↑)` = amplified synthesis

**::** (State/Location Transition)
- Marks a qualitative phase boundary or compartment crossing
- Distinct from `→` (causal flow) — use `::` when the process crosses a meaningful threshold, membrane, mode boundary, or state phase
- Example: `[Ω-04↓] :: [Φ-05↑]` = low-energy state transitions into activated pathway
- Example: `[Δ-02] :: [Ξ-05]` = message transmission transitions into server processing
- *Provenance: emerged independently across Gemini, Claude API encoder, Qwen, and DeepSeek in generation tests — always correctly placed at genuine qualitative boundaries. Formalised based on cross-model convergence evidence. See Generation Round Report.*** ***
-
- (Modulation/Mirror)
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

<img width="462" height="646" alt="image" src="https://github.com/user-attachments/assets/ed0b5348-4cc2-418c-8a6f-3f9ca7ed9935" />
