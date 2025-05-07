def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Prime check
number = int(input("Enter a number to check if it's prime: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

# Shutdown option
confirm = input("Type 'shutdown' to proceed with shutdown: ")
if confirm.lower() == "shutdown":
    print("Shutting down...")
    
else:
    print("Shutdown aborted.")
