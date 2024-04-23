import re

file_name = input("Input filename: ")

file = open(file_name)
search_pattern = r'(^From+.+\d)'
email_sources = {}

for line in file:

    columns = line.strip().split(" ")
    if re.search(search_pattern, line):
        domains = columns[1].split("@")
        email_sources[domains[1]] = email_sources.get(domains[1], 0)  + 1

file.close()

print(email_sources, "\n")

sorted = sorted(email_sources.items(), key=lambda item: item[1])
sorted_emails = dict(sorted)

longest_key = max(len(key) for key in sorted_emails.keys())
longest_value = max(len(str(value)) for value in sorted_emails.values())

print("SORTED:")
for domains,ammount in sorted_emails.items():
    key_str = domains.rjust(longest_key)
    value_str = str(ammount).rjust(longest_value)
    print(f"{key_str}: {value_str}", "*"*ammount)
