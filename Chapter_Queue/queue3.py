class Queue:
    def __init__(self, list=None):
        self.error_d = 0
        self.error_inp = 0
        self.last_num = -1

        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            self.error_d += 1

    def size(self):
        return len(self.items)

    def peek(self):
        if self.isEmpty():
            return 0
        else:
            return self.items[-1]


def Output(l):
    ans = []
    for i in l:
        ans.append("*%d" % i)
    return ans


q = Queue()
s = Queue()

inp = input('input : ').split(',')
q.items = inp

for i in q.items:
    print("Step : %s" % i)
    j = 0

    if i[j] == 'E' and i[1::1].isdigit():
        n1 = int(i[1::1])
        if n1 > 0:
            if s.isEmpty():
                for k in range(s.last_num+1, n1+(s.last_num)+1):
                    s.enqueue(k)

            else:
                for k in range(s.peek()+1, int(s.peek())+1+n1):
                    s.enqueue(k)

            s.last_num = s.peek()

        print("Enqueue :", Output(s.items))

    elif i[j] == 'D' and i[1::1].isdigit():
        n2 = int(i[1::1])
        if n2 > 0:
            for r in range(0, n2):
                s.dequeue()

        print("Dequeue :", Output(s.items))

    else:
        s.error_inp += 1
        print(Output(s.items))

    print("Error Dequeue : %d" % s.error_d)
    print("Error input : %d" % s.error_inp)
    print('--------------------')
