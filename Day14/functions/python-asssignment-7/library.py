"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.
"""

library = []

def add_book(**book):
    """Add a new book into the library with flexible details.
        return "Book {book_title} added successfully!"
    """
    library.append(book)
    print(library)
add_book(ID = (len(library) + 1), title = "Animal Farm", author = "George Owell", available = True)
def search_books(*search_param):
    """Search for books by multiple keywords (title, author).
    return books that match search description.
    """
    if search_param in library:

search_books("Animal Farm", "George Owell")
def borrow_book(book_id):
    """Borrow a book if available (msg: You borrowed {book_title}).
        else-> msg: Book {book_title} not available
    """
