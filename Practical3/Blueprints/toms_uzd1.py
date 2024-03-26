MAX_RATING = 1000
MIN_RATING = -1000
lowest_ratings = {"C": MAX_RATING, "H": MAX_RATING}
highest_ratings = {"C": MIN_RATING, "H": MIN_RATING}
rating_sums = {"C": 0, "H": 0}
rating_counts = {"C": 0, "H": 0}
lowest_cereal_name = {"C": "", "H": ""}
highest_cereal_name = {"C": "", "H": ""}

#Open the file
with open("cereals.csv", "r") as file:
    #Skip the header line
    next(file)
    #Read line by line
    for line in file:
        parts = line.strip().split(",")  #Split the line into parts
        cereal_name = parts[0]  #Extract cereal name
        cereal_type = parts[2]  #Extract cereal type
        cereal_rating = float(parts[-1])  #Extract cereal rating

        #Update lowest and highest ratings if necessary
        if cereal_rating < lowest_ratings[cereal_type]:
            lowest_ratings[cereal_type] = cereal_rating
            lowest_cereal_name[cereal_type] = cereal_name
        if cereal_rating > highest_ratings[cereal_type]:
            highest_ratings[cereal_type] = cereal_rating
            highest_cereal_name[cereal_type] = cereal_name

        #Update sum and count for calculating average
        rating_sums[cereal_type] += cereal_rating
        rating_counts[cereal_type] += 1

#Calculate average values
average_ratings = {cereal_type: rating_sums[cereal_type] / rating_counts[cereal_type] for cereal_type in rating_sums}

#Print results
for cereal_type in lowest_ratings:
    print(f"Cereal type: {'Cold' if cereal_type == 'C' else 'Hot'}")
    print(f"Lowest rating: {lowest_ratings[cereal_type]} Cereals name: {lowest_cereal_name[cereal_type]}")
    print(f"Average rating: {average_ratings[cereal_type]}")
    print(f"Highest rating: {highest_ratings[cereal_type]} Cereals name: {highest_cereal_name[cereal_type]}")
    print()
