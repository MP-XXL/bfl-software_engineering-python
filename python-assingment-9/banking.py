# ===== TASK 4: Bank Account Withdrawal System =====
# Create TWO custom exceptions:
# - InsufficientFundsError: raised when withdrawal amount exceeds balance
# - InvalidTransactionError: raised when amount is negative or zero
# 
# The function should:
# - Accept prompt, current balance, and minimum balance (for overdraft protection)
# - Validate withdrawal amount is a valid number (raise ValueError if not)
# - Check if amount is positive (raise InvalidTransactionError if not)
# - Check if withdrawal would bring balance below minimum (raise InsufficientFundsError if so)
# - Return the withdrawal amount if valid
# - Keep asking until valid input

print("=== Task 1: Bank Account Withdrawal System ===")
print("Current Balance: $1000.00")
print("Minimum Balance: $100.00\n")

class InsufficientFundsError(Exception):
    pass

class InvalidTransactionError(Exception):

    def __init__(self, message):
        Exception.__init__(self, error_message)
        self.error_message = error_message

#error_message = InvalidTransactionError("Amounted by user is invalid!")
#print(error_message.message)
def process_withdrawal(prompt, balance, min_balance):
    #
    # Write your code here.
    # Define InsufficientFundsError class
    # Define InvalidTransactionError class
    # Validate withdrawal rules
    # Handle all exceptions with appropriate messages
    #
    withdraw = True
    while withdraw:
        try:
            user_input = float(input(prompt))
            if user_input > balance:
                raise InsufficientFundsError
            elif user_input <= 0:
                raise InvalidTransactionError("")#remember to parse errorif we are not using try-except block 
            else:
                return user_input
        except ValueError:
            print("Withdrawal amount must be a valid number!")
        except InsufficientFundsError:
            print("Amount entered by user exceeds current balance!")
        except InvalidTransactionError:
            print("Amounted by user is invalid!")
        except Exception:
            print("Oops! Something went wrong!")


amount = process_withdrawal("Enter withdrawal amount: $", 1000.00, 100.00)
print(f"Withdrawal successful: ${amount}")
print(f"New balance: ${1000.00 - float(amount)}")
print()

