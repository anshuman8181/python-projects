user_input = input("Enter something: ")
count = 0

for ch in user_input:
    if '0' <= ch <= '9':
        count += 1

print("Number of digits:", count)


