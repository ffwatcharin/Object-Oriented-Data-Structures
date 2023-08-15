# Palindrome
# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

# เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่


# def ispalindrome(word):
#     return word == word[::-1]

def ispalindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return ispalindrome(word[1:-1])


inp = input('Enter Input : ')
if ispalindrome(inp):
    print(f"'{inp}' is palindrome")
else:
    print(f"'{inp}' is not palindrome")
