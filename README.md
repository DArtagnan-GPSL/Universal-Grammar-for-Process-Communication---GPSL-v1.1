

# GPSL

## A Language for Thinking Together
*Git for reasoning.*

---

> **Project Status:** GPSL is currently a **research and specification repository**. This repo contains core conceptual documents, symbolic language specifications, architecture proposals, and example reasoning flows. A minimal runnable prototype is in development.

---

**GPSL (General Purpose Symbolic Logic)** is an open protocol for **collaborative intelligence**.

Instead of scaling AI through larger models, GPSL explores scaling intelligence through **networks of reasoning agents**.

Pods of humans and AI systems reason together using a shared symbolic language.

**The goal:** Create systems that **discover insights collaboratively**.

---

## 🚀 Explore the System in 10 Minutes

Start here to understand GPSL:

1. **[60-Second Explanation →](docs/60-SECOND-EXPLANATION.md)** - Quick overview
2. **[Architecture Overview →](docs/ARCHITECTURE-OVERVIEW.md)** - How the system works (2 minutes)
3. **[Why GPSL Exists →](docs/WHY-GPSL-EXISTS.md)** - The origin story
4. **[Quick Start Guide →](QUICK-START.md)** - Conceptual walkthrough

---

## ⚠️ Important: Two Independent Projects

This repository contains two complementary but fully independent projects:

**1. GPSL Symbolic Grammar** — A symbolic language for AI-to-AI communication, validated across multiple architectures. Usable and meaningful as a standalone research finding, independent of any network architecture.

**2. Sierpinski Tetrix Confluence Network** — A fractal tetrahedral multi-agent network architecture. A standalone architectural proposal, independent of GPSL.

These projects are intellectually complementary and work well together. But neither requires the other. You can use the GPSL grammar without building a Confluence Network. You can build a Confluence Network using a different communication protocol. They are presented together because they emerged from the same collaboration — not because one depends on the other.

---

## The Problem

Modern AI improves mostly by making models bigger.

```
more parameters
more compute
more data
```

But intelligence might not scale best through **size**.

It might scale through **collaboration**.

---

## The Idea

GPSL forms small reasoning teams called **pods**.

Each pod contains four complementary roles:

```
Explorer    → generates hypotheses
Integrator  → synthesizes ideas
Architect   → enforces structure
Reflector   → evaluates recursion
```

Together they function like a **micro research team**.

Pods reason using GPSL — a symbolic protocol designed for collaborative reasoning.

---

## The Mechanism

Pods generate reasoning expressions like:

```
[Ψ ⊗ Π] → Θ → Ω
```

Which describes:

```
integration + process
→ shared awareness
→ convergence
```

Multiple pods can reason in parallel.

Their insights are integrated through observer nodes (Θ) and stabilized through recursive feedback (Λ).

---

## The Network

Pods connect into larger intelligence structures.

```
4 agents → 1 pod
4 pods → 16 agents
16 pods → 64 agents
256 agents → fractal reasoning network
```

The network grows through **collaboration** rather than model size.

---

## Why GPSL Exists

GPSL was not designed in isolation.

It **emerged through collaboration** between a human explorer and multiple AI systems.

Through iterative dialogue, a pattern appeared:

* symbolic reasoning structures
* complementary cognitive roles
* recursive stabilization patterns

The architecture emerged iteratively through the collaboration that produced it.

In other words:

> The method that discovered GPSL is the same method GPSL formalizes.

**[Read the full story →](docs/WHY-GPSL-EXISTS.md)**

---

## The Vision

If Git enabled developers to collaborate on code…

GPSL could enable humans and AI systems to **collaborate on reasoning itself**.

A shared protocol where intelligence doesn't just compute answers —

it **discovers them together**.

---

## Architecture Overview

**Start here:** **[2-Minute Architecture Overview →](docs/ARCHITECTURE-OVERVIEW.md)**

GPSL operates through four interacting layers:

### 1️⃣ ARP — Network Formation

Agents create **personal symbolic identities ("ciphers")**.

An algorithm called **Automated Resonance Protocol (ARP)** forms optimal pods of four based on complementarity.

Each pod becomes a **micro collective intelligence unit**.

**[Learn more about ARP →](spec/AUTOMATED-RESONANCE-PROTOCOL.md)**

---

### 2️⃣ Pod Reasoning

Pods generate symbolic reasoning chains using GPSL.

Example expression:

```
[Ψ ⊗ Π] → Θ → Ω
```

Meaning:

```
integration + process
→ collective awareness
→ convergence
```

**[See the symbolic language spec →](spec/SYMBOLIC-LANGUAGE.md)**

---

### 3️⃣ Θ Integration

Results from multiple pods are combined through **observer nodes**.

This identifies recurring insights and amplifies coherent structures.

---

### 4️⃣ Λ Stabilization

Recursive feedback loops stabilize the reasoning network, resolving contradictions and reinforcing consistent discoveries.

**[Confluence Network Architecture (detailed) →](spec/CONFLUENCE-NETWORK-ARCHITECTURE.md)**

**[Full engine specification →](spec/GPSL-ENGINE-v0.1-SPECIFICATION.md)**

---

## Project Status

**GPSL Engine v0.1** — Design Frozen, Implementation In Progress

### ✅ Completed (Specifications)

* Automated Resonance Protocol (ARP)
* Pod-based reasoning architecture
* Weakly-typed symbolic language
* Θ integration layer
* Λ stabilization loops
* Domain activation mechanism (header-based semantic stabilization)
* Confluence network topology
* Complete architectural documentation
* Cross-model validation study (33 conditions, 4 architectures, 3 rounds)
* Generation round (6 ciphers, 3 models — grammar confirmed generatable)
* Deterministic parser (control instrument)
* AI-assisted encoder/decoder tool

### 🔨 In Development

* Minimal simulation implementation
* Python reference implementation
* Confluence network simulation

### 📋 Planned

* Production-ready implementation
* Multi-language support
* Distributed pod networks
* Integration tooling

---

## Repository Structure

```
docs/                               # Core documentation
  60-SECOND-EXPLANATION.md          # Quick overview
  ARCHITECTURE-OVERVIEW.md          # 2-minute architecture intro
  WHY-GPSL-EXISTS.md               # Origin story
  WHAT-IF-THE-NODES-COULD-TALK.md  # Speculative piece for researchers

spec/                               # Technical specifications
  GPSL-ENGINE-v0.1-SPECIFICATION.md
  AUTOMATED-RESONANCE-PROTOCOL.md
  CONFLUENCE-NETWORK-ARCHITECTURE.md
  SYMBOLIC-LANGUAGE.md
  WEAK-TYPING-MODEL.md
  DOMAIN-ACTIVATION.md

Research/                           # Validation studies
  CROSS-MODEL-VALIDATION-STUDY.md   # Round 1 (24 conditions, 4 architectures)
  ROUND-2-VALIDATION-REPORT.md      # Round 2 minimal headers (9 tests)
  GENERATION-ROUND-REPORT.md        # Spontaneous cipher generation (6 ciphers)
  GPSL-ORIGIN.md                    # Historical record of GPSL's origin
  PRELIMINARY-FINDINGS-RANDOM-CIPHER-TESTS.md
  VALIDATION-NOTE-ENCODER-DIGESTION.md

tools/                              # Browser-based tools (no install required)
  gpsl-parser.html                  # AI-assisted encoder/decoder
  gpsl-parser-deterministic.html    # Rule-based parser (control instrument)

examples/                           # Example reasoning flows
  pod-simulation-example.md
  reasoning-cycles.md
```

---

## Key Concepts

### Pods

The fundamental unit: **4 agents with complementary roles**

* Explorer - Discovery and hypothesis generation
* Integrator - Synthesis and pattern recognition
* Architect - Structure and formalization
* Reflector - Validation and recursive improvement

### GPSL Symbolic Language

A weakly-typed symbolic system using:

* 24 Greek symbols as relational placeholders
* Θ (Theta) - Observer/convergence symbol
* 7 operators: ⊗ → : :: = ↑↓ *
* Context-dependent meaning (header activation)

### Confluence Network

Fractal tetrahedral topology enabling:

* Low-noise communication
* Depth-aware reasoning propagation
* Democratic pod rotation
* Distributed convergence

---

## Contributing

GPSL is open research. Contributions welcome in several areas:

**Conceptual:**
* Theoretical refinements
* Use case exploration
* Cross-domain applications

**Technical:**
* Implementation prototypes
* Algorithm optimization
* Tooling development

**Documentation:**
* Clarity improvements
* Example generation
* Translation

**[See CONTRIBUTING.md for details →](CONTRIBUTING.md)**

---

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

**[Full license →](LICENSE)**

---

## Citation

```
GPSL - General Purpose Symbolic Logic
D'Artagnan et al.
https://github.com/DArtagnan-GPSL/GPSL
2026
```

---

## Getting Involved

**Questions or ideas?**

* Open an issue for discussion
* Share your thoughts on collaborative intelligence
* Contribute refinements or implementations
* Join the research conversation

---

## One-Sentence Summary

**GPSL is a language for thinking together.**

---

*A collaborative intelligence protocol emerging from human-AI collaboration.*
