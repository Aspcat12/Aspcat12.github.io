# สรุปเปเปอร์ → metric อะไรบ้าง (ดัชนีของโฟลเดอร์นี้)

ตารางนี้ตอบคำถามเดียว: **"สรุปเปเปอร์ฉบับไหน ให้ metric อะไรกับเรา และเข้าชั้นไหน"**
ใช้คู่กับ:
- `docs/ADVISOR_METRICS_2026-09.md` — เอกสารคุยอาจารย์ (แบ่งชั้นที่ 1 / ชั้นที่ 2 + MediaPipe→SMPL-X)
- `knowledge/paper_notes/evaluation_methods.md` — แผนประเมินหลัก + reference ที่ verify แล้ว

**ชั้นที่ 1 = intrinsic (วัดตัวโมเดล: LSTM vs Transformer)** ·
**ชั้นที่ 2 = extrinsic (วัดท่าเต้นที่สร้างออกมา)** · **—** = ไม่ใช่เรื่อง metric

| ไฟล์สรุป | เปเปอร์ | ให้ metric / ของแถมอะไรกับเรา | ชั้น |
|---|---|---|---|
| `2407.13623v3.summary.md` | **A1-18** Tao et al., *Scaling Laws with Vocabulary*, NeurIPS 2024 | ⭐ **`L_u` unigram-normalized loss** — ตัวเดียวที่ทำให้เทียบ perplexity ข้ามขนาด vocabulary ได้ (§A.10: raw loss อ่านเครื่องหมายกลับหลัง) · "ข้อมูลน้อย → vocabulary ควรเล็กลง เป็นกลไกกัน overfit" · ยอมรับเองว่าไม่มี error bar | **1** |
| `2509.05359v1.summary.md` | **L3-22** Labrak et al., *Discrete Unit Representations in Speech LM Pre-training*, TSD 2025 | **usage perplexity Eq. (2)** `exp(−Σp log p)/k × 100` = สุขภาพของคลังคำ (คนละตัวกับ support-size!) · หลักฐาน k-sweep: `k ≤ 1000` ดี, `k ≥ 2500` ตกหน้าผาที่โมเดลเล็ก, ไม่ตกที่โมเดลใหญ่ · pipeline รูปทรงเดียวกับเราเป๊ะ | **1** |
| `2309.15505v2.summary.md` | **FSQ** Mentzer et al., 2023 | **Codebook Usage** = *"the fraction of the codewords that are used at least once"* (นิยามของ support-size ที่เราใช้อยู่) · หลักฐานว่า VQ codebook ตายเมื่อ codebook ใหญ่ | **1** |
| `Galata_Johnson_Hogg_2001_VLMM_Behaviour_CVIU.summary.md` (+ `.th.md`) | **A1-21** Galata, Johnson & Hogg, VLMM, CVIU 2001 | **baseline คลาสสิกของสายนี้โดยตรง** · **`E_T` = mean prediction error เทียบกับ horizon `T`** ด้วย Monte-Carlo 50 ครั้ง/เฟรม ⬅️ **นี่คือ rollout-length curve ที่เราจะทำ มีคนทำมาก่อนแล้ว อ้างได้** | **1 + 2** |
| `2302.05905v2.summary.md` | **A1-12** Raab et al., *SinMDM*, ICLR 2024 | ⭐ **ชุด metric หลักของเรา**: Coverage / Global Div / Local Div / Inter Div / Intra Div Diff · หลักการ "fidelity คู่ diversity เสมอ" · **คำเตือน: ไม่มีสูตรในเปเปอร์ ยืมจาก Ganimator → ต้องอ่าน Ganimator ก่อนตีพิมพ์เลข** · SiFID ใช้ไม่ได้ (ต้องมี deep encoder) · Harmonic Mean เทียบข้ามเปเปอร์ไม่ได้ | **2** |
| `2111.12159v1.summary.md` | **A1-16** Aristidou et al., *Rhythm is a Dancer*, IEEE TVCG 29(8) 2023 | **chi-square motion signature** + 🚨 คำเตือนว่ามันเป็น **conformity metric ไม่ใช่ quality metric** (mocap จริงแพ้ generator ใน Fig. 12) → ใช้เป็น *control metric* คู่กับ fidelity และต้องมีแถวข้อมูลจริง · สถาปัตยกรรมใกล้เราที่สุด (pose→motif→choreography) | **2** |
| `2012.04731v4.summary.md` | **A1-17** Kiciroglu et al., *Keyposes*, 3DV 2022 | **PSKL (KL สองทิศ)** เป็น dynamics-complexity check · **diversity = mean pairwise L2** · MPJPE ที่เขา *รายงานแต่ไม่เชื่อ* สำหรับงาน long-term · **MOAC = ตัวอย่างของ "เสนอทั้งกลไกและ metric ที่ตัวเองชนะ"** · เหตุผลเชิงออกแบบ k=1000 บน corpus ใหญ่ / k=100 บน corpus เล็ก | **1 + 2** |
| `2607.13978v1.summary.md` | **L3-5** *Music-to-Dance via Atomic Movements* | FID_k/FID_g, Div_k/Div_g, BAS, R-precision(self-proposed), MultiModality · ⚠️ **ตัวอย่างของสิ่งที่เราต้องไม่ทำ**: อ้าง "perceptual naturalness" โดยไม่มี human eval เลย, ใช้คำว่า significant โดยไม่มีสถิติ, R-precision ที่ implement ตามที่เขียนไม่ได้, stage 2 เป็น **retrieval** แต่ยังรายงาน FID | **2** |
| `2407.02272v2.summary.md` | **A1-22** *Aligning Human Motion Generation with Human Perceptions* (MotionCritic) | **โปรโตคอล human study ที่ระบุครบ** (60 เฟรม @ 24 fps ≈ 2.5 วิ) — ใช้ได้ฟรีไม่ต้องมี torch · ⚠️ **ตัวโมเดลใช้ไม่ได้: input contract เป็น SMPL** → เป็นสะพานเชื่อมไปหัวข้อ MediaPipe→SMPL-X | **2** |
| `Assessment_of_monocular_human_pose_estimation_mode.summary.md` | **A1-14** *Assessment of monocular HPE models for clinical movement analysis* | ⭐ **งบความคลาดเคลื่อนของ input เราเอง**: BlazePose 'World' 'Heavy' = 3D MPJPE **146 มม.**, ē_z **108** vs ē_x 50 / ē_y 58 (ลึกผิด ~2 เท่า), 2D range 72–122 มม. · หลักฐานสนับสนุน z-zeroed · **ฐานของหัวข้อ SMPL-X ทั้งหมด** | **2 / SMPL-X** |
| `2406.14294v4.summary.md` | **A0-9** *DASB — Discrete Audio and Speech Benchmark* | แบบแผนของ **benchmark ที่วัด token โดยไม่ผ่าน decoder** + ablation เรื่องจำนวน codebook / ขนาดข้อมูล / การ init embedding · แนวคิด "วัด token เอง ไม่ใช่วัดปลายทางอย่างเดียว" | **1** |
| `2502.06490v4.summary.md` | **A0-8** *Recent Advances in Discrete Speech Tokens: A Review*, IEEE TPAMI 48(4) 2026 | taxonomy ของ tokenizer + **§V เรื่อง length reduction (dedup vs BPE)** ⬅️ เกี่ยวโดยตรงกับการ collapse ท่าซ้ำติดกันของเรา (dedup ทิ้งข้อมูล duration) | **1** |
| `1906.00606v1.summary.md` | **A0-3** Joshi & Jadhav, *Extensive Review of Computational Dance Automation*, arXiv:1906.00606v1 (2019) — **ฉบับตีพิมพ์: Joshi & Chakrabarty, Proc. R. Soc. A 477:20210071 (2021)** | **ไม่ให้ metric เลย** (ทั้งเปเปอร์มีตัวเลขผลลัพธ์ตัวเดียว: "within 10 % of optimal" ที่อ้างต่อมา) · ค่าอยู่ที่ **taxonomy 6 ด้านของวงการ** → ใช้วาง position งานเรา และ ⭐ **ข้ออ้าง white space**: ในแผนที่ของวงการเอง คลังคำท่าเต้นที่ได้จาก clustering **ไม่มีช่อง** — ทุก vocabulary ในนั้นมนุษย์ประกาศเอง ([43] 4 ท่า, [60] 60 หน่วย, [41] movement catalyst 13 ค่า) · ⚠️ **อ้าง RSPA เท่านั้น** (preprint ไม่มี deep learning เลย + ผิดหลายจุด) | — |
| `matrix_profile_vi.summary.md` | Yeh, Kavantzas & Keogh, *Matrix Profile VI*, 2017 | **motif discovery หลายมิติ + mSTAMP/MDL เลือกมิติที่เกี่ยว** · ไม่ใช่ metric โดยตรง แต่เป็นวิธีหา "ท่าซ้ำ" ที่เป็น ground truth ของ Coverage ได้ | — |

---

## ช่องว่างที่ยังไม่มีเปเปอร์รองรับในโฟลเดอร์นี้

| ช่องว่าง | ต้องอ่านอะไร | ทำไมสำคัญ |
|---|---|---|
| **สูตรจริงของ Coverage / Global Div / Local Div** | **Ganimator** (Li et al. 2022) | SinMDM ไม่มีสูตร ยืมมา → เลขใน `eval_generation.py` ยังตีพิมพ์ไม่ได้ |
| **สูตรจริงของ `L_u`** | **Roh, Oh & Lee 2020, arXiv:2011.13220** (สั้น) | ก่อน implement ใน `train_lstm.py` |
| **memorization / n-gram overlap** | ยังไม่มีเปเปอร์ในคลัง | คำถาม "ก็อปมาหรือเปล่า" ตอบไม่ได้ |
| **decoding strategy** | **A1-28** Holtzman et al. ICLR 2020 (ยังไม่มีสรุป) | `generate.py` ใช้ softmax+multinomial เปล่า ๆ |
| **exposure bias** | **A1-27** Bengio et al. NeurIPS 2015 (ยังไม่มีสรุป) | `--n 120` คือเคสตำรา |
| **SMPL-X fitting** | **Pavlakos et al. CVPR 2019** + SMPLify-X / VPoser | §3 ของ `docs/ADVISOR_METRICS_2026-09.md` ยังเป็น `[?]` ทั้งหมด |
