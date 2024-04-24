import re

class LetterCounter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.letter_count = {}
        self.total_letters = 0

    def count_letters(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for line in file:
                # Convert uppercase letters to lowercase
                line = re.sub(r'[A-Z]', lambda x: x.group(0).lower(), line)
                
                # Remove special characters, digits, and whitespaces
                line = re.sub(r'[^a-z]', '', line)
                
                # Count occurrences of each letter
                for letter in line:
                    self.letter_count[letter] = self.letter_count.get(letter, 0) + 1
                    self.total_letters += 1

                print(line, end='')

    def print_letter_counts(self):
        print("\nLetter Counts (% of Total):")
        for letter, count in sorted(self.letter_count.items(), key=lambda item: item[1], reverse=True):
            percentage = (count / self.total_letters) * 100
            print(f"{letter}: {percentage:.2f}% ({count}/{self.total_letters})")


# Get file names from user
file_name1 = "C://Users//tbrit//Desktop//latwiki.txt" #input("Enter the first file name: ")
file_name2 = "C://Users//tbrit//Desktop//england.txt" #input("Enter the second file name: ")

# Create instances of LetterCounter for each file
counter1 = LetterCounter(file_name1)
counter2 = LetterCounter(file_name2)

# Count letters for each file
print("First File:")
counter1.count_letters()
print("\nSecond File:")
counter2.count_letters()

# Print letter counts for each file side by side
print("\nFirst File Letter Counts\tSecond File Letter Counts")
for (letter1, count1), (letter2, count2) in zip(sorted(counter1.letter_count.items(), key=lambda item: item[1], reverse=True),
                                                sorted(counter2.letter_count.items(), key=lambda item: item[1], reverse=True)):
    percentage1 = (count1 / counter1.total_letters) * 100
    percentage2 = (count2 / counter2.total_letters) * 100
    print(f"{letter1}: {percentage1:.2f}% ({count1}/{counter1.total_letters})\t\t{letter2}: {percentage2:.2f}% ({count2}/{counter2.total_letters})")
