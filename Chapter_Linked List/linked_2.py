class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

    def __str__(self) -> str:
        return f'{self.data}'


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def __str__(self) -> str:
        return ' -> '.join([str(x) for x in self.items])


inp = input("Enter Input : ").split(",")


q = Queue()
posi = None
s_back = False
s_fw = False


for sec in inp:
    try:
        action, data = sec.split(" ")
    except:
        action = sec
    if action == "E":
        n = Node(data)
        if not posi:
            posi = n
            web = Node("welcome.com")
            n.pre = web
        else:
            posi.next = n
            n.pre = posi
            posi = n
        q.enqueue(posi)
    elif action == "B":
        if posi.pre and posi:
            # if posi.next :
            #     posi.next = None
            s_back = True
            posi = posi.pre
            if posi.data == "welcome.com":
                continue
            q.enqueue(posi)
    elif action == "F":
        if posi and posi.next:
            # if posi.pre :
            #     posi.pre = None
            posi = posi.next
            q.enqueue(posi)
print("History :", q)
s = []
while posi:
    if posi.pre and posi:
        if posi.data == "welcome.com":
            continue
        s.append(posi.data)
        if posi.next:
            posi.next = None

        posi = posi.pre

    else:
        if posi.data == "welcome.com":
            break
        s.append(posi.data)
        break
print("BackPath :", " -> ".join(s))
