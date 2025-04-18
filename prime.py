num1=int(input("enter a number:"))
for i in range(2,num1):
    if num1%i==0:
        print("the number is not prime")
        break
else:
    print("it is a prime")


        
