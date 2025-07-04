
# SubstringSearch

ณ ดินแดน Algorithmia อันไกลโพ้น มีนักรบผู้กล้าชื่อว่า Byte เขาได้รับมอบหมายภารกิจสำคัญในการค้นหา "ร่องรอย" ที่ซ่อนอยู่ใน "แผนที่" โบราณ ร่องรอยนั้นคือลำดับอักษรลับที่อาจนำไปสู่ขุมทรัพย์มหาศาล Byte ต้องเขียนโปรแกรมเพื่อค้นหาว่าร่องรอยนั้นปรากฏอยู่ในแผนที่หรือไม่ และถ้าปรากฏ เขาต้องระบุตำแหน่งเริ่มต้นของร่องรอยนั้น

**Input**

บรรทัดแรก: ข้อความ `text` ซึ่งเป็นแผนที่โบราณ (ความยาวไม่เกิน 200 ตัวอักษร)
บรรทัดที่สอง: ข้อความ `pattern` ซึ่งเป็นร่องรอยที่ต้องการค้นหา (ความยาวไม่เกินความยาวของ `text`)

**Output**

ตำแหน่งเริ่มต้นของ `pattern` ใน `text` (นับจาก 0) หากไม่พบ `pattern` ใน `text` ให้พิมพ์ `-1`

**ตัวอย่าง**

<table>
<tr>
<th>Input</th>
<th>Output</th>
</tr>
<tr>
<td>
abcabcd<br>
abc
</td>
<td>
0
</td>
</tr>
<tr>
<td>
abcabcd<br>
bcd
</td>
<td>
2
</td>
</tr>
<tr>
<td>
abcabcd<br>
def
</td>
<td>
-1
</td>
</tr>
</table>

**ข้อกำหนด**

*   Time limit: 1000 ms
*   Memory limit: 256 MB
