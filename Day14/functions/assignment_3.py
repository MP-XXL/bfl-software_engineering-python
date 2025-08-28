# Online Store Inventory & Sales System
store = {
        "Laptop":{"price": 1200, "quantity": 5},
        "Headphones": {"price": 150, "quantity": 10},
        "Mouse": {"price": 40, "quantity": 20}
        }
def start():
    while True:
        option = int(input("""
                WELCOME TO THE IVENTORY

                1. Enter \"1\" to add product to iventory
                2. Enter \"2\" to update stock in inventory
                \n>>> : """))
        user_choice(option)

def user_choice(choice_option):
    if choice_option == 1:
        product = input("Enter product name to add to inventory: ").capitalize()
        price = int(input("Enter product price : "))
        quantity = int(input("Enter product quantity: "))
        add_product(store, product, price, quantity)
    elif choice_option == 2:
        product = input("Enter name of product to update: ").capitalize()
        new_quantity = int(input("Enter the quantity to add or reduce : "))
        update_stock(store, product, new_quantity)
# Adding a new product to the to inventory
def add_product(store, name, price, quantity):
    if name in store:
        print("Product already exists in the inventory. Use the update inventory option")
    else:
        store[name] = {"price": price, "quantity": quantity}
        print(f"Product added successfully! Product details = Name: {name}, Price: {store[name]['price']}, Quantity: {store[name]['quantity']}")
# Updating stock
def update_stock(store, name, quantity):
    if name not in store:
        print("Prouct not found! Try the add product option.")
    else:
        update_math = int(input("Enter \"1\" to add to stock or \"2\" to reduce from stock : "))
        if update_math == 1:
            store[name]["quantity"] += quantity
            print(f"Item updated successfully! {quantity} {store[name]} have been added to stock!")
        elif update_math == 2:
            store[name]["quantity"] -= quantity
            print(f"Item update successfully! {quantity} {store[name]} have been removed from stock!")
    print("UPDATED INVENTORY")
    for item in store:
        print(f"Name = {item}: Price:{store[item]['price']}, Quantity:{store[item]['quantity']}")
start()
