# A0-6 · Nogueira, Menezes & Maçãs de Carvalho (2024) — Exploring the impact of machine learning on dance performance: a systematic review

> **ไฟล์:** `knowledge/reading_docs/Exploringtheimpactofmachinelearningondanceperformanceasystematicreview-2 (1).pdf` · 51 หน้า PDF (หน้า 1 = ปกของ tandfonline, เนื้อหา = หน้าวารสาร 60–109)
> **ผู้แต่ง:** Maria Rita Nogueira (Manchester Metropolitan Univ. + ISR, Univ. of Coimbra) · Paulo Menezes (ISR / ECE, Coimbra) · José Maçãs de Carvalho (Centre for Interdisciplinary Studies, Coimbra)
> **Venue:** *International Journal of Performance Arts and Digital Media* **20(1):60–109 (2024)** · DOI 10.1080/14794713.2024.2338927 · Taylor & Francis · **Open Access CC-BY 4.0** · received 20 Jun 2023 / accepted 25 Mar 2024 / online 24 Apr 2024 · ปกระบุ "Article views: 2898 · Citing articles: 2" (ณ วันที่ดาวน์โหลด)
> **ระดับ venue (ตาม `reading_guide.md`):** วารสาร peer-reviewed สายศิลปะการแสดง/สื่อดิจิทัล — **ไม่ใช่ venue สาย CS/ML** · *รอบนี้ไม่ได้ตรวจ SJR quartile* → ถ้าจะอ้างในเชิงความน่าเชื่อถือ ต้องเช็คเพิ่ม
> **ข้อสังเกตในหน้าเปเปอร์:** มี *Correction statement* — *"corrected with major corrections, but these changes do not impact the academic content"* (p.106)
> **วิธีอ่าน:** Three-Pass (Keshav) ตาม `reading_guide.md` — pass 1 + pass 2 ครบทุกหน้า รวม Table 1–5 และ reference list · ตาราง render เป็นภาพเพื่อตรวจว่าข้อความในแต่ละช่องอยู่แถวไหนจริง (pdftotext ทำให้ข้อความข้ามแถวในตาราง — ดู §9) · pass 3 บางส่วน: ตรวจความสอดคล้องภายใน (ตัวเลข/ปี/การอ้าง) และเทียบข้อเท็จจริงเรื่อง chor-rnn กับสรุปต้นฉบับที่เรามีอยู่แล้ว (`1605.06921v1.summary.md`) · **ไม่ได้** เปิดเปเปอร์ต้นทางอีก 22 ชิ้นเพื่อตรวจทุกข้อความ
> **เขียน:** 2026-09-24 (scheduled `read-a-paper`)

---

## ⚠️ อ่านตรงนี้ก่อน — ข้อที่เปลี่ยนวิธีใช้เปเปอร์นี้

1. **เป็น "systematic review" แค่ในชื่อ** — อ้าง PRISMA + Petticrew & Roberts (2008) แต่ **ไม่มี PRISMA flow diagram, ไม่มี search string, ไม่มีจำนวนที่ตัดออกในแต่ละขั้น, ไม่มี quality appraisal, ไม่มี inter-rater** มีแค่ **345 → 23** (p.61) · exclusion criteria เป็นเชิงคุณภาพล้วน ("did not primarily address the creative aspects") → **ทำซ้ำไม่ได้** · และแม้จะบอกว่า screening เป็น *"peer-reviewed studies"* (p.67) แต่ตัวอย่างที่เลือกรวม **บทความข่าว WIRED (Leprince-Ringuet 2018), หน้า Google Arts & Culture (Living Archive, Becoming, Bill T. Jones), arXiv preprint (chor-rnn, Pettee, Castro, AIST++)** ด้วย — ขัดกับ p.61 ของเปเปอร์เองที่เปิดเผยว่าเป็น *"a comparative study of research studies, artistic creations, and performances"* → ความไม่สอดคล้องอยู่ **ระหว่าง p.61 กับ p.67 ภายในเปเปอร์** ไม่ใช่ข้อบกพร่องที่ซ่อนไว้
2. **คุณค่าจริงสำหรับเรา = แผนที่ฝั่ง "ศิลปะ/การแสดง" ไม่ใช่ฝั่ง ML** — ไม่มี metric, ไม่มีการเปรียบเทียบเชิงปริมาณข้ามงาน, ตัวเลขทั้งหมดยกมาจากเปเปอร์ต้นทาง · ใช้เป็น **related work สำหรับประเด็นจริยธรรม/ความเป็นเจ้าของ/การมีส่วนร่วมของนักเต้นมืออาชีพ** ได้ดี
3. **อย่ายกคำอธิบายงานต้นทางจากเปเปอร์นี้ไปอ้างต่อ** — พบความผิดพลาดเชิงข้อเท็จจริง/ความไม่สอดคล้องภายในหลายจุด (§9) เช่น
   - chor-rnn: *"After five hours of training ... began to resemble human movement"* (p.69) — เปเปอร์ต้นทางใช้ **5 ชั่วโมงเป็นขนาด corpus** ส่วนจุดสังเกตระหว่างเทรนคือ ~10 นาที / ~6 ชม. / ~48 ชม. (ตาม `1605.06921v1.summary.md`) → น่าจะสับสนกับขนาด corpus หรือปัด checkpoint ~6 ชม.
   - AIST++: p.75 = **5.2 ชม. / 1,408 sequences** แต่ p.87 = **"over 5000 dance sequences"**
   - Yalta et al. (2019) เป็นงาน **สร้างท่าเต้นจากเสียงเพลง** *(อนุมานจากชื่อเรื่อง + คอลัมน์ Arguments + Table 5 limitations ที่พูดถึง music track/MADMOM; ยังไม่เปิดต้นฉบับ Yalta)* แต่ Table 3 และ §4.3 บอกว่าเป็นระบบ *"track the movements of ballet dancers and provide real-time feedback on posture"*
   - McGregor *"We can generate 24,000 permutations"* ถูกผูกกับ Living Archive (p.70) แต่ reference ของเปเปอร์เอง (The Guardian 3 Oct 2017, URL `.../wayne-mcgregor-autobiography-dna-dance-sadlers-wells`) เป็นเรื่องงาน *Autobiography* (2017)
   - "Between Us" ถูกบรรยายว่า *"interaction-based authoring approach, blending case-based and imitative learning"* (Table 1, §5.1) — ซึ่งเป็นคำบรรยายของ **Jacob & Magerko** ไม่ใช่ของ Between Us
   → **อ้างเปเปอร์นี้ได้เฉพาะในฐานะ "review ที่จัดหมวด + ยกประเด็นจริยธรรม"** ส่วนข้อเท็จจริงของงานแต่ละชิ้นให้อ้างต้นฉบับ
4. **🔗 ข้อที่มีประโยชน์ตรงกับ pipeline เรา (จากงานที่เขา review):**
   - **Hwang, Yang & Kwak (2020)** — ใช้ **k-means บน pose** แล้วนิยาม *rare pose* = จุดที่ไกลจาก cluster center; **ความแม่นยำของ pose estimation ลดลงเมื่อระยะจาก center เพิ่มขึ้น** (ตามคำสรุปใน Table 2) → *(การอนุมานของเรา — แหล่งพูดแค่ว่า pose-estimation accuracy ลดลง)* ท่าเต้นที่แปลกอาจทั้ง *landmark แย่ลง* และ *ถูก quantize แย่ลง* พร้อมกัน · ทดลองบน COCO/MPII ไม่ใช่ BlazePose · ต้องอ่านต้นฉบับก่อนอ้าง
   - **Carlson et al. (2020)** — SVM บน mocap ของการเต้นอิสระกับเพลง 8 แนว: **จำแนก "ตัวนักเต้น" ได้แม่นกว่า "แนวเพลง" อย่างชัดเจน** → ถ้า Phase 2 ของเราจะหา style association ต้องระวังว่า "สไตล์" กับ "ตัวคนเต้น" ปนกัน (confound)
   - **Lee et al. (2019) Dancing to Music** — แตกท่าเต้นเป็น "basic dance units" แล้วประกอบใหม่ = งานที่ใกล้ "vocabulary ของหน่วยท่า" ที่สุดในชุด 23 ชิ้นนี้ — แหล่งบอกแค่ว่า *"decomposes a dance into a series of basic dance units and learns how to move"* (Table 4) · *(การอนุมานของเรา: น่าจะไม่ใช่ clustering ของท่านิ่ง — ต้องเช็คต้นฉบับ Lee 2019)*
5. **ข้ออ้าง white space (ระมัดระวัง):** ในตัวอย่าง 23 ชิ้นของเขา (2010–2023, ฝั่งศิลปะ) **ไม่มีงานไหนสร้าง pose vocabulary ด้วย clustering แล้วเอาไปใช้สร้างท่าเต้น** — k-means ที่ปรากฏ (Hwang 2020) ใช้เพื่อ *หา rare pose* ไม่ใช่เป็น vocabulary · แต่เพราะวิธีค้นทำซ้ำไม่ได้ (ข้อ 1) นี่เป็น **หลักฐานเสริมอ่อน ๆ** เท่านั้น ห้ามใช้เป็นหลักฐานหลัก

---

## 1. Five Cs (`reading_guide.md`, pass 1)

| C | คำตอบ |
|---|---|
| **Category** | **Literature review (ติดป้าย systematic)** — ไม่ใช่งานทดลอง ไม่ใช่ prototype · รีวิว 23 ชิ้นที่รวมทั้งงานวิจัยและงานศิลปะ/การแสดง |
| **Context** | ฐานคือประวัติ computer + dance (Smoliar & Weber 1977, Calvert & Chapman 1978, Camurri et al. 1986, Sagasti 2019), ศิลปินกลุ่ม OpenEndedGroup (Downie, Kaiser), McGregor × Google, Graves (2013) สำหรับ RNN สร้างลำดับ · ระเบียบวิธี review อ้าง Petticrew & Roberts (2008) + PRISMA |
| **Correctness** | **อ่อน** — ระเบียบวิธีรายงานไม่ครบ (ข้อ ⚠️1), การจัดหมวดไม่สม่ำเสมอ (งานเดียวอยู่ 2–3 หมวด โดยเกณฑ์ไม่ชัด), มีข้อเท็จจริงผิดเกี่ยวกับงานที่รีวิวหลายจุด (§9), ใช้คำว่า "significantly" โดยไม่มีสถิติ (p.100 เรื่อง Correia et al.) · รีวิวงานของผู้แต่งเอง (FORMS) พร้อมประกาศ *"No potential conflict of interest"* (p.106) |
| **Contributions** | (1) กรอบ 4 หมวดของจุดตัด ML × dance performance (2) ตารางสรุปต่อหมวด (Table 1–4) + ตารางรวม impact/limitations 22 แถว (Table 5) (3) รายการประเด็นจริยธรรม 5 ข้อ (§5.3) โดยเฉพาะ **การขาดการมีส่วนร่วมของนักเต้นมืออาชีพ** และ **authorship/ownership** |
| **Clarity** | อ่านง่ายระดับภาษา แต่ **ซ้ำซ้อนมาก** (งานเดียวถูกบรรยายซ้ำเกือบคำต่อคำใน Table 1, 2, 3, 5 และในเนื้อหา) และคำคุณศัพท์ส่งเสริมเยอะ ("ground-breaking", "revolutionizes", "paradigm shift") เกินหลักฐาน |

## 2. ตารางสกัดของ อ.Proadpran

| ช่อง | คำตอบ |
|---|---|
| **Motivation** | ความสนใจ ML × dance เพิ่มขึ้น แต่ *"there is a lack of comprehensive research that evaluates the impact of machine learning on dance from multiple perspectives"* (abstract) · และโครงการจำนวนหนึ่งไม่ได้ให้นักเต้นมืออาชีพมีส่วนร่วม โดยเฉพาะตอน curate dataset จากวิดีโอ (p.61) |
| **Research Question** | **RQ1:** ML ถูกใช้ทำอะไรใน dance performance และส่งผลอย่างไรต่อ 4 ด้าน (choreographic creation support / dataset or network collection and training / improved human-pose detection / perception and new visual representations) · **RQ2:** ML ส่งผลต่อความคิดสร้างสรรค์ของนักแสดง นักออกแบบท่า ผู้เข้าร่วม และบุคลากรด้านเต้นอย่างไร (p.66) |
| **Proposed Method** | ค้น Web of Science, Scopus, Google Scholar ด้วยคำค้น 'machine learning', 'dance', 'dance movement', 'human-pose detection', 'dance performance', 'audience engagement' · ภาษาอังกฤษ ปี 2010–2023 · 345 → 23 ชิ้น · ตัดงานที่เน้น somatics / authentic movement · จัดเข้า 4 หมวด (งานหนึ่งอยู่ได้หลายหมวด) แล้วสรุปเป็นตาราง |
| **Evaluation** | ไม่มีการวัดเชิงปริมาณของตัว review · "ผล" คือการสังเคราะห์เชิงบรรยาย + Table 5 (impact vs limitations ต่องาน) |
| **Contribution** | แผนที่เชิงหมวดของงาน ML × dance ฝั่งศิลปะ + ประเด็นจริยธรรม 5 ข้อ |

---

## 3. ปัญหาและแรงจูงใจ (§1–2)

- ML ใช้ใน dance ทั้งฝั่ง **ออกแบบท่า** (McGregor × Google), **การแสดงสด** (Bill T. Jones 2019, FORMS), และ **pose detection** (p.60–61) — ในประโยคเรื่อง detection ของร่างกาย เปเปอร์อ้าง Crnkovic-Friis (2016) [chor-rnn], Chan et al. (2019), Cao et al. (2019) [OpenPose] ไว้ด้วยกัน
- ตัวอย่างผู้บุกเบิก: OpenEndedGroup (Marc Downie, Paul Kaiser) ร่วมงานกับ Merce Cunningham, Trisha Brown, Wayne McGregor (p.61)
- ข้อสังเกตตั้งต้นที่วนกลับมาตลอดเปเปอร์: dataset อย่าง MADS (Zhang et al. 2017) และงาน Yalta et al. (2019) ถูกยกเป็นตัวอย่างบทบาทของนักเต้นมืออาชีพ แต่ **หลายโครงการไม่ได้ให้นักเต้นมืออาชีพมีส่วนร่วม โดยเฉพาะตอน curate dataset จากวิดีโอ** (p.61) · ⚠️ แต่ p.81/p.96 บอกเองว่าท่าเต้นใน MADS *"were not executed by dance professionals"* → ขัดกับ p.61 (ดู §9 #15)

## 4. วิธีการ (§3)

### 4.1 Search strategy (§3.1, p.61 + p.66–67)
| รายการ | ค่า |
|---|---|
| ฐานข้อมูล | Web of Science, Scopus, Google Scholar |
| คำค้น | 'machine learning', 'dance', 'dance movement', 'human-pose detection', 'dance performance', 'audience engagement' (ไม่บอกว่ารวมกันด้วย AND/OR อย่างไร) |
| ช่วงปี / ภาษา | 2010–2023 · อังกฤษ (*"due to resource constraints"*) |
| จำนวน | **345 → 23** |
| Inclusion | งานที่ตัดกันระหว่าง ML กับ dance performance ใน 4 หมวด ไม่จำกัดสไตล์การเต้น |
| Exclusion | งานที่ไม่ได้เน้นด้านสร้างสรรค์ของการเต้น / จุดตัดกับเทคโนโลยี · งานที่เน้น somatics และ authentic movement ล้วน (เหตุผลอ้าง "post-human body") |
| Screening | 2 ขั้น: identification และ screening ของ peer-reviewed studies แล้ว merge ที่ขั้น eligibility |

### 4.2 สี่หมวด (§3.2, p.67–68)
1. **Choreographic creation support** — วิเคราะห์ movement vocabulary ของนักออกแบบท่า/คณะ แล้วสร้างรูปแบบใหม่ (*"machine learning algorithms can be trained to recognize specific movements or sequences and generate new variations"*)
2. **Dataset or network collection and training** — ต้องมี dataset กว้าง · ยังขาด dataset ด้าน dance (อ้าง Zhang 2017, Yalta 2019)
3. **Improve techniques of human-pose detection** — ตรวจ/ติดตามท่าให้แม่นขึ้น ใช้ใน performance analysis, training, rehabilitation
4. **Perception and new visual representations of dance movement** — ML ช่วยให้ผู้ชมรับรู้การเคลื่อนไหวต่างไป (เช่น อ่านอารมณ์, ปฏิสัมพันธ์ระหว่างส่วนร่างกาย)

---

## 5. ผล — งานที่รีวิวแยกตามหมวด (§4, Table 1–4)

> ตัวเลขทุกตัวข้างล่าง **ยกมาจากคำสรุปของ Nogueira et al.** ไม่ได้ตรวจกับต้นฉบับ (ยกเว้นที่ระบุ)

### 5.1 Choreographic creation support (Table 1, §4.1)
| งาน | ปี (ตามตาราง) | สาระที่เปเปอร์บอก |
|---|---|---|
| Jacob & Magerko — *Interaction-based Authoring for Scalable Co-creative Agents* (LuminAI / Viewpoints AI) | 2015 | ผสม case-based + imitative learning · Kinect · ข้อจำกัด: sample เล็ก, มีเสียงว่า agent แค่ mimic ผู้ใช้, มือใหม่ trigger gesture segmentation ไม่ค่อยได้ (Table 5) |
| Crnkovic-Friis & Crnkovic-Friis — **chor-rnn** | 2016 | RNN, mocap contemporary dance 5 ชม. ด้วย Kinect v2 · สร้างท่าในสไตล์ของ corpus · ข้อจำกัด: solo dancer, Kinect จับ occlusion ไม่ได้ (Table 5) · ⚠️ ดู §9 เรื่องเวลาเทรน |
| Chan et al. — *Everybody Dance Now* | 2018 (ตาราง) / 2019 (เนื้อหา, ICCV) | motion transfer "do as I do" ผ่าน pose (OpenPose) · ปล่อย dataset วิดีโอที่ใช้เทรนได้ถูกกฎหมาย + forensics tool · ข้อจำกัด: artifact จากเสื้อผ้าหลวม/ผม, แขนขาหาย |
| Leprince-Ringuet (WIRED) — Google × Wayne McGregor | 2018 | PoseNet + ML สร้างท่าใหม่จากท่าเดิม ทดสอบกับนักเต้นมืออาชีพ |
| Pettee et al. — *Beyond Imitation* | 2019 | RNN + autoencoder บน 53 จุด 3D ต่อ time step · สร้าง sequence ใหม่และ variation |
| Wayne McGregor × Google — **Living Archive** | 2019 | ระบบเทรนบน archive ของ McGregor · ผู้ใช้เต้นหน้า webcam แล้วค้นท่าคล้าย · McGregor: *"We can generate 24,000 permutations"* (เปเปอร์ผูกกับ Living Archive แต่ reference เป็นบทความ Guardian 2017 เรื่อง *Autobiography* — §9 #16) · ทั้งคู่ (chor-rnn, Living Archive) ได้แรงบันดาลใจจาก Graves (2013) |
| Li (Ruilong) et al. — **AIST++ / FACT** | 2021 | dataset 3D dance + music 10 genre, multi-view · FACT = Full-Attention Cross-modal Transformer · ⚠️ ขนาด dataset ขัดกันเอง (§9) · ข้อจำกัด: kinematic ล้วน (foot sliding/floating), deterministic |
| MotionBank × Staatstheater Mainz × Kunsthalle Mainz — **Between Us** (ชิ้น *Effect* ของ Taneli Törmä) | 2021 | บันทึกกระบวนการสร้าง 6 สัปดาห์ · mocap แบบ markerless ต่อเนื่อง 60 นาที, วิดีโอ HD 8 มุม, เสียง 4 ช่อง (p.86) · "Online Score" · เปิดให้สาธารณะ |
| Bill T. Jones × Google — *Body, Movement, Language* | 2019 | *อยู่ในเนื้อหาเท่านั้น ไม่มีแถวในตาราง* · speech recognition + PoseNet ในการแสดงสด |

### 5.2 Dataset or network collection and training (Table 2, §4.2)
| งาน | ตัวเลข/สาระ |
|---|---|
| Zhang et al. 2017 — **MADS** | martial arts (Tai-chi, Karate), dance (hip-hop, jazz), กีฬา 6 ชนิด · depth-based แม่นกว่า color-based · ผู้แสดง: ปรมาจารย์ศิลปะป้องกันตัว 2, นักเต้น 2, นักกีฬา 1 · **ผู้เขียนเองยอมรับว่าท่าเต้นไม่ได้ทำโดยนักเต้นมืออาชีพ** (p.81, 96) · discriminative tracker ดีกว่าเมื่อข้อมูลพอ, generative ทนความหลากหลายของท่าแต่หลุดเมื่อเคลื่อนเร็ว |
| Kishore et al. 2018 | CNN จำแนก action ของ Indian classical dance (offline + YouTube) · **93.33%** recognition rate |
| Castro et al. 2018 (เนื้อหา) / 2020 (ตาราง) — **Let's Dance** | **1,000 วิดีโอ, 10 หมวด** (ballet, flamenco, latin, square, tango, breakdance, foxtrot, quickstep, swing, waltz), คลิปละ **10 วินาที @ 30 fps** · 3 representation: video, optical flow, multi-person pose |
| Priya & Arulselvi 2019 | multi-view dataset Bharathanatyam + Karate · pose classification **62%** · ข้อจำกัด: รูปน้อย |
| Living Archive 2019 | (ซ้ำจากหมวด 1) |
| **Hwang, Yang & Kwak 2020** — *Exploring Rare Pose in HPE* (IEEE Access) | **k-means** หา rare pose โดยไม่ต้องเรียนเพิ่ม · outlier ไกลจาก center = rare · **ความแม่นยำลดลงเมื่อระยะจาก center เพิ่ม** · 3 วิธีแก้: duplicate rare pose, synthetic rare pose, weighted loss ตามระยะ · เพิ่มสูงสุด **13.5 mAP บน rare pose** · ทดลองบน COCO + MPII · ภาพรวมไม่ดีขึ้นมากเพราะ rare pose มีสัดส่วนน้อย |
| AIST++ 2021, Between Us 2021 | (ซ้ำ) |

### 5.3 Improve techniques of human-pose detection (Table 3, §4.3)
| งาน | ตัวเลข/สาระ |
|---|---|
| Zhang et al. 2017 (MADS) | (ซ้ำ) · Table 5: tracking error จาก fast motion (โบกแขน, กระโดด) เพราะ init จาก pose เฟรมก่อน · self-occlusion |
| Protopapadakis et al. 2018 | จำแนกท่าประจำของ **folk dance 6 แบบ** + variation จาก Kinect skeleton · ข้อจำกัด: Kinect จับ spatio-temporal ซับซ้อนไม่ไหว, ข้อมูลน้อย |
| Kim & Kim 2018 | RGB-D markerless · Korean traditional dance + K-pop · ทน full-body rotation/self-occlusion · **mAP 0.9358, average pose error 3.88 cm, 98% concordance กับการประเมินของผู้เชี่ยวชาญ** (Table 5) · เสนอ metric ความคล้ายระหว่าง dance sequence · ข้อจำกัด: ไวต่อแสงและ occlusion |
| Chan et al. | (ซ้ำ) |
| Yalta et al. 2019 | ⚠️ ดู §9 — Table 5 ข้อจำกัด: performance ตก **เกือบครึ่ง** เมื่อใช้เพลงที่ไม่ได้เทรน, ไม่ชนะ model ที่ประมวลแค่ beat (MADMOM) |
| Mohammed, Lv & Islam 2019 | CNN ตรวจจับมือ + จำแนก gesture · ทดสอบบน ICD (Indian classical dance), Oxford, 5-signers, EgoHands + LaRED, TinyHands |
| Zhang & Zhang 2020 — MM-TDMC | กู้คืน motion จาก observation เสื่อม (short-term) · เทียบกับ auto-conditioned RNN, low-rank matrix completion ฯลฯ |

### 5.4 Perception and new visual representations (Table 4, §4.4)
| งาน | ตัวเลข/สาระ |
|---|---|
| OpenEndedGroup (Downie, Rothwell, McGregor) — **Becoming** | 2013 · agent นามธรรมพยายามเลียนการเคลื่อนไหวจาก **1,240 shot** ของหนัง sci-fi ยุค 1980 ด้วย heuristic search · จอ 3D สูง 6 ฟุต แนวตั้ง · caption แสดงคำสั่งของ agent |
| Long, Jacob & Magerko 2019 — *Designing Co-Creative AI for Public Spaces* | **ตัวเปเปอร์เองบอกว่าไม่ได้ประยุกต์กับ dance โดยตรง** (Table 4, Table 5) — แต่ยังถูกนับเข้า 23 |
| Lee et al. 2019 — **Dancing to Music** (NeurIPS) | synthesis-by-analysis: แยก dance เป็น **basic dance units** แล้วประกอบใหม่ตามเพลง · ข้อจำกัด: beat hit rate ลดลง, ข้อมูลรวบรวมอัตโนมัติ noisy, LSTM ไม่ multimodal จึงไม่มี multimodality score |
| **Carlson, Saari, Burger & Toiviainen 2020** (JNMR) | mocap การเต้นอิสระกับเพลง **8 แนว** · SVM · **จำแนกรายบุคคลแม่นกว่าจำแนกแนวเพลงอย่างเห็นได้ชัด ("contrary to expectations")** |
| Nogueira et al. 2022/2023 — **FORMS** (งานของผู้แต่งเอง) | human pose detection → รูปทรงเรขาคณิต/เส้นโค้ง real-time บนเวที · นักเต้นอาชีพรุ่นเยาว์ **8 คน** (Table 5) · คำพูดนักเต้น 3 ประโยค (p.100) · ⚠️ self-citation ในหมวดที่ผู้แต่งสรุปว่าได้ผลดี |
| Correia et al. 2022 (DIS '22) | MLIV + CAIV แปลง body map นิ่งเป็นภาพ interactive · participatory study **12 นักเต้น** · ข้อจำกัด: เวลา/งบไม่พอ |

### 5.5 Table 5 — ตารางรวม (p.88–95)
22 แถว (2013–2022) คอลัมน์ "Impact and Main Application" กับ "Disadvantages or Limitations" · **ไม่มี Kishore et al. และ Leprince-Ringuet** ที่อยู่ใน Table 1–2

---

## 6. การอภิปรายและข้อสรุป (§5–6)

- **RQ1 (§5.1):** สรุปซ้ำ 4 หมวด — งานหมวด choreographic 3 ชิ้น (chor-rnn, Living Archive, Beyond Imitation) ใช้ deep learning สร้างท่าใหม่จากข้อมูลเดิม แต่ *"each project differs significantly in method and purpose"* (p.101) · ในหมวด perception บอกว่ารีวิว "six research projects" (Long, Lee, Carlson, **Leach & Stevens 2020**, Nogueira 2023, Correia) — ⚠️ Leach & Stevens ไม่อยู่ใน Table 4 และ Becoming หายไปจากรายการนี้
- **RQ2 (§5.2):** ML เป็น *"wellspring of inspiration"* ให้ choreographer ทดลอง variant และ *"computational analysis of choreographic effectiveness"* · ด้านลบ = authorship/ownership
- **§5.3 ประเด็นจริยธรรม/ศิลปะ 5 ข้อ:**
  1. **Limited engagement with dance professionals** — วิเคราะห์ตื้น, ข้ามข้อกำหนดทางเทคนิค/คุณภาพของการเต้น, การใช้วิดีโอจาก YouTube ยิ่งห่างจากมุมมองของนักเต้น
  2. **Artistic ownership and authorship** — เครดิตเป็นของอัลกอริทึม โปรแกรมเมอร์ นักเต้น หรือรวมกัน
  3. **Cultural impact and unintended biases** — output ของอัลกอริทึมอาจมี bias/ไม่อ่อนไหวต่อวัฒนธรรม กระทบความแท้ของรูปแบบการเต้น
  4. **Diminishing human expression** — พึ่งท่าที่เครื่องสร้างอาจลดความลึกทางอารมณ์
  5. **Striking a delicate balance** — ชุมชนเต้น นักพัฒนา และนักจริยธรรมต้องร่วมมือ
- **Conclusion (§6):** ML เป็น catalyst ของความคิดสร้างสรรค์ แต่ต้องรักษา "authentic human touch" · ⚠️ ย่อหน้าแรกอ้าง *"as reflected in the next section"* ทั้งที่เป็น section สุดท้าย
- **ไม่มี future work ที่เป็นรูปธรรม** (ไม่มีรายการคำถามวิจัยเปิด ไม่มีข้อเสนอ benchmark)

---

## 7. ความสัมพันธ์กับงานที่อ้าง

- **ฐานประวัติศาสตร์:** Smoliar & Weber 1977 (Labanotation), Calvert & Chapman 1978, Camurri et al. 1986, Maletic 1987 (Laban), Herbison-Evans 1991, Sagasti 2019
- **ระเบียบวิธี:** Petticrew & Roberts 2008, PRISMA (อ้างชื่อแต่ไม่มี reference entry ของ PRISMA เอง)
- **Pose estimation ที่อ้าง:** OpenPose (Cao et al. 2019), PoseNet (ผ่าน Google) — **ไม่ได้อ้าง BlazePose/MediaPipe เลย**
- **งานที่ทับกับคลังเรา:** chor-rnn = A1-2 (`1605.06921v1.summary.md`) · AIST++ / FACT (อ้างในหลายสรุปของเรา) · Everybody Dance Now · Dancing to Music (Lee 2019)
- **ถูกอ้างโดย:** A0-2 Neurocomputing 2026 review (`1-s2.0-S0925231226008635-main.summary.md`) อ้างเปเปอร์นี้เป็น [117] และจัด Relevance = Direct
- **ขาด (ในมุมของเรา):** ตัวอย่างมีงาน generation สาย CS อยู่บ้าง (AIST++/FACT 2021, Dancing to Music NeurIPS 2019, Everybody Dance Now ICCV 2019, chor-rnn, Yalta IJCNN 2019) แต่ **ไม่มีงาน dance/motion generation สาย CS หลัง AIST++/FACT (2021)** ใน reference list (pp.107–109) — *[ความรู้ภายนอก]* เช่น Bailando, EDGE, TM2D ไม่อยู่ในรายชื่อ แม้ปี 2021–2023 จะอยู่ในช่วงค้น → ตัวอย่างเอียงไปฝั่ง arts/HCI

---

## 8. สมมติฐานและข้อจำกัด (pass 3)

1. **ระเบียบวิธี review ทำซ้ำไม่ได้** — ไม่มี query ที่แท้, ไม่มี PRISMA diagram, ไม่มีจำนวนในแต่ละขั้น, ไม่มีเกณฑ์คุณภาพ
2. **เกณฑ์ peer-reviewed ขัดกับตัวอย่าง** — p.67 *"screening of peer-reviewed studies"* แต่ p.61 บอกเองว่าเปรียบเทียบ *"research studies, artistic creations, and performances"* · ตัวอย่างมีบทความข่าว (WIRED), หน้า Google Arts & Culture (Living Archive, Becoming, Bill T. Jones), arXiv preprint (Castro, Pettee, AIST++, chor-rnn)
3. **การนับ 23 ตรวจสอบไม่ได้** — นับแถวไม่ซ้ำใน Table 1–4 ได้ **24** (ถ้านับ Leprince-Ringuet กับ Living Archive เป็นโครงการเดียวกันจะได้ 23 — *เป็นการตีความของเรา เปเปอร์ไม่ได้ระบุ*) · Table 5 มี 22 แถว · Bill T. Jones และ Leach & Stevens ถูกพูดถึงในเนื้อหาแต่ไม่อยู่ในตาราง
4. **งานนอก scope ถูกนับ** — Long et al. 2019 ที่ผู้เขียนบอกเองว่าไม่เกี่ยวกับ dance · Mohammed et al. 2019 เป็นงาน hand detection/gesture ทั่วไป (แต่ทดสอบบน dataset มือของ Indian classical dance ด้วย, p.97 → ถกเถียงได้)
5. **การจัดหมวดหลวม** — งานเดียวอยู่หลายหมวดโดยเหตุผลในคอลัมน์ "Arguments to classify" บางครั้งขัดกับหมวดที่จัด (เช่น Chan et al. ใน Table 3 เขียนว่า *"seems to be primarily focused on the choreographic creation aspect rather than on improving techniques of human-pose detection"* แต่ก็ยังอยู่ใน Table 3)
6. **Self-citation** — FORMS ของผู้แต่งถูกสรุปว่า *"results unequivocally affirm the success"* (p.100) ขณะที่ Disclosure ระบุ *"No potential conflict of interest was reported"* (p.106) · *("conflict of interest เชิงผลลัพธ์" เป็นการตัดสินของเรา)*
7. **ไม่มีหลักฐานเชิงปริมาณสนับสนุน RQ2** — ข้อสรุปเรื่องผลต่อความคิดสร้างสรรค์มาจากคำบอกเล่า/คำพูดนักเต้น ไม่มีการสังเคราะห์เชิงระบบ

## 9. 🚨 ทะเบียนความไม่สอดคล้อง/ข้อผิดพลาด (เช็คก่อนอ้าง)

| # | จุด | รายละเอียด | ระดับ |
|---|---|---|---|
| 1 | chor-rnn เวลาเทรน (p.69) | *"After five hours of training the model, the choreography ... began to resemble human movement. After two days of total training time..."* — ต้นฉบับ: **5 ชม. = ขนาด corpus**; จุดสังเกตระหว่างเทรน ~6 ชม. ("very basic movement") และ ~48 ชม. (ตาม `1605.06921v1.summary.md`) → "5 hours of training" **น่าจะ** สับสนกับขนาด corpus 5 ชม. หรือปัด checkpoint ~6 ชม. ("2 days" ≈ 48 ชม. ตรง) | ข้อเท็จจริงผิด |
| 2 | chor-rnn optimiser (p.69) | *"trained with a neural network via RMS propagation through time"* — ต้นฉบับ: *"RMS Prop using Back Propagation Through-Time"* · และไม่กล่าวถึง LSTM 3×1024 + Mixture Density Network | บรรยายคลาดเคลื่อน |
| 3 | ชื่อสะกด | "Chorn-rnn" (p.69, p.101) vs "Chor-rnn" (Table 1) | typo |
| 4 | AIST++ ขนาด | p.75: **5.2 h, 1,408 sequences, 10 genres** · p.87: **"over 5000 dance sequences"** | ขัดกันเอง |
| 5 | AIST++ ชื่อ/ผู้แต่ง | เรียก "AI Choreographer: ..." (p.75) และ "Learn to Dance with AIST++" (Table 1, reference) · ผู้แต่งถูกอ้างเป็น "Ruilong et al." (ใช้ชื่อต้นเป็นนามสกุล; reference: "Ruilong, Li") | บรรณานุกรม |
| 6 | Yalta et al. 2019 | ปรากฏ 5 จุด: Table 3 (Type of dance "Ballet", technology "RGB + D sensors, motion capture system", Main findings) + Table 5 Impact (p.90: *"identifies and classifies ballet movements in real-time"*) + §4.3 (p.96) + §5.1 (p.102): *"system that can track the movements of ballet dancers and provide real-time feedback on posture and technique"* · แต่ชื่อเปเปอร์, คอลัมน์ Arguments และ Table 5 limitations พูดถึง **การสร้างท่าเต้นจากเพลง** (motion beat f-score, MADMOM) → คำบรรยาย "ballet feedback" ไม่เข้ากับงานนี้ | ข้อเท็จจริงน่าจะผิด (ต้องเช็คต้นฉบับ Yalta) |
| 7 | Between Us | Table 1 Arguments + §5.1: *"introduces an innovative interaction-based authoring approach, blending case-based and imitative learning"* = คำบรรยายของ Jacob & Magerko | ข้อความผิดงาน |
| 8 | Jacob & Magerko | ข้อความ p.69 *"In the same year [2016], Jacob and Magerko (2015)"* · reference ของ Jacob & Magerko 2015 ใส่ venue = *C&C 2019*, หน้า 271–284, DOI 10.1145/3325480.3325504 — **ตรงกับของ Long, Jacob & Magerko 2019 ทุกตัว** | บรรณานุกรมผิด |
| 9 | ปีไม่ตรงกัน | Everybody Dance Now: 2018 (Table 1, 3, 5) vs 2019 (เนื้อหา/reference) · Let's Dance: 2020 (Table 2, 5) vs 2018 (เนื้อหา/reference) | minor |
| 10 | Mohammed et al. ใน §5.1 | *"introduced a deep learning-based system for human posture estimation"* — แต่งานคือ hand detection + gesture recognition (ตาม Table 3 ของเปเปอร์เอง) | บรรยายคลาดเคลื่อน |
| 11 | Perception "six projects" (§5.1) | รายชื่อมี Leach & Stevens (ไม่อยู่ใน Table 4) และไม่มี Becoming (อยู่ใน Table 4) | ขัดกันเอง |
| 12 | Let's Dance "Type of dance" | Table 2 ระบุ "Ballroom dances" แต่เนื้อหา (p.81) ระบุ 10 หมวดที่รวม ballet, flamenco, breakdance | ขัดกันเอง (เล็ก) |
| 13 | Conclusion p.105 | *"as reflected in the next section"* แต่ไม่มี section ถัดไป | minor |
| 14 | "significantly heightened" (p.100, Correia) | ไม่มีสถิติประกอบในเปเปอร์นี้ | ภาษาเกินหลักฐาน |
| 15 | MADS กับนักเต้นมืออาชีพ | p.61: Zhang et al. (2017) และ Yalta et al. (2019) *"underscore the role of dance professionals in advancing datasets"* · p.81/p.96: ท่าเต้นใน MADS *"were not executed by dance professionals"* | ขัดกันเอง |
| 16 | คำพูด "24,000 permutations" (p.70) | ถูกนำเสนอว่าเป็นเรื่อง Living Archive (2019) แต่ reference (The Guardian 3 Oct 2017, URL `...wayne-mcgregor-autobiography-dna-dance-sadlers-wells`, p.108) เป็นเรื่อง *Autobiography* (2017) | อ้างผิดงาน |
| 17 | Jacob & Magerko กับ LuminAI (p.69, p.101) | ย่อหน้า "Jacob and Magerko (2015)" บรรยายงานศึกษา taxonomy ของ LuminAI แล้วอ้าง Long et al. (2017) → ดูเหมือนเป็นงานของ Long et al. 2017 ที่ถูกเครดิตให้ Jacob & Magerko 2015 | น่าจะอ้างผิดงาน (อนุมาน) |

> **หมายเหตุวิธีตรวจ:** ข้อความใน pdftotext ของตารางไหลข้ามแถว (เช่นข้อความเรื่อง rare pose/clustering ดูเหมือนอยู่ในแถว Living Archive) — **ตรวจจากภาพ render แล้ว (p.72–73) ข้อความอยู่ในแถวที่ถูกต้อง** ไม่นับเป็นข้อผิดพลาดของเปเปอร์

---

## 10. ความสัมพันธ์กับงานข้างเคียงและกับโปรเจกต์ของเรา

### 10.1 เทียบกับคลังที่สรุปแล้ว
| สรุปในคลัง | ความเชื่อมโยง |
|---|---|
| `1605.06921v1.summary.md` (A1-2 chor-rnn) | เปเปอร์นี้บรรยาย chor-rnn คลาดเคลื่อน (§9 #1–2) → **อ้าง chor-rnn จากต้นฉบับเท่านั้น** · สอดคล้องกับข้อแก้ของเราว่า "5 ชม." คือ corpus ใหญ่ ไม่ใช่ small data |
| `1-s2.0-S0925231226008635-main.summary.md` (A0-2) | A0-2 อ้างเปเปอร์นี้ [117] Relevance = Direct · ทั้งสองเป็น review ที่ **ไม่มี search protocol ที่ทำซ้ำได้** (A0-2 ไม่มีเลย, อันนี้มีบางส่วน) |
| `2307.10894v3.summary.md` (A0-1 survey) | A0-1 จัดตามสัญญาณเงื่อนไข ฝั่ง CS · อันนี้จัดตามบทบาทในงานศิลปะ → **ใช้คู่กัน** เพื่อวาง position ทั้งสองฝั่ง |
| `1906.00606v1` / `rspa.2021.0071` (A0-3 Joshi) | อีก review ฝั่ง dance computation · ทั้งสองไม่มี clustering-based vocabulary → ข้อ white space มีหลักฐานเสริม 2 แหล่ง |
| `Assessment_of_monocular_...summary.md` (A1-14) | A1-14 ให้ตัวเลข error ของ BlazePose · Hwang 2020 (ผ่านเปเปอร์นี้) ให้กลไก: **ท่าที่แปลก (ไกล centroid) → pose estimation แย่ลง** → เสริมกันเรื่องงบความคลาดเคลื่อนของ input สำหรับท่าเต้น |
| `2409.00203v1.summary.md` (Text2Tradition, Thai) | เปเปอร์นี้ **ไม่มีงานเต้นไทย** · ครอบคลุม Indian classical, Korean traditional, folk dance (Protopapadakis) · ประเด็น cultural bias (§5.3 ข้อ 3) ใช้ได้กับคลิปไทยของเรา |

### 10.2 ผลต่อ thesis ของเรา
1. **Related work / Ethics paragraph:** อ้างเปเปอร์นี้สำหรับ (ก) ประเด็นการมีส่วนร่วมของนักเต้นมืออาชีพ (ข) authorship ของท่าที่สร้าง (ค) cultural bias — เหมาะกับคลิปเต้นไทยของเรา
2. **Evaluation:** ข้อ "limited engagement with dance professionals" สนับสนุนให้มี expert/user study ในแผน eval (สอดคล้อง R11-1 ระดับ practice) — แต่เปเปอร์นี้ **ไม่ได้ให้ protocol**
3. **Phase 2 (style association):** ผลของ Carlson 2020 (ตัวคนเต้น > แนวเพลง) = เหตุผลที่ต้องควบคุม dancer identity ก่อนสรุปว่า cluster ใดผูกกับ "สไตล์" · *ต้องอ่าน Carlson ต้นฉบับก่อนอ้าง*
4. **DATA stage:** Hwang 2020 → ท่าหายากอาจถูกทั้ง BlazePose และ k-means ปฏิบัติแย่ · คู่กับ utilisation diagnostic (L3-22) · *ต้องอ่านต้นฉบับก่อนอ้าง*

### 10.3 จุดแข็ง / จุดอ่อน
- **แข็ง:** มุมมองฝั่งศิลปะที่คลังเรามีน้อย · ตาราง limitations ต่องาน (Table 5) · ประเด็นจริยธรรมที่ชัด · open access
- **อ่อน:** ระเบียบวิธีไม่ครบ, ข้อเท็จจริงผิดหลายจุด, ซ้ำซ้อน, ไม่มีมุม CS/generation สมัยใหม่, self-citation

### 10.4 ตัดสินใจตาม pass 2
**พอที่ pass 2** — ไม่ควรลง pass 3 ต่อ · ใช้เป็น citation รองสำหรับ ethics/related work · งานต้นทางที่ควรตามอ่าน (ถ้ามีเวลา): **Hwang et al. 2020** (IEEE Access 8:194964–194977) และ **Carlson et al. 2020** (JNMR 49(2):162–177)

---

## 11. Checklist pass (`knowledge/reading_checklist.md` ทีละข้อ)

### 11.1 รายการที่เปเปอร์นี้ถูกระบุไว้ตรง ๆ
| รายการ | สถานะ | หมายเหตุ |
|---|---|---|
| **A0-6 · Nogueira et al. (2024)** (หมวด "ต้องให้คุณช่วย") — *"CC-BY แต่ tandfonline 403 ... เลื่อนมา 4 รอบแล้ว → อ่านรอบหน้าหรือตัดทิ้งไปเลย"* | ✅ **Addressed** — อ่านครบ pass 2 จาก PDF ในเครื่อง | **ไม่ควรตัดทิ้ง** แต่ก็ไม่ใช่ core: ใช้เป็น related work ฝั่ง arts/ethics · ติ๊ก `[✅]` (ช่อง team read+verify) **หลัง** verification pass ใน §12 เสร็จ — ช่องที่สองเป็นของ Cop |
| A0-2 Music-driven dance generation review (Neurocomputing 2026) | related (ไม่ใช่รายการของเปเปอร์นี้) | A0-2 อ้างเปเปอร์นี้เป็น [117] Relevance = Direct — การอ่านรอบนี้ปิด pointer นั้น |

### 11.2 รายการอื่นที่เปเปอร์นี้แตะ
| รายการ | สถานะ | สิ่งที่เปเปอร์บอก |
|---|---|---|
| #21 A1-2 chor-rnn | **Partially** | บรรยาย chor-rnn แต่ผิด 2 จุด (§9 #1–2) → ไม่เปลี่ยนข้อสรุปเดิมของเรา |
| #5 A1-14 monocular pose error | **Not covered — pointer only** | ไม่มีตัวเลข BlazePose · มีแค่สรุปมือสองบรรทัดเดียวของ Hwang 2020 (COCO/MPII): accuracy ลดลงตามระยะจาก cluster center · Zhang 2017: fast motion + self-occlusion ทำ tracking พัง |
| #22 A1-6 BlazePose | **Not covered** | อ้าง OpenPose, PoseNet เท่านั้น |
| #14 Text2Tradition / Thai | **Not covered** | ไม่มีเต้นไทย · มีประเด็น cultural bias ทั่วไป (§5.3 ข้อ 3) |
| #11 / #20 white space ของ token vocabulary | **Partially** | ใน 23 ชิ้นไม่มี clustering-based vocabulary สำหรับ generation · ใกล้สุดคือ Lee 2019 (basic dance units) · หลักฐานอ่อนเพราะวิธีค้นทำซ้ำไม่ได้ |
| #16 A0-1 survey | **Related, not partial** | review ฝั่ง arts vs A0-1 ฝั่ง CS — ใช้คู่กันได้ แต่ไม่ได้ตอบรายการนี้ |
| #30 Laban-based style recognition (Tier 3) | **Tangential** | ไม่มีงาน Laban-based · Carlson 2020 (SVM บน mocap): dancer identity แยกได้ดีกว่า genre → confound ของ style association |
| R11-1 Sturm & Ben-Tal (ระดับ practice / ผู้ปฏิบัติ) | **Partially** | เน้นให้นักเต้นมืออาชีพมีส่วนร่วม · FORMS มีคำพูดนักเต้น แต่ไม่มี protocol ประเมิน |
| #2 SinMDM metrics / E7 | **Not covered** | ไม่มี metric ของ generation |
| R11-6 mirroring augmentation | **Not covered** | — |
| E1–E11 | **Not covered** | ไม่มีข้อไหนที่เปเปอร์นี้ให้วิธีหรือหลักฐานตรง |

### 11.3 รายการที่ไม่เกี่ยว
Tier 0 #1, #3, #4 (VLMM, DASB, speech tokens), Tier 1 #6–10, #12–13, Tier 2 #15, #17–19, #23, Tier 3 #24–29, #31, R11-2 ถึง R11-5, R11-7 — เปเปอร์นี้ไม่พูดถึง

### 11.4 คำตัดสิน checklist
- รายการเป้าหมาย **A0-6 = addressed** → ติ๊ก `[✅]` หลัง verification (§12)
- **Partially** 3 แถว (#21 chor-rnn, #11/#20 white space, R11-1 practice level) · **related/tangential/pointer** 3 แถว (#5, #16, #30) · ที่เหลือ not covered · **ไม่มีรายการไหนที่เปเปอร์นี้ปิดได้ด้วยตัวเอง**
- **ไม่มี** รายการใน checklist ที่ต้องแก้ข้อความ (และสคริปต์อนุญาตแค่ติ๊ก) — แต่ข้อความ "tandfonline 403" ล้าสมัยแล้วเพราะ PDF อยู่ในเครื่อง

---

## 12. Verification (independent second pass)

### 12.1 สิ่งที่ verifier ตรวจ
Verifier อิสระ (Vera / `fact-auditor`, ไม่แก้ไฟล์) ตรวจ draft กับ PDF ต้นฉบับตาม `reading_guide.md` เดียวกัน: ตัวเลขทุกตัวใน ⚠️ box และ §5 (เทียบข้อความ + **render ตารางเป็นภาพ** p.65, 72, 73, 78), การนับแถวตาราง (Table 1–4 = 24 แถวไม่ซ้ำ, Table 5 = 22 แถว), ทุกแถวใน §9 ว่าเป็นข้อผิดของเปเปอร์จริงไม่ใช่ artifact ของ pdftotext, ข้อเท็จจริง chor-rnn เทียบ `1605.06921v1.pdf` + สรุปเดิม, Five Cs / ตาราง Proadpran, และคำตัดสิน §11 เทียบ `reading_checklist.md`

### 12.2 คำตัดสินรอบแรก: **REVISE** — ไม่มีตัวเลขผิดเลย แต่มี blocker 2 · should-fix 7 · nit 7

### 12.3 สิ่งที่แก้ตาม verifier (แก้ครบทุกข้อ)
| # | ปัญหาใน draft | แก้เป็น |
|---|---|---|
| B1 | §11 เขียนว่า A0-6 "ติ๊กแล้ว" ทั้งที่ยังไม่ได้ติ๊ก | ติ๊กหลัง verification เสร็จ (ทำแล้วในรอบนี้) |
| B2 | §7 บอกว่า "ไม่มีงาน motion generation สาย CS เลย" — ผิด (มี AIST++/FACT, Dancing to Music, EDN, chor-rnn, Yalta) | "ไม่มีงานหลัง AIST++/FACT (2021)" + ติดป้ายชื่อ Bailando/EDGE/TM2D ว่าเป็นความรู้ภายนอก |
| S3 | §9 ขาดความขัดแย้ง MADS/นักเต้นมืออาชีพ (p.61 vs p.81/96) | เพิ่ม §9 #15 + หมายเหตุใน §3 |
| S4 | §9 ขาด: คำพูด "24,000 permutations" อ้าง Guardian 2017 เรื่อง *Autobiography* ไม่ใช่ Living Archive | เพิ่ม §9 #16 + แก้แถว Living Archive + ⚠️3 |
| S5 | §9 #1 ฟันธงสาเหตุ chor-rnn "5 hours of training" เกินไป | "น่าจะสับสนกับ corpus หรือปัด checkpoint ~6 ชม." (⚠️3 ด้วย) + ใส่ถ้อยคำต้นฉบับ RMSProp/BPTT |
| S6 | ข้อ peer-reviewed ไม่ยุติธรรม — ไม่ได้ยกว่า p.61 บอกเองว่ารวม artistic creations | ยกทั้ง p.61 และ p.67 + ระบุรายการที่ไม่ peer-reviewed ครบ |
| S7 | §6 "งานส่วนใหญ่ใช้ deep learning..." — ต้นฉบับพูดถึงแค่ 3 ชิ้น | ระบุ 3 ชิ้น + ยกประโยค "each project differs significantly" |
| S8 | §8 #6 ไม่ได้ยก Disclosure "No potential conflict of interest" | เพิ่ม + ติดป้ายว่าคำว่า COI เชิงผลลัพธ์เป็นการตัดสินของเรา |
| S9 | §11.2 ให้ "Partially" ใจดีเกิน (#5, #30, #16) | #5 → pointer only · #30 → tangential · #16 → related · นับใหม่ใน §11.4 |
| N10 | §9 #6 Yalta บอกแค่ 3 จุด | ระบุครบ 5 จุด (Table 3 ×2 ช่อง, Table 5 Impact, §4.3, §5.1) |
| N11 | ⚠️3 ฟันธงว่า Yalta = music-to-dance | ติดป้าย "อนุมาน ยังไม่เปิดต้นฉบับ" |
| N12 | ⚠️4 ข้อ Lee "ไม่ใช่ clustering" และ Hwang "quantize แย่ลง" เป็นการอนุมาน | ติดป้ายการอนุมาน + ยกถ้อยคำแหล่ง |
| N13 | ย่อหน้า Jacob & Magerko บรรยายงาน LuminAI taxonomy ที่อ้าง Long et al. 2017 | เพิ่ม §9 #17 (อนุมาน) |
| N14 | §3 ใส่ chor-rnn ในกลุ่มออกแบบท่า แต่ p.61 อ้างมันในประโยคเรื่อง detection | แก้ §3 |
| N15 | §8 #4 เรียก Mohammed ว่า "hand gesture ทั่วไป" แข็งไป | ระบุว่าทดสอบบน ICD dataset → ถกเถียงได้ |
| N16 | §11.3 ซ้ำ SinMDM กับ §11.2 และไม่พูดถึง A0-2 | ลบซ้ำ + เพิ่มแถว A0-2 ใน §11.1 |

### 12.4 สิ่งที่ verifier ยืนยันว่าถูก
bibliographic metadata ทั้งหมด · 345 → 23, ฐานข้อมูล 3 + คำค้น 6, ช่วงปี/ภาษา · **ไม่มี figure ใด ๆ ใน PDF** (จึงไม่มี PRISMA diagram จริง), PRISMA ไม่มี reference entry · ตัวเลขทุกตัวใน §5 (93.33%, 62%, 13.5 mAP, 0.9358/3.88 cm/98%, 1,000 วิดีโอ/10 s/30 fps, 5.2 h/1,408 vs >5,000, 1,240 shots, 6-foot, 6 สัปดาห์/60 นาที/8 HD/4 ช่อง, 8 และ 12 นักเต้น, 8 genres, 53 จุด, 6 folk dances, "almost half"/MADMOM) · การนับ 24 / 22 แถว · §9 #1–#14 เป็นข้อผิดของเปเปอร์จริง (ไม่ใช่ artifact) · การอ้างเป็น [117] ใน A0-2 · Five Cs + ตาราง Proadpran ครบ และการตัดสินหยุดที่ pass 2 มีเหตุผล

### 12.5 คำตัดสินสุดท้าย
แก้ครบ 16 ข้อ → ใช้ได้เป็น KB entry · ข้อจำกัดที่เหลือ: **ไม่ได้เปิดเปเปอร์ต้นทาง** (Yalta, Hwang, Carlson, Lee, Jacob & Magerko) — ข้อที่ติดป้าย "อนุมาน" ยังต้องยืนยันกับต้นฉบับก่อนใช้ในวิทยานิพนธ์ · ไม่ได้ตรวจ SJR quartile ของวารสาร

---

## บทสรุปในประโยคเดียว
Review ฝั่งศิลปะที่ติดป้าย "systematic" (345 → 23 ชิ้น, 2010–2023, 4 หมวด) ที่มีประโยชน์จริงแค่ **กรอบจริยธรรม 5 ข้อ** และ **ตัวชี้ไปยัง Hwang 2020 / Carlson 2020** — ข้อเท็จจริงเกี่ยวกับงานแต่ละชิ้นในเปเปอร์นี้ผิดหลายจุด จึงต้องอ้างงานต้นฉบับแทนเสมอ
