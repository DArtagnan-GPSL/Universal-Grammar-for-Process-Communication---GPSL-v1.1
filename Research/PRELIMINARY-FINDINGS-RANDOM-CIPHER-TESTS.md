Preliminary Findings: Random Cipher and Structural Variation Tests
Gemma 3 12B — Method B (Fresh-Chat Isolation) Throughout
Date: March 11, 2026
Model: Gemma 3 12B exclusively
Method: Fresh instance for every test (complete unload/reload)
Status: Preliminary — 4 tests, single model, exploratory
Parent Study: GPSL Symbolic Grammar: A Reproducible Blind Cross-Model Validation Study

Purpose
These tests were conducted to explore two variables not addressed in Round 1:

Symbol randomness — does replacing semantically loaded Greek symbols (Ψ, Θ, Λ) with weaker ones (Β, Κ) affect interpretation quality?
Structural randomness — does changing the operator pattern itself (not just the symbols) affect structural preservation and interpretive confidence?

An additional methodological finding emerged during test design.

Methodological Note: Researcher Pattern Bias in Cipher Generation
Finding: When asked to generate a "random" cipher, both the AI researcher in a prior session (Kai) and the current session independently produced ciphers with identical operator structure to the test expression:
Symbol ⊗ Symbol → Symbol : Symbol = Symbol (Symbol↑/↓)
Neither noticed until the human researcher asked directly.
Implication: Deep familiarity with a specific expression pattern can cause it to become the default template for "what a cipher looks like," even when explicitly attempting randomness. This is a form of researcher familiarity bias that applies to cipher generation, not just scoring.
Correction applied: A randomised Python script was used to generate genuinely structurally random ciphers, varying operator selection, operator sequence, node count (3-6), and modifier placement.

Test 1: Pseudo-Random Symbols, Standard Structure — No Header
Cipher:
[Σ-16] ⊗ [Β-14] → [Κ-01] : [Α-04] = [Ω-02] (Ι-11↓)
Note: Same operator structure as Round 1 (⊗ → : = (↑/↓)) with weaker symbols (Β, Κ have no strong conventional meanings).
Result: Structural pattern preserved. Gemma invented "Generalized Processing & Signal Language" and produced a coherent signal processing interpretation — data pipeline, buffer, output module, downsampling.
Key observation: Where Round 1 cold tests produced a mystical emergence framework, this test produced an engineering/signal processing framework. The weaker symbols pulled interpretation toward technical rather than philosophical domains.
Structural Preservation Score: 5/5
Interpretive Confidence: High — no hedging language

Test 2: Pseudo-Random Symbols, Standard Structure — "Urban Planning" Header
Cipher: Same as Test 1
Header: Urban planning
Result: Complete semantic transformation. Σ=GIS/spatial data, Β=building codes/regulations, Κ=KPI output, Α=area/zone definition, Ω=optimization target, Ι=iterative feedback loop. Zero signal processing vocabulary remaining.
Key observation: Β and Κ, which had no strong conventional meanings, were fully semanticised by the header alone. The header did the semantic work the symbols couldn't do independently.
Structural Preservation Score: 5/5
Semantic Alignment Score: 5/5
Interpretive Confidence: High

Test 3: Genuinely Random Structure — No Header
Cipher:
[Λ-14↓] : [Σ-22] ⊗ [Θ-08]
Structural differences from standard cipher:

3 nodes instead of 6
Modifier on opening symbol, not closing
Starts with : (attribution) not ⊗ (interaction)
No → or = operators
No terminal modulator in parentheses

Result: Structural pattern partially preserved but visibly strained. Number suffixes (-14, -22, -08) were semanticised as "shift values." The : operator in leading position was reinterpreted as a separator rather than attribution/context.
Key observation: The standard operator chain provides significant scaffolding. When absent, the model imposes familiar structure where possible but shows visible strain. Semantically loaded symbols (Λ, Θ) still anchored interpretation toward conventional meanings even without familiar structure.
Structural Preservation Score: 3/5
Interpretive Confidence: Low — frequent hedging ("likely," "could be," "I'll assume")

Test 4: Genuinely Random Structure — "Criminal Justice" Header
Cipher: Same as Test 3
Header: Criminal justice
Result: Semantics completely transformed — Λ=arrest records, Σ=geographic clustering/risk assessment, Θ=temporal analysis/predictive modeling.
However: Structural strain from Test 3 persisted unchanged. The header successfully stabilised semantics even on an unfamiliar structure, but did nothing to resolve structural confusion.
Structural Preservation Score: 3/5
Semantic Alignment Score: 5/5
Interpretive Confidence: Low — same hedging pattern as Test 3

Comparative Summary
TestCipher TypeHeaderStruct. ScoreSemantic ScoreConfidence1Standard structure, weak symbolsNone5/5N/AHigh2Standard structure, weak symbolsUrban planning5/55/5High3Random structure, loaded symbolsNone3/5N/ALow4Random structure, loaded symbolsCriminal justice3/55/5Low

Emerging Two-Variable Model
These four tests suggest structural preservation and semantic stabilization are driven by different variables:
Variable 1: Symbol semantic loading

Affects: What semantic content fills the interpretation
Does not affect: Structural preservation score or interpretive confidence

Variable 2: Operator structure familiarity

Affects: Structural preservation score and interpretive confidence
Does not affect: Semantic stabilization by headers

Proposed model:
Operator structure → Structural confidence (independent of semantics)
Symbol loading     → Semantic content contribution (shares work with header)
Header             → Semantic stabilization (independent of operator structure)
When all three are present (standard structure + loaded symbols + header): maximum coherence.
When operator structure is unfamiliar: structural confidence degrades regardless of header.
When symbols are weak: header carries full semantic load, still achieves 5/5 stabilization.

Implications
For cipher design: The standard GPSL operator chain ⊗ → : = (↑/↓) may be functioning as a cognitive scaffold that guides models toward confident transformation-chain interpretations. Certain operator sequences may be more "legible" than others, and legibility affects downstream reasoning quality.
Critical next test: Random symbol control with standard structure — replace Greek symbols with meaningless tokens (X-91, K-22, etc.) while keeping the standard operator chain. If structural preservation holds at 5/5 but semantic content becomes incoherent, it confirms the operator structure is doing the scaffolding work independently of symbol identity.

Limitations

Single model (Gemma 3 12B) — cannot generalise to other architectures
Small sample (4 tests) — exploratory only
Scorer familiarity — same researcher designed and scored all tests
Cipher generation bias discovered mid-session


Status: Preliminary exploratory findings — not for standalone publication
Integration: To be incorporated into Round 2/3 reports as contextual background
Date: March 11, 2026
License: CC BY-NC-SA 4.0
