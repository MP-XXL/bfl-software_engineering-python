number = 1
while number <= 100:
    if number % 2 == 0:
        number += 1
        continue
    else:
        print(number)
        number += 1

students = {
        "John": 60,
        "Mimi": 50,
        "Sarah": 30
        }
count = 0
while count < len(students):
    for key, value in students.items():
        print(key, value)
        count += 1

### Without for loop
new_numbers = list(students.keys())
print(new_numbers)

new_reccord = list(students.values())
print(new_reccord)
dot = 0
while dot < len(new_numbers):
    print(new_numbers[dot], new_reccord[dot])
    dot += 1
