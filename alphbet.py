somthing=str(input("Enter alphabet"))
if len(somthing)>1:
    print("invalid input")
else:
    if somthing>="a" and somthing<="z":
        print("it is alphabet")
    elif somthing>="A" and somthing<="Z":
        print("it is alphabet")
    else:
        print("it is not an alphabet")

    