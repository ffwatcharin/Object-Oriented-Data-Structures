# จงเขียนฟังก์ชั่นที่แสดงผลเลข 1 จนถึง n

# และฟังก์ชั่นที่แสดงผลเลขตั้งแต่ n จนถึง 1

# โดยแสดงผลตามตัวอย่าง

# ****ห้ามใช้คำสั่ง len, for, while, do while, split*****

# หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว

def print1ToN(n):
    if n < 0:
        return print('1 ', end='')
    elif n >= 1:
        print1ToN(n - 1)
        print(n, end=' ')

def printNto1(n):
    if n < 0:
        return print('1', end='')
    elif n >= 1:
        print(n, end=' ')
        printNto1(n - 1)

def main():
    n = int(input("Enter Input : "))

    if n > 0 :
        print1ToN(n)
        printNto1(n)
    else:
        print('1 1')

if __name__ == "__main__":
    main()