"""
TASK: Create a Library class.

Requirements:
1. The class should track available books (list).
2. Provide a method to add new books to the library.
3. Provide a method for users to borrow books.
   - Remove the borrowed book from available list.
   - Store borrowed books with user info.
4. Provide a method for returning borrowed books.
5. Provide a method to show all available books.

Example Usage:
    lib = Library()
    lib.add_book("Python 101")
    lib.add_book("Data Science Handbook")
    lib.borrow_book("Alice", "Python 101")
    print(lib.show_available_books())  # ["Data Science Handbook"]
    lib.return_book("Alice")
    print(lib.show_available_books())  # ["Data Science Handbook", "Python 101"]
"""

class Library:

    def __init__(self, available, **borrowed):
        self.available = available
        self.borrowed = borrowed


    def add_book(self, book):
        if book in self.available:
            return f"{book} already exists in the library"
        else:
            self.available.append(book)

    def borrow_book(self, book, user):
        if book in self.available:
            self.available.remove(book)
            if user in self.borrowed:
                self.borrowed[user].append(book)
            else:
                self.borrowed.append({user:[book]})
        else:
            return "Book not found in the Library!"
        print(self.borrowed)


    def return_book(self, book, user):
        if user in self.borrowed:
            if book in self.borrowed[user]:
                self.borrowed[user].remove(book)
                self.available.append(book)
            else:
                return "Book not found in brrowed section"
        else:
            return "User not found in the borrowed section"
        print(self.borrowed)



    def display_available_books(self):
        print(f" Available books = {self.available}")


lib = Library(["Python 101", "DSA", "Data Science Handbook"], Alice = ["Gravity"])
print(lib.available, lib.borrowed)
lib.add_book("Animal Farm")
lib.borrow_book("Python 101", "Alice")
lib.return_book("Python 101", "Alice")
lib.display_available_books()
