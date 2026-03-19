# GPSL v1.8.0 — Specification

## 1. Overview

GPSL (Generalized Process Symbolic Language) is a minimal symbolic system for representing
processes, states, and their interactions under constraint.

The system is intentionally limited. Expressivity is achieved through composition,
recursion, and structured context rather than feature expansion.

## 2. Core Elements

### 2.1 Node Types

#### Process node
`[A]`

Represents transformation, action, or operation.

#### State node
`{A}`

Represents condition, field, result, or stabilized state.

### 2.2 Core operators

#### Transition
`[A] → [B]`

Process-to-process transformation.

#### Assignment / resolution
`X = Y`

Resolves an expression into an output state or process.

#### Entanglement / composition
`X ⊗ Y`

Combines two symbolic elements into a coupled structure.

#### Bridge
`X :: Y`

Structural linkage or phase boundary.

#### Loop / feedback
`X ↺ Y`

Recursive or feedback relation.

#### Parallel
`X ; Y`

Parallel or co-present expressions.

### 2.3 Modifiers

#### Amplification
`↑`

#### Dampening
`↓`

Modifiers alter the interpretation of a result but do not change the underlying node type.

## 3. Canonical Expression Pattern

A common GPSL form is:

`[A] → [B] : {C} ⊗ {D} = [E] (Δ↓)`

This is read as:

- a process `[A]` transforms into `[B]`
- under the contextual relation `:`
- with state coupling `{C} ⊗ {D}`
- resolving to `[E]`
- with a dampening or amplification modifier

## 4. Grammar Principles

### Rule 1 — Processes initiate transitions
Only process expressions may initiate `→`.

Valid:
- `[A] → [B]`

Invalid:
- `{A} → [B]`
- `{A} → {B}`

### Rule 2 — States are non-initiating
State nodes do not directly emit transitions.

### Rule 3 — Assignment accepts expressions
The left-hand side of `=` may be a process or a valid compound expression.

Valid:
- `[A] = {B}`
- `[A] → [B] = {C}`
- `{A} ⊗ {B} = [C]`

This explicitly resolves the compound-expression ambiguity identified in earlier versions.

### Rule 4 — Symbolic purity
GPSL is symbolic, not numeric. Numeric assignment, arithmetic, and variable mutation are
outside the core grammar.

Disallowed:
- `A = 0.7`
- `A + B`
- `A × 1.2`

### Rule 5 — Non-nested core syntax
GPSL v1.8.0 uses flat expressions. Nested formal subexpressions are not part of the core grammar.

Disallowed:
- `{A : [B] → {C}}`

### Rule 6 — Symbol identity is stable
Symbols do not mutate during evaluation. Grammar evolution may introduce new operators over time,
but an expression does not rewrite its own symbol identities during execution.

## 5. Forbidden Constructs

The following are excluded from v1.8.0 core syntax:

- arithmetic operators (`+`, `-`, `×`, `/`)
- explicit temporal markers (`t=`, `at t`)
- state-to-state transitions
- numeric variable assignment
- unrestricted nesting
- unrestricted symbol generation

These introduce ambiguity, drift, or loss of closure.

## 6. Emergent Operator Status

The following operator has emerged in experiments but is not yet part of the fully settled core grammar.

### Meta-transition
`X ⟶ Y`

Observed use: progression between cipher stages or between representational levels.

Status: documented as an emergent operator and candidate for later formal inclusion.

## 7. Design Principle

GPSL works through:

- minimal operator count
- stable symbolic identity
- recursive closure
- constrained composition

Its power comes from what it excludes as much as from what it contains.

## 8. Version Notes

v1.8.0 includes:

- clarified assignment behavior for compound expressions
- explicit exclusion of arithmetic and temporal syntax
- documentation of `⟶` as emergent rather than fully canonical

## 9. Status

This is the canonical specification for the current release.
Future change should occur through repeated empirical emergence and cross-model validation,
not ad hoc feature addition.
