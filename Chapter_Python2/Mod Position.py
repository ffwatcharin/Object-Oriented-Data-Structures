def mod_position(arr, s):
    
    characters = []
    for i, char in enumerate(arr):
        if (i+1) % s == 0:
            characters.append(char)
    return characters

print("*** Mod Position ***")
arr, s = input("Enter Input : ").split(",")
s = int(s)
result = mod_position(arr, s)
print(result)
