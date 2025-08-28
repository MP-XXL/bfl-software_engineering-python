students_db = {}
contain = {"student_id": 1}

#function to start our program
def start():
    student_id = 1
    while True:
        print("""
        1. Add student
        2. Delete student
        3. Update student record
        4. Get student record
        5. Display all students""")
        user_choice = int(input("Enter command : "))
        if user_choice == 1:
            add_student(student_id)#Calling the add student function to begin the add student function
           # student_id += 1
        elif user_choice == 2:
            delete_student()# Caling the delete student function
        elif user_choice == 3:
            update_record()# Calling the update record function
        elif user_choice == 4:
            get_student()# Calling the get student function
        elif user_choice == 5:
            display_students()# Calling the display students function
        else:
            print("Invalid input. Please enter valid input")

# Function to add student
def add_student(student_id):
    name = input("Student name : ")
    age = int(input("Age : "))
    department = input("Department : ")
    students_db[contain["student_id"]] = {"name": name, "age":age, "dept": department}
    contain["student_id"] += 1
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
            new_name = input("Enter the name of the student : ")
            students_db[id_to_update]["name"] = new_name
            print(students_db)
        elif update_choice == 2:
            new_age = input("Enter the new age of the student : ")
            students_db[id_to_update]["age"] = new_age
            print(students_db)
        if update_choice == 3:
            new_dept = input("Enter the new depart name : ")
            students_db[id_to_update]["dept"] = new_dept
            print(students_db)

# Function to get student
def get_student():
    student_to_get = int(input("Enter ID of student to get : "))
    if student_to_get in students_db:
        print(f"Details of student with ID {student_to_get} are : ")
        for key, value in students_db[student_to_get].items():
            print(key,"==", value)

# Function to display students
def display_students():
    for key, value in students_db.items():
        print(key)
        for  key, value in value.items():
            print(key, value)


# start program
start()
