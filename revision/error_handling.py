# Task1
"""try:
    value = float(input("Enter a number")) #Type casting with float will raise value error instead of type error
    print(10/value)

except ValueError:
    print("Please enter only valid numbers!")
except ZeroDivisionError:
      print("Enter any valid number apart from zero '0'")
except Exception:
    print("Ops! Something happend!")
"""
# Task2

'''try:
    name = input("Enter student name: ")
    grade = students_grades[name]
    print(f"{name}'s grade is : {grade}")

except KeyError:
    print("Please enter only valid numbers!")
except BaseException:
    print("Only valid inputs are allowed!")'''

#Task3
"""fruits = ["apple", "banana", "cherry", "date"]
print(f"Available fruits:{fruits}")

try:
    position = int(input("Enter the position to get fruit : "))
    print(f"You got: {fruits[position]}")
except IndexError:
    print("You entered a range out of index")
except ValueError:
    print("You entered an invalid value")
except BaseException:
    print("Ops! Something went wrong!")"""
#Task4
"""try:
    user_input = input("Enter numbers separated by commas : ")
    if "," in user_input:
        numbers = user_input.split(",")
    total =0
    for num in numbers:
        total += int(num)

    print(f"The sum of all numbers : {total}")

except NameError:
    print("An invalid input was received and split did not occur!")
except BaseException:
    print("Oops! Something went wrong!")"""

def read_int(prompt, minn = -10, maxx = 10):
    read = True
    while read:
        try:
            user_input = int(input("Enter a number: from -10 to 10: "))
            if user_input >= minn and user_input <= maxx:
                print(f"The number is {user_input}")
                return
            else:
                print("Value is out of range!")
        except ValueError:
            print("Wrong input!")
        except Exception:
            print("Something happend!")


read_int("")

