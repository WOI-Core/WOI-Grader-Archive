
# ConquerTheKingdom

กาลครั้งหนึ่งนานมาแล้ว มีอาณาจักรที่ยิ่งใหญ่ชื่อว่า "อัลโกริทเมีย" อาณาจักรนี้ประกอบด้วยเมืองน้อยใหญ่มากมาย แต่ละเมืองมีความมั่งคั่งแตกต่างกัน พระราชาผู้ชาญฉลาดต้องการเลือกเมืองที่มั่งคั่งเป็นอันดับที่ k เพื่อเป็นเมืองหลวงแห่งใหม่ แต่ด้วยจำนวนเมืองที่มากมาย ทำให้การค้นหาเป็นไปได้ยาก พระราชาจึงต้องการความช่วยเหลือจากนักเขียนโปรแกรมผู้เก่งกาจ เพื่อค้นหาเมืองที่มั่งคั่งเป็นอันดับที่ k อย่างรวดเร็ว เพื่อที่จะนำความสงบสุขและความเจริญรุ่งเรืองมาสู่อาณาจักร

**Input**

บรรทัดแรกประกอบด้วยจำนวนเต็มสองจำนวน `n` และ `k` โดยที่ `n` คือจำนวนเมืองทั้งหมดในอาณาจักร (1 <= n <= 1000) และ `k` คืออันดับความมั่งคั่งที่ต้องการ (1 <= k <= n)
บรรทัดที่สองประกอบด้วยจำนวนเต็ม `n` จำนวน ซึ่งแสดงถึงความมั่งคั่งของแต่ละเมือง (1 <= ความมั่งคั่ง <= 1000)

**Output**

แสดงความมั่งคั่งของเมืองที่มั่งคั่งเป็นอันดับที่ `k`

**ตัวอย่าง**

<table>
  <tr>
    <th>Input</th>
    <th>Output</th>
  </tr>
  <tr>
    <td>
      5 3<br>
      3 1 4 1 5
    </td>
    <td>
      3
    </td>
  </tr>
  <tr>
    <td>
      10 1<br>
      10 9 8 7 6 5 4 3 2 1
    </td>
    <td>
      1
    </td>
  </tr>
</table>

**ข้อกำหนด**

*   Time Limit: 1000 ms
*   Memory Limit: 256 MB
