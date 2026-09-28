# Galata, Johnson & Hogg (2001) — Learning Variable Length Markov Models of Behaviour

*Computer Vision and Image Understanding* **81**(3):398–413 · DOI 10.1006/cviu.2000.0894
*(volume / pages / DOI taken from `paper_notes/paper_index_A.csv` line 60 — none of it appears in the local file)*
Local file: `knowledge/reading_docs/Galata_Johnson_Hogg_2001_VLMM_Behaviour_CVIU.pdf`
Read: 2026-09-16 · Method: Three-Pass (Keshav) per `knowledge/reading_guide.md` · verified by an independent second pass (§8)

> **Version caveat:** the local PDF is the **author manuscript / preprint**, not the CVIU typeset
> version. Evidence: a cover page carrying postal address, telephone, facsimile and email; no journal
> header, no DOI, no copyright line, no received/accepted dates; internal pagination running 1→33;
> references on pp. 20–22, a "List of figures" page on p. 23, figure plates on pp. 24–33; and
> uncorrected typos a copy-editor would have caught ("occurances", "enchanced", "silhoutte",
> "Qualisis", "perfoming", "permformance"). `paper_index_A.csv` gives the source as the author-hosted
> `cs.man.ac.uk/~agalata/publications/cviu_paper.pdf`, which corroborates this.
> **Consequences:** page-level citations must use the published 398–413 pagination, not this file's.
> Section and equation numbers are used throughout below but **could not be checked against the
> typeset version** — confirm before citing a specific equation number.
>
> **Symbol caveat:** this PDF's text layer **drops every Greek glyph**, so the paper's own symbol
> names are not recoverable from it (the PFSA tuple renders as "M = (Q )"). Greek letters below are
> this summary's placeholders, chosen to avoid collision; verify against the typeset version before
> quoting notation.

---

## Five Cs (pass 1)

- **Category** — Research prototype + experimental evaluation. Proposes two model architectures and
  evaluates them on two self-collected datasets. Not a survey, not a systems analysis.
- **Context** — Positioned against HMM-based activity modelling: Bobick & Ivanov's hand-coded
  stochastic context-free grammar over HMM primitives [4]; Bregler's probabilistic decomposition of
  human dynamics [5]; Pentland & Liu [14] and Rittscher & Blake [17], who couple dynamic models with
  a Markov chain. The VLMM machinery is imported from text compression [7, 2] and language/handwriting
  modelling — Ron, Singer & Tishby's "The Power of Amnesia" [18] and Guyon & Pereira [9]. The
  vector-quantisation front end is the authors' own prior work, Johnson & Hogg [13].
- **Correctness** — Assumptions are reasonable and mostly stated. The weak link is not the model but
  the evaluation: results are reported **only as figures**, with no tables, no numeric values in the
  running text, and no significance testing (see §5).
- **Contributions** — (1) VLMM over VQ pose prototypes as a behaviour model; (2) automatic temporal
  segmentation into "atomic behaviours" via velocity minima, plus a **second-level VLMM over those
  atoms** — a two-timescale hierarchy learned without prior knowledge; (3) a Monte-Carlo long-horizon
  prediction-error protocol; (4) demonstrations in synthesis (VRML humanoid) and prediction.
- **Clarity** — Generally clear and compact. Notation is dense in §4.4; the dimensionality
  bookkeeping in §2.1 is inconsistent; and the paper contradicts itself on the level-2 alphabet
  (§4.2 vs §4.5) — all detailed in §5.

## Extraction table (อ.Proadpran)

| ช่อง | สรุป |
|---|---|
| **Motivation** | HMMs "do not encode high order temporal dependencies easily"; iterative optimisation hits local optima when there are many free parameters, so model topology and size are "often highly constrained prior to training". And Bobick & Ivanov [4] had to **hand-code** the high-level structure as a stochastic context-free grammar. |
| **Research question** | Can the high-level stochastic structure of a semantically rich activity be acquired **automatically, without any prior knowledge**, in a form supporting both recognition and generation? |
| **Proposed method** | Augmented configuration space (pose + first derivative) → robust VQ into prototypes → prototype string → VLMM. Then a hierarchy: velocity-minima key prototypes → atomic behaviours (DTW-clustered template sequences) → a second VLMM over those atoms. |
| **Evaluation** | Mean prediction error `E_T` vs. horizon `T`, weighted by Monte-Carlo sampling (50 stochastic predictions per frame); plus qualitative inspection of synthesised sequences and VRML animation. |
| **Contribution** | A learned, generative, two-timescale behaviour model; a baseline family (first-order Markov → VLMM → hierarchical VLMM); an interpolation scheme (Eq. 8) that recovers timing after prototype de-duplication. |

---

## 1. Problem and motivation

An activity is modelled as "a sequence of primitive movements with a high-level structure controlling
the temporal ordering." Bobick & Ivanov [4] achieved this with a *hand-coded* stochastic context-free
grammar over HMM primitives; other work on structured activity [6, 20, 21] used phase-space
constraints or HMMs without an explicit high-level grammar. The authors object that HMMs do not encode
high-order temporal dependencies easily and that local optima under many free parameters mean topology
and size are "often highly constrained prior to training." The target is therefore **automatic
acquisition** of the high-level structure, for behaviours such as dance, aerobics and sign language.

The paper commits early to **two specific time scales**: the prototype level spans motion "typically
spanning of the order of **20ms**", while atomic behaviours represent primitive actions "typically
lasting of the order of **a second**", the example given being *raising an arm*. These two numbers are
what make the "two-timescale" claim concrete.

## 2. Core contribution and method

### 2.1 Augmented configuration space and discretisation (§2)

A behaviour is a trajectory in an **augmented configuration space** stacking the d-dimensional
configuration `C_t` with its first derivative `Ċ_t`:

    F_t = (C_t, λ Ċ_t),   F_t ∈ [0,1]^{2d}

with λ balancing the derivative contribution when Euclidean distance is used as the dissimilarity
measure. Including derivatives is justified twice: it **"helps resolve ambiguities in configuration
space"** (the same pose passed through in two directions is not the same state), and it "facilitates
the use of models in performing generative tasks."

Each `F_t` is replaced by its nearest prototype from a finite set `P = {p_0 … p_n}` learned by the
robust vector quantisation of Johnson & Hogg [13]. Crucially: **"Multiple occurances [sic] of the same
prototype are replaced by a single occurance [sic]."** The prototype string therefore carries *order
but not duration* — a design decision the paper later has to repair (Eq. 8).

### 2.2 Variable length Markov models (§3.1)

A VLMM lets memory length vary by context instead of being fixed at order n. For memory string `w`
and candidate extension `aw`, a weighted Kullback–Leibler divergence measures the information gained
by lengthening the memory:

    H(aw, w) = P̂(aw) Σ_{a'} P̂(a'|aw) · log [ P̂(a'|aw) / P̂(a'|w) ]        (Eq. 5)

If `H(aw, w)` exceeds threshold ε the longer memory `aw` is used; otherwise `w` is deemed sufficient.
(Note a small inconsistency in the paper's own framing: §1 calls this "a cross-entropy measure", while
§3.1 calls it "a weighted Kullback-Leibler divergence [18]".) Transition probabilities and priors are
relative frequencies over the training corpus (Eqs. 6–7, where `v(·)` counts token-string occurrences
and `v₀` is "the total length of the training sequences").

Training builds a **prefix tree** [9] of strings up to a predetermined length N, counting transitions
by sliding a fixed-length-N window along the training token sequence. The tree is pruned into a
**prediction suffix tree** [18] — a suffix node is created only if the KL divergence between the
distribution at the prefix node and that at its ancestor exceeds ε — and converted into an automaton.

The result is equivalent to a **Probabilistic Finite State Automaton** `M = (Q, Σ, δ, γ, π)`: a finite
alphabet Σ of tokens; a finite state set Q, each state corresponding to a token string of length at
most N (the memory); a transition function `δ: Q × Σ → Q`; an output probability function
`γ: Q × Σ → [0,1]` giving memory-conditioned probabilities of the next token; and a start-state
distribution `π: Q → [0,1]`. Normalisation is stated explicitly: for every `q ∈ Q`, `Σ_a γ(q,a) = 1`,
and `Σ_q π(q) = 1`.

The pitch is explicitly the **"ability to locally optimise the length of memory required for
prediction"** — long memory where behaviour needs it, short memory elsewhere.

### 2.3 Level 1 — VLMM over prototypes (§3.2)

Training sequences are converted to prototype strings by nearest-neighbour assignment at each instant;
"only transitions between different prototypes are considered for training." These train a PFSA `M_p`.

- **Generation (§3.2.1):** traverse the PFSA, taking either the most likely transition (maximum
  likelihood generation) or a sample from the transition distribution (stochastic generation),
  emitting the corresponding prototype vectors.
- **Recovering timing (Eq. 8):** because repeats were removed, the interval between generated
  prototypes is "initially unspecified (due to the removal of repeated prototypes)". Assuming
  **constant acceleration**, it is approximated by

      Δ_r = 2 |C_{r+1} − C_r| / ( |Ċ_r| + |Ċ_{r+1}| )                     (Eq. 8)

  This is exactly **distance divided by mean speed**: under constant acceleration the mean speed is
  `(|Ċ_r| + |Ċ_{r+1}|)/2`. A **cubic Hermite interpolant** defined by endpoints `C_r, C_{r+1}` and
  tangent vectors `Ċ_r, Ċ_{r+1}` (scaled by Δ_r) is then sampled at data frame rate to give a
  temporally regular sequence. This is why the derivative had to be in the feature vector: without
  `Ċ` there are no tangents and no duration estimate.
- **Prediction (§3.2.2):** because states encode history, the model is first run in *recognition mode*
  — consuming observed prototypes and making the corresponding transitions in order to locate the
  current state — then switched to generation. (This narrow sense of "recognition" should not be
  confused with behaviour-class recognition, which the paper claims as a capability but never
  measures; see §5.)
- **Unseen events:** if `M_p` is presented with a prototype that the current state emits with
  probability zero, the model "return[s] to the initial model state, lose[s] all the previous memory
  and predict[s] p_i with the prior P̂(p_i)". The authors call this back-off "simple but effective"
  and point at Jelinek [11] for more complex alternatives.

### 2.4 Level 2 — structured / hierarchical model (§4)

Motivation: motion in human activities "has different characteristics at different time scales,
usually carrying syntactic and semantic information at larger temporal scales," which a single
prototype-level VLMM cannot span.

- **Key prototypes (§4.1):** given the physical constraints of the human body, "any change in the type
  of human movement usually causes dips in velocity." Prototypes for which the magnitude of the first
  derivative `|Ċ_t|` is a **"local minimum and below a fixed threshold (chosen by inspection)"** form
  the key set `K ⊆ P`. (Note this threshold is applied to the *unscaled* `Ċ_t`, not to `λĊ_t`.) The
  authors concede that ideally segmentation points "might be derived from a global maximisation of
  likelihood over the training data" and flag this as future research.
- **Atomic behaviours:** each ordered pair of key prototypes `(k_i, k_j), i ≠ j` defines an atomic
  behaviour `α_ij` spanning the behaviour observed between them. Each `α_ij` comprises m **template
  sequences** `T^l_ij`, each an ordered set of prototypes (Eq. 11), with m and template length varying
  per component. Templates are built by collecting all training sub-sequences spanning `k_i → k_j`,
  partitioning them into "clusters of self-similar sequences using dynamic time warping [19]" to
  assess similarity, then generating one template per cluster by "re-sampling, averaging, and
  re-quantisation". Template priors `P(T^l_ij)` (summing to 1 within a component) come from the
  relative frequency with which templates are matched in the corpus.
- **Higher-level grammar (§4.2):** a second VLMM `M_k` is trained **using the key prototypes as its
  alphabet**. Because `α_ij` *is* the transition `k_i → k_j`, it follows that
  `P_{M_k}(α_ij | s k_i) = P_{M_k}(k_j | s k_i)` — so transitions between atomic behaviours are
  implicit in a model whose tokens are key prototypes. The template-level probability is

      P_{M_k}(T^l_ij | s k_i) = P(T^l_ij) · P_{M_k}(α_ij | s k_i)          (Eq. 12)

  ⚠️ §4.5 contradicts this, describing the same models as "using **atomic behaviours** as an
  alphabet". The §4.2 construction (key prototypes as alphabet, atomic behaviours implicit) is the
  one given in detail and is taken as authoritative here.
- **Generation (§4.3):** traverse `M_k`, emitting a key prototype at each step and replacing each
  `k_i k_j` subsequence with `k_i T^l_ij k_j`, choosing the template either by maximising Eq. 12 or by
  sampling. Entirely hypothetical sequences start from the start-state distribution, approximated by
  the relative frequency of starting at each state in training. **Fig. 6** shows such a synthesised
  routine (dataset 2, N = 4) animating "a virtual humanoid using the VRML modelling language" — the
  Acknowledgments identify it as "Baxter", a standard H-Anim 1.1 VRML humanoid.
- **Prediction (§4.4):** harder than level 1 — one must also identify *which* template is currently
  being traversed and *where* in it. A Bayesian formulation uses the learned transition probabilities
  as priors:

      P(T^l_ij | O_t, s k_i) ∝ P(O_t | T^l_ij) · P_{M_k}(T^l_ij | s k_i)   (Eq. 13)

  All templates from the last observed key prototype `k_i` to any `k_q` are considered; for each, DTW
  finds the position minimising alignment cost, giving minimum cost `c_t(i,q,r)`. The likelihood is
  *approximated* by the relative cost

      P(O_t | T^l_ij) = 1 − c_t(i,j,l) / Σ_{q,r} c_t(i,q,r)                (Eq. 14)

  Maximising Eq. 13 identifies the subsequent key prototype and hence the next VLMM state. Generated
  future behaviour is the remainder of the current template plus continuation from the new state.
  **Unseen events** are detected when the maximum probability falls below a threshold; the high-level
  history is then discarded and the next key prototype predicted from Eq. 14 alone.
  **Fig. 7** shows the qualitative output: maximum-likelihood extrapolation at selected instants, with
  recent behaviour drawn as filled contours shaded by recency (lightest = current) and "the first 12
  frames of each extrapolation" illustrated.

## 3. Evaluation protocol

Mean prediction error at horizon T, measured in configuration space per §3.2.3 (not token space):

    E_T = ( Σ_{j=1..n} | C^j_{t+T} − C_{t+T} | ) / n                        (Eq. 9)

where n is "the total number of trials carried out over all test sequences" and `C_{t+T}` is ground
truth. Errors are averaged over predictions generated "on every frame of every test sequence", and
"updated only if both a prediction and the ground truth exist for the particular T".

> ⚠️ The source is ambiguous about the space: §3.2.3 says "in configuration space", but the captions
> of Figs. 4 and 10 both say "in the **augmented** configuration space". Since the plotted magnitudes
> come from those figures, the units of the y-axis are not pinned down by the text.

Because cycles in the transition structure make it impossible in general to enumerate all possible
predictions from a state, the probabilistic weighting is obtained by **Monte-Carlo simulation** —
**"50 stochastic predictions were generated on each frame"**, with their relative frequency providing
the weighting. Figure error bars are **mean error ± mean absolute deviation**.

## 4. Data and results

### Dataset 1 — 2-D contour tracking (§2.1.1)
One individual performing an exercise routine, tracked with a simple contour tracker [12, 1];
**40 s at 25 fps**. Configuration = n control points of a closed uniform B-spline approximating the
silhouette boundary, evenly spaced and ordered relative to a consistent reference point (enhanced from
[1] so the top of the head is located more accurately), transformed into an object-centred frame and
normalised to [0,1]. With **32 control points**, the paper reports a **128-dimensional augmented
configuration space (2 × 2 × 32)**. Scaling factor **λ = 10** → **71 prototypes**. Routine structure
(Fig. 1b): two exercises, each repeated four times and each followed by four repetitions of a
sub-exercise (labelled Exercise 1, 1a, 2, 2a).

- VLMM over prototypes, **ε = 0.0001**: **N = 5 → 117 states**; **N = 20 → 290 states**.
- Test sequence: same two exercises and sub-exercises, but each repeated **three** times.
- Prediction plotted over **1 ≤ T ≤ 70** ("≈3 sec."); mean-error axis 0–1.8 (Figs. 4a, 10a).
- Hierarchical model: **5 key prototypes, 8 atomic behaviours**; VLMMs at N = 4, 6, 8 (ε = 0.0001)
  → **22, 34, 45 states**. Prediction reported for N = 6.

### Dataset 2 — 3-D motion capture (§2.1.2)
Commercial system (ProReflex camera, MacReflex software, "Qualisis 97" [sic — Qualisys]); **3-D
locations of 13 body markers at 50 fps**; **8 training sequences of ≈25 s each** from one individual.
Points transformed to object-centred coordinates and normalised to [0,1]. Scaling factor **λ = 30** →
**87 prototypes**. Routine (Fig. 2): three exercises with the first repeated twice; a sub-exercise
occurring in the last two exercises, repeated twice within each.

- VLMM over prototypes, ε = 0.0001: **N = 5 → 112 states**; **N = 20 → 226 states**.
- Two test sequences of ≈25 s; prediction plotted to **T ≈ 140** ("up to about 3 seconds"); error
  axis 0–0.9.
- Hierarchical model: **5 key prototypes, 8 atomic behaviours**; VLMMs at N = 2 and N = 4
  → **9 and 12 states**. Prediction reported for N = 4.

### Findings
1. **VLMM ≫ first-order Markov.** "As can be seen from the prediction graphs … substantially better
   results are obtained using VLMMs in comparison to a first order Markov model" — both datasets.
2. **Hierarchical ≫ flat VLMM.** "the structured behaviour models consistently give better prediction
   results, demonstrating the increased ability of the model to encode the complex, long-term
   temporal dependencies."
3. **Structure is visible in synthesis (Fig. 9, dataset 1).** At **N = 1 — which the paper states is
   "equivalent to a first order Markov model"** — "the model does not capture longer-term temporal
   constraints between atomic behaviours as can be seen by the random order in which the separate
   exercises and sub-exercises are generated." At N = 4 and N = 8 there is "correct progression from
   one exercise or sub-exercise to the next." The figure displays every second frame of the first
   **700 frames** (≈28 s at 25 fps), which is what makes the order-shuffling visible. This is the
   paper's cleanest qualitative result: first-order order-shuffles the routine.
4. **Memory length is genuinely variable** (Figs. 3, 8): the per-state memory-length histograms are
   the direct evidence that the KL criterion assigns long memory only where it is needed.

> ⚠️ **All quantitative results in this paper live in figures.** There are no tables and no numeric
> error values in the running text. The toolchain available in this run (`pdftotext` only; no
> `pdftoppm`/PyMuPDF for page rasterisation) could recover figure axes, tick ranges and series legends
> but **not the plotted curve values**, so no specific `E_T` magnitudes are quoted here. The *ordering*
> of the curves is asserted by the authors in text and is reproduced verbatim above; the *magnitudes*
> remain unverified from this file. Figures 4 and 10 each carry a `FIRST ORDER MARKOV MODEL` series,
> confirming the comparison was actually plotted.

## 5. Assumptions and limitations

**Stated or acknowledged by the authors**
- The key-prototype velocity threshold is "chosen by inspection"; global likelihood-based segmentation
  is explicitly left to future research.
- Back-off on unseen events is "simple but effective," with better schemes [11] not pursued.
- Eq. 8 explicitly assumes **constant acceleration** between prototypes.
- Eq. 14 is presented as *approximating* the likelihood by a "relative probability" — the paper does
  not claim it is a normalised probability.
- Extension beyond two hierarchy levels is speculative ("could be envisaged").

**Unstated / observed on close reading**
- **No statistical significance testing anywhere.** The only dispersion reported is "mean error ±
  mean absolute deviation" in the Fig. 4 and Fig. 10 captions — no confidence intervals, no tests, no
  seeds, no repeat-run variance.
- **Tiny, single-subject data.** Dataset 1 is "a 40 second sequence of **an individual**"; dataset 2
  is "eight sequences … of **an individual**" (≈200 s). The section openers use the generic plural
  ("individuals performing exercise routines"), but the training data is explicitly one person in
  both cases. Nothing here demonstrates generalisation across subjects.
- **Test material is drawn from the same routine as training.** For dataset 1 the test sequence
  differs only in repetition count (three vs four); for dataset 2 the paper states the test sequences
  comprise "the same three exercises and sub-exercises as those in the training data" with **no**
  stated difference at all. No unseen activity structure is ever tested.
- **Vocabulary size is an unreported dependency.** 71 and 87 are *outputs* of the robust VQ of [13],
  not chosen values; the VQ's own parameters are never stated, and no sensitivity analysis over
  prototype count is reported.
- **λ is never tuned or ablated** (10 for 2-D contours, 30 for 3-D mocap, both unjustified). It
  affects segmentation only *indirectly* — by changing which prototypes exist, and hence the set from
  which key prototypes are drawn — since the §4.1 threshold is applied to the unscaled `|Ċ_t|`.
- **De-duplication is a real information loss**, only partially repaired: Eq. 8 *reconstructs* timing
  under a constant-acceleration assumption rather than preserving measured dwell time, so a long hold
  and a brief pause at the same pose are indistinguishable in the token string.
- **Eq. 14 is not a normalised probability.** Summed over M competing templates, `1 − c/Σc` equals
  M − 1, so it normalises only when M = 2; its scale depends on how many competing templates happen
  to exist. The paper hedges ("approximate", "relative probability", and Eq. 13 is a proportionality),
  so this is a presentational weakness rather than an error.
- **Dimensionality bookkeeping is inconsistent.** §2.1.1 uses d for the *configuration* dimension
  (d = 2n = 64; augmented = 128 = 2×2×32), whereas §2.1.2 uses d for the *augmented* dimension. Worse,
  §2.1.2 states **"d = 72 (2 × 3 × 13)"**, but 2 × 3 × 13 = **78**. Two defects in one sentence: §2
  defines `F_t ∈ [0,1]^{2d}`, so with 13 markers d should be 39 and the augmented space 78. Since
  "13 points" is stated twice, **78 is the likely intended value**. Quote this number with care.
- **The level-2 alphabet is stated two ways** — key prototypes (§4.2, with the derivation) vs atomic
  behaviours (§4.5). These are reconcilable in substance but the text contradicts itself.
- **Evaluation is prediction-only.** Behaviour recognition is claimed as a capability in §3 ("able to
  support both recognition and generative capabilities") and in the Conclusions ("can be utilised for
  behaviour recognition"), but every experiment (§3.2.4, §4.5) is prediction or synthesis. Synthesis
  quality is assessed purely by eye.
- **No runtime cost, no code, no data release** — noted as an artefact-availability gap by modern
  norms rather than as a methodological defect for a 2001 CVIU paper.

## 6. Relation to adjacent work the paper cites

- **vs. Bobick & Ivanov [4]** — they parse activity using a *hand-coded* stochastic context-free
  grammar over HMMs modelling low-level primitives; this paper's central claim is that the equivalent
  high-level grammar can be **learned** from data. This is the sharpest positioning in the paper.
- **vs. Bregler [5], Pentland & Liu [14], Rittscher & Blake [17]** — all decompose human dynamics into
  phases or dynamic models coupled by a Markov chain representing long-term continuity constraints;
  that chain is fixed-order, which is precisely the VLMM's target.
- **vs. HMMs [16]** — stated objections: high-order temporal dependencies are not encoded easily, and
  local optima under many free parameters mean topology and size are "often highly constrained prior
  to training".
- **Inherits from Ron, Singer & Tishby [18]** — prediction suffix trees and the KL-pruning criterion
  come wholesale from "The Power of Amnesia"; the same lineage includes Guyon & Pereira [9] (also
  cited for the prefix tree), Hu et al. [10] (language modelling), and text compression [7, 2].
- **Inherits from Johnson & Hogg [13]** and Baumberg & Hogg [1] — the robust VQ front end and the
  flexible contour model are the authors' own earlier machinery. The paper is honestly a
  *composition*: an existing VQ pipeline joined to an existing language-modelling tool, applied to
  behaviour, with the hierarchy (§4) as the genuinely new part.
- **DTW [19] (Sakoe & Chiba)** does double duty — clustering sub-sequences into templates (§4.1) and
  localising position within a template at prediction time (§4.4).
- **Problem-space context** [6, 20, 21]: phase-space constraints (Campbell & Bobick) and ASL
  recognition with HMMs (Starner & Pentland; Vogler & Metaxas) are cited as the "structured,
  semantically rich behaviour" literature, but are not compared against.

---

## 7. Checklist pass (`knowledge/reading_checklist.md`)

`reading_checklist.md` is a prioritised reading queue rather than a per-paper questionnaire, so this
pass is run in four parts: (a) the read-for targets the checklist sets for **this** paper (Tier 0
item 1), (b) other checklist entries this paper actually speaks to, (c) the experiments E1–E7 that the
checklist says the reading should trigger, and (d) entries with no bearing.
*The checklist file was read only; it was not modified.*

### (a) Tier 0 item 1 — the targets set for this paper

| Checklist target | Verdict | What the paper actually says |
|---|---|---|
| §3 — VQ + VLMM, KL threshold ε | **Addressed** | §2 gives the VQ front end (robust VQ of [13], repeats collapsed — the checklist files VQ under §3, but it is §2); §3.1 gives the weighted KL criterion (Eq. 5) and the prefix-tree → prediction-suffix-tree → PFSA procedure. **ε = 0.0001 in all four reported experiments** — both datasets, both model levels. |
| §4.1–4.5 — hierarchical: key prototypes → atomic behaviours | **Addressed in full** | §4.1 key prototypes = velocity local minima below a hand-chosen threshold; atomic behaviours = ordered key-prototype pairs, realised as DTW-clustered, re-sampled/averaged/re-quantised templates. §4.2 second VLMM (Eq. 12). §4.3 generation by expanding `k_i k_j → k_i T^l_ij k_j`. §4.4 Bayesian template identification (Eqs. 13–14). §4.5 experiments. **This closes the gap carried in `paper_chain.md` (R9-5 item 1, restated as R10-4 item 5), where §4.1–4.5 was listed as still unread.** |
| Eq. 8 — cubic Hermite recovers duration from velocity | **Addressed** | Confirmed: `Δ_r = 2|C_{r+1} − C_r| / (|Ċ_r| + |Ċ_{r+1}|)` = distance ÷ mean speed under constant acceleration, feeding a cubic Hermite interpolant with endpoints `C_r, C_{r+1}` and tangents `Ċ_r, Ċ_{r+1}` scaled by Δ_r, resampled at data frame rate. **Caveat the checklist does not anticipate:** this *reconstructs* plausible timing; it does not *preserve* measured dwell time. It is a repair for de-duplication, not a substitute for keeping duration. |
| Mean error `E_T` vs horizon, Monte Carlo 50 per frame | **Addressed** | Eq. 9 defines `E_T`; §3.2.3 states 50 stochastic predictions per frame, justified by the impossibility of enumerating continuations when the transition structure has cycles. Error bars = mean absolute deviation. **Directly reusable as a project metric** — but note the §3.2.3 / Fig. 4 & 10 ambiguity over configuration vs *augmented* configuration space. |
| Claim: our `transition_matrix.npy` is "the weakest member of the family" | **Addressed — and stronger than the checklist states** | First-order is beaten on prediction error on both datasets, *and* §4.5 adds an independent qualitative failure: at N = 1, "equivalent to a first order Markov model", synthesis produces "the random order in which the separate exercises and sub-exercises are generated." So first-order fails both quantitatively (`E_T`) and structurally (it shuffles routine order). |
| Claim: "closest structural ancestor … VQ prototypes → string → Markov model" | **Confirmed** | The pipeline shape matches exactly. **⚠️ One correction owed upstream:** `paper_index_A.csv` line 60 describes this as VLMM "on dance". It is **not** dance. "dance" occurs exactly twice in the entire document, both in the same motivating list ("dance, aerobics, and sign language", Abstract and §1); "exercise" occurs 29 times, and every dataset, figure and caption is an **exercise/aerobics routine** (2-D silhouette contours; 13-marker 3-D mocap). Fix before it propagates into the thesis. |

### (b) Other checklist entries this paper bears on

| # | Entry | Verdict | Bearing |
|---|---|---|---|
| 3 / 13 | DASB bitrate; Scaling Laws with Vocabulary (small vocab when data-bottlenecked) | **Partially addressed** | Supplies two more data points in the low-hundreds bracket — **71** prototypes (40 s of 25 fps video) and **87** (~200 s of 50 fps mocap). Consistent with "small corpus → small vocabulary", but this is *corroboration by example only*: the counts are VQ outputs, there is **no vocabulary sweep and no sensitivity analysis**, and the paper never argues for these sizes. Do not cite as evidence *for* an optimal V. |
| 4 | Discrete speech tokens review — dedup destroys duration | **Addressed, and it is the same problem** | §2 collapses repeats; §3.2.1 concedes the interval is "initially unspecified (due to the removal of repeated prototypes)". Independent 2001-era confirmation of the concern, plus a concrete mitigation (Eq. 8). |
| 8 | FSQ / codebook collapse | **Not covered** | Predates the issue; collapse is never discussed. Consistent with the checklist's warning that collapse is a *large*-codebook pathology, but this paper is not evidence either way. |
| 10 / 19 | Matrix Profile VI limb-subspace risk; Skeleton Motion Words | **Partially addressed — as a cautionary example** | The configuration space is **whole-body** (all 32 spline control points, or all 13 markers) under a single global Euclidean metric, with no per-limb decomposition anywhere. It therefore *exhibits* the risk item 10 names rather than addressing it: a small-amplitude arm motif would be masked by torso and leg displacement. Useful as prior art showing the whole-body choice is conventional — **not** as a defence of it. |
| 6 / 7 / 11 / 17 | Rhythm is a Dancer; Keyposes; Atomic Movements; Motion Texture | **Partially addressed** | This paper is the earlier ancestor of all four patterns: quantised pose units, a hierarchy over them, "atomic behaviours" (the same term item 11 uses), and transition-matrix structure. It sets the novelty bar: **an automatically learned two-level hierarchy over movement atoms existed in 2001.** Any claim to *discovering* hierarchical structure must be distanced from §4 explicitly. |
| 12 | Aligning motion generation with human perceptions | **Not covered** | No perceptual study, no user study, no learned critic; synthesis is judged by eye (Figs. 6, 9). Reinforces the project's need for an independent generation metric — this paper offers none. |
| 24–31 | Tier 3 Phase-2 / energy-curve entries | **Partially addressed (relevant, unexpectedly)** | Segmentation by **velocity minima** (§4.1) is motion-energy-based structural segmentation, and §4 as a whole is macro-structure modelling of movement. `paper_chain.md` already records an obligation to distance Phase 2 from A1-21 §4; this full read **confirms** it. Difference in kind: Galata et al. segment by *instantaneous* velocity minima on the pose trajectory, not by clustering a smoothed whole-sequence energy curve. |

### (c) Experiments the checklist derives from this reading

| Exp. | Status after this read |
|---|---|
| **E2 — VLMM + first-order Markov as LSTM baselines** | **Unblocked.** The paper supplies the VLMM hyperparameters needed: ε = 0.0001; N ∈ {5, 20} at the prototype level and N ∈ {2, 4, 6, 8} at the higher level; training via prefix tree → KL-pruned prediction suffix tree → PFSA; back-off to the initial state on zero-probability tokens; evaluation by `E_T` with 50 Monte-Carlo predictions per frame and mean-absolute-deviation error bars. The project already has the transition matrix, so first-order is nearly free. **Not supplied, and must be decided locally:** the robust-VQ parameters behind 71/87 (deferred to [13]), the *value* of the §4.1 velocity threshold, the number of template clusters m per atomic behaviour and the DTW clustering stopping criterion, and the §4.4 unseen-event threshold. **Budget caveat:** the state counts (117/290 and 22/34/45 from V=71; 112/226 and 9/12 from V=87) came from vocabularies of 71/87 — a vocabulary of 216 at N = 20 should be expected to yield a substantially larger automaton. |
| **E3 — velocity in the feature vector, then dedup** | **Fully justified.** Eq. 8 needs `Ċ` at both endpoints, so velocity must be *inside* the feature vector before de-duplication for timing to be recoverable at all. λ is the balancing knob (10 for 2-D contours, 30 for 3-D mocap) — chosen without ablation there, so the project must tune it itself. |
| **E1 — limb-subspace check (`stumpy.mstump`)** | **Not addressed.** See row 10/19: whole-body only, no subspace analysis. |
| **E4 — V-sweep at fixed window rate** | **Weakly supported only.** 71 and 87 are data points, not evidence; no sweep is performed. |
| **E5 — continuous-baseline LSTM** | **Not addressed.** No continuous baseline; the paper never asks what discretisation costs. |
| **E6 — z-zeroed vs full 3-D tokenisation** | **Not addressed.** Dataset 2 is marker-based mocap with no depth-error discussion, so it says nothing about monocular z reliability. |
| **E7 — corpus-free metrics (Coverage / LocalDiv / InterDiv / SiFID)** | **Not addressed.** `E_T` is a *ground-truth-matching* prediction metric requiring paired test sequences; it is not a corpus-free diversity metric and cannot substitute for E7. Complementary, not overlapping. |

### (d) Checklist entries with no bearing on this paper

Items 2 (SinMDM), 5 (Rode et al. monocular pose), 9 (Labrak et al.), 14–16, 18, 20–23 (Tier 2
related-work entries), and the entire paywalled/blocked group (L3-29, L3-26, A0-2, A0-5, A0-6) are
unrelated to this paper's content. **Not covered — correctly so.**

### ⚠️ Corrections owed upstream (found during this pass; not applied — these files are inputs)

1. **`paper_notes/paper_index_A.csv` line 60** — "variable-length Markov over pose strings **on dance**"
   is wrong. Should read: *on exercise/aerobics routines (2-D silhouette contours; 13-marker 3-D mocap)*.
2. **`reading_checklist.md` line 17** — gives this paper's PDF path as
   `knowledge/references/Galata_...pdf`. The file is **not** there (`knowledge/references/` holds only
   course slides and `paperหนัง.pdf`). The actual location is `knowledge/reading_docs/`.

### Checklist verdict in one line
Every read-for target the checklist set for this paper is **addressed in full** — §3, §4.1–4.5, Eq. 8
and the `E_T`/Monte-Carlo-50 protocol are all confirmed, unblocking **E2** and **E3** — while
**E1, E5, E6, E7 are untouched** and **E4 only weakly corroborated**; two corrections are owed to the
project's own input files (this is **exercise/aerobics** data, not dance; and the checklist's PDF path
is wrong).

---

## 8. Verification (independent second pass)

A separate fact-auditor re-extracted the PDF itself (`pdftotext` in both `-layout` and `-raw` modes),
re-read `reading_guide.md` and `reading_checklist.md`, and audited the draft adversarially against the
source. Verdict: **REVISE — no fabrications, no invented citations, no misquoted numbers.**

**What it checked and confirmed correct**
- **Every number**, traced to the PDF and checked for attribution to the right dataset *and* the right
  model level: 71/87 prototypes; 117/290, 112/226, 22/34/45, 9/12 states; ε = 0.0001 across all four
  experiments; λ = 10/30; 25/50 fps; 40 s, 8 × ≈25 s; 32 control points; 13 markers; 128 = 2×2×32;
  5 key prototypes and 8 atomic behaviours (both datasets); Monte Carlo 50; horizons 70 / ≈140; axis
  maxima 1.8 / 0.9; training four repetitions vs test three.
- **All six flagged equations** (5, 8, 9, 12, 13, 14) transcribe correctly including
  numerator/denominator placement; Eqs. 6, 7, 10, 11 spot-checked. The reading of **Eq. 8 as "distance
  ÷ mean speed" was explicitly confirmed**.
- **19 of 20 quotations verbatim**; **every reference number** checks out against the bibliography.
- **Both upstream corrections verified and cleared to send**: the exercise-not-dance finding (word
  counts: "dance" ×2, both in the same motivating list; "exercise" ×29) and the `d = 72 (2 × 3 × 13)`
  arithmetic error (78 is the likely intended value).
- The preprint-vs-typeset determination, and the Limitations claims on significance testing,
  single-subject data, de-duplication loss, recognition never being measured, and the dimensionality
  inconsistency.

**Corrections it produced, all applied above**
1. Cross-reference fixed: `paper_chain.md` has no section R10-5 → now cited as **R9-5 item 1 / R10-4
   item 5**.
2. A quote had been silently spell-corrected → restored as **"Multiple occurances [sic] … a single
   occurance [sic]."**
3. `E_T` space ambiguity surfaced: §3.2.3 says "configuration space", Figs. 4 & 10 captions say
   "**augmented** configuration space" → now flagged rather than asserted.
4. Dropped hedge restored: "resolves ambiguities" → **"helps resolve ambiguities"**.
5. Mis-attribution fixed: hand-coded grammars were **only** Bobick & Ivanov [4], not the whole
   dance/aerobics/sign-language literature [6, 20, 21], which used phase-space constraints or HMMs.
6. Dropped hedge restored: HMM topology "must be fixed in advance" → **"often highly constrained prior
   to training"**.
7. Symbol collision removed (τ had been used for both the transition function and template sequences),
   plus a caveat that Greek glyphs are unrecoverable from this PDF's text layer.
8. Overstatement softened: "vocabulary sizes are unjustified" → 71/87 are **outputs of the VQ of [13]**,
   whose own parameters are unreported.
9. "List of figures" located correctly (p. 23, after references, before the plates, pp. 24–33).
10. Bibliographic header now attributed to `paper_index_A.csv`, since none of it appears in the file.

**Overstatements it caught and forced down**
- **E2 "supplies every hyperparameter needed"** → four specific parameters are *not* supplied (VQ
  parameters, velocity-threshold value, template-cluster count m, §4.4 unseen-event threshold).
- **λ coupling** → the §4.1 threshold uses the *unscaled* `|Ċ_t|`, so λ's effect on segmentation is
  **indirect** (via which prototypes exist), not the direct shared-term coupling originally claimed.
- **"Test material is the same routine as training"** → fully supported for dataset 1 only; for
  dataset 2 no difference from training is stated at all.
- **Eq. 14** → sharpened to note the paper itself hedges ("approximate", "relative probability"),
  making this presentational rather than an error.
- **"No code/data release"** → reframed as an artefact-availability note, not a 2001 methodological
  defect.

**Omissions it caught, all now added**
The 20 ms / ~1 s time scales from §1; Figure 7 (the qualitative prediction result); the §4.2-vs-§4.5
contradiction over the level-2 alphabet; the §1 "cross-entropy" vs §3.1 "weighted KL" wording;
attribution of the prefix tree to [9]; Fig. 9's "every second frame of the first 700 frames"; dataset
attribution for Figs. 6 (dataset 2, N = 4) and 9 (dataset 1); and the H-Anim 1.1 / "Baxter" provenance
from the Acknowledgments. It also flagged the narrower §3.2.2 sense of "recognition mode", and the
generic-plural "individuals" framing against the single-individual training data — both now
distinguished in the text.

**Scope note:** the auditor correctly objected that a remark about the `notebooklm` MCP server failing
in this run is a claim about the session, not the paper. It has been moved out of this summary into
the run report.

**Residual unverified items** (stated plainly rather than resolved):
- Figure *curve magnitudes* — no rasteriser available in this environment, so only the authors'
  textual ordering claims are reported.
- Section and equation *numbering* against the published CVIU version.
- The paper's own Greek symbol names.
- "Double-spaced" in the version caveat is an impression from line spacing, not a measurement.
