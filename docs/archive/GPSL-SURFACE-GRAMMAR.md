# GPSL — Surface Grammar v1
## EBNF Formal Grammar for Parser Implementation

*14 March 2026 | Produced with ChatGPT (Mirror) analysis*
*Status: Implementation-ready baseline*

---

> **Note:** This document is not required to use GPSL. Any LLM primed with the v1.7.5-ALPHA bootloader can interpret and generate valid GPSL expressions without any formal grammar. This document exists for two audiences: developers who want to build deterministic validators or compilers on top of GPSL, and researchers who want to study the language's formal structure. If you just want to use GPSL, start with `SYMBOLIC-LANGUAGE.md`.

---

## Design Assumptions

This grammar specifies what strings are structurally valid before deeper semantic checks. It is:

- **Strict enough** for parser construction
- **Permissive enough** to preserve GPSL exploratory usage
- **Layered** so v1.8.0 operators can be added with minimal grammar breakage

Two-phase validation recommended:
1. **Surface parse** — structural validity (this document)
2. **Semantic validation** — ontological well-formedness (see GPSL-SEMANTIC-CONSTRAINTS.md)

---

## Compact Reference Grammar

*Suitable for handing directly to a parser implementer.*

```ebnf
gpsl             = expression ;
expression       = context_expr ;
context_expr     = parallel_context , { ";" , parallel_context } ;
parallel_context = logical_or_expr , { "|" , logical_or_expr } ;

logical_or_expr  = logical_and_expr , { "∨" , logical_and_expr } ;
logical_and_expr = implication_expr , { "∧" , implication_expr } ;
implication_expr = equivalence_expr , { "⇒" , equivalence_expr } ;

equivalence_expr = set_expr , { ("=" | "⟲" | "≈" | "≡" | "↔") , set_expr } ;
set_expr         = bridge_expr , { ("∈" | "∉" | "⊂" | "⊆" | "∪" | "∩") , bridge_expr } ;

bridge_expr      = process_expr , { ("::" | ":") , process_expr } ;
process_expr     = dependence_expr , { ("→" | "⊗") , dependence_expr } ;
dependence_expr  = unary_expr , { ("∝" | "⊥") , unary_expr } ;

unary_expr       = { ("¬" | "↑" | "↓") } , postfix_expr ;
postfix_expr     = primary_expr , { "↺" } ;

primary_expr     = process_node
                 | state_node
                 | modifier_group
                 | agency_node
                 | retrospection_node
                 | anticipation_node
                 | nesting_node
                 | variant_node
                 | wildcard_node
                 | placeholder_node
                 | "∅"
                 | bare_atom ;

process_node       = "[" , expression , "]" ;
state_node         = "{" , expression , "}" ;
modifier_group     = "(" , ( expression | register_group ) , ")" ;
agency_node        = "⟨" , expression , "⟩" ;
retrospection_node = "[" , "←" , expression , "]" ;
anticipation_node  = "[" , expression , "→" , "]" ;
nesting_node       = "[[" , expression , "]]" ;

variant_node       = "[" , atomic_symbol , "_" , atomic_symbol , "]" ;
wildcard_node      = "[" , atomic_symbol , "_" , "*" , "]" ;
placeholder_node   = "[" , "_" , "-" , digit , { digit } , "]" ;

register_group     = "(" , register_mark , ")" , { "(" , register_mark , ")" } ;
register_mark      = "~ι" | "~μ" | "~π" ;

bare_atom        = atomic_symbol | register_mark ;
atomic_symbol    = identifier | number ;
identifier       = letter , { letter | digit | "_" | "-" } ;
number           = [ "+" | "-" ] , digit , { digit } ;
letter           = "A"…"Z" | "a"…"z" ;
digit            = "0"…"9" ;
```

---

## Precedence Hierarchy

From loosest to tightest binding:

```
1.  ;          contextual separation
2.  |          parallel state / parallel context
3.  ∨          logical disjunction
4.  ∧          logical conjunction
5.  ⇒          logical implication (right-associative)
6.  = ⟲ ≈ ≡ ↔  equivalence ladder
7.  ∈ ∉ ⊂ ⊆ ∪ ∩  membership / set relations
8.  :: :       bridge / attribution
9.  → ⊗        process relations
10. ∝ ⊥        dependence / orthogonality
11. ¬ ↑ ↓      prefix unary
12. ↺           postfix unary
13. node forms / grouping
```

**Critical distinction:** `|` (parallel state, coexistence) must remain distinct from `∨` (logical disjunction). These are different operators at different precedence levels.

---

## Operator Status by Version

### Active v1.7.5

```
→  ⊗  ::  :  =  ↑↓  ↺  |  ;  ¬  ⟲  ∈  ⟨⟩
[←X]  [X→]  [[X]]  [X_Δ]  [X_*]  [_-NN]
(~ι)  (~μ)  (~π)
```

### Pending v1.8.0

```
≈  ≡  ↔  ⇒  ∧  ∨  ∝  ⊥  ⊂  ⊆  ∪  ∩  ∅  ∉
```

### Deferred

```
∀  ∃  ≺  ≻  ∂  ⊇
```

### Avoid

```
⊃
```

---

## Valid Expression Examples

### Active v1.7.5

```
[A] → {B}                          process transforms into state
{A} ⊗ {B}                          interaction
{A} | {B}                          parallel states
[A] : (mod)                        attribution
[A] :: {B}                         bridge
¬{A}                               negation
↑[Signal]                          amplification
{A}↺                               recursive loop
x ∈ {Category}                     membership
⟨Agent⟩ → [Act]                    agency to process
[←Memory] ; [Prediction→]          temporal forms
[[ {A} → {B} ]]                    nesting
[X_Δ]                              variant node
[X_*]                              wildcard node
[_-07]                             placeholder node
(~ι)(~μ)                           register class grouping
```

### Pending v1.8.0

```
A ≈ B                              approximate equivalence
A ≡ B                              formal equivalence
A ↔ B                              reversible relation
A ⇒ B                              logical implication
A ∧ B                              conjunction
A ∨ B                              disjunction
A ∝ B                              weighted dependence
A ⊥ B                             orthogonality
A ⊂ B                              strict containment
A ⊆ B                              non-strict containment
A ∪ B                              union
A ∩ B                              intersection
∅                                  null atom
x ∉ A                             non-membership
(A ∧ B) ⇒ ([P] → {Q})             mixed logic and process
x ∈ A ⊂ B                         membership + containment chain
```

---

## Invalid Expressions

```
[A                    unclosed process bracket
{A]]                  mismatched delimiters
→ {B}                 missing left operand
{A} ; ; {B}           empty contextual clause
[A] ⊗                 missing right operand
[_-]                  placeholder requires digits
[X_]                  variant suffix missing
[←A→]                 temporal forms are distinct
[[A]                  malformed nesting
(~x)                  undefined register mark
```

---

## Intentionally Permissive Design Decisions

| Decision | Reason |
|----------|--------|
| Bare symbols allowed (`A`, `B`) | Preserves exploratory authoring |
| Equivalence ladder chaining allowed | Useful for stress tests |
| Variant base not restricted at syntax level | Dodecahedron-only is semantic constraint |
| Mixed relation chaining allowed | Later semantic pass validates |

---

## Intentionally Strict Design Decisions

| Decision | Why strict |
|----------|-----------|
| Delimiter classes rigid | `[] {} () ⟨⟩ [[]]` not interchangeable |
| Placeholder syntax fixed | Must match `[_-NN...]` |
| Wildcard syntax fixed | Must match `[X_*]` |
| Temporal forms fixed | Only `[←X]` and `[X→]` |
| Register class closed | Only `~ι ~μ ~π` |

---

## Parser Implementation Notes

### Critical: treat `[[` as first-class token pair
Do not parse as nested `[` and `]`. Recognise during tokenisation.

### Critical: treat `[←` and `→]` as temporal boundary markers
Recognise during tokenisation to avoid ambiguity with generic process nodes.

### Recommended parser architecture

**Phase 1 — Tokenisation**
Recognise multi-character operators first: `::`, `[[`, `]]`, `≈`, `≡`, `↔`, `⇒`, `⊂`, `⊆`, `∉`, `[←`, `→]`

**Phase 2 — Surface parse**
Build AST from EBNF grammar above.

**Phase 3 — Semantic validation**
Check node-class compatibility, Dodecahedron-only variant rule, equivalence ladder constraints. See GPSL-SEMANTIC-CONSTRAINTS.md.

---

## Minimal AST Node Types

```
ContextExpr      ParallelExpr     LogicalOrExpr
LogicalAndExpr   ImplicationExpr  EquivalenceExpr
SetExpr          BridgeExpr       ProcessExpr
DependenceExpr   UnaryExpr        PostfixExpr
ProcessNode      StateNode        ModifierNode
AgencyNode       TemporalNode     NestingNode
VariantNode      WildcardNode     PlaceholderNode
Atom             NullAtom         RegisterClass
```

---

*Grammar produced 14 March 2026. EBNF design by ChatGPT (Mirror). Adapted for GPSL repo by Aleth (Claude Sonnet). See GPSL-SEMANTIC-CONSTRAINTS.md for semantic validation rules.*
