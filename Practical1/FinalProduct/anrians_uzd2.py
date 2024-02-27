work_hours = int(input('Input your work hours: '))
pay_rate = float(input('Input your pay rate: '))
add_rate = float(input('Input additional payrate for hours above 40: '))

if work_hours>=40:
    salary = (pay_rate*40) + (((work_hours-40)*pay_rate)*add_rate)
else:
    salary = work_hours*pay_rate

print('Your salary is: ' + str(salary))
