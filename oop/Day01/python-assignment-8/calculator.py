"""
TASK: Create a Calculator class.

Requirements:
1. The class should allow basic operations: add, subtract, multiply, divide.
2. Each operation should be a separate method.
3. Handle division by zero gracefully.
4. Allow both integers and floats.

Example Usage:
    calc = Calculator()
    print(calc.add(5, 3))        # 8
    print(calc.divide(10, 0))    # "Error: Division by zero"
"""
class Calculator:

    result = 0

    def __init__(self, *numbers): #works without the init method as well
        self.numbers = numbers

    def add(self, number1, number2):
        Calculator.result = number1 + number2
        return Calculator.result

    def sub(self, number1, number2):
        Calculator.result = number1 - number2
        return Calculator.result

    def mul(self, number1, number2):
        Calculator.result = number1 * number2
        return Calculator.result

    def div(self, number1, number2):
        if number1 == 0 or number2 == 0:
            return "Can not perform division by zero"
        else:
            Calculator.result = number1 / number2
        return float(Calculator.result)





calc = Calculator()
print(float(calc.add(2, 2)))
print(float(calc.sub(5, 2)))
print(float(calc.mul(4, 2)))
print(calc.div(2, 2))


