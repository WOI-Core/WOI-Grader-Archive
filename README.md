-----

# 📚 WOI-Grader-Archive

นี่คือแหล่งรวมโจทย์และสื่อการเรียนรู้สำหรับ **Walailak University Olympiad in Informatics (WOI)** ค่าย 1 ถึง ค่าย 3 ของเรา

-----

## 🎯 เกี่ยวกับ Repository นี้

Repository นี้ถูกสร้างขึ้นเพื่อเป็น **ศูนย์รวมโจทย์และเนื้อหาสำคัญ** ที่ใช้ในการฝึกฝนและเตรียมความพร้อมสำหรับนักเรียนที่เข้าร่วมค่าย **Walailak University Olympiad in Informatics (WOI)** ตั้งแต่ค่ายเริ่มต้น (ค่าย 1) ไปจนถึงค่ายระดับสูง (ค่าย 3) โดยเน้นการรวบรวมโจทย์ที่ใช้ในระบบ **Grader** หรือระบบตรวจอัตโนมัติ เพื่อให้นักเรียนได้ฝึกฝนเหมือนจริง

-----

## 💡 เนื้อหาที่คุณจะพบ

ภายใน Repository นี้ คุณจะพบกับ:

  * **โจทย์ฝึกฝน (Practice Problems):** โจทย์จากค่าย WOI ในปีก่อนๆ รวมถึงโจทย์ที่คัดสรรมาเพื่อเสริมสร้างความเข้าใจในแต่ละหัวข้อ พร้อมรองรับการนำไปใช้ในระบบ Grader
  * **เฉลยและแนวคิด (Solutions & Approaches):** สำหรับโจทย์บางข้อ อาจมีเฉลยหรือแนวคิดเบื้องต้นเพื่อช่วยให้เข้าใจวิธีการแก้ปัญหา
  * **สื่อการสอน/สไลด์ (Lecture Materials/Slides):** เอกสารประกอบการบรรยาย หรือสไลด์ที่ใช้สอนในค่าย เพื่อทบทวนเนื้อหาสำคัญ
  * **ตัวอย่างโค้ด (Sample Codes):** ตัวอย่างการใช้งานอัลกอริทึม หรือโครงสร้างข้อมูลที่สำคัญ เพื่อเป็นแนวทางในการนำไปปรับใช้
  * **Test Cases (ถ้ามี):** ชุดข้อมูลทดสอบ (Input/Output) สำหรับโจทย์บางข้อ เพื่อให้สามารถทดสอบโค้ดด้วยตนเองได้
  * **Scripts (ถ้ามี):** สคริปต์หรือโค้ดที่ใช้ในการสร้าง Test Cases สำหรับโจทย์นั้นๆ
  * **แหล่งข้อมูลเพิ่มเติม (Additional Resources):** ลิงก์ไปยังบทความ, เว็บไซต์, หรือตำราที่เกี่ยวข้องเพื่อการศึกษาด้วยตนเอง

-----

## 🗺️ โครงสร้าง Repository

Repository นี้จะจัดระเบียบเนื้อหาตามค่ายและหัวข้อ เพื่อให้ง่ายต่อการค้นหาและเข้าถึง:

```
.
├── Camp1/                   # เนื้อหาและโจทย์สำหรับค่าย 1 (พื้นฐาน)
│   ├── TaskName/
│       ├── Problems/        # ไฟล์โจทย์ (เช่น streetfighter.md, streetfighter.pdf)
│       ├── Solutions/       # (ถ้ามี) เฉลยหรือแนวคิด (เช่น streetfighter.cpp)
│       ├── TestCases/       # (ถ้ามี) ชุดข้อมูลทดสอบ (เช่น input/input01.txt, output/output01.txt)
│       └── Scripts/         # (ถ้ามี) สคริปต์สำหรับสร้าง Test Cases
├── Camp2/                   # เนื้อหาและโจทย์สำหรับค่าย 2 (ระดับกลาง)
│   ├── TaskName/
│       ├── Problems/        # ไฟล์โจทย์ (เช่น investor.md, investor.pdf, investor.docx)
│       ├── Solutions/       # (ถ้ามี) เฉลยหรือแนวคิด (เช่น investor.cpp)
│       ├── TestCases/       # (ถ้ามี) ชุดข้อมูลทดสอบ (เช่น input/input1.in, output/output1.txt)
│       └── Scripts/         # (ถ้ามี) สคริปต์สำหรับสร้าง Test Cases
├── Camp3/                   # เนื้อหาและโจทย์สำหรับค่าย 3 (ระดับสูง)
│   ├── TaskName/
│       ├── Problems/        # ไฟล์โจทย์ (เช่น disaster_dragon.pdf)
│       ├── Solutions/       # (ถ้ามี) เฉลยหรือแนวคิด (เช่น disaster_dragon.cpp)
│       ├── TestCases/       # (ถ้ามี) ชุดข้อมูลทดสอบ (เช่น input/input01.txt, output/output01.txt)
│       └── Scripts/         # (ถ้ามี) สคริปต์สำหรับสร้าง Test Cases
├── Contests/
│   ├── ContestName/                   # เนื้อหาและโจทย์สำหรับ Contest ย่อยในค่าย
│       ├── TaskName/
│           ├── Problems/        # ไฟล์โจทย์ (เช่น disaster_dragon.pdf)
│           ├── Solutions/       # (ถ้ามี) เฉลยหรือแนวคิด (เช่น disaster_dragon.cpp)
│           ├── TestCases/       # (ถ้ามี) ชุดข้อมูลทดสอบ (เช่น input/input01.txt, output/output01.txt)
│           └── Scripts/         # (ถ้ามี) สคริปต์สำหรับสร้าง Test Cases
├── TUSCO/                   # เนื้อหาและโจทย์สำหรับ TUSCO
    ├── TaskName/
        ├── Problems/        # ไฟล์โจทย์ (เช่น disaster_dragon.pdf)
        ├── Solutions/       # (ถ้ามี) เฉลยหรือแนวคิด (เช่น disaster_dragon.cpp)
        ├── TestCases/       # (ถ้ามี) ชุดข้อมูลทดสอบ (เช่น input/input01.txt, output/output01.txt)
        └── Scripts/         # (ถ้ามี) สคริปต์สำหรับสร้าง Test Cases
```

-----

## 🚀 เริ่มต้นใช้งาน

คุณสามารถ `git clone` Repository นี้เพื่อเข้าถึงไฟล์ทั้งหมด หรือดาวน์โหลดเป็นไฟล์ ZIP ก็ได้

```bash
git clone https://github.com/WOI-Core/woi-grader-archive.git
```

-----

## 🤝 การมีส่วนร่วม

หากคุณมีข้อเสนอแนะ, ต้องการแก้ไขข้อมูล, หรือต้องการเพิ่มโจทย์/เนื้อหาที่เป็นประโยชน์ สามารถ [เปิด Issue](https://www.google.com/search?q=https://github.com/WOI-Core/woi-grader-archive/issues) หรือ [ส่ง Pull Request](https://www.google.com/search?q=https://github.com/WOI-Core/woi-grader-archive/pulls) เข้ามาได้เลย\!

-----

# Kim Slick The Legendary \!\!\!
