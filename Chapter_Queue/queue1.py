class Queue():
    def __init__(self):
        self.lst = []

    def dequeue(self):
        del self.lst[0]

    def enqueue(self, x):
        self.lst.append(x)

    def item(self):
        return (self.lst[0])


inp = input('Enter Input : ').split(',')
q = Queue()
for i in range(len(inp)):
    b = inp[i].split(' ')
    if inp[i][0] == 'E':
        q.enqueue(int(b[1]))
        print(len(q.lst))
    elif inp[i][0] == 'D':
        if len(q.lst) == 0:
            print('-1')
        else:
            print(q.item(), '0')
            q.dequeue()
if len(q.lst) == 0:
    print('Empty')
else:
    print(*q.lst, sep=' ')
