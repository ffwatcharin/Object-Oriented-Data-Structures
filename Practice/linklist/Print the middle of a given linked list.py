class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def pushNode(self, head_ref, data_val):
        new_n = Node(data = data_val)
        new_n.next = head_ref[0]
        head_ref[0] = new_n

head = [None]
temp = LinkedList()
for i in range(5, 0, -1):
    temp.pushNode(head, i)
v = []
while head[0]:
    v.append(head[0].data)
    head[0] = head[0].next
print("Middle Value Of Linked List is :", v[len(v)//2])