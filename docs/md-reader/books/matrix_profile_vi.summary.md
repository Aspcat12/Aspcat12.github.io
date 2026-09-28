# Yeh, Kavantzas & Keogh (2017) — Matrix Profile VI: Meaningful Multidimensional Motif Discovery

Chin-Chia Michael Yeh, Nickolas Kavantzas, Eamonn Keogh · University of California, Riverside + Oracle Corporation
IEEE ICDM 2017, pp. 565–574 · DOI 10.1109/ICDM.2017.66
*(venue / pages / DOI taken from `paper_notes/paper_index_B.csv` row B1-15 — **none of it appears anywhere in the local PDF**, which carries no conference header, no page numbers, no copyright line)*
Local file: `knowledge/reading_docs/matrix_profile_vi.pdf` (10 pages)
Read: 2026-09-16 · Method: Three-Pass (Keshav) per `knowledge/reading_guide.md` · verified by an independent second pass (§9)
Checklist position: **TIER 1, item #10 (B1-15)** — flagged as *both* a read and an experiment (E1), carried for 3+ runs

> **Extraction note.** `pdftotext -layout` gives clean prose but **silently drops every math glyph**
> (the complexity bound renders as `( log   )`). `pypdf` recovers them as Unicode math-italic
> (`𝑂(𝑑 log 𝑑 𝑛²)`). **Every symbol and every complexity bound below was re-extracted with `pypdf`,
> not with `pdftotext`.** If a future run quotes notation from this paper using only `pdftotext`,
> it will quote holes — and not merely cosmetic ones: `pdftotext` renders **Algorithm I line 14**
> (`𝐷′′ ← 𝐷′ ÷ 𝑖`) as an empty cell, silently deleting the normalisation step that makes the whole
> selection method work (§2.2, §6.13). The first draft of this summary got that wrong for exactly
> that reason; the verification pass (§9) caught it.
>
> **Figures-only evaluation.** Like Galata et al. (2001), this paper reports *every* experimental
> result as an unlabelled or sparsely-labelled plot. There is **not a single table of numbers in the
> paper.** The only exact numeric results stated in running text are: the −0.0052 correlation, the
> "eight additional irrelevant dimensions" claim, "about 22 of the 45" pairwise correlation
> combinations, the ~2-hour/525,600-point runtime estimate, and the F-measure of 0.88. Axis endpoints below (e.g. "~600 s at d = 250") are **axis maxima read off plots**, not
> measured values, and must never be cited as reported runtimes.

---

## Five Cs (pass 1)

- **Category** — Research prototype + experimental evaluation, with a strong negative-result component.
  Half the paper's force is the *demonstration that the existing problem formulation is wrong*
  (all-dimensions motif search), and half is the algorithm that replaces it.
- **Context** — Sits on top of the authors' own Matrix Profile line: Matrix Profile I (STAMP) [26],
  II (STOMP / GPU-STOMP) [28], III (visualisation) [27], and SiMPle [16] for music. It is explicitly
  positioned against four prior multidimensional-motif efforts — Minnen et al. [18] (closest in
  spirit; first to note the harm of irrelevant dimensions), Tanaka et al. [22] (project MTS down to
  1-D, MDL-based), Vahdatpour et al. [24] (per-dimension motifs stitched by clustering), and
  Balasubramanian et al. [1]. Method components are borrowed rather than invented: MASS [17] for
  distance profiles, Rissanen's MDL [14], Thorndike's elbow [23], Salvador & Chan [15] for automatic
  elbow location, and the must-link/cannot-link analogy from constrained clustering [25].
- **Correctness** — The core algorithmic claim (that column-wise sort + column-wise cumulative sum
  over the per-dimension distance matrix yields the *exact* k-dimensional distance profile for all k
  at once) is argued directly from non-negativity of the z-normalised Euclidean distance and is
  sound. The weak links are all in the *evaluation*: the rival baseline in the headline accuracy
  figure is a **proxy**, not a reimplementation (see §6), and the one quantitative real-data result
  (F = 0.88) depends on an **oracle stopping point** that the paper itself admits is unobtainable.
- **Contributions** — (1) The negative result: all-dimension motif search is meaningless once a
  handful of irrelevant dimensions are present, quantified. (2) **mSTAMP**, which computes the
  k-dimensional matrix profile for *every* k ∈ [1, d] simultaneously, exactly, in 𝑂(𝑑 log 𝑑 · 𝑛²)
  time and 𝑂(𝑑𝑛) space. (3) The **k-dimensional matrix profile subspace**, which records *which*
  dimensions each motif lives in. (4) Constrained search (include/exclude dimension sets).
  (5) An MDL-based rule for choosing the "natural" k without user input, plus an iterative variant
  for top-K. (6) Case studies in mocap, music, electrical load, and activity monitoring.
- **Clarity** — Very readable; the argument is built from a single running example carried through
  Figs. 2, 3, 4, 6, 7. Two genuine notation slips (Def. 12 and the P-vs-matrix shape mismatch) are
  noted in §6. The near-total absence of numeric tables is the main clarity failure.

## Extraction table (อ.Proadpran)

| ช่อง | สรุป |
|---|---|
| **Motivation** | Analysts know motifs exist in *some* subset of a many-channel time series but do not know which channels, or even how many. Every existing multidimensional motif algorithm searches all dimensions, and "using all dimensions will generally not produce meaningful motifs, except in the most contrived situations." The concrete driver is industrial: an oil distillation column has "well over a hundred time series," but the "rainstorm" motif "may only show up on the `{temp, pressure, flowrate}` tags". |
| **Research question** | Can we find, exactly and scalably, the motif that lives in the *best k-of-d dimensional subspace* — including the case where k itself is unknown and must be inferred? |
| **Proposed method** | **mSTAMP**: for each query subsequence, compute the *per-dimension* distance profile into a d × (n−m+1) matrix `D`; sort each column ascending; take the column-wise cumulative sum. Row k of that cumulative sum, **divided by k** (Algorithm I line 14), is what gets stored: the k-dimensional distance of Def. 9 is the *sum* of the k smallest per-dimension distances, but the profile records their *mean*, which is what makes values comparable across k. Update d matrix profiles elementwise. Record which dimensions were selected → *matrix profile subspace*. Choose k by **MDL** (minimum bits to difference-encode the motif pair). |
| **Evaluation** | (a) Scalability plots vs subsequence length m, series length n, dimensionality d; (b) anytime-convergence RMSE; (c) synthetic accuracy vs number of irrelevant dimensions (40 trials), mSTAMP+MDL vs all-dimensions; (d) four qualitative/semi-quantitative case studies: CMU mocap boxing, Rick Astley Mel-spectrogram, UK household electrical load, PAMAP2 activity monitoring (F-measure 0.88). |
| **Contribution** | Reframes multidimensional motif discovery as a *subspace* problem; delivers the first exact algorithm for it; makes the number of relevant dimensions an output rather than an input; and inherits anytime/incremental/GPU properties from the Matrix Profile family. |

---

## 1. Problem and motivation

A time series motif is "the most similar subsequence pair of a time series" (Def. 3). Motifs are
useful because "if a time series pattern is conserved, we may assume that there is some high-level
atomic mechanism/behavior that causes that pattern to be conserved" — and motif discovery is
therefore "often the first step in various kinds of higher-level time series analytics."

The paper's opening figure is **motion capture**. Two boxing traces: the top is a cross, the bottom a
one-two combo. "If we focus solely on the boxer's dominant hand, the two behaviors are almost
identical. However, if we look that the full set of Mo-Cap markers on all of the limbs, the
differences in the non-dominant hand and in the footwork 'swamp' the similarity of the punch, making
this repeated behavior impossible to find with the classic multidimensional motif discovery
algorithms, that use all the available dimensions." *(quoted verbatim, including the paper's own
typo "look that the".)*

### 1.1 The quantified decay — the number that matters most

Using the synthetic running example of Fig. 2 — a 30-point motif implanted at positions 150 and 350
in dimensions `T1` and `T2`, with all remaining dimensions pure random walks:

- Searching only `{T1, T2}` finds the motif correctly.
- Adding **one** random walk: still robust — "the signal of the true subset {T1,T2} is strong enough
  to resist the irrelevant information added by a single random walk."
- **"empirically averaging over 100 trials, we have found that if there are eight additional
  irrelevant dimensions, then we do about as well as random chance."**

And a critical aggravating clause that is easy to miss: **"the above motifs make up about 5% of the
data. However, motifs are often much rarer, which accelerates the rate at which increasing
dimensionality masks motifs that exist in a subspace of the data."** So *eight* is an optimistic
bound obtained at a generous motif density; realistic motif rarity makes the collapse faster.

### 1.2 Three query types the framework must support

- **Guided search** — best motif on k dimensions, k given by the user, but *which* k unspecified.
  The paper's example (§IV.E) is a twelve-dimensional MFCC representation of a musical performance:
  the user "can be sure that the motif will span about three dimensions, but which three depends on
  whether the instrument is a soprano, alto, tenor, baritone, or bass saxophone" [11].
- **Constrained search** — same, but with an explicitly included or excluded dimension subset.
- **Unconstrained search** — k is *not* given; the algorithm must pick the "natural" subset.

"The first two tasks mostly reduce to questions of speed and scalability; the last task is subtler,
requiring us rank different tentative solutions and return the most natural one."

### 1.3 Motif length changes which dimensions matter

An underrated point: "the important dimensions for the motif depend on the user-specified motif
length. In such datasets, a motif query of one hour may turn up the thunderstorm example, but a motif
query of length one day may find the motif representing a monthly calibration/cleaning run, which
affects many more dimensions." **The subspace is a function of m.** This matters directly for us
(§7.2).

### 1.4 Two apparent solutions the paper dismisses

Section II.A pre-empts the obvious cheap fix — use **correlation** (or any measure of mutual
dependence) between channels to pre-select the subspace. It does not work: the correlation between
`T1` and `T2` — the two channels that genuinely share the motif — is **−0.0052**, effectively zero.
Worse, "if we create 10 random walks of the same length, then on average, we expect that about **22
of the 45** pairwise combinations will have a higher correlation." The stated reason is the general
principle of the paper: **"We are interested in repeated local patterns; statistics about global
tendencies are unlikely to be informative."**

---

## 2. Core contribution and method

### 2.1 Definitions (Defs. 1–13)

Defs. 1–5 are standard Matrix Profile machinery: time series `T`, subsequence `T_{i,m}`, motif pair
(Def. 3, under z-normalised Euclidean distance), **distance profile** `D` (Def. 4, computed via
MASS [17]), and **matrix profile** `P` (Def. 5) — a meta time series storing, for each subsequence,
the distance to its nearest neighbour. The motif is the two lowest (tying) values in `P`.

Defs. 6–8 lift these to the multidimensional case: multidimensional time series `T ∈ ℝ^{d×n}`,
multidimensional subsequence `T_{i,m}`, and the key new object, the **subdimensional subsequence**
`T_{i,m}(X)` where `X` is an indicator vector with `‖X‖₀ = k`.

**Def. 9 — k-dimensional distance:**

> `dist⁽ᵏ⁾(T_{i,m}, T_{j,m}) := min_X dist(T_{i,m}(X), T_{j,m}(X))`, where `‖X‖₀ = k`.

i.e. the distance using only the **best** k of d dimensions — best *for that specific pair*.

Defs. 10–12 lift distance profile, motif, and matrix profile accordingly. **Def. 13 — k-dimensional
matrix profile subspace** — "a multidimensional meta time series that stores the selected k dimension
for each subsequence when computing the distance with others." This is the object that answers
"*which* joints/channels", and it is the part that matters most for our project.

### 2.2 The mSTAMP algorithm (Algorithm I)

The naïve route — compute a matrix profile for all `C(d,k)` dimension combinations — is
"only computable for trivially small datasets due to the combinatorial explosion."

mSTAMP instead computes the k-dimensional matrix profile **for every k from 1 to d simultaneously**,
in **𝑂(𝑑 log 𝑑 · 𝑛²) time and 𝑂(𝑑𝑛) space**. The main loop, per query subsequence `T_{i,m}`:

1. **Lines 5–8** — compute the *per-dimension* distance profile for each of the d dimensions, stacking
   them into a matrix `D` of shape d × (n−m+1). Row j of `D` is a **1-dimensional** distance profile
   (Def. 4), not a k-dimensional one.
2. **Line 10** — **column-wise ascending sort** of `D`.
3. **Lines 12–15** — **column-wise cumulative sum**, then **divide by k**
   (line 13 `𝐷′ ← 𝐷′ + 𝑫[𝑖,:]`, **line 14 `𝐷′′ ← 𝐷′ ÷ 𝑖`**), then elementwise-min `𝐷′′` into
   `P[k, :]`. After adding row k, `𝐷′` is the k-dimensional distance profile in the sense of Def. 9
   (a *sum*), but what is stored is `𝐷′′`, the **per-dimension mean**.

> **Do not skip the ÷ k.** It is the step that makes matrix profile values **commensurable across
> k**, and therefore the step that makes the elbow plot of Fig. 6 and the whole unconstrained search
> meaningful — a raw sum would grow with k almost mechanically and no elbow would be interpretable.
> It is also the one line `pdftotext` deletes entirely. Def. 9 (sum) and Algorithm I line 14 (mean)
> are **not** the same quantity, and the paper never flags the discrepancy (§6.13).

**Distance-profile choice is coupled to the anytime property.** If queries are processed in *random*
order (which gives the anytime behaviour), **MASS** [17] is used, at 𝑂(𝑛 log 𝑛). If processed *in
order*, Zhu et al.'s STOMP method [28] is used at 𝑂(𝑛), which is faster but "nullifies the
anytime-algorithm property." This is a real trade-off the user must make, and it is stated only in
passing.

### 2.3 Why it is exact (§IV.B)

The argument is one paragraph and is convincing: because the z-normalised Euclidean distance is
non-negative, every entry of `D` is non-negative. The **1-dimensional** distance profile is therefore
the smallest value in each column of `D`; the **2-dimensional** one is the sum of the two smallest;
and in general the k-dimensional one is the sum of the k smallest. Column-wise sort plus column-wise
cumulative sum produces exactly that, for all k, in one pass — the paper's own phrasing is that
"the combinatorial search space can be searched efficiently and **admissibly in a greedy fashion**."
**No approximation.** (The value then stored is the mean, per line 14; the exactness argument is
about `𝐷′`, the sum.)

> **Inference (mine, not stated in the paper):** the stored k-dimensional matrix profile value is
> **monotonically non-decreasing in k**. For the *sum* this is immediate (a non-negative term is
> added); for the *mean* actually stored it still holds, because the k-th smallest per-dimension
> distance is ≥ each of the previous k−1 and therefore ≥ their mean, so appending it cannot lower the
> mean. This is *why* an elbow/MDL rule is needed at all: you cannot simply minimise the profile
> value over k, because k = 1 would always win. The paper never states it, but every one of its
> selection figures (Figs. 6, 16) depends on it. Worth stating explicitly if we cite this method.

### 2.4 Expressiveness — a lower-dimensional motif need not be a subset of a higher one

Fig. 5 gives a three-channel counterexample: the best 3-dimensional motif pair occurs at times '3'
and '4' across all three series, but the best 2-dimensional motif pair occurs at times '1' and '2' in
just channels B and C. **Different locations, not just fewer dimensions.**

The paper is candid about the cost: "This property is unfortunate, since it excludes the possibility
to use various pruning and dynamic programing techniques to speed up the computation. However, as we
will see, it is this expressiveness that allows the discovery of semantically meaningful motifs in
high-dimensional data."

### 2.5 Constrained search (§IV.D)

- **Exclusion** (blacklist) — trivially implemented: drop those dimensions before calling mSTAMP.
- **Inclusion** (whitelist) — harder: after the column-wise ascending sort (line 10) you must
  **move the whitelisted dimensions' distances up to the front**, so the cumulative sum always
  includes them.

Explicitly analogised to "must-link" and "cannot-link" in constrained clustering [25]. The motivating
example came from Dr. John Criley (UCLA School of Medicine): a cardiologist hunting predictors of
Pulsus Paradoxus may insist on **including** `RESPIRATION`; a neurosurgeon on the same sleep-study
archive may **exclude** one of the two `ELECTROOCULOGRAM` channels, "Because the two eyes typically
move in tandem, they are redundant, and the pairing of {EOGleft, EOGright} will tend to report a
strong, but spurious 2-dimenional motif."

> **This redundancy trap is the single most transferable warning in the paper for us.** Two channels
> that move together produce a strong low-k motif that is an artefact of redundancy, not of behaviour.
> Our feature files are full of exactly such pairs (see §7.3).

### 2.6 Unconstrained search and the MDL rule (§IV.E)

The selection score is **the matrix profile value of each k-dimensional motif**, plotted against k
(Fig. 6); the elbow marks the natural dimensionality. In the running example (2 signal + 4 random
walk dimensions), "the matrix profile value for 3-dimensional motif is noticeably greater than the
2-dimensional motif's matrix profile value," correctly recovering k = 2.

To automate the elbow, the paper uses **MDL** [14]: "the model, that allows the observed data to be
compressed the most, is likely to be the true model. In other words, the MDL principle has cast the
elbow-finding problem into a maximum compression (or minimum model size) finding problem."

**The worked encoding example (the only fully-numeric worked example in the paper):**

A time series `T` is encoded by storing its difference from a **reference time series** `Tᵣ`:

```
T   = 1 2 0 12 4 5 2 1 10 15     (4-bit integers)
Tᵣ  = 1 2 0 11 4 5 1 0 10 15
```
Storing both directly: 20 × 4 bits = **80 bits**. The difference
`𝛥 = T − Tᵣ = 0 0 0 1 0 0 1 1 0 0` contains only 0s and 1s, "so we can use 10 1-bit integers to
store `𝛥`, and compression can be achieved by storing the same information indirectly with **`Tᵣ` and
`𝛥`** (which requires **50 bits** to store)". (Encoding scheme "similar to the difference-encoding
scheme used in [27]".)

Applied here: for each k, difference-encode the motif *pair* over the subspace that the k-dimensional
matrix profile subspace reports, and take the **k with minimum bit cost** (Fig. 7 — minimum at k = 2,
matching the ground truth).

**Iterative top-K.** When several meaningful motifs of different dimensionality coexist, apply MDL
repeatedly: (1) find the minimum-bit-size k-dimensional motif, (2) set the matrix profile values of
that motif **and its trivial match** to infinity, repeat. Applied to Fig. 5's data, the 3-dimensional
motif is found first, the 2-dimensional one second. **The termination condition is only half-specified**: "it can be
either be an input for the user or a more advanced technique could be applied. Due to space
limitations, we will have to leave the discussion on termination condition to future works." A
user-supplied stopping count *is* offered; what is left to future work is an **automatic** rule —
which, as §6.3 notes, is the hole the F = 0.88 result falls through.

The paper also recommends a human safeguard (stated later, in §V.A, after the Fig. 12 experiment):
"Becase the multidimensional matrix profile is already
computed exactly for the MDL-based algorithm, a manual inspection of the matrix profile value curve
(see Fig. 6) could also be performed as a safeguard measure." *(typo "Becase" is the paper's.)*

---

## 3. Experimental evaluation

**Setup.** Intel® Xeon® E5-2620 v3 @ 2.40 GHz; MATLAB implementation, with a Python version also
released. All data, code and supporting videos at the project site [19]
(`https://sites.google.com/view/mstamp/`). Stated experimental philosophy: "We have designed all
experiments such that they can be easily reproduced."

### 3.1 Scalability (synthetic)

| What was varied | Fixed | Result |
|---|---|---|
| Subsequence length m, 100 → 900 (Fig. 8) | d = 4, n = 2¹⁴ | **Flat.** "the change of subsequence length does not impact the runtime". y-axis ticks 0 / 4 / 8 **sec** |
| Series length n, ~100k → 900k (Fig. 9) | d = 4, m = 256 | **Quadratic**, matching STOMP [28]. y-axis ticks 0 / 4 / 8 **hour** |
| Dimensionality d, up to 250 (Fig. 11) | n = 2¹⁴, m = 256 | **Linearithmic**, matching the 𝑂(𝑑 log 𝑑 · 𝑛²) bound. y-axis ticks 0 / 200 / 400 / 600 **sec** |

⚠️ Those are **axis maxima**, not measured endpoints — the text layer does not say where the curves
actually land, and Fig. 8's curve is explicitly flat. Cite them as the range of the plot, never as
"mSTAMP took 8 hours / 600 seconds".

The m-invariance is flagged as the remarkable one: "We can perform motif search with complete freedom
from the curse of dimensionality (unlike everywhere else in this paper, here the term dimensionality
is used to denote subsequence length) that plagues all other approaches."

**The one concrete runtime figure in the paper:** an oil distillation column with four dimensions
sampled once per minute gives **525,600 data points for a full year**, and Fig. 9 "indicates that it
will take about **two hours of CPU time**" to find motifs in it.

**Anytime convergence (Fig. 10).** On a 3-dimensional series with a 2-dimensional motif embedded,
RMSE against the exact matrix profile "decreases quickly in the first few percent of iterations.
After only **10 percent** of the computations have been completed, the current 'best-so-far' matrix
profile is not only visually similar to the exact matrix profile … but the RMSE is also very low."

### 3.2 Accuracy vs irrelevant dimensions (Fig. 12) — the headline result

- Task: recover an embedded **4-dimensional** motif hidden among multidimensional random walks.
- Irrelevant dimensions swept **1 → 256**. Results **averaged over forty trials**.
- Compared: MDL-based mSTAMP vs "the original matrix profile by using all dimensions."
- Result: "The MDL-based algorithm almost always finds the correct embedded motif, while the all
  dimensions algorithm failed in most cases. Even if we increase the number of irrelevant dimensions
  to **64 times** the number of relevant dimensions, the accuracy is still **near perfect**."

**Read the baseline carefully.** The all-dimensions curve is *not* [1], [18], [22] or [24]. The paper
justifies the substitution: "Note the latter is an upper bound for the performance of all known rival
methods [22] that use all dimensions, since they are using all dimensions, and are approximate."
That is a reasonable argument — an exact all-dimensions method should beat an approximate one — but
it means **no rival system was actually run.** See §6.

### 3.3 Motion capture case study (§V.B) — the one that concerns us

- Data: **CMU Motion Capture Database** [6], **subject 13**, "performs various boxing moves for
  40 seconds", **38 dimensions, each corresponding to the motion of a given joint**.
- **All 38 dimensions:** the discovered motif pair is semantically wrong — "the subject is performing
  an uppercut punch in one of the snippets, but the other snippet consists of blocking/dodging
  motion."
- **mSTAMP, k = 3:** "the motif pair discovered consists of the subject performing a cross and a
  one-two combo. Our algorithm matches a simple cross with the cross in a one-two combo, and the
  three matching dimensions are from joints in the **right humerus** (right upper arm), **right
  radius** (right forearm), and **left femur** (left upper lag)." *(typo "lag" is the paper's.)*

Note the third dimension: **left femur**, a *leg*, paired with two right-arm joints. The natural
subspace of a punch is therefore not "the arm". *(Inference, mine: the obvious reading is that weight
transfer through the opposite leg is part of the motif — but the paper only lists the three joints
and offers no biomechanical explanation, so do not attribute that reasoning to it.)* Either way, this
is a caution against hand-picking "obviously relevant" limbs.

The stated downstream payoff is animation: the subspace motif "allows the construction of a seamless
motion graph after blending all other limbs [10]" — i.e. mSTAMP is presented as a tool for building
**better motion graphs** (Kovar, Gleicher & Pighin [10]), which is squarely adjacent to our pipeline.

### 3.4 Music processing (§V.C)

- Data: Mel-spectrogram of *Never gonna give you up*, Rick Astley. MIR-standard parameters:
  **46 ms STFT window, 23 ms hop, 32 Mel-scale triangular filters**. Subsequence length **5 seconds**.
- **All 32 dimensions:** motif = the **chorus** (consistent with SiMPle [16]).
- **k = 1 and k = 2:** motif = the **drum pattern**, living in "the two lowest frequency bands (i.e.,
  typical frequency range for percussion), which confirms our intuition."

The methodological point: "Once the multidimensional matrix profile is computed, users can explore
the matrix profile for different dimensionalities **without additional computational cost**." One run,
many answers, at different semantic granularities — chorus at high k, rhythm at low k.

### 3.5 Electrical load measurement (§V.D)

- Data [21]: UK household appliance-level loads plus an aggregate. Five appliances: fridge-freezer,
  freezer, tumble dryer, dishwasher, washing machine. **19 April 2014 – 15 May 2014**, length
  **17,000**. Subsequence length **4 hours**.
- Unconstrained search → natural dimensionality **k = 2**, and the two dimensions are **tumble dryer
  and washing machine** — "Since both machines are typically used one after another in a short window
  of time, it is not surprising that the discovered 2-dimensional motif spanned the use of these
  related appliances."

A clean sanity check: the algorithm recovered a subspace whose semantics are verifiable by common
sense without ground-truth labels.

### 3.6 Physical activity monitoring (§V.E) — the only quantitative real-data number

- Data: **PAMAP2** [13], **subject 101**. Channels: a heart-rate monitor plus **three IMUs** (wrist,
  chest, ankle), each measuring temperature, 3-D acceleration, 3-D gyroscope, 3-D magnetometer.
- Activities: lying, sitting, standing, walking, running, cycling, Nordic walking, ascending stairs,
  descending stairs, vacuum cleaning, ironing, rope jumping.
- Hypothesis: the first three (lying, sitting, standing) are "more about the subject's passive posture
  rather than his or her action. As there are little or no repeated motion when the subject is not
  moving, the motif pairs that exist within these temporal regions should be less similar (and less
  meaningful)". So if iterative MDL retrieves motifs in similarity order, **dynamic** activities
  should rank above **passive** ones.
- Result (Fig. 17): the ordering "largely coincides with our speculation." At the optimal stopping
  iteration, **F-measure = 0.88**.
- **The paper's own caveat, verbatim:** "Although the result F-measure is impressive given such
  simple MDL-based method, we cannot know the optimal stopping iteration without consulting the
  ground truth label. The F-measure provided here is for gauging the potential of the mSTAMP-based
  motif discovery framework."

---

## 4. Related work as the paper frames it

| Work | What it does | The paper's objection |
|---|---|---|
| **Minnen et al. [18]** (ICDM 2007) | "closest in spirit"; **first to note the detrimental impact of irrelevant dimensions**; subdimensional motifs | Approximate. "Even in an ideal case, with just six dimensions, they report 'with no noise, (our approach) achieves roughly 80% accuracy.'" Robust only to "a small number of smooth, but irrelevant dimensions, or just one noisy irrelevant dimension" |
| **Tanaka et al. [22]** (Mach. Learn. 2005) | Projects MTS to 1-D, then MDL-based motif search | "requires all (or at least most) of the dimensions to be relevant, as the algorithm is brittle to even a handful of irrelevant dimensions"; **five parameters** to tune |
| **Vahdatpour et al. [24]** (IJCAI 2009) | Per-dimension motifs "stitched" by clustering; medical monitoring | Never exceeded **85 %** accuracy across three domains, with at most **three** irrelevant dimensions (vs a **17 %** single-dimension strawman); **seven parameters** |
| **Balasubramanian et al. [1]** (2016) | Multidimensional motifs in physiological signals | Grouped with the rest: slow, approximate, brittle |
| **Berlin & Van Laerhoven [4]** (UbiComp 2012) | Dense motif discovery for leisure activities | Scales via piecewise-linear approximation → approximate |
| **Matrix Profile I/II/III [26][27][28]** | The parent data structure; STAMP, STOMP, GPU-STOMP | **Not objected to — inherited.** The paper is emphatic that speed "is simply a property we inherit from the use of the matrix profile [27], which is not a claimed original contribution" |
| **SiMPle [16]** (ISMIR 2016) | Matrix Profile for music similarity | Extended, not criticised; §V.C's all-dimensions chorus result is noted as consistent with it ("it is unsurprising that the motif we discovered is the chorus of the song [16]") — a consistency remark, not a replication |
| **Hu et al. [9]** (ICDM 2013) | Multi-dimensional streaming TS **classification** | Cited as making the same "don't use all dimensions" observation "forcefully", in the classification setting |
| **Kovar et al. [10]** / Beaudoin et al. [2] | Motion graphs / motion-motif graphs | The **downstream application** the mocap case study serves |

Summary judgement: "all current multidimensional motif discovery algorithms in the literature are
slow, approximate, and brittle to irrelevant dimensions. In contrast, we desire an algorithm that is
fast, exact, and robust to hundreds of irrelevant dimensions."

---

## 5. Assumptions

1. **Motif = the single most similar pair.** Not a motif *set*, not a frequency-based motif.
   Repetition count plays no role. Def. 5 notes that "other definitions of motifs (range motifs, top-K
   motifs etc.) can also be extracted trivially from the matrix profile [27][28]" in the *univariate*
   case; in the **multidimensional/MDL** setting the only top-K mechanism offered is the iterative
   masking heuristic of §IV.E.
2. **z-normalised Euclidean distance, per dimension.** Each channel is z-normalised independently,
   so per-channel amplitude is discarded and channels on wildly different scales are made comparable.
   This is what makes the "sum of the k smallest" formulation legitimate — and it also means the
   method cannot see *magnitude* differences between occurrences.
3. **Equal weighting across dimensions.** The k-dimensional distance is an *unweighted* sum of the k
   smallest per-dimension distances (stored as their mean, §2.2). No channel can be down-weighted,
   only included or excluded.
4. **The best subspace is chosen per pair** (Def. 9 minimises over X for each `(i, j)`). The
   subspace is therefore *not* globally fixed; different positions in the matrix profile may report
   different dimension sets. Def. 13 exists precisely because of this.
5. **Fixed subsequence length m**, supplied by the user, uniform across all dimensions — and §1.3
   establishes that the answer *depends on it*.
6. **Time-aligned, equal-length, uniformly-sampled channels.** No lag between channels is modelled: a
   motif in which the arm leads the leg by 0.2 s is not a motif here.

## 6. Limitations and weaknesses (what to say when we cite it)

**Evaluation weaknesses — these are the ones a reviewer would attack:**

1. **No rival system was ever run.** Fig. 12's comparator is "the original matrix profile using all
   dimensions," justified as an *upper bound* on rival methods — though the sentence doing the
   justifying cites only **[22]**. The argument is defensible, but the speed claim is made twice —
   "at least two orders of magnitude faster than [1][18][22][24]" (§III) and "orders of magnitude
   faster than existing works [1][18][22][24]" (§III) — and **neither is supported by a measurement
   anywhere in the paper**. No rival runtime is reported. Do not quote that speedup as measured.
2. **No tables. Anywhere.** Every result is a plot, several with only two or three axis ticks. Exact
   values for Figs. 6, 7, 8, 9, 10, 11, 12, 16, 17 are not recoverable from the paper.
3. **The 0.88 F-measure needs an oracle.** The paper says so itself (§3.6). Since an *automatic* termination
   condition is "left to future works", the headline number is not achievable without ground-truth
   labels or a user-supplied stopping count.
   **This is the number most likely to be mis-cited, including by us.**
4a. **The mocap success story carries its own caveat**, easily missed: Fig. 13's caption notes "how
   the right arm of the subject is in a different position in latter frames within different
   occurrences of the motif." The matched pair is not identical even on the dimensions that were
   selected.

4. **Three of four case studies have no quantitative evaluation** — mocap, music and electrical load
   are all assessed by the authors' own semantic inspection — "we visually examined the video
   snippet" (§V.B); "we have examined the dimensions spanned by the 2-dimensional motif" (§V.D).
   Persuasive, but not measured, and not blind.
5. **Synthetic accuracy uses random walks as the irrelevant dimensions.** Real irrelevant channels
   are often *structured* (periodic, drifting, sensor-artefacted) and may produce spuriously good
   low-k matches far more readily than a random walk does. The paper acknowledges the failure mode in
   §V.A, when motivating the Fig. 12 experiment — "this could happen if the motifs are subtle and the large number of irrelevant
   dimensions happens to produce a spuriously similar pair of subsequences" — but never tests it.

**Method-level limitations:**

6. **𝑂(𝑛²) in series length.** Mitigated (GPU, anytime, incremental) but not removed.
7. **Pruning and dynamic programming are ruled out** by the paper's own Fig. 5 argument (§2.4) — the
   wording is that it "excludes the possibility to use various pruning and dynamic programing
   techniques", i.e. that class of speed-ups, not a general impossibility proof.
8. **Parameter-count claim is softened by m.** The abstract advertises "requiring fewer parameters",
   and relative to [22]'s five and [24]'s seven that is true — but m remains, and §1.3 shows the
   *answer changes* with m. In practice a user sweeps m, which restores much of the burden.
9. **Redundant channels manufacture spurious low-k motifs** (the EOG example, §2.5). The algorithm
   has no internal defence against this; the only remedy offered is a human-supplied exclusion list.
10. **MDL encoding details are thin.** The worked example uses 4-bit integers and a difference
    encoding "similar to" [27]; the paper does not specify the discretisation cardinality used in its
    own experiments, which is a real reproducibility gap for the MDL step.

**Notation slips (minor, but relevant if we quote definitions):**

11. **Def. 12** states that "the 𝑖 th position in 𝑃 stores `dist⁽ᵏ⁾(T_{i,m}, T_{j,m}) ∀ j ∈ [1,…,n−m+1], where i ≠ j`" — a scalar position cannot store a value for all j. The preceding prose
    ("nearest neighbor") makes clear a `min_j` is intended, but the formal statement is ill-formed.
12. **Def. 12 declares `P ∈ ℝ^{n−m+1}`** (a vector), while Algorithm I's Output line and line 1 use
    `𝑷 ∈ ℝ^{d×(n−m+1)}` — a **matrix** holding every k simultaneously. Both are "the k-dimensional
    matrix profile" in the text. Say which you mean when citing. **Def. 13** has the same problem: it
    declares the subspace `𝑺 ∈ ℝ^{k×(n−m+1)}` for a *single* k, while Algorithm I computes all k at
    once — and Algorithm I **omits the subspace bookkeeping entirely** ("To simplify the
    presentation, we omit the operations related to storing of the k-dimensional matrix profile
    subspace"). Since §7 leans on the subspace object, note that **the paper never gives pseudocode
    for producing it.**

13. ⚠️ **Def. 9 and Algorithm I disagree about what the profile stores.** Def. 9 defines the
    k-dimensional distance as the **sum** of the k smallest per-dimension distances; Algorithm I
    line 14 divides by k, so what is stored, plotted in Figs. 6 and 16, and fed to the elbow/MDL
    rule is the **mean**. The paper never acknowledges the discrepancy. It is not a harmless
    normalisation — comparability across k is the whole basis of the selection method — and it is
    the single most important thing to get right when reimplementing or when comparing against a
    library's output.

---

## 7. What this means for our project

### 7.1 The threat named in the checklist is real, and the paper is sharper than our note

`reading_checklist.md` #10 records the risk as: *we cluster over all 33 landmarks, so arm/hand
structure may be swamped by legs and torso.* The paper supports that, but with three refinements our
notes did not have:

- The decay is **quantified** — 8 irrelevant dimensions ⇒ chance-level — and the "**about 5% of the
  data**" clause means that bound is *optimistic* for rarer motifs. Thai classical gesture motifs are
  plausibly rarer than 5 % of a clip.
- **Correlation-based channel pre-selection is explicitly ruled out** (§1.4). If we were tempted to
  drop "redundant" features by correlation before clustering — a natural instinct — this paper says
  that is unprincipled for *local repeated pattern* discovery. `−0.0052` between the two channels
  that actually share the motif is the counterexample.
- **Redundant channel pairs create spurious motifs** (EOG). This is the *opposite* failure from
  swamping and we had not recorded it at all.

### 7.2 Three corrections to the queued E1 experiment

The checklist's **E1** reads: *"`pip install stumpy` → `stumpy.mstump` on landmark series, let MDL
pick k."* Three things need fixing before that runs:

1. **`stumpy.mstump` does not give you MDL for free.** STUMPY exposes `mstump`/`mstumped` (the
   k-dimensional matrix profile and subspace) and separate helpers for subspace and MDL
   (`stumpy.subspace`, `stumpy.mdl`). *The reading confirms MDL is a **post-processing step over the
   already-computed profile**, not part of the profile computation* (§IV.E: "all k multidimensional
   motifs are found by the time the selection method is invoked"). Budget it as two steps.
   ⚠️ *The exact STUMPY API names are asserted from memory and are **not** verifiable from this
   paper — check the STUMPY docs before writing the script.*
3. **Expect mean-normalised profile values, and do not hand-roll the sum.** Per §2.2/§6.13, the
   algorithm stores the k-smallest distances **divided by k**. A from-scratch implementation that
   follows Def. 9 literally (sum) will produce values that are not comparable across k, and its
   elbow/MDL step will be meaningless — while a library implementation returns the normalised
   version. If we ever cross-check our own code against STUMPY, this is where they will disagree.
2. **m must be swept, not guessed.** §1.3 is explicit that the relevant subspace changes with motif
   length. A single m chosen to match "a gesture" will silently determine which limbs the answer
   names. E1 should report a small grid of m (e.g. 0.5 s / 1 s / 2 s / 4 s at our frame rate) and
   show the subspace as a function of m. Without that the result is not interpretable.

### 7.3 Which of our artefacts this actually applies to — and a caution

Our repo has **two different** multidimensional series this could run on:

- `data/features/frame_features.csv` — **23 feature channels** per frame (`sh_axis_deg`,
  `torso_lean_deg`, `d_lwrist_C`, `d_rwrist_C`, `d_lankle_C`, `d_rankle_C`, `d_head_C`,
  `ang_elbow_l/r`, `ang_knee_l/r`, `lw_x/y`, `rw_x/y`, `la_x/y`, `ra_x/y`, `energy_wrist`,
  `energy_ankle`, `motion_energy`, `scale`).
- `data/features/window_features.csv` — 50 columns = 4 index/time columns (`frame_start`,
  `frame_end`, `t_start_sec`, `t_end_sec`) + **46 aggregate channels**. These are *window
  aggregates* (mostly mean/std/min/max per feature; `motion_energy` gets six:
  sum/mean/peak/std/min/max), which is the wrong granularity for subsequence motif search.

**Run E1 on `frame_features.csv`, not `window_features.csv`.** And note the EOG trap applies
immediately: `energy_wrist`, `energy_ankle` and `motion_energy` are **not independent** —
`motion_energy` is an aggregate that will move in tandem with its components, and left/right pairs
(`d_lwrist_C` / `d_rwrist_C`) will co-move in any symmetric gesture. Expect a strong, spurious k = 2
motif in exactly those pairs. Per §2.5, the remedy is an **exclusion list**, decided in advance and
stated in the thesis, not discovered after seeing the answer.

A separate caution on raw landmarks: if we instead run on the 33 × (x,y,z) landmark series, note
that mSTAMP treats each coordinate as an independent channel, so a "joint" is 2–3 channels and the
MDL-selected k is a count of *coordinates*, not of joints. Report both.

### 7.4 The left-femur finding changes the shape of the limb-subset ablation

Our planned ablation is framed as "hands-only vs full-body". §3.3 shows the *correct* subspace for a
punch was `{right humerus, right radius, left femur}` — two arm joints **and the opposite leg**. If
our ablation only offers "upper body" and "whole body" as options, it cannot discover a cross-body
subspace, and it will look like a fair test when it is not. **Let mSTAMP choose the subspace; use the
hands-only condition as a comparison point, not as the hypothesis.**

### 7.5 Where it does *not* transfer

- mSTAMP finds a motif **inside one continuous series**. Our vocabulary construction is
  *clustering across frames pooled from a corpus* — a different operation. This paper does not
  license replacing k-means/HDBSCAN with motif discovery; it licenses using motif discovery as a
  **diagnostic on the feature space** before clustering, and as a **Phase-2 structure tool**.
- No **generation** component. Nothing here bears on the LSTM or on token sequence modelling.
- The `−0.0052` / "22 of 45" argument is about *correlation as a subspace selector*. It is **not** an
  argument against correlation-based feature pruning in general, and must not be cited that way.
- The z-normalisation assumption means mSTAMP would ignore exactly the amplitude differences that
  distinguish a large from a small version of the same Thai-classical gesture.

### 7.6 Related-work obligation

Because the mocap case study explicitly serves **motion-graph construction** [10], B1-15 is not only
a Branch-B methods citation — it is a **"why didn't you just do this?" paper for the Related Work
section**, sitting next to A1-8 (Motion Graphs) and A1-20 (Skeleton Motion Words). The honest answer
we can give is §7.5: motif discovery finds *where a pattern repeats in one sequence*; we are building
a *vocabulary across a corpus*, then generating from it. Those are complementary, and the thesis
should say so explicitly rather than leaving the reader to wonder.

### 7.7 References this read adds to the queue

- **[18] Minnen, Isbell, Essa, Starner (ICDM 2007), "Detecting Subdimensional Motifs"** — the
  *original* statement of our risk, ten years earlier. If we cite the risk, this is arguably the
  priority citation and B1-15 the quantification. **Not currently in `paper_index_B.csv`.**
- **[9] Hu, Chen, Zakaria, Ulanova, Keogh (ICDM 2013)** — the same argument for classification;
  relevant if we ever frame token assignment as classification.
- **[16] SiMPle (ISMIR 2016)** — matrix profile for music; the closest thing to a Phase-2 precedent
  for "repeated section discovery".
- **[13] PAMAP2** and **[6] CMU Mocap** — datasets, already known.

---

## 8. Checklist pass (`knowledge/reading_checklist.md`)

### (a) The item this paper *is* — TIER 1 #10 (B1-15)

| What the checklist asserted | Status | What the paper actually says |
|---|---|---|
| "mSTAMP หา motif ใน subspace k มิติที่ดีที่สุด (MDL เลือก k)" | ✅ **Addressed — confirmed exactly** | Defs. 9–13 + §IV.A/IV.E. MDL is a post-hoc selector over the already-computed profile, not part of it |
| Opening example is mocap boxing where full-body distance swamps the punch | ✅ **Addressed — confirmed verbatim** | Fig. 1 + §I, quoted in §1 above |
| *"eight additional irrelevant dimensions → about as well as random chance"* | ✅ **Addressed — quote is verbatim and correct** | §I. **Plus** the "about 5% of the data" clause our note omitted, which makes the bound optimistic |
| "เราจัดกลุ่มบน landmark ทั้ง 33 จุด → โครงสร้างของแขน/มืออาจถูกขาและลำตัวกลบหมด" | ⚠️ **Partially addressed — and imprecise about our own repo** | The mechanism is confirmed. But our *feature-based* pipeline runs on 23 engineered channels (`frame_features.csv`), not on 33 raw landmarks; and the `build_pose_dictionary` path already weights 12 key joints. The checklist wording over-states the exposure. See §7.3 |
| "ความเสี่ยงระดับ DATA stage ที่ยังไม่ได้ตรวจเลย" | ✅ **Addressed** | Still uninspected; this read makes E1 concrete and executable |
| *(not in the checklist)* redundant co-moving channels → spurious low-k motifs | ❌ **Not covered — new** | §IV.D EOG example. Directly applies to `motion_energy` vs `energy_wrist`/`energy_ankle`. **Add to the risk register** |
| *(not in the checklist)* the relevant subspace depends on m | ❌ **Not covered — new** | §I. Forces E1 to sweep m |
| *(not in the checklist)* correlation cannot be used to pre-select the subspace | ❌ **Not covered — new** | §II.A, r = −0.0052 |

### (b) Other checklist entries this paper bears on

- **#19 A1-20 Skeleton Motion Words (ICCV 2025)** — B1-15 is the 2017 quantification of why splitting
  joints helps. Cite them as a pair: precedent + mechanism.
- **#17 A1-7 Motion Texture** and the "อ้างอย่างเดียว" entry **A1-8 Motion Graphs** — §V.B is
  explicitly aimed at improving motion graphs [10], so B1-15 belongs beside A1-8 in Related Work.
- **TIER 3 #26–27 (k-Shape, SAX, time-series clustering)** — B1-15 is the *motif*-side counterpart to
  that entire clustering block. If Phase 2 is written as an extension, it should note that repeated
  structure inside a single dance is a motif problem, not a clustering problem.
- **E1 (limb-subspace check)** — ✅ unblocked and now **specified** (§7.2, §7.3): run on
  `frame_features.csv`, sweep m, declare the exclusion list in advance, report subspace-vs-m.
- **`memory.txt` line 546** ("B1-15 mSTAMP UNBLOCKED: use stumpy.mstump … exact mSTOMP variant") —
  consistent with the paper: **§V.A** states that "The mSTAMP algorithm can be built on top of either
  the STAMP or STOMP algorithm; therefore, it inherits all the positive characteristics from its
  parent algorithm", so an exact mSTOMP variant is a faithful implementation, losing only the
  anytime property (§2.2). *(This is the paper's claim, not an inference.)*

### (c) Checklist entries with no bearing on this paper

TIER 0 #1–5, TIER 1 #6–9 and #11–13, TIER 2 #14–23, TIER 3 #24–25 and #28–31, and the entire paywall
section are untouched by this read. This paper says nothing about vocabulary size, tokenisation,
codebook collapse, pose-estimation error, or generation quality.

### (d) Corrections owed upstream (found during this pass; **not applied** — those files are inputs)

- `reading_checklist.md` #10 says "เราจัดกลุ่มบน landmark ทั้ง 33 จุด". For the angle/feature pipeline
  this is inaccurate — see §7.3. The risk survives; the wording should be tightened to name the
  actual channel set.
- `paper_chain.md` B1-15 entry quotes the Fig. 1 passage as "if we look at the full set of Mo-Cap
  markers". The PDF reads "if we look **that** the full set" — an author typo. If that sentence is
  quoted verbatim in the thesis, use `[sic]` or paraphrase.
- Neither `paper_chain.md` nor the checklist records the **"about 5 % of the data"** qualifier, the
  **EOG redundancy trap**, or the **m-dependence of the subspace**. All three change what E1 should do.

### Checklist verdict in one line

**TIER 1 #10 (B1-15) is fully read and every claim our notes made about it is confirmed** — the
verbatim quote, the mocap framing, and the eight-dimension collapse — **but the note was incomplete
in three ways that materially change the queued experiment E1**, and it over-states our own exposure
by naming 33 landmarks where the pipeline actually uses 23 engineered channels.

---

## 9. Verification (independent second pass)

A separate verification agent re-read the paper from both extractions (`pdftotext -layout` and
`pypdf`), following the same Three-Pass method, with the draft of §§1–8 in hand and an explicit brief
to be adversarial. It was asked to check four things: (a) that every claim about the paper is
traceable to the paper; (b) every number and every quoted string, character by character; (c)
omissions and overstatements; (d) whether the draft's own inferences are correct *and* correctly
labelled as inferences rather than as paper claims. It was also asked to verify the two CSV headers
cited in §7.3. Its verdict was **REVISE**, with three blocking findings.

### Corrections it produced (all applied above)

**Blocking**

1. **The algorithm stores the *mean*, not the sum.** The draft asserted that the column-wise
   cumulative sum "is" the k-dimensional distance profile and is stored directly. Algorithm I
   **line 14** reads `𝐷′′ ← 𝐷′ ÷ 𝑖`, and the prose confirms that `𝐷′′` is what gets min-ed into the
   profile. Def. 9 (sum) and the stored value (mean) are different quantities and the paper never
   flags it. Root cause: this is precisely the line `pdftotext` renders as an empty cell, and the
   draft's claim to have "re-extracted every symbol with pypdf" had failed on the one line where it
   mattered most. **I re-verified this against the PDF directly before applying it.** Fixed in §2.2
   (with a call-out box), §2.3, §5.3, §6.13 (new), §7.2 (new item 3), the extraction table, and the
   header extraction note. This also changes the queued E1: a hand-rolled sum-based implementation
   would not match STUMPY's output.
2. **A quote was misattributed to the abstract.** "this could happen if the motifs are subtle and the
   large number of irrelevant dimensions happens to produce a spuriously similar pair of
   subsequences" is in **§V.A**, introducing the Fig. 12 experiment — not in the abstract. Fixed in
   §6.5.
3. **The MDL worked example used invented notation and reversed what is stored.** The paper's second
   series is a **reference** `Tᵣ`, the difference is `𝛥`, and compression comes from storing **`Tᵣ`
   and `𝛥`** — not, as the draft had it, `T` and the difference. (The digits, 80/50 bits, 4-bit and
   1-bit counts were all correct; the subscript and `𝛥` glyph are further `pdftotext` casualties.)
   Fixed in §2.6.

**Should-fix**

4. Fig. 8/9/11 "endpoints" were **axis maxima**, not measured runtimes — the curves' actual values
   are not readable. Fixed in §3.1 with an explicit warning.
5. The termination condition is **half**-specified, not absent: "it can be either be an input for the
   user or a more advanced technique could be applied." Only the *automatic* rule is future work.
   "Not achievable by a user" was an overstatement. Fixed in §2.6 and §6.3.
6. The STAMP-or-STOMP statement is in **§V.A**, not §IV.A (substance correct, locator wrong), and it
   is a paper claim rather than an inference. Fixed in §8(b).
7. The "Becase…" safeguard quote sits in **§V.A after Fig. 12**, not in §IV.E. Fixed in §2.6.
8. The upper-bound justification for Fig. 12's baseline cites only **[22]**; the draft had silently
   expanded it to [1][18][22][24] in §6.1. Fixed.
9. Def. 5 does allow top-K "trivially from the matrix profile" in the *univariate* case; the draft's
   assumption 1 overstated. Scoped to the multidimensional/MDL setting in §5.1.
10. **`window_features.csv` has 46 feature channels, not 49** (50 columns, 4 of them index/time), and
    the aggregates are not uniformly mean/std/min/max. Fixed in §7.3. `frame_features.csv` = 23
    feature channels **was confirmed correct**.
11. The distillation-column hedge was dropped: the paper says the rainstorm motif **"may only show
    up"** on those tags. Fixed in the extraction table.
12. "We visually examined the video snippet" is §V.B (mocap) wording only; §V.D uses different
    phrasing. Fixed in §6.4 — the underlying point stands.

**Nits, all applied**

13. "At least two orders of magnitude faster" appears **once**; a weaker "orders of magnitude faster"
    appears separately. Both unmeasured. §6.1 now says so precisely.
14. The weight-transfer reading of the left-femur result is **my** interpretation, not the paper's —
    now labelled as an inference (§3.3).
15. §V.C's chorus result is a **consistency remark** with SiMPle [16], not a claimed replication (§4).
16. "No pruning is possible" softened to the paper's actual scope: "various pruning and dynamic
    programing techniques" (§6.7).
17. §2.3 now uses the paper's own phrase, "admissibly in a greedy fashion".
18. "About 22 of the 45" added to the header's list of exact in-text numbers.
19. The guided-search MFCC/saxophone example [11] was missing; added to §1.2.
20. **Def. 13 has the same shape mismatch as Def. 12**, *and* Algorithm I explicitly omits subspace
    bookkeeping — so the paper gives no pseudocode for the object §7 depends on. Added to §6.12.
21. Fig. 13's own caveat — "the right arm of the subject is in a different position in latter frames
    within different occurrences of the motif" — was missing. Added as §6.4a.

### What the second pass checked and confirmed correct

Character-exact and re-confirmed: the Fig. 1 boxing quote (including the paper's "look that the"
typo); the eight-irrelevant-dimensions collapse **averaged over 100 trials**; the "about 5 % of the
data" clause and the draft's reading that it makes the bound optimistic; r = −0.0052, "about 22 of
the 45", 10 random walks; the motif of length 30 at positions 150 and 350; 𝑂(𝑑 log 𝑑 𝑛²) time and
𝑂(𝑑𝑛) space, matrix profile 𝑂(𝑛²), MASS 𝑂(𝑛 log 𝑛) vs Zhu et al. 𝑂(𝑛) and the anytime trade-off;
Def. 9's formula and Def. 13's wording verbatim; Minnen's six dimensions and "roughly 80 % accuracy";
Vahdatpour's 85 % / 17 % / three irrelevant dimensions / seven parameters; Tanaka's five parameters;
Fig. 12's embedded **4**-dimensional motif, 1 → 256 irrelevant dimensions, **forty trials**, "64
times … still near perfect", and the draft's insistence that the baseline is a proxy rather than a
reimplementation; all scalability parameters (n = 2¹⁴, m = 256, m swept 100–900, d up to 250, the
525,600-points ≈ two-hours estimate, anytime 10 %); the hardware line; all four case studies in full
(CMU subject 13 / 40 s / 38 dimensions / uppercut-vs-blocking failure / right humerus + right radius
+ left femur including the "left upper lag" typo; 46 ms / 23 ms / 32 Mel filters / 5 s, chorus at
all-dims vs drum pattern at k = 1–2 in the two lowest bands; the five appliances, 19 Apr – 15 May
2014, length 17,000, 4-hour subsequence, natural k = 2 = tumble dryer + washing machine; PAMAP2
subject 101, three IMUs and their four measurement types, all twelve activities, F = 0.88 with its
caveat verbatim); the preserved "2-dimenional" and "Becase" typos; the monotonicity inference in §2.3
(**mathematically correct, and it survives the ÷ k**, though its justification needed rewriting); the
two Def. 12 notation slips; that the "two orders of magnitude" speedup is never measured anywhere;
that the PDF is 10 pages and contains **no** venue, page-number or DOI string.

### Standing caveat after verification

The `pdftotext`-drops-glyphs problem caused a **substantive** error here, not a cosmetic one, and it
survived a full first pass that believed it had already controlled for it. For any future paper in
this folder: run **both** extractors and diff them, and treat any blank cell inside pseudocode as a
missing operation until proven otherwise.

---
---

# ฉบับภาษาไทย (Thai version)

## สรุปสั้น

**Matrix Profile VI: Meaningful Multidimensional Motif Discovery** — Yeh, Kavantzas, Keogh (IEEE ICDM
2017, pp. 565–574, DOI 10.1109/ICDM.2017.66 · *ข้อมูล venue/หน้า/DOI มาจาก `paper_index_B.csv` ไม่ได้อยู่ในไฟล์ PDF*)

เปเปอร์นี้บอกสองเรื่อง หนึ่ง — **ผลลัพธ์เชิงลบ**: การหา motif ในอนุกรมเวลาหลายมิติโดยใช้ *ทุกมิติ*
"จะไม่ให้ motif ที่มีความหมาย ยกเว้นในสถานการณ์ที่ถูกจัดฉากมาอย่างที่สุด" สอง — **mSTAMP**: อัลกอริทึมที่หา motif
ใน **subspace k จาก d มิติที่ดีที่สุด** ได้แบบ **แม่นยำจริง (exact)** และคำนวณ k ทุกค่าตั้งแต่ 1 ถึง d
**พร้อมกันในรอบเดียว** ด้วยเวลา 𝑂(𝑑 log 𝑑 · 𝑛²) และหน่วยความจำ 𝑂(𝑑𝑛) แล้วเลือก k อัตโนมัติด้วย **MDL**

**รูปเปิดเรื่องของเปเปอร์คือข้อมูลแบบเดียวกับเรา** — mocap นักมวยสองท่า ถ้าดูเฉพาะมือข้างถนัด สองท่านี้แทบเหมือนกัน
แต่ถ้าดู marker ครบทั้งตัว ความต่างของมือข้างที่ไม่ถนัดกับฟุตเวิร์กจะ **"กลบ" (swamp)** ความเหมือนของหมัดจนหาไม่เจอ

---

## Five Cs (ฉบับย่อภาษาไทย)

- **Category** — research prototype + การประเมินเชิงทดลอง โดยครึ่งหนึ่งของน้ำหนักเปเปอร์อยู่ที่ *การพิสูจน์ว่าโจทย์เดิมตั้งผิด*
- **Context** — ต่อยอดจาก Matrix Profile I/II/III [26][27][28] ของกลุ่มตัวเอง และตั้งตัวเป็นคู่แข่งของ Minnen et al. [18],
  Tanaka et al. [22], Vahdatpour et al. [24], Balasubramanian et al. [1] · ยืมของคนอื่นมาใช้เยอะ: MASS [17], MDL ของ
  Rissanen [14], elbow ของ Thorndike [23], must-link/cannot-link จาก constrained clustering [25]
- **Correctness** — ข้ออ้างหลักเรื่องความแม่นยำ (sort ตามคอลัมน์ + cumulative sum = k-dimensional distance profile
  ที่ถูกต้อง) **สมเหตุสมผลจริง** พิสูจน์จากการที่ z-normalized Euclidean distance ไม่เป็นลบ · **จุดอ่อนอยู่ที่การประเมินทั้งหมด**
- **Contributions** — (1) ผลลัพธ์เชิงลบพร้อมตัวเลข (2) mSTAMP (3) **matrix profile subspace** = บอกว่า motif อยู่ใน
  *มิติไหน* (4) constrained search (5) กฎ MDL เลือก k (6) case study 4 โดเมน
- **Clarity** — อ่านง่ายมาก แต่ **ไม่มีตารางตัวเลขแม้แต่ตารางเดียวทั้งเปเปอร์**

---

## ตัวเลขที่สำคัญที่สุด

| ตัวเลข | ที่มา | ความหมาย |
|---|---|---|
| **8 มิติที่ไม่เกี่ยวข้อง → แม่นเท่าการเดาสุ่ม** | §I, เฉลี่ยจาก **100 trials** | แกนของความเสี่ยงต่อ DATA stage ของเรา |
| **"motif กินพื้นที่ราว 5% ของข้อมูล … แต่โดยทั่วไป motif หายากกว่านั้นมาก ซึ่งเร่งอัตราที่มิติที่เพิ่มขึ้นจะกลบ motif"** | §I | **เลข 8 เป็นค่าที่มองโลกในแง่ดีแล้ว** — โน้ตเดิมของเราไม่มีประโยคนี้ |
| **r = −0.0052** ระหว่าง T1 กับ T2 (สองมิติที่มี motif ร่วมกันจริง) | §II.A | **ใช้ correlation คัดมิติล่วงหน้าไม่ได้** |
| ถ้าสร้าง random walk 10 เส้น จะมีราว **22 จาก 45** คู่ที่ correlation สูงกว่านั้น | §II.A | ตอกย้ำข้อเดียวกัน |
| 𝑂(𝑑 log 𝑑 · 𝑛²) เวลา, 𝑂(𝑑𝑛) หน่วยความจำ | §IV.A | คำนวณ k ทุกค่าพร้อมกัน |
| ทนได้ถึง **64 เท่า** ของจำนวนมิติที่เกี่ยวข้อง ยัง "near perfect" (เฉลี่ย **40 trials**, motif ฝัง 4 มิติ, กวาดมิติขยะ 1→256) | Fig. 12 | ผลหลักของเปเปอร์ |
| mocap: CMU **subject 13**, ชกมวย **40 วินาที**, **38 มิติ** | §V.B | ใช้ทุกมิติ → เจอ "หมัดอัปเปอร์คัต" จับคู่กับ "การบล็อก/หลบ" = ผิดความหมาย |
| mSTAMP k=3 → **right humerus + right radius + left femur** | §V.B | จับ cross คู่กับ cross ใน one-two combo ได้ถูกต้อง |
| PAMAP2 subject 101 → **F-measure = 0.88** | §V.E | ⚠️ **ต้องรู้ ground truth ก่อนถึงจะรู้จุดหยุดที่ดีที่สุด — เปเปอร์ยอมรับเอง** |
| ไฟฟ้าในบ้าน: k ธรรมชาติ = **2** = เครื่องอบผ้า + เครื่องซักผ้า | §V.D | sanity check ที่ตรวจด้วยสามัญสำนึกได้ |
| เพลง: ใช้ทุกมิติ → เจอ **ท่อนฮุก** · k=1, k=2 → เจอ **ลายกลอง** ใน 2 ย่านความถี่ต่ำสุด | §V.C | k ต่างกัน = ความหมายคนละระดับ จากการคำนวณรอบเดียว |

---

## ⚠️ สามข้อที่ checklist ของเรายังไม่มี และทั้งสามข้อเปลี่ยนวิธีทำการทดลอง E1

### 1. **subspace ขึ้นกับความยาว motif (m)**

เปเปอร์บอกชัดว่า "มิติที่สำคัญของ motif ขึ้นอยู่กับความยาว motif ที่ผู้ใช้กำหนด" — query ความยาว 1 ชั่วโมงเจอ motif
พายุฝน แต่ query ความยาว 1 วันเจอ motif การล้างระบบรายเดือน ซึ่งกินมิติมากกว่ามาก

→ **E1 ต้อง sweep m ไม่ใช่เดา m ค่าเดียว** ถ้าเลือก m ค่าเดียวให้ "พอดีกับหนึ่งท่า" เราจะเป็นคนกำหนดคำตอบเองโดยไม่รู้ตัว
เสนอ: รายงาน subspace เป็นฟังก์ชันของ m ที่ประมาณ 0.5 / 1 / 2 / 4 วินาที

### 2. **ช่องสัญญาณที่ซ้ำซ้อนกันสร้าง motif ปลอมที่ k ต่ำ**

ตัวอย่างจาก Dr. John Criley (UCLA): ศัลยแพทย์ระบบประสาทอาจต้อง **ตัด** ช่อง `ELECTROOCULOGRAM` ข้างหนึ่งทิ้ง
"เพราะตาสองข้างมักเคลื่อนไปพร้อมกัน จึงซ้ำซ้อน และคู่ {EOGleft, EOGright} มักจะรายงาน motif 2 มิติที่แรงแต่เป็นของปลอม"

→ **ใน `frame_features.csv` ของเรามีกับดักนี้เต็มไปหมด**: `motion_energy` เป็นค่ารวมที่ต้องขยับตาม `energy_wrist`
และ `energy_ankle` อยู่แล้ว · คู่ซ้าย-ขวา (`d_lwrist_C` / `d_rwrist_C`) จะขยับพร้อมกันในทุกท่าที่สมมาตร
→ **ต้องประกาศ exclusion list ล่วงหน้า** แล้วเขียนลงวิทยานิพนธ์ ไม่ใช่มาตัดทีหลังตอนเห็นคำตอบแล้ว

### 3. **ใช้ correlation คัดมิติไม่ได้**

r = −0.0052 ระหว่างสองมิติที่มี motif ร่วมกันจริง เหตุผลที่เปเปอร์ให้: **"เราสนใจ pattern เฉพาะที่ที่ซ้ำกัน
สถิติเกี่ยวกับแนวโน้มภาพรวมมักไม่ให้ข้อมูลอะไร"**

→ ⚠️ ระวัง: ข้อนี้เป็นข้อโต้แย้งเรื่อง **การใช้ correlation เลือก subspace สำหรับหา motif** เท่านั้น
**ไม่ใช่** ข้อโต้แย้งเรื่องการตัด feature ด้วย correlation โดยทั่วไป ห้ามอ้างข้ามบริบท

---

## ⚠️ กับดักการดึงข้อความจาก PDF นี้ (สำคัญ — ทำให้ draft แรกผิดจริง)

`pdftotext -layout` ได้ prose สะอาด แต่ **ลบสัญลักษณ์คณิตศาสตร์ทิ้งทั้งหมดโดยไม่เตือน** — และมันไม่ได้เสียแค่ความสวยงาม

**ALGORITHM I บรรทัดที่ 14 คือ `𝐷′′ ← 𝐷′ ÷ 𝑖`** แต่ `pdftotext` แสดงเป็นช่องว่างเปล่า
แปลว่า **ค่าที่เก็บใน matrix profile คือ "ค่าเฉลี่ย" ของระยะทาง k ตัวที่น้อยที่สุด ไม่ใช่ "ผลรวม"**
ขณะที่ Definition 9 นิยามไว้เป็น **ผลรวม** — เปเปอร์ไม่เคยพูดถึงความไม่ตรงกันนี้เลย

**ทำไมถึงสำคัญ:** การหาร k คือสิ่งที่ทำให้ค่า matrix profile **เทียบกันข้าม k ได้** ซึ่งเป็นฐานของกราฟ elbow (Fig. 6)
และของ unconstrained search ทั้งหมด ถ้าเป็นผลรวมดิบ ค่าจะโตตาม k แบบเกือบกลไก และ elbow จะตีความไม่ได้

→ **ผลต่อ E1:** ถ้าเราเขียนโค้ดเองตาม Def. 9 ตรง ๆ (ผลรวม) ผลจะไม่ตรงกับ `stumpy.mstump` ที่คืนค่าแบบ normalize แล้ว
→ **กฎใหม่สำหรับทุกเปเปอร์ในโฟลเดอร์นี้:** รันทั้ง `pdftotext` และ `pypdf` แล้ว diff กัน และให้ถือว่า
**ช่องว่างเปล่าใน pseudocode = คำสั่งที่หายไป** จนกว่าจะพิสูจน์ได้ว่าไม่ใช่

---

## ผลต่อโปรเจกต์เรา

### 1. ความเสี่ยงที่ checklist ข้อ 10 บันทึกไว้ **เป็นจริง** แต่ข้อความของเราคลาดเคลื่อนเรื่องตัวเอง

checklist เขียนว่า "เราจัดกลุ่มบน landmark ทั้ง 33 จุด" — สำหรับ pipeline สาย angle/feature **ไม่ตรง**:
`frame_features.csv` มี **23 ช่องสัญญาณ** (`sh_axis_deg`, `torso_lean_deg`, `d_*wrist_C`, `d_*ankle_C`,
`d_head_C`, `ang_elbow_*`, `ang_knee_*`, พิกัดข้อมือ/ข้อเท้า, `energy_*`, `motion_energy`, `scale`)
และ `build_pose_dictionary.ipynb` ก็ถ่วงน้ำหนัก 12 key joints อยู่แล้ว (= การเลือก subspace ด้วยมือแบบไม่มีหลักการ)

**ความเสี่ยงยังอยู่ แต่ต้องแก้ถ้อยคำให้ตรงกับ channel set จริง**

### 2. รัน E1 บนไฟล์ไหน

- ✅ `data/features/frame_features.csv` — 24 คอลัมน์ = index 1 + **23 ช่องสัญญาณ**
- ❌ `data/features/window_features.csv` — 50 คอลัมน์ = index/เวลา 4 + **46 ช่องสัญญาณ** แต่เป็น *ค่าสรุปราย window*
  (mean/std/min/max ต่อ feature; `motion_energy` มี 6 ตัว) → **ผิด granularity สำหรับการหา motif แบบ subsequence**

ถ้าจะรันบน landmark ดิบ 33 × (x,y,z) แทน: mSTAMP มอง **แต่ละพิกัดเป็นหนึ่งช่องสัญญาณ** ดังนั้น "หนึ่งข้อต่อ" = 2–3 ช่อง
และ k ที่ MDL เลือกจะเป็นจำนวน *พิกัด* ไม่ใช่จำนวน *ข้อต่อ* → **ต้องรายงานทั้งสองแบบ**

### 3. ผลจาก left femur เปลี่ยนรูปแบบของ limb-subset ablation

เราวางแผน ablation ไว้เป็น "มือ/แขนอย่างเดียว vs ทั้งตัว" แต่ subspace ที่ถูกต้องของหมัดในเปเปอร์คือ
**{right humerus, right radius, left femur}** = แขนขวาสองข้อต่อ **+ ขาฝั่งตรงข้าม**

→ ถ้า ablation ของเรามีแค่ตัวเลือก "ท่อนบน" กับ "ทั้งตัว" มันจะ **ค้นพบ subspace แบบไขว้ตัวไม่ได้เลย**
และจะดูเหมือนเป็นการทดสอบที่ยุติธรรมทั้งที่ไม่ใช่
→ **ให้ mSTAMP เลือก subspace เอง** แล้วใช้เงื่อนไข "มืออย่างเดียว" เป็นจุดเปรียบเทียบ ไม่ใช่เป็นสมมติฐาน

*(หมายเหตุ: คำอธิบายเรื่อง "การถ่ายน้ำหนักผ่านขาฝั่งตรงข้าม" เป็น **การตีความของผู้สรุป** เปเปอร์บอกแค่ชื่อสามข้อต่อ
ไม่ได้อธิบายเชิงชีวกลศาสตร์ ห้ามยกไปอ้างว่าเป็นคำพูดของเปเปอร์)*

### 4. ส่วนที่ **ไม่** ถ่ายทอดมาถึงเรา

- mSTAMP หา motif **ภายในอนุกรมเดียวที่ต่อเนื่อง** ส่วนการสร้าง vocabulary ของเราคือ *การ cluster เฟรมที่รวมมาจากคลัง*
  → เปเปอร์นี้ **ไม่ได้อนุญาต** ให้เอา motif discovery ไปแทน k-means/HDBSCAN แต่อนุญาตให้ใช้เป็น **เครื่องมือวินิจฉัย
  feature space ก่อน cluster** และเป็น **เครื่องมือของ Phase 2**
- **ไม่มีส่วน generation เลย** — ไม่กระทบ LSTM หรือ token sequence modelling
- z-normalization ต่อมิติ แปลว่า mSTAMP จะ **มองข้ามความต่างของแอมพลิจูด** — คือความต่างระหว่างท่ารำแบบกว้างกับแบบแคบ
  ซึ่งเป็นสิ่งที่เราอาจอยากเห็น

### 5. ภาระ Related Work

เพราะ case study mocap มุ่งไปที่การสร้าง **motion graph** [10] โดยตรง B1-15 จึงไม่ใช่แค่ citation สาย Branch B
แต่เป็น **เปเปอร์ประเภท "ทำไมไม่ใช้อันนี้ไปเลย?"** ที่ต้องวางไว้ข้าง A1-8 (Motion Graphs) และ A1-20 (Skeleton Motion Words)
คำตอบที่ซื่อสัตย์คือข้อ 4 ข้างบน: motif discovery หาว่า *pattern ซ้ำตรงไหนในอนุกรมเดียว* ส่วนเรากำลังสร้าง
*vocabulary ข้ามคลัง* แล้ว generate จากมัน — สองอย่างนี้เสริมกัน และวิทยานิพนธ์ต้องเขียนให้ชัดเอง

---

## จุดอ่อนที่ต้องระบุเวลาอ้างเปเปอร์นี้

1. **ไม่เคยรันระบบคู่แข่งจริงเลย** — ตัวเทียบใน Fig. 12 คือ matrix profile แบบใช้ทุกมิติ ซึ่งอ้างว่าเป็น *ขอบบน*
   ของวิธีอื่น (และประโยคที่อ้างนั้นอ้างถึง **[22] เท่านั้น**) · ข้ออ้าง **"เร็วกว่าอย่างน้อยสองเท่าของอันดับ"**
   **ไม่มีการวัดรองรับที่ไหนในเปเปอร์เลย** — ห้ามอ้างว่าเป็นตัวเลขที่วัดมา
2. **ไม่มีตารางตัวเลขเลยสักตาราง** ทุกผลเป็นกราฟ บางรูปมีขีดแกนแค่สองสามขีด
3. **F = 0.88 ต้องใช้ oracle** — เปเปอร์ยอมรับเองว่า "เราไม่สามารถรู้จุดหยุดที่ดีที่สุดได้โดยไม่ดู ground truth label"
   (เงื่อนไขหยุดแบบ *อัตโนมัติ* ถูกโยนไป future work แม้จะเปิดช่องให้ผู้ใช้กำหนดจำนวนเองได้)
   **นี่คือตัวเลขที่มีโอกาสถูกอ้างผิดมากที่สุด รวมทั้งโดยเราเอง**
4. **3 ใน 4 case study ไม่มีการประเมินเชิงปริมาณ** — ผู้เขียนตรวจความหมายเอง ไม่ blind ไม่วัด
5. **มิติขยะในการทดลองสังเคราะห์เป็น random walk** ของจริงมักมีโครงสร้าง (เป็นคาบ, drift, artefact ของเซนเซอร์)
   ซึ่งน่าจะสร้าง match ปลอมที่ k ต่ำได้ง่ายกว่ามาก เปเปอร์รู้ตัว (§V.A) แต่ไม่เคยทดสอบ
6. **𝑂(𝑛²)** ตามความยาวอนุกรม · ใช้ GPU/anytime/incremental ช่วยได้ แต่ไม่หายไป
7. **ตัดทางเทคนิค pruning/DP** ตามข้อโต้แย้ง Fig. 5 ของตัวเอง
8. **ข้ออ้าง "พารามิเตอร์น้อยกว่า" อ่อนลงเพราะ m** — เทียบกับ 5 ตัวของ [22] และ 7 ตัวของ [24] ก็จริง
   แต่ m ยังอยู่ และ §I บอกเองว่า **คำตอบเปลี่ยนตาม m** ในทางปฏิบัติผู้ใช้ต้อง sweep m ซึ่งเอาภาระกลับคืนมาเกือบหมด
9. **Def. 9 กับ ALGORITHM I บรรทัด 14 ขัดกัน** (ผลรวม vs ค่าเฉลี่ย) และเปเปอร์ไม่เคยยอมรับ
10. **Def. 12 และ Def. 13 ประกาศรูปร่างไม่ตรงกับ ALGORITHM I** และ ALGORITHM I **ตัด bookkeeping ของ subspace ทิ้ง**
    ("เพื่อให้การนำเสนอง่ายขึ้น") → **เปเปอร์ไม่ได้ให้ pseudocode สำหรับสร้าง object ที่เราต้องใช้จริง**

---

## reference ที่ต้องตามอ่านต่อ

- **[18] Minnen, Isbell, Essa, Starner (ICDM 2007) — "Detecting Subdimensional Motifs"** — เป็นคน
  **แรกที่ชี้ผลเสียของมิติที่ไม่เกี่ยวข้อง** ก่อน B1-15 สิบปี ถ้าจะอ้างความเสี่ยงนี้ อันนี้อาจเป็น citation หลัก
  ส่วน B1-15 เป็นตัวให้ตัวเลข · ⚠️ **ยังไม่มีใน `paper_index_B.csv`**
- **[9] Hu et al. (ICDM 2013)** — ข้อโต้แย้งเดียวกันในฝั่ง classification
- **[16] SiMPle (ISMIR 2016)** — matrix profile กับดนตรี = ตัวอย่างใกล้เคียงที่สุดของ "หาท่อนที่ซ้ำ" สำหรับ Phase 2

---

## บันทึกการตรวจสอบ (ฉบับย่อ — ดู §9 ภาษาอังกฤษสำหรับฉบับเต็ม)

ใช้ agent ตรวจสอบอิสระ อ่านเปเปอร์ใหม่จากทั้งสอง extraction ตามวิธี Three-Pass เดียวกัน พร้อมโจทย์ให้จับผิด
**ผลตัดสิน: REVISE** พบข้อผิดพลาดระดับ blocking **3 ข้อ** (แก้ครบแล้วทั้งหมด):

1. **อัลกอริทึมเก็บ "ค่าเฉลี่ย" ไม่ใช่ "ผลรวม"** (ALGORITHM I บรรทัด 14 `÷ 𝑖`) — draft แรกเขียนผิด
   เพราะ `pdftotext` ลบบรรทัดนั้นทิ้ง **ยืนยันกับ PDF ต้นฉบับเองอีกครั้งก่อนแก้**
2. **quote ถูกอ้างแหล่งผิด** — ประโยคเรื่อง "spuriously similar pair" อยู่ใน §V.A ไม่ใช่ abstract
3. **ตัวอย่าง MDL ใช้สัญกรณ์ที่คิดขึ้นเอง และสลับสิ่งที่เก็บ** — ของจริงคือ `T`, reference `Tᵣ`, ผลต่าง `𝛥`
   และเก็บ **`Tᵣ` กับ `𝛥`** (ตัวเลข 80/50 บิต ถูกหมด)

พร้อมข้อแก้ระดับ should-fix อีก 9 ข้อ (รวมถึง **`window_features.csv` มี 46 ช่อง ไม่ใช่ 49** —
ส่วน `frame_features.csv` = 23 ช่อง **ถูกต้อง**) และ nit อีก 9 ข้อ

ตัวเลขและ quote ที่ตรวจแล้ว **ถูกต้องเป๊ะทุกตัวอักษร**: 100 trials, 5%, −0.0052, 22/45, 𝑂(𝑑 log 𝑑 𝑛²),
40 trials, 64 เท่า, subject 13 / 40 วินาที / 38 มิติ, สามข้อต่อที่เลือก, 46ms/23ms/32 filters/5 วินาที,
17,000 / 4 ชั่วโมง / k=2, PAMAP2 subject 101, F = 0.88 พร้อมคำเตือน, และ typo ของเปเปอร์เอง
("look that the", "left upper lag", "2-dimenional", "Becase") ที่เก็บไว้ครบ
