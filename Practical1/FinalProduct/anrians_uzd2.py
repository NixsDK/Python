workhours = int(input('Input your work hours: '))
payrate = float(input('Input your pay rate: '))
addrate = float(input('Input additional payrate for hours above 40: '))

if workhours>=40:
    salary = (payrate*40) + (((workhours-40)*payrate)*addrate)
else:
    salary = workhours*payrate

print('Your salary is: ' + str(salary))