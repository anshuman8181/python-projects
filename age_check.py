def check_age():
    age_input = input("Enter your age: ")

    if not age_input.isdigit():
        print("Invalid input. Please enter a valid number.")
        return

    age = int(age_input)

    if age < 0 or age > 120:
        print("Error: Entered age is not realistic.")
        return

    if age % 2 == 0:
        print(f"The age {age} is even.")
    else:
        print(f"The age {age} is odd.")

check_age()
