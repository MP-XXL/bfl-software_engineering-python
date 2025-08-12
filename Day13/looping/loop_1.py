# For loop
"""
variable initialization iterable
    <body></body>
"""
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
#for i in range (1, 100):
#    print(i)


user = {
        "name": "Kat",
        "class": "2",
        "Yello": "x"}
for key, value in user.items():
    print(key, value)

names = ["Tom", "Jerry", "Mimi", "Val", "John"]
for name in names:
    print(name)



names = ["Tom", "Jerry", "Mimi", "Val", "John"]
for i in names:
    print(i)

#Printing the items and index
names = ["Tom", "Jerry", "Mimi", "Val", "John"]
for i in names:
    print(name, i)

# Using step values and range
names = ["Tom", "Jerry", "Mimi", "Val", "John"]
for i in range(0, len(names), 2):
    print(i)


vip = ["Tom", "Jerry", "Mimi", "Val", "John"]
for name in vip:
    user = input("Enter your name : ").capitalize()
    if user in vip:
        print("VIP status!")
        break
    else:
        print("Regular")
        break

#Multipication table    
for i in range(100):
    print(f"{i}x{i} =", i*i)
   

for i in range(5):
    for j in range(5):
        print(f"{i}x{j} = ", i * j)

#Fizz Buzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz!")
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buzz!")
    else:
        print(i)
