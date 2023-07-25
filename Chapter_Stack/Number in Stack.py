class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items


def numinSTack(list):
    st = Stack()
    st_temp = Stack()
    list = list.split(",")
    for items in list:
        item = items.split()
        keyword = item[0]

        if keyword == 'A':
            number_list = item[1]
            number_list = int(number_list)
            st.push(number_list)
            print('Add = ' + str(number_list))
        elif keyword == 'P':
            if st.size() > 0:
                s = str(st.pop())
                print('Pop = '+s)
            else:
                print('-1')
        elif keyword == 'D':
            num_eraser = item[1]
            num_eraser = int(num_eraser)
            if st.size() > 0:
                for i in range(0, st.size()):
                    s = st.pop()
                    if s == num_eraser:
                        print('Delete = ' + str(s))

                    else:
                        st_temp.push(s)
                for i in range(0, st_temp.size()):
                    st.push(st_temp.pop())
            else:
                print('-1')
        elif keyword == 'LD':
            num_eraser = item[1]
            num_eraser = int(num_eraser)
            if st.size() > 0:
                for i in range(0, st.size()):
                    s = st.pop()
                    if s < num_eraser:
                        print('Delete = ' + str(s)+' Because ' +
                              str(s) + ' is less than ' + str(num_eraser))
                    else:
                        st_temp.push(s)
                for i in range(0, st_temp.size()):
                    st.push(st_temp.pop())
            else:
                print('-1')
        elif keyword == 'MD':
            num_eraser = item[1]
            num_eraser = int(num_eraser)
            if st.size() > 0:
                for i in range(0, st.size()):
                    s = st.pop()

                    if s > num_eraser:
                        print('Delete = ' + str(s)+' Because ' +
                              str(s) + ' is more than ' + str(num_eraser))
                    else:
                        st_temp.push(s)
                for i in range(0, st_temp.size()):
                    st.push(st_temp.pop())
            else:
                print('-1')
    print('Value in Stack = ', end="")
    last_list = [int(x) for x in st.peek()]
    print(last_list)


x = input('Enter Input : ')
numinSTack(x)
