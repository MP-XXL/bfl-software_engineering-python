"""
TASK: Create a ShoppingCart class.

Requirements:
1. Store cart items in a dictionary (item → quantity).
2. Provide a method to add items.
3. Provide a method to remove items.
4. Provide a method to clear the cart.
5. Provide a method to calculate total price (with price list).

Example Usage:
    prices = {"Shirt": 5000, "Shoes": 12000}
    cart = ShoppingCart(prices)
    cart.add_item("Shirt", 2)
    print(cart.calculate_total())  # 10000
    cart.remove_item("Shirt", 1)
    print(cart.calculate_total())  # 5000
"""

class Shopping_cart:

    def __init__(self, **details):
        self.details = details


    def add_item(self, item, price, quantity):
        if item in self.details:
            return "Item already exists!"
        else:
            self.details[item] ={"price": price, "quantity": quantity}

    def remove_item(self, item):
        if item in self.details:
            del self.details[item]
        else:
            return "Item does not exists!"

    def clear_cart(self):
        self.details.clear()

    def total_item_price(self):
        total_price = 0
        for item in self.details:
            total_price += self.details[item]["price"] * self.details[item]["quantity"]
        return f"Total price of items in cart = {total_price :,.2f}"





cart = Shopping_cart(Shoes = {"price": 5000, "quantity": 45}, Shirts = {"price": 2000, "quantity": 3})
print(cart.details)
cart.add_item("Headphones", 200,  2)
print(cart.remove_item("Laptop"))
cart.clear_cart()
print(cart.total_item_price())
print(cart.details)
