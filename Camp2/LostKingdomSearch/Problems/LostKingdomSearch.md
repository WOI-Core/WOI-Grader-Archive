
# Lost Kingdom Search

นานมาแล้ว มีอาณาจักรที่สาบสูญชื่อว่า "Lost Kingdom" ซึ่งเต็มไปด้วยสมบัติล้ำค่ามากมาย ว่ากันว่ากุญแจสำคัญในการค้นหา Lost Kingdom คือการค้นหาตำแหน่งของสิ่งของวิเศษในคลังสมบัติโบราณ

คลังสมบัติมีลักษณะเป็นแถวเรียงหนึ่งของหีบสมบัติ แต่ละหีบมีหมายเลขกำกับ ภายในหีบอาจมีสิ่งของวิเศษซ่อนอยู่หรือไม่ก็ได้ นักผจญภัยผู้กล้าหาญได้รับแผนที่ซึ่งระบุหมายเลขของหีบสมบัติทั้งหมด และรายการของสิ่งของวิเศษที่เขาต้องค้นหา

ภารกิจของคุณคือการช่วยนักผจญภัยค้นหาตำแหน่งของหีบสมบัติที่เก็บสิ่งของวิเศษที่เขากำลังตามหา โดยที่เขาต้องการทราบว่าสิ่งของวิเศษแต่ละชิ้นอยู่ที่หีบหมายเลขอะไร หากไม่มีสิ่งของวิเศษที่ต้องการในคลังสมบัติ ให้รายงานว่า "-1"

**Input**

บรรทัดแรกประกอบด้วยจำนวนเต็มสองจำนวน `n` และ `q` (1 <= n <= 10000, 1 <= q <= 100) แทนจำนวนหีบสมบัติในคลัง และจำนวนสิ่งของวิเศษที่นักผจญภัยต้องการค้นหา ตามลำดับ

บรรทัดที่สองประกอบด้วยจำนวนเต็ม `n` จำนวน ซึ่งแสดงถึงหมายเลขของหีบสมบัติแต่ละหีบ (หีบสมบัติถูกเรียงลำดับจากน้อยไปมาก)

บรรทัดที่สามประกอบด้วยจำนวนเต็ม `q` จำนวน ซึ่งแสดงถึงสิ่งของวิเศษที่นักผจญภัยต้องการค้นหา

**Output**

สำหรับสิ่งของวิเศษแต่ละชิ้นที่นักผจญภัยต้องการค้นหา ให้พิมพ์ตำแหน่ง (index) ของหีบสมบัติที่เก็บสิ่งของนั้น (index เริ่มต้นที่ 0) หากไม่พบสิ่งของวิเศษในคลังสมบัติ ให้พิมพ์ "-1"

**ตัวอย่าง**

<table>
    <tr>
        <th>Input</th>
        <th>Output</th>
    </tr>
    <tr>
        <td>
            5 3<br>
            2 5 7 8 11<br>
            5 8 1
        </td>
        <td>
            1<br>
            3<br>
            -1
        </td>
    </tr>
</table>

**ข้อกำหนด**

*   Time limit: 1000 ms
*   Memory limit: 256 MB
