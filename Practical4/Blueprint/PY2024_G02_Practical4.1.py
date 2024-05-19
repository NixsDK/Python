def main():
    # Prompt user for the file name
    file_name = "Practical4\mbox-short.txt"

    try:
        # Open the file
        with open(file_name, 'r') as file:
            from_lines = []
            count = 0

            # Process each line in the file
            for line in file:
                # Debug print to see each line
                # print(f"Processing line: {line.strip()}")
                
                # Check if the line starts with "From "
                if line.startswith("From "):
                    words = line.split()
                    # Ensure the line has the expected format
                    if len(words) >= 2:
                        email = words[1]
                        from_lines.append(email)
                        count += 1

            # Sort email addresses alphabetically
            from_lines.sort()

            # Print sorted email addresses
            for email in from_lines:
                print(email)

            # Print the count of "From " lines
            print(f"There were {count} lines in the file with From as the first word")

    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please check the file name and try again.")

if __name__ == "__main__":
    main()
