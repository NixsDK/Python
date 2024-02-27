work_hours = int(input("Please input your work hours: "))
pay_rate = float(input("Please input your pay rate: "))

if work_hours > 40:
    gross_pay = ((work_hours - 40) * pay_rate * 1.25) + 40 * pay_rate
    print("Your pay is: ", gross_pay, "(gross)")
else:
    gross_pay = work_hours * pay_rate
    print("Your pay is: ", gross_pay, "(gross)")
