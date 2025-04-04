mass=int(input("Please enter your weight in kg"))
hieght=float(input("Please enter your height in M"))

bmi=mass/(hieght**2)
print("this is your bmi",bmi)

if bmi<=18.5:
    print("you are underweight")
elif bmi>18.5 and bmi<25:
    print("you are normal")
elif bmi>25 and bmi<30:
    print("you are overweight")
elif bmi>30 and bmi<35:
    print("you are obese")
else:
    print("you are extremly obese")