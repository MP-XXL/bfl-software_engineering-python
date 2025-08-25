#storing data in a json file
import json

admin = {
        "name": "MP",
        "admin": True,
        "age": 300
        }

with open("admin_db.json", "w") as file:
    json.dump(admin, file)
print("JSON data has been stored in , admin_db.json")

#Reading or retrieving data from a json file
with open("admin_db.json", "r") as file:
    admin = json.load(file)
print("Admin database = ", admin)

# Formatting the json output
admin = {"name": "MP","admin": True,"age": 300}

with open("admin_db_indented.json", "w") as file:
    json.dump(admin, file, indent=16)
print("JSON data has been idented in admin_db_indented")

