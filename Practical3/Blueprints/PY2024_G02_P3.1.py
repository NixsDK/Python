# Define the file path
file_path = 'Practical3\cereals.csv'

# Read the dataset file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Print the first line to verify the header
header_line = lines[0].strip()
print("Header Line:", header_line)

# Split the header line by commas
header = header_line.split(',')

# Print the header list to verify it
print("Parsed Header:", header)

# Ensure the expected column names are present
if 'name' not in header or 'type' not in header or 'rating' not in header:
    print("Error: Expected column names not found in the header.")
else:
    # Skip the header line
    data_lines = lines[1:]

    # Index positions based on the header
    name_idx = header.index('name')
    type_idx = header.index('type')
    rating_idx = header.index('rating')

    # Initialize lists to store values
    cold_cereals = []
    hot_cereals = []

    for line in data_lines:
        fields = line.strip().split(',')
        cereal_name = fields[name_idx]
        cereal_type = fields[type_idx]
        cereal_rating = float(fields[rating_idx])
        
        if cereal_type == 'C':
            cold_cereals.append((cereal_name, cereal_rating))
        else:
            hot_cereals.append((cereal_name, cereal_rating))

    # Function to calculate statistics
    def calculate_statistics(cereals):
        if not cereals:
            return None, None, None
        
        cereals_sorted = sorted(cereals, key=lambda x: x[1])
        
        min_cereal = cereals_sorted[0]
        max_cereal = cereals_sorted[-1]
        avg_rating = sum(r[1] for r in cereals) / len(cereals)
        
        return min_cereal, max_cereal, avg_rating

    # Calculate statistics for cold and hot cereals
    cold_min, cold_max, cold_avg = calculate_statistics(cold_cereals)
    hot_min, hot_max, hot_avg = calculate_statistics(hot_cereals)

    # Function to print statistics
    def print_statistics(cereal_type, min_cereal, max_cereal, avg_rating):
        print(f'Cereal type: {cereal_type}')
        print(f'The lowest cereals rating value: {min_cereal[1]} Cereal name: {min_cereal[0]}')
        print(f'The average cereals rating value: {avg_rating}')
        print(f'The highest cereals rating value: {max_cereal[1]} Cereal name: {max_cereal[0]}')
        print()

    # Print statistics for cold cereals if data exists
    if cold_min and cold_max and cold_avg:
        print_statistics('Cold', cold_min, cold_max, cold_avg)

    # Print statistics for hot cereals if data exists
    if hot_min and hot_max and hot_avg:
        print_statistics('Hot', hot_min, hot_max, hot_avg)
