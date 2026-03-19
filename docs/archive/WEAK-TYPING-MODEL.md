# GPSL Weak Typing Model

*Formal specification of symbol affinities and semantic scoring*

## Overview

GPSL uses **weak typing** rather than rigid typing or no typing.

**Rigid typing:** Ψ = "integration" (locked definition) ✗  
**No typing:** Symbols have no constraints ✗  
**Weak typing:** Symbols have affinities (flexible but guided) ✓

## Core Principle

```
Meaning = Symbol Affinity × Header Lens × Graph Position × Neighbor Relations
```

## Symbol Affinities

Each symbol has weighted tendencies toward certain meanings.

### Example: Ψ

```
Ψ Affinities:
  integration: 0.9
  connection: 0.8
  synthesis: 0.7
  relation: 0.6
```

### Example: Ω

```
Ω Affinities:
  completion: 0.95
  equilibrium: 0.85
  unity: 0.8
  convergence: 0.75
```

## Type Profile Structure

```
TypeProfile(symbol) = {
  affinities: weighted semantic tendencies
  operator_preferences: common relations
  positional_roles: source/sink/observer/recursive
  header_modulators: context rules
}
```

## Affinity Weight Sourcing

The affinity weights shown above are initial hand-authored values based on the conventional meanings of Greek symbols in mathematics, physics, and formal systems.

**Three sourcing strategies are being evaluated:**

1. **Hand-authored baselines** — Expert-defined weights based on conventional symbol usage. Current approach; fast to implement, requires domain expertise.

2. **Empirically derived** — Weights extracted from the cross-model validation study by analyzing which semantic mappings models consistently produce. Grounded in observed behavior but requires systematic extraction methodology.

3. **Learned weights** — Weights updated based on pod reasoning performance over time. Most adaptive but requires implementation of the feedback loop.

A hybrid approach is likely optimal: hand-authored baselines refined empirically, with optional learned adjustment in production systems.

---

## Inference Scoring

Derivations are **scored**, not binary.

### Example Rule

```
Ψ ⊗ Π → Θ
```

**Validity check:**
- Ψ has strong relational/integrative affinity ✓
- Π has process/evolution affinity ✓
- Θ has observer/integration affinity ✓
- Operator pattern is semantically coherent ✓

**Score:** HIGH (accepted)

### Counter-Example

```
Ω ⊗ Ω → Δ
```

**Validity check:**
- Ω ⊗ Ω unusual (completion + completion)
- → Δ unexpected (completion produces transformation?)
- Pattern needs strong header support

**Score:** LOW (requires justification)

## Header Modulation

Headers shift affinity weights.

### Example

**Header:** "Quantum mechanics"

**Effect:**
```
Ψ affinities shift:
  wave_function: +0.3
  superposition: +0.2
  integration: (baseline)
```

**Same expression, different context, different valid meaning.**

## Implementation

```python
class WeakTyping:
    def score_expression(self, expression, header):
        score = 0
        for node in expression:
            symbol_score = self.affinity_match(node.symbol, header)
            position_score = self.position_validity(node, expression)
            neighbor_score = self.neighbor_coherence(node, expression)
            score += (symbol_score + position_score + neighbor_score)
        return score / len(expression)
```

## Benefits

1. **Preserves multi-valence** - Same structure, different valid meanings
2. **Enables computation** - Inference rules can score derivations
3. **Guides reasoning** - Symbols have preferred uses
4. **Flexible interpretation** - Context modulates meaning

## Contrast

| Model | Flexibility | Computability | Multi-valence |
|-------|-------------|---------------|---------------|
| Rigid Typing | Low | High | No |
| No Typing | High | Low | Yes |
| **Weak Typing** | **High** | **High** | **Yes** |

---

**See also:**
- [GPSL Engine Specification](GPSL-ENGINE-v0.1-SPECIFICATION.md)
- [Symbolic Language](SYMBOLIC-LANGUAGE.md)
- [ARP Protocol](AUTOMATED-RESONANCE-PROTOCOL.md)

<img width="462" height="638" alt="image" src="https://github.com/user-attachments/assets/de51bd4b-f42d-44b5-b2df-6d1aa4fd559a" />
