def compute_wage (work_hours, pay_rate):
    if work_hours > 40:
        gross_pay = ((work_hours - 40) * pay_rate * 1.25) + 40 * pay_rate

    else:
        gross_pay = work_hours * pay_rate
    return gross_pay

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


print('Your pay is ', compute_wage(work_hours, pay_rate), "(gross)")
