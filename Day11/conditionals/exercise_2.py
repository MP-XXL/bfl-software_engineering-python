#Task 2: Smart Restaurant Discount System
"""
Task 2: Smart Restaurant Discount System

You are helping a restaurant in Jos implement an automated discount system for their weekend promo.

The rules are:

    1.Customers with a loyalty card get a 10% discount.

    2.If the customer's order amount is above 20,000 NGN:

        -Loyalty card holders get an additional 5% discount.

        -Non-loyalty card holders get a free soft drink instead.
    3.Students (verified with student ID) get an extra 5% discount on top of whatever they qualify for.
Customer data is stored in a dictionary like this:

customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

Write a nested if-else block that:

    Calculates the final discount or freebie for the customer.

Stores the result in a dictionary called order_summary.Prints out a summary for the cashier."""
   
customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

loyalty_card_discount_Percentage = 10
order_amount_discount_percentage = 5
student_ID_discount_percentage = 5

if customer["loyalty_card"] == True:
   loyalty_card_discount = customer["order_amount"] * (loyalty_card_discount_Percentage / 100)
   print(loyalty_card_discount)

if customer["order_amount"] > 20000:
    if customer["loyalty_card"] == True:
        order_amount_discount = customer["order_amount"] * (order_amount_discount_percentage / 100)
    else:
        print("Free Drink")
    print(order_amount_discount)
if customer["is_student"] == True:
    student_ID_discount = (student_ID_discount_percentage / 100) * customer["order_amount"]
else:
    student_ID_discount = 0
discount = loyalty_card_discount + order_amount_discount + student_ID_discount
print(discount)
order_summary = customer.copy()
order_summary.update({"discount": discount})
print("Order Summary = ", order_summary)

