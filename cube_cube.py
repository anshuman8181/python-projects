def cube(number):
    return number**3

def display(number):
    if number%3 == 0:
        return cube(number)
    else:
        return False
n=int(input("enter a integer:"))
print(display(n))