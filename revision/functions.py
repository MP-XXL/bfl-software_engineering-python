z = 10

def return_global_variable():
    return z

def show_global_variable():
    print(return_global_variable())

show_global_variable()


def age_print(name):
    print(f"My name is {name} and I am", return_global_variable())

age_print("John")


def return_num1():
    return int(input("Enter first number : "))

def return_num2():
    return int(input("Enter second number : "))

def get_sum():
    total = return_num1() + return_num2()
    print(total)

get_sum()


