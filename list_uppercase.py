user_input = input("Enter words separated by spaces: ")

words = user_input.split()

uppercase_words = [word.upper() for word in words]

print("Words in uppercase:", uppercase_words)
