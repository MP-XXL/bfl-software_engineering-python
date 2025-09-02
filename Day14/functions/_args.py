def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(add_numbers(1, 2, 3, 4, 5, ))


def student_bio(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
student_bio(name = "leo", level = 100, age = 23)

def account(owner, *transactions, ** details):
    amount = 0
    for num in transactions:
        amount += num
        return{
                "owner": owner,
                "balance": amount,
                "details": details
                }
print(account("John", 200, -50, 100, account_type = "savings", branch = "Lagos"))


def register_event(event_name, *participants, ** details):
    return{
            "Event": event_name,
            "participanta": participants,
            "details": details}
print(register_event("Tech Conference", "Alice", "Bob", "Charlie", location = "Abuja", date = "10th sept", organizer = "Filibus" ))

def event(event_name, *participants, ** details):
    print("Event : ", event_name)
    print("participanta :", participants)
    print("details :", details)
event("Tech Conference", "Alice", "Bob", "Charlie", location = "Abuja", date = "10th sept", organizer = "Filibus" )

