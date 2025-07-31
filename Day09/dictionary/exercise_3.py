contact_list = {
        "Yonko":777,
        "Yami":704,
        "Marvy": 9090,
        "Sol":7633,
        "Tosin":123,
        "K9ine":444}
print(contact_list)
print(contact_list["Tosin"])
print(contact_list.get("Tosin"))
# Updating items in dictionary
contact_list["K9ine"] = 6060
print(contact_list)
contact_list.update({"K9ine": 8080})
print(contact_list)

# Removing an item from a dictionary
del contact_list["Tosin"]
print(contact_list)
# .pop removes an item by specification
contact_list.pop("K9ine")
print(contact_list)
# Trying to delete a key that does not exist will throw a KeyError
print(contact_list.items(), type(contact_list.items()))

# .clear clears and returns an empty dictionary
# Removing the last item from a dictionary.
contact_list.popitem()
print(contact_list)

# .copy
new = contact_list #This only assigns the new variable to share the same location with contact_list
new.popitem()
print("Contact list after assinging", contact_list)
new2 = contact_list.copy() #This makes a copy of the dictionary and they do not share same memory location.
new2.popitem()
print("Contact list after poping new2 = ", contact_list)
print("Contact list for new2 = ", new2)
