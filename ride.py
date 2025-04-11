option=(input("enter do you want bike or car:"))
if option=="car":
    size=input("small or big:")
    if size=="big":
        print("you want a big car ")
    else:
        print("you want a small car")
else:
    print("you have selected bike")
    typebike=input("bike or scooty:")
    if typebike=="bike":
        print("you have selected bike")
    else:
        print("you have selected scooty")

