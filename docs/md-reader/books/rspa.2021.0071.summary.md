# A0-3b · Joshi & Chakrabarty (2021) — An extensive review of computational dance automation techniques and applications

**File read:** `knowledge/reading_docs/rspa.2021.0071.pdf` (21 pages, 6 figures, 1 table, 83 references)
**Citation (the version to cite):** Joshi M, Chakrabarty S. 2021. *An extensive review of computational dance automation techniques and applications.* **Proc. R. Soc. A 477: 20210071.** doi:10.1098/rspa.2021.0071 · Received 2 March 2021, accepted 9 June 2021 · Article type: Review · Subject areas: artificial intelligence, human–computer interaction, computer modelling and simulation.
**Affiliations:** Manish Joshi — School of Computer Sciences, KBC North Maharashtra University, Jalgaon (ORCID 0000-0001-8783-8567, corresponding author). Sangeeta Chakrabarty — S.S. Dempo College of Commerce and Economics, Cujira, Bambolim, Goa.
**Companion file:** the arXiv preprint `1906.00606v1.pdf` already has a full summary, `1906.00606v1.summary.md`, whose §8 is a two-version comparison. **This file is the journal version's own summary.** It does not repeat that comparison. It records what the journal says, adds journal-only defects the earlier comparison missed (§6.3), and lists errors found in the earlier summary (§8).
**Reading method:** Three-Pass (Keshav) per `reading_guide.md`. Pass 3 for a survey means auditing the taxonomy against Table 1 and the citation graph against the reference list. §6 records that audit.
**Read + verified:** 2026-09-21 (scheduled `read-a-paper` run; independent second pass, see §10)

---

## ⚠️ Read this first

1. **This is the version to cite, and it is a map, not a benchmark.** In 21 pages it reports **no metric, no dataset table, no comparison and no evaluation protocol**. Every number in it is second-hand from a cited work (§5). Use it for **one Related Work sentence** and nothing in `evaluation_methods.md`.
2. **"Static Pose / Dynamic Connection" is not in this paper.** Neither phrase appears in the body, Table 1, the figure trees or the reference list. The closest wording is "GAs to find **static dance poses** for single beat and Multi Beat" (§6(a)(i), about Jadhav et al. [51–54]). The checklist's attribution in item 15 has to be removed or re-sourced. This matches the preprint finding.
3. **The earlier comparison missed some citation errors.** One is new in the journal: ref [7] changed from the preprint's correct "Annemette P. Karpen" to **"Annemette PK"**, which files the given name as the surname. Carried over from the preprint: ref [62] reads **"Dipankar D, Zbigniew M"**, with both given names used as surnames (the real surnames, Dasgupta & Michalewicz, are outside knowledge). Ref [5] is **Wikipedia (2014)**. Check these before any bibliography export pulls author names from this paper (§6.3).
4. **The white-space claim needs one nuance for the journal version.** The earlier summary said k-means is "the one place a clustering algorithm appears at all". The journal also cites **SLIC (Simple Linear Iterative Clustering)** [63], but only for pixel-level superpixel **segmentation of dance-pose images**. It is still not a movement vocabulary, so the claim survives with its wording tightened (§7.2).

---

## 1. Five Cs (`reading_guide.md`, pass 1)

| C | Answer |
|---|---|
| **Category** | **Survey / taxonomy paper.** It proposes a classification of "Dance Automation" and sorts the cited literature into it. It is not experimental and not a prototype. |
| **Context** | It positions itself against **an unattributed 1990 *Leonardo* bibliography**, cited inline in the abstract with no author and no reference number (the preprint's ref [1] identifies it as Politis; the name "Politis" appears nowhere in the journal), and **Sagasti 2019** (*Dance Chronicle* 42:1–52, ref [4], §1), which it says "covers only one aspect of dance automation". It adopts no theoretical framework. The organising principle is the authors' own aspect scheme. |
| **Correctness** | The taxonomy is plausible but unvalidated. There is no search protocol, no inclusion criteria and no inter-rater check. The paper contradicts itself on three counts: **six** aspects in the abstract and conclusion but **eight** rows in Table 1; the abstract implies the only prior review dates to 1990, yet §1 cites Sagasti 2019; "at least 100" papers against 83 references. Several individual items are filed in the wrong place (§6.2). |
| **Contributions** | (a) The terms **"Dance Automation"** ("We define and illustrate the concept…", abstract) and **"dance informatics"** (§1), both used for the same scope. (b) The **six-aspect taxonomy**, drawn as six tree figures. (c) **Table 1, "Dance automation compilation"**, which maps every sub-category to its reference numbers and is the most useful artefact in the paper. (d) A narrative pass over 1967–2020 with strong coverage of **Indian classical dance** computing. |
| **Clarity** | Readable, but it is a list of "X et al. did Y" with no synthesis, no critique of any reviewed work and no stated open problems. That falls short of the abstract's promise that readers can "easily determine the state of research and the new avenues left for exploration". |

## 2. อ.Proadpran extraction table

| Field | Content |
|---|---|
| **Motivation** | Dance is creative, social ("we cannot consider dance in isolation at all", because teachers, choreographers, co-dancers and musicians are involved even in a solo), and it "was the slowest to adopt technology". Research since 1967 is scattered, and the authors see no comprehensive multi-aspect review. |
| **Research Question / Thesis** | A curation goal: group computer-assisted dance work into aspects so that a newcomer can see the state of research and its gaps ("one-stop information", §10). |
| **Proposed Method** | Six aspects (abstract/§10): **dance representation, dance capturing, dance semantics, dance generation, dance processing approaches, applications**. The body adds **dance visualization (§7)** and **dance robotics (§8)** as separate sections, and Table 1 lists them as separate aspects. Each aspect is split into sub-categories and populated with citations. |
| **Evaluation** | **None.** The only support offered is the coverage claim "We have reviewed at least 100 of such research papers and articles" (§10). |
| **Contribution** | Terminology, a navigational map with a reference table, and an entry point into BharataNatyam/Odissi/Kuchipudi/Kathakali computing. |

## 3. Problem and motivation (§1)

- History: Noll 1967, *Dance Magazine* [1]; Cunningham [2] (a 1968 book, cited as a 2019 reprint); Savage & Officer's interactive model "Choreo", 1978 [3]. Then, "after a long gap", Sagasti's 2019 review [4].
- The gap claimed is a **literature-map gap**. The abstract says the only review found dates to 1990. §1 then admits Sagasti 2019 but calls it single-aspect.
- New framing in the journal version: "Computer empowerment to any aspects of dance ensures enhancement in dance performance". This is asserted, not supported.
- The conclusion names the audience: "one-stop information of automation of any of the aspects of dance including the choreographic process". First author Joshi co-authored the BharataNatyam choreography-generation line (refs [40], [51]–[54], [60], all "Jadhav S, Joshi M, Pawar J"; the paper names only [51]–[54] "ArttoSMart"). That Jadhav and Chakrabarty are the same person is a circumstantial inference from the earlier summary, not something this PDF states. This self-involvement explains both the paper's Indian-classical strength and its bias toward GA-based generation.

## 4. Core contribution: the taxonomy and Table 1

The whole contribution is the classification. Here it is as drawn in Figures 1–6 and Table 1 (journal reference numbers):

| Aspect (section) | Sub-categories → refs (Table 1) |
|---|---|
| **Dance Representation** (§2, Fig. 1) | Notation [5,6] → Labanotation [7–10], LMA [11–13] · Grammar → dance grammar [14–17], **CLA** (Choreographic Language Agent) [18–20] |
| **Dance Capturing** (§3, Fig. 2) | Sensors [21–26] · Motion capture [27] → monocular vision [21,28–30], multi-view vision [22,31–33] |
| **Dance Semantics** (§4, Fig. 3) | Annotation [14,34–38] · Ontology [35,37,38] · Dance grammar (verbs) [14,15,39] · Vector space [40,41] · Graph [30,42] |
| **Dance Generation** (§5, Fig. 4) | Animated dance steps [9,43–45] · Computer-aided choreography [41] → fully automated [25,31,41,46–57], semi-automated [15,16,21,58], image generation [40,59–61] |
| **Dance-Processing Approaches** (§6, Fig. 5) | Evolutionary [62] → GAs [31,41,48,49,51–54], flock [30] · Classification [63–65] → neural network [66–68], SVM [37,69] · Graph-based [16,42,70] · Image processing through gesture recognition [22,69–73] · Corpus-based [16,17,74] · Multi-agent [47] |
| **Dance Visualization** (§7) | [27,66,75,76] |
| **Dance Robotics (Humanoid)** (§8) | [32,77–80] |
| **Applications** (§9, Fig. 6) | Entertainment [78] · E-learning/distance learning [12,29,36,45,70–73,81] · Heritage preservation [7,35] · Medical therapy [21,82] · Tutor [27,44,83] |
| (footer rows) | Pioneering work [1–3] · Review and bibliography [4] |

Content worth keeping, by section:
- **§2 Representation.** The two main Western notations are Labanotation and Benesh; Eshkol-Wachman and DanceWriting are used less (sourced to Wikipedia [5]). Karpen [7] found that Sutton DanceWriting and Labanotation both fail on BharataNatyam facial expressions, hand gestures, neck and shoulder movement, and footwork. LabanDancer [9] turns Labanotation scores into 3D animation. Dance grammars: CorX if-then rules [15], Stuart & Bradley's corpus-based grammar of joint movements [16], Bull's aerobics grammar from a national-survey corpus [17]. CLA writes sentences in a formal language and animates points, lines and planes in 3D [18–20] (used in Wayne McGregor's studio).
- **§3 Capturing.** Qian et al.: **41 markers**, real-time gesture-driven system, real-time marker cleaning, **eight-camera VICON** [22]. Instrumented dancing shoes [23]. Wireless wrist and ankle sensors [24]. Butoh wearable classification [26]. OptiTrack folk-dance learning system [27]. Monocular: silhouette-based markerless 3D [28], Virtual Kathakali [29], BharataNatyam skin-colour tracking of the **upper body only** [30]. Multi-view: Nakazawa et al. used **eight cameras and eight PCs** to find motion primitives of *Soran Bushi* and **concatenate them into new motions** with IK and dynamic balancing [32]. *Style Machines* [33] is filed here.
- **§4 Semantics.** Mallik et al. built ontology and annotation for Indian classical dance [35,37,38]. Video annotation with MOWL + a Bayesian network used **200 videos of about 10–15 min** [38 only]. Hsieh & Luciani's Newtonian "dance verbs" [39]. Jadhav et al.'s limb-wise vector-space model with Natyasastra names [40]. **Carlson et al.'s 13-value "movement catalyst"**: 8 joint angles (shoulders, elbows, hips, knees), 1 height level and 4 effort qualities, evolved by a GA [41]. Graph: a pose is a node and a transition is an edge [30]; an attributed relational graph of upper-body poses [42].
- **§5 Generation.** *Animated steps:* Latin-dance shoulder/hip phase difference [43], LabanDancer [9], a ballet tutor on Life Forms [44], a BharataNatyam movement library [45]. *Fully automated:* an HMM humanoid dance rated by **three professional judges** [46]; Hagendoorn's emergent group patterns [47]; a GA waltz system that "resulted within **10%** of the optimal choreography" [48]; Choreogenetics variants over **five basic movements** [31]; the dancing-genome duet [49]; swarm toolkit plus Life Forms [50]; Scuddle [41]; ArttoSMart (input is the number of beats plus a starting pose) [51–54]; **GrooveNet** [55]; **Yalta et al.**, a conv + multi-layer LSTM on an audio power spectrum [56]; **Pettee et al.**, RNN + autoencoder on mocap [57]. *Semi-automated:* Stuart & Bradley interpolate between postures over a corpus of **10 Balanchine ballets** [16]; the Pleo robot [21]; CorX [15]; collaborative choreography [58]. *Image generation:* BharataNatyam karanas from stick figures to a volumetric model [59]; automated stick figures from the 30-attribute model [60]; **chor-rnn** [61].
- **§6 Processing.** GA fitness functions: the waltz system weights couple position, stage use, step sequence, closeness to ideal steps and so on "equally" [48]; ArttoSMart's fitness converges "neither too close nor far" from ideal *adavus* [51–54]; Lapointe & Epoque's "virtual vocabulary of four movements: run, jump, turn and fall" [49]. Classification: Kumar et al. SLIC/watershed segmentation of **100 Kuchipudi mudras** [63]; foot-posture (*Stanas*) classification with a DNN and Naive Bayes [64], extended to video annotation by foot-pose class [65]; a CNN for *Navrasas* emotions on Kinect data [67]; Nrityantar deep action recognition [68]; **k-means + SVM** over expert-labelled video segments [37]; SVM *adavu* classifier [69]. Graph/gesture: **28 single-hand gestures (Asamyukta Hastas)** [70–73]. Corpus: ACCOLADE aerobics corpus [17]; **Tang et al., 907,200 frames of 3D dance across four dance types, LSTM-autoencoder music→dance** [74].
- **§7–8.** Calvert et al. stage visualization [75]; NAC virtual studio [76]; Dance Evolution (Panda 3D) [66]; HRP-2 dancing via operational-space inverse dynamics [77]; **Shinozaki et al., 60 dance units extracted and concatenated** for hip-hop robot dance [78]; beat-synchronised robot [79]; Aibo [80].
- **§9 Applications.** VR Salsa training [81]; Parkinson's dance intervention: "improved motor symptoms in both short (1-day) and long-term (12-week) durations" [82]; dance used to teach computer literacy [83]; hip-hop chosen over ballet for the robot because ballet "does not have specific rules for the details of whole body motions" [78].

## 5. Results: what is actually reported

The paper has **no results of its own.** Every figure is quoted from a cited work without context:
10% of optimal [48]; three judges [46]; five basic movements [31]; four-movement vocabulary [49]; 41 markers and 8-camera VICON [22]; 8 cameras / 8 PCs [32]; 200 videos × 10–15 min [38]; 100 mudras [63]; 28 gestures [70]; 10 Balanchine ballets [16]; 13-value catalyst [41]; 30-attribute model [40,60]; 60 dance units [78]; 907,200 frames / 4 dance types [74]; 1-day / 12-week [82]; 1967–2020 span; "at least 100" papers. No statistics and no significance tests appear. Nothing here can be compared across studies.

## 6. Assumptions, limitations, defects

### 6.1 Methodological
- No search databases, no query strings, no inclusion criteria, no PRISMA-style accounting. The "1967–2020" range is stated, but the ML generation references stop in 2019 and the newest references are 2020 [27,64,65,81].
- There is no critique, no synthesis and no open-problems section. The abstract's promise of "new avenues left for exploration" is never delivered.
- §6 promises "Genetic, Flock and **Ant optimization**" algorithms, but no Ant section exists and Fig. 5 shows only GA and flock. Likewise §1 promises approaches "including **probabilistic model**, evolutionary model, classification, multi-agent systems", but there is no probabilistic sub-section.
- The **author bias** is visible. Self-citations are 6 of 83 references (~7%: [40], [51]–[54], [60]), and GA methods get their own detailed sub-section, while the deep-learning generators [55–57,61,74] get one to four sentences each.

### 6.2 Taxonomy defects (Table 1 vs text)
- **Six vs eight aspects.** The abstract, §1 and §10 all say six. §1 treats visualization and robotics as "discussed separately in §§7 and 8". But Table 1 gives them their own aspect rows, making **eight**.
- **Image generation**: the §5 text and **Fig. 4** make it a top-level sibling ("three major aspects") of animated dance steps and computer-aided choreography. The section numbering ((b)(iii)) and Table 1 put it **under** computer-aided choreography.
- **Choreogenetics [31] is filed under Capturing → multi-view vision.** It is a GA choreography method (§5, §6 GA list). In the text, the "eight cameras and eight PCs" in the same paragraph belong to Nakazawa [32].
- ***Style Machines* [33]**, a generative style-synthesis method, is filed under Capturing.
- **Kumar et al. [63]** is SLIC/watershed image segmentation but is filed under Classification. That clashes with the section's own definition ("the user knows ahead how classes are defined").
- **Multiple filing without explanation:** Qian [22] appears under sensors, multi-view and gesture recognition; Nakazawa [32] under multi-view and robotics; Takahashi & Ueda [25] under sensors and fully automated generation.
- **Yu & Johnson [50]** is described "with a multi-agent system", but the Table 1 multi-agent row lists only [47].
- **Flock → [30]**: "Mamani et al. [30] has used a flock technique". Ref [30] is **Mamania, Shaji & Chandran 2004, "Markerless motion capture from monocular videos"**, not a flocking work. (The preprint had "Hagendoorn [31]", where [31] is Mallik's *Nrityakosha*: a certainly wrong number and **probably** the right name, an inference neither PDF confirms independently. The journal made name and number agree while still being wrong, and propagated the error into Table 1.)

### 6.3 Citation and reference-list defects (checked against the reference list)
| Location | Defect | Present in preprint? |
|---|---|---|
| Ref [7] | **"Annemette PK. 1990"**: the given name is filed as the surname. The body says "Karpen" (§2) and "Annemette Karpen" (§9c). | **No.** Preprint [7] reads "Annemette P. Karpen" (correct). **New in the journal**, not listed in the earlier summary's §8.4. |
| Ref [62] | **"Dipankar D, Zbigniew M. 1997"**: both given names filed as surnames. *(Outside knowledge, not from the PDF: the book is by D. Dasgupta & Z. Michalewicz.)* | Yes (preprint [51]). **Not recorded** in the earlier summary. |
| Ref [5] | **Wikipedia (2014)** cited for the main notation systems. | Yes (preprint [5]). Not recorded earlier. |
| §2(b)(ii) | "Work by **Scott [19]**": [19] is **DeLahunta S. 2016**, so the given name is used as the surname. | No (journal-only). Already recorded in the earlier summary's §8.4. |
| Body vs ref [46] | Body says "Manfre et al."; the list says "**Manfra** A…". | Journal-only. Already recorded. |
| Abstract vs refs | The 1990 *Leonardo* bibliography is cited inline in the abstract **without author or reference number**. Politis (preprint ref [1]) was dropped from the journal list, and Table 1's "review and bibliography" row is [4] (Sagasti) only. | Already recorded. |
| Ref [24] | Publisher field reads "Paris, France, France: IRCAM **&#8212;** Centre Pompidou". An HTML entity leaked into the typeset reference, and "France" is doubled. | Yes (preprint [21]). Carried over. |
| Ref [2] | Cunningham 1968, *Changes*, cited as a "Reprint edition (17 September 2019)". | Not relevant. |
| §7 | "Calvert et al. … [75] and **edited by Potel**". Potel is named in the text but appears nowhere in ref [75] (Calvert T, Wilke W, Ryman R, Fox I). *(Outside knowledge, not from the PDF: Potel was probably the IEEE CG&A department editor.)* | Yes (preprint, same wording for its [58]). |

### 6.4 One fix the journal made that the earlier summary missed
The preprint §2 said "**Latin American** dance styles like Ballroom, Foxtrot, Waltz has been used". The journal changed this to "Dance styles like Ballroom, Foxtrot and Waltz have been used", so it stopped labelling those three as Latin American. The journal keeps the previous sentence's "Labanotation followed by Latin American dance styles". The earlier summary's style list (line 103) still repeats the preprint's "Latin American (Ballroom, Foxtrot, Waltz)".

## 7. Relation to adjacent work and to our project

### 7.1 Adjacent work it cites that matters to us
- **Concatenative unit lineage:** Nakazawa et al. 2002, *Soran Bushi* motion primitives [32]; Shinozaki et al. 2007, 60 dance units [78]. Unit-based dance generation is roughly 20 years old. Our novelty cannot be "we use units".
- **Graph/transition lineage:** a pose is a node and a transition is an edge [30]; Stuart & Bradley's "transition graphs for capturing transition probabilities for every body joint" with A* search over a 10-ballet corpus [16]. This is a 1998 precedent for our `transition_matrix.npy`, alongside A1-21 Galata VLMM.
- **Deep-learning lineage (journal only):** chor-rnn [61] (= our checklist item 21, A1-2), GrooveNet [55], Yalta [56], Pettee [57], Tang LSTM-autoencoder [74]. This is the early end of the line that ends at L3-5 (Atomic Movements) and A1-16 (Rhythm is a Dancer).
- **Hand-designed pose codes:** Carlson's 13-value movement catalyst [41] and Jadhav's 30-attribute model [40]. These are the nearest things to a quantised pose code in the paper, and both are **declared by humans**.

### 7.2 White-space claim (tightened wording for the journal version)
In the journal's own map, **no movement vocabulary is described as obtained by clustering pose data.** Some vocabulary-like objects are explicitly human-designed: Lapointe & Epoque's 4 movements [49], Carlson's 13-value catalyst [41], Jadhav's 30-attribute model [40]. For the others (Nakazawa's primitives [32], "recognized" by "a motion analysis method"; Shinozaki's 60 units [78], which "were extracted") **the review does not say how the units were obtained.** Checking that needs the primary papers. The two clustering algorithms that do appear are used for **other purposes**: **k-means** is used in training an SVM ("Using a k-means clustering algorithm, Mallik et al. [37] have trained an SVM classifier") over expert-labelled video segments (recognition) [37], and **SLIC** does pixel superpixel segmentation of pose images [63]. Neither is used as a generative vocabulary.
**Safe wording:** "In Joshi & Chakrabarty's (2021) broad review of computational dance, clustering appears only for recognition or image segmentation, never as the source of a generative movement vocabulary."
**Do not write:** "clustering never appears", "k-means is the only clustering", "the most recent review" (later surveys exist, e.g. checklist A0-1, A0-10, A0-2), or "all units were hand-cut".

### 7.3 Other uses
- It closes the "non-Western classical dance is untouched" door (Indian classical dance is heavily covered), in the same way L3-12 Text2Tradition does for Thai dance.
- Motivation material: heritage preservation [7,35], therapy [21,82].

## 8. Errors found in the existing `1906.00606v1.summary.md` (the "verify what already exists" pass)

| Where in that file | What it says | What the PDFs say | Severity |
|---|---|---|---|
| §4.2 (line 70), §5 (line 105); §11 (line 337) | "Multi-view: choreogenetics with **8 cameras / 8 PCs** [27]". §11 confirms the *numbers* verbatim, but never checked the attribution | Preprint: "Lapointe et al. [27] have used genetic algorithm … through choreogenetics algorithm. Using motion capture with 8 cameras and 8 PCs, **Nakazawa et al. [28]** …" The camera count belongs to **Nakazawa [28]** (journal [32]), not choreogenetics. **Both earlier passes missed this.** | Medium: a misattributed number |
| §8.4 | Lists two new journal defects (Scott [19], Manfra [46]) | A third one exists: **ref [7] "Annemette PK"**, where the preprint's correct "Annemette P. Karpen" became given-name-as-surname | Low |
| §6.3 | Names errors fixed or kept | Omits **ref [62] "Dipankar D, Zbigniew M"** (in both versions) and the **Wikipedia ref [5]** | Low |
| §9.2 | "The one place a clustering algorithm appears at all, k-means" | True for the preprint. **False for the journal**, which adds SLIC [63] (segmentation) | Low, but it is a quotable claim, so fix the wording (see §7.2) |
| §9.2 and §9.5 | Mixes numbering systems. In §9.2, [43], [60], [28], [36] and [33] are **preprint** numbers, while [41] Carlson is a **journal** number. §9.5 (line 228) mixes preprint [31], [7], [18] with journal [82] (Parkinson's) | Journal equivalents: Lapointe & Epoque [49], Shinozaki [78], Nakazawa [32], Jadhav vector space [40], Mallik k-means [37] | Low: confusing if copied into the thesis |
| §4 / §5 (line 103) | "Latin American (Ballroom, Foxtrot, Waltz)" | This is the preprint's wording. The journal corrected it (§6.4 above) | Trivial |

*(Suggestion only. This run did not edit that file, because the task allows modifying only the checklist ticks and writing the new summary.)*

## 9. Checklist pass — `reading_checklist.md`, item by item

Legend: **Addressed** = the paper gives usable content for the item · **Partial** · **Not covered**.

**TIER 0**
1. A1-21 Galata VLMM — **Not covered.** VLMM is not cited. The closest thing is Stuart & Bradley's per-joint transition-probability graphs [16] (1998), a useful extra precedent for E2.
2. A1-12 SinMDM — **Not covered** (it predates SinMDM). No diversity or coverage metric.
3. A0-9 DASB — **Not covered.**
4. A0-8 speech-token review — **Not covered.**
5. A1-14 monocular HPE accuracy — **Not covered.** Monocular capture methods are listed [28–30], but there is no pose-estimation accuracy content (only the "upper body only" restriction [30]).

**TIER 1**
6. A1-16 Rhythm is a Dancer — **Not covered** (published after this review).
7. A1-17 Keyposes — **Not covered.** A related idea appears: Stuart & Bradley interpolate between prescribed postures [16].
8. A1-19 FSQ — **Not covered.**
9. L3-22 Labrak — **Not covered.**
10. B1-15 Matrix Profile VI — **Not covered.** (A loose analogy only: Karpen [7] found that notation misses face, hands, neck and footwork detail.)
11. L3-5 Atomic Movements — **Partial**, as lineage only: GrooveNet [55], Yalta [56] and Tang [74] are the music→dance precursors.
12. A1-22 MotionCritic — **Partial.** Only human-judge evaluation (three professional judges [46]; "expert evaluation is sought" [50]), with no protocol.
13. A1-18 vocab scaling — **Not covered.**

**TIER 2**
14. L3-12 Text2Tradition — **Not covered** directly. It supports the same "classical dance is not untouched" argument (§7.3).
15. **This item (A0-3b)** — **Addressed.** Both versions are now read and summarised, and the comparison is done (`1906.00606v1.summary.md` §8 plus this file's §6.3 and §8). **"Static Pose / Dynamic Connection" is not in this paper.**
16. A0-1 motion-generation survey — **Not covered.**
17. A1-7 Motion Texture — **Not covered.** Its ancestors are covered: primitives [32] and 60 units [78].
18. L3-30 DC-Motion — **Not covered.**
19. A1-20 Skeleton Motion Words — **Partial.** Limb-wise coding (Jadhav's per-limb vector space [40]; Carlson's per-joint angles [41]) is a hand-designed precedent for per-joint units.
20. Dance Fingerprinting / DanceCrafter / TokenDance — **Not covered.**
21. A1-2 chor-rnn — **Addressed as a citation**: [61], a deep RNN generating solo-dancer sequences shown as stick figures. It confirms the checklist's description of chor-rnn as a single-dancer precursor.
22. A1-6 BlazePose — **Not covered.**
23. L3-20 DisCoRD — **Not covered.**

**TIER 3:** 24–27, 29–31 **Not covered.** 28 (Camurri, QoM) is **Not covered**: LMA is mentioned [11–13], but not Camurri's indices.

**Paywalled list, R11 items, E1–E11:** **Not covered**, except as follows. R11-4 folk-rnn: **Not covered**, though the same "declared vs discovered" contrast applies (§7.2). E2: Stuart & Bradley [16] adds a 1998 transition-graph precedent.

**Checkbox action:** item 15 is already `[✅]`. **Tick definitions conflict:** item 15's own note asks for one ✅ when both versions are read and summarised and a second ✅ when they are compared, while the legend (line 12) says first ✅ = team, second ✅ = Cop. Under either reading, the team's first ✅ is already there. The second ✅ is Cop's under the legend, so this run does not add it. **No checkbox was changed this run.** The user should decide which definition applies.

## 10. Verification (independent second pass)

**Who:** Vera (the `fact-auditor` subagent), working independently from the PDFs. It did not rely on the draft's own text extraction. It re-extracted both PDFs (pdftotext raw and layout, plus PyMuPDF, with line-break hyphens removed), rendered pp. 4, 5, 6, 9, 10, 13 and 16 as images to check Table 1 and Figs 1–6, and checked §8's claims against the actual lines of `1906.00606v1.summary.md`. **Verdict: REVISE.** All corrections below have been applied.

**What was checked:** every row and reference range in Table 1; all six figure trees; every number (41 markers, 8-camera VICON, 8 cameras / 8 PCs, 200 videos × 10–15 min, 13 = 8+1+4, three judges, 10%, five movements, 10 ballets, 30 attributes, 100 mudras, 28 gestures, 907,200 frames / 4 types, 60 units, 1-day / 12-week, 83 refs, 21 pp., dates); all quotes; the citation-error claims; the "Static Pose / Dynamic Connection" search (0 hits in both versions); the SLIC/k-means claim; the §8 error claims about the earlier summary; the §9 checklist verdicts.

**Blockers fixed (3):**
1. The draft said the abstract names **Politis**. It does not; "Politis" appears 0 times in the journal. The abstract cites "Leonardo 1990 Computers and dance: A bibliography" with no author. Fixed in §1 and §6.3.
2. The "safe wording" called this "**the most recent** broad review". That is outside knowledge and false for our own registry (A0-1, A0-10 and A0-2 are later). Removed.
3. The draft said Nakazawa's primitives and Shinozaki's 60 units were "human-declared or hand-segmented". The review does not say how they were obtained. Fixed in §7.2.

**Numeric and citation corrections (7):** ref [24]'s `&#8212;` and the Potel wording are both **carried over from the preprint**, not "not checked"; MOWL and the 200 videos belong to **[38] only**; the DNN + Naive Bayes classifier is **[64]**, and [65] is the annotation extension; the mixed numbering in the earlier summary is in **§9.2 and §9.5**; its line 337 confirmed the *numbers* verbatim but never the attribution; Tang [74] gets four sentences, not "one to three".

**Overstatements corrected (8):** §1 of the paper **supports six aspects** (the draft wrongly said §1 lists eight), so the contradiction is Table 1 alone; "only a 1990 review" was quoted but is a paraphrase; the Dasgupta/Michalewicz and Potel facts are now labelled outside knowledge; the ArttoSMart involvement is attributed to **first author Joshi** only (Jadhav = Chakrabarty stays circumstantial); flock = Hagendoorn is softened to "probably"; the "Latin American" fix is narrowed; checklist items 5 and 10 are downgraded to Not covered.

**Omissions added (6):** Fig. 4 sides with the text against the numbering and Table 1 on image generation; the unfulfilled "probabilistic model" promise in §1; the Politis drop plus Table 1's review row being [4] only; multiple filings (Qian [22], Nakazawa [32], Takahashi & Ueda [25]); the self-citation rate of 6/83 (~7%); the conflict between the two checklist tick definitions.

**Confirmed safe to cite:** all Table 1 contents; the six-aspect claim in the abstract, §1 and §10; the ref [7] "Annemette PK" regression (the preprint has "Annemette P. Karpen"); ref [62] and ref [5]; "Scott [19]" and "Manfre/Manfra"; flock → [30] Mamania; SLIC [63] and k-means [37]; all §8 errors in the earlier summary (in particular **8 cameras / 8 PCs belongs to Nakazawa, not choreogenetics**).

**Residual uncertainty:** real-world facts about Potel, Dasgupta & Michalewicz, and Karpen's surname were not checked against external sources. Flock = Hagendoorn depends on the preprint authors' intent. Jadhav = Chakrabarty is still circumstantial. How Nakazawa's and Shinozaki's units were built needs the primary papers [32] and [78].

---

## 11. ฉบับภาษาไทย (Thai version)

### 11.1 ข้อมูลเปเปอร์
**Joshi M, Chakrabarty S. 2021.** *An extensive review of computational dance automation techniques and applications.* **Proc. R. Soc. A 477: 20210071** · doi:10.1098/rspa.2021.0071 · 21 หน้า, 6 รูป, 1 ตาราง, 83 references · ฉบับตีพิมพ์ของ arXiv:1906.00606 (ซึ่งมีสรุปแยกแล้วใน `1906.00606v1.summary.md` §8 เปรียบเทียบสองฉบับ) → **ให้อ้างฉบับนี้เท่านั้น**

### 11.2 ⚠️ อ่านตรงนี้ก่อน
1. **เป็น "แผนที่" ไม่ใช่ benchmark.** ทั้ง 21 หน้า **ไม่มี metric, ไม่มีตาราง dataset, ไม่มีการเปรียบเทียบ, ไม่มีโปรโตคอลประเมิน** ตัวเลขทุกตัวยกมือสองจากงานที่อ้าง → ใช้ได้แค่ **1 ประโยคใน Related Work** ห้ามอ้างใน `evaluation_methods.md`
2. **"Static Pose / Dynamic Connection" ไม่มีในเปเปอร์นี้** (ค้นทั้งเนื้อความ, Table 1, รูป tree, บรรณานุกรม = 0) คำที่ใกล้สุดคือ "GAs to find static dance poses for single beat and Multi Beat" (§6(a)(i)) → ต้องลบ/หาที่มาใหม่ให้ checklist ข้อ 15
3. **ข้อผิดพลาดการอ้างอิงที่รอบก่อนตกหล่น:** ref [7] ฉบับ journal เขียน **"Annemette PK"** (เอาชื่อต้นเป็นนามสกุล — preprint เขียนถูกว่า "Annemette P. Karpen" → **journal ทำพังเอง**) · ref [62] **"Dipankar D, Zbigniew M"** (ชื่อต้นเป็นนามสกุลทั้งคู่ มีมาตั้งแต่ preprint) · ref [5] คือ **Wikipedia (2014)**
4. **ข้ออ้าง white space ต้องปรับถ้อยคำ:** ฉบับ journal มี **SLIC (Simple Linear Iterative Clustering)** [63] ด้วย — แต่ใช้แบ่ง superpixel ในภาพ ไม่ใช่คลังคำท่าเต้น

### 11.3 Five Cs
| C | คำตอบ |
|---|---|
| **Category** | Survey/taxonomy — จัดหมวด "Dance Automation" แล้วโยนงานที่อ้างเข้าหมวด |
| **Context** | เทียบกับ bibliography ปี 1990 ใน *Leonardo* (อ้างใน abstract แบบไม่มีชื่อผู้แต่ง ไม่มีเลขอ้างอิง — preprint ระบุว่าเป็น Politis) และ Sagasti 2019 [4] ซึ่งเขาบอกว่า "ครอบคลุมแค่ด้านเดียว" · ไม่มีฐานทฤษฎี |
| **Correctness** | ไม่มี search protocol / เกณฑ์คัดเลือก · ขัดแย้งในตัวเอง 3 จุด: abstract/§1/§10 บอก **6 ด้าน** แต่ Table 1 มี **8 แถว** · abstract ส่อว่ามี review เดียวปี 1990 แต่ §1 อ้าง Sagasti 2019 · "อย่างน้อย 100 เปเปอร์" แต่มี 83 refs |
| **Contributions** | คำว่า "Dance Automation"/"dance informatics" · taxonomy 6 ด้าน (6 รูป tree) · **Table 1** (ของที่มีประโยชน์ที่สุด) · ครอบคลุมงานนาฏศิลป์อินเดียดีมาก |
| **Clarity** | อ่านง่ายแต่เป็นลิสต์ "X ทำ Y" ไม่มีการสังเคราะห์ ไม่วิจารณ์ ไม่มี open problems ทั้งที่ abstract สัญญาไว้ |

### 11.4 ตารางสกัดของ อ.Proadpran
| ช่อง | เนื้อหา |
|---|---|
| Motivation | การเต้นเป็นศิลปะเชิงสร้างสรรค์และเชิงสังคม ("we cannot consider dance in isolation at all") และ "slowest to adopt technology" · งานกระจัดกระจายตั้งแต่ 1967 |
| Research Question | จัดกลุ่มงานให้มือใหม่เห็นสถานะงานวิจัยและช่องว่าง ("one-stop information") |
| Method | 6 ด้าน: representation · capturing · semantics · generation · processing approaches · applications (+ visualization §7, robotics §8 แยกออกมา) |
| Evaluation | **ไม่มี** มีแค่ "reviewed at least 100 … papers" |
| Contribution | ศัพท์ + แผนที่ + Table 1 + ประตูเข้างาน BharataNatyam/Odissi/Kuchipudi/Kathakali |

### 11.5 ตัวเลขที่อยู่ในเปเปอร์ (มือสองทั้งหมด)
10% จาก optimal (GA waltz [48]) · กรรมการมืออาชีพ 3 คน [46] · 5 ท่าพื้นฐาน [31] · "virtual vocabulary" 4 ท่า run/jump/turn/fall [49] · 41 markers + VICON 8 กล้อง [22] · **8 กล้อง 8 PC = Nakazawa [32]** · 200 วิดีโอ × 10–15 นาที [38] · 100 mudras Kuchipudi [63] · 28 hand gestures [70] · 10 บัลเลต์ Balanchine [16] · movement catalyst 13 ค่า = 8 มุมข้อต่อ + 1 ระดับความสูง + 4 effort [41] · 30-attribute model [40,60] · 60 dance units [78] · 907,200 เฟรม 4 ประเภท (Tang LSTM-autoencoder) [74] · Parkinson ดีขึ้นทั้ง 1 วันและ 12 สัปดาห์ [82]

### 11.6 จุดอ่อนหลัก
- สัญญา "Ant optimization" (§6) และ "probabilistic model" (§1) แต่ไม่มีหัวข้อนั้นจริง
- จัดหมวดผิด: Choreogenetics [31] (GA) อยู่ใต้ Capturing → multi-view · *Style Machines* [33] อยู่ใต้ Capturing · Kumar [63] (segmentation) อยู่ใต้ Classification · **flock → [30]** แต่ [30] คือ Mamania 2004 markerless mocap (ไม่ใช่งาน flock) และลามเข้า Table 1
- image generation: text + Fig. 4 ให้เป็นพี่น้องระดับบน แต่เลขหัวข้อ + Table 1 ให้อยู่ใต้ computer-aided choreography
- อ้างผิดใหม่ใน journal: "Scott [19]" (= DeLahunta), "Manfre" vs "Manfra" [46], "Annemette PK" [7]
- self-citation 6/83 (~7%) + GA ได้พื้นที่มาก แต่ deep learning ได้ 1–4 ประโยคต่อชิ้น

### 11.7 ผลต่อโปรเจกต์เรา
- **ถ้อยคำ white space ที่ปลอดภัย:** "ใน review กว้างของ Joshi & Chakrabarty (2021) clustering ปรากฏเฉพาะงาน recognition (k-means + SVM [37]) หรือ segmentation ภาพ (SLIC [63]) — ไม่เคยเป็นที่มาของคลังคำท่าเต้นเพื่อ generation"
- **ห้ามเขียน:** "clustering ไม่เคยปรากฏ" · "k-means เป็นอันเดียว" · "review ล่าสุด" · "ทุกหน่วยตัดด้วยมือ" (เปเปอร์ไม่บอกว่า Nakazawa [32] / Shinozaki [78] ได้หน่วยมาอย่างไร)
- บรรพบุรุษที่ต้องยอมรับ: หน่วยท่าต่อกัน (Nakazawa 2002, Shinozaki 2007) · transition graph ต่อข้อต่อ (Stuart & Bradley 1998 [16]) → novelty ของเราต้องอยู่ที่ **"คลังคำได้มาจากการค้นพบ ไม่ใช่ประกาศ"**
- ปิดประตู "นาฏศิลป์ที่ไม่ใช่ตะวันตกยังไม่มีใครแตะ"

### 11.8 ข้อผิดพลาดที่พบในสรุปเก่า `1906.00606v1.summary.md` (ยังไม่ได้แก้ไฟล์นั้น — เสนอให้แก้)
1. **"choreogenetics with 8 cameras / 8 PCs [27]"** (บรรทัด 70, 105) → ผิด ตัวเลขนี้เป็นของ **Nakazawa [28]** · §11 บรรทัด 337 ยืนยันแค่ตัวเลข ไม่ได้เช็คว่าเป็นของใคร (**ทั้งสองรอบตรวจพลาด**)
2. §8.4 ขาด ref [7] "Annemette PK" (ความผิดใหม่ของ journal)
3. §6.3 ขาด ref [62] "Dipankar D, Zbigniew M" และ ref [5] Wikipedia
4. §9.2 "k-means เป็นที่เดียวที่มี clustering" → ไม่จริงสำหรับฉบับ journal (มี SLIC [63])
5. §9.2 / §9.5 ใช้เลข ref ปนกันระหว่าง preprint กับ journal
6. บรรทัด 103 "Latin American (Ballroom, Foxtrot, Waltz)" เป็นถ้อยคำ preprint ที่ journal แก้แล้ว

### 11.9 สรุป checklist (ย่อ)
- **ข้อ 15 (เปเปอร์นี้): Addressed** — อ่าน+สรุปครบทั้งสองฉบับ และเปรียบเทียบแล้ว · กล่องมี [✅] อยู่แล้ว **รอบนี้ไม่ได้เปลี่ยน checkbox** (✅ ที่สองเป็นของ Cop ตาม legend — แต่หมายเหตุในข้อ 15 นิยามคนละแบบ ให้ผู้ใช้ตัดสิน)
- **Partial:** ข้อ 11 (GrooveNet/Yalta/Tang เป็นต้นสาย music→dance) · ข้อ 12 (มีแค่ "กรรมการ 3 คน" ไม่มีโปรโตคอล) · ข้อ 19 (โค้ดแยกรายแขนขาแบบออกแบบเอง [40,41])
- **Addressed as citation:** ข้อ 21 chor-rnn [61]
- **ที่เหลือ: Not covered** (ข้อ 5 ถูกลดจาก Partial → Not covered หลังตรวจ) · E2 ได้ precedent เพิ่ม: Stuart & Bradley [16]

### 11.10 การตรวจสอบ
Vera (fact-auditor) ตรวจอิสระจาก PDF ทั้งสองฉบับ (re-extract เอง + render หน้า Table 1 และรูป 1–6) → **REVISE**: แก้ blocker 3 ข้อ (Politis ไม่ได้ถูกระบุชื่อใน abstract · "review ล่าสุด" เป็นความรู้นอกเปเปอร์ · อ้างว่าหน่วยของ Nakazawa/Shinozaki ตัดด้วยมือทั้งที่เปเปอร์ไม่ได้บอก) + ตัวเลข/อ้างอิง 7 จุด + overstatement 8 จุด + เพิ่มที่ตกหล่น 6 จุด — **แก้ครบแล้วทั้งหมด** · ตัวเลขทุกตัวใน §5 ตรงกับ PDF
