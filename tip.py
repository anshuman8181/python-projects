def total_calc(billamt,tip):
    total=float(billamt*(1+0.01*tip))
    print(f"please enter rs.{total}")
billamt=float(input("enter the bill amount:"))
tip_percentage=float(input("enter the tip percent"))
total_calc(billamt,tip_percentage)
