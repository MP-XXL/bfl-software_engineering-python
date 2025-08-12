students = {
"S001": {"name": "John Doe", "age": 20, "score": 85},
"S002": {"name": "Jane Smith", "age": 19, "score": 92},
"S003": {"name": "Michael Brown", "age": 21, "score": 78},
"S004": {"name": "Emily Davis", "age": 22, "score": 88},
"S005": {"name": "Daniel Johnson", "age": 20, "score": 95},
"S006": {"name": "Sarah Wilson", "age": 18, "score": 81},
"S007": {"name": "David Lee", "age": 23, "score": 76},
}
age = int(input("Enter your age: "))
for student in students:
    if age == students[student]["age"]:
        print(students[student])
    else:
        continue
