def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('Error: Please enter a numeric value.')

def calculate_salary(hours, rate, additional_rate):
    if hours >= 40:
        return (40 * rate) + ((hours - 40) * rate * additional_rate)
    else:
        return hours * rate

def print_salary(salary):
    print('Your salary is: {:.2f}'.format(salary))

def validate_positive_number(value, prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print('Error: Please enter a positive value.')
        except ValueError:
            print('Error: Please enter a numeric value.')

# Example usage
work_hours = validate_positive_number('Input your work hours: ')
pay_rate = validate_positive_number('Input your pay rate: ')
additional_rate = validate_positive_number('Input additional pay rate for hours above 40: ')

total_salary = calculate_salary(work_hours, pay_rate, additional_rate)
print_salary(total_salary)