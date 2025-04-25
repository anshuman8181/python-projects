def add(Q,R):
    return Q+R
def subtract(Q,R):
    return Q-R
def multiyply(Q,R):
    return Q*R
def divid(Q,R):
    return Q/R

print("a. addition\n b. subtraction\n c. multiplycation\n d. division")
chose=input("Please enter your chose:")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if chose=="a":
    print(num1," + ",num2," = ",add(num1,num2))
elif chose=="b":
    print(num1," - ",num2," = ",subtract(num1,num2))
elif chose=="c":
    print(num1," * ",num2," = ",multiyply(num1,num2))
elif chose=="d":
    print(num1," / ",num2," = ",divid(num1,num2))
else:
    print("Invalid input")
