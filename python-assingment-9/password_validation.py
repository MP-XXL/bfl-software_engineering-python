# ===== TASK 1: Password Validator =====
# Create a custom WeakPasswordError exception
# The function should validate password strength and raise WeakPasswordError if:
# - Password is less than 8 characters
# - Password doesn't contain at least one digit
# If input is empty, raise ValueError with message "Error: password cannot be empty"
# Keep asking until a valid password is entered

print("=== Task 1: Password Validator ===")
print("Password must be at least 8 characters and contain at least one digit\n")

class WeakPasswordError(Exception):
    pass

def validate_password(prompt):
    #
    # Write your code here.
    # Define WeakPasswordError class
    # Validate password rules
    # Handle exceptions and keep prompting
    #
    validating = True
    while validating:
        try:
            user_input = input(prompt)
            if user_input == "":
                raise ValueError
            elif len(user_input) < 8 or user_input.isalnum() != True:
                raise WeakPasswordError
            else:
                return user_input
        except ValueError:
            print("Please enter valid input. Password can not be empty!")
        except WeakPasswordError:
            print("User password does not meet requirements!")
        except Exception:
            print("Oops! Something went wrong!")



password = validate_password("Enter your password: ")
print(f"Password accepted: {'*' * len(password)}")
print()
