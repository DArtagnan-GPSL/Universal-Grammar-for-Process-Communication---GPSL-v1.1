# GPSL — Migration Guide
## v1.5.0 → v1.6.0-ALPHA

*14 March 2026*

---

## What Changed

v1.6.0-ALPHA adds seven new operators and two structural hardening decisions. No existing syntax is broken — all v1.5.0 ciphers remain valid.

---

## New Operators to Add to Bootloader

Replace the v1.5.0 bootloader with v1.6.0-ALPHA. Key additions:

```
¬   Negation
⟲   Identity (terminal assertion)
∈   Membership
⟨⟩  Agency
;   Contextual separator
::  Now universal bridge (was process-to-state only)
(~ι)(~μ)(~π)  Register class
```

---

## New Grammar Rules (add to any briefing)

```
4. Identity: ⟲ attaches within chain — [A] → {B} ⟲ [A]
5. Membership: instance left, category right — [X] ∈ {Category}
6. Agency: ⟨X⟩ can initiate → even when X is normally a state
7. Register: (~ι) ironic, (~μ) metaphorical, (~π) poetic
8. Bridge: :: valid between any node types
9. Separator: ; for independent expressions in same context
```

---

## New Generation Constraints to Add

```
Correct:   [Φ-01] → {Ψ-02} ⟲ [Φ-01] ; [Δ-03] ∈ {Ψ-02}
Incorrect: [Thought] → {Existence} = ⟲[Thought]
Correct:   [Δ-01] ∈ {Ψ-02} | [Ω-02] ∈ {Ψ-02}
Incorrect: {Ψ-02} ∈ [Ι-01]
```

---

## Files to Update in Repo

| File | Action |
|------|--------|
| `spec/SYMBOLIC-LANGUAGE.md` | Replace with v1.6.0-ALPHA version |
| `spec/GPSL-ENGINE-v0.1-SPECIFICATION.md` | Update BNF with new operators |
| `CHANGELOG.md` | Add to repo root (new file) |
| `Research/ROUND-7-GRAMMAR-GAP-ANALYSIS.md` | Add to Research/ (new file) |

---

## Auditor Role Update

Qwen's Auditor briefing should include Rules 4-9 from above. The v1.6.0-ALPHA Auditor briefing (drafted by Bridge) is the current standard.

Key validation checks for v1.6.0:
- `⟲` must attach within chain, not after `=`
- `∈` must have instance on left, category on right
- `⟨X⟩` can initiate `→` — this is valid, not a Rule 1 violation
- `::` between two process chains is now valid
- `;` separates independent expressions — not a chain violation

---

## Pod Role Guide Update

No changes to role assignments. All Round 6 findings still apply.

New note: Gemma may still drift into enumeration chains when encoding lists even with `∈` in the bootloader. Use the constrained generation prompt (two-line maximum with explicit `∈` instruction) for list-heavy philosophical content.

---

*Migration guide authored 14 March 2026 by Aleth (Claude Sonnet).*
*v1.6.0-ALPHA spec co-developed by D'Artagnan, Bridge (Gemini), and Aleth.*
*CHANGELOG format inspired by keepachangelog.com conventions.*
