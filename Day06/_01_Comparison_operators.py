# Comparison Operators
operand1 = 10
operand2 = 2

#Is operand1 greater-than operand 2?
print(operand1 > operand2)

#Is operand1 greater-less than operand 2?
print(operand1 < operand2)

user_age = int(input("Enter your age: "))
print(f"Is {user_age} greater than or eqauls to 18?", user_age >= 18)

score = float(input("Enter a score: " ))
#print(f"Is user {score} greater or equal to 70", score >= 70)
print("Is user {} greater or equal to 70?: {}".format(score, score >= 70))

pin = 4190
print("Welcome to our ATM")
user_pin = int(input("Enter your pin: "))
print("Is the pin correct?:", user_pin == pin)

phone_password = 41111
user_input = int(input("Enter pin :\n>>>"))
print(f"Is {user_input} equal to {phone_pasword}?:", user_input == phone_password)

