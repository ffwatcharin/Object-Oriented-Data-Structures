class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        # กำหนดตัวแปร current ให้เท่ากับหัวของ linked list
        current = self.head  
        
        # สร้างรายการชั่วคราวที่จะใช้ในการเก็บข้อมูลจาก linked list.
        data_list = []

        # เริ่มลูป while เพื่อวนลูปผ่าน linked list จนกว่า current จะกลายเป็น None
        while current != None:  

            # เพิ่มข้อมูลจาก current.data (ข้อมูลใน node ปัจจุบัน) เข้าใน data_list และแปลงข้อมูลนั้นเป็นสตริง.
            data_list.append(str(current.data))

        # current ไปยัง node ถัดไปใน linked list
            current = current.next

        # สลับลำดับของ data_list โดยใช้สัญลักษณ์ [::-1] (สลับ)
        reversed_data_list = data_list[::-1]

        # สุดท้ายคืนค่าสตริงที่เกิดขึ้นจาก join() เป็นผลลัพธ์ของฟังก์ชัน __str__.
        return ' -> '.join(reversed_data_list)

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


inp = input('Enter Input : ').split()
c = LinkedList()

for item in inp:
    c.insert(item)

c.reverse()
print(c)
