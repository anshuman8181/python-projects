def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    

fact=int(input("Enter a number to find the factorial : "))
print("the factorial of",fact, "=",factorial(fact))
