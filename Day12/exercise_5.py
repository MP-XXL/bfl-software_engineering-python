password = 1234
user_db = ["core", "tk", "mp"]
user_name = input("Enter user name: ")

if user_name in user_db:
    print("Account exists")
    confirmation = int(input("Enter Password: "))
    if confirmation == password:
        print("Password match")
    else:
        print("Password does not match")

else:
    print("Account not found!")

