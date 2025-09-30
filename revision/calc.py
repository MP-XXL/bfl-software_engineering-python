# V1
def calculate(*args):
    for x in args:
        print(x)
    print(args)


calculate(1+2-4*7)
"""expression = list(input("Enter expression : "))
def calculate(args):
    if "*" in args:
        ind = args.index("*")
        args[ind + 1] = int(args[ind + 1])
        var = args[ind + 1]
        print(type(var))
calculate(expression)"""

# V Mult
"""expression = list(input("Enter expression : "))
def calc(args):
    for num in args:
        if  num == "*":
            ind = args.index(num)
            mult = args[ind-1:ind+2]
            operand1, operator, operand2 = mult
            operand1 = int(operand1)
            operand2 = int(operand2)
            if operator == "*":
                result = operand1 * operand2
                print(result)


calc(expression)"""    

"""expression = list(input("Enter expression : "))
operand1, operator, operand2 = expression
operand1 = int(operand1)
operand2 = int(operand2)
def calc():
    if operator == "*":
        return operand1 * operand2
    elif operator == "+":
        return operand1 + operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "//":
        return operand1 // operand2
    elif operator == "%":
        return operand1 % operand2
    elif operator == "-":
        return operand1 - operand2
    else:
        return"invalid input"


print(calc())"""
