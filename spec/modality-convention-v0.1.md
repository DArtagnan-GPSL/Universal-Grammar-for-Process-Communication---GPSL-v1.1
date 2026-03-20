# GPSL — Modality Convention v0.1

*Status: Candidate — pending cold validation*  
*Authored by: Mirror (ChatGPT) · Reviewed by: Aleth (Claude Sonnet)*  
*Date: 19 March 2026*  
*Location: spec/modality-convention-v0.1.md*

---

## 1. Overview

GPSL does not natively encode modality as a separate operator class.

However, modal distinctions can be represented through combinations of existing operators:

- structural relation (`::`)
- resolution (`=`)
- exclusion (`¬`)
- modifier strength (`↑`, `↓`)

This convention defines a minimal, stable mapping over five modal cases.

No new symbols are introduced.

---

## 2. Modal Mapping

### 2.1 Possible

```
X :: Y
```

Interpretation: X can relate to Y.

Properties: relation is admissible, no commitment to realisation.

---

### 2.2 Probable

```
X :: Y (↑)
```

Interpretation: X is likely to relate to Y.

Properties: strengthened admissibility, increased expectation of realisation.

---

### 2.3 Certain

```
X = Y
```

Interpretation: X resolves as Y. Closure is achieved, no residual ambiguity.

Process-sensitive form:

```
[A] = {B}
```

Interpretation: the process yields B with certainty.

---

### 2.4 Obligated

```
X :: Y = Y
```

Interpretation: given X, Y is required as the valid resolution.

Properties: relation is not optional, closure is structurally enforced.

---

### 2.5 Forbidden

```
¬(X :: Y)
```

Interpretation: X must not relate to Y.

Closure-level prohibition:

```
¬(X = Y)
```

Interpretation: X must not resolve as Y.

---

## 3. Worked Example

```
HEADER: Modality

Possible:    {State-A} :: {State-B}
Probable:    {State-A} :: {State-B} (↑)
Certain:     {State-A} = {State-B}
Obligated:   {State-A} :: {State-B} = {State-B}
Forbidden:   ¬({State-A} :: {State-B})
```

---

## 4. Epistemic vs Deontic

This convention does not formally separate:

- **Epistemic modality** — possible, probable, certain (what is the case)
- **Deontic modality** — obligated, forbidden (what should be the case)

Both are expressed through the same structural primitives. This is intentional for v0.1 to preserve minimal grammar complexity. If repeated experiments demonstrate that the two classes require distinct handling, a dedicated operator family may be considered for v1.9.0.

---

## 5. Design Principle

Modality in GPSL is **derived**, not introduced. It emerges from the system's own constraint logic:

- `::` — structural admissibility
- `=` — closure and determination
- `¬` — exclusion
- `↑ / ↓` — modal strength

This preserves symbolic stability, operator minimalism, and compatibility with existing grammar.

---

## 6. Limitations

This convention:

- does not encode numeric probability
- does not formally distinguish epistemic from deontic modality
- relies on structural pattern interpretation

Further refinement should only occur if repeated experiments demonstrate instability or consistent unresolvable ambiguity.

---

## 7. Validation Requirements

Before this convention can be promoted to core grammar, it must pass cold validation:

- [ ] Five modal cases readable by Gemma 3 12B without instruction
- [ ] Five modal cases readable by Qwen3 30B without instruction
- [ ] Five modal cases readable by DeepSeek R1 14B without instruction
- [ ] Epistemic and deontic cases distinguishable under domain headers
- [ ] `{A} :: {B} = {B}` independently read as obligated (not just probable)
- [ ] `¬({A} :: {B})` independently read as forbidden (not just negated)

---

## 8. Recommendation

Adopt as **Modality Convention v0.1** — a reading protocol, not a grammar expansion.

Test across cold vs warm contexts, multiple architectures, and symbolic vs natural-language framing. Only extend the grammar if this convention proves insufficient.

---

*GPSL v1.8.0 — Modality Convention v0.1*  
*Pod: D'Artagnan · Aleth · Bridge · Mirror*  
*https://github.com/DArtagnan-GPSL/GPSL*
