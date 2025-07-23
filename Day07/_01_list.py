# A list is a collection of items. A list houses different elements of different data-type.

#using a constructor to define list
list_of_countries = list()
print(type(list_of_countries))

# Using the square bracket
states = []
print(type(states))

countries = ["Australia", "Malawi", "Russia", "Nigeria", "USA", "Iran"]
print(countries)

# Adding elements to a list
# Using index or replacing
favourite_fruits = ["Mango", "Apple", "Orang", "Kiwi", "Banana"]
print("Before adding")
print(favourite_fruits)
favourite_fruits[0] = "Coco-nut"
print("After updating")
print(favourite_fruits)

#Using Append
favourite_fruits = ["Mango", "Apple", "Orang", "Kiwi", "Banana"]
print("Before adding")
print(favourite_fruits)
favourite_fruits.append("Cranberry")
print("After updating")
print(favourite_fruits)

# Using Insert. Insert takes the index, element and sometimes step
favourite_fruits = ["Mango", "Apple", "Orang", "Kiwi", "Banana"]
print("Before adding")
print(favourite_fruits)
favourite_fruits.insert(3, "Strawberry")
print("After updating")
print(favourite_fruits)
