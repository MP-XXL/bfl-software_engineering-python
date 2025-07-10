#decimal places
user_account_bal = 3331345

print(f"User account balance is : ${user_account_bal:.2f}")

#checking for a string in a string
bio = "My name is Tom"
print("Tom" in bio)
print(not "name" in bio)

#using the escape character
print("id|\t Name|\t Gender")
print("02|\t Bruce|\t male")
print("alert \a")

#Checking if a string begins with a particular character
print(bio.startswith("Jerry"))
#print(bio.endswith("Tom"))

is_married = input("").lower()
print(is_married.startswith("true"))

#converting a string list to a list type
fruits = "Apple Banna Kiwi Orange"
list_of_fruits = fruits.split(" ")
print(list_of_fruits[0])
print(list_of_fruits)

#Question 1
record = "james Abuja 150000.5 NG0921"
record_list = record.split(" ")
name = record_list[0].capitalize()
initials = record[0].capitalize()
salary = float(record_list[2])

print("Salary Slip")
print("----------------")
print(f"Name:\t\t{name}\nInitials:\t{initials}\nID:\t\t{record_list[3]}\nValid ID:\tYes\nMonthly Salary:\t${salary:,.2f}")

#Question 2
message = "GhostNet#X44CR#98.654#TRC8821"
print("ALERT REPORT")
print("---------------------------------")
print("Code Name:\t",message[:8])
print("Message Code:\t",message[9:14])
print("Last Name:\t",message[13])
print("Trace ID:\t",message[-7:])
print("Taceable:\tYES")
print("Severity Level:\t",message[-14:-9])
