print('''
        Welcome to dataMan 1.0
        Store your data with us
        NB: Wrong inputs terminate the program. The program is in beta phase with no validations for edge cases
        ''')
first_name = input("Enter your firstname: ")
last_name = input( "Enter your lastname: ")
height = float(input("Please enter your height: "))
age = int(input("Please enter your age: "))
marital_status = bool(input("Are you married? true/false: "))
hobbies = []
hobby1 = input("Input your first hobby: ")
hobby2 = input("Input your second hobby: ")
print("The datatype of", hobbies, "is ", type(hobbies))
print("The datatype of", height, "is ", type(height))
print("The datatype of", marital_status, "is ",type(marital_status))
hobbies.append(hobby1)
hobbies.append(hobby2)
print("Your name is {} {}, you are {}m tall and {} years old".format(first_name, last_name, height, age))
print("And your hobbies are ", hobbies)
