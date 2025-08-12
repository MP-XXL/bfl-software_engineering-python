score = float(input("Enter a score : "))
if score >= 70 and score <= 100:
    print("A")
elif score >= 60 and score <= 69.9:
    print("B")
elif score >= 50 and score <= 59.9:
    print("C")
elif score >= 45 and score <= 49.9:
    print("D")
elif score >= 40 and score <= 44.9:
    print("E")
elif score >= 0 and score <= 39.9:
    print("F")
else:
    print("Invalid score!")
