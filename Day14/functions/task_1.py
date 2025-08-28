# Number 1
fruits = ["apple", "banna", "cherry", "orange"]
numbers = [10, 20, 30, 40, 50]
names = ["Alice", "Bob", "Charlie"]
schools = []
def get_first_item(items):
    if len(items) == 0:
       pass 
    else:
        for item in items:
            return items[0]
    return items
first_item = get_first_item(schools)
print(first_item)

numbers = [4, 9, 2, 7, 5]
list_2 = [100, 250, 30, 400, 15]
list_3 = [-5, -10, -3, -8, -1 ]
def get_max(numbers):
    max_ = 0
    for number in numbers:
        if number > max_:
            max_ = number
    return max_
max_number = get_max(numbers)
print(max_number)
max_number = get_max(list_2)
print(max_number)
max_number = get_max(list_3)
print(max_number)

