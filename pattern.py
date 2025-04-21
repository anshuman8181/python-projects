# for i in range(5):
#     for i in range(5):
#         print("*",end="")
#     print("\n")


#right angle triange

# for i in range(5):
#     for j in range(i):
#         print("*",end=" ")
#     print("\n",end="")


for i in range(5):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for h in range(i):
        print("/",end=" ")
    print("\n",end="")
