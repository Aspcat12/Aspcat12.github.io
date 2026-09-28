# Assessment of monocular human pose estimation models for clinical movement analysis

**Rode, D.; Dunkel, A.; Willi, R.; Wolf, P.; Xiloyannis, M.; Riener, R.**
*Scientific Reports* (2025) 15:38767 · DOI [10.1038/s41598-025-22626-7](https://doi.org/10.1038/s41598-025-22626-7)
Affiliations: ETH Zurich (D-HEST), Akina AG, Schulthess Klinik Human Performance Lab, Medical Faculty Univ. Zurich.
Received 15 April 2025 · Accepted 30 September 2025 · Open Access (CC BY 4.0) · Competing interests: none declared.

Local file: `knowledge/reading_docs/Assessment_of_monocular_human_pose_estimation_mode.pdf`
Project index ID: **A1-14** (Tier 0, item #5 of `reading_checklist.md`)
Read following `reading_guide.md` (Keshav Three-Pass). Pass depth reached: **pass 2 complete + partial pass 3**
(equations re-derived and cross-checked against the text; author code/supplementary tables **not** available — see *Coverage gaps*).

---

## 0. Five Cs (pass 1)

| C | Answer |
|---|---|
| **Category** | Empirical measurement / benchmark study. Not a new method — it builds a new ground-truth dataset and measures 11 existing open-source systems against it. |
| **Context** | Sits on top of the HPE survey literature (Chen 2020; Zheng 2023; Wang 2021), the standard 3D benchmark line (Human3.6M, HumanEva, MPII, COCO, AMASS; exercise-specific MOYO, Fit3D), and the clinical-biomechanics literature on the Conventional Gait Model and soft-tissue artifact (Leboeuf 2023; Baker 2017; Peters 2010). |
| **Correctness** | Assumptions are reasonable and the authors themselves bound them: passive-marker OMC is used as ground truth despite its own error, and the paper quantifies that error so the reader can see the comparison is still valid (HPE error is several times larger). Sampling, synchronisation and coordinate-frame handling are described in enough detail to be **re-implementable in principle, though not reproducible in practice** — no data, no code, no supplementary tables, and a guessed depth-normalisation constant (see *Coverage gaps*). |
| **Contributions** | (1) **Physio2.2M** — 2.2 M RGB frames of physical exercise with simultaneous 27-camera Vicon ground truth; (2) a head-to-head accuracy/precision/speed benchmark of 11 estimators (18 2D model configurations; 26 3D model configurations, which include direct×lifting combinations); (3) a clean quantification of the monocular depth penalty (≈2–3× in-plane error) and of where it comes from. |
| **Clarity** | Good. Metrics are given as explicit equations, model choices are justified. Several small internal inconsistencies exist (see *Discrepancies*), and the per-model result tables live in supplementary material that is not bundled with the PDF. |

## 0b. Extraction table (อ.Proadpran format)

| Field | Content |
|---|---|
| **Motivation** | Passive-marker OMC is accurate but slow to set up, expensive, needs anatomical expertise → impractical for routine clinical or home use. Markerless monocular HPE is cheap and fast, but *how wrong is it* on real physical-exercise poses is not known, because existing 3D-ground-truth datasets (Human3.6M etc.) largely lack irregular/complex poses. |
| **Research question** | What accuracy, precision and inference speed do off-the-shelf monocular markerless pose estimators actually achieve on physical exercise, measured against marker-based OMC — and are they good enough for clinical interpretation? |
| **Proposed method** | Capture a purpose-built paired dataset (Physio2.2M), express HPE and OMC poses in a common camera-specific frame, and evaluate 11 estimators with MPJPE, per-axis MAE, Procrustes-aligned MPJPE, knee/elbow flexion MAE, detection ratio and FPS. |
| **Evaluation** | Averages over the *entire* dataset — all participants, exercises and camera angles — deliberately, to produce general rather than best-case numbers. |
| **Contribution** | A usable selection guide (which estimator for which constraint) plus an explicit statement of the current ceiling: no tested estimator reaches the <5° joint-angle error needed for clinical interpretation, but *some* 2D estimators reach accuracy comparable to or better than visual assessment of knee flexion, and the paper states that the *majority of 3D* estimators outperform it. |

---

## 1. Problem and motivation

Passive-marker optical motion capture (OMC) is the de-facto noninvasive gold standard for human movement
measurement, but it carries a heavy operational cost: surrounding the capture volume with infrared cameras,
calibrating them, identifying anatomical landmarks, and taping markers to those landmarks. Accuracy depends
strongly on correct marker placement and is degraded by soft-tissue artifact. Together with infrared-camera and
software-licence costs, this restricts OMC primarily to research and development settings.

Markerless monocular HPE promises the opposite trade: a single camera, no markers, trivial setup — attractive for
clinical evaluation, supervised exercise, therapy-progress tracking, and unsupervised home use. But monocular
methods are less accurate in depth and more sensitive to self-occlusion than multidirectional methods, and the
datasets normally used to benchmark them (HumanEva, Human3.6M, MPII, COCO, AMASS) are thin on the irregular poses
that physical exercise produces. MOYO and Fit3D are among the few exercise-focused exceptions. The gap the paper
targets is therefore: **only few datasets allow monocular HPE error to be quantified against state-of-the-art
marker-based OMC in 3D, and those with a strong focus on physical exercise are scarce — so the accuracy of these
tools on exercise poses is largely uncharacterised, and their clinical usability is unknown.**

## 2. Method

### 2.1 Physio2.2M

- **25 unimpaired participants** (11 male, 14 female). Mean age 26 (range 20–33); mean height 1724 mm (1580–1920);
  mean weight 68 kg (47–94). People unable to exercise due to musculoskeletal, neurological or cognitive
  deficiency were excluded.
- Unilateral and bilateral exercises (*Shoulder Rotation and Elbow Flexion* and *Squat* were the bilateral ones,
  all others unilateral), each performed in **3 sets of 5 repetitions**.
- **Ground truth:** Vicon, **27 infrared cameras** (22 Vero v2.2, 3 MX T10, 2 MX T20-S) at **200 Hz**, arranged with
  overlapping views for redundancy against marker occlusion.
- **46 reflective markers**, **Plug-in Gait** model (a widely used variant of the Conventional Gait Model),
  reconstructing hip, knee, ankle, shoulder, elbow and wrist locations in Vicon Nexus 2.15. 38 markers taped to
  anatomical landmarks by two trained experts; the rest on a 4-marker headband and two 2-marker wristbands. Model
  calibration = 15 s static T-pose plus dynamic leg/arm/upper-body rotations.
- **Video:** 4 Logitech HD C920 webcams at **30 Hz**, at two heights (270 mm and 950 mm) on two stands at
  perpendicular viewpoints, participants at 3 m and 3.5 m. Exercises were performed so that one camera pair saw the
  participant frontally and the other saw the sagittal plane. Reflective markers on the cameras recovered their
  position and orientation in the global frame.
- **Synchronisation:** hand clap, then maximising cross-correlation of wrist positions between systems. OMC
  downsampled 200 → 30 Hz by linear interpolation.
- Total: **2.2 million RGB frames** with corresponding 3D joint-centre locations.
- Ethics: ETH Zurich Ethics Commission EK 2023-N-4, informed consent obtained.
- **Data availability: on reasonable request only — the dataset is *not* publicly available** (privacy protection).

### 2.2 Inference setup

All models run on one machine (AMD Ryzen 9 7900X, NVIDIA RTX 4080, 128 GB RAM, CUDA 12.2, Python 3) with GPU
acceleration. Each camera processed separately (monocular only). Estimated poses were expressed in the ground-truth
coordinates using the known camera orientation, **root-translated so the hip midpoint coincides with the OMC hip
midpoint**, and pixel coordinates converted to metric units using a per-frame, per-camera factor
= (camera-to-ground-truth-hip-midpoint distance) / (focal length in pixels).

### 2.3 Models evaluated

11 open-source estimators, expanded into **18 2D model configurations and 26 3D model configurations**:

- **2D direct:** OpenPose (bottom-up, PAFs), AlphaPose ('Fast Pose', ResNet50 backbone + YoloV3 detector, Halpe),
  HRNet (width 48, 384×288, COCO), Detectron2 (Keypoint R-CNN, ResNet-101 + FPN),
  RTMPose / RTMO / RTMW (SimCC dual-classification; Lightweight / Balanced / Performance each).
- **3D direct:** BlazePose in `Lite` / `Full` / `Heavy`, in `Local` (normalised pixel) and `World` (metric,
  hip-midpoint origin) modes.
- **2D→3D lifting:** MotionBERT 'Lite' (243 frames), PoseFormerV2 (243 frames, DCT frequency-domain input; it and
  BlazePose 'World' are the only estimators here that return landmarks in metric units), MotionAGFormer 'Big'
  (243 frames, transformer + GCN), each run on 2D pose sequences produced by the direct estimators above.
  **The paper does not state which direct×lifting combinations were run**; only combinations on BlazePose 'Local'
  'Heavy' are named in the Results and figures. 3 lifters × 18 2D inputs would be 54 configurations, but only 26 3D
  configurations are reported — so the set is **not** a full cross-product, and its composition is recoverable only
  from Supplementary tables S3–S4. For the same reason the component list above cannot be summed to reproduce
  either the 18 or the 26; those counts are stated by the paper but not decomposed in the article body.

### 2.4 Metrics

Error vectors point from the HPE joint to the OMC joint, expressed in a camera-specific (x = horizontal,
y = vertical, z = depth) frame. **12 joints** are compared: left/right wrist, elbow, shoulder, hip, knee, ankle.

- `PE_{i,j}` = Euclidean norm of the error vector (Eq. 2); `MPJPE_i` = mean PE over the 12 joints (Eq. 3);
  `MPJPE` = mean over all frames (Eq. 6). For 2D estimators the z term is dropped → **2D MPJPE**; with depth → **3D MPJPE**.
- Per-axis joint- and frame-averaged absolute errors `ē_x`, `ē_y`, `ē_z` (Eqs. 4–5).
- **PAMPJPE** (Eq. 7): generalised orthogonal Procrustes alignment solved by SVD (MATLAB R2023a `procrustes`,
  **with scaling, no reflections**), which reduces scaling error from the pixel→metric conversion and the systematic
  hip-midpoint influence, making per-joint comparisons fair.
- **Flexion-angle MAE** (Eqs. 8–9): elbow and knee assumed to be 1-DoF hinges, angle from the scalar product; the
  frame error is the mean of the left- and right-side absolute errors. Reported both as **3D MAE** (full 3D vectors)
  and **2D MAE** (projection onto the image plane), so that 2D estimators are compared fairly.
- **Detection ratio:** frames with no detected pose are excluded from the error metrics and reported separately.
  For lifting methods, the ratio reported is the final one after the full 2D→lift chain.
- **Inference speed:** averaged per inference step over the dataset; for lifting methods **only the lifting step is timed**.

## 3. Key results

### 3.1 Direct 2D estimators (the 18 "2D pose estimation models")

| Quantity | Range across models |
|---|---|
| 2D MPJPE | **72 – 122 mm** |
| Knee flexion 2D MAE | **9.3° – 21.9°** |
| Elbow flexion 2D MAE | **21.5° – 28.9°** |
| Inference speed | **25 – 200 FPS** |
| Detection ratio | **56.50 % – 100 %** |

> ⚠️ **Scope note (a third internal inconsistency in the source).** The paper's own best 2D figures —
> MotionAGFormer on BlazePose 'Local' 'Heavy', **2D MPJPE 61 mm** and **knee 2D MAE 8.5°** — fall *below* the
> stated 72–122 mm / 9.3–21.9° ranges. Those ranges therefore cover only the 18 **direct** 2D models, not lifted
> 2D poses. The paper does not say so explicitly.

- **Best direct 2D — RTMPose 'Performance':** ē_x 37 mm, ē_y 52 mm, **2D MPJPE 72 mm**, 2D PAMPJPE 53 mm,
  knee 2D MAE **9.3°**, elbow 2D MAE 24.9°, **pose predicted in all frames**, 30 FPS.
- **Best 2D overall — MotionAGFormer lifting BlazePose 'Local' 'Heavy':** ē_x 34 mm, ē_y 43 mm,
  **2D MPJPE 61 mm**, 2D PAMPJPE 46 mm, knee 8.5°, elbow 22.1°, 100 % detection (it **fills all encountered gaps**
  in the input sequence — the paper attributes this gap-filling ability to **both** MotionAGFormer and
  PoseFormerV2), 4580 FPS for the lifting step. → *A lifting model can improve the in-plane 2D pose too,
  not only add depth.*
- Most estimators show their lowest Procrustes-aligned error at the **hip**; RTMPose and its derivative RTMO are
  the exception, being more accurate at the **knee**.

### 3.2 3D estimators (26 model configurations)

| Quantity | Range across models |
|---|---|
| 3D MPJPE | **146 – 249 mm** |
| Knee flexion 3D MAE | **14.1° – 25.8°** (abstract & discussion; the Results section states 25.9° — see *Discrepancies*) |
| Elbow flexion 3D MAE | **16.3° – 26.0°** |
| Inference speed (lifting) | **117 – 9341 FPS** (abstract; Results section states 9339 — see *Discrepancies*) |
| Detection ratio | **14.40 % – 100 %** |

- **Best direct 3D — BlazePose 'World' 'Heavy':** ē_x 50 mm, ē_y 58 mm, **ē_z 108 mm**, **3D MPJPE 146 mm**,
  3D PAMPJPE 110 mm, knee 17.2°, elbow 18.3°, **98.8 % detection**, **147 FPS**.
- **Best 3D overall — MotionAGFormer on BlazePose 'Local' 'Heavy':** ē_x 34 mm, ē_y 43 mm, **ē_z 119 mm**,
  **3D MPJPE 146 mm**, 3D PAMPJPE **105 mm**, knee 16.7°, elbow **16.3°**, 100 % detection, 4580 FPS.
  Note it matches BlazePose World Heavy on 3D MPJPE while being better in-plane and *worse* in depth.
- **All** 3D estimators have their smallest Procrustes-aligned joint position error at the hip; wrists and ankles
  are worst.

### 3.3 The three results that matter most

1. **Depth error is ≈2–3× the in-plane error for every 3D estimator tested.** The paper states the mean absolute
   depth error is approximately two to three times greater than the mean absolute horizontal and vertical errors
   for all pose estimators investigated. Causes: self-occlusion (by design, two of the four cameras always
   experienced significant self-occlusion — right legs during the squat, right upper extremities during shoulder
   rotation / elbow flexion when viewing the sagittal plane) and the inherent projective ambiguity of monocular
   depth estimation.
2. **Vertical error exceeds horizontal error for every estimator.** A subsequent analysis attributed this to the
   frontal-plane views: from the frontal plane ē_y ≫ ē_x, while from the sagittal plane the two tended to be
   similar; equal numbers of frontal and sagittal cameras meant the dataset average inherited the frontal asymmetry.
3. **No estimator reaches clinical usability; on the knee, some estimators match or beat visual assessment.**
   Clinical interpretation requires joint angle errors below **5°**; none of the estimators tested achieved that.
   However, visual measurement of knee flexion during running by human raters has been reported at errors of
   **−54° to 21°** (MAE extracted from the source figure ≈ **20.6°**), with poor consistency even among experienced
   observers. Against that, the paper's own wording is careful: **"some"** 2D estimators (9.3–21.9°) reach accuracy
   *comparable to or better than* visual inspection, while **"the majority of investigated 3D pose estimators
   outperform visual assessments of knee flexion angles"** (14.1–25.8°). For the **elbow** the verdict reverses:
   expert visual raters achieve MAE **8.4°**
   (large flexion angles) / **12.2°** (small angles), whereas the estimators sit at 21.5–28.9° (2D) and
   16.3–26.0° (3D) — **HPE currently loses to visual inspection on the elbow.**
   Supporting reliability figures: elbow inter-observer reliability 0.38 (inexperienced rater vs expert surgeon)
   to 0.96 (two experts); knee visual ICC 0.82–0.97; only about 16.8 % of novices rated elbow angles with
   significant correlation.

4. **The paper's own forward claim — 2D-only use could reach clinical accuracy.** It states that the largest
   limitation of existing monocular markerless estimators is their lack of accuracy in depth estimation, and that
   although overall 3D accuracy is currently inadequate for clinical interpretation, **limiting their use to 2D
   applications with optimal camera orientations could potentially achieve the desired level of accuracy** — and,
   in the Conclusion, that accuracy is much greater when use cases are limited to 2D ones without depth estimation.
   This is the single strongest in-source justification for our experiment **E6** (see §8).

### 3.4 Why the models differ (the paper's own explanation)

- **Detectron2** shows *lower* accuracy than the purpose-built estimators — Keypoint R-CNN was not purposefully
  designed for HPE and therefore does not consider context and spatial relations when predicting joint locations.
  (The paper does not rank it last; per-model values are in Supplementary tables S1–S2.)
- **HRNet > OpenPose/AlphaPose** because parallel high-resolution branches avoid reconstructing high-resolution
  features from low-resolution ones.
- **RTMPose/RTMW/RTMO are the most accurate 2D family** — SimCC's two independent per-axis classifications give
  sub-pixel precision and reduce heatmap quantisation error, plus transformer attention over global and local
  joint dependencies.
- **BlazePose is accurate despite direct regression and no parallel network**, attributed to (a) its training set,
  hand-labelled with GHUM 3D ground truth and heavily weighted toward **yoga and fitness poses very similar to this
  dataset**, and (b) an encoder trained on heatmap estimation even though the heatmap path is removed at inference.
  Its speed comes from regression + the skip-frame detection mechanism (detection re-run only when no human is
  visible).
- **Lifting methods** are fast (smaller inputs) and can *improve in-plane* accuracy by capturing temporal and
  spatial relations across frames, but **their depth estimation underperformed BlazePose**, a direct estimator —
  which the paper attributes, tentatively, to **differences in their training datasets**.
  PoseFormerV2 shows slightly better accuracy than MotionBERT for most input sequences (frequency filtering reduces
  noise and jitter), though MotionBERT is better in-plane and worse in depth. MotionAGFormer is the most accurate
  lifter (transformer + GCN) but runs at about half MotionBERT's speed.
- **Lifting accuracy is strongly dependent on the 2D estimator feeding it — a range of 3D MPJPE up to 40 mm.**
- Real-time context: even the early two-stage methods (OpenPose, Detectron2, HRNet, AlphaPose) exceeded 15 FPS,
  the threshold associated with viewer enjoyment and real-time performance.

## 4. Assumptions and limitations

Stated by the authors:

1. **Ground truth is itself imperfect.** Passive-marker OMC with the Conventional Gait Model suffers soft-tissue
   artifact: marker displacement of **3–54 mm** has been reported for this model (note the underlying source,
   Fiorentino et al., is specifically about **the hip**, though the paper attributes the figure to the CGM
   generally); hip-joint-centre error has been
   estimated at ≈ **31 mm**; knee-flexion angle error ≈ **0.9°** from marker misplacement and ≈ **3.3°** from
   soft-tissue artifact; **<5°** for knee flexion across 3D gait measurement methods generally; upper-body angle
   errors ≈ **10°** with the comparable Heidelberg Upper Extremity model. The authors argue OMC remains a valid
   reference because HPE errors are multiple times larger: **2D PAPE at the hip 43–51 mm (up to twice the OMC hip
   joint position error); 3D PAPE at the hip 74–114 mm (three to four times larger).** The CGM's documented
   weaknesses — unconstrained segment lengths, insufficiently validated upper-body model, poorer hip-joint-centre
   estimation than alternatives — apply here. A different accepted marker set would give different ground-truth
   joint positions.
   **Sharper than the paper puts it:** the <5° clinical threshold and the "<5° knee-flexion error across 3D gait
   measurement methods" figure are cited to the **same reference** (McGinley et al. 2009, which appears twice in
   the bibliography as refs 68 and 82). So the ground-truth method's own knee-flexion error sits at **the very
   line the paper uses to declare HPE clinically unusable** — a stronger limitation than "ground truth is itself
   imperfect", and worth stating plainly if this paper is cited as an accuracy bound.
2. **Dataset-wide averaging hides conditions.** Means are taken over all participants, exercises and camera angles,
   similar to how accuracy is assessed on other datasets — so these are **general, not ideally achievable**,
   accuracies. Self-occlusion and optimal viewing angles are not factored out.
3. **Population is narrow.** Young, healthy, unimpaired, and ethnically homogeneous (ethnicity was not considered in
   recruitment). Findings may not extend to clinical use cases with impaired individuals, such as pathological gait.
   Appearance may affect accuracy through the models' training data; this was not investigated.
4. **Laboratory conditions.** One visible human, uniform lighting, minimal background interference, predominantly
   tight and short sports clothing. At-home / in-the-wild accuracy may be **lower** (lighting, occlusions,
   background, clothing, multiple visible humans).
5. **A BlazePose-specific measurement caveat.** In 'Local' mode the developers do not provide a clear specification
   of the normalisation constant for the depth coordinate; the authors reconstructed absolute pixel depth using the
   **vertical** image size because it gave better results than the more common horizontal normalisation. The paper
   notes 'Local' might show even higher accuracy if a constant depth normalisation factor were found.
   *(Our inference, not stated in the paper: part of BlazePose-Local's reported depth error may therefore be an
   artefact of this unknown constant.)*
6. **Off-the-shelf only.** No further training or fine-tuning, by design, because that is how these tools are most
   commonly used.

### Recommendations the paper derives

- Orient the camera so the angles of interest lie **in the image plane** as much as possible; perform the movements
  within the image plane where feasible.
- If high 3D accuracy is essential, use **multi-view** methods that fuse several cameras.
- If monocular is unavoidable, prefer estimators with an integrated kinematic body model (**HSMR**) or methods that
  consider time-series information (MotionBERT, PoseFormerV2, MotionAGFormer) — and note these lifters improve 2D
  accuracy even when a depth estimate is not required.
- For very high inference speed with good 2D accuracy: **BlazePose 'Local', discarding the depth estimates.**
- **Fine-tune on application-specific datasets.** The paper lists this alongside avoiding partially occluded joint
  angles and specifying participant posture/orientation to limit depth measurement, and notes that training on
  application-specific data "as done with BlazePose, seems to be highly beneficial". This is the most directly
  actionable recommendation for a dance-domain project.
- Lifting methods introduce latency (long input sequences, and much more if future frames are included), so they
  suit applications that do not require real-time results but benefit from accuracy — tracking rehabilitation
  progress, measuring range of motion.

## 5. Relation to the work it cites

- **Benchmark lineage.** Fig. 1 plots 3D MPJPE on Human3.6M under Protocol 1 (subjects 9 and 11 for testing, no
  Procrustes alignment) across Ionescu et al. → Li et al. → Tung et al. → Zhou et al. → Cai et al. → Zhao et al.,
  showing a steady accuracy increase from architecture improvements, changed approaches and more training data.
  *(Our reading, not the paper's claim — flagged because it is tempting and confounded:* one could read this
  paper as asking what those Human3.6M gains are worth on *exercise* poses against *OMC*, since 146–249 mm 3D
  MPJPE is far worse than Human3.6M-protocol numbers. **The paper never makes that comparison**, and it would be
  confounded anyway: different ground truth, different joint-centre definitions, no Procrustes alignment here, and
  dataset-wide averaging that deliberately includes self-occluded views. The paper in fact flags the definition
  problem as future work — collecting datasets "with joint locations defined similarly to established methods".
  Do not cite this comparison as the paper's.*)*
- **Architecture history it summarises:** hand-crafted features (HOG/SIFT) → DeepPose (cascaded direct regression)
  → heatmaps → Convolutional Pose Machines (large receptive fields; easy joints improve hard joints) → stacked
  hourglass → pyramid residual / cascaded pyramid → HRNet (parallel resolutions) → multi-person top-down vs
  bottom-up (PAFs) → one-stage (RTMO, Dynamic Bin Allocation/Encoding) → SimCC classification (RTMPose) →
  BlazePose regression. Model-based (e.g. SMPL) vs model-free (direct / lifting) is the 3D split.
- **Dataset context:** positions Physio2.2M against HumanEva, Human3.6M, MPII, COCO and AMASS as the general sets
  that lack irregular poses, and against MOYO and Fit3D as the few comparable exercise-focused ones.
- **Clinical/biomechanical grounding:** the <5° clinical threshold, the visual-assessment baselines, and the
  soft-tissue-artifact and Conventional Gait Model literature are what turn raw millimetres into a usability
  verdict. This is the part that distinguishes it from a pure computer-vision benchmark.

## 6. Strengths and weaknesses (pass-3 style)

**Strengths to borrow.**
- The metric suite is well constructed and reusable: raw MPJPE *plus* Procrustes-aligned MPJPE *plus* per-axis
  decomposition. The per-axis decomposition is what makes the depth finding visible at all — an aggregate MPJPE
  would have hidden it.
- Reporting **detection ratio alongside accuracy** is methodologically important. *(The reasoning here is ours,
  not the paper's — the paper reports the ratios and states that undetected frames were excluded, and the Fig. 3
  caption notes the ratio varies significantly, but it does not spell out the consequence.)* Error metrics
  computed only on detected frames are optimistically biased, so a model at 14.40 % detection is not comparable
  to one at 100 % no matter how good its MPJPE looks.
- Quantifying the error of its own ground truth, then arguing the comparison survives it, is exactly the right move.
- Evaluating **direct × lifting combinations** rather than single models surfaces the non-obvious result that the
  choice of upstream 2D estimator moves 3D MPJPE by up to 40 mm.

**Weaknesses / attack surface.**
- **The dataset is not public.** The central contribution cannot be independently re-used or reproduced; it is
  "available from the corresponding author on reasonable request" only.
- **The per-model numbers live in supplementary tables S1–S5, which are not in the distributed PDF.**
  Any claim about a specific model other than the handful named in the Results text cannot be checked from the
  article body alone.
- **Averaging over camera angles and exercises** mixes a controlled factor (frontal vs sagittal) into a single
  number. The paper acknowledges this, and its own subsequent analysis shows the frontal/sagittal split drives the
  ē_y > ē_x result — so a per-condition breakdown would have been more informative than the grand mean.
- **Self-occlusion is baked into the design** (two cameras always occluded for some exercises) rather than being an
  isolated variable, so "general accuracy" here is partly a property of this camera rig.
- **The angle set is narrow** — only knee and elbow flexion, both assumed to be 1-DoF hinges. No rotation, no
  shoulder, no trunk. The upper-extremity ground truth is also the weakest part of the CGM (~10° per the
  Heidelberg-model reference), which makes the elbow verdict softer than the knee verdict. **The authors agree:**
  their own future-work section calls for studies of isolated joint flexion without self-occlusion and for
  developments that increase the accuracy of upper-limb joints and angles — i.e. they flag the elbow/upper-limb
  result as the weakest part of their own finding.
- **n = 25, homogeneous**, no impaired participants — a notable limitation for a paper whose title claims
  *clinical* movement analysis.
- The **BlazePose 'Local' depth normalisation is an educated guess** by the authors, which weakens any comparison
  involving BlazePose-Local depth specifically.

## 7. Source-credibility check (per `reading_guide.md`)

*Scientific Reports* is peer-reviewed and open access under CC BY 4.0, and is not a predatory venue. Its SJR
quartile for multidisciplinary sciences is commonly Q1/Q2 — **not verifiable from the article itself; look it up on
scimagojr.com and record the date before quoting a quartile in the thesis.** It is a mega-journal, so venue prestige
alone carries less weight than for a CORE A*/A conference; the credibility here rests more on the institutional
base (ETH Zurich D-HEST, Akina AG, Schulthess Klinik Human Performance Lab, Medical Faculty Univ. Zurich), the
capture venue (Swiss Center for Movement Analysis at Balgrist Campus, acknowledged for support and infrastructure —
not an author affiliation), and on the fact that the methodology is stated in checkable detail. No competing
interests declared; open-access funding by ETH Zurich. **Safe to cite.**

---

## 8. CHECKLIST PASS — `knowledge/reading_checklist.md`

The checklist is a *reading-priority list* for the whole corpus, not a per-paper questionnaire. It is therefore
walked item by item below, stating what **this** paper (A1-14) says about each and flagging coverage. Most
items are other papers and are correctly **not covered** by this one; the substantive entries are #5 (this
paper), #22 (BlazePose), and experiments **E6** and **E5**.

`reading_checklist.md` was **not modified** — input only.

### TIER 0

| # | Item | What this paper says | Verdict |
|---|---|---|---|
| 1 | A1-21 Galata/Johnson/Hogg VLMM | Nothing. Different problem (behaviour modelling vs pose measurement). | **Not covered** |
| 2 | A1-12 SinMDM | Nothing. No generation, no diversity metrics. | **Not covered** |
| 3 | A0-9 DASB | Nothing. No tokenisation or bitrate content. | **Not covered** |
| 4 | A0-8 Discrete speech tokens review | Nothing. | **Not covered** |
| **5** | **A1-14 — this paper** | **Fully addressed, with three corrections to the checklist's own numbers.** See the claim-by-claim table below. | **Addressed (with corrections)** |

**Item 5 — claim-by-claim against the source:**

| Checklist claim | Paper says | Verdict |
|---|---|---|
| "Rode et al. (2025), *Scientific Reports*, doi:10.1038/s41598-025-22626-7" | Matches exactly. | ✅ |
| "BlazePose Heavy World 3D MPJPE 146 mm" | Confirmed — BlazePose 'World' 'Heavy', 3D MPJPE **146 mm**, best-performing direct 3D method (ē_x 50 / ē_y 58 / ē_z 108 mm; 98.8 % detection; 147 FPS). | ✅ |
| "2D ~80 mm" | **Not verifiable from the PDF.** The main text gives the 2D range 72–122 mm and names only RTMPose 'Performance' (72 mm) and MotionAGFormer-on-BlazePose-Local-Heavy (61 mm). BlazePose 'Local' 'Heavy' has no 2D MPJPE stated in the article body — that number would be in **Supplementary table S1, which is not bundled with the PDF**. | ⚠️ **Unverified** |
| "knee flexion MAE 14.1–31.2°" | **Wrong upper bound.** The paper reports knee flexion **3D MAE 14.1–25.8°** (abstract and discussion; the Results section says 25.9°) and **2D MAE 9.3–21.9°**. The values 31.2°, 23.7°, 41.3° and 35.0° — which also appear in the A1-14 entry of `paper_notes/paper_chain.md` — **do not occur anywhere in the paper.** | ❌ **Must be corrected** |
| "error in depth 2–3× higher than in-plane" | Confirmed in substance: the mean absolute depth error is approximately two to three times greater than the mean absolute horizontal and vertical errors, for all pose estimators investigated. | ✅ |
| "threatens half of the 36 angle features that depend on z" | The paper supports the *premise* (depth is 2–3× worse). It says nothing about our feature vector. Note `paper_chain.md` already establishes from our own code that **all 36** angle features consume `v_p_z`, not half — so the checklist wording understates the exposure. | **Partially addressed** (premise yes; the "half" figure is ours and is contradicted by our own code audit) |
| "ผลที่ต้องทำต่อ: z-zeroed vs full 3-D tokenization" | The paper's own recommendation points the same way: keep angles of interest **in the image plane**, or use multi-view. It also notes BlazePose 'Local' with depth discarded is the fast, accurate 2D option — effectively the z-zeroed configuration. | **Addressed / reinforced** |
| "⏱ pass 2" | Followed; pass 2 complete, partial pass 3 (equations re-derived; no author code is released). | ✅ |

### TIER 1 (items 6–13)

Rhythm is a Dancer, Keyposes, FSQ, Labrak, Matrix Profile VI, Atomic Movements, MotionCritic, Scaling Laws with
Vocabulary — **none covered**. This paper contains no tokenisation, vocabulary-size, clustering, motif-discovery or
generation content. One indirect touch: item 12 (MotionCritic / human perception of motion quality) shares this
paper's underlying concern — that automatic numbers may not match human judgement — but from the opposite side
(this paper measures *against instruments*, not perceptions). **Not covered.**

### TIER 2 (items 14–23)

| # | Item | Relevance here | Verdict |
|---|---|---|---|
| 22 | **A1-6 BlazePose** (arXiv:2006.10204) | **Substantially addressed.** The paper describes BlazePose's architecture (two-stage top-down, hourglass-inspired, dual heatmap + regression training paths sharing an encoder, heatmap path removed at inference, skip-frame detection mechanism), its `Lite`/`Full`/`Heavy` variants and `Local`/`World` modes, its GHUM-based hand-labelled yoga/fitness training set — **and independently benchmarks it against OMC**. For our purposes this is a stronger source on BlazePose's *measured behaviour* than the BlazePose paper itself, which reports no OMC comparison. | **Addressed** |
| 16 | A0-1 Human Motion Generation survey | Adjacent field only; no generation content. | Not covered |
| 19 | A1-20 Skeleton Motion Words (per-joint separation) | Indirect support: per-joint Procrustes-aligned errors differ sharply (hip smallest, wrists and ankles largest), which is evidence that **joints are not equally reliable** and therefore arguably not equally weightable in a whole-body feature vector. The paper does not discuss joint subsets. | **Partially addressed** |
| 23 | L3-20 DisCoRD (jitter as a known property) | Indirect: PoseFormerV2's DCT frequency filtering is described as reducing high-frequency noise and jitter arising from frame-to-frame 2D estimation — i.e. the paper names **estimator-side jitter** as a real, documented phenomenon with a known mitigation. Useful for our Limitations section. | **Partially addressed** |
| 14, 15, 17, 18, 20, 21 | Text2Tradition, Joshi & Chakrabarty, Motion Texture, DC-Motion, dance-token papers, chor-rnn | No content. | Not covered |

### TIER 3 (items 24–31, Phase 2 / descoped)

**Not covered.** No energy curves, time-series clustering, narrative structure, Laban analysis or audio segmentation.
One small crossover: item 28 (Camurri Quantity of Motion, computed from silhouette pixels vs our landmark velocity)
— this paper quantifies how much the landmark positions themselves are in error (72–122 mm in 2D), which is a useful
bound to cite whenever a *derived* landmark quantity such as velocity is claimed to be meaningful. **Partially relevant.**

### "ต้องให้คุณช่วย" (paywalled / blocked)

Not applicable to this paper — it is open access and the PDF is local. **However, one new blocked item is added by
this read: Supplementary tables S1–S5 are not in the local PDF** and are needed for any per-model number beyond the
few quoted in the Results text. They are freely available at the article DOI. **Action: fetch the supplementary
information from https://doi.org/10.1038/s41598-025-22626-7 before citing "BlazePose 'Local' ≈ 80 mm".**

### Experiments the reading mandates (E1–E7)

| # | Experiment | This paper's bearing | Verdict |
|---|---|---|---|
| **E6** | **z-zeroed vs full 3-D tokenization** | **Directly mandated and reinforced.** Depth error is 2–3× in-plane for *every* 3D estimator, and BlazePose 'World' 'Heavy' has ē_z 108 mm vs ē_x 50 / ē_y 58 mm. **The paper's strongest statement for us:** the largest limitation of monocular markerless estimators is depth accuracy, and *"limiting their use to 2D applications with optimal camera orientations could potentially achieve the desired level of accuracy"* — i.e. the paper itself says the z-zeroed configuration is the one that might reach clinical-grade accuracy. Its other advice ("keep angles in the image plane"; BlazePose 'Local' with depth discarded is accurate and fast) points the same way. **Additional evidence from this read:** BlazePose 'Local' depth normalisation is undocumented and the authors had to guess it — one more reason not to trust our z channel. **Caveat on which row to cite:** `models/pose_landmarker_heavy.task` is the MediaPipe heavy bundle, which exposes *both* normalised ('Local') and metric ('World') landmarks. The applicable benchmark row depends on which output `src/tokenize_with_model.py` consumes — if it reads normalised landmarks, the relevant row is BlazePose 'Local' 'Heavy', whose 2D MPJPE is **not in the article body** and whose depth is the channel degraded by the guessed normalisation constant. Check the code before citing 146 mm against our pipeline. | **Addressed — highest-value experiment confirmed** |
| **E5** | continuous-baseline LSTM on raw landmarks | Indirect but relevant: raw landmarks carry 72–122 mm (2D) / 146–249 mm (3D) of measurement error, so a "continuous" baseline is not error-free ground truth either. Worth stating when framing what discretisation costs. | **Partially addressed** |
| **E7** | corpus-free metrics incl. limb-length SD, foot-skating % | Indirect support: wrists and ankles have the largest Procrustes-aligned errors → limb-length SD and foot-skating computed from BlazePose output will contain estimator error, not only model error. A floor should be reported. | **Partially addressed** |
| E1, E2, E3, E4 | mSTAMP subspace, VLMM baseline, velocity+dedup, vocab sweep | No bearing. | **Not covered** |

### Checklist verdict

**Item 5 (A1-14) is now read and can be ticked** — with the correction that its knee-flexion figure is wrong and
must be changed to **14.1–25.8° (3D) / 9.3–21.9° (2D)**, and its "2D ~80 mm" marked unverified pending the
supplementary tables. **No other checklist item is advanced by this paper**, though #22 (BlazePose) is
substantially covered as a by-product. Nothing in the paper contradicts the Tier ordering. The one new action it
adds is fetching Supplementary Information S1–S5.

---

## 9. Discrepancies found in the paper itself

Five internal inconsistencies, all minor individually but worth knowing before quoting:

1. **Knee flexion 3D MAE upper bound:** abstract and discussion say **25.8°**; the Results section says **25.9°**.
   Quote 25.8° (it appears twice, including the abstract), or quote the range as "≈14–26°".
2. **Lifting inference-speed upper bound:** abstract says **9341 FPS**; the Results section says **9339 FPS**.
   Immaterial to any argument; quote as "≈9.3 kFPS".
3. **The stated 2D ranges exclude the paper's own best 2D result** (61 mm / 8.5° falls outside 72–122 mm /
   9.3–21.9°). The ranges describe the 18 *direct* 2D models only; the paper never says so. See §3.1.
4. **'Global' vs 'World':** the BlazePose metric mode is called 'World' throughout, except once in the
   PoseFormerV2 description where it is called BlazePose **'Global'**. Same mode.
5. **Duplicated bibliography entries.** Ref 10 and ref 20 are the same paper (Munea et al., *IEEE Access* 8,
   133330–133348, 2020). Ref 68 and ref 82 are the same paper (McGinley et al., 2009). The second duplication is
   **not cosmetic** — see the note in §4.1: it means the <5° clinical threshold and the <5° OMC knee-flexion error
   come from one and the same source.
6. Also note a figure cross-reference slip: the exercises are introduced with "(Fig. 2b)" but the exercises are
   shown in Fig. 2**c**; Fig. 2b is the marker set.
7. Cosmetic: the PDF's running footer is a mangled interleaving of the citation line and the Springer
   "content courtesy of" notice, and the final copyright line reads "© The Author(s) 2026" while the citation line
   resolves to (2025) 15:38767. Cite as **Sci Rep 15:38767 (2025)**, consistent with the DOI and the
   accepted date of 30 September 2025.

## 10. Coverage gaps in this read

- **Supplementary tables S1–S5 are not in the local PDF.** Per-model exact values (all 18 2D and 26 3D
  configurations), per-joint PAPE values, per-model detection ratios, and the sources for Fig. 1 are therefore
  unavailable. Everything in this summary comes from the article body.
- **No code or data.** The dataset is not public and no author implementation is released, so the pass-3
  "virtually re-implement" step could not be performed on the experiments themselves — only on the metric
  definitions, which were re-derived from Eqs. 1–9 and are self-consistent.
- Figures 3–5 are boxplots and skeleton renderings; exact values cannot be read off the extracted text, so only
  values stated in prose are quoted here.

## 11. Actions for the project

1. **Correct the A1-14 entry in `knowledge/paper_notes/paper_chain.md`** (~line 1367) and item 5 of
   `reading_checklist.md`: the flexion-MAE ranges 9.3–23.7 / 14.1–31.2 / 21.5–41.3 / 16.3–35.0 are not in the
   paper. Published values: knee 2D **9.3–21.9°**, knee 3D **14.1–25.8°**, elbow 2D **21.5–28.9°**,
   elbow 3D **16.3–26.0°**.
2. **Remove or re-source the quoted phrase** "depth estimation remains substantially inaccurate" in the
   `paper_chain.md` A1-14 entry — that string does not appear in the paper. The supportable paraphrase is:
   *the mean absolute depth error is approximately two to three times greater than the in-plane errors for all
   estimators investigated*; the Conclusion's own wording is that 3D pose estimators and transformer-based
   approaches do not currently deliver accurate depth estimations.
3. **Fetch Supplementary tables S1–S5** before citing any per-model number not named in the Results text —
   including "BlazePose 'Local' ≈ 80 mm".
4. **Run E6 (z-zeroed vs full 3-D tokenization).** Best-supported experiment in the current backlog.
5. **Cite this paper as the measurement-error floor** in the thesis Limitations: our landmarks come from
   BlazePose Heavy, benchmarked here at 146 mm 3D MPJPE / 108 mm mean absolute depth error. **Use the paper's own
   argument, which is stronger than "the footage is easier":** the authors attribute BlazePose's top ranking partly
   to a train/test distribution match — it was trained on a purpose-captured yoga/fitness dataset whose poses are
   *highly similar to the exercises in Physio2.2M*. Dance is outside that distribution, so **146 mm should be
   treated as an optimistic floor for our pipeline, not a transferable figure.** (The lab conditions — uniform
   lighting, single person, tight clothing — are a second, independent reason, which the paper also states.)
6. Optional but cheap: the paper's advice to prefer in-image-plane angles argues for recording or selecting dance
   clips where the salient motion is roughly parallel to the image plane, where we have that choice.

---

## 12. Verification (independent second pass)

A separate verification agent re-read the paper from the PDF — re-extracting the text itself and confirming its
extraction was byte-identical to the one used for the draft — then audited this summary against the source
following the same Three-Pass method. **Verdict: REVISE — safe to file with the corrections below applied; no
re-read of the source required.** All corrections it produced have been incorporated into the text above.

**What it checked.** Every numeric claim (~70) grepped against the full text with line references; every
non-numeric claim about method, causes, recommendations and limitations; the draft's four *negative* claims
(that certain strings do not appear in the paper); the two claimed internal inconsistencies; and the reference
identities behind the Five-Cs "Context" row.

**What it confirmed.**
- **No fabricated number, model, metric or citation anywhere in the draft.** Every figure resolves to the paper,
  attributed to the correct model, metric and dimension, with no rounding drift: the 2D/3D MPJPE ranges, all
  per-axis and PAMPJPE values for RTMPose 'Performance', BlazePose 'World' 'Heavy' and MotionAGFormer-on-BlazePose
  'Local' 'Heavy', all four flexion-MAE ranges, FPS figures, detection ratios, demographics, the camera/marker
  counts and rates, the OMC/CGM error block, and the whole visual-assessment comparison.
- **The draft's central deliverable stands.** The strings `23.7`, `31.2`, `41.3`, `35.0` and the phrase
  "substantially inaccurate" return **zero hits** in the full text. The verifier independently located the
  fabricated values at `knowledge/paper_notes/paper_chain.md:1367–1368` and confirmed the "all 36 features consume
  `v_p_z`" code audit at `:1539`. The corrections in §11.1–11.2 should be actioned.
- Both claimed internal inconsistencies (25.8° vs 25.9°; 9341 vs 9339 FPS) are real and correctly located.

**Corrections it produced, now applied.**
1. **Scope of the "18 2D models" ranges** — the paper's own best 2D result (61 mm / 8.5°) falls *outside* the
   stated 72–122 mm / 9.3–21.9° ranges, so those ranges cover only the 18 **direct** 2D models. Added as a scope
   note in §3.1 and as discrepancy #3 in §9.
2. **The lifting cross-product was asserted, not stated.** The paper never says every lifter ran on every 2D
   estimator, and 3 × 18 = 54 ≠ the 26 reported 3D configurations. §2.3 rewritten.
3. **"No dataset" overstated** the paper's "only few datasets" / "lack of datasets with a strong focus on physical
   exercise". §1 softened.
4. **"Detectron2 is the weakest"** → the paper says "lower accuracy", not lowest, and gives no body-text ranking.
5. **"2D beats the eye"** → the paper's "majority … outperform" sentence is about **3D**; for 2D it says only
   that *some* estimators are *comparable to or better than* visual assessment. §3.3 heading and §0b reworded.
6. **Three further source defects added to §9**: 'Global' vs 'World'; duplicated references (10≡20, 68≡82);
   the Fig. 2b/2c cross-reference slip.
7. **Interpretation now labelled as interpretation** in three places: the Human3.6M comparison in §5 (the paper
   never makes it, and it is confounded by differing ground truth, joint-centre definitions and the absence of
   Procrustes alignment), the BlazePose-Local depth-artefact inference in §4.5, and the detection-ratio argument
   in §6.
8. **"Reproducible in principle"** softened to "re-implementable in principle, though not reproducible in
   practice", consistent with §10.
9. Source-credibility fixes: the Swiss Center for Movement Analysis is the capture venue and an acknowledgement,
   not an author affiliation; the SJR quartile is not checkable from the article and now carries a lookup caveat.

**Omissions it caught, now added.**
- The <5° clinical threshold and the "<5° OMC knee-flexion error" figure are cited to **the same reference**
  (McGinley et al. 2009, duplicated as refs 68 and 82) — so the ground truth's own knee error sits on the very
  line used to declare HPE unusable. Added to §4.1.
- The paper's explicit forward claim that **2D-only use with optimal camera orientation could reach the desired
  accuracy** — the strongest in-source justification for E6. Added to §3.3 and quoted in the E6 row of §8.
- **Fine-tuning on application-specific datasets** as the paper's own improvement route. Added to Recommendations.
- BlazePose's rank-1 result is partly a **train/test distribution match** (yoga/fitness training data highly
  similar to Physio2.2M) — a stronger and more citable caveat than "dance footage is harder". Added to §11.5.
- PoseFormerV2 also fills gaps and also returns metric units; the lifters' depth shortfall is attributed by the
  paper to training-dataset differences; the 3–54 mm soft-tissue-artifact source is hip-specific; and the authors'
  future-work section itself flags the upper-limb result as their weakest. All added.

**Residual risk.** One blocking dependency remains for any claim beyond this note: **Supplementary tables S1–S5**
must be fetched before citing per-model numbers not named in the Results text (including "BlazePose 'Local'
≈ 80 mm"). This was already flagged in the draft and the verifier agreed it is correctly scoped.
---
---

# ฉบับภาษาไทย

# การประเมินโมเดลประมาณท่าทางมนุษย์แบบกล้องเดี่ยว สำหรับการวิเคราะห์การเคลื่อนไหวทางคลินิก

**Rode, D.; Dunkel, A.; Willi, R.; Wolf, P.; Xiloyannis, M.; Riener, R.**
*Scientific Reports* (2025) 15:38767 · DOI 10.1038/s41598-025-22626-7 · Open Access (CC BY 4.0)
สังกัด: ETH Zurich (D-HEST), Akina AG, Schulthess Klinik, คณะแพทยศาสตร์ มหาวิทยาลัยซูริก
รับบทความ 15 เมษายน 2025 · ตอบรับ 30 กันยายน 2025 · ผู้เขียนแจ้งว่าไม่มีผลประโยชน์ทับซ้อน

ไฟล์: `knowledge/reading_docs/Assessment_of_monocular_human_pose_estimation_mode.pdf` · รหัสในโปรเจกต์: **A1-14**
(Tier 0 ข้อ 5 ของ `reading_checklist.md`) · อ่านตาม `reading_guide.md` (Three-Pass ของ Keshav)
ระดับที่อ่านถึง: **pass 2 เต็ม + pass 3 บางส่วน** (ไล่สมการซ้ำและเทียบกับเนื้อความ แต่ไม่มีโค้ดผู้เขียนและไม่มีตาราง
supplementary — ดูหัวข้อ *ช่องว่างของการอ่านรอบนี้*)

---

## 0. Five Cs (pass 1)

| C | คำตอบ |
|---|---|
| **Category** | งานวัดผลเชิงทดลอง / benchmark ไม่ใช่วิธีใหม่ — สร้างชุดข้อมูล ground truth ใหม่แล้ววัดระบบโอเพนซอร์สที่มีอยู่ 11 ตัว |
| **Context** | ต่อยอดจาก survey ด้าน HPE (Chen 2020, Zheng 2023, Wang 2021), สาย benchmark 3D (Human3.6M, HumanEva, MPII, COCO, AMASS; เฉพาะการออกกำลังกาย: MOYO, Fit3D) และวรรณกรรมชีวกลศาสตร์คลินิกเรื่อง Conventional Gait Model กับ soft-tissue artifact (Leboeuf 2023, Baker 2017, Peters 2010) |
| **Correctness** | สมมติฐานสมเหตุผล และผู้เขียน **วัดความคลาดเคลื่อนของ ground truth ตัวเองด้วย** แล้วแสดงว่าความคลาดของ HPE ใหญ่กว่าหลายเท่า → การเทียบยังใช้ได้ · วิธีเก็บข้อมูล การซิงก์ และการจัดการระบบพิกัด เขียนละเอียดพอจะ **สร้างขึ้นใหม่ได้ในหลักการ แต่ทำซ้ำจริงไม่ได้** — ไม่มีข้อมูล ไม่มีโค้ด ไม่มีตาราง supplementary และมีค่าคงที่ normalisation ความลึกที่ได้จากการเดา (ดู *ช่องว่างของการอ่านรอบนี้*) |
| **Contributions** | (1) ชุดข้อมูล **Physio2.2M** — 2.2 ล้านเฟรม RGB ของการออกกำลังกาย คู่กับ ground truth จาก Vicon 27 กล้อง (2) benchmark เทียบตรงด้านความแม่น/ความเที่ยง/ความเร็ว ของตัวประมาณท่า 11 ตัว (18 config สำหรับ 2D; 26 config สำหรับ 3D ซึ่งรวมคู่ direct×lifting) (3) ระบุปริมาณ "ค่าปรับด้านความลึก" ของกล้องเดี่ยว (≈2–3 เท่าของความคลาดในระนาบภาพ) และที่มาของมัน |
| **Clarity** | ดี · เขียน metric เป็นสมการชัดเจน มีเหตุผลกำกับการเลือกโมเดล · มีจุดที่ขัดกันเองภายในหลายจุดแต่เล็กน้อย (ดูหัวข้อ *ตัวเลขขัดกันเอง*) และตารางผลรายโมเดลอยู่ใน supplementary ที่ไม่ได้แนบมากับ PDF |

## 0b. ตารางสกัด (แบบ อ.Proadpran)

| ช่อง | เนื้อหา |
|---|---|
| **Motivation** | OMC แบบติด marker แม่นแต่ตั้งระบบนาน แพง ต้องใช้ความรู้กายวิภาค → ใช้จริงในคลินิกหรือที่บ้านไม่ไหว · HPE กล้องเดี่ยวถูกและเร็ว แต่ **ไม่มีใครรู้ว่าผิดเท่าไหร่** บนท่าออกกำลังกายจริง เพราะชุดข้อมูลที่มี ground truth 3D ส่วนใหญ่ขาดท่าที่ผิดแปลก |
| **Research Question** | ตัวประมาณท่าแบบกล้องเดี่ยวที่ใช้กันจริง (off-the-shelf) แม่นแค่ไหน เที่ยงแค่ไหน เร็วแค่ไหน เมื่อวัดกับ OMC แบบติด marker — และพอใช้ตีความทางคลินิกหรือยัง |
| **Proposed Method** | เก็บชุดข้อมูลคู่ขึ้นมาเอง (Physio2.2M) แปลงพิกัด HPE กับ OMC ให้อยู่ระบบเดียวกัน แล้ววัดตัวประมาณ 11 ตัวด้วย MPJPE, MAE รายแกน, PAMPJPE, MAE มุมงอเข่า/ศอก, อัตราการตรวจพบ และ FPS |
| **Evaluation** | เฉลี่ยทั้งชุดข้อมูล — ทุกคน ทุกท่า ทุกมุมกล้อง **โดยตั้งใจ** เพื่อให้ได้ตัวเลข "ทั่วไป" ไม่ใช่ "ดีที่สุดที่เป็นไปได้" |
| **Contribution** | คู่มือเลือกตัวประมาณท่าตามข้อจำกัดที่มี + คำตอบชัดว่าเพดานตอนนี้อยู่ตรงไหน: **ยังไม่มีตัวไหนถึงเกณฑ์คลินิก (<5°)** แต่ตัวประมาณ 2D *บางตัว* แม่นเทียบเท่าหรือดีกว่าการประเมินมุมงอเข่าด้วยสายตา และเปเปอร์ระบุว่าตัวประมาณ *3D ส่วนใหญ่* แม่นกว่าการประเมินด้วยสายตา |

---

## 1. ปัญหาและแรงจูงใจ

OMC แบบ passive marker คือมาตรฐานทองที่ไม่รุกล้ำสำหรับการวัดการเคลื่อนไหวของมนุษย์ แต่แลกมาด้วยต้นทุนการใช้งานที่สูง:
ต้องล้อมพื้นที่วัดด้วยกล้องอินฟราเรด คาลิเบรตกล้อง ระบุจุดกายวิภาค และติด marker ลงบนจุดเหล่านั้น ความแม่นขึ้นกับการติด
marker ถูกตำแหน่ง และถูกบั่นทอนด้วย soft-tissue artifact รวมกับค่ากล้อง IR และค่าลิขสิทธิ์ซอฟต์แวร์ ทำให้ OMC
ถูกจำกัดอยู่ในงานวิจัยและพัฒนาเป็นหลัก

HPE กล้องเดี่ยวแบบไม่ติด marker ให้ข้อแลกเปลี่ยนตรงข้าม: กล้องตัวเดียว ไม่ต้องติด marker ตั้งระบบง่าย — น่าสนใจสำหรับ
การประเมินทางคลินิก การคุมการออกกำลังกาย การติดตามความก้าวหน้าของการบำบัด และการใช้เองที่บ้านโดยไม่มีผู้ดูแล
แต่วิธีกล้องเดี่ยวแม่นน้อยกว่าในแกนลึกและไวต่อการบังตัวเองมากกว่าวิธีหลายกล้อง อีกทั้งชุดข้อมูลที่ใช้ benchmark กันปกติ
(HumanEva, Human3.6M, MPII, COCO, AMASS) มีท่าผิดแปลกน้อย — MOYO และ Fit3D เป็นไม่กี่ชุดที่เน้นการออกกำลังกาย
**ช่องว่างที่เปเปอร์นี้จับ** จึงเป็น: มีชุดข้อมูล **เพียงไม่กี่ชุด** ที่ทำให้เทียบ HPE กับ OMC ระดับ SOTA ในสามมิติได้
และชุดที่เน้นการออกกำลังกายจริง ๆ ยิ่งมีน้อย (MOYO, Fit3D) → ความแม่นของเครื่องมือเหล่านี้บนท่าออกกำลังกาย
จึงยังแทบไม่ถูกระบุลักษณะ และไม่มีใครรู้ว่าใช้ทางคลินิกได้หรือยัง

## 2. วิธีการ

### 2.1 ชุดข้อมูล Physio2.2M

- **ผู้เข้าร่วม 25 คน** ไม่มีความบกพร่อง (ชาย 11 หญิง 14) อายุเฉลี่ย 26 ปี (ช่วง 20–33) ส่วนสูงเฉลี่ย 1724 มม.
  (1580–1920) น้ำหนักเฉลี่ย 68 กก. (47–94) · คัดผู้ที่ออกกำลังกายไม่ได้จากความบกพร่องทางกล้ามเนื้อ-กระดูก ระบบประสาท
  หรือการรู้คิดออก
- ท่าออกกำลังกายทั้งข้างเดียวและสองข้าง (*Shoulder Rotation and Elbow Flexion* และ *Squat* เป็นท่าสองข้าง
  ที่เหลือเป็นข้างเดียว) ท่าละ **3 เซ็ต × 5 ครั้ง**
- **Ground truth:** Vicon **27 กล้องอินฟราเรด** (Vero v2.2 22 ตัว, MX T10 3 ตัว, MX T20-S 2 ตัว) ที่ **200 Hz**
  จัดวางให้มุมมองซ้อนทับกันเพื่อกันการบัง marker
- **marker สะท้อนแสง 46 จุด** ใช้โมเดล **Plug-in Gait** (สายพันธุ์ที่ใช้กันแพร่หลายของ Conventional Gait Model)
  กู้ตำแหน่งข้อสะโพก เข่า ข้อเท้า ไหล่ ศอก ข้อมือ ด้วย Vicon Nexus 2.15 · marker 38 จุดติดบนจุดกายวิภาคโดย
  ผู้เชี่ยวชาญที่ผ่านการฝึก 2 คน ที่เหลืออยู่บนแถบคาดศีรษะ 4 จุด และแถบข้อมือข้างละ 2 จุด · คาลิเบรตโมเดลด้วย
  ท่า T-pose นิ่ง 15 วินาที ตามด้วยการหมุนขา แขน และลำตัวส่วนบน
- **วิดีโอ:** เว็บแคม Logitech HD C920 **4 ตัว ที่ 30 Hz** สองระดับความสูง (270 มม. และ 950 มม.) บนขาตั้งสองชุด
  ที่ตั้งฉากกัน ผู้เข้าร่วมอยู่ห่าง 3 ม. และ 3.5 ม. · จัดท่าให้กล้องคู่หนึ่งเห็นด้านหน้าเสมอ อีกคู่เห็นระนาบ sagittal
  · ติด marker บนกล้องเพื่อหาตำแหน่งและทิศทางของกล้องในระบบพิกัดโลก
- **การซิงก์:** ตบมือ แล้ว maximise cross-correlation ของตำแหน่งข้อมือระหว่างสองระบบ · ลดความถี่ OMC
  200 → 30 Hz ด้วย linear interpolation
- รวม **2.2 ล้านเฟรม RGB** พร้อมตำแหน่งศูนย์กลางข้อต่อ 3D ที่สอดคล้องกัน
- จริยธรรม: คณะกรรมการจริยธรรม ETH Zurich รหัส EK 2023-N-4 · ได้รับความยินยอมโดยแจ้งข้อมูลแล้ว
- **การเข้าถึงข้อมูล: ขอจากผู้เขียนเป็นราย ๆ เท่านั้น — ชุดข้อมูล *ไม่เปิดสาธารณะ*** (เหตุผลด้านความเป็นส่วนตัว)

### 2.2 การตั้งค่า inference

รันทุกโมเดลบนเครื่องเดียวกัน (AMD Ryzen 9 7900X, NVIDIA RTX 4080, RAM 128 GB, CUDA 12.2, Python 3) พร้อม GPU
· ประมวลผลแยกรายกล้อง (เพราะพิจารณาเฉพาะวิธีกล้องเดี่ยว) · แปลงท่าที่ประมาณได้เข้าระบบพิกัดของ ground truth
โดยใช้ทิศทางกล้องที่รู้ แล้ว **เลื่อนให้จุดกึ่งกลางสะโพกทับกับของ OMC** · แปลงพิกเซล→หน่วยเมตริกด้วยตัวคูณ
รายเฟรม-รายกล้อง = (ระยะจากกล้องถึงจุดกึ่งกลางสะโพกของ ground truth) / (focal length หน่วยพิกเซล)

### 2.3 โมเดลที่ทดสอบ

ตัวประมาณโอเพนซอร์ส 11 ตัว ขยายเป็น **18 config สำหรับ 2D และ 26 config สำหรับ 3D**:

- **2D แบบ direct:** OpenPose (bottom-up, PAFs), AlphaPose ('Fast Pose', backbone ResNet50 + ตัวตรวจจับ YoloV3,
  ชุด Halpe), HRNet (width 48, 384×288, COCO), Detectron2 (Keypoint R-CNN, ResNet-101 + FPN),
  RTMPose / RTMO / RTMW (แบบ SimCC จำแนกสองทาง; อย่างละ Lightweight / Balanced / Performance)
- **3D แบบ direct:** BlazePose รุ่น `Lite` / `Full` / `Heavy` × โหมด `Local` (พิกัดพิกเซลที่ normalise แล้ว)
  และ `World` (หน่วยเมตริก จุดกำเนิดที่กึ่งกลางสะโพก)
- **2D→3D lifting:** MotionBERT 'Lite' (243 เฟรม), PoseFormerV2 (243 เฟรม, อินพุตผ่าน DCT เข้าโดเมนความถี่ ·
  เป็นตัวเดียวในงานนี้นอกจาก BlazePose 'World' ที่คืนค่า landmark เป็นหน่วยเมตริก), MotionAGFormer 'Big'
  (243 เฟรม, transformer + GCN) — แต่ละตัวรันบนลำดับท่า 2D ที่ผลิตจากตัวประมาณแบบ direct ข้างต้น
  · **เปเปอร์ไม่ได้ระบุว่ารันคู่ direct×lifting คู่ไหนบ้าง** — ในส่วน Results และรูปภาพระบุชื่อเฉพาะคู่ที่รันบน
  BlazePose 'Local' 'Heavy' เท่านั้น · ถ้าเป็น cross-product เต็ม 3 lifter × 18 อินพุต 2D จะได้ 54 config
  แต่เปเปอร์รายงาน 26 config สำหรับ 3D → **ไม่ใช่ cross-product เต็ม** และองค์ประกอบที่แท้จริงกู้ได้จาก
  Supplementary S3–S4 เท่านั้น · ด้วยเหตุผลเดียวกัน รายการข้างต้นบวกกันแล้วไม่ได้ 18 หรือ 26 ตามที่เปเปอร์ระบุ
  — เปเปอร์ให้แต่ตัวเลขรวม ไม่ได้แจกแจงในตัวบทความ

### 2.4 Metric

เวกเตอร์ความคลาดชี้จากข้อต่อที่ HPE ทำนายไปยังข้อต่อที่ OMC วัดได้ แสดงในระบบพิกัดเฉพาะกล้อง
(x = แนวนอน, y = แนวตั้ง, z = แกนลึก) · เทียบ **12 ข้อต่อ**: ข้อมือ ศอก ไหล่ สะโพก เข่า ข้อเท้า ซ้ายและขวา

- `PE_{i,j}` = ความยาวยุคลิดของเวกเตอร์ความคลาด (สมการ 2); `MPJPE_i` = ค่าเฉลี่ย PE ของ 12 ข้อต่อ (สมการ 3);
  `MPJPE` = เฉลี่ยทุกเฟรม (สมการ 6) · ตัวประมาณ 2D ตัดพจน์ z ออก → **2D MPJPE**; ถ้ารวมความลึก → **3D MPJPE**
- **MAE รายแกน** `ē_x`, `ē_y`, `ē_z` เฉลี่ยทั้งรายข้อต่อและรายเฟรม (สมการ 4–5)
- **PAMPJPE** (สมการ 7): generalised orthogonal Procrustes แก้ด้วย SVD (ฟังก์ชัน `procrustes` ของ MATLAB R2023a
  **เปิด scaling ไม่ใช้ reflection**) เพื่อลดความคลาดด้านสเกลจากการแปลงพิกเซล→เมตริก และลดอิทธิพลเชิงระบบของ
  จุดกึ่งกลางสะโพก ทำให้เทียบความคลาดรายข้อต่อได้อย่างเป็นธรรม
- **MAE ของมุมงอ** (สมการ 8–9): ถือเข่าและศอกเป็นข้อต่อบานพับ 1 องศาอิสระ คำนวณมุมจากผลคูณสเกลาร์ ·
  ความคลาดของเฟรมคือค่าเฉลี่ยของความคลาดสัมบูรณ์ฝั่งซ้ายกับฝั่งขวา · รายงานทั้ง **3D MAE** (ใช้เวกเตอร์ 3D เต็ม)
  และ **2D MAE** (ฉายลงระนาบภาพ) เพื่อให้เทียบกับตัวประมาณ 2D ได้อย่างเป็นธรรม
- **อัตราการตรวจพบ:** เฟรมที่ตรวจไม่พบท่าถูกตัดออกจากการคำนวณ metric แล้วรายงานสัดส่วนแยกต่างหาก ·
  สำหรับวิธี lifting รายงานอัตราสุดท้ายหลังผ่านทั้งสายโซ่ 2D→lift
- **ความเร็ว inference:** จับเวลาแต่ละขั้นแล้วเฉลี่ยทั้งชุดข้อมูล · สำหรับวิธี lifting **นับเฉพาะขั้นตอน lift**

## 3. ผลลัพธ์สำคัญ

### 3.1 ตัวประมาณ 2D แบบ direct (คือ "18 โมเดล 2D" ที่เปเปอร์นับ)

| ปริมาณ | ช่วงของทุกโมเดล |
|---|---|
| 2D MPJPE | **72 – 122 มม.** |
| MAE มุมงอเข่า (2D) | **9.3° – 21.9°** |
| MAE มุมงอศอก (2D) | **21.5° – 28.9°** |
| ความเร็ว inference | **25 – 200 FPS** |
| อัตราการตรวจพบ | **56.50 % – 100 %** |

> ⚠️ **หมายเหตุเรื่องขอบเขต (เป็นจุดขัดกันเองจุดที่สามในต้นฉบับ)** ผลลัพธ์ 2D ที่ดีที่สุดของเปเปอร์เอง —
> MotionAGFormer บน BlazePose 'Local' 'Heavy' ได้ **2D MPJPE 61 มม.** และ **MAE มุมงอเข่า 8.5°** —
> อยู่ *ต่ำกว่า* ช่วง 72–122 มม. / 9.3–21.9° ที่ระบุไว้ · แปลว่าช่วงเหล่านั้นครอบคลุมเฉพาะโมเดล 2D
> แบบ **direct** ทั้ง 18 ตัว ไม่รวมท่า 2D ที่ผ่าน lifting · เปเปอร์ไม่ได้ระบุเรื่องนี้ไว้

- **ดีที่สุดแบบ direct — RTMPose 'Performance':** ē_x 37 มม., ē_y 52 มม., **2D MPJPE 72 มม.**,
  2D PAMPJPE 53 มม., เข่า **9.3°**, ศอก 24.9°, **ทำนายท่าได้ทุกเฟรม**, 30 FPS
- **ดีที่สุดโดยรวม — MotionAGFormer lift จาก BlazePose 'Local' 'Heavy':** ē_x 34 มม., ē_y 43 มม.,
  **2D MPJPE 61 มม.**, 2D PAMPJPE 46 มม., เข่า 8.5°, ศอก 22.1°, ตรวจพบ 100 % (**เติมช่องว่างที่พบทั้งหมดได้**
  — เปเปอร์ระบุความสามารถเติมช่องว่างนี้ให้ **ทั้ง** MotionAGFormer และ PoseFormerV2),
  4580 FPS เฉพาะขั้น lift → *วิธี lifting ช่วยให้ท่า 2D ในระนาบแม่นขึ้นด้วย ไม่ใช่แค่เติมความลึก*
- ตัวประมาณส่วนใหญ่มีความคลาดแบบ Procrustes ต่ำสุดที่ **สะโพก** · ยกเว้น RTMPose และ RTMO ที่แม่นกว่าที่ **เข่า**

### 3.2 ตัวประมาณ 3D (26 config)

| ปริมาณ | ช่วงของทุกโมเดล |
|---|---|
| 3D MPJPE | **146 – 249 มม.** |
| MAE มุมงอเข่า (3D) | **14.1° – 25.8°** (บทคัดย่อและ discussion; ส่วน Results เขียน 25.9° — ดู *ตัวเลขขัดกันเอง*) |
| MAE มุมงอศอก (3D) | **16.3° – 26.0°** |
| ความเร็ว inference (lifting) | **117 – 9341 FPS** (บทคัดย่อ; ส่วน Results เขียน 9339 — ดู *ตัวเลขขัดกันเอง*) |
| อัตราการตรวจพบ | **14.40 % – 100 %** |

- **ดีที่สุดแบบ direct — BlazePose 'World' 'Heavy':** ē_x 50 มม., ē_y 58 มม., **ē_z 108 มม.**,
  **3D MPJPE 146 มม.**, 3D PAMPJPE 110 มม., เข่า 17.2°, ศอก 18.3°, ตรวจพบ **98.8 %**, **147 FPS**
- **ดีที่สุดโดยรวม — MotionAGFormer บน BlazePose 'Local' 'Heavy':** ē_x 34 มม., ē_y 43 มม., **ē_z 119 มม.**,
  **3D MPJPE 146 มม.**, 3D PAMPJPE **105 มม.**, เข่า 16.7°, ศอก **16.3°**, ตรวจพบ 100 %, 4580 FPS
  — สังเกตว่าเสมอ BlazePose World Heavy ที่ 146 มม. โดยดีกว่าในระนาบแต่ **แย่กว่าในแกนลึก**
- ตัวประมาณ 3D **ทุกตัว** มีความคลาดตำแหน่งข้อต่อแบบ Procrustes ต่ำสุดที่สะโพก · ข้อมือและข้อเท้าแย่ที่สุด

### 3.3 สามผลลัพธ์ที่สำคัญที่สุด

1. **ความคลาดในแกนลึก ≈ 2–3 เท่าของความคลาดในระนาบภาพ สำหรับตัวประมาณ 3D ทุกตัวที่ทดสอบ**
   สาเหตุ: การบังตัวเอง (โดยการออกแบบ มี 2 ใน 4 กล้องที่เจอการบังตัวเองอย่างมีนัยเสมอ — ขาขวาตอน squat
   และแขนขวาท่อนบนตอน shoulder rotation / elbow flexion เมื่อมองระนาบ sagittal) และความกำกวมเชิงฉายภาพ
   ที่ติดมากับการประมาณความลึกด้วยกล้องเดี่ยว (จุดหลายจุดฉายลงเป็นจุดเดียวกันในภาพได้)
2. **ความคลาดแนวตั้งมากกว่าแนวนอนในทุกตัวประมาณ** — การวิเคราะห์ต่อเนื่องพบว่ามาจากมุมมองระนาบหน้า:
   เมื่อมองจากระนาบหน้า ē_y มากกว่า ē_x อย่างชัดเจน ส่วนมุม sagittal ทั้งสองแกนใกล้เคียงกัน · เนื่องจากใช้กล้อง
   frontal และ sagittal จำนวนเท่ากัน ค่าเฉลี่ยรวมของชุดข้อมูลจึงรับความไม่สมมาตรนี้มาด้วย
3. **ยังไม่ถึงเกณฑ์ใช้งานทางคลินิก แต่ที่ข้อเข่า ตัวประมาณบางตัวเทียบเท่าหรือดีกว่าการประเมินด้วยสายตา** —
   การตีความทางคลินิกต้องการความคลาดของมุม **ต่ำกว่า 5°** ซึ่ง **ไม่มีตัวไหนทำได้** · แต่มีรายงานว่าการวัดมุมงอเข่า
   ขณะวิ่งด้วยสายตาของผู้ประเมินมนุษย์มีความคลาด **−54° ถึง 21°** (MAE ที่อ่านจากรูปต้นทาง ≈ **20.6°**)
   และมีความสอดคล้องต่ำแม้ในผู้สังเกตที่มีประสบการณ์ · ถ้อยคำของเปเปอร์เองระมัดระวัง: ตัวประมาณ 2D
   **"บางตัว"** (9.3–21.9°) แม่น *เทียบเท่าหรือดีกว่า* การตรวจด้วยสายตา ส่วน **"ตัวประมาณ 3D ที่ศึกษาส่วนใหญ่
   แม่นกว่าการประเมินมุมงอเข่าด้วยสายตา"** (14.1–25.8°) · **แต่ที่ข้อศอกผลกลับด้าน:** ผู้ประเมินที่เชี่ยวชาญได้ MAE **8.4°** (มุมงอกว้าง) และ **12.2°** (มุมงอแคบ)
   ขณะที่ตัวประมาณอยู่ที่ 21.5–28.9° (2D) และ 16.3–26.0° (3D) — **ปัจจุบัน HPE แพ้การตรวจด้วยสายตาที่ข้อศอก**
   · ตัวเลขความเชื่อถือประกอบ: ความเชื่อถือระหว่างผู้สังเกตของมุมศอก 0.38 (ผู้ไม่มีประสบการณ์เทียบศัลยแพทย์ผู้เชี่ยวชาญ)
   ถึง 0.96 (ผู้เชี่ยวชาญสองคน) · ICC ของการประเมินมุมเข่าด้วยสายตา 0.82–0.97 · มีมือใหม่เพียงราว **16.8 %**
   ที่ประเมินมุมศอกได้โดยมีสหสัมพันธ์อย่างมีนัยสำคัญ

4. **ข้ออ้างเชิงอนาคตของเปเปอร์เอง — การใช้แบบ 2D ล้วนอาจถึงเกณฑ์ความแม่นทางคลินิกได้** เปเปอร์ระบุว่า
   ข้อจำกัดใหญ่ที่สุดของตัวประมาณกล้องเดี่ยวคือความไม่แม่นในการประมาณความลึก และแม้ความแม่น 3D โดยรวม
   จะยังไม่พอสำหรับการตีความทางคลินิก แต่ **การจำกัดการใช้งานไว้ที่ 2D พร้อมมุมกล้องที่เหมาะสม อาจไปถึงระดับ
   ความแม่นที่ต้องการได้** และในบทสรุประบุว่าความแม่นดีขึ้นมากเมื่อจำกัดกรณีใช้งานไว้ที่ 2D โดยไม่ประมาณความลึก
   · นี่คือเหตุผลจากตัวเปเปอร์ที่หนักแน่นที่สุดสำหรับการทดลอง **E6** ของเรา (ดูหัวข้อ 8)

### 3.4 ทำไมโมเดลจึงต่างกัน (คำอธิบายของผู้เขียนเอง)

- **Detectron2 แม่นน้อยกว่า** ตัวที่ออกแบบมาเพื่องานนี้โดยตรง — Keypoint R-CNN ไม่ได้ออกแบบมาเพื่อ HPE โดยเฉพาะ
  จึงไม่พิจารณาบริบทกับความสัมพันธ์เชิงพื้นที่ตอนทำนายตำแหน่งข้อต่อ (เปเปอร์ **ไม่ได้** จัดอันดับให้อยู่ท้ายสุด
  ค่ารายโมเดลอยู่ในตาราง S1–S2)
- **HRNet ชนะ OpenPose/AlphaPose** เพราะเส้นทางความละเอียดสูงแบบขนานทำให้ไม่ต้องกู้ feature ความละเอียดสูง
  กลับจากความละเอียดต่ำ
- **ตระกูล RTMPose/RTMW/RTMO แม่นที่สุดในกลุ่ม 2D** — SimCC จำแนกแยกอิสระรายแกน ได้ความละเอียดระดับ sub-pixel
  และลดความคลาดจาก quantisation ของ heatmap อีกทั้งใช้ transformer จับความสัมพันธ์ระหว่างข้อต่อทั้งระดับ global และ local
- **BlazePose แม่นทั้งที่ใช้ regression ตรงและไม่มีเครือข่ายขนาน** — อธิบายได้จาก (ก) ชุดฝึกที่ label ด้วยมือโดยใช้
  ground truth 3D จากโมเดล GHUM และ **เน้นท่าโยคะกับฟิตเนสซึ่งคล้ายชุดข้อมูลนี้มาก** และ (ข) encoder
  ถูกฝึกด้วยการทำนาย heatmap แม้เส้นทาง heatmap จะถูกถอดออกตอน inference · ความเร็วมาจาก regression
  บวกกลไก skip-frame (รันการตรวจจับใหม่เฉพาะเมื่อไม่เห็นคนในภาพ)
- **วิธี lifting** เร็ว (อินพุตเล็กกว่า) และ *ช่วยความแม่นในระนาบ* ได้ เพราะจับความสัมพันธ์เชิงเวลาและเชิงพื้นที่ข้ามเฟรม
  แต่ **การประมาณความลึกของมันแพ้ BlazePose** ซึ่งเป็น direct estimator — เปเปอร์สันนิษฐานว่าน่าจะมาจาก
  **ความแตกต่างของชุดข้อมูลฝึก** · PoseFormerV2 แม่นกว่า MotionBERT
  เล็กน้อยในลำดับอินพุตส่วนใหญ่ (การกรองในโดเมนความถี่ลด noise และ jitter) แม้ MotionBERT จะดีกว่าในระนาบ
  แต่แย่กว่าในแกนลึก · MotionAGFormer เป็น lifter ที่แม่นที่สุด (transformer + GCN) แต่เร็วราวครึ่งเดียวของ MotionBERT
- **ความแม่นของ lifting ขึ้นกับตัวประมาณ 2D ที่ป้อนเข้าไปอย่างมาก — 3D MPJPE ต่างกันได้ถึง 40 มม.**
- บริบท real-time: แม้แต่วิธีสองขั้นรุ่นแรก ๆ (OpenPose, Detectron2, HRNet, AlphaPose) ก็เกิน **15 FPS**
  ซึ่งเป็นเกณฑ์ที่เกี่ยวกับความพึงพอใจของผู้ชมและสมรรถนะ real-time

## 4. สมมติฐานและข้อจำกัด

ตามที่ผู้เขียนระบุเอง:

1. **Ground truth เองก็ไม่สมบูรณ์** — OMC แบบ passive marker กับ Conventional Gait Model มี soft-tissue artifact:
   มีรายงานว่า marker เลื่อน **3–54 มม.** ในโมเดลนี้ (หมายเหตุ: แหล่งต้นทาง Fiorentino et al. เป็นเรื่อง
   **ข้อสะโพก** โดยเฉพาะ แม้เปเปอร์จะยกมาอ้างกับ CGM โดยรวม) · ความคลาดของศูนย์กลางข้อสะโพกประเมินไว้ ≈ **31 มม.**
   · มุมงอเข่าคลาด ≈ **0.9°** จาก marker ผิดตำแหน่ง และ ≈ **3.3°** จาก soft-tissue artifact · โดยรวม **<5°**
   สำหรับมุมงอเข่าในวิธีวัดการเดิน 3D ทั่วไป · ส่วนมุมของร่างกายท่อนบนคลาด ≈ **10°** เมื่อใช้โมเดล Heidelberg Upper
   Extremity ที่เทียบเคียงกันได้ · ผู้เขียนแย้งว่า OMC ยังใช้เป็น reference ได้เพราะความคลาดของ HPE ใหญ่กว่าหลายเท่า:
   **2D PAPE ที่สะโพก 43–51 มม. (สูงถึงสองเท่าของความคลาดตำแหน่งสะโพกของ OMC) และ 3D PAPE ที่สะโพก
   74–114 มม. (สามถึงสี่เท่า)** · ข้อด้อยที่มีบันทึกไว้ของ CGM — ความยาวชิ้นส่วนที่ไม่ถูกบังคับ โมเดลร่างกายท่อนบน
   ที่ยังตรวจสอบความถูกต้องไม่พอ และการประมาณศูนย์กลางข้อสะโพกที่ด้อยกว่าวิธีอื่น — มีผลกับงานนี้ด้วย
   · การใช้ชุด marker อื่นที่ยอมรับกันก็จะให้ตำแหน่งข้อต่อ ground truth ต่างออกไป
   · **คมกว่าที่เปเปอร์เขียนไว้:** เกณฑ์คลินิก <5° กับตัวเลข "ความคลาดมุมงอเข่าของวิธีวัดการเดิน 3D น้อยกว่า 5°"
   อ้างมาจาก **แหล่งเดียวกัน** (McGinley et al. 2009 ซึ่งปรากฏซ้ำสองครั้งในบรรณานุกรมเป็น ref 68 และ ref 82)
   → แปลว่าความคลาดมุมงอเข่าของตัว ground truth เอง **อยู่ตรงเส้นเดียวกับที่เปเปอร์ใช้ตัดสินว่า HPE
   ใช้ทางคลินิกไม่ได้** ซึ่งเป็นข้อจำกัดที่หนักกว่าการพูดแค่ว่า "ground truth เองก็ไม่สมบูรณ์"
   และควรระบุให้ชัดถ้าจะอ้างเปเปอร์นี้เป็นขอบเขตความแม่น
2. **การเฉลี่ยทั้งชุดข้อมูลกลบรายละเอียดของเงื่อนไข** — เฉลี่ยข้ามผู้เข้าร่วม ท่า และมุมกล้องทั้งหมด คล้ายกับที่
   ชุดข้อมูลอื่นรายงานกัน → ตัวเลขเหล่านี้คือความแม่น **"ทั่วไป" ไม่ใช่ "ดีที่สุดที่ทำได้"** และไม่ได้แยกผลของ
   การบังตัวเองกับมุมมองที่เหมาะสมออก
3. **กลุ่มตัวอย่างแคบ** — คนหนุ่มสาว สุขภาพดี ไม่มีความบกพร่อง และเชื้อชาติค่อนข้างเป็นเนื้อเดียวกัน
   (ไม่ได้พิจารณาเชื้อชาติตอนคัดเลือก) → อาจใช้ไม่ได้กับกรณีทางคลินิกที่มีผู้ป่วย เช่น การวิเคราะห์รูปแบบการเดินผิดปกติ
   · รูปลักษณ์ของผู้เข้าร่วมอาจกระทบความแม่นผ่านชุดข้อมูลฝึกของโมเดล ซึ่งงานนี้ไม่ได้ศึกษา
4. **สภาพห้องปฏิบัติการ** — มีคนเดียวในภาพ แสงสม่ำเสมอ ฉากหลังรบกวนน้อย ส่วนใหญ่ใส่ชุดกีฬารัดรูปและสั้น
   → การใช้ที่บ้านหรือในสภาพจริงอาจได้ความแม่น **ต่ำกว่านี้** (แสง การบัง ฉากหลัง เสื้อผ้า หรือมีคนหลายคนในภาพ)
5. **ข้อควรระวังเฉพาะ BlazePose** — ในโหมด 'Local' ผู้พัฒนาไม่ได้ระบุค่าคงที่ normalisation ของพิกัดความลึกไว้ชัดเจน
   ผู้เขียนจึงใช้ **ขนาดภาพแนวตั้ง** กู้พิกัดพิกเซลสัมบูรณ์ของความลึก เพราะให้ผลดีกว่าการ normalise ด้วยขนาดแนวนอน
   ตามที่นิยมกัน · เปเปอร์ระบุว่าโหมด 'Local' อาจแม่นกว่านี้อีกถ้าหาค่าคงที่ normalisation ความลึกที่ถูกต้องได้
   *(การอนุมานของเรา ไม่ได้อยู่ในเปเปอร์: ความคลาดด้านลึกของ BlazePose-Local ที่รายงานไว้ บางส่วนจึงอาจเป็น
   ผลพลอยได้จากค่าคงที่ที่ไม่รู้นี้)*
6. **ใช้แบบ off-the-shelf ล้วน** — ไม่มีการฝึกเพิ่มหรือ fine-tune โดยตั้งใจ เพราะนั่นคือวิธีที่คนใช้เครื่องมือเหล่านี้จริง

### คำแนะนำที่เปเปอร์สรุปได้

- จัดกล้องให้มุมที่สนใจอยู่ **ในระนาบภาพ** ให้มากที่สุด และทำการเคลื่อนไหวในระนาบภาพเท่าที่ทำได้
- ถ้าต้องการความแม่น 3D สูงจริง ให้ใช้วิธี **หลายมุมมอง** ที่หลอมข้อมูลจากหลายกล้อง
- ถ้าเลี่ยงกล้องเดี่ยวไม่ได้ ให้เลือกวิธีที่มีโมเดลจลนศาสตร์ในตัว (**HSMR**) หรือวิธีที่ใช้ข้อมูลอนุกรมเวลา
  (MotionBERT, PoseFormerV2, MotionAGFormer) — และสังเกตว่า lifter เหล่านี้ช่วยความแม่น 2D ด้วย
  แม้จะไม่ต้องการค่าความลึกก็ตาม
- ถ้าต้องการความเร็ว inference สูงมากพร้อมความแม่น 2D ที่ดี: **BlazePose 'Local' แล้วทิ้งค่าความลึก**
- **Fine-tune โมเดลบนชุดข้อมูลเฉพาะงาน** — เปเปอร์ระบุข้อนี้คู่กับการเลี่ยงวัดมุมข้อต่อที่ถูกบังบางส่วน
  และการกำหนดท่าทาง/ทิศทางของผู้เข้าร่วมเทียบกล้องเพื่อลดการวัดในแกนลึก · และระบุว่าการฝึกบนชุดข้อมูลเฉพาะงาน
  "อย่างที่ BlazePose ทำ ดูจะเป็นประโยชน์อย่างยิ่ง" · นี่คือคำแนะนำที่นำไปทำได้ตรงที่สุดสำหรับโปรเจกต์โดเมนการเต้น
- วิธี lifting เพิ่ม latency (ลำดับอินพุตยาว และยิ่งมากขึ้นมากถ้าจะรวมเฟรมอนาคตเข้าใน receptive field)
  จึงเหมาะกับงานที่ไม่ต้องการผลแบบ real-time แต่ได้ประโยชน์จากความแม่น เช่น การติดตามความก้าวหน้าการฟื้นฟู
  หรือการวัดพิสัยการเคลื่อนไหว

## 5. ความสัมพันธ์กับงานที่อ้างถึง

- **สายเลือด benchmark:** รูปที่ 1 พล็อต 3D MPJPE บน Human3.6M ภายใต้ Protocol 1 (ใช้ subject 9 และ 11
  เป็นชุดทดสอบ ไม่มี Procrustes alignment) ไล่จาก Ionescu et al. → Li et al. → Tung et al. → Zhou et al. →
  Cai et al. → Zhao et al. แสดงความแม่นที่ดีขึ้นอย่างต่อเนื่องจากการปรับสถาปัตยกรรม การเปลี่ยนแนวทาง
  และข้อมูลฝึกที่มากขึ้น · *(การตีความของเรา ไม่ใช่ข้ออ้างของเปเปอร์ — ระบุไว้เพราะมันชวนให้คิดแต่มีตัวแปรกวน:*
  อาจอ่านเปเปอร์นี้เป็นการถามว่าความก้าวหน้าบน Human3.6M มีค่าแค่ไหนบนท่า *ออกกำลังกาย* เมื่อเทียบกับ *OMC*
  เพราะ 3D MPJPE 146–249 มม. แย่กว่าตัวเลขระดับ Human3.6M มาก · **แต่เปเปอร์ไม่เคยเทียบแบบนั้น**
  และการเทียบนั้นมีตัวแปรกวนอยู่แล้ว: ground truth คนละแบบ นิยามศูนย์กลางข้อต่อคนละแบบ ที่นี่ไม่มี Procrustes
  alignment และเฉลี่ยทั้งชุดข้อมูลโดยรวมมุมมองที่ถูกบังตัวเองไว้ด้วยโดยตั้งใจ · ที่จริงเปเปอร์ระบุปัญหาเรื่องนิยาม
  ไว้เป็นงานอนาคต — ให้เก็บชุดข้อมูล "ที่นิยามตำแหน่งข้อต่อคล้ายกับวิธีที่เป็นมาตรฐานอยู่แล้ว"
  · **อย่าอ้างการเทียบนี้ว่าเป็นของเปเปอร์**)*
- **ประวัติสถาปัตยกรรมที่เปเปอร์สรุปไว้:** feature ที่ออกแบบมือ (HOG/SIFT) → DeepPose (regression ตรงแบบ cascade)
  → heatmap → Convolutional Pose Machine (receptive field ใหญ่; ข้อต่อที่ง่ายช่วยข้อต่อที่ยาก) → stacked hourglass
  → pyramid residual / cascaded pyramid → HRNet (ความละเอียดแบบขนาน) → multi-person แบบ top-down vs
  bottom-up (PAFs) → one-stage (RTMO, Dynamic Bin Allocation/Encoding) → SimCC แบบจำแนก (RTMPose)
  → BlazePose แบบ regression · ส่วน 3D แบ่งเป็น model-based (เช่น SMPL) กับ model-free (direct / lifting)
- **บริบทชุดข้อมูล:** วาง Physio2.2M เทียบกับ HumanEva, Human3.6M, MPII, COCO, AMASS ที่เป็นชุดทั่วไป
  แต่ขาดท่าผิดแปลก และเทียบกับ MOYO กับ Fit3D ที่เป็นไม่กี่ชุดที่เน้นการออกกำลังกาย
- **ฐานทางคลินิก/ชีวกลศาสตร์:** เกณฑ์ <5° ทางคลินิก ค่าฐานของการประเมินด้วยสายตา และวรรณกรรมเรื่อง
  soft-tissue artifact กับ Conventional Gait Model คือสิ่งที่เปลี่ยนตัวเลขมิลลิเมตรดิบให้กลายเป็นคำตัดสินเรื่องการใช้งานได้
  — และเป็นส่วนที่ทำให้งานนี้ต่างจาก benchmark ด้าน computer vision ล้วน ๆ

## 6. จุดแข็ง / จุดอ่อน (สไตล์ pass 3)

**จุดแข็งที่ควรหยิบมาใช้**
- ชุด metric ออกแบบดีและนำกลับมาใช้ได้: MPJPE ดิบ *บวก* PAMPJPE *บวก* การแยกความคลาดรายแกน ·
  การแยกรายแกนคือสิ่งเดียวที่ทำให้เห็นปัญหาแกนลึก — ถ้าดู MPJPE รวมอย่างเดียวจะถูกกลบไปหมด
- **รายงานอัตราการตรวจพบคู่กับความแม่น** เป็นเรื่องสำคัญเชิงระเบียบวิธี *(เหตุผลส่วนนี้เป็นของเรา ไม่ใช่ของเปเปอร์ —
  เปเปอร์รายงานแต่สัดส่วนและระบุว่าตัดเฟรมที่ตรวจไม่พบออก และคำบรรยายรูปที่ 3 ระบุว่าสัดส่วนต่างกันมาก
  แต่ไม่ได้สรุปผลที่ตามมา)* เพราะ metric ที่คำนวณเฉพาะเฟรมที่ตรวจพบมี bias เข้าข้างตัวเอง —
  โมเดลที่ตรวจพบ 14.40 % เทียบกับที่ตรวจพบ 100 % ไม่ได้ ไม่ว่า MPJPE จะดูดีแค่ไหน
- **วัดความคลาดของ ground truth ตัวเอง แล้วแย้งว่าการเทียบยังใช้ได้** คือท่าที่ถูกต้อง
- ประเมิน **คู่ direct × lifting** แทนที่จะประเมินโมเดลเดี่ยว ทำให้เห็นผลที่ไม่ชัดมาก่อนว่าการเลือกตัวประมาณ 2D
  ต้นทางเปลี่ยน 3D MPJPE ได้ถึง 40 มม.

**จุดอ่อน / พื้นที่ที่ถูกโจมตีได้**
- **ชุดข้อมูลไม่เปิดสาธารณะ** → ผลงานหลักไม่สามารถนำไปใช้ซ้ำหรือทำซ้ำโดยอิสระได้ ขอได้จากผู้เขียนเป็นราย ๆ เท่านั้น
- **ตัวเลขรายโมเดลอยู่ในตาราง supplementary S1–S5 ที่ไม่ได้อยู่ใน PDF ที่เผยแพร่** → ข้อกล่าวอ้างเกี่ยวกับโมเดล
  ใด ๆ นอกจากไม่กี่ตัวที่ระบุชื่อในเนื้อ Results ตรวจสอบจากตัวบทความอย่างเดียวไม่ได้
- **การเฉลี่ยข้ามมุมกล้องและท่า** ผสมตัวแปรที่ควบคุมได้ (frontal vs sagittal) เข้าไปในตัวเลขเดียว ·
  เปเปอร์ยอมรับเรื่องนี้ และการวิเคราะห์ต่อเนื่องของเปเปอร์เองก็แสดงว่าการแบ่ง frontal/sagittal เป็นตัวขับผล
  ē_y > ē_x → การรายงานแยกตามเงื่อนไขจะให้ข้อมูลมากกว่าค่าเฉลี่ยรวม
- **การบังตัวเองถูกฝังอยู่ในการออกแบบ** (บางท่ามีสองกล้องที่ถูกบังเสมอ) แทนที่จะเป็นตัวแปรที่แยกออกมา →
  "ความแม่นทั่วไป" ที่ได้จึงเป็นคุณสมบัติของชุดกล้องชุดนี้อยู่ส่วนหนึ่ง
- **วัดมุมน้อยเกินไป** — เฉพาะมุมงอเข่าและศอก และถือเป็นบานพับ 1 องศาอิสระทั้งคู่ ไม่มีการหมุน ไม่มีไหล่ ไม่มีลำตัว
  · อีกทั้ง ground truth ของรยางค์ส่วนบนคือส่วนที่อ่อนที่สุดของ CGM (~10° ตามอ้างอิงโมเดล Heidelberg)
  ทำให้คำตัดสินเรื่องข้อศอกหนักแน่นน้อยกว่าคำตัดสินเรื่องข้อเข่า · **ผู้เขียนเห็นด้วย:** ส่วนงานอนาคตของเขาเอง
  เรียกร้องให้ศึกษาการงอข้อต่อแบบแยกเดี่ยวที่ไม่มีการบังตัวเอง และให้พัฒนาความแม่นของข้อต่อและมุมของรยางค์ส่วนบน
  — คือเขาเองก็ชี้ว่าผลเรื่องข้อศอก/รยางค์บนเป็นส่วนที่อ่อนที่สุดของงานตัวเอง
- **n = 25 และเป็นกลุ่มเนื้อเดียวกัน ไม่มีผู้มีความบกพร่องเลย** — เป็นข้อจำกัดที่น่าสังเกตสำหรับเปเปอร์ที่ชื่อเรื่อง
  อ้างว่าเป็นการวิเคราะห์ *ทางคลินิก*
- **ค่า normalisation ความลึกของ BlazePose 'Local' เป็นการเดาอย่างมีหลักการ** ของผู้เขียน ซึ่งทำให้การเทียบใด ๆ
  ที่เกี่ยวกับความลึกของ BlazePose-Local อ่อนลง

## 7. การตรวจความน่าเชื่อถือของแหล่ง (ตาม `reading_guide.md`)

*Scientific Reports* ผ่าน peer review และเปิดเข้าถึงแบบ CC BY 4.0 ไม่ใช่วารสาร predatory · quartile SJR
สาย multidisciplinary มักอยู่ระดับ Q1/Q2 แต่ **ตรวจสอบจากตัวบทความไม่ได้ — ให้ไปเปิดดูที่ scimagojr.com
แล้วบันทึกวันที่ตรวจไว้ ก่อนจะอ้าง quartile ในวิทยานิพนธ์** · เป็น mega-journal ดังนั้นชื่อวารสารอย่างเดียว
หนักแน่นน้อยกว่าการประชุมระดับ CORE A*/A — ความน่าเชื่อถือที่แท้จริงมาจากฐานสถาบัน (ETH Zurich D-HEST,
Akina AG, Schulthess Klinik Human Performance Lab, คณะแพทยศาสตร์ มหาวิทยาลัยซูริก), สถานที่เก็บข้อมูล
(Swiss Center for Movement Analysis ที่ Balgrist Campus ซึ่งถูกขอบคุณเรื่องการสนับสนุนและโครงสร้างพื้นฐาน
— **ไม่ใช่สังกัดของผู้เขียน**) และจากการที่ระเบียบวิธีเขียนละเอียดพอให้ตรวจสอบได้
· ไม่มีผลประโยชน์ทับซ้อน · ทุนเผยแพร่แบบเปิดจาก ETH Zurich · **อ้างได้อย่างปลอดภัย**

---

## 8. การตรวจตาม CHECKLIST — `knowledge/reading_checklist.md`

Checklist เป็น *รายการลำดับการอ่าน* ของทั้งคลัง ไม่ใช่แบบสอบถามรายเปเปอร์ จึงไล่ทีละข้อด้านล่าง โดยระบุว่าเปเปอร์
**นี้** (A1-14) พูดถึงข้อนั้นว่าอย่างไร และติดสถานะความครอบคลุม · ข้อส่วนใหญ่เป็นเปเปอร์อื่นและ **ไม่ครอบคลุม**
อย่างถูกต้องแล้ว · ข้อที่มีเนื้อหาจริงคือ **ข้อ 5** (เปเปอร์นี้เอง), **ข้อ 22** (BlazePose) และการทดลอง **E6** กับ **E5**

**ไม่ได้แก้ไข `reading_checklist.md`** — ใช้เป็น input อย่างเดียว

### TIER 0

| ข้อ | รายการ | เปเปอร์นี้พูดถึงอะไร | สถานะ |
|---|---|---|---|
| 1 | A1-21 Galata/Johnson/Hogg VLMM | ไม่มีเลย คนละโจทย์ (สร้างแบบจำลองพฤติกรรม vs การวัดท่า) | **ไม่ครอบคลุม** |
| 2 | A1-12 SinMDM | ไม่มีเลย ไม่มีการสร้าง ไม่มี metric ความหลากหลาย | **ไม่ครอบคลุม** |
| 3 | A0-9 DASB | ไม่มีเลย ไม่มีเรื่อง tokenisation หรือ bitrate | **ไม่ครอบคลุม** |
| 4 | A0-8 รีวิว discrete speech tokens | ไม่มีเลย | **ไม่ครอบคลุม** |
| **5** | **A1-14 — เปเปอร์นี้** | **ครอบคลุมเต็ม พร้อมคำแก้ 3 จุดในตัวเลขที่ checklist เขียนไว้เอง** ดูตารางไล่ทีละข้ออ้างด้านล่าง | **ครอบคลุม (มีคำแก้)** |

**ข้อ 5 — ไล่ทีละข้ออ้างเทียบกับต้นฉบับ:**

| ที่ checklist เขียน | ที่เปเปอร์เขียนจริง | สถานะ |
|---|---|---|
| "Rode et al. (2025), *Scientific Reports*, doi:10.1038/s41598-025-22626-7" | ตรงทุกประการ | ✅ |
| "BlazePose Heavy World 3D MPJPE 146 mm" | ยืนยัน — BlazePose 'World' 'Heavy' ได้ 3D MPJPE **146 มม.** เป็นวิธี direct 3D ที่ดีที่สุด (ē_x 50 / ē_y 58 / ē_z 108 มม., ตรวจพบ 98.8 %, 147 FPS) | ✅ |
| "2D ~80 mm" | **ตรวจสอบจาก PDF ไม่ได้** — เนื้อบทความให้เพียงช่วง 2D 72–122 มม. และระบุชื่อเฉพาะ RTMPose 'Performance' (72 มม.) กับ MotionAGFormer-บน-BlazePose-Local-Heavy (61 มม.) · ค่า 2D MPJPE ของ BlazePose 'Local' 'Heavy' ไม่ได้เขียนไว้ในตัวบทความ — น่าจะอยู่ใน **Supplementary table S1 ซึ่งไม่ได้แนบมากับ PDF** | ⚠️ **ยังไม่ยืนยัน** |
| "knee flexion MAE 14.1–31.2°" | **ขอบบนผิด** — เปเปอร์รายงานมุมงอเข่า **3D MAE 14.1–25.8°** (บทคัดย่อและ discussion; ส่วน Results เขียน 25.9°) และ **2D MAE 9.3–21.9°** · ค่า 31.2°, 23.7°, 41.3° และ 35.0° — ซึ่งปรากฏในรายการ A1-14 ของ `paper_notes/paper_chain.md` ด้วย — **ไม่ปรากฏที่ใดเลยในเปเปอร์** | ❌ **ต้องแก้** |
| "ความคลาดในแกนลึกสูงกว่าในระนาบ 2–3 เท่า" | ยืนยันในสาระ: ความคลาดสัมบูรณ์เฉลี่ยในแกนลึกมากกว่าความคลาดสัมบูรณ์เฉลี่ยในแนวนอนและแนวตั้งประมาณสองถึงสามเท่า สำหรับตัวประมาณทุกตัวที่ศึกษา | ✅ |
| "คุกคามครึ่งหนึ่งของ 36 angle features ที่พึ่ง z" | เปเปอร์หนุน *ข้อตั้ง* (ความลึกแย่กว่า 2–3 เท่า) แต่ไม่ได้พูดถึง feature vector ของเรา · และ `paper_chain.md` ตรวจโค้ดของเราเองแล้วสรุปว่า **ทั้ง 36 ตัว** ใช้ `v_p_z` ไม่ใช่ครึ่งเดียว → ถ้อยคำใน checklist ประเมินความเสี่ยงต่ำเกินไป | **ครอบคลุมบางส่วน** (ข้อตั้งใช่ แต่ตัวเลข "ครึ่งหนึ่ง" เป็นของเราเองและขัดกับการตรวจโค้ดของเราเอง) |
| "ผลที่ต้องทำต่อ: z-zeroed vs full 3-D tokenization" | คำแนะนำของเปเปอร์ชี้ทางเดียวกัน: ให้มุมที่สนใจอยู่ **ในระนาบภาพ** หรือใช้หลายกล้อง · และระบุว่า BlazePose 'Local' ที่ทิ้งค่าความลึกคือทางเลือก 2D ที่เร็วและแม่น — ซึ่งก็คือการตั้งค่าแบบ z-zeroed นั่นเอง | **ครอบคลุม / เสริมกำลัง** |
| "⏱ pass 2" | ทำตามแล้ว — pass 2 เต็ม และ pass 3 บางส่วน (ไล่สมการซ้ำ; ผู้เขียนไม่ได้เผยแพร่โค้ด) | ✅ |

### TIER 1 (ข้อ 6–13)

Rhythm is a Dancer, Keyposes, FSQ, Labrak, Matrix Profile VI, Atomic Movements, MotionCritic, Scaling Laws with
Vocabulary — **ไม่ครอบคลุมทั้งหมด** · เปเปอร์นี้ไม่มีเนื้อหาเรื่อง tokenisation ขนาด vocabulary การจัดกลุ่ม
การค้นหา motif หรือการสร้าง · มีจุดสัมผัสทางอ้อมจุดเดียว: ข้อ 12 (MotionCritic / การรับรู้คุณภาพการเคลื่อนไหว
ของมนุษย์) มีความกังวลพื้นฐานร่วมกับเปเปอร์นี้ — ว่าตัวเลขอัตโนมัติอาจไม่ตรงกับการตัดสินของมนุษย์ — แต่มาจาก
คนละด้าน (เปเปอร์นี้วัดเทียบกับ *เครื่องมือ* ไม่ใช่การรับรู้) **ไม่ครอบคลุม**

### TIER 2 (ข้อ 14–23)

| ข้อ | รายการ | ความเกี่ยวข้องในที่นี้ | สถานะ |
|---|---|---|---|
| 22 | **A1-6 BlazePose** (arXiv:2006.10204) | **ครอบคลุมอย่างมีสาระ** · เปเปอร์อธิบายสถาปัตยกรรม BlazePose (สองขั้นแบบ top-down, ได้แรงบันดาลใจจาก hourglass, เส้นทางฝึกคู่ heatmap + regression ที่ใช้ encoder ร่วมกัน, ถอดเส้นทาง heatmap ออกตอน inference, กลไก skip-frame), รุ่น `Lite`/`Full`/`Heavy` และโหมด `Local`/`World`, ชุดฝึกที่ label ด้วยมือบนฐาน GHUM เน้นโยคะ/ฟิตเนส — **แล้ววัดผลอย่างอิสระเทียบกับ OMC** · สำหรับงานเรา นี่เป็นแหล่งที่หนักแน่นกว่าเปเปอร์ BlazePose เองในแง่ *พฤติกรรมที่วัดได้จริง* เพราะเปเปอร์ต้นฉบับไม่มีการเทียบกับ OMC | **ครอบคลุม** |
| 16 | A0-1 Human Motion Generation survey | เป็นสาขาข้างเคียงเท่านั้น ไม่มีเนื้อหาการสร้าง | ไม่ครอบคลุม |
| 19 | A1-20 Skeleton Motion Words (การแยก joint) | หนุนทางอ้อม: ความคลาดแบบ Procrustes รายข้อต่อต่างกันชัดเจน (สะโพกน้อยสุด ข้อมือกับข้อเท้ามากสุด) = หลักฐานว่า **ข้อต่อไม่ได้น่าเชื่อถือเท่ากัน** จึงอาจไม่ควรให้น้ำหนักเท่ากันใน feature vector ทั้งตัว · เปเปอร์ไม่ได้อภิปรายเรื่องการเลือก subset ของข้อต่อ | **ครอบคลุมบางส่วน** |
| 23 | L3-20 DisCoRD (jitter เป็นคุณสมบัติที่รู้จักกัน) | ทางอ้อม: การกรองความถี่ด้วย DCT ของ PoseFormerV2 ถูกอธิบายว่าช่วยลด noise ความถี่สูงและ jitter ที่เกิดจากการประมาณ 2D ทีละเฟรม — คือเปเปอร์ตั้งชื่อให้ **jitter ฝั่งตัวประมาณ** ว่าเป็นปรากฏการณ์จริงที่มีบันทึกและมีวิธีบรรเทาที่รู้จักกัน · ใช้ได้ในหัวข้อ Limitations ของเรา | **ครอบคลุมบางส่วน** |
| 14, 15, 17, 18, 20, 21 | Text2Tradition, Joshi & Chakrabarty, Motion Texture, DC-Motion, กลุ่มเปเปอร์ dance token, chor-rnn | ไม่มีเนื้อหา | ไม่ครอบคลุม |

### TIER 3 (ข้อ 24–31, Phase 2 / ถูกถอยลง)

**ไม่ครอบคลุม** · ไม่มีเรื่อง energy curve, time-series clustering, โครงสร้างเชิงเรื่องเล่า, การวิเคราะห์แบบ Laban
หรือการแบ่งส่วนด้วยเสียง · มีจุดข้ามฟากเล็ก ๆ จุดเดียว: ข้อ 28 (Quantity of Motion ของ Camurri ที่คิดจากพิกเซล
silhouette เทียบกับความเร็ว landmark ของเรา) — เปเปอร์นี้ระบุปริมาณว่าตำแหน่ง landmark เองคลาดไปเท่าไร
(72–122 มม. ใน 2D) ซึ่งเป็นขอบเขตที่ใช้อ้างได้ทุกครั้งที่จะเคลมว่าปริมาณที่ *อนุมาน* จาก landmark เช่นความเร็ว
มีความหมาย **เกี่ยวข้องบางส่วน**

### "ต้องให้คุณช่วย" (ติด paywall / ถูกบล็อก)

ไม่เกี่ยวกับเปเปอร์นี้ — เป็น open access และ PDF อยู่ในเครื่องแล้ว · **แต่การอ่านรอบนี้เพิ่มรายการที่ถูกบล็อก
ใหม่ 1 รายการ: ตาราง Supplementary S1–S5 ไม่ได้อยู่ใน PDF ในเครื่อง** และจำเป็นสำหรับตัวเลขรายโมเดลใด ๆ
ที่นอกเหนือจากไม่กี่ตัวที่ยกมาในเนื้อ Results · ตารางเหล่านี้ดาวน์โหลดได้ฟรีที่ DOI ของบทความ
**สิ่งที่ต้องทำ: ดึง supplementary information จาก https://doi.org/10.1038/s41598-025-22626-7
ก่อนจะอ้าง "BlazePose 'Local' ≈ 80 มม."**

### การทดลองที่การอ่านสั่งให้ทำ (E1–E7)

| ข้อ | การทดลอง | เปเปอร์นี้เกี่ยวอย่างไร | สถานะ |
|---|---|---|---|
| **E6** | **z-zeroed vs full 3-D tokenization** | **ถูกสั่งโดยตรงและได้รับการเสริมกำลัง** · ความคลาดแกนลึกเป็น 2–3 เท่าของในระนาบสำหรับตัวประมาณ 3D *ทุกตัว* และ BlazePose 'World' 'Heavy' มี ē_z 108 มม. เทียบกับ ē_x 50 / ē_y 58 มม. · **ประโยคที่แรงที่สุดของเปเปอร์สำหรับเรา:** ข้อจำกัดใหญ่ที่สุดของตัวประมาณกล้องเดี่ยวคือความแม่นด้านความลึก และ *"การจำกัดการใช้งานไว้ที่ 2D พร้อมมุมกล้องที่เหมาะสม อาจไปถึงระดับความแม่นที่ต้องการได้"* — คือเปเปอร์เองบอกว่าการตั้งค่าแบบ z-zeroed คือทางที่อาจถึงระดับคลินิก · คำแนะนำอื่น ("ให้มุมที่สนใจอยู่ในระนาบภาพ", "BlazePose 'Local' ที่ทิ้งค่าความลึกนั้นแม่นและเร็ว") ก็ชี้ทางเดียวกัน · **หลักฐานเพิ่มจากการอ่านรอบนี้:** ค่า normalisation ความลึกของ BlazePose 'Local' ไม่มีเอกสารกำกับและผู้เขียนต้องเดาเอง — เป็นอีกเหตุผลที่ไม่ควรไว้ใจช่อง z ของเรา · **ข้อควรระวังว่าจะอ้างแถวไหน:** `models/pose_landmarker_heavy.task` คือ bundle heavy ของ MediaPipe ซึ่งให้ landmark *ทั้ง* แบบ normalise ('Local') และแบบเมตริก ('World') → แถว benchmark ที่ใช้ได้ขึ้นกับว่า `src/tokenize_with_model.py` อ่าน output ตัวไหน · ถ้าอ่านแบบ normalise แถวที่เกี่ยวคือ BlazePose 'Local' 'Heavy' ซึ่ง **2D MPJPE ไม่ได้อยู่ในตัวบทความ** และความลึกของมันคือช่องที่ถูกบั่นทอนด้วยค่าคงที่ที่เดาเอา · ให้ตรวจโค้ดก่อนอ้างเลข 146 มม. กับ pipeline เรา | **ครอบคลุม — ยืนยันว่าเป็นการทดลองที่คุ้มที่สุด** |
| **E5** | continuous-baseline LSTM บน landmark ดิบ | ทางอ้อมแต่เกี่ยวข้อง: landmark ดิบมีความคลาดในการวัดติดมา 72–122 มม. (2D) / 146–249 มม. (3D) ดังนั้น baseline แบบ "continuous" ก็ไม่ใช่ ground truth ที่ปลอดความคลาด · ควรระบุเรื่องนี้ตอนตีกรอบว่า discretisation แลกอะไรไป | **ครอบคลุมบางส่วน** |
| **E7** | metric ที่ไม่ต้องมี corpus รวมถึง limb-length SD และ foot-skating % | หนุนทางอ้อม: ข้อมือและข้อเท้ามีความคลาดแบบ Procrustes สูงที่สุด → limb-length SD และ foot-skating ที่คำนวณจากผลลัพธ์ BlazePose จะมีความคลาดของตัวประมาณปนอยู่ ไม่ใช่ความคลาดของโมเดลเราอย่างเดียว · ควรรายงานค่าพื้นไว้ด้วย | **ครอบคลุมบางส่วน** |
| E1, E2, E3, E4 | mSTAMP subspace, VLMM baseline, velocity+dedup, vocab sweep | ไม่เกี่ยวข้อง | **ไม่ครอบคลุม** |

### คำตัดสินของ checklist

**ข้อ 5 (A1-14) อ่านจบแล้วและติ๊กได้** — โดยต้องแก้ว่าตัวเลข MAE มุมงอเข่าผิด ต้องเปลี่ยนเป็น
**14.1–25.8° (3D) / 9.3–21.9° (2D)** และต้องทำเครื่องหมายว่า "2D ~80 มม." ยังไม่ยืนยัน รอตาราง supplementary
· **ไม่มีข้ออื่นใน checklist ที่คืบหน้าจากเปเปอร์นี้** แม้ข้อ 22 (BlazePose) จะถูกครอบคลุมอย่างมีสาระเป็นผลพลอยได้
· ไม่มีอะไรในเปเปอร์ที่ขัดกับการจัดลำดับ Tier · สิ่งที่เพิ่มเข้ามาคือการไปดึง Supplementary Information S1–S5

---

## 9. ตัวเลขขัดกันเองในเปเปอร์

พบความไม่สอดคล้องภายใน 5 จุด แต่ละจุดเล็กน้อยแต่ควรรู้ก่อนยกมาอ้าง:

1. **ขอบบนของ MAE มุมงอเข่าแบบ 3D:** บทคัดย่อและ discussion เขียน **25.8°** แต่ส่วน Results เขียน **25.9°**
   → ให้อ้าง 25.8° (ปรากฏสองที่ รวมบทคัดย่อ) หรืออ้างเป็นช่วง "≈14–26°"
2. **ขอบบนของความเร็ว lifting:** บทคัดย่อเขียน **9341 FPS** แต่ส่วน Results เขียน **9339 FPS**
   → ไม่มีผลต่อข้อโต้แย้งใด ให้อ้างเป็น "≈9.3 kFPS"
3. **ช่วงตัวเลข 2D ที่ระบุไว้ ไม่ครอบคลุมผลลัพธ์ 2D ที่ดีที่สุดของเปเปอร์เอง** (61 มม. / 8.5° อยู่นอกช่วง
   72–122 มม. / 9.3–21.9°) → ช่วงเหล่านั้นอธิบายเฉพาะโมเดล 2D แบบ *direct* 18 ตัว แต่เปเปอร์ไม่ได้บอกไว้ · ดูหัวข้อ 3.1
4. **'Global' vs 'World':** โหมดเมตริกของ BlazePose ถูกเรียกว่า 'World' ตลอดทั้งเปเปอร์ ยกเว้นครั้งเดียว
   ในคำอธิบาย PoseFormerV2 ที่เรียกว่า BlazePose **'Global'** — เป็นโหมดเดียวกัน
5. **รายการบรรณานุกรมซ้ำ** — ref 10 กับ ref 20 เป็นเปเปอร์เดียวกัน (Munea et al., *IEEE Access* 8,
   133330–133348, 2020) และ ref 68 กับ ref 82 เป็นเปเปอร์เดียวกัน (McGinley et al., 2009)
   · การซ้ำอันหลัง **ไม่ใช่เรื่องเชิงรูปแบบ** — ดูหมายเหตุในหัวข้อ 4 ข้อ 1: แปลว่าเกณฑ์คลินิก <5°
   กับความคลาดมุมงอเข่าของ OMC ที่ <5° มาจากแหล่งเดียวกัน
6. มีการอ้างอิงรูปผิดด้วย: ตอนแนะนำท่าออกกำลังกายเขียนว่า "(Fig. 2b)" แต่ท่าอยู่ในรูปที่ 2**c**
   ส่วนรูปที่ 2b คือชุด marker
7. เชิงรูปแบบ: footer ของ PDF เป็นข้อความสองชุดซ้อนกันจนอ่านยาก และบรรทัดลิขสิทธิ์ท้ายสุดเขียน
   "© The Author(s) 2026" ขณะที่บรรทัดอ้างอิงคือ (2025) 15:38767
   → **อ้างเป็น Sci Rep 15:38767 (2025)** ให้สอดคล้องกับ DOI และวันตอบรับ 30 กันยายน 2025

## 10. ช่องว่างของการอ่านรอบนี้

- **ตาราง Supplementary S1–S5 ไม่ได้อยู่ใน PDF ในเครื่อง** → ค่าที่แน่นอนรายโมเดล (ทั้ง 18 config 2D และ
  26 config 3D), ค่า PAPE รายข้อต่อ, อัตราการตรวจพบรายโมเดล และแหล่งที่มาของรูปที่ 1 **จึงใช้ไม่ได้**
  · ทุกอย่างในสรุปนี้มาจากเนื้อบทความเท่านั้น
- **ไม่มีโค้ดและไม่มีข้อมูล** — ชุดข้อมูลไม่เปิดสาธารณะและผู้เขียนไม่ได้ปล่อย implementation ดังนั้นขั้น pass 3
  แบบ "virtually re-implement" จึงทำกับตัวการทดลองไม่ได้ ทำได้เฉพาะกับนิยาม metric ซึ่งไล่จากสมการ 1–9
  แล้วพบว่าสอดคล้องกันเอง
- รูปที่ 3–5 เป็น boxplot และภาพโครงกระดูก อ่านค่าที่แน่นอนจากข้อความที่สกัดมาไม่ได้ จึงอ้างเฉพาะค่าที่เขียนเป็นร้อยแก้ว

## 11. สิ่งที่ต้องทำต่อในโปรเจกต์

1. **แก้รายการ A1-14 ใน `knowledge/paper_notes/paper_chain.md`** (ราวบรรทัด 1367) และข้อ 5 ของ
   `reading_checklist.md`: ช่วง MAE มุมงอ 9.3–23.7 / 14.1–31.2 / 21.5–41.3 / 16.3–35.0 **ไม่มีในเปเปอร์**
   · ค่าที่ตีพิมพ์จริง: เข่า 2D **9.3–21.9°**, เข่า 3D **14.1–25.8°**, ศอก 2D **21.5–28.9°**, ศอก 3D **16.3–26.0°**
2. **ลบหรือหาแหล่งใหม่ให้ข้อความในเครื่องหมายคำพูด** "depth estimation remains substantially inaccurate"
   ในรายการ A1-14 ของ `paper_chain.md` — **สตริงนี้ไม่ปรากฏในเปเปอร์** · ถ้อยคำที่หนุนได้คือ
   *ความคลาดสัมบูรณ์เฉลี่ยในแกนลึกมากกว่าความคลาดในระนาบประมาณสองถึงสามเท่าสำหรับตัวประมาณทุกตัวที่ศึกษา*
   ส่วนถ้อยคำในบทสรุปของเปเปอร์เองคือ ตัวประมาณ 3D และวิธีแบบ transformer ยังให้ค่าความลึกที่ไม่แม่นยำ
3. **ดึงตาราง Supplementary S1–S5** ก่อนจะอ้างตัวเลขรายโมเดลใด ๆ ที่ไม่ได้ระบุชื่อในเนื้อ Results
   — รวมถึง "BlazePose 'Local' ≈ 80 มม."
4. **รัน E6 (z-zeroed vs full 3-D tokenization)** — การทดลองที่มีหลักฐานหนุนแน่นที่สุดใน backlog ตอนนี้
5. **อ้างเปเปอร์นี้เป็น "พื้นความคลาดของการวัด"** ในหัวข้อ Limitations ของวิทยานิพนธ์: landmark ของเรามาจาก
   BlazePose Heavy ซึ่งที่นี่วัดได้ 3D MPJPE 146 มม. และความคลาดสัมบูรณ์เฉลี่ยในแกนลึก 108 มม.
   · **ให้ใช้ข้อโต้แย้งของเปเปอร์เอง ซึ่งหนักกว่าการบอกว่า "วิดีโอง่ายกว่า":** ผู้เขียนอธิบายว่าการที่ BlazePose
   ได้อันดับหนึ่งส่วนหนึ่งมาจากการที่ชุดฝึกกับชุดทดสอบมีการกระจายตรงกัน — มันถูกฝึกบนชุดข้อมูลโยคะ/ฟิตเนส
   ที่เก็บมาเฉพาะ ซึ่ง *ท่าคล้ายกับท่าออกกำลังกายใน Physio2.2M มาก* · การเต้นอยู่นอกการกระจายนั้น ดังนั้น
   **146 มม. ควรถือเป็นพื้นที่มองโลกในแง่ดีสำหรับ pipeline เรา ไม่ใช่ตัวเลขที่ถ่ายโอนมาใช้ได้ตรง ๆ**
   (ส่วนสภาพห้องแล็บ — แสงสม่ำเสมอ คนเดียวในภาพ ชุดรัดรูป — เป็นเหตุผลที่สองที่แยกจากกัน ซึ่งเปเปอร์ก็ระบุไว้เช่นกัน)
6. เสริมแบบต้นทุนต่ำ: คำแนะนำของเปเปอร์ให้ใช้มุมที่อยู่ในระนาบภาพ สนับสนุนการถ่ายหรือเลือกคลิปเต้น
   ที่การเคลื่อนไหวสำคัญขนานกับระนาบภาพ เท่าที่เรามีสิทธิ์เลือก

---

## 12. การตรวจสอบยืนยัน (second pass แบบอิสระ)

มี agent ตรวจสอบแยกอีกตัวอ่านเปเปอร์ซ้ำจาก PDF — สกัดข้อความขึ้นมาเองและยืนยันว่าตรงกันทุกไบต์กับไฟล์ที่ใช้ร่างสรุป
— แล้วตรวจสอบสรุปฉบับนี้เทียบกับต้นฉบับ โดยใช้วิธี Three-Pass เดียวกัน · **คำตัดสิน: ให้แก้ไข (REVISE) —
บันทึกเก็บเข้าคลังได้เมื่อแก้ตามรายการด้านล่างแล้ว ไม่ต้องอ่านต้นฉบับใหม่** · คำแก้ทั้งหมดถูกรวมเข้าในเนื้อข้างบนแล้ว

**ตรวจอะไรบ้าง** — grep ข้ออ้างเชิงตัวเลขทุกตัว (~70 ตัว) เทียบกับข้อความเต็มพร้อมเลขบรรทัด · ข้ออ้างที่ไม่ใช่ตัวเลข
ทุกข้อเกี่ยวกับวิธีการ สาเหตุ คำแนะนำ และข้อจำกัด · ข้ออ้าง **เชิงลบ** 4 ข้อของร่าง (ที่บอกว่าบางสตริงไม่มีในเปเปอร์)
· จุดขัดกันเองภายในที่ร่างอ้างไว้ 2 จุด · และตัวตนของ reference ที่อยู่เบื้องหลังช่อง "Context" ใน Five Cs

**สิ่งที่ยืนยันแล้ว**
- **ไม่พบตัวเลข โมเดล metric หรือการอ้างอิงที่กุขึ้นเลยในร่างนี้** · ทุกตัวเลขสืบกลับไปหาเปเปอร์ได้ ผูกกับโมเดล
  metric และมิติที่ถูกต้อง โดยไม่มีการปัดเศษเพี้ยน: ช่วง 2D/3D MPJPE, ค่ารายแกนและ PAMPJPE ทั้งหมดของ
  RTMPose 'Performance', BlazePose 'World' 'Heavy' และ MotionAGFormer-บน-BlazePose 'Local' 'Heavy',
  ช่วง MAE มุมงอทั้งสี่ช่วง, ตัวเลข FPS, อัตราการตรวจพบ, ข้อมูลประชากร, จำนวนกล้อง/marker และอัตราสุ่ม,
  บล็อกความคลาดของ OMC/CGM และการเทียบกับการประเมินด้วยสายตาทั้งหมด
- **ผลงานหลักของร่างนี้ยืนได้** · สตริง `23.7`, `31.2`, `41.3`, `35.0` และวลี "substantially inaccurate"
  **ไม่พบเลยแม้แต่ครั้งเดียว** ในข้อความเต็ม · ผู้ตรวจหาตำแหน่งค่าที่กุขึ้นได้เองที่
  `knowledge/paper_notes/paper_chain.md:1367–1368` และยืนยันการตรวจโค้ด "ทั้ง 36 feature ใช้ `v_p_z`" ที่ `:1539`
  → คำแก้ในหัวข้อ 11 ข้อ 1–2 ควรลงมือทำจริง
- จุดขัดกันเองทั้งสองจุดที่ร่างอ้าง (25.8° vs 25.9° และ 9341 vs 9339 FPS) มีอยู่จริงและระบุตำแหน่งถูกต้อง

**คำแก้ที่ผู้ตรวจให้มา และได้แก้แล้ว**
1. **ขอบเขตของช่วงตัวเลข "18 โมเดล 2D"** — ผลลัพธ์ 2D ที่ดีที่สุดของเปเปอร์เอง (61 มม. / 8.5°) อยู่ *นอก* ช่วง
   72–122 มม. / 9.3–21.9° ที่ระบุ ดังนั้นช่วงนั้นครอบคลุมเฉพาะโมเดล 2D แบบ **direct** 18 ตัว ·
   เพิ่มเป็นหมายเหตุขอบเขตในหัวข้อ 3.1 และเป็นจุดขัดกันเองข้อ 3 ในหัวข้อ 9
2. **การ cross-product ของ lifting เป็นการอนุมาน ไม่ใช่สิ่งที่เปเปอร์ระบุ** — เปเปอร์ไม่เคยบอกว่ารัน lifter ทุกตัว
   บนตัวประมาณ 2D ทุกตัว และ 3 × 18 = 54 ≠ 26 config 3D ที่รายงาน · เขียนหัวข้อ 2.3 ใหม่
3. **"ไม่มีชุดข้อมูลเลย" พูดเกินจริง** จากที่เปเปอร์เขียนว่า "มีเพียงไม่กี่ชุด" และ "ขาดชุดข้อมูลที่เน้นการออกกำลังกาย"
   · ลดน้ำหนักในหัวข้อ 1
4. **"Detectron2 แย่ที่สุด"** → เปเปอร์เขียนว่า "แม่นน้อยกว่า" ไม่ใช่ "น้อยที่สุด" และไม่ได้จัดอันดับในตัวบทความ
5. **"2D ชนะสายตาคน"** → ประโยค "ส่วนใหญ่…แม่นกว่า" ของเปเปอร์พูดถึง **3D** · ส่วน 2D เปเปอร์เขียนเพียงว่า
   *บางตัว* แม่น *เทียบเท่าหรือดีกว่า* การประเมินด้วยสายตา · แก้หัวข้อย่อย 3.3 และตาราง 0b
6. **เพิ่มข้อบกพร่องของต้นฉบับอีก 3 จุดในหัวข้อ 9**: 'Global' vs 'World' · reference ซ้ำ (10≡20, 68≡82)
   · การอ้างรูป 2b/2c ผิด
7. **ติดป้ายว่าเป็น "การตีความ" ในสามจุด**: การเทียบกับ Human3.6M ในหัวข้อ 5 (เปเปอร์ไม่เคยเทียบ และการเทียบนั้น
   มีตัวแปรกวนจาก ground truth นิยามศูนย์กลางข้อต่อ และการไม่มี Procrustes alignment), การอนุมานเรื่อง
   artefact ความลึกของ BlazePose-Local ในหัวข้อ 4 ข้อ 5, และเหตุผลเรื่องอัตราการตรวจพบในหัวข้อ 6
8. **"ทำซ้ำได้ในหลักการ"** ลดเหลือ "สร้างขึ้นใหม่ได้ในหลักการ แต่ทำซ้ำจริงไม่ได้" ให้สอดคล้องกับหัวข้อ 10
9. แก้เรื่องความน่าเชื่อถือของแหล่ง: Swiss Center for Movement Analysis เป็นสถานที่เก็บข้อมูลและอยู่ในกิตติกรรมประกาศ
   ไม่ใช่สังกัดของผู้เขียน · และ quartile SJR ตรวจจากตัวบทความไม่ได้ จึงใส่ข้อควรระวังเรื่องการไปตรวจสอบเองไว้

**ส่วนที่ขาดหายและผู้ตรวจจับได้ ตอนนี้เพิ่มแล้ว**
- เกณฑ์คลินิก <5° กับตัวเลข "ความคลาดมุมงอเข่าของ OMC <5°" อ้างมาจาก **แหล่งเดียวกัน**
  (McGinley et al. 2009 ที่ซ้ำเป็น ref 68 และ 82) → ความคลาดของ ground truth เองอยู่ตรงเส้นเดียวกับที่ใช้ตัดสินว่า
  HPE ใช้ไม่ได้ · เพิ่มในหัวข้อ 4 ข้อ 1
- ข้ออ้างเชิงอนาคตของเปเปอร์ว่า **การใช้แบบ 2D ล้วนพร้อมมุมกล้องที่เหมาะสมอาจถึงระดับความแม่นที่ต้องการได้**
  — เหตุผลจากตัวเปเปอร์ที่หนักแน่นที่สุดสำหรับ E6 · เพิ่มในหัวข้อ 3.3 และยกมาอ้างในแถว E6 ของหัวข้อ 8
- **การ fine-tune บนชุดข้อมูลเฉพาะงาน** ในฐานะแนวทางปรับปรุงที่เปเปอร์เสนอเอง · เพิ่มในรายการคำแนะนำ
- ผลอันดับหนึ่งของ BlazePose ส่วนหนึ่งมาจาก **การที่ชุดฝึกกับชุดทดสอบมีการกระจายตรงกัน** (ข้อมูลฝึกโยคะ/ฟิตเนส
  คล้าย Physio2.2M มาก) — เป็นข้อควรระวังที่หนักแน่นและอ้างได้ดีกว่าการบอกว่า "วิดีโอเต้นยากกว่า" · เพิ่มในหัวข้อ 11 ข้อ 5
- PoseFormerV2 ก็เติมช่องว่างได้และก็คืนค่าเป็นหน่วยเมตริกเช่นกัน · เปเปอร์อธิบายว่าความลึกของ lifter ที่แพ้
  น่าจะมาจากความต่างของชุดข้อมูลฝึก · แหล่งของตัวเลข 3–54 มม. เป็นเรื่องข้อสะโพกโดยเฉพาะ · และส่วนงานอนาคต
  ของผู้เขียนเองก็ชี้ว่าผลเรื่องรยางค์ส่วนบนเป็นจุดอ่อนที่สุดของงาน · เพิ่มครบทุกข้อแล้ว

**ความเสี่ยงที่ยังเหลือ** — มีเงื่อนไขปิดกั้นเหลืออยู่หนึ่งข้อสำหรับข้ออ้างใด ๆ ที่เกินกว่าบันทึกนี้:
ต้องไปดึง **ตาราง Supplementary S1–S5** ก่อนจะอ้างตัวเลขรายโมเดลที่ไม่ได้ระบุชื่อในเนื้อ Results
(รวมถึง "BlazePose 'Local' ≈ 80 มม.") · ร่างระบุเรื่องนี้ไว้แล้วและผู้ตรวจเห็นด้วยว่าตีกรอบไว้ถูกต้อง
