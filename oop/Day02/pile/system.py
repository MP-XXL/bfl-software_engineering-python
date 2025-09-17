import json
import time

def read_students_db():
    with open(STUDENT_DB_FILE, "r") as file:
        students = json.load(file)


def write_students_db(students):
    with open(STUDENT_DB_FILE, "w") as file:
        json.dump(Student.students, file, indent = 4)

STUDENT_DB_FILE = "students_db.json"


def start():
    while True:
        print("""
                WELCOME TO PILE
                (PERSONALIZED.INTEGRATED.LEARNING.ENVIRONMENT)""")
        print("""
                1. Enter "1" to login
                2. Enter "2" to register
                3. Enter "0" to logout
                """)
        user_choice = input("Enter command : ")
        if user_choice == "0":
            print("Logging out...")
            time.sleep(2)
            print("Logged out successfully!")
            break
        user_choice_handler(user_choice)

def user_choice_handler(user_choice):
    if user_choice == "2":
        user_first_name = True
        while user_first_name:
            first_name = input("Please enter first name : ").capitalize()
            if first_name == "":
                print("Please input a valid name. Name field can not be left empty!")
            else:
                user_first_name = False
                user_last_name = True
                while user_last_name:
                    last_name = input("Please enter last name : ").capitalize()
                    if last_name == "":
                        print("Last name field can not be left empty! Input a valid name!")
                    else:
                        user_password = True
                        user_last_name = False
                        while user_password:
                            password = input("Please choose password : ")
                            if password == "":
                                print("Password field can not be left empty!")
                            else:
                                while True:
                                    user_password = False
                                    age = int(input("Please enter age : "))
                                    if age == "":
                                        print("Age can not be left empty!")
                                    elif age == str:
                                        print("Age can not be a string!")
                                    else:
                                        break
        s = Student(first_name, last_name, password, age)
        s.showStudent()
    elif user_choice == "1":
        while True:
            login_id = input("Enter your student ID : ").upper()
            login_checker(login_id)
    else:
        print("Invalid command. Please enter a valid command!")

        
def studentIdMaker(student_id):
    Student.i += 1
    Student.student_id = f"SID{Student.i}"

def login_checker(login_id):
    with open(STUDENT_DB_FILE, "r") as file:
        students = json.load(file)

    if login_id in students:
        login = True
        while login:
            login_password = input("Enter your password : ")
            if login_password == students[login_id]["password"]:
                login = False
                print(f"Welcome {students[login_id]['first_name'].upper()}")
                print("What are you doing today?")
                print("""
                        1. Enter "1" to study
                        2. Enter "2" to write test
                        """)
                student_action = input("Enter command : ")
            else:
                print("Wrong password! Please enter correct password")
            
    else:
        print("Student ID not found!. Please enter valid student ID!")



class SystemMember:


    def __init__(self, first_name:str, last_name:str, password ):
        self.first_name:str = first_name
        self.last_name:str = last_name
        self.password = password

class Library:
    

    def __init__(self, book_id, book_name, book_title):
        self.book_id = book_id
        self.book_name = book_name
        self.book_title = book_title 

class Student(SystemMember):

    i = 0
    student_id = f"SID{i}"
    students = {}
        
    def __init__(self, first_name:str, last_name:str, password, age:int):
        SystemMember.__init__(self, first_name, last_name, password)
        self.age:int = age
        self.is_student = True
        self.active_courses = []
        self.completed_courses = []
        studentIdMaker(Student.student_id)
        read_students_db()
        Student.students.update({
                Student.student_id:{
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "password": self.password,
                    "age": self.age,
                    "is_student": self.is_student,
                    "Active courses": self.active_courses,
                    "Completed courses": self.completed_courses}})
        write_students_db(Student.students)
        print("New student registered successfully!")

    def showStudent(self):
        print(f"""
                First Name = {self.first_name}
                Last Name = {self.last_name}
                Age = {self.age}
                Student = {self.is_student}
                Active courses = {self.active_courses}
                Completed courses = {self.completed_courses}
                Your Student ID = {Student.student_id}""")
