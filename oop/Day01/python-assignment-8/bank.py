"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance.
2. Provide a method to deposit money.
3. Provide a method to withdraw money (only if sufficient balance).
4. Provide a method to check current balance.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""

class Bank_account:

    history = []

    def __init__(self, **accounts):
        self.accounts = accounts

    def deposit(self, name, amount):
        if name in self.accounts:
            print(f"{name} found in the accounts")
            self.accounts[name] += amount
        else:
            return "Name not found in the accounts"

    def withdraw(self, name, amount):
        if name in self.accounts:
            print(f"{name} found in the accounts")
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
            else:
                return "Insuffiencient funds!"
        else:
            return "Name not found in the accounts"

    def check_balance(self, name):
        if name in self.accounts:
            print(f"{name} found in the accounts")
            return f" Your account balance = {self.accounts[name]}"
        else:
            return "Name not found in the accounts"

    def check_history(self, name):
        if name in self.accounts:
            Bank_account.history.append({name:account.withdraw([name])})
            print(Bank_account.history)
        #history.append()
 




account = Bank_account(Alice = 10400, Bobby = 38000, Mark = 150000)
print(account.accounts)
print(account.deposit("Abby", 31450))
account.withdraw("Mark", 6050)
print(account.check_balance("Mark"))
account.check_history("Mark")
print(account.accounts)
