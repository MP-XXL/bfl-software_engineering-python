'''
lucky = 33

while True:
    user = int(input("Enter lucky Number: "))
    if user == lucky:
        print("Correct")
        break
    else:
        print("Keep trying")
'''

user_data = []

print("---USER FORM---")
while True:
    name = input("Enter Your Name: ")
    if name == " " and len(name) >= 3:
        print("Name cannot be empty or less than three characters")
    else:
        print("\n---You Must be 18 years and above---")
        age = int(input("Enter your Age: "))
        if age >= 18:
            if age.isdigit():
                print("\n---Enter Your Gender Male Or Female")
                gender = input("Your Gender: ").lower()
                if gender == "m" or gender == "male" or gender == "f" or gender == "female":
                    user_bio = {
                            "name":name,
                            "age":age,
                            "gender":gender,
                            }
                    user_data.append(user_bio)
                    print("Registration Successful...")
                    print(user_data)
                else:
                    print("Invalid Input: Choose male or female")
            else:
                print("Enter a Valid Intiger")
        else:
            print("Sorry Come Back when you are old enough!")
