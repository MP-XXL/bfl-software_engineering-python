response = {"success":True, "message":"Welcome!", "data":[{"email":"testmail.x.com", "username":"MP"}]}
print(response["data"], response["success"])
print(response)

import pprint;
oxford = {
        "apple": "a common fruit",
        "ball": "a round object",
        "cat": "an animal of the family Felidae",
        "dog": "nanwans dog meat",
        "egg": "a spherical object",
        "fish": "a cold blooded animal",
        "goat": "Rivaldo",
        "house": "a buikding",
        "idiot": "wild animal",
        "jackal": "wild animal"
        }

pprint.pprint(oxford)
print("Meaning of ball = " + oxford["ball"])

#Adding data to dictionary
oxford["kettle"] = "A vessel for boiling"
print(oxford.keys())
print(oxford.values(), "\n", type(oxford.values()))

