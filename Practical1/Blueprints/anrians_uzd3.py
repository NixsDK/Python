while True:
    try:
        workhours = int(input('Input your work hours: '))
        break
    except:
        print('Please enter numeric value!\n')

while True:
    try:
        payrate = float(input('Input your pay rate: '))
        break
    except:
        print('Please enter numeric value!')

while True:
    try:
        addrate = float(input('Input additional payrate for hours above 40: '))
        break
    except:
        print('Please enter numeric value!')

if workhours>=40:
    salary = (payrate*40) + (((workhours-40)*payrate)*addrate)
else:
    salary = workhours*payrate

print('Your salary is: ' + str(salary))