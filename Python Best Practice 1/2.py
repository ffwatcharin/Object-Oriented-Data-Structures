print(" *** Divisible number ***")
num = int(input("Enter a positive number : "))

if num <= 0:
    print(str(num)+" is OUT of range !!!")
else:
    if num == 1:
        print("Output ==> " + str(num))
        print("Total ==> " +  str(num))
    
    else:
        l = [1, num]
        i = 2

        while i != num:
            if num % i == 0 and int(i) not in l:
                l.append(int(num/i))
                l.append(i)
                i += 1
            else:
                i += 1

        l.sort()
 
        l_num = " ".join(str(x) for x in l)

        print("Output ==> " + l_num)
        print("Total ==> " + str(len(l)))

