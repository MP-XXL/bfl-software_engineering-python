"""
TASK: Create a RestaurantOrder class.

Requirements:
1. Store orders in a dictionary (item → quantity).
2. Provide a method to add items to the order.
3. Provide a method to remove items from the order.
4. Provide a method to calculate the total bill (use a price list dictionary).
5. Provide a method to show the current order.

Example Usage:
    prices = {"Pizza": 2000, "Burger": 1500, "Drink": 500}
    order = RestaurantOrder(prices)
    order.add_item("Pizza", 2)
    order.add_item("Drink", 3)
    print(order.calculate_total())  # 5500
"""

class Restaurant_order:

    def __init__(self, **items):
        self.items = items

    def add_items(self, item, price, quantity):
        if item in self.items:
            return "Item already exists!"
        else:
            self.items[item] ={"price": price, "quantity": quantity}

    def display_current_order(self):
        print(f" Current order = {self.items}")

    def remove_item(self, item):
        if item in self.items:
            print(f"{item} has been removed from your order")
            del self.items[item]
        else:
            return "Item does not exists!"

    def calculate_bill(self):
        total_bill = 0
        for item in self.items:
            total_bill += self.items[item]["price"] * self.items[item]["quantity"]
        return f"Total bill of items in on order = {total_bill :,.2f}"



order = Restaurant_order(Burger = {"price": 350, "quantity": 2}, Milkshake = {"price":1000, "quantity": 1}, Chips = {"price": 500, "quantity": 1})
print(order.items)
order.add_items("Chicken", 1200, 1)
order.remove_item("Burger")
print(order.calculate_bill())
order.display_current_order()
