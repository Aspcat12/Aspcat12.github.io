# Knowledge-base audit — 2026-09-23 (scheduled `read-a-paper`, secondary output)

**Primary output of this run** was a new paper summary: `566570.566604.summary.md` (A1-7 Motion Texture).
This file is the **secondary** output: the run began by auditing the existing knowledge files, because at
start-of-session `reading_docs/` appeared to hold 16 PDFs and 16 summaries.

> ⚠️ **That premise was wrong, and this is worth recording.** Ten new PDFs were dropped into
> `reading_docs/` at **13:11–13:15 today**, *after* this session's opening directory listing. The run
> therefore started in "no unread papers" mode on stale information. The verification subagent caught it by
> re-listing the directory instead of trusting the draft. The run then switched to reading the oldest unread
> paper, as the task specifies. **Lesson for future runs: re-list `reading_docs/` immediately before deciding
> the mode, not once at session start.**

**Method.** Cross-file sweep by the main agent, then an independent second pass by Vera (`fact-auditor`),
which re-extracted every cited PDF with `pdftotext` (newlines flattened, line-break hyphens joined) and
re-opened every file:line before confirming a finding.

**Verdict: REVISE.** **Every finding from the 2026-09-22 run is still unfixed**, and two of them are blockers
that would put an unsupported claim into the thesis. Three new defects were found. **No file was edited
except `reading_checklist.md` item 17 (one checkbox tick, for the paper read this run) and the new summary.**

---

## Part 1 — Status of the 2026-09-22 findings: all eight still open

| # | Finding | Status | Evidence re-verified this run |
|---|---|---|---|
| **C1** (was B1) 🔴 | "Static Pose / Dynamic Connection" attributed to A0-3, but the phrase appears **0 times** in both `rspa.2021.0071.pdf` and `1906.00606v1.pdf` | **UNFIXED** | Still live at `paper_chain.md:766–767`, `paper_index_A.csv:35`, `reading_checklist.md:109`, `2607.13978v1.summary.md:25,110,338,473,557,787`, `2409.00203v1.summary.md:262` |
| **C2** (was B2) 🔴 | A1-14 flexion angles wrong | **UNFIXED, and in one more file than last run reported** | PDF abstract, extracted independently: *"knee flexion angle was measured with a mean absolute error of **9.3–21.9** in 2D and **14.1–25.8** in 3D. The elbow flexion angle … **21.5–28.9** in 2D and **16.3–26.0** in 3D."* The strings `23.7`, `31.2`, `41.3`, `35.0` and the quote `"substantially inaccurate"` each return **0 hits**. Live at `paper_chain.md:1367–1368`, `reading_checklist.md:54`, and **`paper_index_A.csv:43`** ← *not listed in the 2026-09-22 report* |
| **C3** (was S1) 🟠 | `1906.00606v1.summary.md` mis-credits "8 cameras / 8 PCs" | **UNFIXED** | Preprint: *"Using motion capture with **8 cameras and 8 PCs, Nakazawa et al. [28]**"* — `[27]` is Choreogenetics. Still wrong at lines **70, 105, 337**. Line 219 ("the one place a clustering algorithm appears at all") still false for the journal, which adds SLIC [63]. Line 103 still uses the preprint's "Latin American" wording |
| **C4** (was S2) 🟠 | Checklist corrections recorded in summaries but never carried into the checklist | **UNFIXED** | Re-verified two directly: DASB's `bitrate = log2 V · C · R` sits under the heading **`3.2 Discrete Audio Encoder`**, but `reading_checklist.md:38` still says §5.2. A1-22 page 1 reads *"Published as a conference paper at **ICLR 2025**"*, but `reading_checklist.md:95` still says "(2024)" |
| **C5** (was S3) 🟡 | `summaries/README.md` gaps | **UNFIXED** | Still **0 rows** for `rspa.2021.0071.summary.md` and `2409.00203v1.summary.md`. `README.md:14` still claims k≥2500 *"ไม่ตกที่โมเดลใหญ่"*, but the 1.7B model is **OOM** at k=2500 and 5000 — never tested. Paper: *"the 1.7B model demonstrating remarkable stability … **though encountering memory limitations at higher clusters**"* |
| **C6** (was F5) 🟡 | Checklist item 1 gives the Galata PDF path as `knowledge/references/…` | **UNFIXED** | File exists only at `knowledge/reading_docs/Galata_…pdf`; `knowledge/references/` holds only course slides |
| **C7** (was S4) 🟡 | A0-8 year contradiction | **UNFIXED** | `reading_checklist.md:45` "IEEE TPAMI **2025**" vs `:209` "**TPAMI 48(4):4184-4204, เมษายน 2026**". `paper_index_A.csv:52` sides with 2026 |
| **C8** (was F7) 🟡 | Checklist item 15 has one `[✅]`; its own note asks for two | **UNCHANGED, deliberately** | The item's note asks for a tick on "read both" and on "compared" — both conditions are met. But the legend at line 12 assigns the second tick to **"Cop"** (the user). Two conflicting definitions; **left for the user to decide** |

---

## Part 2 — New defects found this run

### 🔴 N1. Checklist E10 declares a caveat closed that cannot be closed by the paper it cites

`reading_checklist.md:220–222` (E10) says the `eval_generation.py` caveat is handled: *"**อ่านแล้ว** …
เหลือแค่ลงมือ reconcile"* (already read; only the reconcile remains).

But `src/eval_generation.py:16–23` still carries, verbatim:

```
>>> CAVEAT -- READ BEFORE PUBLISHING ANY NUMBER FROM THIS SCRIPT <<<
The formulas below are OUR READING of the metric DEFINITIONS quoted in the
SinMDM evaluation section. We do not have the paper's exact formulas. ...
Before any of these numbers enter the thesis, read the full SinMDM method
section and reconcile it with this file.
```

**Reading SinMDM cannot discharge this, because SinMDM has no formulas to reconcile against.** Verified from
the PDF, not just from our summary — SinMDM §6.2 gives prose only: *"The metrics in Ganimator consist of
(a) coverage … (b) global diversity … (c) local diversity"*, prefaced by *"For a fair comparison, we use the
metrics suggested by them."* Our own summary reaches the same conclusion at
`2302.05905v2.summary.md:14`: *"To implement these we must read Ganimator and SinGAN. **This paper is not a
sufficient source.**"* And `summaries/README.md:34` still lists the real formulas as an **open gap** with
*"เลขใน `eval_generation.py` ยังตีพิมพ์ไม่ได้"*.

**Risk:** someone reads E10, believes the caveat is discharged, and publishes Coverage/Diversity numbers.

**Two further blockers inside the same caveat that E10 does not address:**
- the **normalized-Hamming substitution**, which the file's own header calls *"a design choice of ours, not
  something the paper endorses"* — also not fixable by reading SinMDM;
- checklist items feeding E10 are themselves still wrong: `:30` advertises *"metric ที่ไม่ต้องมี corpus"* and
  `:33` asks for *"สูตรจริง ไม่ใช่ชื่อ"*, but SiFID **requires a deep feature extractor**.

**Fix:** reword E10 to "SinMDM read; caveat **still open** pending Ganimator (Li et al. 2022) and SinGAN."

### 🔴 N2. `summaries/README.md:25` mixes two reference-numbering systems inside the starred white-space claim

The row instructs *"⚠️ **อ้าง RSPA เท่านั้น**"* (cite RSPA only) and then supports the ⭐ novelty claim with
`([43] 4 ท่า, [60] 60 หน่วย, [41] movement catalyst 13 ค่า)`. Resolved against both reference lists:

| | preprint 1906 | journal RSPA |
|---|---|---|
| `[43]` | **Lapointe & Epoque**, dancing genome | Nagata, Okumoto, Iwai, Toro, Inokuchi |
| `[60]` | **Shinozaki, Iwatani, Nakatsu**, dance robot | Jadhav, Aras, Joshi, Pawar |
| `[41]` | Hagendoorn, emergent patterns | **Carlson, Schiphorst, Pasquier** ← the intended one |

So `[41]` is **journal** numbering while `[43]` and `[60]` are **preprint** numbering, in a row that says to
cite RSPA. A bibliography built from this attributes the 4-movement vocabulary to Nagata and the 60-unit
vocabulary to Jadhav — neither of which is the source. RSPA's own text: *"**60 dance units** were extracted
and these short dance motions were concatenated for a robot dance system"*; *"Carlson et al. [41] generated
**13 valued vector (movement catalyst**…"*.

**This is the most-cited claim in the corpus and the one most likely to reach a reviewer.**

### 🔴 N3. `paper_index_A.csv:61` records A1-22 as `2024, arXiv preprint`

`2407.02272v2.pdf` page 1: *"Published as a conference paper at **ICLR 2025**."* The 2026-09-22 run caught the
checklist's "(2024)" but not the CSV row — and **the CSV is the file a bibliography is generated from**.
Every other venue-corrected row in that CSV carries a `RUN11 VENUE VERIFIED (Crossref)` note; this one does not.

---

## Part 3 — Smaller corrections

- 🟠 **"half of 36" vs "all 36" is a live contradiction about our own code.** `reading_checklist.md:55` says
  *"ครึ่งหนึ่งของ 36 angle features ที่พึ่ง z"* and `paper_index_A.csv:43` says *"the z-dependent half"*. But
  `paper_chain.md:1382` says *"all 36 features inherit the depth error"* and `:1562` says *"**all** of our 36
  features rest on (verified in the code)"*. **This sets the scope of experiment E6** (z-zeroed vs full 3-D),
  so it is not cosmetic.
- 🟠 **"2D ~80 mm" is refutable, not merely unlocatable.** The 2026-09-22 run hedged this as "possibly in
  Supp. S1". The article body in fact gives the number: *"BlazePose 'Local' with the 'Heavy' model. This
  approach showed a ex of **34 mm** and ey of **43 mm**, leading to a **2D MPJPE of 61 mm**."* So `≈ 80 mm` is
  wrong by ~30 % and the correct value is available. Upgrade from "unverified" to **"incorrect → 61 mm"** at
  `paper_chain.md:1364`, `reading_checklist.md:54`, `paper_index_A.csv:43`.
- 🟠 **Correction to the 2026-09-22 report itself.** It called A1-17's `k=1000→100` an *"unablated design
  choice"*. Half wrong: `2012.04731v4` §4 says *"**We report results of using different number of clusters in
  Table 5.** … We chose to use 1000 clusters."* The **1000 is ablated**; only the 100 is not. Its conclusion
  (that "vocabulary scaled to corpus size" is overreach) still stands — and is *stronger*, since Table 5 finds
  more clusters cost only training time — but the stated reason should not be copied forward.
- 🟡 **`reading_checklist.md:80` "cluster utilisation 74–92%" is a composite matching no encoder.** Paper:
  *"HuBERT and WavLM demonstrate superior cluster utilization (**77-92% and 74-91%** respectively)"*. The same
  error is at **`paper_index_A.csv:48`**.
- 🟡 **Checklist item 10's quote is compressed *and* mis-contextualised.** `:87` prints
  *"eight additional irrelevant dimensions → about as well as random chance"* in quotation marks; the paper
  reads *"**However, empirically averaging over 100 trials**, we have found that **if there are** eight
  additional irrelevant dimensions, **then we do** about as well as random chance."* More importantly, `:86–88`
  attributes it to the boxing-mocap opening example, but the setup is a **synthetic 2-D motif with random
  walks added** as the irrelevant dimensions. **This number is the entire justification for experiment E1**,
  so the splice matters.
- 🟡 **`reading_checklist.md:101` (A1-18 verbatim quote) drops its scoping.** The full sentence is
  *"**Taking Nnv = 302M as an example**, when available data is the bottleneck, the optimal vocabulary size
  decreases empirically, i.e. 16K → 10K"*, and it has a **converse**: *"when training on excessive amounts of
  data … the optimal vocabulary size increases."* The quote is a real substring; the conditioning is missing.
- 🟡 **Stale status text.** `2409.00203v1.summary.md:262` still says both A0-3 PDFs are *"still unread"*.
  Both were summarised on 2026-09-21.

---

## Part 4 — Checked and found correct (no action needed)

Recorded so a future run does not re-litigate these:

- **A1-14 core numbers all verified from the PDF:** 3D MPJPE **146 mm**; `ē_x` **50** / `ē_y` **58** /
  `ē_z` **108 mm**; 2D range **72–122 mm**; 3D range **146–249 mm**; 3D PAMPJPE 110 mm; 98.8 % detected;
  147 FPS. The depth claim is supported verbatim: *"The mean absolute depth error is approximately **two to
  three times greater** than the mean absolute horizontal and vertical errors for all pose estimators."*
  `paper_chain.md:1365`'s "best **direct** method" qualifier is correct.
- **`docs/ADVISOR_METRICS_2026-09.md` is correctly hedged** — line 580 explicitly warns
  *"ตรวจโค้ดแล้ว 2026-09-20 — แถว 146 มม. ไม่ใช่ของ pipeline เรา ห้ามอ้างแบบนั้น"*. No action.
- **`evaluation_methods.md` and `memory.txt` are clean** of the C1/C2 contamination.
- **FSQ (checklist item 8):** *"VQ … below 50% usage for codebooks larger than 2¹¹"* (= 2048). Correct.
  Companion claim at `csv:53` also correct: *"for low codebook sizes …, **VQ marginally outperforms FSQ**"*.
- **L3-22 "k = 500 best" (item 9):** *"WavLM achieves the best performance (NLL=2.05, k = 500) at Step 300."*
  Correct.
- **Venue spot-check:** A1-18 really does print *"38th Conference on Neural Information Processing Systems
  (NeurIPS 2024)"* and DASB prints *"Published in Transactions on Machine Learning Research (04/2026)"*. The
  2026-09-22 report's blanket "venues not in the PDFs" was **too broad** — A1-16/A1-17/A1-19/L3-22/A0-8 all
  carry explicit Crossref/OpenReview verification notes in the CSV.

---

## Verification (second pass)

**What Vera checked:** every "still unfixed" claim re-opened at the named file and line; every number and
quoted string re-extracted from the source PDF; and an independent sweep for defects the draft had missed.

**Result:** C1–C8 **CONFIRMED** (with one line-number correction: C1 is `paper_chain.md:766–767`, not 767).
N1 confirmed and **promoted from ORANGE to BLOCKER** after Vera checked `src/eval_generation.py` directly and
read SinMDM §6.2 from the PDF. N2 and N3 are Vera's own additions — the draft had dropped the README
reference-numbering defect entirely and had not checked the CSV's A1-22 row. The draft's "checked and found
correct" list survived except for checklist item 10, which Vera removed from it (see Part 3).

**Correction Vera made to the draft's own count:** the draft said C2 appeared in two files; it is three.

---

## Suggested next steps (for the user)

1. **Fix N1, N2, C1 and C2 before anything from them is cited.** These four are the ones that reach a
   bibliography or a results section.
2. Fix N3 (`paper_index_A.csv:61` → ICLR 2025) while touching the CSV for C2.
3. Resolve the **"half of 36" vs "all 36"** contradiction — it scopes E6.
4. Add the two missing rows to `summaries/README.md`, and decide the C8 tick convention.
5. **Nine unread PDFs remain** in `reading_docs/` after this run (checklist items 16, 18–23 and others, added
   2026-09-23). The next scheduled run has plenty to read — no new PDF needs to be added.

---
---

# ฉบับภาษาไทย — รายงานการตรวจสอบคลังความรู้ 2026-09-23

**ผลลัพธ์หลักของรอบนี้** คือสรุปเปเปอร์ใหม่ `566570.566604.summary.md` (A1-7 Motion Texture)
ไฟล์นี้เป็น **ผลลัพธ์รอง**: การตรวจสอบไฟล์ความรู้เดิม ซึ่งเริ่มทำเพราะตอนเปิดเซสชัน `reading_docs/` ดูเหมือนมี PDF 16 ไฟล์ และสรุป 16 ไฟล์

> ⚠️ **สมมติฐานนั้นผิด และควรบันทึกไว้** · มี PDF ใหม่ 10 ไฟล์ถูกใส่เข้า `reading_docs/` เวลา **13:11–13:15 ของวันนี้**
> ซึ่งเป็นเวลา *หลัง* การไล่รายชื่อไดเรกทอรีครั้งแรกของเซสชัน · รอบนี้จึงเริ่มในโหมด "ไม่มีเปเปอร์ใหม่" บนข้อมูลที่ล้าสมัย
> · subagent ผู้ตรวจจับได้เพราะไปไล่รายชื่อไดเรกทอรีใหม่แทนที่จะเชื่อร่าง · จากนั้นรอบนี้จึงเปลี่ยนไปอ่านเปเปอร์ที่เก่าที่สุดที่ยังไม่ได้อ่านตามที่ task กำหนด
> **บทเรียนสำหรับรอบถัดไป: ให้ไล่รายชื่อ `reading_docs/` ใหม่ทันทีก่อนตัดสินใจเลือกโหมด ไม่ใช่ครั้งเดียวตอนเปิดเซสชัน**

**คำตัดสิน: REVISE** · **ทุกข้อค้นพบจากรอบ 2026-09-22 ยังไม่ได้รับการแก้ไขเลย** โดย 2 ข้อเป็น blocker
และพบข้อบกพร่องใหม่อีก 3 ข้อ · **ไม่ได้แก้ไฟล์ใดเลย** ยกเว้นติ๊ก checkbox ข้อ 17 ใน `reading_checklist.md` (สำหรับเปเปอร์ที่อ่านรอบนี้) และไฟล์สรุปใหม่

## ส่วนที่ 1 — สถานะของข้อค้นพบรอบ 2026-09-22: ยังเปิดอยู่ทั้ง 8 ข้อ

- **C1 🔴** "Static Pose / Dynamic Connection" ไม่มีใน PDF ทั้งสองฉบับ (0 ครั้ง) — **ยังไม่แก้** ·
  ยังอยู่ที่ `paper_chain.md:766–767`, `paper_index_A.csv:35`, `reading_checklist.md:109`,
  `2607.13978v1.summary.md:25,110,338,473,557,787`, `2409.00203v1.summary.md:262`
- **C2 🔴** ตัวเลขมุมงอของ A1-14 ผิด — **ยังไม่แก้ และอยู่ในไฟล์มากกว่าที่รายงานรอบก่อนระบุ 1 ไฟล์** ·
  PDF จริง: เข่า **2D 9.3–21.9° / 3D 14.1–25.8°** · ศอก **2D 21.5–28.9° / 3D 16.3–26.0°** ·
  สตริง `23.7`, `31.2`, `41.3`, `35.0` และ quote `"substantially inaccurate"` = **0 ครั้งทั้งหมด** ·
  ยังอยู่ที่ `paper_chain.md:1367–1368`, `reading_checklist.md:54` และ **`paper_index_A.csv:43`** ← *ไม่ได้อยู่ในรายงานรอบก่อน*
- **C3 🟠** สรุป 1906 ยกเครดิต "8 กล้อง / 8 PC" ผิด — **ยังไม่แก้** · PDF: *"…**8 cameras and 8 PCs, Nakazawa et al. [28]**"*
  ([27] คือ Choreogenetics) · ยังผิดที่บรรทัด 70, 105, 337 · บรรทัด 219 และ 103 ก็ยังเดิม
- **C4 🟠** คำแก้ที่บันทึกในสรุปแต่ไม่เคยเข้า checklist — **ยังไม่แก้** · ตรวจซ้ำ 2 ข้อโดยตรง:
  สมการ bitrate ของ DASB อยู่ใต้หัวข้อ **`3.2 Discrete Audio Encoder`** แต่ `:38` ยังเขียน §5.2 ·
  A1-22 หน้าแรกเขียน *"Published as a conference paper at **ICLR 2025**"* แต่ `:95` ยังเขียน "(2024)"
- **C5 🟡** `README.md` ยัง **ไม่มีแถว** ของ `rspa.2021.0071` และ `2409.00203v1` · และ `:14` ยังเคลมว่า k≥2500 *"ไม่ตกที่โมเดลใหญ่"*
  ทั้งที่โมเดล 1.7B **OOM** ที่ k=2500 และ 5000 คือไม่เคยถูกทดสอบ
- **C6 🟡** path ของ PDF Galata ใน checklist ข้อ 1 ผิด (ไฟล์จริงอยู่ `reading_docs/`) — **ยังไม่แก้**
- **C7 🟡** ปีของ A0-8 ขัดกันเองใน checklist (`:45` = 2025 vs `:209` = 2026) — **ยังไม่แก้**
- **C8 🟡** checklist ข้อ 15 มี ✅ ช่องเดียว · เงื่อนไขครบแล้วแต่ legend กำหนดให้ช่องที่สองเป็นของ "Cop"
  → **คงไว้ตามเดิมโดยเจตนา ให้ผู้ใช้ตัดสิน**

## ส่วนที่ 2 — ข้อบกพร่องใหม่ที่พบรอบนี้

- **🔴 N1. E10 ใน checklist ประกาศปิด caveat ที่ปิดด้วยเปเปอร์ที่มันอ้างไม่ได้** ·
  `:220–222` เขียนว่า *"อ่านแล้ว … เหลือแค่ลงมือ reconcile"* แต่ `src/eval_generation.py:16–23` ยังมีคำเตือนอยู่เต็ม ๆ ว่า
  สูตรเป็น "OUR READING" และ *"ต้องอ่าน method section ของ SinMDM แล้ว reconcile ก่อนตีพิมพ์"* ·
  **การอ่าน SinMDM ปิด caveat นี้ไม่ได้ เพราะ SinMDM ไม่มีสูตรให้ reconcile** (ยืนยันจาก PDF โดยตรง: §6.2 เป็นคำบรรยายล้วน
  และเขียนว่า *"เราใช้ metric ที่ Ganimator เสนอ"*) · สรุปของเราเองที่ `2302.05905v2.summary.md:14` ก็สรุปตรงกันว่า
  *"เปเปอร์นี้ไม่ใช่แหล่งที่เพียงพอ"* และ `README.md:34` ยังขึ้นบัญชีว่าเป็นช่องว่างที่เปิดอยู่
  **ความเสี่ยง:** มีคนอ่าน E10 แล้วเชื่อว่าปิดแล้ว จึงตีพิมพ์ตัวเลข Coverage/Diversity ออกไป
- **🔴 N2. `README.md:25` ปนระบบเลขอ้างอิงสองชุดอยู่ในข้ออ้าง white space ที่ติดดาว** ·
  แถวนั้นสั่งว่า *"อ้าง RSPA เท่านั้น"* แล้วอ้าง `[43] 4 ท่า, [60] 60 หน่วย, [41] movement catalyst 13 ค่า` ·
  แต่ `[41]` เป็นเลขของ **ฉบับวารสาร** ส่วน `[43]`/`[60]` เป็นเลขของ **preprint** ·
  ถ้าสร้างบรรณานุกรมจากแถวนี้ จะยกคลังคำ 4 ท่าให้ Nagata และ 60 หน่วยให้ Jadhav ซึ่งไม่ใช่เจ้าของทั้งคู่
  **นี่คือข้ออ้างที่ถูกใช้มากที่สุดในคลัง และมีโอกาสถึงมือ reviewer มากที่สุด**
- **🔴 N3. `paper_index_A.csv:61` บันทึก A1-22 เป็น `2024, arXiv preprint`** ทั้งที่หน้าแรกเขียน **ICLR 2025** ·
  รอบก่อนจับได้แต่ใน checklist ไม่ได้จับใน CSV — **และ CSV คือไฟล์ที่ใช้สร้างบรรณานุกรม**

## ส่วนที่ 3 — ข้อย่อย

- 🟠 **"ครึ่งหนึ่งของ 36" vs "ทั้ง 36" ขัดกันเองเรื่องโค้ดของเราเอง** · `:55` และ `csv:43` ว่าครึ่งเดียว
  แต่ `paper_chain.md:1382` และ `:1562` ว่า **ทั้งหมด (ตรวจในโค้ดแล้ว)** → **กำหนดขอบเขตการทดลอง E6** ไม่ใช่เรื่องผิวเผิน
- 🟠 **"2D ~80 มม." หักล้างได้ ไม่ใช่แค่หาไม่เจอ** · เนื้อบทความให้ตัวเลขไว้จริง: BlazePose 'Local' 'Heavy'
  มี ex 34 มม., ey 43 มม. → **2D MPJPE 61 มม.** ดังนั้น ~80 มม. ผิดไปราว 30% → เปลี่ยนสถานะจาก "ยังไม่ยืนยัน" เป็น **"ผิด → 61 มม."**
- 🟠 **แก้รายงานรอบ 2026-09-22 เอง** · ที่ว่า `k=1000→100` ของ A1-17 เป็น *"design choice ที่ไม่ได้ทำ ablation"* ถูกครึ่งเดียว —
  §4 เขียนว่า *"เรารายงานผลของจำนวน cluster ที่ต่างกันใน **Table 5**"* → **1000 ผ่าน ablation** มีแต่ 100 ที่ไม่ผ่าน ·
  ข้อสรุปเดิม (ว่า "vocab สเกลตาม corpus" เป็นการเคลมเกิน) ยังยืน และ *แรงขึ้น* ด้วยซ้ำ
- 🟡 **`:80` "cluster utilisation 74–92%" เป็นค่าผสมที่ไม่ตรงกับ encoder ตัวใด** (จริง: HuBERT 77–92%, WavLM 74–91%) ·
  ผิดแบบเดียวกันที่ **`paper_index_A.csv:48`**
- 🟡 **quote ข้อ 10 ถูกย่อ *และ* ผูกผิดบริบท** · ของจริงมี *"averaging over 100 trials"* นำหน้า และ setup คือ
  **motif สังเคราะห์ 2 มิติที่เติม random walk** ไม่ใช่ตัวอย่าง mocap ชกมวย · **ตัวเลขนี้คือเหตุผลทั้งหมดของ E1**
- 🟡 **quote ข้อ 13 (A1-18) ตัดเงื่อนไขทิ้ง** · ของจริงขึ้นต้นว่า *"Taking Nnv = 302M as an example"* และมี**ประโยคกลับด้าน**ด้วย
- 🟡 **ข้อความสถานะล้าสมัย** · `2409.00203v1.summary.md:262` ยังเขียนว่า PDF ของ A0-3 ทั้งสอง *"ยังไม่ได้อ่าน"*

## ส่วนที่ 4 — ตรวจแล้วถูกต้อง (ไม่ต้องแก้)

ตัวเลขหลักของ A1-14 ถูกต้องทั้งหมด (146 มม.; ē_x 50 / ē_y 58 / ē_z 108; 2D 72–122; 3D 146–249; PAMPJPE 110; 98.8%; 147 FPS)
และข้อความ *"ลึกผิดราว 2–3 เท่าของระนาบ"* มีรองรับตรงตัว · `ADVISOR_METRICS_2026-09.md` กันตัวไว้ถูกต้องแล้ว ·
`evaluation_methods.md` และ `memory.txt` สะอาด · FSQ ข้อ 8 ถูก · L3-22 "k=500 ดีที่สุด" ถูก ·
venue ของ A1-18 (NeurIPS 2024) และ DASB (TMLR 04/2026) มีอยู่ใน PDF จริง — คำว่า "venue ไม่มีใน PDF" ของรอบก่อน **กว้างเกินไป**

## การตรวจรอบสอง

Vera เปิดไฟล์ทุกบรรทัดที่อ้างซ้ำ และสกัดทุกตัวเลข/ข้อความจาก PDF ต้นทางใหม่ ·
**ผล:** C1–C8 **ยืนยัน** (แก้เลขบรรทัด C1 เป็น `paper_chain.md:766–767`) · N1 ยืนยันและ **เลื่อนจากส้มเป็น blocker**
หลัง Vera เปิด `src/eval_generation.py` และอ่าน SinMDM §6.2 จาก PDF เอง · **N2 และ N3 เป็นข้อที่ Vera พบเพิ่มเอง** —
ร่างแรกตกข้อ README ไปทั้งข้อ และไม่ได้ตรวจแถว A1-22 ใน CSV · รายการ "ตรวจแล้วถูก" ของร่างผ่านหมด
ยกเว้นข้อ 10 ที่ Vera ถอดออก · **Vera ยังแก้จำนวนไฟล์ของ C2 จาก 2 เป็น 3**

## ขั้นต่อไป (สำหรับผู้ใช้)

1. **แก้ N1, N2, C1, C2 ก่อนนำไปอ้างที่ใดก็ตาม** — สี่ข้อนี้คือข้อที่จะไปโผล่ในบรรณานุกรมหรือส่วนผลลัพธ์
2. แก้ N3 (`paper_index_A.csv:61` → ICLR 2025) ไปพร้อมกับตอนแก้ C2 ใน CSV
3. เคลียร์ความขัดแย้ง **"ครึ่งหนึ่งของ 36" vs "ทั้ง 36"** เพราะมันกำหนดขอบเขต E6
4. เพิ่มแถวที่ขาดใน `README.md` และตัดสินใจเรื่องกติกาการติ๊กของ C8
5. **ยังเหลือ PDF ที่ยังไม่ได้อ่านอีก 9 ไฟล์** ใน `reading_docs/` หลังรอบนี้ → รอบถัดไปมีของให้อ่านพอ ไม่ต้องเพิ่ม PDF ใหม่
