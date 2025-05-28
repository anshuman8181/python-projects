class Employee:

    def __init__(self):
        print("employee created")

    def __del__(self):
        print("destructer called")


def Created_obj():
    print("Making Object...")
    obj = Employee()
    print("function end...") 
    return obj

print("Calling Create_obj()function...")
obj = Created_obj()
del obj
print("Program end...")