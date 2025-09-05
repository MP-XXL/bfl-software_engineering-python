"""
TASK: Create a ContactBook class.

Requirements:
1. Store contacts in a dictionary (name → phone number).
2. Provide a method to add new contacts.
3. Provide a method to delete contacts.
4. Provide a method to search for a contact by name.
5. Provide a method to show all contacts.

Example Usage:
    book = ContactBook()
    book.add_contact("Alice", "08012345678")
    print(book.search_contact("Alice"))  # "08012345678"
"""
class Contact_book:
    
    def __init__(self, **contacts):
        self.contacts = contacts

    def add_contact(self, name, number):
        if contact.check_contact(name) == True:
            return "Contact already exists!"
        else:
            self.contacts[name] = number
            contact.display_contacts()

    def delete_contact(self, name):
        if contact.check_contact(name) == True:
            del self.contacts[name]
            contact.display_contacts()
        else:
            return "Contact does not exist!"

    def check_contact(self, name):
            if name in self.contacts:
                print(f"{name} found in the contacts book")
                return True
            else:
                return "Name not found in the contacts book"

    def display_contacts(self):
        for name, number in self.contacts.items():
            print(f"{name} = {number}")


contact = Contact_book(Shinra = "08112345678", Sakamoto = "0802345679", Kelo = "0912345689")
print(contact.contacts)
contact.add_contact("Choki", "09047575393")
print("----------------------")
contact.delete_contact("Kelo")
print("----------------------")
contact.check_contact("Shinra")
print("----------------------")
contact.display_contacts()
