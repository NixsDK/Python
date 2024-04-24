def analyze_text(input):
    file = open(input, encoding='utf-8')

    letters = {}

    for line in file:
        for char in line:
            if char.isalpha():
                letters[char.lower()] = letters.get(char.lower(), 0) + 1

    file.close()

    total_letters = sum(letters.values())

    letter_precentage = []

    for char, count in letters.items():
        precentage = (count / total_letters) * 100
        letter_precentage.append((char, precentage))

    letter_precentage.sort()

    return letter_precentage

def compare_results(input1, input2):
    first_results = analyze_text(input1)
    second_results = analyze_text(input2)

    comparison_results = []

    first_dict = dict(first_results)
    second_dict = dict(second_results)

    for letter in [chr(i) for i in range(ord('a'), ord('z'))]:
        precentage1 = first_dict.get(letter, 0)
        precentage2 = second_dict.get(letter,0)

        comparison_results.append((letter, precentage1, precentage2))

    return comparison_results

User_input_1 = input('Enter first file name: ')
User_input_2 = input('Enter second file nmae: ')

results = compare_results(User_input_1, User_input_2)

print(f"{'Letter':<7} {'File 1':<10} {'File 2':<10}")
for result in results:
    letter, precentage1, precentage2 = result
    print(f"{letter:<7}  {precentage1:.2f}%   {precentage2:.2f}%")
