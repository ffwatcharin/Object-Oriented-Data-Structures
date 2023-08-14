class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class  LinkedList:
    def __init__(self,data = None):
        
        self.size = 0
        self.head = Node(None)
        if data != None:
            for i in data:
                self.append(i)

    def __str__(self):
        i = 0
        result = 'link list : '
        p = self.head
        while p != None:
                if self.size == 0:
                    result = 'List is empty'
                elif p.data != None:
                    result += str(p.data)
                    if i < self.Size():
                        result += '->'
                p = p.next
                i += 1
        return result
    
    
    def isEmpty(self):
        return self.size == 0
    
    def Size(self):
        return self.size
    
    def append(self,data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.size += 1   
        
         
    def insert(self,index,data):
        i = 0
        if index >= 0 and index <= self.size:
            p = Node(data)
            print(f'index = {index} and data = {data}')
            if self.head == None:
                self.head = p
            else:
                t = self.head
                while i < index:
                    t = t.next
                    i += 1
                p.next = t.next
                t.next = p
                self.size += 1
        else:
            return print('Data cannot be added')      


inp = input('Enter Input : ').split(',')
lst_front = inp[0].split()
lst_add = []
for i in inp[1:]:
    lst_add.extend(i.split(':'))
    
c = LinkedList(lst_front)
print(c)
for i in range(len(lst_add)):
    if i % 2 == 0:
        c.insert(int(lst_add[i]),int(lst_add[i+1]))
        print(c)