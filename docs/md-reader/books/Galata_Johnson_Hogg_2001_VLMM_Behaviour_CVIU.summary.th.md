# Galata, Johnson & Hogg (2001) — Learning Variable Length Markov Models of Behaviour
## (ฉบับแปลไทย)

*Computer Vision and Image Understanding* **81**(3):398–413 · DOI 10.1006/cviu.2000.0894
*(เลข volume / หน้า / DOI เอามาจาก `paper_notes/paper_index_A.csv` บรรทัด 60 — ไม่มีอยู่ในไฟล์ PDF เครื่องนี้เลย)*
ไฟล์: `knowledge/reading_docs/Galata_Johnson_Hogg_2001_VLMM_Behaviour_CVIU.pdf`
อ่านเมื่อ: 2026-09-16 · วิธี: Three-Pass (Keshav) ตาม `knowledge/reading_guide.md` · ผ่าน verification รอบสองแล้ว (§8)

> **ฉบับแปลของ** [`Galata_Johnson_Hogg_2001_VLMM_Behaviour_CVIU.summary.md`](Galata_Johnson_Hogg_2001_VLMM_Behaviour_CVIU.summary.md)
> โครงสร้างหัวข้อตรงกัน 1:1 เทียบอ่านคู่กันได้ · **quote จากเปเปอร์คงภาษาอังกฤษไว้ทั้งหมด** เพราะต้องใช้อ้างจริง
> (มีคำแปลไทยกำกับในวงเล็บเมื่อจำเป็น) · ไฟล์ที่ระบบใช้เช็คว่า "อ่านแล้ว" คือไฟล์อังกฤษ ไม่ใช่ไฟล์นี้

> **⚠️ ข้อควรระวังเรื่องเวอร์ชัน:** PDF ในเครื่องเป็น **author manuscript / preprint** ไม่ใช่ฉบับเรียงพิมพ์ของ CVIU
> หลักฐาน: หน้าปกมีที่อยู่ไปรษณีย์ เบอร์โทร แฟกซ์ อีเมล · ไม่มี header วารสาร ไม่มี DOI ไม่มีบรรทัดลิขสิทธิ์
> ไม่มีวันที่ received/accepted · เลขหน้าภายในไล่ 1→33 · references อยู่หน้า 20–22, หน้า "List of figures"
> อยู่หน้า 23, แผ่นรูปอยู่หน้า 24–33 · และมี typo ที่ copy-editor ต้องจับได้หลงเหลืออยู่ ("occurances",
> "enchanced", "silhoutte", "Qualisis", "perfoming", "permformance")
> `paper_index_A.csv` ระบุแหล่งว่าเป็น `cs.man.ac.uk/~agalata/publications/cviu_paper.pdf` (โฮสต์โดยผู้เขียนเอง) ซึ่งสอดคล้องกัน
> **ผลที่ตามมา:** ถ้าจะอ้างระดับเลขหน้า **ต้องใช้เลขหน้า 398–413 ของฉบับตีพิมพ์** ไม่ใช่เลขในไฟล์นี้
> ส่วนเลข section/equation ที่ใช้ตลอดเอกสารนี้ **ยังไม่ได้เทียบกับฉบับตีพิมพ์** — ยืนยันก่อนอ้างเลขสมการเฉพาะเจาะจง
>
> **⚠️ ข้อควรระวังเรื่องสัญลักษณ์:** text layer ของ PDF นี้ **ตกอักษรกรีกทั้งหมด** (tuple ของ PFSA ออกมาเป็น "M = (Q )")
> ดังนั้นชื่อสัญลักษณ์ที่ใช้ด้านล่างเป็น **ตัวแทนที่เอกสารนี้ตั้งเอง** เพื่อเลี่ยงการชนกัน — ต้องเทียบฉบับเรียงพิมพ์ก่อนอ้าง notation

---

## Five Cs (pass 1)

- **Category** — research prototype + การประเมินเชิงทดลอง เสนอสถาปัตยกรรมโมเดล 2 แบบ แล้ววัดผลบน dataset
  ที่เก็บเอง 2 ชุด · ไม่ใช่ survey ไม่ใช่การวิเคราะห์ระบบที่มีอยู่
- **Context** — วางตัวเองไว้ตรงข้ามกับการโมเดล activity ด้วย HMM: Bobick & Ivanov [4] ที่ใช้ stochastic
  context-free grammar **เขียนมือ** ครอบ HMM primitives · Bregler [5] ที่ย่อยสลาย human dynamics เชิงความน่าจะเป็น ·
  Pentland & Liu [14] และ Rittscher & Blake [17] ที่ผูก dynamic models เข้าด้วย Markov chain
  ส่วนกลไก VLMM นำเข้ามาจากสาย text compression [7, 2] และ language/handwriting modelling —
  "The Power of Amnesia" ของ Ron, Singer & Tishby [18] และ Guyon & Pereira [9]
  ส่วน vector quantisation ด้านหน้าเป็นงานเก่าของผู้เขียนเอง Johnson & Hogg [13]
- **Correctness** — สมมติฐานสมเหตุสมผลและส่วนใหญ่ระบุไว้ชัด **จุดอ่อนไม่ได้อยู่ที่โมเดล แต่อยู่ที่การวัดผล**:
  รายงานผลเป็น **รูปอย่างเดียว** ไม่มีตาราง ไม่มีตัวเลขในเนื้อความ และไม่มีการทดสอบนัยสำคัญทางสถิติ (ดู §5)
- **Contributions** — (1) VLMM บน VQ pose prototypes เป็นโมเดลพฤติกรรม · (2) การตัดแบ่งเวลาอัตโนมัติเป็น
  "atomic behaviours" ด้วย velocity minima + **VLMM ชั้นที่สองที่วิ่งบน atom เหล่านั้น** = ลำดับชั้น 2 ระดับเวลา
  ที่เรียนรู้ได้เองโดยไม่ต้องมีความรู้ล่วงหน้า · (3) โพรโทคอลวัด prediction error ระยะไกลแบบ Monte-Carlo ·
  (4) เดโมทั้งด้าน synthesis (หุ่น VRML) และ prediction
- **Clarity** — โดยรวมชัดและกระชับ แต่ notation ใน §4.4 หนาแน่น · การนับมิติใน §2.1 ไม่สอดคล้องกัน ·
  และเปเปอร์ **ขัดแย้งกันเองเรื่อง alphabet ของชั้นที่ 2** (§4.2 เทียบ §4.5) — รายละเอียดทั้งหมดอยู่ใน §5

## ตารางสกัดของ อ.Proadpran

| ช่อง | สรุป |
|---|---|
| **Motivation** | HMM "do not encode high order temporal dependencies easily" · การ optimise แบบวนซ้ำติด local optima เมื่อมี free parameter เยอะ ทำให้ topology และขนาดโมเดล "often highly constrained prior to training" · และ Bobick & Ivanov [4] ต้อง **เขียนมือ** โครงสร้างระดับสูงเป็น stochastic context-free grammar |
| **Research question** | โครงสร้างเชิงสถิติระดับสูงของกิจกรรมที่มีความหมายซับซ้อน จะ **เรียนรู้ได้เองอัตโนมัติโดยไม่ต้องมีความรู้ล่วงหน้า** ไหม — และอยู่ในรูปที่รองรับทั้ง recognition และ generation? |
| **Proposed method** | augmented configuration space (ท่า + อนุพันธ์) → robust VQ เป็น prototypes → สตริงของ prototype → VLMM · แล้วต่อยอดเป็นลำดับชั้น: key prototypes ที่ velocity ต่ำสุด → atomic behaviours (template ที่ cluster ด้วย DTW) → VLMM ตัวที่สองบน atom เหล่านั้น |
| **Evaluation** | mean prediction error `E_T` เทียบกับ horizon `T` ถ่วงน้ำหนักด้วย Monte-Carlo sampling (50 การทำนายต่อเฟรม) + ตรวจสายตาจากลำดับที่สังเคราะห์ได้และแอนิเมชัน VRML |
| **Contribution** | โมเดลพฤติกรรม 2 ระดับเวลาที่เรียนรู้ได้เองและสร้างท่าใหม่ได้ · ชุด baseline (first-order Markov → VLMM → hierarchical VLMM) · และสูตร interpolation (Eq. 8) ที่กู้จังหวะเวลาคืนหลังจาก dedup prototype |

---

## 1. ปัญหาและแรงจูงใจ

เปเปอร์มองกิจกรรมเป็น "a sequence of primitive movements with a high-level structure controlling the
temporal ordering" (ลำดับของการเคลื่อนไหวพื้นฐาน โดยมีโครงสร้างระดับสูงคุมลำดับเวลา)

Bobick & Ivanov [4] ทำเรื่องนี้ได้ด้วย stochastic context-free grammar ที่ **เขียนมือ** ครอบ HMM primitives
ส่วนงานอื่นเรื่องกิจกรรมที่มีโครงสร้าง [6, 20, 21] ใช้ phase-space constraints หรือ HMM โดยไม่มี grammar ระดับสูงชัดเจน
ผู้เขียนแย้งว่า HMM เข้ารหัส temporal dependency อันดับสูงได้ไม่ง่าย และการติด local optima เมื่อมีพารามิเตอร์เยอะ
ทำให้ topology กับขนาด "often highly constrained prior to training" (มักถูกบีบไว้ก่อนเทรน)
เป้าหมายจึงเป็น **การได้มาซึ่งโครงสร้างระดับสูงโดยอัตโนมัติ** สำหรับพฤติกรรมอย่าง dance, aerobics และ sign language

เปเปอร์ผูกตัวเองกับ **สเกลเวลา 2 ระดับที่ระบุตัวเลขไว้ชัด** ตั้งแต่ต้น: ระดับ prototype ครอบคลุมการเคลื่อนไหว
"typically spanning of the order of **20ms**" ส่วน atomic behaviours แทน primitive action ที่
"typically lasting of the order of **a second**" โดยยกตัวอย่างว่า *การยกแขน* — สองตัวเลขนี้คือสิ่งที่ทำให้คำว่า
"two-timescale" มีความหมายจับต้องได้

## 2. คอนทริบิวชันหลักและวิธีการ

### 2.1 Augmented configuration space และการแปลงเป็นค่าไม่ต่อเนื่อง (§2)

พฤติกรรมคือเส้นทางใน **augmented configuration space** ที่เอา configuration `C_t` มิติ d มาต่อกับอนุพันธ์อันดับหนึ่ง `Ċ_t`:

    F_t = (C_t, λ Ċ_t),   F_t ∈ [0,1]^{2d}

โดย λ ถ่วงน้ำหนักส่วนอนุพันธ์เวลาที่ใช้ระยะทาง Euclidean เป็น dissimilarity measure
การใส่อนุพันธ์เข้าไปมีเหตุผล 2 ข้อ: มัน **"helps resolve ambiguities in configuration space"**
(ช่วยแก้ความกำกวม — ท่าเดียวกันที่ผ่านคนละทิศทางไม่ใช่สถานะเดียวกัน) และมัน "facilitates the use of models
in performing generative tasks"

แต่ละ `F_t` ถูกแทนด้วย prototype ที่ใกล้ที่สุดจากเซตจำกัด `P = {p_0 … p_n}` ที่เรียนด้วย robust vector
quantisation ของ Johnson & Hogg [13] · จุดสำคัญ:
**"Multiple occurances [sic] of the same prototype are replaced by a single occurance [sic]."**
(prototype ซ้ำติดกันถูกยุบเหลือตัวเดียว)
สตริง prototype จึงเก็บ *ลำดับ แต่ไม่เก็บระยะเวลา* — การตัดสินใจนี้เปเปอร์ต้องกลับมาซ่อมเองทีหลังด้วย Eq. 8

### 2.2 Variable length Markov models (§3.1)

VLMM ให้ความยาว memory แปรตาม context แทนที่จะตรึงไว้ที่อันดับ n · สำหรับสตริง memory `w` และส่วนขยาย `aw`
ใช้ weighted Kullback–Leibler divergence วัดข้อมูลที่ได้เพิ่มจากการยืด memory:

    H(aw, w) = P̂(aw) Σ_{a'} P̂(a'|aw) · log [ P̂(a'|aw) / P̂(a'|w) ]        (Eq. 5)

ถ้า `H(aw, w)` เกินเกณฑ์ ε → ใช้ memory ยาว `aw` · ถ้าไม่เกิน → ถือว่า `w` พอแล้ว
(หมายเหตุ: เปเปอร์เรียกสิ่งเดียวกันไม่ตรงกันเอง — §1 เรียก "a cross-entropy measure" ส่วน §3.1 เรียก
"a weighted Kullback-Leibler divergence [18]")
ความน่าจะเป็นของ transition และ prior มาจากความถี่สัมพัทธ์ในคลัง training (Eq. 6–7 โดย `v(·)` นับจำนวนครั้ง
ที่สตริง token ปรากฏ และ `v₀` คือ "the total length of the training sequences")

การเทรนสร้าง **prefix tree** [9] ของสตริงยาวไม่เกิน N โดยนับ transition จากการเลื่อนหน้าต่างขนาด N ไปตามลำดับ token
จากนั้น prune ให้เป็น **prediction suffix tree** [18] — สร้าง node ใน suffix tree ก็ต่อเมื่อ KL divergence
ระหว่างการแจกแจงที่ prefix node กับที่ node บรรพบุรุษเกิน ε — แล้วแปลงเป็น automaton

ผลลัพธ์เทียบเท่า **Probabilistic Finite State Automaton** `M = (Q, Σ, δ, γ, π)`:
Σ = alphabet ของ token · Q = เซตสถานะจำกัด แต่ละสถานะคือสตริง token ยาวไม่เกิน N (คือ memory) ·
`δ: Q × Σ → Q` = transition function · `γ: Q × Σ → [0,1]` = output probability function ที่ให้ความน่าจะเป็น
ของ token ถัดไปโดยมีเงื่อนไขเป็น memory · `π: Q → [0,1]` = การแจกแจงสถานะเริ่มต้น
เปเปอร์ระบุการ normalise ไว้ชัด: ทุก `q ∈ Q` ต้อง `Σ_a γ(q,a) = 1` และ `Σ_q π(q) = 1`

จุดขายคือ **"ability to locally optimise the length of memory required for prediction"** —
memory ยาวตรงที่พฤติกรรมต้องการ memory สั้นตรงที่ไม่ต้องการ

### 2.3 ชั้นที่ 1 — VLMM บน prototypes (§3.2)

แปลงลำดับ training เป็นสตริง prototype ด้วย nearest neighbour ทุกจังหวะเวลา โดย
"only transitions between different prototypes are considered for training" · แล้วเอาไปเทรน PFSA `M_p`

- **การสร้างท่า (§3.2.1):** เดินไปบน PFSA โดยเลือก transition ที่น่าจะเป็นที่สุด (maximum likelihood generation)
  หรือสุ่มจากการแจกแจง transition (stochastic generation) แล้วปล่อย prototype vector ออกมา
- **การกู้จังหวะเวลาคืน (Eq. 8):** เพราะ prototype ซ้ำถูกลบไป ช่วงเวลาระหว่าง prototype จึง
  "initially unspecified (due to the removal of repeated prototypes)" · โดยสมมติ **ความเร่งคงที่** ประมาณได้ว่า

      Δ_r = 2 |C_{r+1} − C_r| / ( |Ċ_r| + |Ċ_{r+1}| )                     (Eq. 8)

  ซึ่งก็คือ **ระยะทางหารด้วยอัตราเร็วเฉลี่ย** พอดี: ภายใต้ความเร่งคงที่ อัตราเร็วเฉลี่ย = `(|Ċ_r| + |Ċ_{r+1}|)/2`
  จากนั้นใช้ **cubic Hermite interpolant** ที่นิยามด้วยจุดปลาย `C_r, C_{r+1}` และเวกเตอร์สัมผัส `Ċ_r, Ċ_{r+1}`
  (สเกลด้วย Δ_r) แล้วสุ่มตัวอย่างที่ data frame rate เพื่อให้ได้ลำดับที่สม่ำเสมอทางเวลา
  → **นี่คือเหตุผลที่อนุพันธ์ต้องอยู่ใน feature vector**: ถ้าไม่มี `Ċ` ก็ไม่มีเวกเตอร์สัมผัสและไม่มีทางประมาณระยะเวลา
- **การทำนาย (§3.2.2):** เพราะสถานะเก็บประวัติไว้ จึงต้องรันโมเดลใน *recognition mode* ก่อน — ป้อน prototype
  ที่สังเกตได้เข้าไปแล้วเดิน transition ตาม เพื่อหาว่าตอนนี้อยู่สถานะไหน — แล้วค่อยสลับไปโหมด generation
  (ความหมายแคบ ๆ ของคำว่า "recognition" ตรงนี้ **คนละเรื่องกับ** การจำแนกประเภทพฤติกรรม ซึ่งเปเปอร์เคลมว่าทำได้
  แต่ไม่เคยวัดเลย — ดู §5)
- **เหตุการณ์ที่ไม่เคยเห็น (unseen events):** ถ้า `M_p` เจอ prototype ที่สถานะปัจจุบันให้ความน่าจะเป็นศูนย์ โมเดลจะ
  "return[s] to the initial model state, lose[s] all the previous memory and predict[s] p_i with the prior P̂(p_i)"
  (กลับไปสถานะเริ่มต้น ทิ้ง memory ทั้งหมด แล้วทำนายด้วย prior)
  ผู้เขียนเรียกวิธี back-off นี้ว่า "simple but effective" และชี้ไปที่ Jelinek [11] สำหรับวิธีที่ซับซ้อนกว่า

### 2.4 ชั้นที่ 2 — structured / hierarchical model (§4)

เหตุผล: การเคลื่อนไหวของมนุษย์ "has different characteristics at different time scales, usually carrying
syntactic and semantic information at larger temporal scales" ซึ่ง VLMM ระดับ prototype ตัวเดียวครอบไม่ไหว

- **Key prototypes (§4.1):** ด้วยข้อจำกัดทางกายภาพของร่างกาย "any change in the type of human movement usually
  causes dips in velocity" (การเปลี่ยนชนิดการเคลื่อนไหวมักทำให้ความเร็วตก)
  prototype ที่ขนาดอนุพันธ์อันดับหนึ่ง `|Ċ_t|` เป็น **"local minimum and below a fixed threshold (chosen by
  inspection)"** จะถูกจัดเป็น key set `K ⊆ P`
  (สังเกต: เกณฑ์นี้ใช้กับ `Ċ_t` **ที่ยังไม่สเกล** ไม่ใช่ `λĊ_t`)
  ผู้เขียนยอมรับเองว่าในอุดมคติจุดตัดแบ่ง "might be derived from a global maximisation of likelihood over the
  training data" และระบุเป็นงานวิจัยต่อไป
- **Atomic behaviours:** คู่อันดับของ key prototype `(k_i, k_j), i ≠ j` แต่ละคู่นิยาม atomic behaviour `α_ij`
  ที่ครอบพฤติกรรมระหว่างสองจุดนั้น · แต่ละ `α_ij` ประกอบด้วย **template sequences** `T^l_ij` จำนวน m ชุด
  แต่ละชุดเป็นเซตอันดับของ prototype (Eq. 11) โดย m และความยาว template ต่างกันไปในแต่ละ component
  การสร้าง template: เก็บ sub-sequence ทั้งหมดในคลังที่พาดจาก `k_i → k_j` แล้วแบ่งเป็น
  "clusters of self-similar sequences using dynamic time warping [19]" จากนั้นสร้าง template 1 ชุดต่อ cluster
  ด้วย "re-sampling, averaging, and re-quantisation" · prior ของ template `P(T^l_ij)` (รวมกันได้ 1 ใน component)
  มาจากความถี่สัมพัทธ์ที่ template ถูก match ในคลัง
- **Grammar ระดับสูง (§4.2):** เทรน VLMM ตัวที่สอง `M_k` โดย **ใช้ key prototypes เป็น alphabet**
  เพราะ `α_ij` *คือ* transition `k_i → k_j` อยู่แล้ว จึงได้ `P_{M_k}(α_ij | s k_i) = P_{M_k}(k_j | s k_i)` —
  แปลว่า transition ระหว่าง atomic behaviour ถูกฝังอยู่โดยปริยายในโมเดลที่ token เป็น key prototype
  ความน่าจะเป็นระดับ template คือ

      P_{M_k}(T^l_ij | s k_i) = P(T^l_ij) · P_{M_k}(α_ij | s k_i)          (Eq. 12)

  ⚠️ **§4.5 พูดขัดกับตรงนี้** โดยบรรยายโมเดลชุดเดียวกันว่า "using **atomic behaviours** as an alphabet"
  → เอกสารนี้ยึดตาม §4.2 (key prototypes เป็น alphabet, atomic behaviours อยู่โดยปริยาย) เพราะเป็นฉบับที่มีการอนุมานประกอบ
- **การสร้างท่า (§4.3):** เดินบน `M_k` ปล่อย key prototype ทีละตัว แล้วแทน subsequence `k_i k_j` ด้วย
  `k_i T^l_ij k_j` โดยเลือก template จากการ maximise Eq. 12 หรือสุ่ม · ลำดับที่สมมติขึ้นล้วน ๆ เริ่มจากการแจกแจง
  สถานะเริ่มต้น ซึ่งประมาณจากความถี่สัมพัทธ์ของสถานะเริ่มต้นในคลัง training
  **Fig. 6** แสดงท่าที่สังเคราะห์ได้ (dataset 2, N = 4) ขยับ "a virtual humanoid using the VRML modelling
  language" — ส่วน Acknowledgments ระบุว่าเป็นหุ่น "Baxter" มาตรฐาน H-Anim 1.1 VRML
- **การทำนาย (§4.4):** ยากกว่าชั้นที่ 1 เพราะต้องรู้ด้วยว่า *กำลังเดินอยู่บน template ไหน* และ *อยู่ตำแหน่งใดใน template นั้น*
  ใช้สูตรแบบ Bayesian โดยเอาความน่าจะเป็น transition ที่เรียนมาเป็น prior:

      P(T^l_ij | O_t, s k_i) ∝ P(O_t | T^l_ij) · P_{M_k}(T^l_ij | s k_i)   (Eq. 13)

  พิจารณา template ทุกตัวจาก key prototype ล่าสุด `k_i` ไปยัง `k_q` ใด ๆ · แต่ละตัวใช้ DTW หาตำแหน่งที่ต้นทุน
  การจัดเรียงต่ำสุด ได้ต้นทุน `c_t(i,q,r)` · แล้ว *ประมาณ* likelihood ด้วยต้นทุนสัมพัทธ์

      P(O_t | T^l_ij) = 1 − c_t(i,j,l) / Σ_{q,r} c_t(i,q,r)                (Eq. 14)

  การ maximise Eq. 13 จะระบุ key prototype ตัวถัดไป และจึงระบุสถานะถัดไปของ VLMM · พฤติกรรมอนาคตที่สร้างออกมา
  = ส่วนที่เหลือของ template ปัจจุบัน + การเดินต่อจากสถานะใหม่
  **unseen events** ตรวจจับเมื่อความน่าจะเป็นสูงสุดต่ำกว่าเกณฑ์ → ทิ้งประวัติระดับสูง แล้วทำนาย key prototype
  ถัดไปจาก Eq. 14 อย่างเดียว
  **Fig. 7** แสดงผลเชิงคุณภาพ: การ extrapolate แบบ maximum-likelihood ณ จังหวะเวลาที่เลือกมา โดยวาดพฤติกรรม
  ล่าสุดเป็น contour ทึบไล่เฉดตามความใหม่ (สว่างสุด = ปัจจุบัน) และแสดง "the first 12 frames of each extrapolation"

## 3. โพรโทคอลการวัดผล

mean prediction error ที่ horizon T วัดใน configuration space ตาม §3.2.3 (ไม่ใช่ token space):

    E_T = ( Σ_{j=1..n} | C^j_{t+T} − C_{t+T} | ) / n                        (Eq. 9)

โดย n = "the total number of trials carried out over all test sequences" และ `C_{t+T}` คือ ground truth
error เฉลี่ยจากการทำนาย "on every frame of every test sequence" และ
"updated only if both a prediction and the ground truth exist for the particular T"

> ⚠️ **ต้นฉบับกำกวมเรื่องปริภูมิ:** §3.2.3 เขียนว่า "in configuration space" แต่คำบรรยายใต้รูป Fig. 4 และ Fig. 10
> เขียนว่า "in the **augmented** configuration space" · เนื่องจากค่าที่พล็อตมาจากรูปเหล่านั้น **หน่วยของแกน y
> จึงไม่ได้ถูกตรึงไว้ด้วยเนื้อความ**

เพราะวงรอบ (cycle) ในโครงสร้าง transition ทำให้แจกแจงความเป็นไปได้ทั้งหมดจากสถานะหนึ่งไม่ได้ จึงถ่วงน้ำหนัก
ความน่าจะเป็นด้วย **Monte-Carlo simulation** — **"50 stochastic predictions were generated on each frame"**
โดยใช้ความถี่สัมพัทธ์ของผลเป็นตัวถ่วงน้ำหนัก · error bar ในรูปคือ **mean error ± mean absolute deviation**

## 4. ข้อมูลและผลลัพธ์

### Dataset 1 — 2-D contour tracking (§2.1.1)
คน 1 คนทำท่าออกกำลังกาย ติดตามด้วย contour tracker แบบง่าย [12, 1] · **40 วินาที ที่ 25 fps**
configuration = จุดควบคุม n จุดของ closed uniform B-spline ที่ประมาณขอบเงา (silhouette) กระจายห่างเท่ากัน
และเรียงเทียบจุดอ้างอิงที่คงที่ (ปรับปรุงจาก [1] ให้หาจุดสูงสุดของศีรษะแม่นขึ้น) แปลงเข้าสู่กรอบพิกัดที่ยึดวัตถุเป็นศูนย์กลาง
และ normalise เป็น [0,1] · ด้วย **จุดควบคุม 32 จุด** เปเปอร์รายงาน **augmented configuration space 128 มิติ (2 × 2 × 32)**
· scaling factor **λ = 10** → **71 prototypes**
โครงสร้างท่า (Fig. 1b): ท่าออกกำลังกาย 2 ท่า แต่ละท่าทำซ้ำ 4 รอบ และแต่ละท่าตามด้วยท่าย่อยอีก 4 รอบ
(ป้ายกำกับ Exercise 1, 1a, 2, 2a)

- VLMM บน prototypes, **ε = 0.0001**: **N = 5 → 117 states** · **N = 20 → 290 states**
- ลำดับทดสอบ: ท่าและท่าย่อยชุดเดียวกัน แต่ทำซ้ำท่าละ **3** รอบ
- พล็อตการทำนายช่วง **1 ≤ T ≤ 70** ("≈3 sec.") · แกน mean error 0–1.8 (Fig. 4a, 10a)
- โมเดลลำดับชั้น: **key prototypes 5 ตัว, atomic behaviours 8 ตัว** · VLMM ที่ N = 4, 6, 8 (ε = 0.0001)
  → **22, 34, 45 states** · รายงานผลการทำนายที่ N = 6

### Dataset 2 — 3-D motion capture (§2.1.2)
ระบบเชิงพาณิชย์ (กล้อง ProReflex, ซอฟต์แวร์ MacReflex, "Qualisis 97" [sic — ที่ถูกคือ Qualisys]) ·
**ตำแหน่ง 3 มิติของ marker 13 จุดบนร่างกาย ที่ 50 fps** · **8 ลำดับ ลำดับละ ≈25 วินาที** จากคน 1 คน
แปลงจุดเข้าสู่พิกัดที่ยึดวัตถุเป็นศูนย์กลางและ normalise เป็น [0,1] · scaling factor **λ = 30** → **87 prototypes**
โครงสร้างท่า (Fig. 2): ท่าออกกำลังกาย 3 ท่า โดยท่าแรกทำซ้ำ 2 รอบ · มีท่าย่อยปรากฏใน 2 ท่าหลัง ทำซ้ำ 2 รอบในแต่ละท่า

- VLMM บน prototypes, ε = 0.0001: **N = 5 → 112 states** · **N = 20 → 226 states**
- ลำดับทดสอบ 2 ชุด ชุดละ ≈25 วินาที · พล็อตถึง **T ≈ 140** ("up to about 3 seconds") · แกน error 0–0.9
- โมเดลลำดับชั้น: **key prototypes 5 ตัว, atomic behaviours 8 ตัว** · VLMM ที่ N = 2 และ N = 4
  → **9 และ 12 states** · รายงานผลการทำนายที่ N = 4

### ผลที่ได้
1. **VLMM ชนะ first-order Markov ขาด** — "As can be seen from the prediction graphs … substantially better
   results are obtained using VLMMs in comparison to a first order Markov model" (ทั้งสอง dataset)
2. **โมเดลลำดับชั้นชนะ VLMM แบบแบน** — "the structured behaviour models consistently give better prediction
   results, demonstrating the increased ability of the model to encode the complex, long-term temporal
   dependencies."
3. **โครงสร้างมองเห็นได้จากการสังเคราะห์ (Fig. 9, dataset 1)** — ที่ **N = 1 ซึ่งเปเปอร์ระบุเองว่า
   "equivalent to a first order Markov model"** → "the model does not capture longer-term temporal constraints
   between atomic behaviours as can be seen by the random order in which the separate exercises and
   sub-exercises are generated" (ลำดับท่าออกมามั่ว) · ส่วนที่ N = 4 และ N = 8 มี "correct progression from one
   exercise or sub-exercise to the next"
   รูปนี้แสดงเฟรมเว้นเฟรมของ **700 เฟรมแรก** (≈28 วินาทีที่ 25 fps) ซึ่งเป็นเหตุผลที่มองเห็นการสลับลำดับได้ชัด
   → **นี่คือผลเชิงคุณภาพที่คมที่สุดของเปเปอร์: first-order สลับลำดับท่าในรูทีน**
4. **ความยาว memory แปรผันจริง** (Fig. 3, 8) — ฮิสโทแกรมความยาว memory ต่อสถานะคือหลักฐานตรง ๆ ว่าเกณฑ์ KL
   จ่าย memory ยาวเฉพาะตรงที่จำเป็น

> ⚠️ **ผลเชิงปริมาณทั้งหมดของเปเปอร์นี้อยู่ในรูปภาพ** ไม่มีตาราง ไม่มีค่า error ตัวเลขในเนื้อความเลย
> เครื่องมือที่มีในรอบนี้ (`pdftotext` เท่านั้น ไม่มี `pdftoppm`/PyMuPDF ที่จะ render หน้าเป็นภาพ) กู้ได้แค่
> แกน ช่วงสเกล และ legend ของซีรีส์ **แต่กู้ค่าบนเส้นกราฟไม่ได้** จึง **ไม่มีการอ้างค่า `E_T` เจาะจงในเอกสารนี้**
> *ลำดับ* ของเส้นเป็นสิ่งที่ผู้เขียนยืนยันไว้ในเนื้อความและคัดมาตรง ๆ ข้างบนแล้ว แต่ *ขนาด* ของค่ายังไม่ได้ตรวจสอบจากไฟล์นี้
> ทั้งนี้ Fig. 4 และ Fig. 10 ต่างมีซีรีส์ `FIRST ORDER MARKOV MODEL` อยู่จริง ยืนยันว่ามีการพล็อตเปรียบเทียบจริง

## 5. สมมติฐานและข้อจำกัด

**ที่ผู้เขียนระบุหรือยอมรับเอง**
- เกณฑ์ velocity สำหรับ key prototype "chosen by inspection" (เลือกด้วยสายตา) · การตัดแบ่งแบบ global likelihood
  ถูกยกไปเป็นงานวิจัยต่อไปอย่างชัดเจน
- วิธี back-off เมื่อเจอ unseen event เป็นแค่ "simple but effective" โดยไม่ได้ลองวิธีที่ดีกว่า [11]
- Eq. 8 สมมติ **ความเร่งคงที่** ระหว่าง prototype อย่างชัดเจน
- Eq. 14 นำเสนอในฐานะ *การประมาณ* likelihood ด้วย "relative probability" — เปเปอร์ไม่ได้เคลมว่าเป็นความน่าจะเป็นที่ normalise แล้ว
- การขยายเกิน 2 ชั้นเป็นแค่การคาดการณ์ ("could be envisaged")

**ที่ไม่ได้ระบุ / พบจากการอ่านละเอียด**
- **ไม่มีการทดสอบนัยสำคัญทางสถิติเลย** · ค่ากระจายเดียวที่รายงานคือ "mean error ± mean absolute deviation"
  ในคำบรรยาย Fig. 4 และ 10 — ไม่มี confidence interval ไม่มี test ไม่มี seed ไม่มีความแปรปรวนจากการรันซ้ำ
- **ข้อมูลน้อยมากและเป็นคนเดียว** · dataset 1 คือ "a 40 second sequence of **an individual**" ·
  dataset 2 คือ "eight sequences … of **an individual**" (≈200 วินาที)
  (หัวข้อทั้งสองเปิดด้วยพหูพจน์กว้าง ๆ ว่า "individuals performing exercise routines" แต่ข้อมูลเทรนระบุชัดว่าเป็นคนเดียวทั้งคู่)
  → **ไม่มีอะไรในเปเปอร์นี้แสดงการ generalise ข้ามบุคคล**
- **ข้อมูลทดสอบมาจากรูทีนเดียวกับ training** · dataset 1 ต่างแค่จำนวนรอบ (3 เทียบ 4) ·
  dataset 2 เปเปอร์ระบุว่าลำดับทดสอบประกอบด้วย "the same three exercises and sub-exercises as those in the
  training data" โดย **ไม่ได้ระบุความต่างใด ๆ เลย** → ไม่เคยทดสอบกับโครงสร้างกิจกรรมที่ไม่เคยเห็น
- **ขนาด vocabulary เป็นตัวแปรที่ไม่ได้รายงาน** · 71 และ 87 เป็น *ผลลัพธ์* ของ robust VQ ตาม [13]
  ไม่ใช่ค่าที่เลือกเอง · พารามิเตอร์ของ VQ เองไม่เคยระบุ และไม่มีการวิเคราะห์ความไวต่อจำนวน prototype
- **λ ไม่เคยถูก tune หรือ ablate** (10 สำหรับ contour 2 มิติ, 30 สำหรับ mocap 3 มิติ ทั้งคู่ไม่มีเหตุผลกำกับ) ·
  λ ส่งผลต่อการตัดแบ่งแบบ *ทางอ้อม* เท่านั้น — โดยเปลี่ยนว่ามี prototype อะไรบ้าง จึงเปลี่ยนเซตที่ key prototype
  ถูกเลือกออกมา — เพราะเกณฑ์ใน §4.1 ใช้กับ `|Ċ_t|` ที่ยังไม่สเกล
- **การ dedup คือการสูญเสียข้อมูลจริง** และซ่อมได้แค่บางส่วน: Eq. 8 *สร้าง* จังหวะเวลาขึ้นใหม่ภายใต้สมมติฐาน
  ความเร่งคงที่ แทนที่จะ *รักษา* dwell time ที่วัดได้จริง → การค้างท่านาน ๆ กับการหยุดแวบเดียวที่ท่าเดียวกัน
  **แยกไม่ออกในสตริง token**
- **Eq. 14 ไม่ใช่ความน่าจะเป็นที่ normalise แล้ว** · เมื่อรวมข้าม template ที่แข่งกัน M ตัว ค่า `1 − c/Σc`
  จะได้ M − 1 จึง normalise ก็ต่อเมื่อ M = 2 · สเกลของมันขึ้นกับว่ามี template แข่งกันกี่ตัว
  แต่เปเปอร์เองก็กันตัวไว้แล้ว ("approximate", "relative probability" และ Eq. 13 เป็นสัดส่วน)
  → ถือเป็นจุดอ่อนเชิงการนำเสนอ ไม่ใช่ความผิดพลาด
- **การนับมิติไม่สอดคล้องกัน** · §2.1.1 ใช้ d เป็นมิติของ *configuration* (d = 2n = 64 · augmented = 128 = 2×2×32)
  แต่ §2.1.2 ใช้ d เป็นมิติของ *augmented* · แย่กว่านั้น §2.1.2 เขียนว่า **"d = 72 (2 × 3 × 13)"**
  ทั้งที่ 2 × 3 × 13 = **78** · เป็นข้อผิดพลาด 2 ชั้นในประโยคเดียว เพราะ §2 นิยาม `F_t ∈ [0,1]^{2d}` ดังนั้น
  ถ้ามี marker 13 จุด d ควรเป็น 39 และ augmented space ควรเป็น 78 · เนื่องจาก "13 points" ระบุไว้ถึง 2 ที่
  **78 จึงน่าจะเป็นค่าที่ตั้งใจ** → อ้างตัวเลขนี้ด้วยความระมัดระวัง
- **alphabet ของชั้นที่ 2 ถูกระบุไว้ 2 แบบ** — key prototypes (§4.2 พร้อมการอนุมาน) เทียบกับ atomic behaviours (§4.5)
  ซึ่งสมานกันได้ในเชิงเนื้อหา แต่ตัวบทขัดกันเอง
- **วัดผลเฉพาะการทำนาย** · behaviour recognition ถูกเคลมเป็นความสามารถทั้งใน §3 ("able to support both
  recognition and generative capabilities") และใน Conclusions ("can be utilised for behaviour recognition")
  แต่การทดลองทุกชิ้น (§3.2.4, §4.5) เป็น prediction หรือ synthesis · คุณภาพการสังเคราะห์ตัดสินด้วยสายตาล้วน ๆ
- **ไม่มีต้นทุนเวลา ไม่มีโค้ด ไม่มีการปล่อยข้อมูล** — ถือเป็นข้อสังเกตเรื่อง artefact availability ตามมาตรฐานสมัยใหม่
  มากกว่าจะเป็นข้อบกพร่องเชิงวิธีวิทยาของเปเปอร์ปี 2001

## 6. ความสัมพันธ์กับงานข้างเคียงที่เปเปอร์อ้าง

- **เทียบ Bobick & Ivanov [4]** — เขา parse กิจกรรมด้วย stochastic context-free grammar ที่ *เขียนมือ*
  ครอบ HMM ที่โมเดล primitive ระดับล่าง · ข้อเคลมแกนกลางของเปเปอร์นี้คือ grammar ระดับสูงแบบเดียวกันนั้น
  **เรียนรู้จากข้อมูลได้** → นี่คือการวางตำแหน่งที่คมที่สุดของเปเปอร์
- **เทียบ Bregler [5], Pentland & Liu [14], Rittscher & Blake [17]** — ทุกงานย่อย human dynamics เป็นเฟสหรือ
  dynamic model ที่ผูกกันด้วย Markov chain ที่แทนข้อจำกัดความต่อเนื่องระยะยาว · chain นั้นเป็นอันดับคงที่
  ซึ่งคือเป้าหมายของ VLMM พอดี
- **เทียบ HMM [16]** — ข้อคัดค้านที่ระบุไว้: เข้ารหัส temporal dependency อันดับสูงได้ไม่ง่าย และ local optima
  เมื่อมีพารามิเตอร์เยอะทำให้ topology กับขนาด "often highly constrained prior to training"
- **สืบทอดจาก Ron, Singer & Tishby [18]** — prediction suffix tree และเกณฑ์ KL-pruning ยกมาทั้งดุ้นจาก
  "The Power of Amnesia" · สายเดียวกันนี้รวม Guyon & Pereira [9] (อ้างสำหรับ prefix tree ด้วย),
  Hu et al. [10] (language modelling) และสาย text compression [7, 2]
- **สืบทอดจาก Johnson & Hogg [13]** และ Baumberg & Hogg [1] — robust VQ ด้านหน้าและ flexible contour model
  เป็นเครื่องมือเดิมของผู้เขียนเอง → เปเปอร์นี้พูดตรง ๆ ได้ว่าเป็น *การประกอบร่าง*: เอา VQ pipeline ที่มีอยู่
  มาต่อกับเครื่องมือ language modelling ที่มีอยู่ แล้วประยุกต์กับพฤติกรรม โดยมี **ลำดับชั้น (§4) เป็นส่วนที่ใหม่จริง**
- **DTW [19] (Sakoe & Chiba)** ทำงาน 2 หน้าที่ — cluster sub-sequence เป็น template (§4.1) และระบุตำแหน่งภายใน
  template ตอนทำนาย (§4.4)
- **บริบทของพื้นที่ปัญหา** [6, 20, 21]: phase-space constraints (Campbell & Bobick) และการรู้จำ ASL ด้วย HMM
  (Starner & Pentland; Vogler & Metaxas) ถูกอ้างในฐานะวรรณกรรมของ "พฤติกรรมที่มีโครงสร้างและความหมายซับซ้อน"
  แต่ **ไม่ได้ถูกนำมาเปรียบเทียบผล**

---

## 7. การตรวจตาม checklist (`knowledge/reading_checklist.md`)

`reading_checklist.md` เป็น *คิวลำดับการอ่าน* ไม่ใช่แบบสอบถามรายเปเปอร์ การตรวจรอบนี้จึงแบ่งเป็น 4 ส่วน:
(ก) เป้าหมาย "อ่านเอา" ที่ checklist ตั้งไว้สำหรับ **เปเปอร์นี้** (Tier 0 ข้อ 1) · (ข) รายการอื่นที่เปเปอร์นี้พูดถึงจริง ·
(ค) การทดลอง E1–E7 ที่ checklist บอกว่าการอ่านควรจุดชนวน · (ง) รายการที่ไม่เกี่ยวข้อง
*ไฟล์ checklist ถูกอ่านอย่างเดียว ไม่ได้ถูกแก้ไข*

### (ก) Tier 0 ข้อ 1 — เป้าหมายที่ checklist ตั้งไว้สำหรับเปเปอร์นี้

| เป้าหมายใน checklist | ผลตรวจ | เปเปอร์พูดว่าอะไรจริง ๆ |
|---|---|---|
| §3 — VQ + VLMM, เกณฑ์ KL ε | **ครบ** | §2 ให้ VQ ด้านหน้า (robust VQ ตาม [13], ยุบตัวซ้ำ — checklist จัดไว้ใต้ §3 แต่จริง ๆ อยู่ §2) · §3.1 ให้เกณฑ์ weighted KL (Eq. 5) และขั้นตอน prefix-tree → prediction-suffix-tree → PFSA · **ε = 0.0001 ในการทดลองที่รายงานทั้ง 4 ชุด** ครบทั้งสอง dataset และทั้งสองระดับโมเดล |
| §4.1–4.5 — hierarchical: key prototypes → atomic behaviours | **ครบถ้วนสมบูรณ์** | §4.1 key prototypes = จุดต่ำสุดเฉพาะที่ของ velocity ที่ต่ำกว่าเกณฑ์ที่เลือกด้วยมือ · atomic behaviours = คู่อันดับของ key prototype ที่สร้างเป็น template ผ่าน DTW cluster + re-sample/average/re-quantise · §4.2 VLMM ตัวที่สอง (Eq. 12) · §4.3 สร้างท่าโดยขยาย `k_i k_j → k_i T^l_ij k_j` · §4.4 ระบุ template แบบ Bayesian (Eq. 13–14) · §4.5 การทดลอง · **ข้อนี้ปิดช่องที่ `paper_chain.md` ค้างไว้ (R9-5 ข้อ 1 ที่ยกมาเป็น R10-4 ข้อ 5) ซึ่งระบุว่า §4.1–4.5 ยังไม่ได้อ่าน** |
| Eq. 8 — cubic Hermite กู้ระยะเวลาคืนจาก velocity | **ครบ** | ยืนยันแล้ว: `Δ_r = 2|C_{r+1} − C_r| / (|Ċ_r| + |Ċ_{r+1}|)` = ระยะทาง ÷ อัตราเร็วเฉลี่ย ภายใต้ความเร่งคงที่ ป้อนเข้า cubic Hermite interpolant ที่มีจุดปลาย `C_r, C_{r+1}` และเวกเตอร์สัมผัส `Ċ_r, Ċ_{r+1}` สเกลด้วย Δ_r แล้วสุ่มที่ data frame rate · **ข้อควรระวังที่ checklist ไม่ได้คาดไว้:** วิธีนี้ *สร้าง* จังหวะเวลาที่ดูสมเหตุผลขึ้นใหม่ ไม่ได้ *รักษา* dwell time ที่วัดได้ → เป็นการซ่อมผลของ dedup ไม่ใช่ของทดแทนการเก็บ duration |
| mean error `E_T` เทียบ horizon, Monte Carlo 50 ครั้ง/เฟรม | **ครบ** | Eq. 9 นิยาม `E_T` · §3.2.3 ระบุ 50 การทำนายต่อเฟรม พร้อมเหตุผลว่าแจกแจงความต่อเนื่องทั้งหมดไม่ได้เมื่อโครงสร้าง transition มีวงรอบ · error bar = mean absolute deviation · **เอามาใช้เป็น metric ของเราได้ทันที** แต่ให้ระวังความกำกวมระหว่าง §3.2.3 กับคำบรรยาย Fig. 4 & 10 เรื่อง configuration space เทียบ *augmented* configuration space |
| ข้อเคลม: `transition_matrix.npy` ของเราเป็น "ตัวที่อ่อนที่สุดในตระกูล" | **ครบ — และแรงกว่าที่ checklist ระบุ** | first-order แพ้ด้าน prediction error ทั้งสอง dataset *และ* §4.5 ยังเพิ่มความล้มเหลวเชิงคุณภาพอีกทางหนึ่ง: ที่ N = 1 ซึ่ง "equivalent to a first order Markov model" การสังเคราะห์ให้ "the random order in which the separate exercises and sub-exercises are generated" → **first-order พังทั้งเชิงปริมาณ (`E_T`) และเชิงโครงสร้าง (สลับลำดับท่า)** |
| ข้อเคลม: "บรรพบุรุษเชิงโครงสร้างที่ใกล้ที่สุด … VQ prototypes → สตริง → Markov model" | **ยืนยัน** | รูปทรง pipeline ตรงกันเป๊ะ · **⚠️ แต่มี 1 จุดที่ต้องแก้ย้อนกลับ:** `paper_index_A.csv` บรรทัด 60 เขียนว่าเป็น VLMM "on dance" — **ไม่ใช่ dance** · คำว่า "dance" ปรากฏในเอกสารทั้งฉบับแค่ 2 ครั้ง และอยู่ในลิสต์จูงใจเดียวกันทั้งคู่ ("dance, aerobics, and sign language" ใน Abstract และ §1) ส่วนคำว่า "exercise" ปรากฏ 29 ครั้ง และทุก dataset ทุกรูป ทุกคำบรรยาย เป็น **ท่าออกกำลังกาย/แอโรบิก** (contour เงา 2 มิติ; mocap 13 marker 3 มิติ) → **แก้ก่อนที่จะไหลเข้าวิทยานิพนธ์** |

### (ข) รายการอื่นใน checklist ที่เปเปอร์นี้พูดถึง

| # | รายการ | ผลตรวจ | เกี่ยวยังไง |
|---|---|---|---|
| 3 / 13 | DASB bitrate; Scaling Laws with Vocabulary (data เป็นคอขวด → vocab ควรเล็ก) | **ครบบางส่วน** | ให้ข้อมูลเพิ่มอีก 2 จุดในย่านร้อยต้น ๆ — **71** prototypes (วิดีโอ 40 วินาที 25 fps) และ **87** (mocap ~200 วินาที 50 fps) · สอดคล้องกับ "คลังเล็ก → vocab เล็ก" แต่เป็นแค่ *การสนับสนุนด้วยตัวอย่าง* เท่านั้น: ตัวเลขเหล่านี้เป็น output ของ VQ · **ไม่มี vocabulary sweep และไม่มีการวิเคราะห์ความไว** · เปเปอร์ไม่เคยให้เหตุผลกับขนาดเหล่านี้ → **ห้ามอ้างเป็นหลักฐานสนับสนุนค่า V ที่เหมาะสม** |
| 4 | Discrete speech tokens review — dedup ทำลาย duration | **ครบ และเป็นปัญหาเดียวกันเป๊ะ** | §2 ยุบตัวซ้ำ · §3.2.1 ยอมรับว่าช่วงเวลา "initially unspecified (due to the removal of repeated prototypes)" → เป็นการยืนยันปัญหานี้อย่างอิสระตั้งแต่ยุค 2001 พร้อมวิธีบรรเทาที่เป็นรูปธรรม (Eq. 8) |
| 8 | FSQ / codebook collapse | **ไม่ครอบคลุม** | เกิดก่อนประเด็นนี้ · ไม่เคยพูดถึง collapse เลย · สอดคล้องกับคำเตือนใน checklist ว่า collapse เป็นโรคของ codebook *ใหญ่* แต่เปเปอร์นี้ไม่ใช่หลักฐานทั้งฝั่งหนุนและฝั่งค้าน |
| 10 / 19 | Matrix Profile VI ความเสี่ยง limb-subspace; Skeleton Motion Words | **ครบบางส่วน — ในฐานะตัวอย่างเตือนใจ** | configuration space ที่นี่เป็น **ทั้งตัว** (จุดควบคุม spline ทั้ง 32 จุด หรือ marker ทั้ง 13 จุด) ภายใต้ metric Euclidean เดียวทั่วทั้งตัว และ **ไม่มีการแยกตามรยางค์เลย** → เปเปอร์นี้จึง *เป็นตัวอย่างของ* ความเสี่ยงที่ข้อ 10 พูดถึง มากกว่าจะแก้มัน: motif ของแขนที่แอมพลิจูดเล็กจะถูกลำตัวและขากลบ · ใช้เป็นหลักฐานว่า "การเลือกทั้งตัวเป็นธรรมเนียมปกติ" ได้ — **แต่ใช้เป็นข้อแก้ต่างให้ตัวเลือกนั้นไม่ได้** |
| 6 / 7 / 11 / 17 | Rhythm is a Dancer; Keyposes; Atomic Movements; Motion Texture | **ครบบางส่วน** | เปเปอร์นี้คือบรรพบุรุษที่เก่ากว่าของทั้ง 4 แพตเทิร์น: หน่วยท่าที่ quantise แล้ว, ลำดับชั้นบนหน่วยเหล่านั้น, "atomic behaviours" (ศัพท์เดียวกับที่ข้อ 11 ใช้) และโครงสร้าง transition matrix · มันตั้งเพดาน novelty ไว้ว่า **ลำดับชั้น 2 ระดับบน movement atom ที่เรียนรู้ได้เองมีมาตั้งแต่ปี 2001** → ข้อเคลมใด ๆ ว่า *ค้นพบ* โครงสร้างลำดับชั้น ต้องขีดเส้นแยกจาก §4 ให้ชัด |
| 12 | Aligning motion generation with human perceptions | **ไม่ครอบคลุม** | ไม่มี perceptual study ไม่มี user study ไม่มี critic ที่เรียนมา · การสังเคราะห์ตัดสินด้วยสายตา (Fig. 6, 9) → ตอกย้ำว่าโปรเจกต์เราต้องมี metric ประเมินการ generate ที่เป็นอิสระ ซึ่งเปเปอร์นี้ไม่ได้ให้ |
| 24–31 | Tier 3 Phase-2 / energy-curve | **ครบบางส่วน (เกี่ยวข้องแบบไม่คาดคิด)** | การตัดแบ่งด้วย **velocity minima** (§4.1) คือการตัดแบ่งโครงสร้างโดยอาศัยพลังงานการเคลื่อนไหว และ §4 ทั้งหัวข้อคือการโมเดล macro-structure ของการเคลื่อนไหว · `paper_chain.md` บันทึกภาระว่าต้องขีดเส้นแยก Phase 2 ออกจาก A1-21 §4 ไว้แล้ว และการอ่านเต็มรอบนี้ **ยืนยัน** ภาระนั้น · **ข้อแตกต่างเชิงชนิด:** Galata et al. ตัดแบ่งด้วยจุดต่ำสุดของ velocity *แบบทันทีทันใด* บนเส้นทางท่า ไม่ใช่การ cluster เส้นโค้งพลังงานทั้งคลิปที่ปรับให้เรียบแล้ว |

### (ค) การทดลองที่ checklist ให้เกิดจากการอ่านนี้

| Exp. | สถานะหลังอ่านจบ |
|---|---|
| **E2 — VLMM + first-order Markov เป็น baseline เทียบ LSTM** | **ปลดล็อกแล้ว** · เปเปอร์ให้ hyperparameter ฝั่ง VLMM ครบ: ε = 0.0001 · N ∈ {5, 20} ระดับ prototype และ N ∈ {2, 4, 6, 8} ระดับสูง · เทรนผ่าน prefix tree → prediction suffix tree ที่ prune ด้วย KL → PFSA · back-off กลับสถานะเริ่มต้นเมื่อเจอ token ความน่าจะเป็นศูนย์ · วัดผลด้วย `E_T` กับ Monte-Carlo 50 ครั้ง/เฟรม และ error bar แบบ mean absolute deviation · เรามี transition matrix อยู่แล้ว first-order จึงแทบฟรี · **สิ่งที่ไม่ได้ให้ และต้องตัดสินใจเอง:** พารามิเตอร์ robust VQ ที่ให้ผลเป็น 71/87 (โยนไป [13]) · *ค่า* ของเกณฑ์ velocity ใน §4.1 · จำนวน template cluster m ต่อ atomic behaviour และเกณฑ์หยุด clustering ของ DTW · และเกณฑ์ unseen-event ใน §4.4 · **ข้อควรเผื่องบ:** จำนวน state (117/290 และ 22/34/45 จาก V=71 · 112/226 และ 9/12 จาก V=87) มาจาก vocabulary 71/87 → ถ้าใช้ vocabulary 216 ที่ N = 20 ควรคาดว่า automaton จะใหญ่ขึ้นมาก |
| **E3 — ใส่ velocity ลง feature vector แล้วค่อย dedup** | **มีเหตุผลรองรับเต็มที่** · Eq. 8 ต้องใช้ `Ċ` ที่จุดปลายทั้งสองข้าง ดังนั้น velocity ต้องอยู่ *ข้างใน* feature vector ก่อน dedup ไม่งั้นกู้จังหวะเวลาไม่ได้เลย · λ คือปุ่มถ่วงน้ำหนัก (10 สำหรับ contour 2 มิติ, 30 สำหรับ mocap 3 มิติ) — ที่นั่นเลือกมาโดยไม่มี ablation เราจึงต้อง tune เอง |
| **E1 — limb-subspace check (`stumpy.mstump`)** | **ไม่ครอบคลุม** · ดูแถว 10/19: ทั้งตัวล้วน ไม่มีการวิเคราะห์ subspace |
| **E4 — sweep V ที่ window rate คงที่** | **สนับสนุนได้อ่อนมาก** · 71 กับ 87 เป็นข้อมูลจุดเดียว ไม่ใช่หลักฐาน · ไม่มีการ sweep |
| **E5 — continuous-baseline LSTM** | **ไม่ครอบคลุม** · ไม่มี continuous baseline · เปเปอร์ไม่เคยถามว่า discretisation แลกอะไรไป |
| **E6 — z-zeroed เทียบ full 3-D tokenisation** | **ไม่ครอบคลุม** · dataset 2 เป็น mocap ที่ใช้ marker และไม่มีการพูดถึง error ในแกนลึกเลย จึงบอกอะไรเกี่ยวกับความน่าเชื่อถือของ z แบบ monocular ไม่ได้ |
| **E7 — metric ที่ไม่ต้องมี corpus (Coverage / LocalDiv / InterDiv / SiFID)** | **ไม่ครอบคลุม** · `E_T` เป็น metric ที่ *ต้องจับคู่กับ ground truth* และต้องมีลำดับทดสอบคู่กัน · มันไม่ใช่ metric วัดความหลากหลายแบบไม่ต้องมี corpus และแทน E7 ไม่ได้ · **เป็นส่วนเสริมกัน ไม่ใช่ซ้อนทับกัน** |

### (ง) รายการใน checklist ที่ไม่เกี่ยวกับเปเปอร์นี้

ข้อ 2 (SinMDM), 5 (Rode et al. monocular pose), 9 (Labrak et al.), 14–16, 18, 20–23 (Tier 2 related work)
และกลุ่มที่ติด paywall/บล็อกทั้งหมด (L3-29, L3-26, A0-2, A0-5, A0-6) ไม่เกี่ยวกับเนื้อหาเปเปอร์นี้
→ **ไม่ครอบคลุม — ซึ่งถูกต้องแล้ว**

### ⚠️ สิ่งที่ต้องแก้ย้อนกลับ (พบระหว่างตรวจ · ยังไม่ได้แก้ เพราะไฟล์เหล่านี้เป็น input)

1. **`paper_notes/paper_index_A.csv` บรรทัด 60** — ข้อความ "variable-length Markov over pose strings **on dance**"
   **ผิด** · ควรเป็น: *on exercise/aerobics routines (2-D silhouette contours; 13-marker 3-D mocap)*
2. **`reading_checklist.md` บรรทัด 17** — ระบุพาธ PDF ของเปเปอร์นี้เป็น `knowledge/references/Galata_...pdf`
   ซึ่ง **ไม่มีไฟล์อยู่ตรงนั้น** (`knowledge/references/` มีแต่สไลด์เรียนกับ `paperหนัง.pdf`)
   · ตำแหน่งจริงคือ `knowledge/reading_docs/`

### สรุปผล checklist หนึ่งบรรทัด
เป้าหมาย "อ่านเอา" ทุกข้อที่ checklist ตั้งไว้สำหรับเปเปอร์นี้ **ครบถ้วนทั้งหมด** — §3, §4.1–4.5, Eq. 8
และโพรโทคอล `E_T`/Monte-Carlo-50 ยืนยันได้ทั้งหมด **ปลดล็อก E2 และ E3 เต็มตัว** ·
ส่วน **E1, E5, E6, E7 เปเปอร์นี้ไม่แตะเลย** และ **E4 สนับสนุนได้อ่อน** ·
และมี **2 จุดที่ต้องแก้ย้อนกลับในไฟล์ input ของโปรเจกต์เอง** (ข้อมูลเป็น **ท่าออกกำลังกาย/แอโรบิก** ไม่ใช่ dance ·
และพาธ PDF ใน checklist ผิด)

---

## 8. Verification (การตรวจสอบรอบสองแบบอิสระ)

fact-auditor แยกตัวได้สกัด PDF ใหม่ด้วยตัวเอง (`pdftotext` ทั้งโหมด `-layout` และ `-raw`) อ่าน `reading_guide.md`
และ `reading_checklist.md` ซ้ำ แล้วตรวจร่างเทียบต้นฉบับแบบตั้งใจหาเรื่อง
ผลตัดสิน: **REVISE — ไม่มีการกุข้อมูล ไม่มีการอ้างอิงลอย ไม่มีตัวเลขผิด**

**สิ่งที่ตรวจแล้วถูกต้อง**
- **ตัวเลขทุกตัว** ไล่กลับไปหา PDF และเช็คว่าถูกผูกกับ dataset *และ* ระดับโมเดลที่ถูกต้อง:
  71/87 prototypes · 117/290, 112/226, 22/34/45, 9/12 states · ε = 0.0001 ครบทั้ง 4 การทดลอง · λ = 10/30 ·
  25/50 fps · 40 วินาที, 8 × ≈25 วินาที · จุดควบคุม 32 จุด · marker 13 จุด · 128 = 2×2×32 ·
  key prototypes 5 และ atomic behaviours 8 (ทั้งสอง dataset) · Monte Carlo 50 · horizon 70 / ≈140 ·
  ค่าสูงสุดแกน 1.8 / 0.9 · training 4 รอบ เทียบ test 3 รอบ
- **สมการทั้ง 6 ตัวที่ให้ตรวจ** (5, 8, 9, 12, 13, 14) ถอดความถูกต้อง รวมถึงตำแหน่งตัวเศษ/ตัวส่วน ·
  Eq. 6, 7, 10, 11 สุ่มตรวจแล้วเช่นกัน · **การตีความ Eq. 8 ว่าเป็น "ระยะทาง ÷ อัตราเร็วเฉลี่ย" ได้รับการยืนยันชัดเจน**
- **quote ถูกต้องตรงตัว 19 จาก 20 จุด** · **เลขอ้างอิงทุกตัว** ตรงกับบรรณานุกรม
- **การแก้ย้อนกลับทั้ง 2 จุดได้รับการยืนยันและอนุมัติให้ส่งต่อ**: ข้อค้นพบเรื่อง exercise ไม่ใช่ dance
  (นับคำ: "dance" 2 ครั้ง อยู่ในลิสต์จูงใจเดียวกันทั้งคู่ · "exercise" 29 ครั้ง) และข้อผิดพลาดเลขคณิต
  `d = 72 (2 × 3 × 13)` (78 คือค่าที่น่าจะตั้งใจ)
- การวินิจฉัยว่าเป็น preprint ไม่ใช่ฉบับเรียงพิมพ์ · และข้อจำกัดเรื่องไม่มีการทดสอบนัยสำคัญ, ข้อมูลคนเดียว,
  การสูญเสียข้อมูลจาก dedup, การไม่เคยวัด recognition, และความไม่สอดคล้องของการนับมิติ

**ข้อแก้ที่ auditor ให้มา — แก้ลงร่างแล้วทั้งหมด**
1. แก้การอ้างอิงข้าม: `paper_chain.md` ไม่มีหัวข้อ R10-5 → เปลี่ยนเป็น **R9-5 ข้อ 1 / R10-4 ข้อ 5**
2. มี quote ที่ถูกแก้คำสะกดให้เงียบ ๆ → คืนเป็น **"Multiple occurances [sic] … a single occurance [sic]."**
3. เปิดเผยความกำกวมของปริภูมิ `E_T`: §3.2.3 เขียน "configuration space" แต่คำบรรยาย Fig. 4 & 10 เขียน
   "**augmented** configuration space" → เปลี่ยนจากการยืนยันเป็นการตั้งธงเตือน
4. คืนคำกันตัวที่หายไป: "resolves ambiguities" → **"helps resolve ambiguities"**
5. แก้การโยนความผิด: grammar ที่เขียนมือเป็นของ Bobick & Ivanov [4] **เท่านั้น** ไม่ใช่วรรณกรรม
   dance/aerobics/sign-language ทั้งกลุ่ม [6, 20, 21] ซึ่งใช้ phase-space constraints หรือ HMM
6. คืนคำกันตัวที่หายไป: topology ของ HMM "ต้องตรึงไว้ล่วงหน้า" → **"often highly constrained prior to training"**
7. เอาการชนกันของสัญลักษณ์ออก (เดิมใช้ τ ทั้งกับ transition function และ template sequence)
   พร้อมเพิ่มคำเตือนว่าอักษรกรีกกู้จาก text layer ของ PDF นี้ไม่ได้
8. ลดระดับข้อเคลมเกินจริง: "ขนาด vocabulary ไม่มีเหตุผลรองรับ" → 71/87 เป็น **output ของ VQ ตาม [13]**
   ซึ่งพารามิเตอร์ของมันเองไม่ได้ถูกรายงาน
9. ระบุตำแหน่งหน้า "List of figures" ให้ถูก (หน้า 23 · หลัง references · ก่อนแผ่นรูปหน้า 24–33)
10. ระบุที่มาของข้อมูลบรรณานุกรมหัวเอกสารว่ามาจาก `paper_index_A.csv` เพราะไม่มีอะไรในไฟล์ PDF เลย

**ข้อเคลมเกินจริงที่ auditor จับได้และบังคับให้ลดระดับ**
- **E2 "ให้ hyperparameter ครบทุกตัวที่ต้องใช้"** → มี 4 พารามิเตอร์ที่เปเปอร์ *ไม่* ให้
  (พารามิเตอร์ VQ, ค่าเกณฑ์ velocity, จำนวน template cluster m, เกณฑ์ unseen-event ใน §4.4)
- **การผูกของ λ** → เกณฑ์ใน §4.1 ใช้ `|Ċ_t|` ที่ *ยังไม่สเกล* ดังนั้นผลของ λ ต่อการตัดแบ่งเป็นแบบ **ทางอ้อม**
  (ผ่านว่ามี prototype อะไรบ้าง) ไม่ใช่การใช้พจน์ร่วมกันโดยตรงอย่างที่ร่างเดิมเขียน
- **"ข้อมูลทดสอบเป็นรูทีนเดียวกับ training"** → สนับสนุนเต็มที่เฉพาะ dataset 1 ·
  ส่วน dataset 2 เปเปอร์ไม่ได้ระบุความต่างจาก training เลย
- **Eq. 14** → ปรับให้คมขึ้นโดยระบุว่าเปเปอร์เองก็กันตัวไว้แล้ว ("approximate", "relative probability")
  ทำให้เป็นจุดอ่อนเชิงการนำเสนอมากกว่าความผิดพลาด
- **"ไม่มีโค้ด/ข้อมูลให้"** → จัดกรอบใหม่เป็นข้อสังเกตเรื่อง artefact availability ไม่ใช่ข้อบกพร่องเชิงวิธีวิทยาของปี 2001

**สิ่งที่ auditor จับได้ว่าตกหล่น — เพิ่มลงร่างครบแล้ว**
สเกลเวลา 20 ms / ~1 วินาที จาก §1 · Figure 7 (ผลเชิงคุณภาพของการทำนาย) · ความขัดแย้ง §4.2 เทียบ §4.5
เรื่อง alphabet ชั้นที่ 2 · การใช้คำ "cross-entropy" ใน §1 เทียบ "weighted KL" ใน §3.1 ·
การอ้าง prefix tree ไปที่ [9] · ข้อความ "every second frame of the first 700 frames" ของ Fig. 9 ·
การระบุว่า Fig. 6 เป็น dataset 2 (N = 4) และ Fig. 9 เป็น dataset 1 · และที่มาของ H-Anim 1.1 / "Baxter"
จาก Acknowledgments · นอกจากนี้ยังตั้งธงเรื่องความหมายแคบของ "recognition mode" ใน §3.2.2
และการใช้พหูพจน์กว้าง ๆ "individuals" ทั้งที่ข้อมูลเทรนเป็นคนเดียว — แยกแยะไว้ในเนื้อความแล้วทั้งคู่

**หมายเหตุเรื่องขอบเขต:** auditor ท้วงถูกต้องว่า ข้อความเรื่อง `notebooklm` MCP server ล้มเหลวในรอบนี้
เป็นข้อเท็จจริงเกี่ยวกับ *เซสชัน* ไม่ใช่เกี่ยวกับ *เปเปอร์* → ย้ายออกจากสรุปนี้ไปไว้ในรายงานการรันแล้ว

**รายการที่ยังตรวจไม่ได้** (ระบุตรง ๆ แทนที่จะแกล้งปิด):
- *ค่าบนเส้นกราฟ* — สภาพแวดล้อมนี้ไม่มีตัว render PDF เป็นภาพ จึงรายงานได้แค่ลำดับที่ผู้เขียนยืนยันในเนื้อความ
- *เลข section และ equation* เทียบกับฉบับ CVIU ที่ตีพิมพ์
- ชื่อสัญลักษณ์กรีกที่เปเปอร์ใช้จริง
- คำว่า "double-spaced" ในข้อควรระวังเรื่องเวอร์ชัน เป็นความรู้สึกจากระยะห่างบรรทัด ไม่ใช่การวัด
