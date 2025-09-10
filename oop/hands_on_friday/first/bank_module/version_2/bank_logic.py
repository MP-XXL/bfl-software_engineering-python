import random

class Bank:


    total_banks = []
    def __init__(self, name:str, bank_type:list, bank_branch:str = "Abuja"):
        self.name = name
        self.acc_type = bank_type
        self.all_accounts:list=None
        self.total_customers:int=None
        self.transactions:list=None
        self.branches:list[str] = [bank_branch.capitalize()]


class Accounts(Bank):


    def __init__(self, name:str, bank_type:list, acc_name:str, acc_type:str, acc_bal:float, bank_branch = "Jos"):
        Bank.__init__(self, name, bank_type, bank_branch)
        self.acc_name:str = acc_name
        self.acc_type:str = acc_type
        self.bank_branch = bank_branch
        self.acc_bal:float = None
        self.acc_num:int = random.randint(1000000000, 9000000000)
        #self.acc_bal:float = None
        self.txn_count:int = 0
        self.all_acc_txn:list  = []


mp = Accounts("Opay", "MFB", "MP", "Savings", 1000, )
print(mp.__dict__)
print(mp.acc_num)
