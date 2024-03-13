def compute_wage (hours, pay_rate):
    if hours >= 40:
        pay=pay_rate * 40 + (hours - 40) * pay_rate * 1.25
    else:
        pay=hours*pay_rate
    return pay


while True:
    try:
        input_hours = int(input('Input your work hours: '))
        break
    except:
        print('Please enter numeric value!')

while True:
    try:
        input_pay_rate = float(input('Input your pay rate: '))
        break
    except:
        print('Please enter numeric value!')


print('Your salary is ', compute_wage(input_hours, input_pay_rate))