############## Version 1
i = 0
limit = 1000
students = []
while i < limit:
    student  = {
            "ID": i + 1,
            "name": (f"student{i + 1}"),
            "score": i+1
            }
    students.append(student)
    i += 1

print("LIST OF 1,000 ODERED STUDENTS \n", students)


############### Version 2

import random

i = 0
limit = 1000
students = []
while i < limit:
    student  = {
            "ID": random.randint(1, 1000),
            "name": (f"student{random.randint(0, 2000)}"),
            "score": random.randint(1,100)
            }
    students.append(student)
    i += 1

print("LIST OF 1,000 RANDOM STUDENTS \n", students)


############### Version 3
i = 0
students = []
while True:
    if i < 1000:
        student  = {
            "ID": random.randint(1, 1000),
            "name": (f"student{random.randint(0, 2000)}"),
            "score": random.randint(1,100)
            }
        students.append(student)
    else:
        break
    i += 1

print("LIST OF 1,000 RANDOM STUDENTS USING IF STATEMENTS\n", students)

