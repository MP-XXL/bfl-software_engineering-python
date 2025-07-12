#QUESTION 1
year_of_birth = int(input("Please enter your year of birth: "))
age = 2025 - year_of_birth

print("You are {} years old".format(age))


#QUESTION 2
account_balance = int(input("Enter yoyr acount balance: "))
#account_balance = 10000
account_balance = int(account_balance)
spend_amount = int(input("Please enter amount you want to spend : "))

print("Your remaining balance  is : ${:,.2f}".format(account_balance - spend_amount))

#QUESTION 3
message = "rPyoagrhmotn is cool!"
print(message[1:2] + message[2:3]+  message[-11:-10] + message[-14:-13]+ message[-3:-2] + message[-10:-9])
