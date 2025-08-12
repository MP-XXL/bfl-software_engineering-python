letters = ["a", "b", "c", "d", "e", "f"]
for letter in letters:
    print(letter*10)

random = {
        "age": 2,
        "height": 6.9,
        "alias": "catfish"
        }
for x in random:
    print(random)

for i in random:
    if i == "height":
        print("Found!")

names = ["Kay", "Kaly", "Doape", "Luci", "Kemi"]
for name in names:
    print(name)

names = ["Kay", "Kaly", "Doape", "Luci", "Kemi"]
for i in range(len(names)):
   print(names[i],i)

names = ["Kay", "Kaly", "Doape", "Luci", "Kemi"]
user = input("Enter User name : ")
for name in names:
    if user in names:
        print(user)
        break
    else:
        print("User not found!")
        break
#Using for else:

names = ["Cage", "Johnny", "Walker", "Soulz", "Bailey"]
person = input("Enter your name: ")
for user in names:
    if user == person:
        print(f"{person} found!")
        break
else:
    print(f"{person} not found")

#########

numbers = [12, 1, 3, 40, 70, 145, 150, 170, 525, 80, 90]
for number in numbers:
    if number > 500:
        break
    if number > 150:
        continue
    if number % 5 == 0:
        print(number)

#Printing the list in reverse without using methods
count = len(numbers) - 1
for number in range(len(numbers)):
    print(numbers[count])
    count -= 1

#Printing the largest number
largest_number = numbers[2]
for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)

# Requesting and appending 3 students to a list
student_record = []
for student in range(3):
    name = input("Enter Name : ")
    age = int(input("Enter age : "))
    car = input("Enter car model : ")
    student = {
            "name": name,
            "age": age,
            "car": car
            }
    student_record.append(student)
print(student_record)

####
orders = [
    {"order_id": 101, "customer": "John", "items": 5, "total_price": 75},
    {"order_id": 102, "customer": "Mary", "items": 10, "total_price": 180},
    {"order_id": 103, "customer": "Alex", "items": 2, "total_price": 50},
    {"order_id": 104, "customer": "Grace", "items": 15, "total_price": 600},
    {"order_id": 105, "customer": "Paul", "items": 5, "total_price": 145}
]
for order in orders:
    if order["items"] >= 10 and order["total_price"] > 500:
        break
    if order["items"] >= 10 and order["total_price"]>= 50 and order["total_price"] <= 145:
        continue
    if order["items"] >= 10:
        print(f'{order["customer"]} : {order["total_price"]}')
