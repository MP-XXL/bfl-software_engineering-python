#Data types
'''
str
int
bool
float
list [] - Not unique
dictionary {"Key":"Value"}
set {} - Unique
'''

#Below is a list data type
all_users = ["Tom", "John", "Mark", "Mimi", "Jade"]
print(all_users[2])
print(all_users)

#The curly braces denotes a dictionary in python. Dictionaries enable us hold more data about our users.
user1 = {"name" : "Tom"}
print(user1["name"])


all_users.append("Joy")

print(all_users)

#Using curly braces will make the list or database a set. And sets provide unique sets of data.
all_users = {"Tom", "John", "Mark", "Mimi", "Jade", "Tom"}
#Printing this will print only one "Tom" in the list
print(all_users)
