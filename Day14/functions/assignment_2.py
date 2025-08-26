students_db = {}
#student_id = 1

#function to start our program
def start():
    while True:
        print("""
        1. Add student
        2. Delete student
        3. Update student record
        4. Get student record
        5. Display all students
        6. Search student by name
        7. Count the students in the database
        8. Filter students by age""")
        user_choice = int(input("Enter command : "))
        if user_choice == 1:
            add_student()#Calling the add student function to begin the add student function
        elif user_choice == 2:
            delete_student()# Caling the delete student function
        elif user_choice == 3:
            update_record()# Calling the update record function
        elif user_choice == 4:
            get_student()# Calling the get student function
        elif user_choice == 5:
            display_students()# Calling the display students function
        elif user_choice == 6:
            search_student_by_name()# Calling the search student by name fucntion
        elif user_choice == 7:
            count_students()# Calling the function to count number of students in the system.
        elif user_choice == 8:
            filter_by_age()# Calling the filter students by age function
        else:
            print("Invalid input. Please enter valid input")
# Function to add student
def add_student():
    name = input("Student name : ").capitalize()
    age = int(input("Age : "))
    department = input("Department : ").capitalize()
    key = len(students_db) + 1
    students_db[key] = {"name": name, "age":age, "dept": department}
    print(students_db)

# function to delete student
def delete_student():
    student_id = int(input("Student ID to delete : "))
    if student_id in students_db:
        del students_db[student_id]
        print("Student with ID {student_id} deleted successfully")
        print(students_db)
    else:
        print("student not found")

# Function to update student record
def update_record():
    id_to_update = int(input("Enter ID of student to update : "))
    if id_to_update in students_db:
        update_choice = int(input("""1. Enter \"1\" to update name\n2. Enter \"2\" to update age\n3. Enter \"3\" to update department : """))
        if update_choice == 1:
            new_name = input("Enter the name of the student : ").capitalize()
            students_db[id_to_update]["name"] = new_name
            print(students_db)
        elif update_choice == 2:
            new_age = input("Enter the new age of the student : ")
            students_db[id_to_update]["age"] = new_age
            print(students_db)
        if update_choice == 3:
            new_dept = input("Enter the new depart name : ").capitalize()
            students_db[id_to_update]["dept"] = new_dept
            print(students_db)

# Function to get student
def get_student():
    student_to_get = int(input("Enter ID of student to get : "))
    if student_to_get in students_db:
        print(f"Details of student with ID {student_to_get} are : ")
        for key, value in students_db[student_to_get].items():
            print(key,"==", value)

# Function to display all students in the database
def display_students():
    for key, value in students_db.items():
        print(key)
        for  key, value in value.items():
            print(key, value)

# Function to search for student by name:
def search_student_by_name():
    name_to_search = input("Enter student name to search for : ").capitalize()
    for student in students_db:
        if students_db[student]["name"] == name_to_search:
            for key, value in students_db.items():
                print(f"ID: {key}, Name: {students_db[student]['name']}, Age: {students_db[student]['age']}")

# Function to count the number of students in the system
def count_students():
    print(f"Total number of students in the database are : {len(students_db)}")

# Function to filter students by a paricular age
def filter_by_age():
    age_to_filter = int(input("Enter the age to filter from : "))
    for student in students_db:
        if students_db[student]["age"] > age_to_filter:
            print(f"List of students above {age_to_filter}")
            print(f"ID: {student}, Name: {students_db[student]['name']}, Age: {students_db[student]['age']}")


# start program
start()
