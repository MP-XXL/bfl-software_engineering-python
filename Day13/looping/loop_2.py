names = ["Tom", "Jerry", "Mimi", "Val"]
user_name = input("Enter username : ")
flag = False
for name in names:
    if user_name == name:
        flag = True
        break
if flag == True:
    print("VIP")
else:
    print("REGULAR")


# Using for...else
user_name = input("Enter username : ")
for name in names:
    if user_name == name:
        print("VIP")
        break
else:
    print("REGULAR")

