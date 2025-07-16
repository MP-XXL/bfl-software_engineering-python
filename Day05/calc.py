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
subtraction = first_number - second_number
print(f"{first_number} - {second_number} = {subtraction:.2f}")

print("Enter two numbers to multiply")
# Prompt user to enter two numbers
first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number : "))
multiplication = first_number * second_number
print(f"{first_number} * {second_number} = {multiplication:.2f}")

print("Enter two numbers to divide")
# Prompt user to enter two numbers
first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number : "))
division = first_number / second_number
print(f"{first_number} / {second_number} = {division:.2f}")

print("Enter two numbers to exponate")
# Prompt user to enter two numbers
first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number : "))
exponentiation = first_number ** second_number
print(f"{first_number} ** {second_number} = {exponentiation:.2f}")

