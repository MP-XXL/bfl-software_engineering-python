# Syntax for match
"""
match expression:
    case x:
        code block
    case y:
        code block
    case z:
        code block

"""

colour = "Red"
match colour:
    case "black":
        print(colour)
    case "blue":
        print(colour)
    case "white":
        print(colour)
    case _:
        print(f"No match case for: {colour}")


# Using Pipe
day = "tues"
match day:
    case "mon" | "tues" | "wed" | "thurs" | "fri":
        print("A weekday")
    case "sat" | "sun"

    case _:
        print("No match")


# Using Python guard
month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekend in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A week day in May")
    case _:
        print("Day not found!")
