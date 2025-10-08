"""
FOUNDATIONS EVICTION TEST - MCQ SECTION
Instructions:
1. Complete all multiple choice questions below
2. Write your answers as variables (Q1_ANSWER, Q2_ANSWER, etc.)
3. Save the file
4. Run: python test_scorer.pyc to see your score
5. Minimum passing score: 70%

DO NOT MODIFY test_scorer.pyc
"""

# ===== SECTION 1: MULTIPLE CHOICE QUESTIONS =====
# Write your answers as variables below each question

"""
1. What is the output of this code?

# greetings = "Hello World"
print(greetings)

A) "Hello World"
B) greetings  
C) Hello World
D) NameError: name 'greetings' is not defined
"""
Q1_ANSWER = "C"  # Replace with your answer (A, B, C, or D)

"""
2. What is the second output?

def append_val(val, my_list=[]):
    my_list.append(val)
    return my_list

print(append_val(1))
print(append_val(2))

A. [2]
B. [1, 2]  
C. [1], [2]
D. Error
"""
Q2_ANSWER = "D"  # Replace with your answer

"""
3. What is the output?
def func(x, *args, **kwargs):
    return args, kwargs

print(func(1, 2, 3, name="Alice", age=25))

A. (2, 3), {'name': 'Alice', 'age': 25}
B. (1, 2, 3), {'name': 'Alice', 'age': 25}
C. ((2, 3), {'name': 'Alice', 'age': 25})
D. Error
"""
Q3_ANSWER = "A"  # Replace with your answer

"""
4. Which of these is invalid as a dictionary key?
A. "name"
B. 42
C. (1, 2)
D. [1, 2]
"""
Q4_ANSWER = "D"  # Replace with your answer

"""
5. What is the output?
nums = [10, 20, 30, 40, 50]
print(nums[1:4][::-1])

A. [20, 30, 40]
B. [40, 30, 20]
C. [10, 20, 30] 
D. [50, 40, 30]
"""
Q5_ANSWER = "B"  # Replace with your answer

"""
6. What happens?
a = [(1, 2), (3, 4)]
b = ([1, 2], [3, 4])
a[0][0] = 99
b[0][0] = 99

A. Both assignments succeed.
B. Both assignments fail.
C. First fails, second succeeds.
D. First succeeds, second fails.
"""
Q6_ANSWER = "B"  # Replace with your answer

"""
7. Modify a string through slicing and concatenation. Which new string is formed?
text = "Programming"
result = text[:4] + text[-4:]
print(result)

A) "Progming"
B) "Programming"
C) "Progammi"
D) "Progrming"
"""
Q7_ANSWER = "A"  # Replace with your answer

"""
8. Examine this bitwise operation. Which result will it produce?
num = 17
print(num & 1)

A) 0
B) 1
C) 17
D) 16
"""
Q8_ANSWER = "C"  # Replace with your answer

"""
9. Analyze the following code snippet. Which value will be displayed?
x = 5
y = 2.0
result = x / y
print(type(result))

A) <class 'int'>
B) <class 'float'>
C) <class 'double'>
D) <class 'number'>
"""
Q9_ANSWER = "B"  # Replace with your answer

"""
10. What does this code output?
x = 10 
def func(): 
    global x 
    x = 20 
func() 
print(x)

A) 10
B) 20
C) None
D) Error
"""
Q10_ANSWER = "B"  # Replace with your answer

"""
11. What will be the output of this code?
data = {'a': 1, 'b': 2, 'a': 3}
print(data['a'])

A) 1
B) 3
C) [1, 3]
D) Error: duplicate keys not allowed
"""
Q11_ANSWER = "A"  # Replace with your answer

"""
12. What is printed?
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(3))

A. 3
B. 6
C. 9
D. Error
"""
Q12_ANSWER = "B"  # Replace with your answer

"""
13. When you run this program, what is the output?
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Zero")
except Exception:
    print("General")

A) General
B) Zero
C) "General"
D) "Zero"
"""
Q13_ANSWER = "B"  # Replace with your answer

"""
14. Why is the finally block important when handling files/resources?
try:
    x = 1/0
except ZeroDivisionError:
    print("Handled")
finally:
    print("Cleanup")

A. It always runs, even if an exception occurs.
B. It runs only if there is no exception.
C. It prevents exceptions entirely.
D. It is optional and not recommended.
"""
Q14_ANSWER = "A"  # Replace with your answer

"""
15. What is the output for factorial(3)?
def factorial(n):
    return n * factorial(n-1)

A. No base case → infinite recursion.
B. Python forbids recursion.
C. n-1 invalid.
D. * not valid in recursion.
"""
Q15_ANSWER = "A"  # Replace with your answer

print("Test completed. Run 'python mcq_scorer.pyc' to see your score!")
