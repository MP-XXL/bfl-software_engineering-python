# 📝 Task 2: Student Profile Creator
def create_student_profile(**details):
    """
    Create a student profile with dynamic attributes.
    
    Parameters:
    details: Any arguments representing student details 
              (e.g., name, age, grade, hobbies).
    
    Example:
        profile = create_student_profile(name="Ada", age=20, grade="A", hobbies=["Reading", "Coding"])
        profile.name should return “Ada”
    """
    profile = details
    #print(profile[name])
    print(profile)

create_student_profile(name = "Ada", age = 20, grade = "A", hobbies = ["Reading", "Coding"])
