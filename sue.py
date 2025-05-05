

total_amount = float(input("Enter the total bill amount: ₹"))

amount_paid = float(input("Enter the amount paid: ₹"))

due_amount = total_amount - amount_paid


if due_amount > 0:
    print("The due amount is: ₹" + str(due_amount))
elif due_amount < 0:
    print("Extra amount paid: ₹" + str(due_amount))
else:
    print("The bill is fully paid. No dues remaining.")
