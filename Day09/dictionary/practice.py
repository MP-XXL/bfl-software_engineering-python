# Dictionary
michael_west = {
        "bag" : "Capacity crap",
        "king" : "servant hoader",
        "cake" : "Kings meal",
        "pudding" : "for the poor"
        }
print(michael_west)
print(michael_west["cake"])

# Adding items to the dictionary
michael_west["garri"] = "student power"
michael_west["boat"] = "boat cruise"
michael_west["cars"] = "Auto-mobile"
print(michael_west)

print(michael_west.keys())
print(michael_west.values())
print(michael_west.items())

# Contact list
contacts = {
        "Luffy" : 800,
        "Cage" : 900,
        "Noob" : 700,
        "Luie" : None,
        "Steel" : 200,
        "Canary" : 400
        }
print(contacts)

# update contact list
contacts["Steel"] = 123
print(contacts)
# using update method
contacts.update({"Canary": 8392})
print(contacts)

# Removing an item
del contacts["Canary"]
print(contacts)

contacts.pop("Steel")
print(contacts)

contacts.popitem()
print(contacts)

# Copying
new_list = contacts # This does not copy but assigns to the new_list variable, same mememory location as contacts. Any change in one reflects in the other.
new_list.popitem()
print(contacts)
print("New list = ", new_list)

new_contacts = contacts.copy() # This makes a copy of the old dictionary and does not share same memory location
new_contacts.popitem()
print("New contacts list", new_contacts)
print(contacts)

bio_data = {
        "Name" : "Slim",
        "Married" : False,
        "Age" : 100,
        "Height" : 6.1,
        "Address" : {
            "City" : "Jos",
            "State" : "Plateau",
            },
        "Status" : None
        }
print(bio_data["Address"]["State"])


blockfuse_labs = [
        {"web3" : {
            "Clement" : 100, 
            "Racy" : 200, 
            "Charlse" : 300}
            },
        {"web2" : {
            "Nan" : 100, 
            "Lere" : 200, 
            "Wallex" : 300}}
        ]
print(blockfuse_labs[1]["web2"]["Wallex"])
blockfuse_labs[1]["web2"]["Wallex"] += 600
blockfuse_labs[1]["web2"].update({"Nan" : 500})
print(blockfuse_labs)

