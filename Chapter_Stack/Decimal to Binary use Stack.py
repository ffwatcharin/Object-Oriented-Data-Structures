class Stack():
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list()
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
def dec2bin(decnum):

    s = Stack()
    binary = ""

    while decnum > 0:
        s.push(decnum % 2)
        decnum = decnum // 2

    while s.size() != 0:
        binary += str(s.pop())
    return binary


    ### Enter Your Code Here ###

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))