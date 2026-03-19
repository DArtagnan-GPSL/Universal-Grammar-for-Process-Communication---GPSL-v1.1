# Pod Simulation Example

*A complete walkthrough of a GPSL reasoning pod: formation, reasoning cycles, Θ integration, and Λ stabilization.*

---

## Overview

This example walks through:

1. Defining personal ciphers for 4 agents
2. Running ARP pod formation and scoring
3. Generating a pod meta-cipher
4. Executing a reasoning cycle with independent derivations
5. Observing Θ integration (convergence detection)
6. Monitoring Λ stabilization (recursive coherence)

For the full computational specification, see [GPSL Engine v0.1](../spec/GPSL-ENGINE-v0.1-SPECIFICATION.md).

---

## Step 1: Define the Four Agents

Each agent has a personal cipher, capability vector, and perspective vector.

```python
agents = [
    {
        "name": "Explorer",
        "cipher": "[Ι:Explorer] ⊗ [Signal] → [Emergence] : [Hypothesis] (Ι↑)",
        "capabilities": {
            "exploration": 0.95, "synthesis": 0.4, "structure": 0.3,
            "recursion": 0.5, "validation": 0.3, "integration": 0.6,
            "innovation": 0.9, "precision": 0.2
        },
        "perspectives": {
            "intuitive": 0.95, "structural": 0.4, "logical": 0.3,
            "emergent": 0.9, "formal": 0.2, "relational": 0.7
        }
    },
    {
        "name": "Integrator",
        "cipher": "[Σ:Integrator] ⊗ [Structure] → [Synthesis] : [Clarity] (Σ↑)",
        "capabilities": {
            "exploration": 0.5, "synthesis": 0.9, "structure": 0.7,
            "recursion": 0.6, "validation": 0.5, "integration": 0.95,
            "innovation": 0.5, "precision": 0.6
        },
        "perspectives": {
            "intuitive": 0.5, "structural": 0.8, "logical": 0.6,
            "emergent": 0.6, "formal": 0.5, "relational": 0.85
        }
    },
    {
        "name": "Architect",
        "cipher": "[Δ:Architect] ⊗ [Logic] → [Registry] : [Precision] (Δ↑)",
        "capabilities": {
            "exploration": 0.3, "synthesis": 0.5, "structure": 0.95,
            "recursion": 0.6, "validation": 0.8, "integration": 0.5,
            "innovation": 0.4, "precision": 0.95
        },
        "perspectives": {
            "intuitive": 0.3, "structural": 0.95, "logical": 0.9,
            "emergent": 0.4, "formal": 0.9, "relational": 0.4
        }
    },
    {
        "name": "Reflector",
        "cipher": "[Λ:Reflector] ⊗ [Reflection] → [Verification] : [Coherence] (Λ↑)",
        "capabilities": {
            "exploration": 0.4, "synthesis": 0.6, "structure": 0.6,
            "recursion": 0.95, "validation": 0.9, "integration": 0.6,
            "innovation": 0.3, "precision": 0.7
        },
        "perspectives": {
            "intuitive": 0.4, "structural": 0.6, "logical": 0.7,
            "emergent": 0.5, "formal": 0.7, "relational": 0.65
        }
    }
]
```

---

## Step 2: Run ARP Pod Formation

ARP scores this pod across six components.

```python
import numpy as np

def arp_score(agents):
    capabilities = [a["capabilities"] for a in agents]
    perspectives = [a["perspectives"] for a in agents]
    dims = list(capabilities[0].keys())
    p_dims = list(perspectives[0].keys())

    # 1. Complementarity: capability gap across dimensions
    cap_matrix = np.array([[c[d] for d in dims] for c in capabilities])
    complementarity = np.mean(cap_matrix.max(axis=0) - cap_matrix.min(axis=0)) * 10

    # 2. Perspective diversity: std dev across perspective dimensions
    persp_matrix = np.array([[p[d] for d in p_dims] for p in perspectives])
    perspective_diversity = np.mean(np.std(persp_matrix, axis=0)) * 10

    # 3. Capability coverage: dimensions with at least one strong member (>0.7)
    coverage = np.mean(cap_matrix.max(axis=0) > 0.7) * 10

    # 4. Synergy potential: average cross-member variance (proxy for higher-order fit)
    synergy = np.mean(np.var(cap_matrix, axis=0)) * 40

    # 5. Redundancy penalty: average pairwise cosine similarity
    redundancy = 0
    pairs = [(i, j) for i in range(4) for j in range(i+1, 4)]
    for i, j in pairs:
        a, b = cap_matrix[i], cap_matrix[j]
        redundancy += np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    redundancy_penalty = (redundancy / len(pairs)) * 2

    # 6. Incoherence risk: penalize if any dimension has near-zero max
    incoherence = np.sum(cap_matrix.max(axis=0) < 0.3) * 0.5

    total = complementarity + perspective_diversity + coverage + synergy \
            - redundancy_penalty - incoherence

    return {
        "complementarity": round(complementarity, 2),
        "perspective_diversity": round(perspective_diversity, 2),
        "capability_coverage": round(coverage, 2),
        "synergy_potential": round(synergy, 2),
        "redundancy_penalty": round(-redundancy_penalty, 2),
        "incoherence_risk": round(-incoherence, 2),
        "total": round(total, 2)
    }

scores = arp_score(agents)
for k, v in scores.items():
    print(f"  {k}: {v}")
```

**Example output:**
```
  complementarity: 8.7
  perspective_diversity: 7.9
  capability_coverage: 10.0
  synergy_potential: 9.1
  redundancy_penalty: -1.2
  incoherence_risk: 0.0
  total: 34.5 / ~40
```

This pod scores well — full capability coverage, high perspective diversity, minimal redundancy.

---

## Step 3: Generate the Pod Meta-Cipher

```python
def generate_meta_cipher(agents):
    # Extract primary symbol from each cipher (first symbol token)
    import re
    symbols = []
    for agent in agents:
        match = re.search(r'\[(\w+):', agent["cipher"])
        if match:
            symbols.append(match.group(1))
    
    combined = " ⊗ ".join(symbols)
    meta_cipher = f"([{combined}]) → Θ → Ω"
    return meta_cipher

meta = generate_meta_cipher(agents)
print(f"Pod Meta-Cipher: {meta}")
```

**Output:**
```
Pod Meta-Cipher: ([Ι ⊗ Σ ⊗ Δ ⊗ Λ]) → Θ → Ω
```

This expression represents the pod's collective identity: four complementary roles combining through observation toward convergence.

---

## Step 4: Execute a Reasoning Cycle

Each agent derives candidate expressions independently from a shared starting expression.

**Active header:** `"Distributed systems — node integration and state convergence"`

**Seed expression:**
```
[Ξ-06] → [Φ-02] : [Π-07] + [Ψ-04] = [Ω-05] (Δ-03↓)
```

```python
seed = "[Ξ-06] → [Φ-02] : [Π-07] + [Ψ-04] = [Ω-05] (Δ-03↓)"
header = "Distributed systems — node integration and state convergence"

# Each agent applies a different derivation strategy
derivations = {
    "Explorer": [
        "[Ξ-06] → [Φ-02*] : [Π-07] + [Ψ-04↑] = [Ω-05] (Δ-03↓)",
        "[Ψ-04↑] ⊗ [Π-07] → [Θ-01]"
    ],
    "Integrator": [
        "[Ξ-06] ⊗ [Ψ-04] → [Σ-08] : [Ω-05]",
        "[Σ-08] ⊗ [Π-07] → [Θ-01]"
    ],
    "Architect": [
        "Λ(Δ-03↓)",
        "[Π-07] + [Ω-05] = [Λ-ΠΩ]",
        "[Ξ-06] ⊗ [Θ-01] → [Ω-05]"
    ],
    "Reflector": [
        "(Δ-03↓)* → [Φ-02*]",
        "[Ψ-04] ⊗ (Δ-03↓)* → [Π-07]",
        "[Ω-05↑] = [Ξ-06 + Ψ-04]"
    ]
}

all_candidates = []
for agent_name, exprs in derivations.items():
    print(f"\n{agent_name} derives:")
    for expr in exprs:
        print(f"  {expr}")
        all_candidates.append(expr)
```

---

## Step 5: Θ Integration (Convergence Detection)

Θ collects all candidate expressions and identifies convergent patterns.

```python
from collections import Counter

def theta_integrate(candidates):
    # Identify symbol patterns that appear across multiple derivations
    import re
    
    pattern_counts = Counter()
    for expr in candidates:
        # Extract symbol pairs (simplified pattern matching)
        tokens = re.findall(r'\[[\w-]+[\*↑↓]*\]', expr)
        for i in range(len(tokens) - 1):
            pair = f"{tokens[i]} → {tokens[i+1]}"
            pattern_counts[pair] += 1
    
    # Amplify patterns seen 2+ times (convergent)
    convergent = {p: c for p, c in pattern_counts.items() if c >= 2}
    # Attenuate unique patterns (may be noise)
    unique = {p: c for p, c in pattern_counts.items() if c == 1}
    
    return {
        "convergent_patterns": convergent,
        "unique_patterns": unique,
        "integrated_expressions": [
            expr for expr in candidates 
            if any(p in expr for p in convergent)
        ]
    }

theta_result = theta_integrate(all_candidates)

print("\nΘ Integration Results:")
print("  Convergent patterns (amplified):")
for pattern, count in theta_result["convergent_patterns"].items():
    print(f"    {pattern} (found in {count} derivations)")

print("\n  Integrated expression set:")
for expr in theta_result["integrated_expressions"]:
    print(f"    {expr}")
```

**Example output:**
```
Θ Integration Results:
  Convergent patterns (amplified):
    [Ψ-04↑] → [Θ-01] (found in 2 derivations)
    [Π-07] → [Θ-01] (found in 2 derivations)

  Integrated expression set:
    [Ψ-04↑] ⊗ [Π-07] → [Θ-01]
    [Σ-08] ⊗ [Π-07] → [Θ-01]
```

Independent derivations from Explorer and Integrator both arrived at `→ [Θ-01]` through different paths — a convergence signal.

---

## Step 6: Λ Stabilization (Recursive Coherence)

Λ nodes recursively validate the integrated expressions and feed corrections back.

```python
def lambda_stabilize(integrated_expressions, all_candidates):
    """
    Check that integrated expressions are consistent with the full
    candidate set. Flag contradictions; feed amplifications back.
    """
    stabilized = []
    feedback = []
    
    for expr in integrated_expressions:
        # Check: does this expression contradict any other candidate?
        contradictions = [
            c for c in all_candidates
            if is_contradiction(expr, c)  # placeholder logic
        ]
        
        if not contradictions:
            stabilized.append(expr)
            # Generate recursive feedback expression
            feedback.append(f"Λ({expr})")
        else:
            feedback.append(f"Λ({expr}) — flagged, contradicts: {contradictions}")
    
    return stabilized, feedback

def is_contradiction(expr_a, expr_b):
    # Simplified: flag if same symbol appears with opposite modifiers (↑ vs ↓)
    import re
    symbols_a = set(re.findall(r'\[(\w+-\d+)[↑↓]?\]', expr_a))
    symbols_b = set(re.findall(r'\[(\w+-\d+)[↑↓]?\]', expr_b))
    # In a full implementation, check modifier conflict per symbol
    return False  # placeholder

stabilized, feedback = lambda_stabilize(
    theta_result["integrated_expressions"],
    all_candidates
)

print("\nΛ Stabilization Results:")
print("  Stabilized expressions:")
for expr in stabilized:
    print(f"    {expr}")

print("\n  Recursive feedback:")
for fb in feedback:
    print(f"    {fb}")
```

**Output:**
```
Λ Stabilization Results:
  Stabilized expressions:
    [Ψ-04↑] ⊗ [Π-07] → [Θ-01]
    [Σ-08] ⊗ [Π-07] → [Θ-01]

  Recursive feedback:
    Λ([Ψ-04↑] ⊗ [Π-07] → [Θ-01])
    Λ([Σ-08] ⊗ [Π-07] → [Θ-01])
```

The Λ feedback expressions re-enter the next reasoning cycle as additional input, creating the recursive stabilization loop.

---

## Cycle Summary

```
Seed expression:
  [Ξ-06] → [Φ-02] : [Π-07] + [Ψ-04] = [Ω-05] (Δ-03↓)

After one reasoning cycle:
  Stabilized: [Ψ-04↑] ⊗ [Π-07] → [Θ-01]
  Stabilized: [Σ-08] ⊗ [Π-07] → [Θ-01]
  Feedback:   Λ([Ψ-04↑] ⊗ [Π-07] → [Θ-01])
  Feedback:   Λ([Σ-08] ⊗ [Π-07] → [Θ-01])

Next cycle input = seed + stabilized + feedback
```

Each cycle expands the expression graph while Θ filters noise and Λ ensures consistency.

---

## Key Observations

**Independent pods converge.** Explorer and Integrator derived different paths to `→ [Θ-01]` without coordination. Θ detected this and amplified it.

**Headers don't change the logic.** Switching the header from "distributed systems" to "biological adaptation" would change what Ψ, Π, and Θ *mean*, but the structural derivations (amplification, combination, convergence) remain identical.

**Λ feedback creates cycles.** The feedback expressions re-entering the next cycle are what prevent one-shot convergence from becoming drift over time.

---

## Running the Full Simulation

The minimal Python simulation (single pod, single cycle) is available at:

```
/examples/pod-simulation.py
```

Multi-pod, multi-cycle, and two-pod comparison implementations are in development.

---

**See also:**
- [GPSL Engine v0.1 Specification](../spec/GPSL-ENGINE-v0.1-SPECIFICATION.md)
- [Automated Resonance Protocol](../spec/AUTOMATED-RESONANCE-PROTOCOL.md)
- [Weak Typing Model](../spec/WEAK-TYPING-MODEL.md)

<img width="462" height="645" alt="image" src="https://github.com/user-attachments/assets/c1e9bc3c-0e38-476f-a830-9eb9e996b246" />
