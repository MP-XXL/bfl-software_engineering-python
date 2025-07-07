#1
'''#Problem: Receive miles and convert to kilometers
#Kilometers = miles * 1.60934
#Enter miles (5)
#Result: 5 miles equals 8.04 kilometers

miles = float(input("Enter the number of miles you wish to convert:\n "))
kilometers = miles * 1.60934
print("{} miles  equals {} kilometers".format(miles, kilometers))

kilometers_register = []

kilometers_register.append(kilometers)

print(kilometers_register)'''

#2
'''num1, operator, num2 = input("Enter calculation: ").split()

num1 = int(num1)
num2 = int(num2)
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))

elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))

elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))

elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))

elif operator == "%":
    print("{} % {} = {}".format(num1, num2, num1 % num2))

else:
    print("Enter a valid arithmetic operator")
'''


#3
'''age = eval(input("Enter your age: "))

if age < 5:
    print("Too young for school")
elif age == 5:
    print("Go to kindergarten")

elif age >= 6 and age <= 17:
    grade = age - 5
    print("Go to grade {}".format(grade))

elif age > 17:
    print("Go to college")
else:
    print("Not qualfied")'''

#4
#Printing odd numbers
'''for i in range(22):
    if (( i % 2 != 0)):
         print(i)
'''
#5
#Desmostrating compund interest for a number of years

'''money_to_be_invested = input("Enter the amount to be invested : ")
interest_rate = input("The money was invested at what interest rate : ")
money_to_be_invested = float(money_to_be_invested)
interest_rate = float(interest_rate) * .01
#lets invest for a range of 10 years
for i in range(1, 11):
    money_to_be_invested = money_to_be_invested + (money_to_be_invested * interest_rate)
    print("ROI after {} years is : {:.2f}".format(i, money_to_be_invested))'''

#6

tree_height = int(input("Enter tree height: "))
spaces = tree_height - 1
hashes = 1
stump_spaces = tree_height - 1
while tree_height != 0:
    for i in range(spaces):
        print(" ", end="")

    for i in range(hashes):
        print("#", end="")

    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1
for i in range(stump_spaces):
    print(" ", end="")
    print("#")
