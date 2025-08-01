items = ["apple", "soap", "biscuit"]
prices = [1000, 650, 270]
shopping = {
        items[0]:prices[0],
        items[1]:prices[1],
        items[2]:prices[2]
        }

print(shopping)

# 2
grades = [("Godiya", "A"), ("Tanko", "B"), ("Pankshak", "C"), ("Bella", "B")]

print(dict(grades))

gradings = {
        grades[0][0]:grades[0][1],
        grades[1][0]:grades[1][1],
        grades[2][0]:grades[2][1],
        grades[3][0]:grades[3][1]
        }
print(gradings)

# 3
cart = {"bread":1, "milk":2}
aaron = cart
isaac = cart
isaac["Sugar"] = 1
print(aaron)

# 4
new_cart = {}

timon = new_cart.copy()
moses = new_cart.copy()
nen = new_cart.copy()


nen.update({"Salada": 500})
nen.clear()
print(nen)
