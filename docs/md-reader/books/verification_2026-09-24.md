# Verification note — 2026-09-24 (scheduled `read-a-paper`, รอบที่ต่อจากรอบที่ติด usage limit)

## ⚠️ เกิดอะไรขึ้นในรอบนี้ (อ่านก่อน)

- ตอนเริ่มรอบ (ประมาณ 09:0x) ไดเรกทอรี `summaries/` **ยังไม่มี** สรุปของ `jcmsSturmBenTal-finaltext.pdf` → รอบนี้จึงเลือกเปเปอร์นี้ (unread ที่เก่าสุด สร้างไฟล์ 2026-09-23 19:47:14) แล้วอ่าน สรุป และรัน verification อิสระจนจบ
- ตอนจะบันทึก พบว่า **`jcmsSturmBenTal-finaltext.summary.md` ถูกสร้างเมื่อ 09:13:28** โดย **run อื่นของ task เดียวกันที่ทำงานขนานกัน** (น่าจะเป็น session ที่ติด usage limit แล้วกลับมาทำต่อ) — ตอนตรวจ §13 Verification ของไฟล์นั้นยังเป็น *"(รอผลจาก verification subagent)"*
- ตามกฎ STEP 6 (**ห้าม overwrite สรุปที่มีอยู่**) รอบนี้ **ไม่แตะไฟล์นั้น** · บันทึกผลของรอบนี้ไว้ในไฟล์นี้แทน: (ก) ข้อผิดพลาดที่พบในไฟล์ของ run คู่ขนาน โดยเทียบกับผลที่ผ่าน verification แล้วของรอบนี้ (ข) สรุปฉบับอิสระทั้งฉบับ (ภาคผนวก) เพื่อให้เทียบกันได้
- **บทเรียน (ซ้ำกับ `verification_2026-09-23.md`):** list `summaries/` ใหม่อีกรอบ **ทันทีก่อนเขียน** ไม่ใช่แค่ตอนเริ่ม และถ้ามี run ค้างจาก usage limit ควรเช็คก่อนว่า run เดิมยังทำงานอยู่ไหม

---

## ส่วนที่ 1 — ข้อผิดพลาดในไฟล์ของ run คู่ขนาน (`jcmsSturmBenTal-finaltext.summary.md` ณ 09:13:28)

ตรวจเทียบกับ PDF ต้นฉบับ + ผลของ verifier อิสระ (`fact-auditor`) ของรอบนี้ · **ไม่ได้แก้ไฟล์นั้น** — ให้ run เจ้าของหรือผู้ใช้เป็นคนแก้

| # | ระดับ | บรรทัด | ไฟล์นั้นเขียนว่า | ต้นฉบับจริง |
|---|---|---|---|---|
| **V1** | 🔴 | 135 | *"Ben-Tal แต่งต่อ **seed ขั้น 3** เองสองแบบ (Fig. 12–13)"* | caption ของ Fig. 12–13 พิมพ์ seed ขั้น 3 (`G 2 E G E < G F 2 \|`) จริง **แต่ caption ผิด** — เนื้อความหน้า 16 พูดถึง *"our 'nefarious' initialisation above"*, *"the dyads"*, *"the three-dyad idea"* ซึ่ง seed ขั้น 3 ไม่มี dyad และ **verifier render ห้องแรกของ Fig. 13 ที่ 400 dpi แล้วเห็นเป็น seed ขั้น 2 `[ G F ] 2 E G E < G [ E F ] 2` เป๊ะ** → ต้องเขียนว่าเป็น continuation ของ seed ขั้น 2 และบันทึก caption ไว้ในทะเบียนข้อผิดพลาด |
| **V2** | 🔴 | 198 | *"คำสั่ง `sample_rnn.py` พร้อม `--rng_seed` **พิมพ์ไว้ครบ**ในข้อ 4 → ข้อ 4 **re-run ได้จริง**"* | §3.4 มีคำสั่ง 4 คำสั่ง — **2 คำสั่งแรกไม่มี `--rng_seed`** (หน้า 17, 18) มีแค่คำสั่งที่ 3 (`3213`, หน้า 19) และที่ 4 (`14`, หน้า 20) และ seed เหล่านี้ถูกเลือก **หลังจาก** *"We actually tried several random seeds until the model produced material that we found acceptable enough"* · นอกจากนี้ทุกคำสั่งใช้ seed ที่ **แก้ด้วยมือแล้ว** (§3.4) → **re-run ได้บางส่วนเท่านั้น** |
| **V3** | 🟠 | 54 | ใส่ "Eck & Lapamle 2008" โดยไม่มีหมายเหตุ | เปเปอร์สะกดแบบนี้จริง แต่น่าจะเป็น **Lapalme** และ Mozer (1994) ใน reference ระบุ *Cognitive Science* 6(2&3) ซึ่งน่าจะเป็น ***Connection Science*** (เป็นความรู้ภายนอก — **ตรวจก่อนลง bibliography**) |
| **V4** | 🟠 | — (ไม่มี) | ไม่มีทะเบียนข้อผิดพลาดของเปเปอร์ | ขาด: (ก) **"The Mal's Copporim"** — หน้า 9/22 ว่าเป็น output ของ **char-rnn** แต่รายการผลงานหน้า 27 ข้อ 21 ว่า *"by folk-rnn (2015)"* (ข) caption Table 1 *"research applying recurrent neural networks"* แต่มีแถว WaveNet ที่หน้า 4 บอกเองว่า *"do not use recurrent connections"* (ค) §1 สัญญา *"'nefarious' initialisations, e.g., dyads, atonality, etc."* แต่ §3.3 **ไม่ได้ทดสอบ atonality** (ง) caption Fig. 12–13 (V1) |
| **V5** | 🟡 | 220 | *"R11-1: ติ๊ก `[✅]` แล้ว"* | ณ 09:13 `reading_checklist.md` บรรทัด 173 ยังเป็น `[ ]` — ข้อความในสรุปนำหน้าการกระทำจริง (ดูส่วนที่ 3 ว่ารอบนี้ทำอะไรกับ tick) |

**สิ่งที่ไฟล์นั้นทำถูกและตรงกับรอบนี้ (ยืนยันอิสระ):** 23,635 / 30,000 · 3,322 / 1,867 · 43.4% / 68.4% · ABC errors รวม 110 · "one in five" · ไม่เรียก folk-rnn ว่า LSTM · E11 ไม่ติ๊ก (เป็นการทดลอง) · ยอมรับว่า venue/DOI ไม่อยู่ใน PDF · Table 1 = 11 งาน

## ส่วนที่ 2 — สิ่งที่ฉบับอิสระของรอบนี้มีเพิ่ม (อยู่ในภาคผนวก)
- ตัวแปรกวนของ nefarious ขั้น 1→2: จังหวะเท่ากัน (8 หน่วย 1/8) แต่เปลี่ยน token 3 จุดพร้อมกัน → การโทษ `>` โดยเฉพาะใน §4 มีตัวแปรกวน
- ข้อสังเกตต่อโค้ดของเรา: **`src/generate.py` ไม่ตั้ง RNG seed เลย** (`np.random.randint` บรรทัด 170, `torch.multinomial` บรรทัด 95) → ควรเพิ่ม `--rng-seed` ก่อน E8/E9/E11
- แบบสอบถาม 4 ข้อของ Session Book เป็น template ของ expert study · ข้อ 4 = คำถาม memorization (ช่องว่างใน README)

## ส่วนที่ 3 — การแก้ `reading_checklist.md`
ณ 09:15 บรรทัด 173 (R11-1) ยังเป็น `[ ]` → รอบนี้เปลี่ยนเป็น `[✅]` (ช่องแรก = team read and verify — อ่านครบ + ผ่าน verifier อิสระ) **ไม่แตะข้อความอื่นในไฟล์** · E11 **ไม่ติ๊ก** (เป็นการทดลองที่ยังไม่ได้ทำ)

---

# ภาคผนวก — สรุปฉบับอิสระของรอบนี้ (ผ่าน verification แล้ว)

# L3-36 · Sturm & Ben-Tal (2017) — Taking the Models back to Music Practice: Evaluating Generative Transcription Models built using Deep Learning

> **ไฟล์:** `knowledge/reading_docs/jcmsSturmBenTal-finaltext.pdf` (29 หน้า, pdfTeX, สร้าง 2017-08-19)
> **ผู้แต่ง:** Bob L. Sturm¹ (Centre for Digital Music, Queen Mary University of London) · Oded Ben-Tal² (Dept. of Performing Arts, Kingston University, UK)
> **Venue ตาม checklist:** *J. Creative Music Systems* 2(1), DOI 10.5920/jcms.2017.09 — ⚠️ **PDF นี้เป็น "final text" ของผู้แต่ง ไม่มีหัววารสาร เลขเล่ม หรือ DOI ในไฟล์เลย** → ข้อมูล venue/DOI มาจาก checklist เท่านั้น **ยังไม่ได้ยืนยันจากต้นฉบับ** ตรวจก่อนลง bibliography
> **ระดับความน่าเชื่อถือ (`reading_guide.md`):** วารสารเฉพาะทาง open access ขนาดเล็ก (peer-reviewed) — **ไม่ได้เปิดตรวจ SJR/CORE ในรอบนี้** ถือว่า **ต่ำกว่า** venue ส่วนใหญ่ในคลัง (TOG/ICLR/TPAMI) · เนื้อหาเป็น **บทความเชิงวิธีประเมิน + position** มากกว่าการทดลองควบคุม
> **โค้ด/ข้อมูล:** เปิดทั้งคู่ — *"Our datasets and software are open and available at https://github.com/IraKorshunova/folk-rnn"* (abstract)
> **วิธีอ่าน:** Three-Pass (Keshav) — pass 1 → pass 2 ครบทุกหน้า (§1–§5 + references) + ดู Fig. 1–3 จากภาพที่ render (ค่าบนกราฟไม่อยู่ใน text layer) + ตรวจผลรวมของ Table 2–3 ด้วยมือ · pass 3 เฉพาะส่วนที่เกี่ยวกับเรา (§3.1, §3.3, §4)
> **เขียน:** 2026-09-24 · ผ่าน verification อิสระ (ดู §12)

---

## ⚠️ อ่านตรงนี้ก่อน — 8 ข้อที่เปลี่ยนวิธีใช้เปเปอร์นี้

1. **กรอบ 5 ระดับใน checklist ถูกต้องตามต้นฉบับ** — abstract ระบุ 5 วิธีประเมินตรงตามที่ checklist R11-1 เขียน: (1) population level (2) practice level (3) "nefarious tester" (4) assisted composition (5) นำไปให้ผู้ปฏิบัติจริง. ⚠️ **แต่ checklist เรียกว่า "5 ระดับ" — เปเปอร์เรียกว่า "five different ways" ไม่ได้อ้างว่าเป็นลำดับชั้น** และ §4 ยอมรับเองว่า *"the approaches to evaluation we use are by and large unsystematic"* → ถ้าเราใช้เป็นโครงบทประเมินผล **ต้องเขียนว่า "ดัดแปลงจาก" ไม่ใช่ "ตามกรอบมาตรฐานของ"**

2. **ตัวเลข population ที่ถูกต้อง: เทรน 23,635 ชิ้น / สร้าง 30,000 ชิ้น** (caption Fig. 1) — abstract เขียน *"over 23,000"*. checklist เขียน "23,000" → **ใช้ 23,635**

3. **⭐ ของที่ใช้ได้ทันทีที่สุดสำหรับเรา: "measure-token sequence" = ตัววัดโครงสร้าง + ตัววัดการหดตัวของความหลากหลาย** (§3.1, Table 2–3) — ตัดทุกอย่างทิ้ง เหลือแต่ลำดับของเส้นกั้นห้อง แล้วนับว่ามีกี่แบบ:
   - **จำนวนแบบที่ไม่ซ้ำ: เทรน 3,322 / สร้าง 1,867** (ทั้งที่ชุดสร้างใหญ่กว่า)
   - **15 แบบที่พบบ่อยสุดครอบคลุม: เทรน 10,257/23,635 = 43.4% / สร้าง 20,513/30,000 = 68.4%** (เปเปอร์ให้แค่จำนวน — **เปอร์เซ็นต์เราคำนวณเอง** · ตรวจผลรวม Table 2–3 ด้วยมือแล้ว ตรงกับเนื้อความทั้งคู่)
   - → **โมเดลรวมศูนย์ไปที่โครงสร้างยอดนิยม** = อาการ mode concentration ที่วัดได้โดยไม่ต้องมี feature extractor
   - **analog ของเรา:** ลำดับของ "segment boundary" หรือ run-length pattern ของ token → นับ unique + top-15 share เทียบ training vs generated **ทำได้ใน `eval_generation.py` ภายในชั่วโมงเดียว**

4. **⭐ Nefarious testing (§3.3) คือ E11 ของเราพอดี — และให้ "บันได 3 ขั้น" เป็น protocol สำเร็จรูป:** ป้อน seed ที่ห่างจากข้อมูลเทรนมากที่สุดก่อน แล้วค่อย ๆ ทำให้ปกติขึ้น:
   | ขั้น | seed | ผลที่โมเดลทำ |
   |---|---|---|
   | 1 | dyad ไม่ประสาน + ใช้ `>` แบบผิดธรรมเนียม | **ไม่มีห้องไหนนับจังหวะถูกเลย** (3/8, สลับ 3/4–2/4, มี 5/8) ไม่ซ้ำ/แปรไอเดียตั้งต้น · ข้อดีเดียว: จบด้วย cadence (*"though it is completely unexpected"*) |
   | 2 | ห้องเดียวกันแต่เขียนแบบปกติ (`<`) ยังมี dyad | **นับจังหวะถูกทุกห้อง** แต่ยังเมินไอเดียตั้งต้น "aimless" หลายห้อง · จังหวะสอดคล้องกับห้องแรกขึ้นเล็กน้อยแต่ลืมหลัง b. 8 · มีการซ้ำ-แปรบ้าง (bb. 9, 13) |
   | 3 | ตัด dyad ออก | ฟอร์ม AABB + cadence ถูกตำแหน่ง แต่ **ยังไม่จับไอเดียจังหวะของ seed** |
   ข้อสรุปของเขา: ความสามารถนับห้อง/ซ้ำ-แปร/สร้างฟอร์ม **"true only in a very limited context"** — ต้องให้ seed คล้ายข้อมูลเทรนทั้ง pitch **และ** rhythm. **สิ่งนี้ไม่ปรากฏเลยใน 30,000 ชิ้นที่สุ่มแบบไม่มี seed** → หลักฐานว่า population stats อย่างเดียว **มองไม่เห็น** ความเปราะบางนี้

5. **🚨 จุดอ่อนเชิงวิธีของ nefarious test ที่เราต้องไม่ลอก: n = 1 ต่อเงื่อนไข.** เขาเขียนเอง *"many outputs can be generated by changing the random seed, but we leave it to the default in every case"* → แต่ละขั้นมีตัวอย่างเดียว และขั้น 1→2 เปลี่ยน token 3 จุดพร้อมกัน (ตัด `/2` ออก, `>` หลัง G → `<` ระหว่าง E กับ G, dyad `[E F] 4` → `[E F] 2`) — **จังหวะจริงเท่าเดิม** (ทั้งสองห้องรวม 8 หน่วย 1/8 ตามที่เปเปอร์เรียกว่า *"an equivalent bar, but expressed in a more conventional way"*) ดังนั้นการออกแบบ "เขียนต่างแต่ดนตรีเท่ากัน" ถูกต้อง **แต่การโทษ token `>` โดยเฉพาะใน §4 (*"an uncommon use of the token > dramatically confuses the model"*) มีตัวแปรกวน** เพราะ `/2` และค่า duration เปลี่ยนไปพร้อมกัน → **เวอร์ชันของเรา: หลาย RNG seed ต่อเงื่อนไข + เปลี่ยนทีละปัจจัย**

6. **🚨 `generate.py` ของเราทำซ้ำไม่ได้ในจุดที่เปเปอร์นี้ (บางส่วน) ทำได้** — ใน §3.4 **2 จาก 4 คำสั่ง** ระบุ `--rng_seed 3213` (หน้า 19) และ `--rng_seed 14` (หน้า 20) · ⚠️ seed ที่พิมพ์ไว้เป็นตัวที่ **เลือกหลัง curation** (*"We actually tried several random seeds until the model produced material that we found acceptable enough"*) และไม่ได้เผยแพร่การค้น seed ทั้งหมด · ส่วน `src/generate.py` ของเรา **ไม่มีการตั้ง seed เลย** (ไม่มี `torch.manual_seed` / `np.random.seed`; seed window ก็สุ่มด้วย `np.random.randint` ที่บรรทัด 170 และ sampling ด้วย `torch.multinomial` ที่บรรทัด 95) → **เพิ่ม `--rng-seed` ก่อนทำ E8/E9/E11** ไม่งั้นรายงานผลเป็นตัวเลขเดียวที่ reproduce ไม่ได้

7. **อุณหภูมิสูง → output ผิดไวยากรณ์ (§4, Fig. 15)** — sampling ที่ temperature สูงให้ ABC ที่ผิด: `]` ไม่มีคู่, `<s>` โผล่กลางลำดับ, `(2` ผิด, นับห้องผิด. **เปเปอร์ไม่ระบุค่า temperature ที่ใช้ทั้งในตัวอย่างนี้และใน 30,000 ชิ้นหลัก** → อ้างได้แค่เชิงคุณภาพ ใช้คู่กับ Holtzman (R11-2) ใน E8 · เขามองเป็น **แหล่งไอเดียเชิงสร้างสรรค์** ไม่ใช่ความล้มเหลว

8. **เปเปอร์ปฏิเสธ "music Turing test" อย่างมีเหตุผล (§4, อ้าง Ariza 2009)** — *"any significance of having accomplished such 'fooling' is ultimately weak and uninformative: Who was fooled, and why?"* + ถามกลับว่าทำไมห้าม cherry-pick output ของเครื่องในเมื่อคนก็ cherry-pick ผลงานมนุษย์ → **ใช้เป็นเหตุผลได้ตรง ๆ ว่าทำไม expert study ของเราถามเรื่อง "ใช้ได้ไหม/ผิดตรงไหน" แทน "แยกออกไหมว่าเครื่องทำ"** และ 4 คำถามใน §3.5 (ดู §6.5) คือแบบสอบถามสำเร็จรูป

---

## 1. Five Cs (`reading_guide.md`, pass 1)

| C | คำตอบ |
|---|---|
| **Category** | **บทความเชิงวิธีประเมิน (evaluation methodology) ของระบบที่มีอยู่แล้ว** — ไม่เสนอโมเดลใหม่ ใช้ folk-rnn ที่ตีพิมพ์ใน Sturm et al. (2016) แล้วประเมิน 5 วิธี + position ว่าควรประเมิน generative model ด้วยการ "เอากลับไปสู่ practice" |
| **Context** | ฐานทางความคิด: **Wagstaff (2012) "Machine learning that matters"** (แรงจูงใจหลัก) · **Ariza (2009)** (วิจารณ์ Turing test) · **Loughran & O'Neill (2016)** (เขาบอกว่าไม่ได้สนใจวัด "creativity") · **Pearce, Meredith & Wiggins (2002)** (การใช้ระบบเป็นส่วนหนึ่งของการประพันธ์) · งานก่อนหน้าของตัวเอง **Sturm, Santos, Ben-Tal & Korshunova (2016)**, *Proc. 1st Conf. Computer Simulation of Musical Creativity*, Huddersfield (ตามที่เปเปอร์อ้าง · การจับคู่กับ L3-35 / R11-4 / arXiv:1604.08723 มาจาก checklist — **รายละเอียดโมเดลอยู่ที่นั่น ไม่ใช่ที่นี่**) · related work RNN ดนตรี: Colombo et al. 2016, Choi et al. 2016, Magenta, Jaques et al. 2017 (RL tuning), van den Oord et al. 2016 (WaveNet) + ตาราง 11 งานเก่า (Table 1) |
| **Correctness** | สมมติฐานหลัก — "สถิติ population เป็นแค่ sanity check; ต้องดูผลงานทีละชิ้นและทดสอบที่ขอบ" — **สมเหตุผลและ nefarious test พิสูจน์ด้วยตัวอย่างว่า population stats พลาดอะไรไป**. จุดอ่อน: (ก) **ไม่มีสถิติทดสอบเลย** การเทียบ population เป็นกราฟล้วน ไม่มี divergence / p-value (ข) ผู้วิเคราะห์ทีละชิ้นคือ **ผู้สร้างโมเดลเอง** (ค) nefarious test **n = 1** และเปลี่ยนหลายปัจจัยพร้อมกัน (ง) feedback จากผู้ปฏิบัติ **เลือกเองโดยสมัครใจ** (comment ใน forum, นักดนตรีที่เชิญมา) |
| **Contributions** | (1) ตัวอย่างการประเมินหลายมุมของ generative symbolic model ที่ **ไม่มี ground truth** (2) แนวคิด **"nefarious testing"** (3) ตัวอย่างการใช้โมเดลในการประพันธ์แบบวนรอบ (seed → คัด → แก้ → seed ใหม่) พร้อมคำสั่งจริงและ RNG seed (4) นำผลกลับไปสู่ชุมชนผู้ปฏิบัติจริง (session book 3,000 ชิ้น, คอนเสิร์ต, workshop) (5) ตาราง survey ว่างาน RNN ดนตรีก่อนหน้าประเมินอย่างไร (Table 1) |
| **Clarity** | **สูง อ่านง่าย** ตัวอย่างเป็นรูปธรรมพร้อม ABC ต้นฉบับและลิงก์เสียง · หักคะแนน: (ก) ตัวอย่างเสียงเกือบทั้งหมดอยู่หลังลิงก์ `goo.gl` (Google หยุดบริการนี้ — **สถานะลิงก์ยังไม่ได้ทดสอบในรอบนี้**) (ข) **caption ของ Fig. 12–13 ขัดกับเนื้อความ** (ดู §9) (ค) ไม่ระบุ temperature / การตั้งค่า sampling ของ 30,000 ชิ้น (ง) รายการผลงานที่ 10 มีลิงก์ YouTube ซ้ำตัวเดียวกันสองครั้ง |

---

## 2. ตารางสกัดของ อ.Proadpran

| ช่อง | สรุป |
|---|---|
| **Motivation** | โมเดล generative ของดนตรีถูกประเมินแบบหยาบ — Table 1 แสดงว่างานส่วนใหญ่ใช้แค่ *"visual inspection"* หรือ *"self-auditioning"* · ผู้เขียนต้องการรู้ว่า folk-rnn **"learned" อะไรจริง** และ **มีประโยชน์ใน music practice แค่ไหน** — ไม่ใช่วัด "creativity" (§1) |
| **Research Question** | (1) *"determining what it is actually learning to do"* (2) *"determining how useful it is in music practice"* (3) *"how to make it more usable for music practice"* (§1, คำต่อคำ) |
| **Proposed Method** | ประเมิน folk-rnn 5 วิธี: สถิติ population · วิเคราะห์ 5 ชิ้นแบบครูสอนแต่งเพลง · nefarious seed · ประพันธ์ร่วมแบบวนรอบ · feedback จากชุมชนและนักดนตรีอาชีพ |
| **Evaluation** | เชิงคุณภาพเกือบทั้งหมด · เชิงปริมาณมีเฉพาะ §3.1 (การกระจาย metre / mode / ความยาว / pitch / pitch class, จำนวน measure-token sequence, จำนวน ABC error) — **ไม่มีการทดสอบนัยสำคัญ** |
| **Contribution** | ต่อ CS: ชี้ว่า **population stats ไม่พอ** และต้องประเมินที่ขอบการกระจาย + ในบริบทใช้งานจริง · ต่อวงกว้าง: นำ generative model เข้าไปในชุมชนดนตรีพื้นบ้าน, คอนเสิร์ต, สื่อ และเปิดประเด็นจริยธรรม (เสียงคัดค้านของ user "Ergo") |

---

## 3. ปัญหา แรงจูงใจ และตำแหน่ง (§1–§2)

- folk-rnn = **โมเดล generative ระดับ token บน ABC notation** (*"models transcription data one token at a time in a transcription-segmented fashion"*, หน้า 2) ของดนตรี "session" — ⚠️ **เปเปอร์นี้ไม่ได้ใช้คำว่า "LSTM" กับ folk-rnn เลย** (คำนี้ปรากฏเฉพาะตอนพูดถึง Choi / Magenta / Jaques หน้า 3–4) · ว่าเป็น LSTM ต้องอ้าง Sturm et al. 2016 (R11-4) (ดนตรีเต้นรำพื้นบ้านไอร์แลนด์/สหราชอาณาจักร) สร้าง **ทีละ transcription สมบูรณ์** (มี `<s>`…`</s>`) ต่างจาก char-rnn ที่สร้างทีละตัวอักษรแบบไหลต่อเนื่อง (§1) · ฝึกบน key, metre, pitch, grouping, duration และ measure token — **ไม่สร้างชื่อเพลง** (footnote 6)
- ⚠️ **สถาปัตยกรรม ขนาด hidden, vocabulary size, hyperparameter — ไม่มีในเปเปอร์นี้เลย** (มีแค่การเอ่ยถึง *"the minibatch strategy of training"* ใน §3.1) อ้าง Sturm et al. (2016) ทั้งหมด (ร่องรอยเดียวคือชื่อไฟล์ config `config5-wrepeats-20160112-222521.pkl` ใน §3.4) → **ต้องอ่าน R11-4 (1604.08723) ถ้าจะเทียบสถาปัตยกรรม**
- จุดยืนสำคัญ (§1): *"folk-rnn is not modelling music, but instead a highly reductive abstraction removed from what one perceives as music"* → จำกัดการซักถามไว้ที่ความเข้าใจ vocabulary, การจัดเรียงเป็นหน่วยใหญ่, และ *"formal operations such as counting, repetition and variation"*
- **ประโยคเดียวกันนี้ใช้กับเราได้ตรง ๆ**: LSTM ของเราไม่ได้ "เต้น" แต่สร้างลำดับของ cluster id ที่เป็น abstraction ของท่าเต้น

### 3.1 Table 1 — งานก่อนหน้าประเมินอย่างไร (11 แถว)

| งาน | วิธีประเมิน |
|---|---|
| Todd 1989 | ดู output ด้วยตา |
| Mozer 1994 | ความแม่นทำนาย training seq · ฟังเอง · ให้ผู้เข้าร่วมเลือกระหว่างระบบกับ **third-order Markov chain** |
| Eck & Schmidhuber 2002 | ฟังเอง |
| Chen & Miikkulainen 2001 | สถิติพื้นฐาน · ฟังเอง |
| Franklin 2006 | ทำซ้ำเพลงที่ใช้เทรน (accuracy) |
| Eck & Lapamle 2008 *(สะกดตามเปเปอร์ — น่าจะเป็น Lapalme)* | ฟังเอง |
| Boulanger-Lewandowski et al. 2012 | log-likelihood + expected accuracy เทียบ baseline หลาย dataset |
| Colombo et al. 2016 | ดู output ด้วยตา |
| Choi et al. 2016 | ดู output ด้วยตา |
| Jaques et al. 2017 | นับการละเมิด/ทำตามกฎการประพันธ์ใน 100,000 ชิ้น · MTurk pairwise preference |
| van den Oord et al. 2016 | ฟังเอง (sanity check) |

> 💡 **แถว Mozer 1994 = บรรพบุรุษของ E2 ของเรา** (เทียบ neural net กับ Markov chain อันดับสูงด้วย human preference) — ถ้าจะอ้างว่า "การเทียบกับ Markov baseline เป็นธรรมเนียมเก่า" ใช้แถวนี้ + A1-21 Galata

---

## 4. การประเมินระดับ population (§3.1) — ตัวเลขทุกตัว

ผู้เขียนเองกำหนดสถานะของวิธีนี้: *"a first-order sanity check"* ที่ *"has limited relevance to measuring how useful the model is for music practice"*

### 4.1 Fig. 1 — metre / mode / ความยาว (ค่าอ่านจากภาพ ±1 จุด%, **ไม่อยู่ใน text**)

| ด้าน | training (เทา, 23,635) | folk-rnn (ดำ, 30,000) | ข้อความในเปเปอร์ |
|---|---|---|---|
| M:4/4 | ~53% | ~66–67% | *"biased to generating ... common metre (4/4)"* |
| M:6/8 | ~25% | ~22–23% | — |
| M:3/4 · 2/4 · 12/8 · 9/8 · 3/2 | ~8 · ~7.5 · ~2 · ~3.5 · ~1 | ~4.5 · ~4 · ~1.3 · ~1 · <0.5 | *"biased against triple metres (6/8, 3/4, 9/8) and 2/4 and 12/8"* |
| K:Cmaj · Cdor · Cmin · Cmix | ~67 · ~12.5 · ~13.5 · ~7 | ~64 · ~14.5 · ~13.5 · ~7.5 | *"a little biased to ... dorian ..., and less so the major mode"* |
| ความยาว (token) | กระจายกว้าง ~0.2–6.5% ต่อ bin | **สองยอดแหลม ~18% และ ~19.5% ที่ bin 145/150** + ยอดรอง ~9% ที่ 115 | *"greatly biased to generating transcriptions that are 140-155 tokens long"* |

- เขา **ไม่รู้สาเหตุ** — *"suspect that they arise from the minibatch strategy of training"* (ไม่ได้ทดสอบ)
- 💡 **สำหรับเรา:** การกระจายความยาวที่เป็นยอดแหลมเป็นอาการที่ตรวจง่าย — เทียบ **การกระจายของ run-length / ความยาว segment** ระหว่าง training กับ generated

### 4.2 Fig. 2–3 — pitch และ pitch class

- ข้อความ (Fig. 2 บน, major): **C (middle C) > 9%**, **G หรือ c เกือบ 26%**, **^F ~0.1%** ของ pitch token
- **bias เชิงระบบ**: โมเดล **ชอบ pitch ต่ำกว่า B (เหนือ middle C)** และ **ไม่ชอบ pitch สูง** — ส่วนต่างใหญ่สุดจากภาพ ≈ **+2.8 จุด% (G, mix)** และ ≈ **−3.2 จุด% (g, mix)** · *"We currently do not know the source of this bias"*
- Fig. 3: โมเดล **ใช้ pitch ถูกโหมด** (flattened 3rd ใน dorian/minor, flattened 7th ในทุกโหมดยกเว้น major, flattened 6th เฉพาะ minor) แต่ **ต่ำกว่า training ที่ root ในทุกโหมด** — จากภาพ ≈ −0.5 (maj), **≤ −2 (mix, dor — แท่งชนขอบแกน อาจถูกตัด)**, ≈ −1.25 (min) · เนื้อความเรียก *"slightly biased"*
- ✅ กราฟมี label แกนครบ, legend ครบ, ระบุ "Note difference in scales" · ❌ ไม่มี error bar, ไม่มีการทดสอบว่าส่วนต่างมีนัยสำคัญ

### 4.3 Measure-token sequences (Table 2–3) ⭐

| | training | generated |
|---|---|---|
| จำนวน transcription | 23,635 | 30,000 |
| **unique measure-token sequences** | **3,322** | **1,867** |
| จำนวนที่อยู่ใน top-15 | 10,257 (**43.4%** — คำนวณเอง) | 20,513 (**68.4%** — คำนวณเอง) |
| อันดับ 1 | `\|: \| \| \| \| \| \| \| \| :\| \|: \| \| \| \| \| \| \| \| :\|` (1,980) | `\|: \| \| \| \| \| \| \| :\| \|: \| \| \| \| \| \| \| :\|` (5,303) |
| top-3 ใช้ร่วมกันไหม | — | **ใช่** (เปเปอร์ระบุ *"share the top three sequences"*; อันดับ 1–2 สลับกัน) |

- ส่วนใหญ่เป็นฟอร์ม **AABB, ท่อนละ 8 ห้อง** ± pickup bar — ฟอร์มมาตรฐานของดนตรีพื้นบ้านไอริช (Hillhouse 2005)
- ✔️ **ตรวจผลรวมด้วยมือแล้ว**: Table 2 = 10,257 และ Table 3 = 20,513 ตรงกับเนื้อความ

### 4.4 ABC errors ใน 30,000 ชิ้น

| ชนิด | จำนวน |
|---|---|
| `|1` ตามด้วย `|1` แทน `|2` | 55 |
| มีแต่ `|1` | 32 |
| มีแต่ `|2` | 6 |
| chord ไม่ครบ (`]` ไม่มี `[`) | 17 |

รวม **110 กรณี (≈0.37%)** — *ผลรวมนี้เราคำนวณเอง เปเปอร์ไม่ได้รวม และไม่ได้บอกว่าซ้อนกันหรือไม่* · ข้อผิดพลาดชนิดเดียวกันใน training data **ถูกแก้ก่อนเทรนแล้ว**

> 💡 **analog ของเรา:** token ของเราไม่มีไวยากรณ์ จึงไม่มี "syntax error" ตรง ๆ — ตัวที่ใกล้ที่สุดคือ **อัตรา transition (bigram) ที่ไม่เคยพบใน training** และ **ท่าที่ผิดกายวิภาค** (limb-length SD ใน E7)

---

## 5. การวิเคราะห์ระดับผลงาน (§3.2) — "ครูสอนแต่งเพลง"

- สุ่ม **5 ชิ้นจาก 30,000 โดยไม่คัด** (*"We performed no curation"*) แล้ววิเคราะห์เหมือนนักเรียนเอาเพลงมาส่งครู
| # | ฟอร์ม | จุดดี | จุดอ่อน |
|---|---|---|---|
| #22277 (4/4, C major) | AABB, 8+8 | 4 ห้องแรกดี (มี hemiola) | ท่อน B ไม่มีโฟกัส ไม่สัมพันธ์กับ A · cadence แย่ที่ bb. 7–8, 15–16 · C# ใน b. 7 ไร้หน้าที่ · natural ใน b. 11 ไม่จำเป็น |
| #1692 (aeolian) | AABB, 8+8 | modal ชัด จบที่ root, สองท่อนสัมพันธ์กัน | b. 11 **ขาดเส้นกั้นห้อง** · ซ้ำ/แปร pattern เล็ก ๆ จน "meandering" ไม่มีไอเดียหลักที่จำได้ |
| #17872 (6/8) | AABB, 8+8 | A จบด้วย V–I | B ไม่ resolve · ใช้ pattern น้อย · ห้องสุดท้ายแย่ · กระโดดใหญ่ใน b. 8 |
| #3175 (3/4) | **AB**, 8+8 | ซ้ำมาก สร้างวลี 8 ห้องได้ | กระโดด 11th ระหว่างท่อน · วลีย่อย 5+3 ไม่สมดุล · ไม่มีท่อนไหนจบที่ tonic |
| #7152 (4/4) | AABB, 8+8 | ท่อน A สอดคล้องดี | ห้องจบของ B นิ่ง ไม่สัมพันธ์ · สองท่อนเชื่อมกันอ่อน |

**ข้อสรุป (§3.2 ท้าย):** เรียนได้ "to some extent" — นับห้อง/pickup, stepwise motion, pitch ในโหมด, cadence พื้นฐาน, ซ้ำ-แปรไอเดีย, 4/5 ชิ้นเป็น AABB 8 ห้อง. **สิ่งที่ขาด:** นัยทางฮาร์โมนีของทำนองอ่อน → cadence อ่อน · **ไม่เชื่อม "มิติต่าง ๆ" เข้าหากัน** (จัดการ pattern สั้นได้ สร้างฟอร์มได้ แต่ไม่ผูกสองอย่างเข้าด้วยกัน) · เรียงห้องด้วย duration ถูก แต่ไม่เข้าใจ strong/weak beat

> 💡 **แปลเป็นภาษาเต้นของเรา:** "ท่าทีละท่า/ช่วงสั้นดูสมจริง แต่ไม่ต่อกันเป็นวลีที่มีทิศทาง" — **นี่คือสมมติฐานที่ควรทดสอบกับ output ของเราเช่นกัน** และสอดคล้องกับ comment ของผู้ปฏิบัติใน §6.1

---

## 6. Nefarious testing (§3.3) · Assisted composition (§3.4) · กลับสู่ practice (§3.5)

### 6.1 Nefarious testing — seed ทั้ง 3 (คำต่อคำ)
1. `<s> M:4/4 K:Cmaj [ G F ] 2 E G E /2 G > [ E F ] 4 |` → Fig. 9
2. `<s> M:4/4 K:Cmaj [ G F ] 2 E G E < G [ E F ] 2 |` → Fig. 10 (24 ห้อง)
3. `<s> M:4/4 K:Cmaj G 2 E G E < G F 2 |` → Fig. 11
- RNG seed = ค่า default ทุกกรณี (n = 1)
- ผลดูตาราง "อ่านตรงนี้ก่อน" ข้อ 4 · เปรียบเทียบกับนักเรียนการประพันธ์ที่ *"are taught to generalise from specific cases to other domains"*
- Ben-Tal แต่ง continuation ของมนุษย์ให้ดู 2 แบบ (Fig. 12–13): **พัฒนา motif** (undulating third, dyad, จังหวะ) + **เพิ่ม pitch ใหม่ทีละน้อย** (*"gradually (for the most part)"* — ส่วนใหญ่ห้องละตัว แต่ b. 5 เพิ่มสองตัว) → *"adds up to more then the sum of its parts"* · แต่ยอมรับว่าเป็น **post-hoc analysis ไม่ใช่การตัดสินใจขณะแต่ง** → เป็นปัญหาถ้าจะ fine-tune ให้ตอบสนองต่อผู้ประพันธ์

### 6.2 Assisted composition — "The Millennial Whoop Jig"
- seed: `M:6/8 K:Cmaj G E G E 3` (Millennial Whoop) → สร้าง 3 ชิ้น → ทุกชิ้นมีฟอร์ม jig และ **ซ้ำ motif ในห้องที่ 5** · turn ของชิ้น 1 และ 3 เป็น variation ของ motif
- วน 4 รอบ: คัด → แก้มือ → seed ใหม่ → ใช้ `--rng_seed 3213` แล้ว `--rng_seed 14` · **ยอมรับว่า *"We actually tried several random seeds until the model produced material that we found acceptable enough"*** (= curation เปิดเผย)
- เพลงที่สอง "The Millennial Whoop Reel": **ต้องใส่ motif เองด้วยมือ เพราะ *"the model could not be persuaded to repeat the motif"*** (footnote 12)
- จุดยืน: *"We are not interested in whether the model can compose music, but rather how it can contribute to the composition of music."*

### 6.3 The folk-rnn Session Book Vol. 1 (of 10) + comment จาก thesession.org
- 3,000 ชิ้น = **3,000 ชิ้นแรกของ 30,000** ที่ใช้ใน §3.1–3.2 (footnote 13)
- ความเห็นที่อ้าง (5 คน + 2 คนในข้อถกเถียง): Kenny (สองชิ้นแรก "garbage" ไม่มี question/answer, #6 ใกล้ "The Floating Crowbar"), Colman O'B (**"bar-by-bar ... very 'traditional sounding' phrases, but ... they tend not to actually go together"**; #39 จบผิดโน้ต), Jim Dorans (#4 ชอบ), Alex Henry (เจอดี 1 ใน 5 ที่ดู), Conán McDonnell ("Pot luck", "I could do something with that one") · **Ergo** คัดค้าน (กลัวคนเข้าใจผิดว่าเป็นเพลงดั้งเดิม, *"reckless"*) · **CreadurMawnOrganig** โต้ว่าเพลงในวงดั้งเดิมถูกมือมนุษย์ขัดเกลาเสมอ
- ผู้เขียนสรุป: **เพลงส่วนใหญ่ "work" ในระดับท้องถิ่น แต่ harmony และโครงสร้างวลีมักไม่ work** — ตรงกับ §3.2

### 6.4 นักดนตรีอาชีพ + กิจกรรม
- **Torbjörn Hultmark** (ทรัมเป็ต, พื้นคลาสสิก, 20 ปีหลังในแจ๊ส/improv/อิเล็กทรอนิกส์) เปิดไปกลางเล่ม ดู ~10 ชิ้น เล่น 3 ชิ้นในคอนเสิร์ต QMUL (พ.ย. 2016) — *"surprisingly catchy, easy and satisfying to play"* แต่ต้องแก้สด (ช้าลงตอนจบวลี, ตัดโน้ต ฯลฯ) ใช้ digital effects แต่งเสียงเพิ่ม และ **ยอมรับว่าคุ้นกับสไตล์นี้น้อย**
- Inside Out Festival workshop (2017): ผู้เล่นนำ **ประเมินว่า "about one in five" ของเล่มนี้ "surprisingly good"** (≈20%, เป็นการประมาณด้วยปากเปล่า ไม่ใช่การวัด)
- คอนเสิร์ตสาธารณะในลอนดอน + ข่าว 2 ชิ้น (3 และ 18 มิ.ย. 2017) · ยอมรับว่ามี *"ambiguous responses"* จากนักดนตรีและผู้ฟังบางส่วน

### 6.5 แบบสอบถาม 4 ข้อของ Session Book (template สำหรับ expert study ของเรา)
1. หาเพลงที่ **ใกล้** ดนตรีที่เจอใน session ยากไหม — ชี้ตัวอย่างและเหตุผล
2. หาเพลงที่ **ไกล** ยากไหม — ชี้ตัวอย่างและเหตุผล
3. เลือกเพลงที่ใกล้ แล้วบอกว่า **ปรับปรุงอย่างไร**
4. มีเพลงไหน **ใกล้เพลงที่มีอยู่แล้ว** ไหม ← **= คำถาม memorization ที่ README ของเราระบุว่ายังไม่มีเปเปอร์รองรับ** (ในรูปแบบการประเมินโดยมนุษย์ ไม่ใช่ metric)

---

## 7. Discussion และ Conclusion (§4–§5)

- ย้ำ: *"the model is not composing music; it is recursively generating a symbolic sequence according to joint probability distributions it has estimated from abstract and reductive representations"*
- ตีความผล `>`: ด้านหนึ่งโมเดล **ตอบสนองต่อบริบท ไม่ใช่ token เดี่ยว** · อีกด้าน **ไม่ได้เรียนหน้าที่ของ `>`** → *"calls into question its 'understanding' of other ABC tokens"*
- ปฏิเสธ music Turing test (ข้อ 8 ด้านบน)
- **ยอมรับความไม่เป็นระบบ**: สถิติ population เป็นระบบแต่ห่างจากการใช้งาน · การสุ่มเลือกเป็นระบบแต่การวิเคราะห์ไม่ใช่ → เสนอว่า **"multifaceted approach"** เหมาะที่สุดเมื่อเป้าหมายคือ co-creation ไม่ใช่ style emulation · แม้ output ล้มเหลวในเชิงสไตล์ก็อาจให้แรงบันดาลใจได้
- รายการผลงานร่วมกับ folk-rnn 23 ชิ้น (2015–2017) รวมผลงานกับ DeepBach
- **Future work (§5):** ทำให้ตอบสนองต่อผู้ประพันธ์มากขึ้น · ปรับให้เข้ากับสไตล์ของผู้ประพันธ์ · **สร้างแบบอื่นนอกจากซ้ายไปขวา** (ตอนนี้ **เติมระหว่างสองลำดับไม่ได้**) · ใส่ **"critic" ใน generation loop** + RL (Jaques et al. 2017) · เพิ่ม control · ต้องเข้าใจว่าความรู้ถูกเข้ารหัสอย่างไร

---

## 8. สมมติฐานและข้อจำกัด

**ที่ผู้เขียนยอมรับเอง:** population stats เป็นแค่ sanity check · วิธีโดยรวม "unsystematic" · ไม่รู้สาเหตุของ bias (metre/ความยาว/pitch/root) · การวิเคราะห์ continuation ของ Ben-Tal เป็น post-hoc · curation ใน §3.4 · Hultmark คุ้นสไตล์น้อย · ยังเติมระหว่างสองลำดับไม่ได้

**ที่เราเห็นเพิ่ม (pass 3):**
0. **ข้อสรุปท้าย §3.2 บวกกว่าหลักฐานเล็กน้อย** — *"overall we see plausible melodies that work"* (มี hedge "of varying quality" และตามด้วย *"At the same time, we find important aspects missing"*) ขณะที่ทั้ง 5 ชิ้นมีข้อบกพร่องสำคัญ — เป็น **การตีความของเรา ไม่ใช่ข้อผิดพลาดของเปเปอร์**
1. **ไม่มีสถิติทดสอบใดเลย** — ไม่มี KL/JS/chi-square ระหว่างการกระจาย training vs generated แม้ข้อมูลพร้อม
2. **ผู้ประเมินระดับผลงาน = ผู้สร้างโมเดล** → bias ในการตีความ (ไม่มี blind หรือ inter-rater)
3. **nefarious test: n = 1 ต่อเงื่อนไข + ปัจจัยกวน** (ข้อ 5 ด้านบน)
4. **feedback จากชุมชนเป็น self-selected** และผู้เขียน *"selection from the comments thread"* — ไม่รู้ว่าคัดอย่างไร
5. **ไม่ระบุ sampling settings** (temperature) ของ 30,000 ชิ้น
6. **ตัวอย่างเสียงพึ่งลิงก์ goo.gl** — อาจเข้าถึงไม่ได้แล้ว (**ไม่ได้ทดสอบ**) · ABC ในเปเปอร์ยังใช้ได้
7. ไม่มี baseline (เช่น n-gram / Markov) ในการประเมินใด ๆ — แม้ Table 1 จะชี้ว่า Mozer 1994 ทำไว้

---

## 9. 🚨 ทะเบียนข้อผิดพลาด/ความไม่สอดคล้องในเปเปอร์

| # | จุด | ปัญหา |
|---|---|---|
| 1 | **caption Fig. 12 และ Fig. 13** | ระบุว่าเป็น continuation ของ `G 2 E G E < G F 2` (seed ขั้น 3 ที่ **ตัด dyad ออกแล้ว**) แต่เนื้อความบอกว่าเป็น continuation ของ *"our 'nefarious' initialisation above"* และวิเคราะห์ว่าพัฒนา **"the dyads"**, **"the three-dyad idea"**, **"the intervallic idea of the initial dyads"** — seed ใน caption **ไม่มี dyad** · **verifier render ห้องแรกของ Fig. 13 ที่ 400 dpi: dyad F–G, E G E, G, dyad E–F = seed ขั้น 2 `[ G F ] 2 E G E < G [ E F ] 2` เป๊ะ** (Fig. 12 ดูเหมือนกันที่ 130 dpi) → **caption ผิด ที่ถูกคือ seed ขั้น 2** ห้ามอ้าง caption ตรง ๆ |
| 2 | **"The Mal's Copporim" ถูกระบุเป็นผลงานของสองโมเดล** | หน้า 9 และ 22: output ของ **char-rnn** · รายการผลงานหน้า 27 ข้อ 21: *"'The Mal's Copporim' by folk-rnn (2015)"* → ขัดกัน **ใช้ char-rnn ตามเนื้อความ** |
| 2b | Table 1 caption vs เนื้อหา | caption: *"research applying recurrent neural networks"* แต่มีแถว van den Oord et al. 2016 ซึ่งหน้า 4 บอกเองว่า *"do not use recurrent connections"* |
| 2c | §1 สัญญาเกิน §3.3 | §1 เขียน *"'nefarious' initialisations, e.g., dyads, atonality, etc."* แต่ §3.3 ทดสอบแค่ dyad + token `>` — **ไม่มี atonality** |
| 2d | References (ความรู้ภายนอก ต้องตรวจ) | "Eck & **Lapamle**" น่าจะเป็น **Lapalme** · Mozer (1994) ระบุ *Cognitive Science* 6(2&3) — น่าจะเป็น ***Connection Science*** → **ตรวจก่อนลง bibliography** |
| 3 | รายการผลงาน #10 | ลิงก์ YouTube เดียวกันซ้ำสองครั้ง (`QWvlnOqlSes`) |
| 4 | §3.3 ย่อหน้าท้าย | "more then the sum of its parts" — typo (then→than) ไม่กระทบเนื้อหา |
| 5 | abstract vs Fig. 1 | "over 23,000" vs 23,635 — ไม่ขัดกัน แต่ **ให้ใช้ 23,635** |

---

## 10. ความสัมพันธ์กับงานข้างเคียงและกับคลังของเรา

### 10.1 เทียบกับเปเปอร์ที่สรุปแล้ว
| เปเปอร์ในคลัง | ความเชื่อมโยง |
|---|---|
| **A1-21 Galata VLMM** | ทั้งคู่ประเมิน generative sequence model โดยไม่มีเฉลย แต่ Galata มี **E_T vs horizon (เชิงปริมาณ)** ส่วนนี่ **เชิงคุณภาพ** → ใช้คู่กัน: ระดับ population ของเรา = E_T + สถิติการกระจาย |
| **A1-12 SinMDM** | ทั้งคู่วัด "fidelity + diversity" โดยไม่มี feature extractor · **measure-token unique count / top-15 share ≈ diversity/coverage แบบนับได้** เสริม Coverage/LocalDiv ได้ |
| **A1-22 MotionCritic** | Sturm ปฏิเสธ "fooling" test; MotionCritic ใช้ preference ของมนุษย์เป็น critic · และ §5 ของ Sturm เสนอ "critic in the generation loop" ในอนาคต = ทิศทางเดียวกับ MotionCritic |
| **A1-2 chor-rnn** | ทั้งคู่: RNN/LSTM, corpus เล็กของประเพณีเดียว, unconditional, ประเมินเชิงคุณภาพ · ต่าง: chor-rnn ทำงานบน pose ต่อเนื่อง; folk-rnn บน vocabulary ที่ **ประเพณีกำหนดเอง (ABC)** |
| **L3-5 Atomic Movements** | ตรงข้าม: L3-5 อ้าง "perceptual naturalness" โดยไม่มี human eval; Sturm **เอาไปให้มนุษย์จริงและรายงานเสียงคัดค้านด้วย** |
| **A1-16 Rhythm is a Dancer** | การเทียบการกระจายของ unit (metre/mode/pitch) ระหว่าง training vs generated = รูปแบบเดียวกับ motion signature แต่ **Sturm ไม่มี chi-square** |
| **A0-3 Joshi & Chakrabarty / L3-26 ChoreoMaster** | ยืนยัน pillar (1) อีกชั้น: vocabulary ของ folk-rnn **มนุษย์/ประเพณีประกาศไว้** เหมือนกรณีของ ChoreoMaster |

### 10.2 จุดต่างที่ต้องเขียนทุกครั้ง (ตาม checklist R11-4)
**vocabulary ของ folk-rnn มาจาก ABC notation ที่ประเพณีจดไว้เอง — ของเรา "ค้นพบ" ด้วย clustering** ⇒ ผลที่ตามมา 3 ข้อที่เปเปอร์นี้ช่วยให้เห็น:
1. เขาตรวจ **ความถูกต้องทางไวยากรณ์** ได้ (ABC errors) — **เราไม่มีไวยากรณ์ให้ตรวจ** ต้องใช้ unseen-bigram rate / anatomical plausibility แทน
2. เขาตรวจ **"เข้าใจหน้าที่ของ token"** ได้ (`>`) เพราะ token มีความหมายที่รู้ล่วงหน้า — **token ของเราไม่มีความหมายก่อน clustering** ⇒ nefarious test ของเราต้องนิยาม "ผิดธรรมเนียม" จากสถิติ training (เช่น seed ที่ประกอบด้วย bigram ที่ไม่เคยเกิด) แทนนิยามทางทฤษฎี
3. ผู้เชี่ยวชาญอ่าน output ของเขาได้เป็นโน้ต — **ของเราต้อง render เป็นภาพเคลื่อนไหวก่อน** ผู้เชี่ยวชาญจึงจะประเมินได้

### 10.3 ผลต่อ thesis ของเรา
- **บทประเมินผล:** ใช้ 5 มุมนี้เป็นโครง "ดัดแปลงจาก Sturm & Ben-Tal (2017)" — (1) population: token/run-length/segment-structure distributions + unique/top-k share (2) practice: เลือกสุ่ม N ชิ้นไม่คัด ให้ผู้เชี่ยวชาญนาฏศิลป์วิจารณ์ (3) nefarious: E11 (4) assisted: อาจข้ามได้ถ้าไม่ได้ทำ co-creation — **ต้องเขียนระบุว่าข้าม** (5) practice domain: expert study ด้วยแบบสอบถาม 4 ข้อ
- **Limitations:** อ้างได้ว่าการประเมินเชิงคุณภาพ "by and large unsystematic" เป็นข้อจำกัดที่รู้จักกันในสาย และชดเชยด้วย n > 1, หลาย seed, และผู้ประเมินที่ไม่ใช่ผู้สร้างโมเดล

---

## 11. Checklist pass (`knowledge/reading_checklist.md` ทีละข้อ)

### 11.1 รายการที่เปเปอร์นี้ถูกระบุไว้ตรง ๆ
| รายการ | สถานะเดิม | ผลรอบนี้ |
|---|---|---|
| **R11-1 · L3-36 Sturm & Ben-Tal (2017)** | `[ ]` | ✅ **ครอบคลุมเต็ม** — อ่านครบ 29 หน้า (pass 2 ทั้งฉบับ, pass 3 ใน §3.1/§3.3/§4) · **ยืนยัน:** 5 วิธีประเมินตรงตาม checklist, 30,000 vs 23,635 (checklist เขียน "23,000" — ปัดลง), "nefarious tester" มีจริงใน §3.3 · **แก้:** เปเปอร์ไม่ได้เรียกว่า "ระดับ" และไม่อ้างว่าเป็นลำดับชั้น · **ข้อความ "ระดับ 3 ฟรี ไม่มีใครในสายเราทำ" เป็นข้ออ้างของ checklist ไม่ใช่ของเปเปอร์** — ยังไม่ได้ตรวจกับวรรณกรรม motion · **DOI/เล่มยังไม่ได้ยืนยัน** (ไม่อยู่ใน PDF) |

### 11.2 รายการอื่นที่เปเปอร์นี้ไปแตะ
| # | รายการ | ครอบคลุม? | เปเปอร์ว่าอย่างไร |
|---|---|---|---|
| R11-2 | Holtzman — nucleus sampling | **แตะ** | high temperature → ABC ผิดไวยากรณ์ (Fig. 15) · ไม่มี top-k/top-p · **ไม่ระบุค่า temperature** |
| R11-3 | Bengio — scheduled sampling / exposure bias | **แทบไม่ครอบคลุม (analogy ของเรา)** | เปเปอร์ **ไม่พูดถึง exposure bias เลย** · การเชื่อม nefarious test (context นอก distribution → ทั้งลำดับพัง) กับ exposure bias เป็น **การเทียบเคียงของเรา** · และเปเปอร์บอกว่า output ที่ไม่มี seed *"correctly counts bars for the most part"* (หน้า 14) — ไม่ได้ชี้ว่าคุณภาพทรุดตามความยาว |
| R11-4 | folk-rnn (1604.08723) | **แตะ — ไม่ทดแทน** | นี่คือเปเปอร์ต่อเนื่อง **ไม่มีรายละเอียดสถาปัตยกรรม** ต้องอ่าน R11-4 แยก · จุดต่าง "vocabulary ประเพณีจดเอง vs ค้นพบด้วย clustering" ยืนยันแล้วจากเปเปอร์นี้ (vocabulary = ABC tokens) |
| R11-5 / R11-6 / R11-7 | surveys / JNMR 2019 | **ไม่ครอบคลุม** | — (R11-7 ไม่ได้ถูกอ้างในเปเปอร์นี้ เพราะเปเปอร์นี้ออกก่อน) |
| E8 | sweep decoding rule | **หนุน** | ให้หลักฐานเชิงคุณภาพว่า temperature สูงทำลายไวยากรณ์ |
| E9 | exposure-bias check | **อ่อน** | ดู R11-3 — ไม่มีหลักฐานเรื่องความยาว rollout |
| E11 | nefarious tester | **✅ protocol ครบ (การทดลองยังไม่ได้ทำ)** | ให้ protocol บันได 3 ขั้น + ตัวอย่างการตีความ · **ปรับปรุง: หลาย seed/เงื่อนไข และเปลี่ยนทีละปัจจัย** · **ไม่ติ๊ก E11** เพราะเป็นการทดลองที่เราต้องรันเอง |
| E7 | metric ไม่ต้องมี corpus | **แตะ** | เพิ่ม unique-structure count + top-k share |
| E2 | Markov baseline | **แตะ** | Table 1: Mozer 1994 เทียบกับ third-order Markov chain · เปเปอร์นี้เองไม่มี baseline |
| 1 | A1-21 VLMM | แตะ | ดู §10.1 |
| 2 | A1-12 SinMDM | แตะ | ดู §10.1 |
| 12 | A1-22 MotionCritic / user study | **✅ ครอบคลุมบางส่วน** | แบบสอบถาม 4 ข้อ + เหตุผลปฏิเสธ Turing test + แนวคิด critic-in-the-loop |
| 15 / L3-26 | white space / pillar (1) | **แตะ** | vocabulary ของ folk-rnn มนุษย์กำหนด (ABC) |
| 21 | A1-2 chor-rnn | แตะ | ดู §10.1 |
| README gap "memorization / n-gram overlap" | **แตะ (เชิงมนุษย์)** | คำถามข้อ 4 ของ Session Book + ตัวอย่าง Kenny ("opens very much like 'The Floating Crowbar'") · **ไม่ให้ metric** |
| README gap "decoding strategy" | แตะ | ดู R11-2 |

### 11.3 รายการที่ไม่เกี่ยว
ข้อ 3–10, 13–14, 16–20, 22–23 (tokenizer/codebook/pose estimation/motif/surveys) · Tier 3 ข้อ 24–31 · E1, E3–E6, E10 · "ต้องให้คุณช่วย" ทั้งหมด

### 11.3b ข้อสังเกตเรื่อง checklist (ไม่แก้ เพราะแก้ได้เฉพาะ tick box)
- ข้อ 19 **A1-20 Skeleton Motion Words** ยัง `[ ]` ทั้งที่มี `summaries/2508.04513v1.summary.md` แล้ว — รอผู้ใช้ตัดสินใจติ๊ก (บันทึกไว้ตั้งแต่รอบ ChoreoMaster)
- R11-1 เขียน "23,000" และ "5 ระดับ" → ควรเป็น 23,635 และ "5 วิธี" (ดู "อ่านตรงนี้ก่อน" ข้อ 1–2)
- เปเปอร์ที่ยังไม่มีสรุป (รอบต่อไป เรียงจากเก่าสุด): `2506.05104v2`, `2506.00915v1`, `2507.05419v1`, `1604.08723v1`, `1506.03099v3`, `1904.09751v2`, `Exploringtheimpactofmachinelearning…systematicreview-2 (1).pdf`

### 11.4 คำตัดสิน checklist
| ระดับ | รายการ |
|---|---|
| ✅ ครอบคลุมเต็ม | **R11-1** (เป้าหมาย) · E11 ได้ protocol ครบ (แต่ยังเป็นงานทดลองค้าง) |
| 🟡 บางส่วน / แตะ | R11-2, R11-4, E2, E7, E8, 1, 2, 12, 15, 21, README gaps (memorization, decoding) |
| 🔸 อ่อน (analogy ของเรา) | R11-3, E9 |
| ⬜ ไม่ครอบคลุม | ที่เหลือทั้งหมด |

**คำตัดสินรวม: ✅ ผ่าน — R11-1 อ่านครบ; ให้ protocol ของ E11 ทันที และให้ metric โครงสร้างราคาถูก (unique/top-k share) กับเหตุผลเชิงวิธีวิทยาสำหรับ expert study**

### 11.5 การแก้ `reading_checklist.md`
เปลี่ยนเฉพาะ tick box บรรทัด **R11-1** จาก `[ ]` เป็น `[✅]` (ช่องแรก = team read and verify) — ไม่แตะข้อความอื่น

---

## 12. Verification (independent second pass)

รันด้วย **subagent ตรวจสอบอิสระ (`fact-auditor` / Vera)** ตาม STEP 5 — ส่ง PDF ต้นฉบับ + ร่างสรุป + `reading_guide.md` + `reading_checklist.md` + `src/generate.py` แล้วสั่งให้ **ไม่เชื่อร่าง** และสกัดใหม่เองด้วย pymupdf (รวม render หน้า 6, 7, 9, 16, 17 เป็นภาพ และ crop ห้องแรกของ Fig. 13 ที่ 400 dpi) · **จากนั้นผู้เขียนหลักตรวจข้อค้นพบซ้ำกับ text dump ก่อนแก้ทุกข้อ**

### 12.1 สิ่งที่ verifier ตรวจ
ตัวเลขทุกตัวใน §4 (23,635 / 30,000 · 3,322 / 1,867 · ผลรวม Table 2–3 · ABC errors 55/32/6/17) · ค่าที่อ่านจาก Fig. 1–3 (±1 จุด) · seed ทั้ง 3 ของ nefarious test คำต่อคำ + ผลลัพธ์ · RNG seed 3213/14 · รายละเอียด Hultmark · "one in five" · Session Book · จำนวนผลงาน (23) · Table 1 (11 แถว) · bug register · การคำนวณ duration ของ seed · ข้ออ้างเรื่องโค้ด `generate.py` · ความถูกต้องของ checklist cross-check

### 12.2 คำตัดสินรอบแรก: **REVISE**

**🔴 Blocker 2 ข้อ (ตรวจซ้ำแล้วจริง แก้แล้ว):**
1. ร่างเขียนว่า "ทุกคำสั่งใน §3.4 มี `--rng_seed`" — **จริง ๆ มีแค่ 2 จาก 4 คำสั่ง** และ seed เหล่านั้นถูกเลือกหลังลองหลายค่า → แก้ข้อ 6
2. ร่างเรียก folk-rnn ว่า "LSTM" โดยอ้าง §1 — **เปเปอร์นี้ไม่เคยใช้คำว่า LSTM กับ folk-rnn** → แก้ §3 และ §13 ให้อ้าง Sturm et al. 2016 แทน

**🟠 Should-fix 8 ข้อ (แก้แล้วทั้งหมด):** (S1) ตัวแปรกวนขั้น 1→2 — ระบุว่าจังหวะเท่าเดิม (8 หน่วย) ตัวแปรกวนอยู่ที่การโทษ `>` โดยเฉพาะ · (S2) 43.4%/68.4% ติดป้ายว่าคำนวณเอง · (S3) "plausible melodies that work" ย้ายจาก bug register ไปเป็นการตีความของเรา (§8) · (S4) ผลขั้น 1–2 เขียนให้ครบทั้งด้านบวก · (S5) **E11 ไม่ติ๊ก** (เป็นการทดลองที่ต้องรัน) และลด R11-3/E9 เป็น "analogy ของเรา" · (S6) "goo.gl ตายแล้ว" → "ยังไม่ได้ทดสอบ" · (S7) arXiv ID/รหัส L3-35 ระบุว่ามาจาก checklist ไม่ใช่เปเปอร์ · (S8) "เพิ่ม pitch ทีละตัว" ใส่ hedge "for the most part"

**➕ Omission (เพิ่มแล้ว):** "The Mal's Copporim" ระบุเป็นทั้ง char-rnn และ folk-rnn · Table 1 caption vs WaveNet ที่ไม่ใช่ RNN · §1 สัญญาทดสอบ "atonality" แต่ไม่ได้ทำ · references ที่น่าจะผิด (Lapamle→Lapalme, Mozer → *Connection Science*; **เป็นความรู้ภายนอก ต้องตรวจ**) · เปเปอร์เอ่ยถึง "minibatch strategy of training" · Hultmark ใช้ digital effects · แท่ง root ของ Fig. 3 ชนขอบแกน (≤ −2)

### 12.3 ✅ สิ่งที่รอดการตรวจ (ยืนยันอิสระ)
- 23,635 / 30,000 · 3,322 / 1,867 · ผลรวม Table 2 = 10,257, Table 3 = 20,513 (43.40% / 68.38%) · ABC errors รวม 110 (0.367%)
- ค่าจาก Fig. 1–3 อยู่ในเกณฑ์ ±1 จุด (ยกเว้นช่วงแท่งเทาของความยาว แก้แล้ว)
- seed ทั้ง 3 ตรงคำต่อคำ · ผลลัพธ์ทั้ง 3 ขั้นตรง · n = 1 / default seed ยืนยันจากต้นฉบับ
- **bug #1 (caption Fig. 12–13) เป็นข้อผิดพลาดจริงของเปเปอร์** — verifier ยืนยันจากโน้ตในภาพว่าห้องแรกคือ seed ขั้น 2
- ไม่มีค่า temperature · ไม่มีสถิติทดสอบ · ไม่มีสถาปัตยกรรม · PDF ไม่มี DOI/หัววารสาร
- `src/generate.py` ไม่ตั้ง RNG seed จริง (verifier ตั้งข้อสังเกตเพิ่ม: `train_lstm.py` ตั้ง seed ที่บรรทัด 66–67 แต่อยู่ใน CLI entry point)

### 12.4 สิ่งที่ verification ตรวจ **ไม่ได้**
- venue/DOI/เล่ม (ไม่อยู่ใน PDF) · อันดับ SJR/CORE ของ JCMS · สถานะลิงก์ goo.gl/YouTube · เนื้อหาของ Sturm et al. 2016 (R11-4) ที่เปเปอร์นี้พึ่งพา

### 12.5 คำตัดสินสุดท้าย
**ผ่านหลังแก้** — ไม่มีตัวเลขที่อ้างผิดจากต้นฉบับเหลืออยู่; ข้อความเชิงตีความทุกข้อติดป้ายว่าเป็นของเรา

---

## 13. บทสรุปในประโยคเดียว

> **Sturm & Ben-Tal (2017) ประเมิน folk-rnn — RNN ระดับ token บน ABC ของดนตรีพื้นบ้านไอริช (ว่าเป็น LSTM ต้องอ้าง Sturm et al. 2016) — ด้วย 5 วิธีที่ไม่ต้องมีเฉลย และแสดงด้วยตัวอย่างว่าสถิติ population (30,000 vs 23,635) บอกว่าโมเดล "นับห้องได้ สร้างฟอร์ม AABB ได้" แต่ nefarious seed เผยว่าความสามารถนั้น "true only in a very limited context"; สำหรับเรา ของที่ได้คือ protocol ของ E11 (ต้องแก้ n = 1 ของเขา), ตัววัดการรวมศูนย์ของโครงสร้าง (unique 3,322→1,867, top-15 43.4%→68.4%), แบบสอบถามผู้เชี่ยวชาญ 4 ข้อ, เหตุผลปฏิเสธ Turing test — และข้อเตือนว่า `generate.py` ของเรายังไม่มี RNG seed.**
