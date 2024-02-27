while True:
    try:
        work_hours = int(input("Please input your work hours: "))
        break
    except:
        print('Please enter a numeric value! \n')
while True:
    try:
        pay_rate = float(input("Please input your pay rate: "))
        break
    except:
        print('Please enter a numeric value! \n')


if work_hours > 40:
    gross_pay = ((work_hours - 40) * pay_rate * 1.25) + 40 * pay_rate
    print("Your pay is: ", gross_pay, "(gross)")

else:
    gross_pay = work_hours * pay_rate
    print("Your pay is: ", gross_pay, "(gross)")
