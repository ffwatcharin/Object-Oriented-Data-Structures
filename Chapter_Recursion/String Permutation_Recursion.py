# พี่อยากให้น้องๆ หา string ทุกตัวที่เป็นไปได้จาก string ที่พี่ให้หน่อย ว่าง่ายๆ คือการประกอบคำนั่นเอง หรือที่เขาเรียกกันว่า String Permutation เป็นการเอาตัวอักษรแต่ละตัวจาก 
# string ที่ให้ไปนำไปสร้าง string ที่มีความเป็นไปได้ทั้งหมด จากตัวอักษรของ string ที่ได้รับมา

# Input มี 2 ค่า

#   string ที่จะนำมาหา Permutation
#   k = ขนาดของ string ที่จะสร้างขึ้นมาใหม่

# โดยหลักการมีดังนี้
#   1.ฟังก์ชัน `permute_string` รับพารามิเตอร์ 2 ตัวคือ string `s` และ integer `k` ที่แทนจำนวนตัวอักษรที่จะถูกสับเปลี่ยนตำแหน่ง
#   2.ฟังก์ชันตรวจสอบว่า `k` มีค่าน้อยกว่า 0 หรือไม่ ถ้าใช่ จะเกิด `ValueError` ที่ระบุว่าไม่อนุญาตให้ใช้ค่า `k` ที่เป็นลบ โดยให้ return "Invalid value of k. k must be a non-
#   negative integer."
#   3.ภายในฟังก์ชัน `generate_permutations` มีการใช้ recursive เพื่อสร้างทุกความเป็นไปได้ของการสับเปลี่ยนตำแหน่งของความยาว `k` จาก string `s` ที่กำหนด. ถ้า `k` 
#   เป็น 0 จะ return เป็น string ว่าง
#   4.ในส่วน recursion ฟังก์ชันวนลูปผ่านแต่ละตัวอักษรใน string `s` โดยนำตัวอักษรปัจจุบันมาเป็น "prefix" และสร้างการสับเปลี่ยนตำแหน่งของตัวอักษรที่เหลือโดยใช้ 
#      recursive ด้วยความยาวที่ลดลงเป็น `k - 1`
#   5.ส่วนหลักการในการทำการสร้างการสับเปลี่ยนตำแหน่งทั้งหมดของความยาว `k` โดยใช้ฟังก์ชัน `generate_permutations` และในผลลัพธ์อาจมี string ที่สับเปลี่ยนแล้วซ้ำ
#   กัน ให้เปลี่ยนผลลัพธ์เป็น string ที่มีความ unique เท่านั้น เช่น ['abb', 'bab', 'bba', 'abb'] -> ['abb', 'bab', 'bba']
#   6.สุดท้าย แต่ละ string ที่เป็นไปได้หลังจากหา unique และทำการ sorted

# หมายเหตุ : ใครไม่รู้อะไร หรือ สงสัย สามารถสอบถาม TA ได้เลยครับ

def permute_string(s, k):

    if k < 0:
        return 'Invalid value of k. k must be a non-negative integer.'
    if k > len(s):
        return 'Invalid value of k. k must be less than or equal to the length of the string.'

    def generate_permutations(pref, remian, l):
        if l == 0:
            return [pref]

        permute = []
        for i in range(len(remian)):
            new_pre = pref + remian[i]
            new_remain = remian[:i] + remian[i+1:]
            permute.extend(generate_permutations(new_pre, new_remain, l - 1))

        return permute

    permute = generate_permutations("", s, k)
    uniq_permute = list(set(permute))
    sort_permute = sorted(uniq_permute)

    return sort_permute


def main():
    inp, k = input("Enter a string and k: ").split('/')
    k = int(k)

    print(permute_string(inp, k))


if __name__ == '__main__':
    main()
