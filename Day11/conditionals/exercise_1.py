score = float(input("Enter a valid score : "))

if score >= 70 and score < 100:
    print("Your grade is A")
elif score >= 50 and score <= 69.9:
    print("Your grade is B")
elif score >= 40 and score <= 49.9:
    print("Your score is C")
elif score >= 30 and score <= 39.9:
    print("Your score is D")
elif score >= 0 and score < 30:
    print("Your score is F")
else:
    print("Invalid Range!")
