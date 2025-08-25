import json


with open("admin_db.json", "r") as file:
    admin = json.load(file)
    if "name" in admin:
        admin["name"] = "Marks Man!"
    admin["age"] = 700
with open("admin_db.json", "w") as file:
    json.dump(admin, file)
with open("admin_db.json", "r") as file:
    admin = json.load(file)
print(admin)
