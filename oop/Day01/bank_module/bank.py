import random
import time


class BankAccount:

    obj = time.localtime()
    time_str = time.asctime(obj)

    promo_prize = 2000

    def __init__(self, account_name:str, account_number:int, balance:float, email = False, sms = False, promo = True, isAdmin = False, isFrozen = False):
        self.name = account_name
        self.number = account_number
        self.balance = balance
        self.email = email
        self.sms = sms
        self.promo = promo
        self.isAdmin = isAdmin
        self.isFrozen = isFrozen


        if self.promo == True:
            self.balance += self.promo_prize
        else:
            pass


    def add_account(self):
        return(f"""
        Account name = {self.name}
        Account Number = {self.number}
        balance = {self.balance:,.2f}
        email = {self.email}
        sms = {self.sms}
        Promo = {self.promo}
        isAdmin = {self.isAdmin}
        isFrozen = {self.isFrozen}
        """)


    def deposit(self, amount:float, transfer = None):
        if amount <= 0:
            return "Invalid amount entered!"
        else:
            if self.isFrozen == True:
                return "Account is frozen. Can not perform transaction!"
            else:
                self.balance += amount
                if transfer == True:
                    self.email_Alert_CR(amount)
                    return
                else:
                    if self.sms == True:
                        self.sms_Alert_CR(amount)
                    if self.email == True:
                        self.email_Alert_CR(amount)

    def withdraw(self, amount:float, transfer = None):
        if self.balance < amount:
            return "Insufficient funds!"
        elif self.balance == 0:
            return "Invalid amount!"
        else:
            if self.isFrozen == True:
                return "Account is frozen. Can not perform transaction"
            else:
                self.balance -= amount
                if transfer == True:
                    self.email_Alert_DR(amount)
                    return
                else:
                    if self.sms == True:
                        self.sms_Alert_DR(amount)
                        return "SUCCESS"
                    if self.email == True:
                        self.email_Alert_DR(amount)

    def transfer(self, receiver, amount:float):
        if self.isFrozen == True:
                return "Sending account is frozen. Can not perform transaction"
        else:
            if amount <= self.balance and amount != 0:
                if receiver.isFrozen == True:
                    return "Destination account is frozen. Can not perform transaction"
                else:
                    self.withdraw(amount, transfer = True)
                    self.sms_TF_Alert_DR(amount, receiver)
                    receiver.deposit(amount, transfer = True)
                    self.sms_TF_Alert_CR(amount, receiver)
            else:
                return "Insufficient funds!"

    def freeze_Acc(self, name):
        if self.isAdmin == False:
            return "Can not modify account. Must be admin!"
        else:
            name.isFrozen = True

    def unfreeze_Acc(self, name):
        if self.isAdmin == False:
            return "Can not modify account. Must be admin!"
        else:
            name.isFrozen = False



    def sms_Alert_CR(self, amount:float):
        print(f"""
        SMS ALERT!!!
Acct: **{self.number}
Amt: NGN{amount:,.2f} CREDIT
Desc: - DEPOSIT FROM {self.name}-OPAY-{self.name}
Avail Bal: {self.balance}
Date: {self.time_str}
""")


    def sms_Alert_DR(self, amount:float):
        print(f"""
        SMS ALERT!!!
Acct: **{self.number}
Amt: NGN{amount:,.2f} DEBIT
Desc: - WITHDRAWAL FROM {self.name}-OPAY-{self.name}
Avail Bal: {self.balance}
Date: {self.time_str}
""")

    def sms_TF_Alert_CR(self, amount, receiver):
        print(f"""
        SMS ALERT!!!
Acct: **{self.number}
Amt: NGN{amount:,.2f} CREDIT
Desc: -TRANSFER FROM {self.name}-OPAY-{receiver.name}
Avail Bal: {receiver.balance}
Date: {self.time_str}
""")


    def sms_TF_Alert_DR(self, amount, receiver):
        print(f"""
        SMS ALERT!!!
Acct: **{self.number}
Amt: NGN{amount:,.2f} DEBIT
Desc: -TRANSFER FROM {self.name}-OPAY-{receiver.name}
Avail Bal: {self.balance}
Date: {self.time_str}
""")



    def email_Alert_CR(self, amount):
        print(f"""
        EMAIL ALERT!!!
Dear {self.name},
Whatsoever Bank electronic Notification Service (WeNS)
We wish to inform you that a CREDIT transaction occurred on your account with us.

The details of this transaction are shown below:
Transaction Notification
Account Number : **{self.number}
Transaction Location : 205
Description : WEB PUR 
Amount : NGN {amount:,.2f}
Value Date : {self.time_str}
Remarks : 539983*****2873
Time of Transaction : {self.time_str}
Document Number : {random.randint(1000000000, 90000000000)}

The balances on this account as at  {self.time_str}  are as follows;
Current Balance : NGN  {self.balance}

The privacy and security of your Bank Account details is important to us. If you would prefer that we do not display your account balance in every transaction alert sent to you via email please dial *737*51*1#.

Thank you for choosing Whatsoever Bank Limited""")


    def email_Alert_DR(self, amount):
        print(f"""
        EMAIL ALERT!!!
Dear {self.name},
Whatsoever Bank electronic Notification Service (WeNS)
We wish to inform you that a DEBIT transaction occurred on your account with us.

The details of this transaction are shown below:
Transaction Notification
Account Number : **{self.number}
Transaction Location : 205
Description : WEB PUR 
Amount : NGN {amount:,.2f}
Value Date : {self.time_str}
Remarks : 539983*****2873
Time of Transaction : {self.time_str}
Document Number : {random.randint(1000000000, 90000000000)}

The balances on this account as at  {self.time_str}  are as follows;
Current Balance : NGN  {self.balance}

The privacy and security of your Bank Account details is important to us. If you would prefer that we do not display your account balance in every transaction alert sent to you via email please dial *7037*51*1#.

Thank you for choosing Whatsoever Trust Bank Limited""")

