""""
Employee Shift Manager
You are asked to build a small program to help manage employee work shifts in a company.  
Create a dictionary `shifts` where each key is an employee's name, and the value is a list of the days they are scheduled to work.  
     shifts = {
       "Alice": ["Monday", "Wednesday"],
       "Bob": ["Tuesday", "Thursday"],
       "Charlie": ["Monday", "Friday"]
   }


fucntion signature function add_shift(employee, day):
The  function should 
1. Checks if the employee exists in the dictionary.

 - If they exist, add the new day to their list (only if it’s not already there).

-  If they don’t exist, create a new key for them with the day inside a list.

-  Return the updated dictionary.


2. Write another function get_schedule(day) that:

Returns a list of employees working on that day.
"""
shifts = {
          "Alice": ["Monday", "Wednesday"],
          "Bob": ["Tuesday", "Thursday"],
          "Charlie": ["Monday", "Friday"]
          }
def shift_manager():
    name = input("Enter employee name : ").capitalize()
    day = input("Add day of shift : ").capitalize()
    if name in shifts:
        add_shift(name, day)
    else:
        add_employee(name, day)
    
def add_shift(employee, day):
    for days in [shifts[employee]]:
        if day in shifts[employee]:
            print("Day already exists")
        else:
            shifts[employee].append(day)

def add_employee(employee, day):
    shifts[employee] = [day]
    print(shifts)

# Getting schedule days
def get_schedule(day):
    for employee in shifts:
        if day in shifts[employee]:
            print(employee)
day = input("Enter the day to filter by : ").capitalize()
get_schedule(day)
shift_manager()
