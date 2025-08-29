store = {
        "Laptop":{"price": 1200, "quantity": 5},
        "Headphones": {"price": 150, "quantity": 10},
        "Mouse": {"price": 40, "quantity": 20}
        }
def program_start():
    while True:
        print("""
                1. Enter 1 to add to inventory
                2. Enter 2 to Update stock
                3. Enter 3 to sell product
                """)
        user_choice = input("Enter command : ")
        user_option(user_choice)

    

def user_option(user_choice):
    if user_choice == "1":
        product = input("Enter product name : ").capitalize()
        price = float(input("Enter price of product : "))
        quantity = int(input("Enter the quantity : "))
        add_product(store, product, price, quantity)
    elif user_choice == "2":
        product = input("Enter Product name : ").capitalize()
        quantity = int(input("Enter the quantity of the product : "))
        print(update_stock(store, product, quantity))
        #update_stock(store, product, quantity)
    elif user_choice == "3":
        product = input("Enter product name : ").capitalize()
        quantity = int(input("Enter quantity to sell : "))
        sell_product(store, product, quantity)

def add_product(store, name, price, quantity):
    for product in [store]:
        if name in store:
            return "Product already exists"
        else:
            store[name] = {"Price": price, "Quantity": quantity}
            print(store)

def update_stock(store, name, quantity):
    if name in store:
        math_update = input("Enter 1 to add to store or 2 to reduce from store : ")
        if math_update == "1":
            store[name]["quantity"] += quantity
        elif math_update == "2":
            store[name]["quantity"] -=  quantity
            print(store)
        else:
            print("Invalid command")
    else:
        return "Product not in store. Use the add option."

def sell_product(store, name, quantity):
    if name in store:
        print(name)
program_start()
