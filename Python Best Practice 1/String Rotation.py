print("*** String Rotation ***")
string1, string2 = input("Enter 2 strings : ").split()

rotate_str1 = string1[-2:] + string1[0:-2]
rotate_str2 = string2[3:] + string2[0:3]

rounds = 1

while rotate_str1 != string1 or rotate_str2 != string2:
    if rounds <=5:
        print(rounds, rotate_str1, rotate_str2)
    rotate_str1 = rotate_str1[-2:] + rotate_str1[0:-2]
    rotate_str2 = rotate_str2 [3:] +rotate_str2 [0:3]
    rounds += 1

if rounds > 5:
    print(" . . . . . ")

print(rounds, rotate_str1, rotate_str2)
print("Total of  " + str(rounds) + " rounds.")