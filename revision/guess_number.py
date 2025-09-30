import random

number_generated = random.randrange(1, 10)

user_guess = int(input("Enter the number you wish to guess : "))

if user_guess == number_generated:
    print("You won!")
else:
    print("Wrong. Try again!")
