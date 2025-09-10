import bank
import random




Aaron = bank.BankAccount("Aaron Black", random.randint(1000000000, 9000000000), 1000, sms = True)
Gina = bank.BankAccount("Gina Storm", random.randint(1000000000, 9000000000), 5000, sms = True)
MP = bank.BankAccount("MP", random.randint(1000000000, 9000000000), 0000, None, isAdmin = True)
Bruno = bank.BankAccount("Bruno Fernandes", random.randint(1000000000, 90000000000), 0000, isFrozen = True)
Ola = bank.BankAccount("Oladade West", random.randint(1000000000, 9000000000), 25000, email = True)

print(Aaron.add_account())
print(Gina.add_account())
print(MP.add_account())
print(Bruno.add_account())
print(Ola.add_account())
print("====================================")
print("After deposit and withdrawal")
print(Gina.deposit(10000))
print(Aaron.withdraw(1000))
print(Gina.add_account())
print(Aaron.add_account())
print("====================================")
print("After transfer")
Gina.transfer(Aaron, 5000)
print(Aaron.add_account())
print(Gina.add_account())
print("====================================")
MP.freeze_Acc(Gina)
MP.unfreeze_Acc(Gina)
print(Aaron.transfer(Bruno, 5000))
print(Aaron.transfer(Ola, 5000))
