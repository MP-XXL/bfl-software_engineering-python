"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance. (starting balance should not be zero or less than)
2. create a custom error to handle zero balance.
3. Provide a method to deposit money.
4. Provide a method to withdraw money (only if sufficient balance).
5. create a custom error to handle insufficient balance
6. Provide a method to check current balance.
7. provide a method for transfer from tosins account to daniella
8. create custom error to handle accounts that do not exists
9. Add proper error handling for invalid amounts, accounts and anything that might go wrong.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""

# Custom Errors - IMPLEMENT THESE
class InvalidBalanceError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class AccountDoesNotExistError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class InvalidAccountNameError(Exception):
    pass

class BankAccount:
    # Class variable to store all accounts
    accounts = {}
    
    def __init__(self, owner: str, initial_balance: float):
        """
        Initialize bank account.
        Raises InvalidBalanceError if initial_balance <= 0
        Raises InvalidAccountNameError if owner is not string or empty
        """
        # TODO: Implement this method
        self.owner = owner
        self.initial_balance = initial_balance
        try:
            if self.initial_balance <= 0:
                raise InvalidBalanceError
            if self.owner != str or self.owner == "":
                raise InvalidAccountNameError
        except InvalidBalanceError:
            print("Negative balance")
        except InvalidAccountNameError:
            print("Name is empty!")

user = BankAccount("MP", 23000)


    def deposit(self, amount: float) -> bool:
        """
        Deposit money into account.
        Returns True if successful.
        Raises InvalidAmountError if amount <= 0
        """
        # TODO: Implement this method
        try:
            if amount <= 0:
                raise InvalidAmountError
            else:
                self.initial_balance += amount
                return True
        except InvalidAmountError:
            print("Invalid amount")

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from account.
        Returns True if successful.
        Raises InsufficientBalanceError if not enough funds
        Raises InvalidAmountError if amount <= 0
        """
        # TODO: Implement this method
        try:
            if amount > self.initial_balance:
                raise InsufficientBalanceError
            elif amount <= 0:
                raise InvalidAmountError
            else:
                return True
        except InsufficientBalanceError:
            print("Insufficient funds!")
        except InvalidAmountError:
            print("Invalid amount!")
    
    def get_balance(self) -> float:
        """
        Return current balance.
        """
        # TODO: Implement this method
        print(self.initial_balance)
    
    def get_owner(self) -> str:
        """
        Return account owner name.
        """
        # TODO: Implement this method
        print(self.owner)
    
    @classmethod
    def transfer(cls, from_account: str, to_account: str, amount: float) -> bool:
        """
        Transfer money between accounts.
        Returns True if successful.
        Raises AccountDoesNotExistError if either account doesn't exist
        Raises InsufficientBalanceError if from_account has insufficient funds
        Raises InvalidAmountError if amount <= 0
        """
        # TODO: Implement this method
        try:
            if amount <= 0:
                raise InvalidAmountError
            elif amount > self.initial_balance:
                raise InsufficientBalanceError
    
    
    @classmethod
    def account_exists(cls, account_name: str) -> bool:
        """
        Check if account exists.
        Returns True if account exists, False otherwise.
        """
        # TODO: Implement this method
        if account_name in account:
            return True
    
    @classmethod
    def get_all_accounts(cls) -> dict:
        """
        Get all accounts.
        Returns dictionary of all accounts.
        """
        # TODO: Implement this method
        for owners in accounts:
            print(owners)


acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())  # 1300

