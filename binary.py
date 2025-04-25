decimal_number = int(input("Enter a decimal number: "))

if decimal_number == 0:
    binary_number = "0"
else:
    binary_number = ""
    n = decimal_number
    while n > 0:
        remainder = n % 2
        binary_number = str(remainder) + binary_number
        n = n // 2

print("Binary representation of", decimal_number, "is:", binary_number)
