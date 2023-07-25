def bon(w):
    temp = w[0]
    count = 0
    i = 0 
    while i != len(w):
        if temp == w[i]:
            count += 1
        else:
            temp = w[i]
            i -= 1
            count = 0
        if count > 1:
            return (ord(temp) - 96)*4
        i += 1


secretCode = input("Enter secret code : ")
print(bon(secretCode))



