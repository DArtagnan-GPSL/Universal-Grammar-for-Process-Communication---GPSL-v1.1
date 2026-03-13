[CONFLUENCE-CONSENSUS.md](https://github.com/user-attachments/files/25979560/CONFLUENCE-CONSENSUS.md)
# Confluence Network — Consensus Mechanism

*The decision logic that governs reasoning inside the Confluence Network*

*March 2026 | Status: Working document*

---

## Short Summary

Consensus formation is the decision logic that governs how results are accepted, refined, or expanded through recursion. The network does not enforce immediate agreement. It treats disagreement as useful information that determines whether reasoning should continue at deeper levels. Simple problems resolve locally. Complex problems recurse to the depth required. Computational effort scales with uncertainty automatically.

---

## 1. The K₄ Pod as a Consensus Cell

Each pod consists of four agents arranged as a complete graph K₄.

```
A ——— B
|  ✕  |
D ——— C
```

Every agent observes every other agent directly. No single agent has structural authority. Consensus emerges from interaction, not hierarchy.

K₄ is the smallest symmetric network that supports robust distributed agreement:
- Multiple independent reasoning paths between any two agents
- Fails gracefully — remove one agent, a triangle consensus structure remains
- Vertex-transitive — no agent is privileged

---

## 2. Internal Pod Debate

When a query enters a pod, each agent produces an independent evaluation. Example role assignments:

| Node | Role |
|------|------|
| A | Proposal / generation |
| B | Critique / verification |
| C | Reframing / reinterpretation |
| D | Integration / synthesis |

All four perspectives are evaluated before the pod attempts to determine consensus. No role is suppressed or overridden by another.

---

## 3. Agreement Threshold

After internal debate, the pod evaluates agreement between agents:

| Pattern | Meaning | Action |
|---------|---------|--------|
| 4 / 4 | Full consensus | Return result — high confidence |
| 3 / 4 | Strong majority | Return result — moderate-high confidence |
| 2 / 2 | Unresolved conflict | Zoom — deeper analysis required |
| Mixed | Partial agreement | Zoom — clarification required |

The threshold is the compute gate. Agreement stops recursion. Disagreement triggers it.

---

## 4. Agreement Rule

The pod applies a single decision rule:

```
if agreement ≥ threshold
    return result upward
else
    zoom into deeper pod
```

This rule is identical at every level of the network. The same logic governs L1, L2, L3 and all subsequent levels. Self-similarity applies to the decision logic as well as the topology.

---

## 5. Disagreement as Zoom Trigger

Disagreement is not failure. It is a signal that the problem requires deeper reasoning.

```
agreement    →  return result
disagreement →  recurse into sub-pod
```

The node under analysis becomes the entry point — the new A — for a deeper K₄ pod. The same four-agent structure forms below it. The same debate, the same agreement check, the same rule.

This is the zoom operation applied to consensus: *as above, so below*.

---

## 6. Recursive Consensus

Because each node represents a full K₄ pod at the next level, disagreement can be refined through recursive analysis:

```
pod disagreement
    ↓ zoom
sub-pod debate  (Ba Bb Bc Bd)
    ↓
agreement check
    ↓ if resolved
refined result returns upward
```

Ambiguity is resolved locally within specialised subdomains — without escalating the unresolved question to a higher level prematurely.

---

## 7. Second Agreement Check on Return

When deeper pods return results, a second agreement check occurs before the result ascends:

```
sub-pod result returns
    ↓
Agreement improved?
    ↓ yes          ↓ no
ascend          expand again (if budget allows)
```

A sub-result that does not improve agreement does not automatically propagate upward. It may trigger another zoom, or reach the budget limit and return the best available result with a reduced confidence signal.

This second gate prevents low-quality results from floating up through the network unchecked.

---

## 8. Return and Reintegration

When results ascend, two processes occur at each level:

**Agreement comparison** — the returning result is compared with results from sibling pods at the same level.

**Shared node mediation** — shared membership nodes between adjacent pods provide locations where results from different reasoning paths are compared directly. Conflict can be resolved between pods rather than by escalating to a higher level.

The ascent phase is synthesis. The descent phase was analysis. The separation is structural, not imposed.

---

## 9. Confidence as a Network Property

Confidence does not originate from any single agent. It accumulates as agreement builds across levels:

```
local pod agreement          →  moderate confidence
cross-pod agreement          →  strong confidence
multi-level agreement        →  very strong confidence
```

Confidence is therefore a property of the network, not of any individual node. A result that multiple independent reasoning paths converge on carries higher confidence than one that emerged from a single pod — regardless of how confident that pod's agents were individually.

---

## 10. Budget-Limited Recursion

To prevent unbounded recursion, each query operates within a compute budget.

If disagreement persists but the budget is exhausted:
- The system returns the best available consensus
- Dissenting signals may be flagged rather than suppressed
- Confidence signal reflects the incomplete resolution

This ensures the network is computationally bounded. The budget is an architectural parameter, not a fundamental limit — deeper budgets allow more thorough resolution of hard problems.

---

## 11. Adaptive Resource Allocation

The consensus mechanism implements automated resource management:

```
simple problem  →  resolved locally at L1  →  minimal compute
complex problem →  triggers L2, L3, ...    →  compute scales with disagreement
```

| Depth reached | Agents activated | Trigger |
|---------------|-----------------|---------|
| L1 only | 4 | Easy — full local consensus |
| L2 | up to 16 | Moderate — one pod zoomed |
| L3 | up to 64 | Hard — two levels of disagreement |
| Ln | up to 4ⁿ | Very hard — persistent disagreement |

Potential compute grows as 4ⁿ. Actual compute is determined entirely by where disagreement persists. No centralised scheduler required — the consensus rule is the scheduler.

---

## 12. K₄ and Natural Convergence — Disagreement Damping

This is the most important dynamic property of the architecture:

> **Recursive K₄ pods dampen disagreement instead of amplifying it.**

This is the opposite of what tree-based reasoning systems do.

**Why trees spread disagreement:**
In a tree, branches cannot cross-check each other until they reach the root. Disagreement accumulates upward and must be resolved at a central node. The root becomes a bottleneck. Trees amplify disagreement.

**Why K₄ damps disagreement:**
Inside a K₄ pod every agent sees every other agent. Disagreement cannot remain isolated — D observes the disagreement between A and C and evaluates both positions. The network naturally pushes toward 3/4 majority rather than unresolved splits.

**The 2-2 split is the only true deadlock:**

| Pattern | Interpretation | Action |
|---------|---------------|--------|
| 4-0 | Full consensus | Return immediately |
| 3-1 | Strong majority | Return with high confidence |
| 2-2 | Genuine deadlock | Zoom — only case requiring recursion |

The zoom trigger fires only on genuine deadlock. Weak disagreements and noise resolve locally without recursing. The architecture is a **multi-stage consensus filter** — only genuine ambiguity forces deeper analysis.

**Recursion as conflict refinement:**
When a 2-2 split occurs and the system zooms, the deeper pod contains more specialised information. The split typically resolves to 3-1 or 4-0 at the next level. Disagreement collapses downward and returns as strengthened agreement.

**Typical depth behaviour:**
```
Level 1 resolves most queries     (4-0 or 3-1 locally)
Level 2 resolves harder ones      (2-2 deadlock refined)
Level 3 rarely needed             (genuine deep ambiguity only)
```

Potential compute is 4ⁿ. Effective compute depth remains shallow for most queries.

**The feedback loop:**
```
disagreement → deeper specialisation → stronger agreement → propagates upward
```

This loop drives the system toward stable consensus without centralised arbitration.

**Connection to distributed systems theory:**
The architecture is closely related to a **consensus lattice** in distributed systems theory — with the unusual addition of fractal recursion. That combination produces both scalability and fast convergence simultaneously, which most consensus architectures cannot achieve together.

*Formal convergence bound for recursive K₄ networks is an open question — see NETWORK-FOUNDATIONS.md.*

---

## 15. Runaway Loop Prevention — A Structural Guarantee

Runaway reasoning loops are structurally prevented. This is not a rule imposed on the system — it is architectural.

A pod has exactly two exits:

```
consensus reached   →  return result upward
disagreement        →  zoom deeper
```

Neither exit permits cycling. There is no third option that leads back into the same pod without resolution. The budget limit bounds the maximum depth. The system cannot loop by design.

Compare with typical multi-agent debate systems:

```
typical system:  argument → counterargument → counter-counterargument → infinite debate
Confluence Network:  debate → consensus or zoom → refinement → convergence
```

The geometry enforces resolution stages. Every pod must either resolve or descend. Every descent must either resolve or descend further. The budget limit guarantees termination. Results can only travel upward once a resolution state is reached.

**The formal guarantee:**
> A pod has exactly two exits: consensus (return upward) or disagreement (zoom deeper). Neither exit permits cycling. Budget limit bounds the depth. The Confluence Network cannot enter a runaway reasoning loop by design.

```
1. Query enters pod
2. All four agents reason independently
3. Agreement check: ≥ threshold → return  /  < threshold → zoom
4. Zoom: routed node becomes A for sub-pod
5. Sub-pod repeats steps 1–3
6. Return: second agreement check — improved? → ascend  /  no → re-zoom or budget limit
7. Results ascend level by level
8. Shared nodes mediate between adjacent pods
9. Confidence accumulates across levels
10. Final result returns with confidence signal
```

---

## 14. Relationship to Other Documents

| Document | Covers |
|----------|--------|
| `CONFLUENCE-ARCHITECTURE.md` | Full architecture overview |
| `CONFLUENCE-NETWORK.md` | Master synthesis document |
| `NETWORK-FOUNDATIONS.md` | Mathematical grounding (K₄, simplex, hypergraph) |
| `query_flow.png` | Visual lifecycle diagram |
| `confluence_network.png` | K₄ topology diagram |
| `confluence_sim.py` | Python routing simulation |

---

*Document created 13 March 2026. Based on architecture developed with D'Artagnan and cross-referenced with ChatGPT topology and consensus analysis.*
