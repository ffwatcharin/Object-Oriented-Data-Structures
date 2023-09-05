class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        data_list = []
        while current != None:
            data_list.append(str(current.data))
            current = current.next
            
        reversed_data_list = data_list[::-1]
        return ' -> '.join(reversed_data_list)

    def reverse(self):
        temp = None
        current = self.head

        while current != None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp != None:
            self.head = temp.prev

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head != None:
            self.head.prev = new_node
        self.head = new_node


inp = input('Enter Input : ').split()
c = DoublyLinkedList()

for item in inp:
    c.insert(item)

c.reverse()
print(c)
