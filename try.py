try:
    num1=int(input(" Enter your number:"))
    print(num1)
except ValueError as ex:
    print("exeption: ",ex)

print("you are outside the try block")