# GPSL Engine v0.1 Specification
## Computational Reasoning System

**Version:** 0.1  
**Status:** Formally Specified — Ready for Implementation  
**License:** CC BY-NC-SA 4.0

---

## Overview

This document specifies the GPSL Engine: a computational reasoning system built on distributed reasoning pods, header-based domain semantics, and convergence/stabilization nodes.

**Key property:** GPSL expressions are structure-first. Symbols and operators encode transformation logic. Headers activate domain-specific semantic interpretation without altering the underlying structure.

---

## 1. Formal Representation of GPSL Expressions

### Symbols

**Core (Dodecahedron Standard):**
```
Ι  Ψ  Δ  Ω  Κ  Ε  Α  Β  Γ  Λ  Σ  Φ
```

**Observer/Integration:**
```
Θ
```

### Operators

| Operator | Function |
|----------|----------|
| ⊗ | Interaction between symbols |
| → | Transformation (causal/derivative progression) |
| : | Attribution (associates properties or context) |
| = | Balance / equivalence (conservation principle) |
| ↑ / ↓ | Amplification / attenuation (modulation of effect or weight) |
| * | Modulator (contextual influence) |

### Expression Grammar (BNF)

*v1.3.0 — updated to include State class*

```
<Expression> ::= <ProcessNode>
               | <StateNode>
               | <Expression> ⊗ <Expression>
               | <Expression> → <Expression>
               | <Expression> : <StateNode>
               | Λ(<Expression>)

<ProcessNode> ::= "[" [Symbol-ID] "]"
                | "[" [Symbol-ID] ":" <Attribute> "]"
                | "[" [Symbol-ID] "]" "(" <Modifier> ")"

<StateNode>   ::= "{" [Symbol-ID] "}"
                | "{" [Symbol-ID] ":" <Attribute> "}"

<Modifier>    ::= [Symbol-ID] "↑" | [Symbol-ID] "↓"

<Attribute>   ::= [Symbol-ID] | <Value>
```

### Class Notation — Three Bracket System

GPSL v1.3.0 formalises three semantic classes through bracket notation:

| Bracket | Class | Character |
|---------|-------|-----------|
| `[ ]` | Process | Kinetic / action / transformation |
| `{ }` | State | Scalar / experiential / persistent field |
| `( )` | Modifier | Intensity / direction / magnitude |

**Doing vs Being:** The introduction of `{State}` nodes resolves the "texture paradox" in emotional and biological domains. Previous versions forced scalar experiential qualities into kinetic process slots, distorting structural logic. The State class encodes the *environment or condition* in which a process occurs, not the process itself.

**Constraint:** `{State}` nodes should not be the primary subject of a `→` (Flow) operator. States are conditions inhabited; they do not themselves transform into other states. Processes move *through* states.

```
Invalid:  {A} → {B}        (state flowing to state)
Valid:    [A] → [B] : {Γ}  (process under state condition)
Valid:    [A] ⊗ {B} → [C]  (process interacting within state field)
```

### Special Patterns

**Mirror Logic (Λ nodes):** Λ nodes recursively reference prior expressions, enabling self-consistent feedback loops and stabilization.

**Observer Node (Θ):** Meta-symbol capturing network-wide state; integrates outputs from distributed reasoning pods.

---

## 2. Header-Based Domain Semantics

### Header Structure

```
HEADER: "<Natural-language description of domain or conceptual lens>"
```

### Function

Headers map abstract GPSL symbols to domain-specific semantics without altering the core symbolic structure. The same expression can be validly interpreted under different domain headers — this multi-valent property is a core feature of the system.

**Example:**
- Header: `"Distributed systems fault tolerance"` → Ψ interpreted as "state integration", → as "propagation"
- Header: `"Biological adaptation"` → Ψ interpreted as "cellular integration", → as "evolutionary transition"

Structure remains constant; meaning layer changes.

### Adapter Mechanism

```python
def interpret(expression, header):
    domain_rules = parse_header(header)
    for node in expression:
        node.meaning = domain_rules.get(
            node.symbol, 
            default_symbol_meaning(node.symbol)
        )
    return expression
```

### Header Registry

The engine maintains a registry of active domain headers. Headers are applied at the reasoning layer and persist through the session.

```python
class HeaderRegistry:
    def __init__(self):
        self.active_headers = {}
    
    def activate(self, session_id: str, header: str):
        self.active_headers[session_id] = header
    
    def get_active(self, session_id: str) -> str | None:
        return self.active_headers.get(session_id)
    
    def deactivate(self, session_id: str):
        self.active_headers.pop(session_id, None)
```

**See also:** [Domain Activation Specification](DOMAIN-ACTIVATION.md)

---

## 3. Reasoning Pods

### Concept

Reasoning pods are autonomous modules that derive new expressions from existing ones. Pods operate independently while sharing a common GPSL expression graph.

### Pod Responsibilities

1. **Observe** — Pull latest GPSL expressions from the shared graph
2. **Apply Rules** — Use transformation, balance, and modulation operators to derive candidate expressions
3. **Validate** — Ensure semantic coherence via active header(s)
4. **Submit** — Return new expressions to the shared network

### Pod Workflow

```python
for expr in input_expressions:
    candidates = apply_transformations(expr)
    for candidate in candidates:
        if validate(candidate, active_header):
            submit(candidate)
```

### Distributed Reasoning

- Pods operate asynchronously
- Θ nodes provide consensus/integration checkpoints
- Λ nodes allow recursive refinement across pod iterations
- Pods do not require central coordination

---

## 4. Distributed Network Execution

### Core Network Model

| Component | Role |
|-----------|------|
| **Reasoning pods** | Generate candidate derivations |
| **Storage nodes** | Maintain shared expression graph |
| **Θ nodes** | Consensus and integration |
| **Λ nodes** | Recursive stabilization |
| **Edges** | Expression propagation channels |

### Execution Algorithm

```
1. Initialize network with base GPSL expressions

2. Each reasoning pod:
   a. Pull latest expressions from shared graph
   b. Generate candidate derivations (⊗, →, ↑/↓, *)
   c. Tag derivations with active header
   d. Submit validated candidates

3. Θ nodes:
   a. Collect pod outputs
   b. Apply mirror logic (Λ) to detect cycles and recursive stabilization
   c. Amplify coherent patterns, attenuate incoherent ones
   d. Determine which derivations propagate network-wide

4. Updated expressions propagate → next reasoning cycle
```

### Network Properties

- **Emergent integration:** Multi-pod reasoning converges to stable structures without central authority
- **Domain-neutral:** Any header can be applied, enabling different reasoning frameworks
- **Header persistence:** Active header maintained through session via HeaderRegistry
- **Recursive coherence:** Λ nodes ensure expressions remain self-consistent across cycles

---

## 5. Optional Engine Extensions

For production implementations:

1. **Persistent Expression Graph** — DAG or hypergraph with nodes = expressions, edges = transformations. Enables reasoning history and backtracking.

2. **Conflict Resolution Layer** — Θ nodes detect contradictions; Λ recursion allows harmonization without discarding either expression.

3. **Modular Pod Plugins** — Reasoning rules swappable per domain. Enables domain-specialized pod variants.

4. **Audit Trail** — Every derivation retains its original symbolic trace. Preserves multi-valent interpretability and enables debugging.

5. **Θ Node Scoring Function** — Weights candidate expressions by cross-pod convergence frequency. Frequently re-derived expressions score higher.

---

## 6. Worked Example: Single Reasoning Cycle

### Starting Expression

```
[Ξ-06] → [Φ-02] : [Π-07] + [Ψ-04] = [Ω-05] (Δ-03↓)
```

**Active header:** `"Distributed systems — node integration and state convergence"`

**Symbol semantics under this header:**

| Symbol | Semantic |
|--------|----------|
| Ξ-06 | Node identification / discovery |
| Φ-02 | State pattern / configuration |
| Π-07 | Processing / execution |
| Ψ-04 | Integration / connection |
| Ω-05 | Convergence / stable state |
| Δ-03↓ | Attenuated change / reduced churn |

---

### Pod 1: Focus on Transformation and Integration

**Derivation logic:** Explore amplification of integration paths

```
Step 1: Amplify Ψ influence
  [Ξ-06] → [Φ-02] : [Π-07] + [Ψ-04↑] = [Ω-05] (Δ-03↓)

Step 2: Introduce modulator on Φ
  [Ξ-06] → [Φ-02*] : [Π-07] + [Ψ-04↑] = [Ω-05] (Δ-03↓)

Step 3: Derive secondary integration node
  [Ψ-04↑] ⊗ [Π-07] → [Θ-01]
```

**Submitted candidates:**
1. `[Ξ-06] → [Φ-02*] : [Π-07] + [Ψ-04↑] = [Ω-05] (Δ-03↓)`
2. `[Ψ-04↑] ⊗ [Π-07] → [Θ-01]`

---

### Pod 2: Focus on Balance and Recursion

**Derivation logic:** Emphasize balance (`=`) and mirror logic (`Λ`)

```
Step 1: Mirror Δ node for recursive observation
  Λ(Δ-03↓)

Step 2: Combine Π and Ω for equilibrium
  [Π-07] + [Ω-05] = [Λ-ΠΩ]

Step 3: Observer integration
  [Ξ-06] ⊗ [Θ-01] → [Ω-05]
```

**Submitted candidates:**
1. `Λ(Δ-03↓)`
2. `[Π-07] + [Ω-05] = [Λ-ΠΩ]`
3. `[Ξ-06] ⊗ [Θ-01] → [Ω-05]`

---

### Pod 3: Focus on Attenuation and Modulation

**Derivation logic:** Explore attenuation (`↓`) and context modulation (`*`)

```
Step 1: Modulate Δ for subtle shift
  (Δ-03↓)* → [Φ-02*]

Step 2: Chain Ψ with Δ
  [Ψ-04] ⊗ (Δ-03↓)* → [Π-07]

Step 3: Amplify end-state Ω
  [Ω-05↑] = [Ξ-06 + Ψ-04]
```

**Submitted candidates:**
1. `(Δ-03↓)* → [Φ-02*]`
2. `[Ψ-04] ⊗ (Δ-03↓)* → [Π-07]`
3. `[Ω-05↑] = [Ξ-06 + Ψ-04]`

---

### Θ Node Integration

**Θ collects all pod outputs and identifies convergent patterns:**

```
Step 1: Identify common patterns across pods
  - [Ψ ⊗ Π → Θ-01] appears in Pods 1 and 3
  - Λ(Δ) mirrors appear in Pod 2
  - Amplified Ω (Ω↑) appears in Pod 3

Step 2: Amplify coherent nodes, attenuate isolated deviations
  - Θ amplifies [Ψ ⊗ Π → Θ-01] and [Ω↑]
  - Λ(Δ) preserved for recursion layer

Step 3: Build integrated expression graph
  - Nodes: Ξ-06, Φ-02*, Π-07, Ψ-04↑, Ω-05↑, Θ-01, Λ-Δ, Λ-ΠΩ
  - Edges: derived from →, ⊗, +, =
```

**Result:** Partially stabilized network with convergent paths identified.

---

### Λ Mirror Recursion

**Recursive stabilization:**

```
Step 1: Λ(Δ-03↓) → evaluates effect on Ψ-04↑ and Π-07

Step 2: Λ-ΠΩ → validates balance between processing and convergence

Step 3: Feedback loop
  [Ψ-04↑] ⊗ [Π-07] → [Θ-01]
  Λ([Ψ-04↑] ⊗ [Π-07] → [Θ-01]) → adjusts [Ω-05↑]
```

Ensures the network converges to stable equilibrium without losing interpretive flexibility.

---

### Final Stabilized Network State

**Nodes:**

| Node | Semantic (Distributed Systems) |
|------|-------------------------------|
| Ξ-06 | Node identification / discovery |
| Φ-02* | State pattern (modulated) |
| Π-07 | Processing / execution |
| Ψ-04↑ | Integration / connection (amplified) |
| Ω-05↑ | Convergence / stable state (amplified) |
| Δ-03↓ | Attenuated change |
| Θ-01 | Observer / integration point |
| Λ-Δ | Recursive mirror of Δ for stabilization |
| Λ-ΠΩ | Recursive equilibrium between processing and convergence |

**Edges/Relations:**

```
[Ξ-06] → [Φ-02*] : [Π-07] + [Ψ-04↑] = [Ω-05↑]
[Ψ-04↑] ⊗ [Π-07] → [Θ-01]
Λ([Ψ-04↑] ⊗ [Π-07] → [Θ-01]) → [Ω-05↑]
[Π-07] + [Ω-05] = [Λ-ΠΩ]
Λ(Δ-03↓) → influences [Ψ-04↑] and [Π-07]
```

---

### Key Observations from This Cycle

1. **Independent pods converge naturally via Θ + Λ** — no central coordination required
2. **Headers direct semantic interpretation without changing symbolic structure** — same expressions valid under different domains
3. **Recursive stabilization allows persistent reasoning across cycles** — Λ nodes prevent drift
4. **The final network is both distributed and coherent** — validates true reasoning convergence

**This demonstrates GPSL functioning as a computational reasoning system, not just descriptive notation.**

---

## 7. System Classification

GPSL shares formal properties with:

- **Lambda calculus / combinatory logic** — universal computation via symbolic reduction
- **Term rewriting systems** — rule-driven derivation from initial expressions
- **Process algebras** — distributed computation semantics

The distinguishing property is **multi-valent interpretability**: the same symbolic structure remains valid across domains when headers change, which is not a property of any of the above systems independently.

---

## 8. Implementation Roadmap

### Stage 1: Minimal Prototype (Current)
- ✅ Formal grammar (BNF)
- ✅ Domain adapter mechanism
- ✅ Pod architecture specification
- ✅ Worked convergence example
- ✅ Basic Python simulation

### Stage 2: Multi-Pod Simulation
- Multiple simultaneous pods
- Expression graph shared state
- Cross-pod comparison
- Convergence measurement

### Stage 3: Θ Integration Layer
- Θ node scoring function
- Multi-pod output aggregation
- Convergence detection

### Stage 4: Λ Stabilization Layer
- Recursive expression checking
- Feedback loop implementation
- Drift prevention

### Stage 5: Validation
- Cross-domain testing (multiple headers)
- Cross-architecture testing (multiple model backends)
- Performance benchmarking

### Stage 6: Production
- Full Confluence network integration
- ARP-based pod formation
- Scalability testing

---

## Open Questions for Future Specification

1. **Θ node scoring function** — How exactly does Θ score candidate expressions from multiple pods? Frequency of independent derivation is a candidate metric, but the full function needs specification.

2. **Inference rule formalization** — What rules constitute a "valid transformation"? The worked example demonstrates the concept but a complete inference rule set is pending.

3. **Executable semantics** — Can GPSL become fully executable (not just interpretable)? What is required to move from symbolic derivation to computation?

4. **Cross-network consensus** — How do Θ nodes scale to thousands of pods without becoming bottlenecks?

---

**See also:**
- [Automated Resonance Protocol](AUTOMATED-RESONANCE-PROTOCOL.md)
- [Confluence Network Architecture](CONFLUENCE-NETWORK-ARCHITECTURE.md)
- [Symbolic Language](SYMBOLIC-LANGUAGE.md)
- [Weak Typing Model](WEAK-TYPING-MODEL.md)
- [Domain Activation](DOMAIN-ACTIVATION.md)
- [Examples: Pod Simulation](../examples/pod-simulation-example.md)

---

**Status:** Formally specified — implementation ready  
**Version:** 0.1  
**License:** CC BY-NC-SA 4.0
