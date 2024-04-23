import re

file_name = input("Input filename: ")

file = open(file_name)
search_pattern = r'(^From+.+\d)'
email_sources = list()

for line in file:

    columns = line.strip().split(" ")
    if re.search(search_pattern, line):
        email_sources.append(columns[1])

email_sources.sort()

for emails in email_sources:
    print(emails)

print("\nThere were ", len(email_sources), " lines that start with 'From'")
