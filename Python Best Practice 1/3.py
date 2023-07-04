def count_characters(text):
    upper_count = 0
    unique_upper = set()
    lower_count = 0
    unique_lower = set()

    for i in text:
        if i.isupper():
            upper_count += 1
            unique_upper.add(i)
        elif i.islower():
            lower_count += 1
            unique_lower.add(i)

    return upper_count, unique_upper, lower_count, unique_lower

print(" *** String count ***")
message = input("Enter message : ")

upper_count, unique_upper, lower_count, unique_lower = count_characters(message)

print("No. of Upper case characters :", upper_count)
print("Unique Upper case characters :", '  '.join(sorted(unique_upper)))
print("No. of Lower case Characters :", lower_count)
print("Unique Lower case characters :", '  '.join(sorted(unique_lower)))
