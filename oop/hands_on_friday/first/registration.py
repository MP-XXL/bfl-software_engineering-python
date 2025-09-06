class Registration:

    tuition = 50000

    def __init__(self, fname, lname, amount):
        self.first_name = fname
        self.last_name = lname
        self.amount_paid = amount

    def details(self):
        return f"""
        firstname = {self.first_name}
        lastname = {self.last_name}
        amount = {self.amount_paid}"""

    def check_balance(self):
        balance = self.tuition - self.amount_paid
        return f"{self.first_name}'s balance = {balance}"

    def balance_checker(self):
        return f"{self.check_balance()} remaining"



joy = Registration("Joy", "Tk", 20000)
tom = Registration("Tom", "Loner", 50000)
print(joy.details())
print(tom.details())
print(joy.check_balance())
print(tom.check_balance())
print(tom.balance_checker())
print(joy.balance_checker())

