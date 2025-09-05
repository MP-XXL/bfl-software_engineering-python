"""
TASK: Create an AttendanceRegister class.

Requirements:
1. The class should allow marking a student as present or absent.
2. Store attendance records in a dictionary where the student's name is the key.
3. Provide a method to check if a student was present or absent.
4. Provide a method to display the full register.

Example Usage:
    register = AttendanceRegister()
    register.mark_present("John")
    register.mark_absent("Mary")
    print(register.get_status("John"))   # "Present"
    print(register.show_register())      # {"John": "Present", "Mary": "Absent"}
"""
class Attendance_register:

    def __init__(self, **register):
        self.register = register

    def mark_present(self, name):
        if name in self.register:
            self.register[name] = "Present"
            register.display_register()
        else:
            return"Name not in the attendance!"

    def mark_absent(self, name):
        if name in self.register:
            self.register[name] = "Absent"
            register.display_register()
        else:
            return"Name not in the attendance!"

    def check_status(self, name):
        if name in self.register:
            return self.register[name]
        else:
            return"Name not in the attendance!"

    def display_register(self):
        for student, status in self.register.items():
            print(f"{student} === {status}")



register = Attendance_register(John = "Present", Mary = None, MP = "Present", K9 = None)
register.mark_present("K9")
register.mark_absent("Mary")
print(register.check_status("MP"))
register.display_register()
