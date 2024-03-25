c_low_rating = 100
c_low_name = ''
c_high_rating = 0
c_high_name = ''

h_low_rating = 100
h_low_name = ''
h_high_rating = 0
h_high_name = ''

c_total_rating = 0
c_line_count = 0
h_total_rating = 0
h_line_count = 0

file = open('cereals.csv')

for line in file:
    column = line.strip().split(',')

    try:
        name = column[0]
        rating = float(column[-1])
    except:
        continue

    if column[2] == 'C':
        if rating < c_low_rating:
            c_low_rating = rating
            c_low_name = name
        
        if rating > c_high_rating:
            c_high_rating = rating
            c_high_name = name
        
        c_total_rating += rating
        c_line_count += 1
    
    if column[2] == 'H':
        if rating < h_low_rating:
            h_low_rating = rating
            h_low_name = name
        
        if rating > h_high_rating:
            h_high_rating = rating
            h_high_name = name

        h_total_rating += rating
        h_line_count += 1



file.close

try:
    c_average = c_total_rating / c_line_count
    h_average = h_total_rating / h_line_count
    print('Highest rating cold type cereals are', c_high_name, 'with the rating', c_high_rating)
    print('Lowest rating cold type cereals are', c_low_name, 'with the rating', c_low_rating)
    print('Average rating between all cold type cereals is', c_average)
    print('Highest rating hot type cereals are', h_high_name, 'with teh rating', h_high_rating)
    print('Lowest rating hot type cereals are', h_low_name, 'with the ratning', h_low_rating)
    print('Average rating between all hot type cereals is', h_average)
except:
    print('Something went wrong')
