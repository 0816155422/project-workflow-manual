# Shared AI Memory Workspace

พื้นที่ทำงานร่วมกันระหว่างมนุษย์กับ AI หลายแพลตฟอร์ม โดยใช้ไฟล์ Git เป็นความรู้ที่มีเวอร์ชัน ตรวจสอบที่มาได้ และผ่านการอนุมัติก่อนแชร์ ไม่ใช่ฐานข้อมูล real-time และไม่ใช่ที่เก็บ secret

## หลักการ
- shared/ เก็บข้อมูลโครงการและความรู้ที่กำหนดสถานะและแหล่งที่มา
- platforms/ เก็บ prompts, configs และ snapshots สำหรับ ChatGPT, Jamin, Claude, Gemini และแพลตฟอร์มอื่น
- private/ เป็นเพียงคำเตือนให้เก็บข้อมูลส่วนตัวไว้นอก Git; ห้าม commit ไฟล์ส่วนตัว
- config/ กำหนด privacy policy และ allowlist เชิงเอกสาร
- logs/ เก็บ metadata การอนุมัติ/การทำงานที่จำเป็น ไม่เก็บเนื้อหาลับ
- archives/ เก็บเอกสารเก่าที่ผ่านการตรวจสอบแล้ว โดยไม่ถือว่าเป็นข้อมูลปัจจุบัน
- docs/ อธิบาย workflow และวิธีทำงานร่วมกัน

## ทำไมใช้ repository เป็น shared memory
Git เก็บประวัติการเปลี่ยนแปลงและช่วยตรวจสอบ diff/ย้อนเวอร์ชันได้ เหมาะกับความรู้ที่ไม่เปลี่ยนทุกวินาที แต่ไม่รับประกัน real-time sync, ความถูกต้อง หรือการเชื่อมต่อกับบัญชี AI โดยอัตโนมัติ

## กฎการใช้
1. ใช้เฉพาะไฟล์ที่ผู้ใช้ระบุหรือไฟล์ shared/ ที่มีสถานะ APPROVED
2. ห้ามนำแชตเก่าหรือความจำส่วนตัวของ AI มาเป็นข้อมูลหลักโดยอัตโนมัติ
3. AI เสนอการเปลี่ยนแปลงได้ แต่ผู้ใช้/ผู้ตรวจต้องอนุมัติ
4. ห้าม commit token, API key, password, credentials หรือข้อมูลส่วนบุคคล/อ่อนไหว
5. ทุกการเขียนต้องตรวจสอบ read-back และ commit/PR
6. ไฟล์ใน repository สาธารณะอาจเปิดเผยต่อสาธารณะ

## เริ่มต้นใช้งาน
1. อ่าน MEMORY_MANIFEST.md และ docs/workflow.md
2. ตรวจ config/privacy-policy.json และ config/allowed-platforms.json
3. เติม shared/core/ และ shared/projects/ ด้วยสถานะ PROPOSED
4. เมื่อผู้ใช้ตรวจสอบแล้ว เปลี่ยนเป็น APPROVED พร้อมแหล่งที่มาและหลักฐานการอนุมัติ
5. เลือกไฟล์ที่จำเป็นส่งให้ AI แต่ละแพลตฟอร์มด้วยตนเอง; ไม่มี auto-sync จากแชต
6. ส่งข้อเสนอแก้ไขกลับเป็น diff/PR และตรวจสอบผลใน GitHub

## Dashboard และ API
- Dashboard source: hap-aicc/index.html
- GitHub Pages workflow: .github/workflows/deploy-pages.yml
- GitHub Actions read/write runner: .github/workflows/api-runner.yml
- MCP HTTP API implementation: MCP_API.md

หน้า GitHub Pages เป็น static site จึงแสดงข้อมูล/ลิงก์ได้ แต่ไม่ควรใส่ token ใน HTML และไม่สามารถเป็น secure write backend ด้วยตัวเองได้ ส่วน MCP HTTP API เป็นบริการแยกและจะใช้ได้ก็ต่อเมื่อ deploy และตั้งค่า secret อย่างปลอดภัย การมีไฟล์ API ใน repo ไม่ได้หมายความว่า endpoint ทำงานแล้ว

## โครงสร้างหลัก
README.md, MEMORY_MANIFEST.md, config/, shared/core/, shared/projects/, shared/knowledge/, platforms/{chatgpt,jamin,claude,gemini,others}/, private/, logs/, archives/old-context/, docs/, templates/, hap-aicc/index.html

สถานะที่ใช้: PROPOSED, APPROVED, REJECTED, SUPERSEDED, ARCHIVED. AI-generated content is not approved merely because it is stored in Git.
