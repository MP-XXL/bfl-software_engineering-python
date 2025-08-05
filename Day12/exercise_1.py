"""
MOVIE TICKET DISCOUNT:
You are building a movie ticketing system.
Ask user to enter their age.
1. Persons 18 or older can buy a ticket.  Output: "Can buy ticket"
2. If the are 60 or older, they get "senior discount" Output: "Senior discount"
3. If they are 18 and 12yrs or older, they can buy teen ticket. Output: "Teen ticekt"
otherwise, they can buy "Kids ticket"
"""
age = int(input("Enter your age: "))

if age >= 18:
    print("Can buy ticket")
    if age >= 60:
        print("Senior discount")
elif age < 18 and age == 12:
    print("Teen Ticket")
else:
    print("Kids ticket")
