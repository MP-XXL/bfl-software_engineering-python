"""Print and display numbers from the list that are divisible by 5 with the following conditions:
1. If the number is greater than 150, skip to the next number
2. If the number is greater than 500, it should break"""

numbers = [12, 75, 150, 180, 145, 525, 50]
for number in numbers:
    if number > 500:
        break
    if number > 150:
        continue
    if number % 5 == 0:
        print(number)

# Print the list in reverse without using any methods
count = len(numbers) - 1
for number in range(len(numbers)):
    print(numbers[count])
    count -= 1

# Find the largest number in the list
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print("Largest number = ",largest_number)

record = []
count = 3
students = {
        "name":"",
        "gender": "",
        "score": ""
        }
for student in range(count):
    name = input("Enter name: ")
    students["name"] = name
    gender = input("Enter gender : ")
    students["gender"] = gender
    score = int(input("Enter score : "))
    students["score"] = score
    record.append(students)
print(record)


