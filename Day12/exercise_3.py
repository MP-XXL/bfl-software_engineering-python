"""
student = {
    "name":"legolas",
    "has_registered": True,
    "has_paid": True,
    "has_internet": False
    }
Only students that have registered are eligible of exams. Any student that has not registered should be denied access with message "Access denied"
1. In as much as students have registered, if they have not paid fees, they should be denied access to exams with message "pay your fees"
2. If they have paid and have internet access, message "Allow", else "Check your internet connection"
"""

student = {
    "name":"legolas",
    "has_registered": True,
    "has_paid": True,
    "has_internet": False
    }
registered = student["has_registered"]
paid = student["has_paid"]
internet = student["has_internet"]

if registered == True:
    if paid == True:
        if internet == True:
            print("Allowed!")
        else:
            print("Check your internet connection")
    else:
        print("Pay your fees")
else:
    print("Acces denied")
