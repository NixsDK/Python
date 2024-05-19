def main():
    # Prompt user for the file name
    file_name = "Practical4/mbox-short.txt"

    try:
        # Open the file
        with open(file_name, 'r') as file:
            domain_counts = {}

            # Process each line in the file
            for line in file:
                # Check if the line starts with "From "
                if line.startswith("From "):
                    words = line.split()
                    # Ensure the line has the expected format
                    if len(words) >= 2:
                        email = words[1]
                        domain = email.split('@')[1]
                        # Debug print to check domain extraction
                        # print(f"Extracted domain: {domain}")
                        # Update domain count in dictionary
                        if domain in domain_counts:
                            domain_counts[domain] += 1
                        else:
                            domain_counts[domain] = 1

            # Print the dictionary
            print(domain_counts)

            # Sort the dictionary by domain name and print formatted output
            print("SORTED:")
            for domain in sorted(domain_counts):
                count = domain_counts[domain]
                print(f" {domain}: {count} {'*' * count}")

    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
