# รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์
# เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที


# แล้วแสดงผลเป็น วินาที
# แสดงผลตามตัวอย่าง

print("*** Converting hh.mm.ss to seconds ***")
h, m, s = input("Enter hh mm ss : ").split()

h = int(h)
m = int(m)
s = int(s)

total = (h * 3600) + (m * 60) + s

if m >= 60 or m < 0:
    print(f"mm({m}) is invalid!")
else:
    print(f"{h:02d}:{m:02d}:{s:02d} = {total:,} seconds")
