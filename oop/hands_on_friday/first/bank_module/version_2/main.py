import random
import time
from enum import Enum

class Bank:


    total_banks = []

    def __init__(self, bank_name:str, bank_type:str, bank_branch:str = "Abuja"):
        self.bank_name = bank_name
        self.bank_type = bank_type
        self.bank_branch = bank_branch
        self.all_accounts:list= []
        self.total_customers:int= 0
        self.transactions:list= []
        self.branches:list[str] = [bank_branch.capitalize()]

        if self.bank_name in Bank.total_banks:
            return "Bank account already exist"
        else:
            Bank.total_banks.append(self.bank_name)

opay = Bank("Opay", "MFB", "Jos")
first_bank = Bank("First Bank", "Commercial", "Kaduna")
stanbic_ibtc = Bank("Stanbic IBTC", "Commercial")
gtbank = Bank("GTBank", "Commericial")


class Account_Type(Enum):
    SAVINGS = 1
    CURRENT = 2

class Txn_Type(Enum):
    DEBIT = 1
    CREDIT = 2


class BankAccounts(Bank):

    obj = time.localtime()
    time_str = time.asctime(obj)

    promo_prize = 2000

    def __init__(self, bank, acc_name:str, acc_bal:float, acc_type = Account_Type(2).name, email = False, sms = False, promo = True, isAdmin = False, isFrozen = False):
        Bank.__init__(self, bank.bank_name, bank.bank_type, bank.branches[0])
        self.bank = bank
        self.acc_name:str = acc_name
        self.acc_type:str = acc_type
        self.acc_bal:float = acc_bal
        self.acc_num:int = random.randint(1000000000, 9000000000)
        self.txn_count:int = 0
        self.all_acc_txn = []
        self.email = email
        self.sms = sms
        self.promo = promo
        self.isAdmin = isAdmin
        self.isFrozen = isFrozen
    

        bank.total_customers += 1
        bank.transactions.append({bank.bank_name:self.all_acc_txn})
        user = f"""
        Account Name = {self.acc_name}
        Account Number = {self.acc_num}
        Account Type = {self.acc_type}
        Balance = {self.acc_bal:,.2f}
        Bank Name = {self.bank_name}
        """
        bank.all_accounts.append(user)



        if self.promo == True:
            self.acc_bal += self.promo_prize
        else:
            pass


    def show_account(self):
        return (f"""
        Account Name = {self.acc_name}
        Account Number = {self.acc_num}
        Account Type = {self.acc_type}
        Balance = {self.acc_bal:,.2f}
        Bank Name = {self.bank_name}
        Bank Branch = {self.bank_branch}
        Bank Type = {self.bank_type}
        Email = {self.email}
        SMS = {self.sms}
        Promo = {self.promo}
        isAdmin = {self.isAdmin}
        isFrozen = {self.isFrozen}
        """)




    def deposit(self, amount, transfer = None):
        if amount <= 0:
            return "Invalid amount entered!"
        else:
            if self.isFrozen == True:
                return "Account is frozen. Can not perform transaction!"
            else:
                self.acc_bal += amount
                self.all_acc_txn.append({"Deposit":amount})
                self.txn_count += 1
                if transfer == True:
                    self.email_Alert_CR(amount)
                    return
                else:
                    if self.sms == True:
                        self.sms_Alert_CR(amount)
                    if self.email == True:
                        self.email_Alert_CR(amount)

    def withdraw(self, amount, transfer = None):
        if self.acc_bal < amount:
            return "Insufficient funds!"
        elif self.acc_bal == 0:
            return "Invalid amount!"
        else:
            if self.isFrozen == True:
                return "Account is frozen. Can not perform transaction"
            else:
                self.acc_bal -= amount
                self.all_acc_txn.append({"Withdraw": amount})
                if transfer == True:
                    self.email_Alert_DR(amount)
                    self.txn_count += 1
                    return
                else:
                    if self.sms == True:
                        self.sms_Alert_DR(amount)
                    if self.email == True:
                        self.email_Alert_DR(amount)

    def transfer(self, receiver, amount):
        if self.isFrozen == True:
                return "Sending account is frozen. Can not perform transaction"
        else:
            if amount <= self.acc_bal and amount != 0:
                if receiver.isFrozen == True:
                    return "Destination account is frozen. Can not perform transaction"
                else:
                    self.withdraw(amount, transfer = True)
                    self.sms_TF_Alert_DR(amount, receiver)
                    receiver.deposit(amount, transfer = True)
                    self.txn_count += 1
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

    class Txn_Type(Enum):
        DEBIT = 1
        CREDIT = 2



    def sms_Alert_CR(self, amount):
        print(f"""
        SMS ALERT!!!
Acct: **{self.acc_num}
Amt: NGN{amount:,.2f} {Txn_Type(2).name}
Desc: - DEPOSIT FROM {self.acc_name}-{self.bank_name}-{self.acc_name}
Avail Bal: {self.acc_bal}
Date: {self.time_str}
""")


    def sms_Alert_DR(self, amount):
        print(f"""
        SMS ALERT!!!
Acct: **{self.acc_num}
Amt: NGN{amount:,.2f} {Txn_Type(1).name}
Desc: - WITHDRAWAL FROM {self.acc_name}-{self.bank_name}-{self.acc_name}
Avail Bal: {self.acc_bal}
Date: {self.time_str}
""")

    def sms_TF_Alert_CR(self, amount, receiver):
        print(f"""
        SMS ALERT!!!
Acct: **{self.acc_num}
Amt: NGN{amount:,.2f} {Txn_Type(2).name}
Desc: -TRANSFER FROM {self.acc_name}-{self.bank_name}-{receiver.acc_name}
Avail Bal: {receiver.acc_bal}
Date: {self.time_str}
""")


    def sms_TF_Alert_DR(self, amount, receiver):
        print(f"""
        SMS ALERT!!!
Acct: **{self.acc_num}
Amt: NGN{amount:,.2f} {Txn_Type(1).name}
Desc: -TRANSFER FROM {self.acc_name}-{self.bank_name}-{receiver.acc_name}
Avail Bal: {self.acc_bal}
Date: {self.time_str}
""")



    def email_Alert_CR(self, amount):
        print(f"""
        EMAIL ALERT!!!
Dear {self.acc_name},
{self.bank_name} Bank electronic Notification Service (WeNS)
We wish to inform you that a CREDIT transaction occurred on your account with us.

The details of this transaction are shown below:
Transaction Notification
Account Number : **{self.acc_num}
Transaction Location : 205
Description : WEB PUR 
Amount : NGN {amount:,.2f}
Value Date : {self.time_str}
Remarks : 539983*****2873
Time of Transaction : {self.time_str}
Document Number : {random.randint(1000000000, 90000000000)}

The balances on this account as at  {self.time_str}  are as follows;
Current Balance : NGN  {self.acc_bal}

The privacy and security of your Bank Account details is important to us. If you would prefer that we do not display your account balance in every transaction alert sent to you via email please dial *737*51*1#.

Thank you for choosing {self.bank_name} Bank Limited""")


    def email_Alert_DR(self, amount):
        print(f"""
        EMAIL ALERT!!!
Dear {self.acc_name},
{self.bank_name} Bank electronic Notification Service (WeNS)
We wish to inform you that a DEBIT transaction occurred on your account with us.

The details of this transaction are shown below:
Transaction Notification
Account Number : **{self.acc_num}
Transaction Location : 205
Description : WEB PUR 
Amount : NGN {amount:,.2f}
Value Date : {self.time_str}
Remarks : 539983*****2873
Time of Transaction : {self.time_str}
Document Number : {random.randint(1000000000, 90000000000)}

The balances on this account as at  {self.time_str}  are as follows;
Current Balance : NGN  {self.acc_bal}

The privacy and security of your Bank Account details is important to us. If you would prefer that we do not display your account balance in every transaction alert sent to you via email please dial *7037*51*1#.

Thank you for choosing {self.bank_name} Bank Limited""")





Aaron = BankAccounts(first_bank, "Aaron Black", 1000, sms=True)
Gina = BankAccounts(gtbank, "Gina Storm", 5000, sms=True)
MP = BankAccounts(opay, "MP", 0000, isAdmin=True)
Bruno = BankAccounts(stanbic_ibtc, "Bruno Fernandes", 0000, isFrozen = True)
Ola = BankAccounts(opay,"Oladade West", 25000, email = True, acc_type = Account_Type(1).name)


print(Aaron.show_account())
print(Gina.show_account())
print(MP.show_account())
print(Bruno.show_account())
print(Ola.show_account())
print("====================================")
print("After deposit and withdrawal")
print(Gina.deposit(10000))
print(Aaron.withdraw(1000))
print(Gina.show_account())
print(Aaron.show_account())
print("====================================")
print("After transfer")
Gina.transfer(Aaron, 5000)
print(Aaron.show_account())
print(Gina.show_account())
print("====================================")
MP.freeze_Acc(Gina)
MP.unfreeze_Acc(Gina)
print(Aaron.transfer(Bruno, 5000))
Aaron.transfer(Ola, 5000)


print(opay.__dict__)
print(opay.all_accounts)
