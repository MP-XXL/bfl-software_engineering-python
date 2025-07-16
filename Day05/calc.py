# A simple calculator app
print('''1. Addition
2. Subtraction
3. Multiplication
4. Division''')

print("Enter two numbers to add")
# Prompt user to enter two numbers
first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number : "))
summation = first_number + second_number
print(f"{first_number} + {second_number} = {summation}")

print("Enter two numbers to subract")
# Prompt user to enter two numbers
first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number : "))
summation = first_number - second_number
print(f"{first_number} - {second_number} = {summation}")
