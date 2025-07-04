
# Magical Crystals

ในดินแดนอันห่างไกล ที่ซึ่งเวทมนตร์ไหลเวียนดั่งสายน้ำ มีหมู่บ้านเล็กๆ ซ่อนตัวอยู่กลางป่าลึก ชาวบ้านที่นี่ดำรงชีวิตด้วยการเก็บผลึกวิเศษจากถ้ำศักดิ์สิทธิ์ที่ซ่อนอยู่ภายในป่า

ทุกๆ ปี เมื่อถึงฤดูเก็บเกี่ยว ชาวบ้านจะส่งนักผจญภัยเข้าไปในถ้ำเพื่อรวบรวมผลึกเหล่านี้ อย่างไรก็ตาม ผลึกแต่ละเม็ดมีพลังงานที่แตกต่างกัน และการเลือกผลึกที่มีพลังงานใกล้เคียงกันที่สุดเป็นสิ่งสำคัญ เพื่อให้การร่ายเวทของหมู่บ้านมีประสิทธิภาพสูงสุด

นักผจญภัยได้รับมอบหมายให้เลือกผลึกมา k เม็ดจากทั้งหมด n เม็ดที่พบในถ้ำ โดยมีเป้าหมายคือการทำให้ผลต่างของพลังงานระหว่างผลึกที่มีพลังงานมากที่สุดและน้อยที่สุดในกลุ่มที่เลือกนั้นมีค่าน้อยที่สุดเท่าที่จะเป็นไปได้

จงเขียนโปรแกรมเพื่อช่วยเหลือนักผจญภัยในการค้นหากลุ่มผลึก k เม็ดที่เหมาะสมที่สุด เพื่อให้หมู่บ้านสามารถร่ายเวทมนตร์ได้อย่างราบรื่นตลอดทั้งปี

**Input**

บรรทัดแรกประกอบด้วยจำนวนเต็มสองจำนวน n และ k (1 <= k <= n <= 1024) ซึ่งแสดงถึงจำนวนผลึกทั้งหมดและจำนวนผลึกที่ต้องเลือกตามลำดับ
บรรทัดที่สองประกอบด้วยจำนวนเต็ม n จำนวน ซึ่งแสดงถึงพลังงานของผลึกแต่ละเม็ด (1 <= พลังงาน <= 1000)

**Output**

พิมพ์ค่าผลต่างที่น้อยที่สุดที่เป็นไปได้ระหว่างผลึกที่มีพลังงานมากที่สุดและน้อยที่สุดในกลุ่มผลึก k เม็ดที่เลือก

**ตัวอย่าง**

<table>
  <tr>
    <td>Input</td>
    <td>Output</td>
  </tr>
  <tr>
    <td>5 3<br>10 4 7 2 9</td>
    <td>5</td>
  </tr>
  <tr>
    <td>5 2<br>10 4 7 2 9</td>
    <td>2</td>
  </tr>
</table>

**ข้อกำหนด**

*   Time limit: 1000 ms
*   Memory limit: 512 MB
