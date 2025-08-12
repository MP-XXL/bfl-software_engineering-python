"""Online Store Orders"""

orders = [
    {"order_id": 101, "customer": "John", "items": 5, "total_price": 75},
    {"order_id": 102, "customer": "Mary", "items": 10, "total_price": 180},
    {"order_id": 103, "customer": "Alex", "items": 2, "total_price": 50},
    {"order_id": 104, "customer": "Grace", "items": 15, "total_price": 600},
    {"order_id": 105, "customer": "Paul", "items": 5, "total_price": 145}
]

"""Task:
1. Print the customer name and total_price for orders with 5 or more items.
2. Skip orders with total_price between 140 and 200.
3. If any total_price is greater than 500, stop the loop."""

for order in orders:
    if order["items"] >= 5 and order["total_price"] > 500:
        break
    if order ["items"] >= 5 and order["total_price"] >= 140 and order["total_price"] <= 200:
        continue
    if order["items"] >= 5:
        print(f"{order['customer']} : {order['total_price']}")

posts = [
        {"post": "Gernacho"},
        {"post": "Welcome"},
        {"post": "Nothing"}
        ]

for post in posts:
    if post["post"] == "Welcome":
        print(post["post"])
        break
else:
    print("Not found")
