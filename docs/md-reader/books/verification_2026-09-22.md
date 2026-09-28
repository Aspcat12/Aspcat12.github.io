# Verification run — 2026-09-22 (scheduled `read-a-paper`)

**Mode:** No unread papers. All 16 PDFs in `reading_docs/` have a `summaries/<name>.summary.md`, so no new paper was read. As the task instructs, this run audited the existing knowledge files instead.
**Method:** I did the cross-file sweep myself. An independent second pass by Vera (the `fact-auditor` subagent) then re-checked every finding against the PDFs using `pdftotext`, in raw and layout modes with line-break hyphens joined, and ran its own spot-check of 12 numbers in `summaries/README.md`.
**Verdict: REVISE.** Two findings are blockers, meaning they would put an unsupported claim into the thesis. **No file was edited except this report.** The task allows only checkbox ticks in `reading_checklist.md`, and I changed no ticks (see F7).

---

## Findings (most severe first)

### 🔴 B1. "Static Pose / Dynamic Connection" has no source, and the claim has spread into four files
- **Claim:** A0-3 (Joshi review) says the minimum units of dance are "Static Pose" and "Dynamic Connection".
- **PDF check:** The phrase appears **0 times** in both `rspa.2021.0071.pdf` and `1906.00606v1.pdf`. The only nearby sentence in either version is: "A grammar of all possible movements can be formulated…".
- **Rest of the corpus:** Across all 16 PDFs, "static pose" appears only in 2012.04731 and 2607.13978, both times in ordinary usage and not as a named theory unit.
- **Where the claim still appears:**
  - `paper_notes/paper_chain.md:764-769` (R3-2 "Bonus fact … Use this in Methods").
  - `reading_checklist.md:109` (item 15).
  - `paper_notes/paper_index_A.csv:35`.
  - **`2607.13978v1.summary.md:338, 473, 557`**, which uses it as part (a) of the planned thesis rebuttal ("all now sourced"). *(Found by the verifier.)*
  - `2409.00203v1.summary.md:262` repeats it and also says both A0-3 PDFs are "still unread", which is now out of date.
- **Fix:** Remove the attribution everywhere. One possible replacement is 2607.13978's own sentence "Movement dynamics capture the transitions between static poses". It uses the pose-plus-transition framing but does not present it as a minimum-unit theory.

### 🔴 B2. A1-14 flexion-angle numbers in `paper_chain.md` are wrong, and one quote does not exist
- **What `paper_chain.md:1367-1368` says:** knee 2D 9.3–**23.7°**, knee 3D 14.1–**31.2°**, elbow 2D 21.5–**41.3°**, elbow 3D 16.3–**35.0°**.
- **What the PDF abstract says:** knee **9.3–21.9° (2D)** and **14.1–25.8° (3D)**. The Results section gives 3D as 14.1–25.9°. Elbow is **21.5–28.9° (2D)** and **16.3–26.0° (3D)**.
- 23.7, 31.2, 41.3 and 35.0 appear nowhere in the paper. I confirmed the abstract numbers myself.
- `paper_chain.md:1368` also quotes "depth estimation remains substantially inaccurate". That string is not in the PDF, so it is a fabricated quote.
- `reading_checklist.md:54` (item 5) still has "14.1–31.2°".
- The Assessment summary (§8, lines 380 and 515) already recorded all of this, but the fix never reached `paper_chain.md` or the checklist.

### 🟠 S1. Errors listed in the `1906.00606v1.summary.md` audit were never fixed
The 2026-09-21 rspa summary (§8) listed these problems. The file is unchanged:
- "8 cameras / 8 PCs" is credited to choreogenetics [27] at **lines 70, 105 and 337**. The preprint credits it to **Nakazawa et al. [28]**: "Using motion capture with 8 cameras and 8 PCs, Nakazawa et al. [28]…".
- Line 219 says "the one place a clustering algorithm appears at all, k-means". That is false for the journal version, which adds SLIC [63] for image segmentation.
- Line 103 says "Latin American (Ballroom, Foxtrot, Waltz)". That is the preprint's wording, and the journal corrected it.
- §8.4 is missing the ref [7] "Annemette PK" defect. §6.3 leaves out ref [62] and the Wikipedia ref [5]. §9.2 and §9.5 mix preprint and journal reference numbers.

### 🟠 S2. Checklist corrections recorded in summaries but not carried into `reading_checklist.md`
| Item | What the checklist still says | What the verified summary found |
|---|---|---|
| 2 SinMDM (l.31, E7 l.162) | "สูตรจริง" (the real formulas), "metric ที่ไม่ต้องมี corpus" (metrics that need no corpus) | The paper **has no metric formulas**: Coverage, Global Div and Local Div come from Ganimator, and SiFID comes from SinGAN. **SiFID needs a deep feature extractor.** |
| 3 DASB (l.38-42) | "§5.2 ให้สมการ bitrate" (§5.2 gives the bitrate equation); VoxtLM 200 > 1000 | The equation is **Eq. (1) in §3.2**. The VoxtLM figure is **cited from Maiti et al. 2024**, not measured by DASB. **DASB never sweeps V.** |
| 5 A1-14 (l.53-55) | "2D ~80 mm", "14.1–31.2°", "ครึ่งหนึ่งของ 36 features" (half of the 36 features) | ~80 mm is **not in the article body** (possibly in Supp. S1). The knee range is **14.1–25.8°**. **All 36** angle features use z (per `paper_chain`). |
| 7 Keyposes (l.70) | "หลักฐานว่า vocab ควรสเกลตามขนาด corpus" (evidence that vocab should scale with corpus size) | k=1000→100 is an **unablated design choice**. The paper justifies it by corpus size **and** by number of action classes (6 vs 15), so it is not scaling evidence. |
| 12 A1-22 (l.95-98) | "2024"; the FID-vs-human correlation is "ยังไม่ verified" (not yet verified) | The paper is **ICLR 2025**. **It reports no correlation number at all.** Its only FID claim is second-hand. |

`paper_chain.md:1363`, "BlazePose 'Local' ≈ 80 mm", has the same problem as item 5.

### 🟡 S3. Overreach and mixed numbering in `summaries/README.md` (verifier spot-check)
- **9 of 12 numbers checked were correct:** 146 mm; ē 50/58/108; 72–122 mm; the FSQ usage quote; L3-22 Eq. 2; Galata's 50 Monte-Carlo runs; 60 frames @ 24 fps; "within 10 %"; A1-18 has no error bars.
- **L3-22 row:** "ไม่ตกที่โมเดลใหญ่" (doesn't drop for the large model) is an overreach. The 1.7B model hit **OOM** at k ≥ 2500, so it was never tested there. Only the 360M model shows a mild rise.
- **A0-3 row:** the row says "cite RSPA only", but [43] and [60] are **preprint** numbers. The journal numbers are Lapointe & Epoque [49] and Shinozaki [78]; Carlson [41] is a journal number.
- **Venues:** SinMDM ICLR 2024, TVCG 29(8) and TPAMI 48(4) 2026 are **not in the PDFs**. Also, checklist l.45 says A0-8 is "TPAMI 2025", while l.209 says "2026 verified". Pick one.
- **Missing rows:** the index table has **no row** for `rspa.2021.0071.summary.md` or `2409.00203v1.summary.md`.

### 🟡 S4. Small issues
- **F5:** Checklist item 1 gives the Galata PDF path as `knowledge/references/…`. It is actually in `knowledge/reading_docs/`.
- **F7:** Item 15 has only one `[✅]`. The *content* condition for both ticks in the item's note is met: both versions are summarised and compared. But the legend on l.12 says the second ✅ belongs to "Cop", and `1906.00606v1.summary.md:462` already claims "เปรียบเทียบ ✅" (compared ✅). **I left the tick unchanged.** The user needs to decide which definition applies.
- **F8:** The vocabulary sizes **216 / 335 / 362** are used side by side (checklist items 3 and 9, `memory.txt`, `paper_chain`, and `2309.15505v2.summary.md:471`), and **no file defines how they relate**. The thesis needs one sentence explaining which vocabulary is which.
- **F9:** The Galata summary has no inline Thai section. It has a separate `.summary.th.md` instead, so no action is needed.
- **Note:** The Galata PDF is the author manuscript. Page numbers in citations must use the journal's pp. 398–413.

---

## Verification (second pass)
- **What Vera checked:** each of the 9 draft findings against the PDFs and the cited lines; 12 numbers in README against the PDFs; and a search for additional places the problems appear.
- **Result:** F1–F6 and F9 were **CONFIRMED**. F7 and F8 were **PARTLY** correct. I had said "both ticks satisfied", but there is only one box; I had not noticed the third number, 335.
- **Additions from Vera:** B1 has spread into the 2607 and 2409 summaries and into `paper_index_A.csv`. B2 includes the elbow ranges and a fabricated quote. S1 includes line 337. S3 is new (L3-22 overreach and A0-3 numbering).
- **Checked by me:** I re-ran the knee/elbow abstract numbers, `2607…summary.md:338` and `paper_index_A.csv:35` myself, and they match.

## Checklist status
Items 1–15 are `[✅]`, and each has a verified summary. Items 16 onward and R11 are unread, and no PDF for them exists in `reading_docs/`. **No boxes changed this run.**

## Suggested next step (for the user)
Fix B1 and B2 in `paper_chain.md`, the checklist, `paper_index_A.csv` and the 2607 summary **before any of it is cited**. Then add the two missing rows to README. To keep the scheduled task running, add the next PDF: checklist item 16 (A0-1, arXiv:2307.10894) or R11-1 (Sturm & Ben-Tal 2017, open access).

---
---

# ฉบับภาษาไทย — รายงานการตรวจสอบ 2026-09-22

**โหมด:** เปเปอร์ทั้ง 16 ฉบับใน `reading_docs/` มีสรุปแล้ว → **ไม่มีเปเปอร์ใหม่** รอบนี้จึงตรวจความถูกต้องของไฟล์ความรู้ที่มีอยู่แทน · ผู้ตรวจรอบสองคือ Vera (fact-auditor) ซึ่งเทียบกับ PDF จริงโดยตรง
**คำตัดสิน: REVISE (ต้องแก้)** พบ 2 จุดที่ร้ายแรง (blocker) · **ไม่ได้แก้ไฟล์ใดเลยนอกจากรายงานนี้** และไม่ได้เปลี่ยน checkbox

### 🔴 B1. "Static Pose / Dynamic Connection" ไม่มีต้นฉบับรองรับ
- วลีนี้**ไม่ปรากฏเลย**ใน PDF ของ A0-3 ทั้งสองฉบับ (rspa และ 1906) มีแค่ประโยค "A grammar of all possible movements can be formulated…"
- ข้ออ้างนี้ยังอยู่ใน 5 ที่:
  - `paper_chain.md:764-769` (เขียนว่า "Use this in Methods")
  - checklist ข้อ 15
  - `paper_index_A.csv:35`
  - **สรุป 2607.13978 บรรทัด 338/473/557** ซึ่งเอาไปใช้เป็นข้อโต้แย้งหลักในวิทยานิพนธ์
  - สรุป 2409.00203 บรรทัด 262
- **ต้องลบออกทุกที่ก่อนนำไปอ้าง**

### 🔴 B2. ตัวเลขมุมเข่า/ศอกของ A1-14 ใน `paper_chain.md` ผิด
- **`paper_chain.md` เขียนว่า:** เข่า 3D 14.1–31.2° และศอก 21.5–41.3° / 16.3–35.0°
- **PDF จริง:** เข่า **2D 9.3–21.9°, 3D 14.1–25.8°** · ศอก **2D 21.5–28.9°, 3D 16.3–26.0°**
- คำพูดที่อ้างว่า "depth estimation remains substantially inaccurate" **ไม่มีอยู่ในเปเปอร์**
- checklist ข้อ 5 ก็ยังใช้ตัวเลขผิดนี้อยู่

### 🟠 S1. ข้อผิดพลาดในสรุป 1906.00606v1 ที่รอบ 2026-09-21 ชี้ไว้ ยังไม่ได้แก้
- บรรทัด 70/105/337 ยกตัวเลข "8 กล้อง / 8 PC" ให้ choreogenetics แต่ที่ถูกเป็นของ **Nakazawa [28]**
- บรรทัด 219 เขียนว่า k-means เป็น clustering ตัวเดียว ซึ่งผิดสำหรับฉบับวารสาร (มี SLIC ด้วย)
- บรรทัด 103 ยังใช้คำว่า "Latin American" ตามฉบับ preprint
- ปนเลข reference ของ preprint กับฉบับวารสาร

### 🟠 S2. คำแก้ที่บันทึกไว้ในสรุปแต่ยังไม่ได้แก้ใน checklist
- **ข้อ 2 SinMDM:** เปเปอร์ไม่มีสูตร metric (ยืมมาจาก Ganimator/SinGAN) และ SiFID ต้องใช้ deep encoder
- **ข้อ 3 DASB:** สมการ bitrate อยู่ใน §3.2 ไม่ใช่ §5.2 · ตัวเลข VoxtLM อ้างมาจาก Maiti 2024 ไม่ได้วัดเอง · DASB ไม่เคย sweep V
- **ข้อ 5:** ค่า "2D ~80 mm" ไม่มีในเนื้อความ · ช่วงเข่าที่ถูกคือ 14.1–25.8° · feature มุมใช้ z ทั้ง 36 ตัว ไม่ใช่ครึ่งเดียว
- **ข้อ 7 Keyposes:** k=1000→100 เป็นการเลือกออกแบบที่ไม่ได้ทำ ablation จึงไม่ใช่หลักฐานเรื่องการสเกลตาม corpus
- **ข้อ 12:** เปเปอร์เป็น ICLR 2025 และไม่มีตัวเลข correlation ระหว่าง FID กับการประเมินของมนุษย์เลย

### 🟡 S3–S4. ข้อย่อย
- **README:** แถว L3-22 เคลมเกินจริง (โมเดล 1.7B เจอ OOM จึงไม่เคยทดสอบที่ k ≥ 2500) · แถว A0-3 ใช้เลข reference ของ preprint · ไม่มีแถวของ rspa และ 2409.00203 · venue หลายรายการไม่ได้ระบุไว้ใน PDF
- **Checklist ข้อ 1:** path ของ PDF Galata ผิด (ไฟล์จริงอยู่ใน `reading_docs/`)
- **Checklist ข้อ 15:** มี ✅ ช่องเดียว เงื่อนไขของทั้งสองช่องครบแล้ว แต่ legend กำหนดให้ ✅ ช่องที่สองเป็นของ Cop → **ไม่ได้ติ๊กเพิ่ม ให้ผู้ใช้ตัดสินใจ**
- **ขนาด vocabulary:** มีทั้ง 216 / 335 / 362 แต่ไม่มีไฟล์ไหนอธิบายว่าเกี่ยวกันอย่างไร

### การตรวจรอบสอง
- Vera ยืนยัน F1–F6 และ F9 ส่วน F7/F8 ถูกบางส่วน
- Vera พบเพิ่มว่าข้อ B1 ลามไปในสรุป 2607 และ 2409 รวมถึง csv, พบตัวเลขศอกที่ผิดกับ quote ที่ไม่มีอยู่จริง, และพบปัญหาใน README
- ตัวเลขใน README ที่สุ่มตรวจ 12 จุด ถูก 9 จุด

### ขั้นต่อไป
แก้ B1 และ B2 ก่อนนำไปอ้าง → เพิ่มแถวที่ขาดใน README → ใส่ PDF ใหม่ (เช่น checklist ข้อ 16 A0-1 หรือ R11-1 Sturm & Ben-Tal 2017)
