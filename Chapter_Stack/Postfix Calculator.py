class Stack():

    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return (self.items)
    
    def peek(self):
        return self.items[-1]


def postFixeval(st):

    s = Stack()
    for i in st:
        if i == "+" or i == "-" or i == "/" or i == "*":
            if i == "+":
                first_num = s.pop()
                last_num = s.pop()
                temp = last_num + first_num
                s.push(temp)
            elif i == "-":
                first_num = s.pop()
                last_num = s.pop()
                temp = last_num - first_num
                s.push(temp)
            elif i == "/":
                first_num = s.pop()
                last_num = s.pop()
                temp = last_num / first_num
                s.push(temp)
            else:
                first_num = s.pop()
                last_num = s.pop()
                temp = last_num * first_num
                s.push(temp)
        else:
            s.push(int(i))

    ### Enter Your Code Here ###

    temp = s.peek()
    return temp


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())


print("Answer : ", '{:.2f}'.format(postFixeval(token)))
