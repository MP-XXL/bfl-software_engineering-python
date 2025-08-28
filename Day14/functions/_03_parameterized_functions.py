#Librabry system
library = ["Python for Beginners", "Data Structures in C", "AI Basics"]
borrowed_books ={}
student_id = 1
def start():
    while True:
        print("""
        1. Display all books
        2. Add books
        3. Borrow book
        4. Return book
        5. Borrowed books
        6. Students that borrowed books
        7. Exit
        """)
        user_choice = int(input("Enter command : "))
        command_option(user_choice)
# Function to initiate user choice
def command_option(user_choice):
    if user_choice == 1:
        display_books()
    elif user_choice == 2:
        book_name = input("Enter the name of book to add : ")
        add_books(book_name)
    elif user_choice == 3:
        book_name = input("Enter the book name to borrow : ")
        borrow_books(book_name)


# Function to display books
def display_books():
    if len(library) != 0:
        for book in library:
            print(book)
    else:
        print("No books in the library!")

# Function to add books
def add_books(book_name):
    if book_name in library:
        print("Book already exists!")
    else:
        library.append(book_name)
        print(f"{book_name} added successfully!")

# Function to borrow books
def borrow_books(book_name):
    global student_id
    if book_name in library:
        library.remove(book_name)
        borrowed_books[student_id] = book_name
        student_id += 1
    else:
        print("Book not found in the library")

start()
