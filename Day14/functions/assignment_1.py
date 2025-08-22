"""1. Write a function check_even_odd(n) that takes an integer n and returns:
"Even" if the number is even,
"Odd" if the number is odd.
"""
# V1
def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


check_even_odd(5)

# V2
user_input = int(input("Enter a number : "))
def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


check_even_odd(user_input)

"""
Write a function count_vowels(text, vowels="aeiou") that counts how many
vowels appear in a given text.
Example: count_vowels("Python is fun") should return 3.
"""
# V1
def count_vowels(text, vowels = "aeiou"):
    i = 0
    for vowel in vowels:
        if vowel in text:
            i += 1

    print(i)
count_vowels("python is fun")

"""3. Write a function count_even(numbers) that counts how many even numbers are
in a list.
Example: count_even([1, 2, 3, 4, 6]) → 3"""

def count_even(numbers):
    even_numbers = 0
    for number in numbers:
        if number % 2 == 0:
            even_numbers += 1
        else:
            continue
    print(even_numbers)


count_even([1, 2, 3, 4, 6, 8])

"""4. Write a function triangle_area(base, height) that calculates
the area of a triangle using the formula:
Area=1/2×base×height
Example: triangle_area(10, 5) → 25.0"""
def triangle_area(base, height):
    area = 0.5 * base * height
    print(area)


triangle_area(10, 5)

"""
Write a function called check_password_strength that takes a password string and returns "Weak", "Medium", or "Strong" based on these criteria: 
Weak (less than 6 characters), Medium (6-10 characters), Strong (more contains both letters and numbers)."""

"""def check_password_strength(password):
    letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for character in password:
        if character in letters or character in numbers:
            print("Strong!")
check_password_strength("7")
"""
