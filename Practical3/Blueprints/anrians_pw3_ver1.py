file = open('cereals.csv')
highest = 0
lowest = 100
total_rating = 0 
line_count = 1
h_name = ''
l_name = ''
for line in file:
    c_column = line.strip().split(',')

    c_name = c_column[0]
    try:
        c_rating = float(c_column[-1])
    except:
        continue
    c_type = c_column[2]

    if c_rating > highest:
        highest = c_rating
        h_name = c_name
    
    if c_rating < lowest:
        lowest = c_rating
        l_name = c_name

    total_rating += c_rating
    line_count += 1

    print(c_name, c_type, c_rating)
file.close()

if line_count > 0:
    average = total_rating / line_count
    print('Highest rating cereals are', h_name, 'with the rating', highest)
    print('Lowest rating cereals are', l_name, 'with the rating', lowest)
    print('Average rating between all cereals is', average)
else:
    print('No valid ratings found in the file.')
