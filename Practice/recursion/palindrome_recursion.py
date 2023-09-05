# def ispalindrome(word):
#     return word == word[::-1]

# def ispalindrome(word):
#     if len(word) < 2:
#         return True
#     if word[0] != word[-1]:
#         return False
#     return ispalindrome(word[1:-1])


# inp = input('Enter Input : ')
# if ispalindrome(inp):
#     print(f"'{inp}' is palindrome")
# else:
#     print(f"'{inp}' is not palindrome")

def ispalindrome(word):
    return word == word[::-1]


inp = input('Enter Input : ')
if ispalindrome(inp):
    print(f'\'{inp}\' is palindrome')
else:
    print(f'\'{inp}\' is not palindrome')
