medical_cause=(input("do you have a medical cause yes or no:"))
if medical_cause=="yes":
    print("you are allowed")
else:
    attendence=int(input(" enter you attendence:"))
    if attendence>=75:
        print("you are allowed ")
    else:
        print("you are not")

