# MEMORY MANIFEST — Shared AI Memory Workspace

## Purpose
Repository นี้เป็นแหล่งความรู้และ working memory ที่มีเวอร์ชันและผ่านการอนุมัติสำหรับ AI หลายแพลตฟอร์ม ไม่ใช่ฐานข้อมูล real-time และไม่ใช่ที่เก็บ secret

## Memory classes
- **Approved shared memory:** ข้อมูลใน shared/ ที่มีสถานะ APPROVED พร้อมแหล่งที่มาและผู้อนุมัติ
- **Private memory:** ข้อมูลเฉพาะบุคคล/เครื่อง เก็บไว้นอก repository ห้าม push ขึ้น GitHub
- **Platform memory:** snapshots, prompts และ configs ใน platforms/ ไม่ถือว่าเป็น shared memory ที่อนุมัติแล้วโดยอัตโนมัติ
- **Archive:** ข้อมูลเก่าที่เก็บเพื่ออ้างอิง ไม่ถือเป็นสถานะปัจจุบัน
- **Draft/proposed:** ข้อมูลที่ยังไม่ผ่านการอนุมัติ

## Approval and provenance
1. ข้อมูลที่จะแชร์ต้องระบุสถานะ เช่น PROPOSED, APPROVED, REJECTED, SUPERSEDED หรือ ARCHIVED
2. ผู้ใช้หรือผู้ดูแลที่ได้รับมอบหมายเป็นผู้อนุมัติ ไม่ใช่ AI ผู้เขียน
3. ใช้ commit/PR พร้อมเหตุผล และบันทึกการตัดสินใจสำคัญใน shared/projects/decision-log.md
4. ห้ามอ้างว่าบันทึกหรืออนุมัติแล้วหากยังไม่มีผลที่ตรวจสอบได้

## No automatic import
- ห้ามนำแชตเก่าหรือความจำส่วนตัวของโมเดลมาเป็นข้อเท็จจริงร่วมโดยอัตโนมัติ
- ใช้เฉพาะไฟล์ที่ผู้ใช้ระบุ หรือไฟล์ shared/ ที่อนุมัติแล้ว
- หากข้อมูลจำเป็นไม่มี ให้ถามผู้ใช้แทนการเดา
- export/import ระหว่างแพลตฟอร์มต้องเริ่มโดยผู้ใช้และตรวจสอบได้

## Privacy
ห้าม commit token, API key, password, credentials, private keys, cookies หรือข้อมูลส่วนบุคคล/อ่อนไหว โฟลเดอร์ private/ เป็นเพียง placeholder; เก็บไฟล์จริงไว้นอก Git Logs บันทึกเฉพาะ metadata ที่จำเป็น

## Conflict and freshness
Git history เป็นหลักฐานเวอร์ชัน ไม่ได้ยืนยันว่าข้อมูลล่าสุดถูกต้อง หากแหล่งข้อมูลขัดแย้งให้ระบุแต่ละแหล่งและวันที่ แล้วขอผู้ใช้ตัดสิน ห้ามนำ archive กลับมาใช้เป็นสถานะปัจจุบันโดยอัตโนมัติ

## Workflow
Read allowed files → summarize sources/uncertainty → propose changes → obtain human approval → commit → verify read-back → record minimal audit metadata.
