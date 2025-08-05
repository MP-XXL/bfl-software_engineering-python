"""
SMARTPHONE PURCHASE:
Ask user to input budget.
1. Check if budget is at least $500, if it is, check if the budget is $1000 or more. Then recommend "Google Pixel 9Pro", otherwise, recommend "iPhone"
2. If budget is below $500, if its is, and at least $200, then recommend "Redmi", otherwise, recommend, "Save more"
"""
budget = float(input("Enter your budget: \n$"))

if budget >= 500:
    if budget >= 1000:
        print("Google pixel 9 Pro")
    else:
        print("iPhone")
else:
    if budget >= 200:
        print("Redmi")
    else:
        print("Save more")
