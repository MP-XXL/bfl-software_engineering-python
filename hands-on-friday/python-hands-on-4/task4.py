"""
Task 4: Tech Conference Registration
The Jos Tech Conference registered participants under ticket categories:

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

During the first day:
- A "Guest" participant named "Daisy" joined.
- The "Student" participant canceled their registration.
- The organizers created a record for the day before removing the most recently added participant from the live system.
"""
# Adding Guest Daisy
participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}
participants.update({"Guest":"Daisy"})
print(participants)

# Student canceling
participants.pop("Student")
print(participants)

# Creating record
participants_snapshot = participants.copy()
print("Record before removing last added participant = ", participants_snapshot)
print(participants_snapshot)

participants.popitem()
print(participants)
