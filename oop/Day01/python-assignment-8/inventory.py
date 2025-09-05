"""
TASK: Create an Inventory class.

Requirements:
1. Store items in a dictionary (item_name → quantity).
2. Provide a method to add items (with quantity).
3. Provide a method to remove items (only if available).
4. Provide a method to update stock levels.
5. Provide a method to display all inventory items.

Example Usage:
    treasure_store = Inventory()
    favour_store = Inventory()

    treasure_store.add_item("Apples", 50)
    treasure_store.add_item("Bananas", 30)
    treasure_store.remove_item("Apples", 10)
    print(treasure_store.show_inventory())  # {"Apples": 40, "Bananas": 30}

    favour_store.add_item("Milk", 50)
    favour_store.add_item("Garri", 30)
    favour_store.remove_item("Milk", 40)
    print(treasure_store.show_inventory())  # {"Milk": 10, "Garri": 30}
"""

class Inventory:

    def __init__(self, **items):
        self.items = items

    def add_item(self, quantity, name):
        if quantity > 0:
            self.items[name] = quantity
        else:
            return "Can not add zero items!"

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            return "Item does not exists!"


    def update_stock(self, name, quantity):
        if name not in self.items:
            return "Prouct not found! Try the add product option."
        else:
            while True:
                update_math = int(input("Enter \"1\" to add to stock or \"2\" to reduce from stock : "))
                if update_math == 1:
                    self.items[name] += quantity
                    print(f"Item updated successfully!")
                    break
                elif update_math == 2:
                    if quantity > self.items[name]:
                        print("Inputed quantity to reduce greater than available quantity. Please view total iventory for accurate stock value.")
                    else:
                        self.items[name] -= quantity
                        print(f"Item update successfully! {quantity} {self.items[name]} have been removed from stock!")
                        print("UPDATED INVENTORY")
                        break
                else:
                    print("Invalid command!")

    def display_inventory(self):
        for item, price in self.items.items():
            print(f"{item} == {price}")


        


shop_city_store = Inventory(Garri = 2000, Sugar = 200, Groundnuts = 300)
print(shop_city_store.items)
shop_city_store.add_item(400, "Beans")
shop_city_store.remove_item("Beans")
shop_city_store.update_stock("Sugar", 400)
shop_city_store.display_inventory()
