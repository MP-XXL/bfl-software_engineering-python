'''# Question 1

user_bio = input("Enter your bio : ")
print(len(user_bio))
first = user_bio[:20]
print(first)
last = user_bio[-20:]
print(last)
print(len(last))


# Question 2

total_bill = float(input("Enter the total bill : "))
amount_of_people = int(input("Enter number of persons : "))
amount_to_pay = total_bill / amount_of_people
print(f"The total bill is {total_bill:.2f}, amongst {amount_of_people:.2f} persons, Each person is to pay ${amount_to_pay:,.2f}")


# Question 3

favourite_movie = input("Enter your favourite movie title: ")
number_of_times_watched = int(input("Enter the number of times watched: "))
print(f"I have watched {favourite_movie} {number_of_times_watched} times")
print(favourite_movie.upper())
print(favourite_movie[-3:])


# Question 4

monday_steps = int(input("Enter number of steps on monday :"))
tuesday_steps = int(input("Enter number of steps on tuesday : "))
wednesday_steps = int((input("Enter number of steps on wednesday : ")))
total_steps = monday_steps + tuesday_steps + wednesday_steps
number_of_days = 3
average_steps = int(total_steps / number_of_days)
print(f"You walked a total number of {total_steps:,} steps in {number_of_days} days. That is an average of {average_steps:,} steps per day")
'''

# Question 5

passcode = input("Enter password: ")
length_of_password = len(passcode)
print("Your password is", passcode, " and has ", length_of_password, "characters")
first=(passcode[0])
last=(passcode[-1:])
print(first)
print(last)
number_of_stars = length_of_password -2
asterisk = "*"
output = (first + (asterisk * number_of_stars) + last)
print(output)

