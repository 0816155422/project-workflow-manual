# แนวทางอัปเดต State / Status ของ IRIS/SMPE

> สถานะเอกสาร: **แนวทางการทำงาน**  
> ขอบเขต: ใช้จัดเก็บและปรับปรุงรายการ State/Status ที่รวบรวมจากหลายบริบท  
> ข้อจำกัดปัจจุบัน: รายการที่มาจากบทสนทนาและหลักฐานเชิงประวัติยังไม่ใช่ Canonical State Registry

## 1. วัตถุประสงค์

กำหนดวิธีเพิ่ม แก้ไข ตรวจสอบ และอนุมัติข้อมูล State/Status ให้ตรวจสอบย้อนหลังได้ โดยไม่รวมสถานะจากคนละ namespace เข้าด้วยกันโดยพลการ และไม่เขียนทับประวัติเดิม

## 2. หลักการบังคับใช้

1. **แยก namespace และ lifecycle** เช่น Runtime State Machine, Verification, Evidence, Provenance, Recovery, Capability และ Work Cycle Phase ห้ามถือว่าทั้งหมดเป็น enum หรือ state machine ชุดเดียวกัน เว้นแต่ source contract จะระบุไว้โดยตรง
2. **รักษาประวัติแบบเพิ่มต่อท้าย** ห้ามลบหรือแก้ไขรายการประวัติเดิม การแก้ไขให้เพิ่ม revision หรือ correction entry ใหม่ พร้อมอ้างถึงรายการที่แก้
3. **แยกคำบอกเล่าจากหลักฐานต้นทาง** ข้อความจากผู้ใช้หรือบทสนทนาบันทึกเป็นหลักฐานตามที่ได้รับ แต่ไม่ถือเป็นการยืนยันจาก runtime/source โดยอัตโนมัติ
4. **ไม่ยกระดับเป็น canonical โดยอนุมาน** การพบชื่อสถานะในเอกสารหรือรายงานไม่ได้พิสูจน์ว่าเป็นค่า runtime ที่ระบบใช้อยู่
5. **บันทึกขอบเขตการตรวจ** คำว่า `NOT_FOUND` ต้องไม่ถูกใช้แทนข้อสรุปว่าไม่มีอยู่ ให้ระบุไฟล์, branch/commit, เครื่องมือ และ scope ที่ตรวจแล้ว
6. **ไม่บันทึกความลับ** ห้ามใส่ token, รหัสผ่าน, API key, credential หรือข้อมูลส่วนบุคคลอ่อนไหว

## 3. การเพิ่มหรืออัปเดตรายการ

ทุกการเปลี่ยนแปลงต้องเพิ่มบันทึกใหม่ โดยมีข้อมูลอย่างน้อยดังนี้:

- รหัส revision หรือรายการเปลี่ยนแปลงที่ไม่ซ้ำ
- วันเวลา (ระบุเขตเวลา หรือใช้ ISO 8601)
- ผู้เสนอ/ผู้ตรวจ/ผู้อนุมัติ แยกบทบาทกันเมื่อทราบ
- namespace และชื่อ State/Status/Phase
- คำอธิบายและบริบทการใช้งาน
- ประเภทแหล่งที่มา: source code, runtime, test, contract, เอกสาร, ผู้ใช้ให้ข้อมูล หรือหลักฐานเชิงประวัติ
- reference ที่ตรวจซ้ำได้: repository, path, branch/commit, URL, test/run ID หรือ artifact ID
- วิธีตรวจและขอบเขตที่ตรวจ
- ผลการตรวจ พร้อมแยก observation ออกจาก inference
- สถานะหลักฐานและการตัดสินใจ: draft, under review, accepted, rejected, superseded หรือยังไม่ยืนยัน
- รายการเดิมที่ถูกแทนที่หรือแก้ไข (ถ้ามี) โดยไม่ลบรายการเดิม

ตัวอย่างแบบฟอร์ม:

```md
## Revision: <unique-id>
- Recorded at: <ISO-8601 timestamp>
- Proposed by: <person/AI/system>
- Reviewed by: <reviewer or NOT_REVIEWED>
- Approved by: <authorized approver or PENDING>
- Namespace: <namespace>
- Token: <exact state/status/phase name>
- Meaning/context: <definition and usage context>
- Source class: <source/runtime/test/contract/document/user/historical>
- Evidence: <repository, path, commit, URL, test/run or artifact reference>
- Inspection scope: <what was actually checked>
- Observation: <directly observed facts>
- Inference: <interpretation, if any>
- Evidence status: <status and rationale>
- Decision: <DRAFT/ACCEPTED/REJECTED/SUPERSEDED>
- Supersedes/corrects: <prior revision or NONE>
- Notes: <limitations, including NOT_HASHABLE if applicable>
```

## 4. การตรวจสอบก่อนยกระดับเป็น Canonical

รายการจะ **ยังคง draft/non-canonical** จจนกว่าจะ:

1. พบ source artifact หรือ contract ต้นทางที่เกี่ยวข้อง เช่น `models.py`, `controller.py`, UserScript/Runtime, state diagram หรือ test oracle
2. บันทึก path และ commit/version ของ artifact และตรวจเนื้อหาจริง ไม่ใช้เพียงชื่อไฟล์หรือคำอ้างจากรายงาน
3. ตรวจว่า token สะกดตรงกันและมีความหมาย/transition ที่รองรับใน namespace นั้น
4. แยกค่าที่ถูกนิยามไว้ ค่าที่ถูกใช้จริง และค่าที่พบเฉพาะในเอกสาร/การทดสอบ
5. ระบุผล runtime test แยกจาก static/source inspection; การตรวจ syntax ไม่ถือเป็น runtime verification
6. ให้ผู้มีอำนาจอนุมัติการยกระดับอย่างชัดเจน และบันทึกผู้อนุมัติ ขอบเขต และวันที่

หาก source/runtime artifact ยังไม่พบ ให้บันทึก `NOT_FOUND_IN_INSPECTED_SCOPE` พร้อม scope ที่ตรวจ และคงรายการไว้เป็น historical/user-supplied/draft ตามหลักฐานจริง ห้ามสรุปว่าไม่มีอยู่ในระบบทั้งหมด

## 5. การเก็บประวัติและไฟล์

- เก็บแนวทางนี้เป็นเอกสารอธิบายกระบวนการ ไม่ใช่ registry ที่ยืนยันค่าทั้งหมดแล้ว
- เก็บ registry draft, source-evidence index และ decision/change log แยกหน้าที่กัน
- ใช้ Git commit/Pull Request เพื่อเก็บประวัติการเปลี่ยนแปลง และอ้าง commit ในบันทึก
- หากต้องส่ง ZIP ให้ระบุ commit ต้นทางและเวลาสร้าง ZIP; ZIP เป็น snapshot สำหรับตรวจ ไม่ใช่หลักฐานที่ป้องกันการแก้ไขด้วยตัวเอง
- SHA-256 ใช้ตรวจว่าข้อมูลตรงกับ manifest ที่เชื่อถือได้หรือไม่ แต่ manifest ที่อยู่ใน ZIP เดียวกันไม่ได้พิสูจน์ความถูกต้องโดยลำพัง
- ห้ามเขียนทับไฟล์ประวัติโดยไม่มีการยืนยันชัดเจนจากผู้มีอำนาจ หากได้รับอนุมัติให้แก้เนื้อหาปัจจุบัน ให้เก็บสำเนา/revision เดิมและเพิ่มบันทึกการเปลี่ยนแปลงก่อน

## 6. การอ่านรายการที่รวบรวมจากบทสนทนา

รายการ State/Status ที่ผู้ใช้ส่งมาจาก current conversation และ prior context ให้บันทึกแหล่งที่มาเป็น user-provided/historical ตามกรณี และคง `[NOT_HASHABLE]` หากไม่มี artifact ต้นทางเดียวให้ hash รายการดังกล่าวเป็น **candidate inventory** เท่านั้น ไม่ใช่ canonical registry จนกว่าจะตรวจเทียบ source/runtime artifact และได้รับการยืนยันตามข้อ 4

## 7. ตัวอย่างการแก้ไขโดยไม่ลบประวัติ

หากภายหลังตรวจพบว่า `WAIT_COPY` มีความหมายต่างจากคำอธิบายเดิม:

1. อย่าแก้หรือลบ revision เดิม
2. เพิ่ม revision ใหม่ ระบุ token, namespace, หลักฐานและความหมายที่แก้ไข
3. เชื่อมรายการใหม่กับ revision เดิมใน `Supersedes/corrects`
4. บันทึกการอนุมัติและ commit ที่นำการแก้ไขเข้า repository
5. ในมุมมองปัจจุบันอาจแสดงรายการใหม่เป็นค่าปัจจุบัน แต่ต้องให้ผู้ตรวจย้อนดูรายการเดิมได้

## 8. แหล่งอ้างอิงของกระบวนการใน repository

- [AI Collaboration Guide](ai-collaboration-guide.md)
- [Approval Policy](approval-policy.md)
- [Reporting Rules](reporting-rules.md)
- [Memory Manifest](../MEMORY_MANIFEST.md)
